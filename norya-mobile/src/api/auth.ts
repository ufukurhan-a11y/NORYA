import { api, setStoredToken } from './client';

export type User = {
  id: number;
  email: string;
  full_name: string;
  phone?: string;
  country?: string;
};

export type Token = { access_token: string };

export async function login(email: string, password: string) {
  const form = new FormData();
  form.append('email', email);
  form.append('password', password);
  const res = await api<Token>('/auth/login', {
    method: 'POST',
    body: form,
    headers: {},
    token: null,
  });
  if (res.data) await setStoredToken(res.data.access_token);
  return res;
}

export async function register(params: {
  email: string;
  password: string;
  full_name: string;
  phone: string;
  country: string;
}) {
  const form = new FormData();
  form.append('email', params.email);
  form.append('password', params.password);
  form.append('full_name', params.full_name);
  form.append('phone', params.phone);
  form.append('country', params.country);
  const res = await api<User>('/auth/register', {
    method: 'POST',
    body: form,
    headers: {},
    token: null,
  });
  return res;
}

export async function me() {
  return api<User>('/auth/me');
}
