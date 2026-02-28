import React from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity } from 'react-native';
import { colors } from '../theme/colors';

export default function ReportScreen({
  result,
  onBack,
}: {
  result: string;
  onBack: () => void;
}) {
  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>Analiz Raporu</Text>
        <TouchableOpacity onPress={onBack} style={styles.backBtn}>
          <Text style={styles.backBtnText}>← Kapat</Text>
        </TouchableOpacity>
      </View>
      <ScrollView
        style={styles.scroll}
        contentContainerStyle={styles.scrollContent}
        showsVerticalScrollIndicator={true}
      >
        <Text style={styles.body}>{result}</Text>
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: colors.navy[900] },
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
  title: { fontSize: 18, fontWeight: '700', color: colors.white },
  backBtn: { paddingVertical: 8, paddingHorizontal: 4 },
  backBtnText: { color: colors.primary[400], fontSize: 16 },
  scroll: { flex: 1 },
  scrollContent: { padding: 20, paddingBottom: 40 },
  body: {
    fontSize: 16,
    lineHeight: 26,
    color: colors.navy[100],
  },
});
