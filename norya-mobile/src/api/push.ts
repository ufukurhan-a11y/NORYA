import { api } from './client';

export async function registerPushToken(token: string) {
  return api('/api/push/register-mobile', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ push_token: token }),
  });
}
