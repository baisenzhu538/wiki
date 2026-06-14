const fs = require('fs');

// 1. 创建药柜补充队列
const medicalSupplement = {
  generatedAt: new Date().toISOString(),
  source: 'non-medical-processing-contamination',
  note: '这些录音最初被分到非药柜主题，经主题提炼后发现实质涉及药柜/医疗/药店业务，现归入药柜长期关注队列补充清单。',
  records: [
    { id: '4226418', title: '药店-选址选品运营讨论', primary: '内部技术/工作讨论', subTheme: '药店运营', priority: 'P1' },
    { id: '4092592', title: '多人-药店数字化改造讨论', primary: 'AI/技术', subTheme: '药店数字化', priority: 'P1' },
    { id: '3424604', title: '云聚米-私有化部署与开发沟通', primary: '内部技术/工作讨论', subTheme: '医疗SaaS/HIS', priority: 'P1' },
    { id: '3166977', title: '润馨堂-品牌运营讨论', primary: '内部技术/工作讨论', subTheme: '医药品牌运营', priority: 'P2' },
    { id: '2247045', title: '瑞心堂-集采与品牌升级讨论', primary: '内部技术/工作讨论', subTheme: '医药供应链', priority: 'P2' },
    { id: '6269640', title: '货柜-结构与电子方案讨论', primary: '供应链/硬件制造', subTheme: '智能药柜硬件', priority: 'P0' },
    { id: '1483043', title: '项目分账与支付对接方案', primary: '未分类', subTheme: '药柜支付合规', priority: 'P1' },
    { id: '6272697', title: '外卖平台-智能分单系统沟通', primary: '未分类', subTheme: '医药即时零售/恒温', priority: 'P2' },
    { id: '2694971', title: '多人-AI与行业发展讨论', primary: 'AI/技术', subTheme: 'AI+药店', priority: 'P2' },
    { id: '1486162', title: '智慧城市AI应用交流', primary: 'AI/技术', subTheme: '医疗AI/智慧健康', priority: 'P2' },
    { id: '6311449', title: '一堂-商业项目宣讲会', primary: '一堂课程', subTheme: '医疗科技项目片段', priority: 'P2', note: '仅相关片段，非整条录音' },
    { id: '4231073', title: '多人-项目问题沟通', primary: '未分类', subTheme: '疑似药柜设备', priority: 'P1', note: '需原文复核后确认' }
  ]
};

fs.writeFileSync('90_control/itingnao-kit/work/medical-queue-supplement.json', JSON.stringify(medicalSupplement, null, 2));

// 2. 读取 102 条未覆盖录音，做更细的主题拆分
const data = JSON.parse(fs.readFileSync('90_control/itingnao-kit/work/non-med-uncovered.json', 'utf8'));
const compactDir = '10_raw/itingnao/compact';
const medicalIds = new Set(medicalSupplement.records.map(r => r.id));
const invalidIds = new Set(['7490653', '6969289', '6272340', '4460180', '4360030', '4067012', '4028344', '3185113', '3111485', '2066588', '1236242', '1236241', '1236240']);

function readCompact(id) {
  const path = `${compactDir}/${id}.json`;
  if (!fs.existsSync(path)) return null;
  return JSON.parse(fs.readFileSync(path, 'utf8'));
}

function subThemeClassify(r) {
  const name = r.name.toLowerCase();
  const tags = r.tags.toLowerCase();
  const full = name + ' ' + tags;
  const c = readCompact(r.id);
  const summary = (c?.meetingSummary?.content || '').toLowerCase();
  const allText = full + ' ' + summary;

  if (medicalIds.has(String(r.id))) {
    return { theme: 'medical-moved', subTheme: '已移入药柜队列' };
  }
  if (invalidIds.has(String(r.id))) {
    return { theme: 'invalid', subTheme: '无效/低价值' };
  }

  if (allText.includes('y模型')) return { theme: 'yitang', subTheme: 'Y模型科学做事框架' };
  if (allText.includes('业务公式') || allText.includes('波特五力') || allText.includes('商业分析方法论') || allText.includes('差距分析') || allText.includes('鱼骨图')) return { theme: 'yitang', subTheme: '业务公式与商业分析工具' };
  if (allText.includes('知识萃取')) return { theme: 'yitang', subTheme: '知识萃取方法论' };
  if (allText.includes('ipo')) return { theme: 'yitang', subTheme: 'IPO学习模型' };
  if (allText.includes('tcpr') || allText.includes('pcpr')) return { theme: 'yitang', subTheme: 'TCPR/PCPR能力模型' };
  if (allText.includes('案例必修')) return { theme: 'yitang', subTheme: '一堂案例课方法论' };
  if (allText.includes('课程地图')) return { theme: 'yitang', subTheme: '一堂课程体系与个人成长地图' };
  if (allText.includes('新人落地')) return { theme: 'yitang', subTheme: '新人落地与团队能力复制' };
  if (allText.includes('教学能力') || allText.includes('训战营')) return { theme: 'yitang', subTheme: '教学能力与线下训战' };
  if (allText.includes('需求评估') || allText.includes('需求分析')) return { theme: 'yitang', subTheme: '需求评估方法论' };
  if (allText.includes('战略') || allText.includes('九层宝塔')) return { theme: 'yitang', subTheme: '战略规划方法论' };
  if (allText.includes('精益')) return { theme: 'methodology', subTheme: '精益创业与假设验证' };
  if (allText.includes('原则')) return { theme: 'personal', subTheme: '《原则》与个人决策系统' };
  if (allText.includes('必然') || allText.includes('凯文凯利')) return { theme: 'personal', subTheme: '科技趋势与个人判断' };
  if (allText.includes('超级个体')) return { theme: 'personal', subTheme: 'AI时代的超级个体' };
  if (allText.includes('消除模糊')) return { theme: 'personal', subTheme: '认知模糊与个人成长' };
  if (allText.includes('偶然') || allText.includes('必然')) return { theme: 'personal', subTheme: '复杂系统与偶然必然' };
  if (allText.includes('中国行') || allText.includes('使命')) return { theme: 'personal', subTheme: '个人使命与教学创新' };
  if (allText.includes('ai场景落地') || allText.includes('ai落地') || allText.includes('ai方法论') || allText.includes('找老的干小的')) return { theme: 'ai', subTheme: 'AI落地方法论与场景选择' };
  if (allText.includes('ai数据') || allText.includes('数据飞轮')) return { theme: 'ai', subTheme: 'AI数据资产与数据飞轮' };
  if (allText.includes('ai工具') || allText.includes('龙虾') || allText.includes('openclaw') || allText.includes('open cloud') || allText.includes('智能入口')) return { theme: 'ai', subTheme: 'AI工具栈与协作平台' };
  if (allText.includes('ai组织') || allText.includes('组织行为')) return { theme: 'ai', subTheme: 'AI时代的组织分工' };
  if (allText.includes('路演') || allText.includes('项目汇报') || allText.includes('战队') || allText.includes('大航海')) return { theme: 'ai', subTheme: 'AI大航海项目路演案例' };
  if (allText.includes('酒店') || allText.includes('贝壳') || allText.includes('选品') || allText.includes('标签审核') || allText.includes('外呼')) return { theme: 'ai', subTheme: '产业AI运营案例' };
  if (allText.includes('剧本创作') || allText.includes('短剧') || allText.includes('四格漫画') || allText.includes('ai内容营销')) return { theme: 'ai', subTheme: 'AI内容创作案例' };
  if (allText.includes('geo') || allText.includes('aio') || allText.includes('机优') || allText.includes('营销')) return { theme: 'ai', subTheme: 'AI营销与搜索优化' };
  if (allText.includes('双柚汁') || allText.includes('金银花') || allText.includes('调配') || allText.includes('口感')) return { theme: 'beverage', subTheme: '餐饮渠道饮料开发' };
  if (allText.includes('系统费用') || allText.includes('进项税') || allText.includes('履约') || allText.includes('分账') || allText.includes('支付') || allText.includes('高新技术')) return { theme: 'business', subTheme: '财务法务商务运营' };
  if (allText.includes('产品方向') || allText.includes('市场分析') || allText.includes('项目问题')) return { theme: 'business', subTheme: '产品战略与商业取舍' };
  if (allText.includes('fd')) return { theme: 'business', subTheme: 'FD模式与客户深度合作' };
  if (allText.includes('智能设备') || allText.includes('外卖对接') || allText.includes('智能分单')) return { theme: 'business', subTheme: '智能设备与外卖自动化' };
  if (allText.includes('网络话密达') || allText.includes('智慧水务')) return { theme: 'business', subTheme: '数据公司技术中台' };
  if (allText.includes('一起引擎')) return { theme: 'business', subTheme: '出海与战略咨询' };
  if (allText.includes('d同学')) return { theme: 'ai', subTheme: 'AI复杂沟通落地案例' };
  if (allText.includes('自习室') || allText.includes('共学')) return { theme: 'ai', subTheme: 'AI辅助教学共学' };
  if (allText.includes('润之美') || allText.includes('草本饮料') || allText.includes('凉茶')) return { theme: 'beverage', subTheme: '草本饮料合作' };

  return { theme: 'other', subTheme: '待复核' };
}

const subGroups = {};
for (const r of data.uncoveredRecords) {
  const { theme, subTheme } = subThemeClassify(r);
  subGroups[theme] = subGroups[theme] || {};
  subGroups[theme][subTheme] = subGroups[theme][subTheme] || [];
  subGroups[theme][subTheme].push(r);
}

fs.writeFileSync('90_control/itingnao-kit/work/non-med-subthemes.json', JSON.stringify({ generatedAt: new Date().toISOString(), subGroups }, null, 2));

console.log('=== 102条未覆盖录音细主题拆分 ===\n');
for (const [theme, subs] of Object.entries(subGroups).sort((a, b) => {
  const countA = Object.values(a[1]).reduce((s, r) => s + r.length, 0);
  const countB = Object.values(b[1]).reduce((s, r) => s + r.length, 0);
  return countB - countA;
})) {
  const total = Object.values(subs).reduce((s, r) => s + r.length, 0);
  console.log(`\n## ${theme} (${total})`);
  for (const [sub, recs] of Object.entries(subs).sort((a, b) => b[1].length - a[1].length)) {
    console.log(`  ### ${sub} (${recs.length})`);
    recs.forEach(r => console.log(`    - ${r.id} | ${r.name}`));
  }
}

console.log('\n\n已保存：90_control/itingnao-kit/work/non-med-subthemes.json');
console.log('已保存：90_control/itingnao-kit/work/medical-queue-supplement.json');
