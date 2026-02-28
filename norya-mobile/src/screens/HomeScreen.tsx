import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import { useAuth } from '../context/AuthContext';
import { colors } from '../theme/colors';

export default function HomeScreen({
  onAnalyze,
  onHistory,
  onLogin,
  onRegister,
}: {
  onAnalyze: () => void;
  onHistory: () => void;
  onLogin: () => void;
  onRegister: () => void;
}) {
  const { user } = useAuth();

  return (
    <View style={styles.container}>
      <View style={styles.hero}>
        <Text style={styles.title}>Norya</Text>
        <Text style={styles.subtitle}>Kan tahlili analizi — 60 saniyede anlaşılır rapor</Text>
      </View>
      {user ? (
        <>
          <Text style={styles.welcome}>Merhaba, {user.full_name || user.email}</Text>
          <TouchableOpacity style={styles.primaryButton} onPress={onAnalyze}>
            <Text style={styles.primaryButtonText}>Analiz Yap</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.secondaryButton} onPress={onHistory}>
            <Text style={styles.secondaryButtonText}>Geçmiş Analizler</Text>
          </TouchableOpacity>
        </>
      ) : (
        <>
          <TouchableOpacity style={styles.primaryButton} onPress={onRegister}>
            <Text style={styles.primaryButtonText}>Ücretsiz Başla</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.secondaryButton} onPress={onLogin}>
            <Text style={styles.secondaryButtonText}>Giriş Yap</Text>
          </TouchableOpacity>
          <Text style={styles.hint}>İlk analiz ücretsiz. Kayıt olup tahlil yükleyebilirsiniz.</Text>
        </>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 24,
    paddingTop: 48,
    backgroundColor: colors.navy[900],
  },
  hero: {
    marginBottom: 32,
  },
  title: {
    fontSize: 32,
    fontWeight: '800',
    color: colors.white,
    letterSpacing: -0.5,
  },
  subtitle: {
    fontSize: 16,
    color: colors.navy[200],
    marginTop: 8,
    lineHeight: 22,
  },
  welcome: {
    fontSize: 16,
    color: colors.navy[200],
    marginBottom: 24,
  },
  primaryButton: {
    backgroundColor: colors.primary[600],
    borderRadius: 16,
    paddingVertical: 18,
    alignItems: 'center',
    marginBottom: 12,
  },
  primaryButtonText: {
    color: colors.white,
    fontSize: 18,
    fontWeight: '700',
  },
  secondaryButton: {
    borderRadius: 16,
    paddingVertical: 18,
    alignItems: 'center',
    borderWidth: 2,
    borderColor: colors.primary[500],
  },
  secondaryButtonText: {
    color: colors.primary[300],
    fontSize: 16,
    fontWeight: '600',
  },
  hint: {
    marginTop: 24,
    fontSize: 14,
    color: colors.navy[200],
    textAlign: 'center',
  },
});
