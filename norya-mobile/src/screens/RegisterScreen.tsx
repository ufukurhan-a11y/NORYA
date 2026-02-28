import React, { useState } from 'react';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  StyleSheet,
  KeyboardAvoidingView,
  Platform,
  ScrollView,
  Alert,
} from 'react-native';
import { useAuth } from '../context/AuthContext';
import { colors } from '../theme/colors';

const COUNTRIES = [
  { code: 'TR', label: 'Türkiye' },
  { code: 'DE', label: 'Almanya' },
  { code: 'US', label: 'ABD' },
  { code: 'GB', label: 'İngiltere' },
  { code: 'NL', label: 'Hollanda' },
  { code: 'AT', label: 'Avusturya' },
  { code: 'CH', label: 'İsviçre' },
  { code: 'FR', label: 'Fransa' },
  { code: 'IL', label: 'İsrail' },
  { code: 'SA', label: 'Suudi Arabistan' },
  { code: 'IN', label: 'Hindistan' },
  { code: 'ES', label: 'İspanya' },
  { code: 'IT', label: 'İtalya' },
  { code: 'GR', label: 'Yunanistan' },
  { code: 'OTHER', label: 'Diğer' },
];

export default function RegisterScreen({ onBack }: { onBack: () => void }) {
  const { register } = useAuth();
  const [fullName, setFullName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [phone, setPhone] = useState('+90');
  const [country, setCountry] = useState('TR');
  const [loading, setLoading] = useState(false);

  const handleRegister = async () => {
    if (!fullName.trim()) {
      Alert.alert('Hata', 'Ad soyad girin.');
      return;
    }
    if (!email.trim()) {
      Alert.alert('Hata', 'E-posta girin.');
      return;
    }
    if (!password || password.length < 6) {
      Alert.alert('Hata', 'Şifre en az 6 karakter olmalı.');
      return;
    }
    if (!phone || phone.length < 8) {
      Alert.alert('Hata', 'Geçerli telefon numarası girin (ülke kodu ile, örn. +905551234567).');
      return;
    }
    const code = country === 'OTHER' ? 'TR' : country;
    setLoading(true);
    const { error } = await register({
      full_name: fullName.trim(),
      email: email.trim(),
      password,
      phone: phone.trim(),
      country: code,
    });
    setLoading(false);
    if (error) Alert.alert('Kayıt', error);
    else onBack();
  };

  return (
    <KeyboardAvoidingView
      behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
      style={styles.container}
    >
      <ScrollView contentContainerStyle={styles.scroll} keyboardShouldPersistTaps="handled">
        <View style={styles.card}>
          <Text style={styles.title}>Ücretsiz Kayıt</Text>
          <Text style={styles.subtitle}>İlk analiz ücretsiz</Text>
          <TextInput
            style={styles.input}
            placeholder="Ad Soyad"
            placeholderTextColor={colors.accent[700]}
            value={fullName}
            onChangeText={setFullName}
            editable={!loading}
          />
          <TextInput
            style={styles.input}
            placeholder="E-posta"
            placeholderTextColor={colors.accent[700]}
            value={email}
            onChangeText={setEmail}
            autoCapitalize="none"
            keyboardType="email-address"
            editable={!loading}
          />
          <TextInput
            style={styles.input}
            placeholder="Şifre (en az 6 karakter)"
            placeholderTextColor={colors.accent[700]}
            value={password}
            onChangeText={setPassword}
            secureTextEntry
            editable={!loading}
          />
          <TextInput
            style={styles.input}
            placeholder="Telefon (+905551234567)"
            placeholderTextColor={colors.accent[700]}
            value={phone}
            onChangeText={setPhone}
            keyboardType="phone-pad"
            editable={!loading}
          />
          <Text style={styles.label}>Ülke</Text>
          <View style={styles.countryRow}>
            {COUNTRIES.slice(0, 6).map((c) => (
              <TouchableOpacity
                key={c.code}
                style={[styles.countryBtn, country === c.code && styles.countryBtnActive]}
                onPress={() => setCountry(c.code)}
                disabled={loading}
              >
                <Text style={[styles.countryBtnText, country === c.code && styles.countryBtnTextActive]}>
                  {c.code}
                </Text>
              </TouchableOpacity>
            ))}
          </View>
          <View style={styles.countryRow}>
            {COUNTRIES.slice(6, 12).map((c) => (
              <TouchableOpacity
                key={c.code}
                style={[styles.countryBtn, country === c.code && styles.countryBtnActive]}
                onPress={() => setCountry(c.code)}
                disabled={loading}
              >
                <Text style={[styles.countryBtnText, country === c.code && styles.countryBtnTextActive]}>
                  {c.code}
                </Text>
              </TouchableOpacity>
            ))}
          </View>
          <TouchableOpacity
            style={[styles.button, loading && styles.buttonDisabled]}
            onPress={handleRegister}
            disabled={loading}
          >
            <Text style={styles.buttonText}>Kayıt Ol</Text>
          </TouchableOpacity>
          <TouchableOpacity onPress={onBack} disabled={loading}>
            <Text style={styles.link}>Zaten hesabım var, giriş yap</Text>
          </TouchableOpacity>
        </View>
      </ScrollView>
    </KeyboardAvoidingView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: colors.navy[900] },
  scroll: { padding: 24, paddingBottom: 48 },
  card: {
    backgroundColor: colors.accent[50],
    borderRadius: 16,
    padding: 24,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.1,
    shadowRadius: 12,
    elevation: 4,
  },
  title: { fontSize: 22, fontWeight: '700', color: colors.navy[900], marginBottom: 4 },
  subtitle: { fontSize: 14, color: colors.accent[700], marginBottom: 20 },
  input: {
    borderWidth: 1,
    borderColor: colors.accent[200],
    borderRadius: 12,
    paddingHorizontal: 16,
    paddingVertical: 14,
    fontSize: 16,
    marginBottom: 12,
    backgroundColor: colors.white,
    color: colors.navy[900],
  },
  label: { fontSize: 14, color: colors.accent[700], marginBottom: 8 },
  countryRow: { flexDirection: 'row', flexWrap: 'wrap', gap: 8, marginBottom: 8 },
  countryBtn: {
    paddingHorizontal: 12,
    paddingVertical: 8,
    borderRadius: 8,
    backgroundColor: colors.accent[200],
  },
  countryBtnActive: { backgroundColor: colors.primary[600] },
  countryBtnText: { fontSize: 12, fontWeight: '600', color: colors.navy[900] },
  countryBtnTextActive: { color: colors.white },
  button: {
    backgroundColor: colors.primary[600],
    borderRadius: 12,
    paddingVertical: 16,
    alignItems: 'center',
    marginTop: 16,
    marginBottom: 16,
  },
  buttonDisabled: { opacity: 0.7 },
  buttonText: { color: colors.white, fontSize: 16, fontWeight: '600' },
  link: { color: colors.primary[600], fontSize: 14, textAlign: 'center' },
});
