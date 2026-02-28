import React, { useCallback, useEffect, useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  FlatList,
  TouchableOpacity,
  ActivityIndicator,
  Alert,
  RefreshControl,
} from 'react-native';
import { getHistory, getAnalysisDetail } from '../api/analyze';
import type { HistoryItem } from '../api/analyze';
import { colors } from '../theme/colors';

export default function HistoryScreen({
  onOpenReport,
  onBack,
}: {
  onOpenReport: (text: string) => void;
  onBack: () => void;
}) {
  const [items, setItems] = useState<HistoryItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);

  const load = useCallback(async () => {
    const res = await getHistory();
    setItems(res.data ?? []);
    setLoading(false);
    setRefreshing(false);
    if (res.error && res.status === 401) return;
    if (res.error) Alert.alert('Hata', res.error);
  }, []);

  useEffect(() => {
    load();
  }, [load]);

  const onRefresh = () => {
    setRefreshing(true);
    load();
  };

  const openItem = async (id: number) => {
    const res = await getAnalysisDetail(id);
    if (res.data) onOpenReport(res.data.result_text);
    else if (res.error) Alert.alert('Hata', res.error);
  };

  const renderItem = ({ item }: { item: HistoryItem }) => (
    <TouchableOpacity
      style={styles.item}
      onPress={() => openItem(item.id)}
      activeOpacity={0.7}
    >
      <Text style={styles.itemPreview} numberOfLines={2}>
        {item.result_preview || item.input_preview}
      </Text>
      <Text style={styles.itemMeta}>
        {item.source} • {formatDate(item.created_at)}
      </Text>
    </TouchableOpacity>
  );

  if (loading) {
    return (
      <View style={styles.centered}>
        <ActivityIndicator size="large" color={colors.primary[500]} />
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>Geçmiş</Text>
        <TouchableOpacity onPress={onBack}>
          <Text style={styles.backText}>← Geri</Text>
        </TouchableOpacity>
      </View>
      <FlatList
        data={items}
        keyExtractor={(i) => String(i.id)}
        renderItem={renderItem}
        contentContainerStyle={items.length === 0 ? styles.emptyList : styles.list}
        ListEmptyComponent={
          <Text style={styles.emptyText}>Henüz analiz yok. İlk analizinizi yapın.</Text>
        }
        refreshControl={
          <RefreshControl refreshing={refreshing} onRefresh={onRefresh} tintColor={colors.primary[500]} />
        }
      />
    </View>
  );
}

function formatDate(s: string) {
  try {
    const d = new Date(s);
    return d.toLocaleDateString('tr-TR', { day: 'numeric', month: 'short', year: 'numeric' });
  } catch {
    return s;
  }
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: colors.navy[900] },
  centered: { flex: 1, justifyContent: 'center', alignItems: 'center', backgroundColor: colors.navy[900] },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: 20,
    paddingTop: 16,
    paddingBottom: 12,
    borderBottomWidth: 1,
    borderBottomColor: colors.accent[700],
  },
  title: { fontSize: 20, fontWeight: '700', color: colors.white },
  backText: { color: colors.primary[400], fontSize: 16 },
  list: { padding: 16, paddingBottom: 40 },
  emptyList: { flex: 1, justifyContent: 'center', padding: 24 },
  emptyText: { fontSize: 16, color: colors.navy[200], textAlign: 'center' },
  item: {
    backgroundColor: colors.accent[800],
    borderRadius: 12,
    padding: 16,
    marginBottom: 12,
    borderLeftWidth: 4,
    borderLeftColor: colors.primary[600],
  },
  itemPreview: { fontSize: 15, color: colors.white, marginBottom: 4 },
  itemMeta: { fontSize: 12, color: colors.navy[200] },
});
