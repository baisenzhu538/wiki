import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { getRecordDetail } from './get-record-detail.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const DEFAULT_OUT_DIR = join(__dirname, '..', '..', '..', '10_raw', 'itingnao');

function parseArgs(argv) {
  const args = { outDir: DEFAULT_OUT_DIR, delayMs: 500, resume: true };
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

function loadMetadata(outDir) {
  const latestPath = join(outDir, 'metadata-latest.json');
  if (!existsSync(latestPath)) {
    throw new Error(`找不到元数据：${latestPath}，请先运行 batch-list`);
  }
  const payload = JSON.parse(readFileSync(latestPath, 'utf8'));
  return payload.records || [];
}

function loadProgress(outDir) {
  const progressPath = join(outDir, 'detail-progress.json');
  if (!existsSync(progressPath)) return { done: new Set(), errors: [] };
  const data = JSON.parse(readFileSync(progressPath, 'utf8'));
  return { done: new Set(data.done || []), errors: data.errors || [] };
}

function saveProgress(outDir, done, errors) {
  const progressPath = join(outDir, 'detail-progress.json');
  writeFileSync(progressPath, JSON.stringify({ done: Array.from(done), errors }, null, 2));
}

async function fetchDetails({ outDir, delayMs = 500, resume = true, filter = null }) {
  mkdirSync(outDir, { recursive: true });
  const records = loadMetadata(outDir);
  let targetRecords = records;
  if (filter && typeof filter === 'function') {
    targetRecords = records.filter(filter);
  }

  const progress = resume ? loadProgress(outDir) : { done: new Set(), errors: [] };
  const { done, errors } = progress;

  console.error(`总计 ${records.length} 条，本次目标 ${targetRecords.length} 条，已完成 ${done.size} 条`);

  const startTime = Date.now();
  for (let i = 0; i < targetRecords.length; i += 1) {
    const record = targetRecords[i];
    const id = record.id;
    if (done.has(id)) {
      console.error(`[${i + 1}/${targetRecords.length}] ${id} 已跳过`);
      continue;
    }

    try {
      const detail = await getRecordDetail(id);
      const filePath = join(outDir, 'details', `${id}.json`);
      mkdirSync(dirname(filePath), { recursive: true });
      writeFileSync(filePath, JSON.stringify(detail, null, 2));
      done.add(id);
      console.error(`[${i + 1}/${targetRecords.length}] ${id} 已保存 | ${detail.detail.name}`);
    } catch (err) {
      errors.push({ id, error: err.message || String(err), at: new Date().toISOString() });
      console.error(`[${i + 1}/${targetRecords.length}] ${id} 失败：${err.message || err}`);
    }

    saveProgress(outDir, done, errors);

    if (i < targetRecords.length - 1) {
      await new Promise((resolve) => setTimeout(resolve, delayMs));
    }
  }

  const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
  console.error(`\n详情拉取完成：成功 ${done.size} 条，失败 ${errors.length} 条，耗时 ${elapsed}s`);
  return { done: Array.from(done), errors };
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const result = await fetchDetails(args);
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  console.error(err.message || err);
  process.exit(1);
});

export { fetchDetails, loadMetadata };
