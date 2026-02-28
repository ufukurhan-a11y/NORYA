/**
 * Norya API base URL.
 * Geliştirme: Bilgisayarınızda backend çalışıyorsa Android emülatör için 10.0.2.2:8000, iOS için localhost:8000.
 * Fiziksel cihaz: Bilgisayar IP'niz (örn. 192.168.1.10:8000) veya canlı sunucu (https://noryaai.com).
 */
export const API_BASE_URL = process.env.EXPO_PUBLIC_API_URL || 'https://noryaai.com';
