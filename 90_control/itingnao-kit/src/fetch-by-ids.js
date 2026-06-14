import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { getRecordDetail } from './get-record-detail.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const OUT_DIR = join(__dirname, '..', '..', '..', '10_raw', 'itingnao');

function parseArgs(argv) {
  const args = { outDir: OUT_DIR, delayMs: 500, ids: '' };
  for (let i = 0; i < argv.length; i += 1) {
    const item = argv[i];
    if (!item.startsWith('--')) continue;
    const key = item.slice(2);
    const next = argv[i + 1];
    if (!next || next.startsWith('--')) {
      args[key] = true;
    } else {
      args[key] = next;
      i += 1;
    }
  }
  return args;
}

function loadProgress(outDir, label) {
  const path = join(outDir, `fetch-${label}-progress.json`);
  if (!existsSync(path)) return { done: new Set(), errors: [] };
  const data = JSON.parse(readFileSync(path, 'utf8'));
  return { done: new Set(data.done || []), errors: data.errors || [] };
}

function saveProgress(outDir, label, done, errors) {
  const path = join(outDir, `fetch-${label}-progress.json`);
  writeFileSync(path, JSON.stringify({ done: Array.from(done), errors }, null, 2));
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (!args.ids) throw new Error('请提供 --ids id1,id2,id3');
  const ids = args.ids.split(',').map(s => s.trim());
  const label = args.label || 'by-ids';
  
  mkdirSync(args.outDir, { recursive: true });
  mkdirSync(join(args.outDir, 'details'), { recursive: true });
  const progress = loadProgress(args.outDir, label);
  const { done, errors } = progress;

  console.error(`目标录音：${ids.length} 条，已完成 ${done.size} 条`);

  const startTime = Date.now();
  for (let i = 0; i < ids.length; i += 1) {
    const id = ids[i];
    if (done.has(id)) {
      console.error(`[${i + 1}/${ids.length}] ${id} 已跳过`);
      continue;
    }
    try {
      const detail = await getRecordDetail(id);
      const filePath = join(args.outDir, 'details', `${id}.json`);
      writeFileSync(filePath, JSON.stringify(detail, null, 2));
      done.add(id);
      console.error(`[${i + 1}/${ids.length}] ${id} 已保存 | ${detail.detail?.name || ''} | 原文 ${detail.detail?.transcript?.count || 0} 段`);
    } catch (err) {
      errors.push({ id, error: err.message || String(err), at: new Date().toISOString() });
      console.error(`[${i + 1}/${ids.length}] ${id} 失败：${err.message || err}`);
    }
    saveProgress(args.outDir, label, done, errors);
    if (i < ids.length - 1) await new Promise(r => setTimeout(r, args.delayMs));
  }

  const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
  console.error(`\n完成：成功 ${done.size} 条，失败 ${errors.length} 条，耗时 ${elapsed}s`);
  console.log(JSON.stringify({ done: Array.from(done), errors }, null, 2));
}

main().catch(err => { console.error(err.message || err); process.exit(1); });
