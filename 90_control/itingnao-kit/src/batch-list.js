import { writeFileSync, existsSync, mkdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { listRecords } from './list-records.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const DEFAULT_OUT_DIR = join(__dirname, '..', '..', '..', '10_raw', 'itingnao');

function parseArgs(argv) {
  const args = { outDir: DEFAULT_OUT_DIR, size: 100 };
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

async function fetchAllMetadata({ outDir, size = 100, delayMs = 300 }) {
  const records = [];
  let page = 1;
  let totalPage = null;
  const startTime = Date.now();

  while (true) {
    const batch = await listRecords({ size, page });
    if (batch.records.length === 0) break;
    records.push(...batch.records);
    console.error(`page ${page}: +${batch.records.length} | total ${records.length}${batch.total ? ` / ${batch.total}` : ''}`);

    if (batch.pagination) {
      totalPage = batch.pagination.total_page;
      if (page >= totalPage) break;
    } else if (batch.records.length < size) {
      break;
    }

    page += 1;
    await new Promise((resolve) => setTimeout(resolve, delayMs));
  }

  const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
  console.error(`\n拉取完成：${records.length} 条，耗时 ${elapsed}s`);

  mkdirSync(outDir, { recursive: true });
  const metaPath = join(outDir, `metadata-${Date.now()}.json`);
  const latestPath = join(outDir, 'metadata-latest.json');
  const payload = {
    fetchedAt: new Date().toISOString(),
    count: records.length,
    records,
  };
  writeFileSync(metaPath, JSON.stringify(payload, null, 2));
  writeFileSync(latestPath, JSON.stringify(payload, null, 2));

  // 同时输出 CSV 摘要
  const csvPath = join(outDir, 'metadata-latest.csv');
  const headers = ['id', 'name', 'folder', 'duration', 'status', 'data_status', 'summary_status', 'tags', 'topics', 'created_at', 'file_path'];
  const rows = records.map((r) => {
    const folder = (r.folders || []).map((f) => f.name).join('|');
    const tags = r.tag || '';
    const topics = (r.meeting_topic || []).join('|');
    return [
      r.id,
      `"${(r.name || '').replace(/"/g, '""')}"`,
      `"${folder.replace(/"/g, '""')}"`,
      r.file_long || '',
      r.status || '',
      r.data_status || '',
      r.summary_status || '',
      `"${tags.replace(/"/g, '""')}"`,
      `"${topics.replace(/"/g, '""')}"`,
      r.create_time || '',
      r.file_path || '',
    ].join(',');
  });
  writeFileSync(csvPath, [headers.join(','), ...rows].join('\n'));

  console.error(`元数据 JSON：${metaPath}`);
  console.error(`元数据 JSON：${latestPath}`);
  console.error(`元数据 CSV：${csvPath}`);
  return payload;
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const result = await fetchAllMetadata(args);
  console.log(JSON.stringify({ count: result.count, outDir: args.outDir }, null, 2));
}

main().catch((err) => {
  console.error(err.message || err);
  process.exit(1);
});
