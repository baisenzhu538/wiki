import { readFileSync, writeFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const OUT_DIR = join(__dirname, '..', '..', '..', '10_raw', 'itingnao');

function normalize(text = '') {
  return String(text).toLowerCase();
}

function score(record) {
  const text = normalize([record.name, record.folder, record.tag, record.topics].join(' '));
  const tags = {
    medicineCabinet: 0,
    clinic: 0,
    medicalSystem: 0,
    aiTech: 0,
    yitangCourse: 0,
    businessMethod: 0,
    supplyChain: 0,
    salesCooperation: 0,
    internalDiscussion: 0,
  };

  const keywords = {
    medicineCabinet: ['药柜', '智能药柜', '药房', '取药机', '售药机', '医保', '处方', '慢病', '慢性病', '互联网医院', '电子处方', '医保报销', '医保个账', '鑫港湾', '七件事', '巨米', '新港湾', '云药房'],
    clinic: ['诊所', '门诊', '医生', '患者', '诊疗', '开方', '问诊', '卫生院', '社区卫生服务中心'],
    medicalSystem: ['医疗系统', '医疗', '医院', '卫健', '药监局', 'gsp', '医疗器械', 'his系统', 'lis'],
    aiTech: ['ai', '大模型', 'agent', 'web coding', '剧本', 'aigc', '人工智能', '机器学习', '算法', '模型训练'],
    yitangCourse: ['一堂', '五步法', '单元模型', '商业壁垒', '需求分析', '产品内核', '业务公式', '增长周期', '建模', '知识萃取'],
    businessMethod: ['商业模式', '护城河', 'ltv', 'cac', 'gmv', 'roi', '转化率', '复购率', '客单价', '私域', '流量', '变现'],
    supplyChain: ['供应链', '钣金', '硅胶', '电机', '售货机', '自动售货机', '外贸', '生产', '硬件', '喷涂', '加工', '模具', '批量'],
    salesCooperation: ['招商', '合作沟通', '合作', '商务', '客户', '销售', '推广', '分销', '分润', '分成', '陪跑', '咨询'],
    internalDiscussion: ['工作进展', '会议', '讨论', '功能讨论', '开发', '前端', '后端', '排期', '迭代', 'bug', '测试'],
  };

  for (const [cat, words] of Object.entries(keywords)) {
    for (const word of words) {
      if (text.includes(word.toLowerCase())) {
        tags[cat] += 1;
      }
    }
  }

  // 根据 folder 名称加权
  const folderName = normalize(record.folder);
  if (['鑫港湾', '七件事', '巨米软件', '新港湾'].some((f) => folderName.includes(f.toLowerCase()))) {
    tags.medicineCabinet += 5;
  }
  if (['一堂五步法', '业务公式拆解', '水水拆书', 'ai短剧'].some((f) => folderName.includes(f.toLowerCase()))) {
    tags.yitangCourse += folderName.includes('ai短剧') ? 0 : 5;
    if (folderName.includes('ai短剧')) tags.aiTech += 5;
  }

  return tags;
}

function classify(record) {
  const s = score(record);
  const entries = Object.entries(s).sort((a, b) => b[1] - a[1]);
  const top = entries[0];
  const typeMap = {
    medicineCabinet: '智能药柜/医疗业务',
    clinic: '诊所/患者相关',
    medicalSystem: '医疗系统/合规',
    aiTech: 'AI/技术',
    yitangCourse: '一堂课程',
    businessMethod: '商业方法论',
    supplyChain: '供应链/硬件制造',
    salesCooperation: '销售/招商/合作沟通',
    internalDiscussion: '内部技术/工作讨论',
  };

  // 如果最高分是 0，归为未分类
  if (top[1] === 0) {
    return { primary: '未分类', scores: s, tags: [] };
  }

  // 取所有得分 >= 最高分 - 2 的类别作为 secondary tags
  const threshold = Math.max(1, top[1] - 2);
  const related = entries.filter((e) => e[1] >= threshold && e[1] > 0).map((e) => typeMap[e[0]]);

  return { primary: typeMap[top[0]], scores: s, tags: related };
}

function main() {
  const metaPath = join(OUT_DIR, 'metadata-latest.json');
  const records = JSON.parse(readFileSync(metaPath, 'utf8')).records;
  const classified = records.map((r) => {
    const c = classify(r);
    const folderText = r.folder || (r.folders || []).map((f) => f.name).join('|') || '';
    return {
      id: r.id,
      name: r.name,
      folder: folderText,
      duration: r.file_long,
      status: r.status,
      data_status: r.data_status,
      summary_status: r.summary_status,
      primary: c.primary,
      tags: c.tags.join('|'),
      created_at: r.create_time,
    };
  });

  // 统计
  const stats = {};
  classified.forEach((c) => {
    stats[c.primary] = (stats[c.primary] || 0) + 1;
  });

  // 输出 JSON
  const outPath = join(OUT_DIR, 'classified-latest.json');
  writeFileSync(outPath, JSON.stringify({ stats, records: classified }, null, 2));

  // 输出 CSV
  const csvPath = join(OUT_DIR, 'classified-latest.csv');
  const headers = ['id', 'name', 'folder', 'duration', 'status', 'data_status', 'summary_status', 'primary', 'tags', 'created_at'];
  const rows = classified.map((r) => [
    r.id,
    `"${r.name.replace(/"/g, '""')}"`,
    `"${r.folder.replace(/"/g, '""')}"`,
    r.duration,
    r.status,
    r.data_status,
    r.summary_status,
    r.primary,
    `"${r.tags.replace(/"/g, '""')}"`,
    r.created_at,
  ].join(','));
  writeFileSync(csvPath, [headers.join(','), ...rows].join('\n'));

  console.log(JSON.stringify(stats, null, 2));
  console.log(`\n分类结果：${outPath}`);
  console.log(`分类 CSV：${csvPath}`);
}

main();
