import React, { createContext, useCallback, useContext, useEffect, useState } from 'react';
import type { User } from '../api/auth';
import * as authApi from '../api/auth';
import { getStoredToken, setStoredToken } from '../api/client';

type AuthState = {
  user: User | null;
  token: string | null;
  loading: boolean;
};

const AuthContext = createContext<{
  user: User | null;
  loading: boolean;
  login: (email: string, password: string) => Promise<{ error?: string }>;
  register: (p: { email: string; password: string; full_name: string; phone: string; country: string }) => Promise<{ error?: string }>;
  logout: () => Promise<void>;
  refreshUser: () => Promise<void>;
} | null>(null);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [state, setState] = useState<AuthState>({ user: null, token: null, loading: true });

  const refreshUser = useCallback(async () => {
    const token = await getStoredToken();
    if (!token) {
      setState({ user: null, token: null, loading: false });
      return;
    }
    const res = await authApi.me();
    setState({
      token,
      user: res.data ?? null,
      loading: false,
    });
    if (res.status === 401) await setStoredToken(null);
  }, []);

  useEffect(() => {
    refreshUser();
  }, [refreshUser]);

  const login = useCallback(async (email: string, password: string) => {
    const res = await authApi.login(email, password);
    if (res.error) return { error: res.error };
    await refreshUser();
    return {};
  }, [refreshUser]);

  const register = useCallback(
    async (p: { email: string; password: string; full_name: string; phone: string; country: string }) => {
      const res = await authApi.register(p);
      if (res.error) return { error: res.error };
      return { error: 'Kayıt başarılı. E-posta doğrulama linkine tıklayıp giriş yapabilirsiniz.' };
    },
    []
  );

  const logout = useCallback(async () => {
    await setStoredToken(null);
    setState({ user: null, token: null, loading: false });
  }, []);

  return (
    <AuthContext.Provider
      value={{
        user: state.user,
        loading: state.loading,
        login,
        register,
        logout,
        refreshUser,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error('useAuth must be used within AuthProvider');
  return ctx;
}
