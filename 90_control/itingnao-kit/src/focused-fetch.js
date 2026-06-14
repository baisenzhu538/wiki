import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { getRecordDetail } from './get-record-detail.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const OUT_DIR = join(__dirname, '..', '..', '..', '10_raw', 'itingnao');

function parseArgs(argv) {
  const args = {
    outDir: OUT_DIR,
    delayMs: 500,
    categories: '智能药柜/医疗业务,医疗系统/合规,诊所/患者相关',
  };
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

function loadClassified(outDir) {
  const path = join(outDir, 'classified-latest.json');
  if (!existsSync(path)) {
    throw new Error(`找不到分类结果：${path}，请先运行 classify.js`);
  }
  return JSON.parse(readFileSync(path, 'utf8')).records;
}

function loadProgress(outDir) {
  const path = join(outDir, 'focused-progress.json');
  if (!existsSync(path)) return { done: new Set(), errors: [] };
  const data = JSON.parse(readFileSync(path, 'utf8'));
  return { done: new Set(data.done || []), errors: data.errors || [] };
}

function saveProgress(outDir, done, errors) {
  const path = join(outDir, 'focused-progress.json');
  writeFileSync(path, JSON.stringify({ done: Array.from(done), errors }, null, 2));
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const targetCats = args.categories.split(',').map((s) => s.trim());
  const records = loadClassified(args.outDir);
  const targetRecords = records.filter((r) =>
    targetCats.some((cat) => r.primary === cat || r.tags.includes(cat))
  );

  mkdirSync(args.outDir, { recursive: true });
  mkdirSync(join(args.outDir, 'details'), { recursive: true });
  const progress = loadProgress(args.outDir);
  const { done, errors } = progress;

  console.error(`目标分类：${targetCats.join('、')}`);
  console.error(`目标录音：${targetRecords.length} 条，已完成 ${done.size} 条`);

  const startTime = Date.now();
  for (let i = 0; i < targetRecords.length; i += 1) {
    const r = targetRecords[i];
    if (done.has(r.id)) {
      console.error(`[${i + 1}/${targetRecords.length}] ${r.id} 已跳过`);
      continue;
    }

    try {
      const detail = await getRecordDetail(r.id);
      const filePath = join(args.outDir, 'details', `${r.id}.json`);
      writeFileSync(filePath, JSON.stringify(detail, null, 2));
      done.add(r.id);
      console.error(`[${i + 1}/${targetRecords.length}] ${r.id} 已保存 | ${detail.detail.name} | 原文 ${detail.detail.transcript.count} 段`);
    } catch (err) {
      errors.push({ id: r.id, error: err.message || String(err), at: new Date().toISOString() });
      console.error(`[${i + 1}/${targetRecords.length}] ${r.id} 失败：${err.message || err}`);
    }

    saveProgress(args.outDir, done, errors);
    if (i < targetRecords.length - 1) {
      await new Promise((resolve) => setTimeout(resolve, args.delayMs));
    }
  }

  const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
  console.error(`\n完成：成功 ${done.size} 条，失败 ${errors.length} 条，耗时 ${elapsed}s`);
  console.log(JSON.stringify({ done: Array.from(done), errors }, null, 2));
}

main().catch((err) => {
  console.error(err.message || err);
  process.exit(1);
});
