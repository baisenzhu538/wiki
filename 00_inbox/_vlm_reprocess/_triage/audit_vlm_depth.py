import os, re, glob
from collections import defaultdict

base='00_inbox/_vlm_reprocess'
wiki='30_wiki'

vlm_map={}
for root,dirs,files in os.walk(base):
    for f in files:
        if f.endswith('_vlm_desc.md'):
            stem=f[:-len('_vlm_desc.md')]
            vlm_map[stem]=os.path.join(root,f)

wiki_map={}
for root,dirs,files in os.walk(wiki):
    for f in files:
        if f.endswith('.md'):
            stem=f[:-3]
            wiki_map[stem]=os.path.join(root,f)

triage_path=os.path.join(base,'_triage','vlm_framework_value_triage.md')
with open(triage_path,'r',encoding='utf-8') as fh:
    triage=fh.read()

sections = re.split(r'\n##\s+', triage)
rows=[]
current_domain=''
for sec in sections:
    if not sec.strip():
        continue
    lines=sec.splitlines()
    header=lines[0].strip()
    in_table=False
    for line in lines:
        if line.startswith('| 文件名'):
            in_table=True
            continue
        if in_table and line.startswith('|'):
            if re.match(r'\|\s*[:-]+\s*\|', line):
                continue
            cells=[c.strip() for c in line.strip('|').split('|')]
            if len(cells)>=4:
                rows.append({
                    'domain': current_domain,
                    'filename': cells[0],
                    'title': cells[1],
                    'action': cells[2],
                    'target': cells[3]
                })
        else:
            in_table=False
    if not any(line.startswith('| 文件名') for line in lines):
        current_domain=header

relevant_actions={'new-framework','new-tool','new-concept','new-dk','case','dk','enrich','enrich-case','new_or_enrich','review'}
records=[r for r in rows if any(a in r['action'] for a in relevant_actions)]

fail_keywords=['失败模式','失效模式','反例','常见错误','典型错误','错误','坑','陷阱','误区','注意事项']
step_keywords=['步骤','流程','SOP','检查单','checklist','操作','怎么做','用法','方法','执行','清单','提问清单','验证清单','模板']
dark_keywords=['暗知识','坑','口诀','心法','教训','血泪','注意','容易','往往','其实','盲区','隐藏','没人说','直觉','惯性','潜意识']
num_pattern=re.compile(r'\d+(?:\.\d+)?[%％]?|第[一二三四五]|十倍|[百千万亿]|元|倍|成|百分之')

def has_long_paragraph(text,min_len=200):
    body=re.sub(r'^---\s*\n.*?\n---\s*\n','',text,flags=re.S)
    paras=re.split(r'\n\s*\n', body)
    for p in paras:
        p=re.sub(r'!\[.*?\]\(.*?\)','',p)
        p=re.sub(r'\[.*?\]','',p)
        p=re.sub(r'[#*|`\-]','',p)
        txt=p.replace(' ','').replace('\n','')
        if len(txt)>=min_len:
            return True
    return False

def check_vlm(path):
    with open(path,'r',encoding='utf-8') as fh:
        text=fh.read()
    checks={}
    checks['has_failure_mode']=any(k in text for k in fail_keywords)
    checks['has_operational_steps']=any(k in text for k in step_keywords)
    checks['has_numbers']=bool(num_pattern.search(text))
    checks['has_dark_markers']=any(k in text for k in dark_keywords)
    checks['has_long_paragraph']=has_long_paragraph(text)
    title=''
    m=re.search(r'"title"\s*:\s*"([^"]+)"', text)
    if m:
        title=m.group(1)
    conf=''
    m=re.search(r'"confidence"\s*:\s*([0-9.]+)', text)
    if m:
        conf=m.group(1)
    return text, checks, title, conf

counts={'total':0,'missing_failure':0,'missing_steps':0,'missing_numbers':0,'missing_dark':0,'missing_long_para':0,'enrich_new_topic':0}
missed=[]

for r in records:
    counts['total']+=1
    stem=r['filename']
    vlm_path=vlm_map.get(stem)
    if not vlm_path:
        missed.append({**r,'reason':'未找到对应 VLM 描述文件','checks':{}})
        continue
    text, checks, vtitle, conf = check_vlm(vlm_path)
    gaps=[]
    action=r['action']
    is_case = 'case' in action
    is_dk = 'dk' in action
    is_new = action.startswith('new') or 'new-' in action
    is_enrich = 'enrich' in action
    if is_case:
        if not checks['has_long_paragraph']:
            gaps.append('缺少≥200字连续叙事段落')
            counts['missing_long_para']+=1
        if not checks['has_numbers']:
            gaps.append('缺少关键数字/量化证据')
            counts['missing_numbers']+=1
        if not checks['has_failure_mode']:
            gaps.append('缺少失败/成功原因或反例')
            counts['missing_failure']+=1
    if is_dk or is_new:
        if not checks['has_failure_mode']:
            gaps.append('缺少失败模式/边界/反例')
            counts['missing_failure']+=1
        if not checks['has_operational_steps']:
            gaps.append('缺少操作步骤/SOP/检查单')
            counts['missing_steps']+=1
        if not checks['has_dark_markers']:
            gaps.append('缺少暗知识/教训/心法标记')
            counts['missing_dark']+=1
    if is_enrich:
        target_stem = r['target'].split('（')[0].strip()
        wiki_path=wiki_map.get(target_stem)
        new_topic=False
        if wiki_path and vtitle:
            with open(wiki_path,'r',encoding='utf-8') as fh:
                wiki_text=fh.read()
            key_terms=[]
            for w in re.findall(r'[\u4e00-\u9fa5]{2,}', vtitle):
                if w not in ['模型','框架','工具','方法','概念','案例','分析']:
                    key_terms.append(w)
            for w in key_terms[:5]:
                if w and w not in wiki_text:
                    new_topic=True
                    break
        if new_topic:
            gaps.append('VLM标题含目标卡片未覆盖的新主题')
            counts['enrich_new_topic']+=1
    if gaps:
        missed.append({**r,'reason':'；'.join(gaps),'checks':checks,'vlm_path':vlm_path,'vlm_conf':conf,'vlm_title':vtitle})

report=[]
report.append('---')
report.append('id: diag_20260625_wangyuyan_vlm-missed-knowledge')
report.append('type: diagnosis')
report.append('created_at: 2026-06-25')
report.append('author: 王语嫣')
report.append('scope: 00_inbox/_vlm_reprocess 结构化 VLM 描述 vs 成品卡所需深度')
report.append('---')
report.append('')
report.append('# VLM 重提取深度诊断：被遗漏的重要知识点')
report.append('')
report.append('> 王语嫣铁律：本报告只写入 `60_feedback/`，不污染 `30_wiki/`。')
report.append('> 目的：用洪七公已产出的结构化 VLM 描述反查上一轮 prompt 漏掉了哪些关键知识要素，并标注给老顽童补挖。')
report.append('')
report.append('## 1. 诊断方法')
report.append('')
report.append('- 扫描范围：`vlm_framework_value_triage.md` 中标注为 `new-* / case / dk / enrich / new_or_enrich / review` 的卡片。')
report.append('- 漏挖判定：对每条 VLM 描述检查是否包含以下要素：')
report.append('  - 失败模式/反例/边界（`失败模式/反例/坑/陷阱/误区`等）')
report.append('  - 操作步骤/SOP/检查单（`步骤/流程/SOP/检查单/清单`等）')
report.append('  - 关键数字/比例/量化证据（数字、`%`、倍数、金额等）')
report.append('  - 暗知识/教训/心法标记（`暗知识/口诀/心法/教训/盲区`等）')
report.append('  - 案例叙事段落长度（≥200 字连续叙事）')
report.append('- `enrich` 类额外对比已有 wiki 卡片标题，若 VLM 描述中出现明显新主题而目标卡片未覆盖，也列为漏挖。')
report.append('')
report.append('## 2. 总体发现')
report.append('')
report.append(f'- 检查卡片总数：**{counts["total"]}**')
report.append(f'- 存在明显漏挖的卡片：**{len(missed)}**')
report.append(f'- 缺少失败/边界/反例：**{counts["missing_failure"]}**')
report.append(f'- 缺少操作步骤/SOP：**{counts["missing_steps"]}**')
report.append(f'- 缺少关键数字：**{counts["missing_numbers"]}**')
report.append(f'- 缺少暗知识/教训标记：**{counts["missing_dark"]}**')
report.append(f'- 案例卡缺少≥200字叙事：**{counts["missing_long_para"]}**')
report.append(f'- enrich 目标卡片未覆盖新主题：**{counts["enrich_new_topic"]}**')
report.append('')
report.append('## 3. 需老顽童重点补挖的卡片清单')
report.append('')
report.append('| 域 | 文件名 | 建议动作 | 目标卡片 | 漏挖要素 | VLM 文件 |')
report.append('|:---|:---|:---:|:---|:---|:---|')
for m in missed:
    reason=m['reason'].replace('|','\\|')
    report.append(f"| {m['domain']} | {m['filename']} | {m['action']} | {m['target']} | {reason} | `{m.get('vlm_path','')}` |")
report.append('')
report.append('## 4. 按域重点说明')
report.append('')

domain_groups=defaultdict(list)
for m in missed:
    domain_groups[m['domain']].append(m)

for dom in ['单元模型','科学决策','泛产品设计','个人修炼','其他']:
    if dom not in domain_groups:
        continue
    report.append(f'### {dom}')
    report.append('')
    for m in domain_groups[dom][:40]:
        report.append(f"**{m['filename']}** → `{m['target']}`")
        report.append(f"- 建议动作：{m['action']}")
        report.append(f"- 漏挖：{m['reason']}")
        text=open(m['vlm_path'],'r',encoding='utf-8').read() if m.get('vlm_path') else ''
        body=re.sub(r'^---\s*\n.*?\n---\s*\n','',text,flags=re.S)
        snippet=re.sub(r'[#*|\-`\n]',' ',body).strip()
        snippet=snippet[:120]+'……' if len(snippet)>120 else snippet
        report.append(f"- VLM 片段：{snippet}")
        report.append('')

report.append('## 5. 给老顽童的补挖指令')
report.append('')
report.append('对上述清单中的卡片，老顽童在生产成品卡时必须：**不能仅依赖 VLM 描述**，必须回看原图 + OCR 文本，重点补挖以下要素：')
report.append('')
report.append('1. **失败模式/边界/反例**：每个 framework/tool/concept/dk 卡至少补 3 条失败模式或边界条件。')
report.append('2. **操作步骤/SOP/检查单**：把图中隐含的“怎么做”显式化为可执行的步骤或清单。')
report.append('3. **关键数字与证据**：案例卡必须提取具体数字、比例、金额、时间；非案例卡提取图中给出的量化指标或阈值。')
report.append('4. **暗知识/心法/口诀**：把讲师随口提到的判断口诀、失败教训、避坑经验单独标注为 `dk` 候选。')
report.append('5. **叙事段落扫描**：案例卡必须定位 ≥200 字连续叙事段落，完整度评分 ≥4 分方可立项。')
report.append('')
report.append('补挖结果应在成品卡 `source_refs` 中同时注明 VLM 描述文件 + 原图路径，并在正文中对补挖内容标注 `[conf=0.80, source=原图/OCR]`。')
report.append('')
report.append('---')
report.append('*诊断人：王语嫣 | 日期：2026-06-25*')

out_path='60_feedback/diagnosis/diag_20260625_wangyuyan_vlm-missed-knowledge.md'
with open(out_path,'w',encoding='utf-8') as fh:
    fh.write('\n'.join(report))
print('wrote', out_path, 'lines', len(report))
print('missed', len(missed), 'of', counts['total'])
