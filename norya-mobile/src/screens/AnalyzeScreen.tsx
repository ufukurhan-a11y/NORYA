import React, { useState } from 'react';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  StyleSheet,
  ScrollView,
  ActivityIndicator,
  Alert,
  KeyboardAvoidingView,
  Platform,
} from 'react-native';
import { useNavigation } from '@react-navigation/native';
import * as ImagePicker from 'expo-image-picker';
import { analyzeText, analyzeUpload } from '../api/analyze';
import { colors } from '../theme/colors';

export default function AnalyzeScreen({ onResult }: { onResult: (text: string, analizId: number | null) => void }) {
  const navigation = useNavigation();
  const [text, setText] = useState('');
  const [loading, setLoading] = useState(false);

  const runAnalyze = async (payload: { text: string } | { uri: string; filename: string }) => {
    setLoading(true);
    let res: { data?: { sonuc: string; analiz_id?: number | null }; error?: string };
    if ('uri' in payload) {
      res = await analyzeUpload(payload.uri, payload.filename, 'tr');
    } else {
      res = await analyzeText({ text: payload.text, lang: 'tr' });
    }
    setLoading(false);
    if (res.error) {
      const msg = res.error.length > 200 ? `${res.error.slice(0, 200)}…` : res.error;
      Alert.alert('Analiz hatası', msg);
      return;
    }
    if (res.data) onResult(res.data.sonuc, res.data.analiz_id ?? null);
  };

  const pickImage = async () => {
    const { status } = await ImagePicker.requestMediaLibraryPermissionsAsync();
    if (status !== 'granted') {
      Alert.alert('İzin gerekli', 'Galeri erişimi için izin verin.');
      return;
    }
    const result = await ImagePicker.launchImageLibraryAsync({
      mediaTypes: ['images'],
      quality: 0.9,
      base64: false,
    });
    if (result.canceled || !result.assets?.[0]?.uri) return;
    runAnalyze({ uri: result.assets[0].uri, filename: 'photo.jpg' });
  };

  const takePhoto = async () => {
    const { status } = await ImagePicker.requestCameraPermissionsAsync();
    if (status !== 'granted') {
      Alert.alert('İzin gerekli', 'Kamera erişimi için izin verin.');
      return;
    }
    const result = await ImagePicker.launchCameraAsync({
      quality: 0.9,
      base64: false,
    });
    if (result.canceled || !result.assets?.[0]?.uri) return;
    runAnalyze({ uri: result.assets[0].uri, filename: 'camera.jpg' });
  };

  const submitText = () => {
    const t = text.trim();
    if (!t) {
      Alert.alert('Metin girin', 'Tahlil metnini yapıştırın veya fotoğraf yükleyin.');
      return;
    }
    runAnalyze({ text: t });
  };

  return (
    <KeyboardAvoidingView
      behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
      style={styles.container}
    >
      <TouchableOpacity style={styles.backBtn} onPress={() => navigation.goBack()}>
        <Text style={styles.backBtnText}>← Geri</Text>
      </TouchableOpacity>
      <ScrollView contentContainerStyle={styles.scroll} keyboardShouldPersistTaps="handled">
        <Text style={styles.title}>Tahlil analizi</Text>
        <Text style={styles.subtitle}>Metni yapıştırın veya fotoğraf/PDF seçin</Text>

        <TextInput
          style={styles.textArea}
          placeholder="Tahlil sonuç metnini buraya yapıştırın..."
          placeholderTextColor={colors.accent[700]}
          value={text}
          onChangeText={setText}
          multiline
          numberOfLines={8}
          editable={!loading}
        />

        <TouchableOpacity
          style={[styles.button, loading && styles.buttonDisabled]}
          onPress={submitText}
          disabled={loading}
        >
          {loading ? (
            <ActivityIndicator color="#fff" />
          ) : (
            <Text style={styles.buttonText}>Metni analiz et</Text>
          )}
        </TouchableOpacity>

        <View style={styles.divider}>
          <View style={styles.dividerLine} />
          <Text style={styles.dividerText}>veya</Text>
          <View style={styles.dividerLine} />
        </View>

        <TouchableOpacity
          style={styles.outlineButton}
          onPress={pickImage}
          disabled={loading}
        >
          <Text style={styles.outlineButtonText}>Galeriden fotoğraf seç</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={styles.outlineButton}
          onPress={takePhoto}
          disabled={loading}
        >
          <Text style={styles.outlineButtonText}>Kamera ile çek</Text>
        </TouchableOpacity>
      </ScrollView>
    </KeyboardAvoidingView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: colors.navy[900] },
  backBtn: { paddingHorizontal: 20, paddingTop: 16, paddingBottom: 8 },
  backBtnText: { color: colors.primary[400], fontSize: 16 },
  scroll: { padding: 24, paddingBottom: 48 },
  title: { fontSize: 22, fontWeight: '700', color: colors.white, marginBottom: 4 },
  subtitle: { fontSize: 14, color: colors.navy[200], marginBottom: 20 },
  textArea: {
    borderWidth: 1,
    borderColor: colors.accent[700],
    borderRadius: 12,
    padding: 16,
    fontSize: 16,
    minHeight: 140,
    textAlignVertical: 'top',
    backgroundColor: colors.accent[800],
    color: colors.white,
    marginBottom: 16,
  },
  button: {
    backgroundColor: colors.primary[600],
    borderRadius: 12,
    paddingVertical: 16,
    alignItems: 'center',
    marginBottom: 24,
  },
  buttonDisabled: { opacity: 0.7 },
  buttonText: { color: colors.white, fontSize: 16, fontWeight: '600' },
  divider: { flexDirection: 'row', alignItems: 'center', marginBottom: 20 },
  dividerLine: { flex: 1, height: 1, backgroundColor: colors.accent[700] },
  dividerText: { marginHorizontal: 12, color: colors.navy[200], fontSize: 14 },
  outlineButton: {
    borderWidth: 2,
    borderColor: colors.primary[500],
    borderRadius: 12,
    paddingVertical: 16,
    alignItems: 'center',
    marginBottom: 12,
  },
  outlineButtonText: { color: colors.primary[300], fontSize: 16, fontWeight: '600' },
});
