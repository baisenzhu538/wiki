import { listRecords } from './list-records.js';

async function main() {
  const result = await listRecords({ size: 5 });
  console.log(JSON.stringify({
    ok: true,
    total: result.total,
    sample: result.records.slice(0, 3).map((r) => ({
      id: r.id,
      name: r.name,
      status: r.status,
      updated_at: r.updated_at,
    })),
  }, null, 2));
}

main().catch((err) => {
  console.error(JSON.stringify({ ok: false, error: err.message || String(err) }, null, 2));
  process.exit(1);
});
