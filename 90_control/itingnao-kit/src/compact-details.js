import { readFileSync, writeFileSync, mkdirSync, readdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const BASE_DIR = join(__dirname, '..', '..', '..', '10_raw', 'itingnao');

function compact(detail) {
  const raw = detail.detail?.raw || {};
  const transcriptData = detail.detail?.transcript?.data || [];
  const meetingSummary = detail.detail?.meetingSummary?.content || '';

  return {
    id: detail.detail?.id || raw.id,
    name: detail.detail?.name || raw.name,
    folderId: detail.detail?.folderId || raw.folder_id,
    duration: detail.detail?.duration || raw.file_long,
    createdAt: detail.detail?.createdAt || raw.created_at,
    status: detail.detail?.status,
    transcript: {
      count: transcriptData.length,
      status: detail.detail?.transcript?.status,
      text: transcriptData.map((item) => {
        if (typeof item === 'string') return item;
        if (item && typeof item === 'object') {
          return item.text || item.content || JSON.stringify(item);
        }
        return '';
      }).join('\n'),
    },
    meetingSummary: {
      content: meetingSummary,
      status: detail.detail?.meetingSummary?.status,
    },
    topics: raw.meeting_topic || [],
    tags: raw.tag || '',
  };
}

function main() {
  const detailsDir = join(BASE_DIR, 'details');
  const compactDir = join(BASE_DIR, 'compact');
  mkdirSync(compactDir, { recursive: true });

  const files = readdirSync(detailsDir).filter((f) => f.endsWith('.json'));
  let totalSaved = 0;

  for (const file of files) {
    const detail = JSON.parse(readFileSync(join(detailsDir, file), 'utf8'));
    const small = compact(detail);
    const outPath = join(compactDir, file);
    writeFileSync(outPath, JSON.stringify(small, null, 2));

    const originalSize = readFileSync(join(detailsDir, file)).length;
    const compactSize = readFileSync(outPath).length;
    totalSaved += originalSize - compactSize;
  }

  console.error(`精简完成：${files.length} 个文件`);
  console.error(`节省空间：${(totalSaved / 1024 / 1024).toFixed(1)} MB`);
  console.error(`输出目录：${compactDir}`);
}

main();
