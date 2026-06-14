import { readFileSync } from 'node:fs';
import { homedir } from 'node:os';
import { join } from 'node:path';

export const BASE_URL = 'https://api.itingnao.com';

export function loadApiKey() {
  // 优先环境变量
  if (process.env.ITINGNAO_API_KEY) {
    return process.env.ITINGNAO_API_KEY.trim();
  }
  // 其次本地 .itingnao_api_key
  const candidates = [
    join(homedir(), '.itingnao_api_key'),
    join(process.cwd(), '.itingnao_api_key'),
  ];
  for (const path of candidates) {
    try {
      return readFileSync(path, 'utf8').trim();
    } catch {
      // ignore
    }
  }
  throw new Error('未找到 ITINGNAO_API_KEY：请设置环境变量或在 ~/.itingnao_api_key 放置 key');
}

export function createHeaders(token) {
  return {
    Accept: 'application/json, text/plain, */*',
    Authorization: `Bearer ${token}`,
    'Content-Type': 'application/json;charset=UTF-8',
  };
}

export function buildUrl(apiPath, query = {}) {
  const url = new URL(apiPath, BASE_URL);
  Object.entries(query).forEach(([key, value]) => {
    if (value === undefined || value === null || value === '') return;
    if (Array.isArray(value)) {
      value.forEach((item) => url.searchParams.append(key, String(item)));
      return;
    }
    url.searchParams.set(key, String(value));
  });
  return url.toString();
}

export async function requestJSON({ method, apiPath, query, body, token }) {
  const url = buildUrl(apiPath, query);
  const options = {
    method: method.toUpperCase(),
    headers: createHeaders(token),
  };
  if (body !== undefined && options.method !== 'GET') {
    options.body = JSON.stringify(body);
  }
  const response = await fetch(url, options);
  const text = await response.text();
  let data;
  try {
    data = text ? JSON.parse(text) : {};
  } catch {
    throw new Error(`接口返回非 JSON: ${text}`);
  }
  if (!response.ok || data.code !== 200) {
    throw new Error(`请求失败 ${response.status}: ${text}`);
  }
  return data;
}
