import { api } from './client';

export type AnalyzeResponse = {
  sonuc: string;
  notu?: string;
  analiz_id: number | null;
};

export async function analyzeText(params: {
  text: string;
  doctor_notes?: string;
  lang?: string;
}) {
  return api<AnalyzeResponse>('/analyze', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      text: params.text,
      doctor_notes: params.doctor_notes || null,
      lang: params.lang || 'tr',
    }),
  });
}

export async function analyzeUpload(uri: string, filename: string, lang: string = 'tr') {
  const token = await import('./client').then((c) => c.getStoredToken());
  const form = new FormData();
  // @ts-expect-error FormData append accepts Blob in RN
  form.append('file', {
    uri,
    name: filename || 'image.jpg',
    type: 'image/jpeg',
  });
  form.append('lang', lang);

  const url = `${(await import('../config')).API_BASE_URL.replace(/\/$/, '')}/analyze/upload`;
  const headers: Record<string, string> = {};
  if (token) headers['Authorization'] = `Bearer ${token}`;

  const res = await fetch(url, {
    method: 'POST',
    body: form,
    headers: { ...headers },
  });
  const text = await res.text();
  let data: AnalyzeResponse | undefined;
  try {
    data = text ? JSON.parse(text) : undefined;
  } catch {
    return { error: text || res.statusText, status: res.status };
  }
  if (!res.ok) {
    const errMsg = (data as { detail?: string })?.detail || text;
    return { error: typeof errMsg === 'string' ? errMsg : JSON.stringify(errMsg), status: res.status };
  }
  return { data, status: res.status };
}

export type HistoryItem = {
  id: number;
  input_preview: string;
  result_preview: string;
  source: string;
  created_at: string;
  is_favorite: boolean;
};

export async function getHistory() {
  return api<HistoryItem[]>('/analyze/history');
}

export type AnalysisDetail = {
  id: number;
  input_text: string;
  result_text: string;
  source: string;
  created_at: string;
  doctor_notes?: string;
  is_favorite: boolean;
};

export async function getAnalysisDetail(id: number) {
  return api<AnalysisDetail>(`/analyze/history/${id}`);
}
