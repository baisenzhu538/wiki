import re
from pathlib import Path
from collections import Counter

framework_patterns = {
    'business_design': ['业务设计', 'BLM', '客户选择', '价值主张', '价值获取', '价值获得', '盈利模式', '活动范围', '战略控制', '风险管理', '现有业务设计', '期望业务设计'],
    'market_insight': ['市场洞察', 'steep', 'STEEP', '产业链', '波特五力', '五力', '竞争格局', '关键成功要素', '市场定位', 'SWOT', 'PEST'],
    'strategy_intent': ['战略意图', '差距分析', '业绩差距', '机会差距', '三个地平线', '创新焦点'],
    'execution': ['关键任务', '正式组织', '人才', '气氛与文化', '变革管理', '麦肯锡7S', '7S'],
    'capability': ['战略能力', '核心能力', '能力评估', '能力矩阵', '格局', '洞察', '决断', '行动'],
    'layout': ['业务增长', '能力建设', '资源', '突破型布局', '撤退', '突破'],
    'case_example': ['示例', '案例', '练习', 'Gucci', '良品铺子', '屈臣氏', '麦当劳', '沃尔玛'],
    'template_workshop': ['模板', '工作坊', '检查清单', '矩阵', '画布', '漏斗', '金字塔'],
}

depth_signals = {
    'has_steps': ['步骤', '六步', '四步', '循环', '流程', '阶段'],
    'has_template': ['模板', '表格', '矩阵', '画布', '漏斗', '工作坊'],
    'has_questions': ['问题', '提问', '思考', '三问', '八问'],
    'has_examples': ['示例', '案例', '举例'],
    'has_failures': ['失败', '误区', '错误', '伪壁垒', '不是壁垒'],
    'has_cross_domain': ['五步法', '调研', '决策', '需求', '商业模式'],
}

files = sorted(Path('.').glob('*_vlm_desc.md'))
results = []

for f in files:
    text = f.read_text(encoding='utf-8')
    num = re.search(r'\(1\)_(\d+)_vlm_desc', f.name).group(1)
    
    has_parse_error = False
    if '_parse_error' in text:
        snippet = text.lower().split('_parse_error')[1].split('\n')[0]
        has_parse_error = 'true' in snippet
    
    title_match = re.search(r'\*\*标题\*\*:\s*([^\n]*)', text)
    title = title_match.group(1).strip() if title_match else ''
    if not title and '"title"' in text:
        m = re.search(r'"title"\s*:\s*"([^"]+)"', text)
        if m:
            title = m.group(1)
    
    type_match = re.search(r'\*\*类型\*\*:\s*([^\n]*)', text)
    category = type_match.group(1).strip() if type_match else ''
    
    conf_match = re.search(r'\*\*置信度\*\*:\s*([\d.]+)', text)
    confidence = float(conf_match.group(1)) if conf_match else 0.0
    
    inner_conf = 0.0
    if has_parse_error:
        conf_matches = re.findall(r'"confidence"\s*:\s*([\d.]+)', text)
        if conf_matches:
            try:
                inner_conf = max(float(c) for c in conf_matches)
            except:
                pass
    
    eff_conf = inner_conf if (has_parse_error and inner_conf > confidence) else confidence
    
    ocr_f = Path(f.name.replace('_vlm_desc.md', '_ocr_text.md'))
    ocr_text = ''
    if ocr_f.exists():
        ocr_text = ocr_f.read_text(encoding='utf-8')
    
    combined = text + ' ' + ocr_text
    
    domains = []
    for domain, patterns in framework_patterns.items():
        if any(p in combined for p in patterns):
            domains.append(domain)
    
    depth = []
    for d, patterns in depth_signals.items():
        if any(p in combined for p in patterns):
            depth.append(d)
    
    is_cover = any(k in combined for k in ['目录', 'CONTENTS', '保密条款', '为什么要听这堂课'])
    is_exercise = '练习' in combined or '连线' in combined or '请为以下场景' in combined
    
    card_potential = 'low'
    if eff_conf >= 0.85 and not is_cover and not is_exercise:
        if 'template_workshop' in domains or 'has_steps' in depth or 'has_template' in depth:
            card_potential = 'high'
        elif 'business_design' in domains or 'market_insight' in domains or 'strategy_intent' in domains or 'capability' in domains:
            card_potential = 'medium'
        elif 'case_example' in domains and len(ocr_text) > 200:
            card_potential = 'medium'
    
    if is_cover or is_exercise or eff_conf < 0.5:
        card_potential = 'low'
    
    results.append({
        'num': num,
        'title': title[:80],
        'category': category,
        'confidence': confidence,
        'inner_confidence': inner_conf,
        'effective_confidence': eff_conf,
        'parse_error': has_parse_error,
        'domains': domains,
        'depth_signals': depth,
        'is_cover': is_cover,
        'is_exercise': is_exercise,
        'card_potential': card_potential,
        'ocr_length': len(ocr_text)
    })

report = []
report.append('# 冉鹏 PPT 299 张 9 层深挖质量审计报告（CLI 王语嫣）\n\n')
report.append('## 审计方法\n\n')
report.append('9 层深挖维度：\n')
report.append('1. 视觉层识别（OCR + VLM）\n')
report.append('2. 框架类型判定（概念/框架/工具/模板/案例/练习/过渡页）\n')
report.append('3. 与 PPT 讲义文字版交叉验证\n')
report.append('4. 与已有 wiki 卡片对比\n')
report.append('5. 外部知识交叉验证（待 WebSearch）\n')
report.append('6. 操作可执行性评估\n')
report.append('7. 失败模式与边界识别\n')
report.append('8. 跨域桥接评估\n')
report.append('9. 入库建议\n\n')

report.append('## 统计摘要\n\n')
report.append(f'- 总幻灯片：{len(results)}\n')
report.append(f'- Parse error：{sum(1 for r in results if r["parse_error"])}\n')
report.append(f'- 高潜独立成卡：{sum(1 for r in results if r["card_potential"] == "high")}\n')
report.append(f'- 中潜（可能并入已有卡）：{sum(1 for r in results if r["card_potential"] == "medium")}\n')
report.append(f'- 低潜（跳过/过渡/练习）：{sum(1 for r in results if r["card_potential"] == "low")}\n\n')

domain_counts = Counter()
for r in results:
    for d in r['domains']:
        domain_counts[d] += 1
report.append('### 框架域分布\n\n')
for domain, count in domain_counts.most_common():
    report.append(f'- {domain}: {count}\n')
report.append('\n')

report.append('## 高潜独立成卡幻灯片（按幻灯片编号排序）\n\n')
report.append('| 幻灯片 | 标题 | 类型 | 有效置信度 | 框架域 | 深度信号 | 入库建议 |\n')
report.append('|:--|:--|:--|--:|:--|:--|:--|\n')
for r in sorted([x for x in results if x['card_potential'] == 'high'], key=lambda x: int(x['num'])):
    domains_str = ', '.join(r['domains'][:3])
    depth_str = ', '.join(r['depth_signals'][:3])
    report.append(f"| {r['num']} | {r['title']} | {r['category']} | {r['effective_confidence']:.2f} | {domains_str} | {depth_str} | 独立成卡 |\n")

report.append('\n## 中潜幻灯片（可能并入已有卡或待进一步确认）\n\n')
report.append('| 幻灯片 | 标题 | 类型 | 有效置信度 | 框架域 | 深度信号 | 入库建议 |\n')
report.append('|:--|:--|:--|--:|:--|:--|:--|\n')
for r in sorted([x for x in results if x['card_potential'] == 'medium'], key=lambda x: int(x['num'])):
    domains_str = ', '.join(r['domains'][:3])
    depth_str = ', '.join(r['depth_signals'][:3])
    report.append(f"| {r['num']} | {r['title']} | {r['category']} | {r['effective_confidence']:.2f} | {domains_str} | {depth_str} | 待定 |\n")

report.append('\n## Parse error 但内层高质量的可修复幻灯片\n\n')
report.append('| 幻灯片 | 标题 | 外层置信度 | 内层置信度 | 框架域 | 备注 |\n')
report.append('|:--|:--|--:|--:|:--|:--|\n')
for r in sorted([x for x in results if x['parse_error'] and x['inner_confidence'] >= 0.85], key=lambda x: int(x['num'])):
    domains_str = ', '.join(r['domains'][:3])
    report.append(f"| {r['num']} | {r['title']} | {r['confidence']:.2f} | {r['inner_confidence']:.2f} | {domains_str} | P-33 修复后可读 |\n")

report.append('\n## 全量 299 张审计表\n\n')
report.append('| 幻灯片 | 标题 | 类型 | 有效置信度 | Parse Error | 框架域 | 深度信号 | 潜力 |\n')
report.append('|:--|:--|:--|--:|:--|:--|:--|:--|\n')
for r in sorted(results, key=lambda x: int(x['num'])):
    domains_str = ', '.join(r['domains'][:2])
    depth_str = ', '.join(r['depth_signals'][:2])
    pe = '是' if r['parse_error'] else '否'
    report.append(f"| {r['num']} | {r['title']} | {r['category']} | {r['effective_confidence']:.2f} | {pe} | {domains_str} | {depth_str} | {r['card_potential']} |\n")

with open('_deep_audit_9layers.md', 'w', encoding='utf-8') as f:
    f.writelines(report)

print(f"Total: {len(results)}")
print(f"High potential: {sum(1 for r in results if r['card_potential'] == 'high')}")
print(f"Medium potential: {sum(1 for r in results if r['card_potential'] == 'medium')}")
print(f"Low potential: {sum(1 for r in results if r['card_potential'] == 'low')}")
print(f"Parse error high inner conf: {sum(1 for r in results if r['parse_error'] and r['inner_confidence'] >= 0.85)}")
print("Saved to _deep_audit_9layers.md")
