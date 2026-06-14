import { readFileSync, writeFileSync, readdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const BASE_DIR = join(__dirname, '..', '..', '..', '10_raw', 'itingnao');

function main() {
  const compactDir = join(BASE_DIR, 'compact');
  const files = readdirSync(compactDir).filter((f) => f.endsWith('.json'));

  const index = files.map((file) => {
    const data = JSON.parse(readFileSync(join(compactDir, file), 'utf8'));
    return {
      id: data.id,
      name: data.name,
      duration: data.duration,
      createdAt: data.createdAt,
      topics: data.topics,
      tags: data.tags,
      transcriptLength: data.transcript.text.length,
      summaryPreview: data.meetingSummary.content.slice(0, 800),
    };
  });

  const outPath = join(BASE_DIR, 'focused-index.json');
  writeFileSync(outPath, JSON.stringify({ count: index.length, records: index }, null, 2));
  console.error(`索引完成：${index.length} 条`);
  console.error(`输出：${outPath}`);
}

main();
