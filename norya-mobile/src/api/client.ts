import * as SecureStore from 'expo-secure-store';
import { API_BASE_URL } from '../config';

const TOKEN_KEY = 'norya_token';

export async function getStoredToken(): Promise<string | null> {
  try {
    return await SecureStore.getItemAsync(TOKEN_KEY);
  } catch {
    return null;
  }
}

export async function setStoredToken(token: string | null): Promise<void> {
  if (token) await SecureStore.setItemAsync(TOKEN_KEY, token);
  else await SecureStore.deleteItemAsync(TOKEN_KEY);
}

export async function api<T>(
  path: string,
  options: RequestInit & { token?: string | null } = {}
): Promise<{ data?: T; error?: string; status: number }> {
  const { token, ...fetchOpts } = options;
  const headers: Record<string, string> = {
    ...((fetchOpts.headers as Record<string, string>) || {}),
  };
  const auth = token ?? (await getStoredToken());
  if (auth) headers['Authorization'] = `Bearer ${auth}`;

  const url = path.startsWith('http') ? path : `${API_BASE_URL.replace(/\/$/, '')}${path.startsWith('/') ? path : `/${path}`}`;
  try {
    const res = await fetch(url, {
      ...fetchOpts,
      headers: { ...headers, ...(fetchOpts.headers as object) },
    });
    const text = await res.text();
    let data: T | undefined;
    try {
      data = text ? (JSON.parse(text) as T) : undefined;
    } catch {
      if (!res.ok) return { error: text || res.statusText, status: res.status };
    }
    if (!res.ok) {
      const errMsg = (data as { detail?: string })?.detail || text || res.statusText;
      return { error: typeof errMsg === 'string' ? errMsg : JSON.stringify(errMsg), status: res.status };
    }
    return { data: data as T, status: res.status };
  } catch (e) {
    const msg = e instanceof Error ? e.message : 'Bağlantı hatası';
    return { error: msg, status: 0 };
  }
}
