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

export function normalizeDetail(detail = {}) {
  const transcript = Array.isArray(detail.data) ? detail.data : [];
  const meetingSummary = detail.meeting_summary || '';
  const meetingSummaryStatus = detail.meeting_summary_status === undefined
    ? null
    : Number(detail.meeting_summary_status);
  const dataStatus = detail.data_status === undefined ? null : Number(detail.data_status);
  const overallStatus = detail.status === undefined ? null : Number(detail.status);

  const statusText = (() => {
    if (overallStatus === -2) return '权益受限';
    if (overallStatus === 90) return '需手动生成转写';
    if (overallStatus === 100) return '文件解析失败';
    if (overallStatus === 4) return '处理完成';
    if ([0, 1, 2, 11, 12, 101].includes(overallStatus)) return '处理中';
    return '未知状态';
  })();

  const transcriptText = (() => {
    if (overallStatus === -2) return '权益受限';
    if (dataStatus === 2 || overallStatus === 100) return '转写失败';
    if (dataStatus === 1) return '转写完成';
    if (overallStatus === 90) return '需手动生成转写';
    if (transcript.length && overallStatus === 4) return '转写完成';
    if (dataStatus === 0 || [0, 1, 2, 101, 11, 12].includes(overallStatus)) return '转写中';
    if (transcript.length) return '转写完成';
    return '未知状态';
  })();

  const summaryText = (() => {
    if (meetingSummaryStatus === 2) return '纪要已生成';
    if (meetingSummaryStatus === -1) return '纪要生成失败';
    if ([-2, 0, 1].includes(meetingSummaryStatus)) return '纪要生成中';
    if (overallStatus === 90) return '需先手动生成转写';
    if (meetingSummary) return '纪要已返回';
    return '暂无纪要';
  })();

  return {
    id: detail.id || null,
    name: detail.name || '',
    folderId: detail.folder_id || null,
    duration: detail.long || detail.duration || null,
    createdAt: detail.created_at || null,
    updatedAt: detail.updated_at || null,
    status: { value: overallStatus, text: statusText, done: overallStatus === 4 },
    transcript: {
      data: transcript,
      count: transcript.length,
      status: { value: dataStatus, text: transcriptText, done: dataStatus === 1 || transcript.length > 0 },
    },
    meetingSummary: {
      content: meetingSummary,
      status: { value: meetingSummaryStatus, text: summaryText, done: meetingSummaryStatus === 2 },
    },
    raw: detail,
  };
}

export async function getRecordDetail(id, options = {}) {
  const token = loadApiKey();
  const query = {
    id: Number(id),
    summary_new: options['summary-new'] || '1',
  };
  if (options['content-type']) query.content_type = options['content-type'];

  const data = await requestJSON({
    method: 'GET',
    apiPath: '/api/record/detail',
    query,
    token,
  });

  return {
    success: true,
    request: query,
    detail: normalizeDetail(data.data),
  };
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (!args.id) {
    console.error('缺少 --id 参数');
    process.exit(1);
  }
  const result = await getRecordDetail(args.id, args);
  console.log(JSON.stringify(result, null, 2));
}

main().catch((err) => {
  console.error(err.message || err);
  process.exit(1);
});
