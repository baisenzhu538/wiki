import { loadApiKey, requestJSON } from './config.js';

function parseArgs(argv) {
  const args = {};
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

export async function listRecords(options = {}) {
  const token = loadApiKey();
  const page = Number(options.page || options.p || 1);
  const size = Math.min(Number(options.size || options.limit || 20), 100);
  const body = {
    page,
    size,
  };
  if (options.name || options.q) body.record_name = options.name || options.q;
  if (options.folder_id) body.folder_id = options.folder_id;
  if (options.file_type) body.file_type = options.file_type;
  if (options.sortby) body.sortby = options.sortby;
  if (options.source) body.source = options.source;

  const data = await requestJSON({
    method: 'GET',
    apiPath: '/api/record/list',
    query: body,
    token,
  });

  return {
    page,
    size,
    total: data.data?.total ?? data.data?.count ?? data.data?.items?.length ?? 0,
    records: data.data?.records || data.data?.items || [],
    raw: data,
  };
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const result = await listRecords(args);
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  console.error(err.message || err);
  process.exit(1);
});
