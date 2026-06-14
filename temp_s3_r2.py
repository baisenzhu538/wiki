import yaml
from pathlib import Path

root = Path('C:/Users/Administrator/Desktop/wiki/30_wiki')
card_dirs = ['concepts','frameworks','tools','cases','dark-knowledges','entities','decisions','systems','projects']

PERSON_RULES = {
    'truman': ['yitang', 'ai-collaboration'],
    '纪浩': ['ai-collaboration'],
    '马易': ['ai-saas', 'ai-collaboration'],
    '水水': ['master', 'ai-collaboration'],
    '李诞': ['personal-growth'],
    '月白': ['design'],
}

KW_MAP = [
    (['ai-','llm','prompt','AIGC','aigc','agent','算法','模型训练','AI','gpt'], ['ai-saas']),
    (['design','设计','电商','PS','像素','PPT','海报','印刷','DPI','薅羊毛','口喷式'], ['design']),
    (['healthcare','HIS','医院','诊所','药柜','医疗','药房','医保'], ['healthcare']),
    (['management','管理','团队','领导','组织','协作','会议','招聘','OKR'], ['management']),
    (['decision','决策','判断','选择'], ['decision-making']),
    (['business','商业','创业','营销','销售','品牌','渠道','GMV','增长','获客','SaaS','电商'], ['business-strategy']),
    (['product','产品','内核','假设','验证','MVP','迭代','需求','用户','UX'], ['product']),
    (['master','元认知','系统思维','第一性原理','批判性','反脆弱','思维模型'], ['master']),
    (['finance','财务','税务','合规','法务','合同','股权','融资'], ['finance-legal']),
    (['supply','供应链','物流','仓储','采购','配送'], ['supply-chain']),
    (['entrepreneur','创业','startup','孵化','天使'], ['entrepreneurship']),
    (['personal','个人','成长','修炼','表达','学习','认知','思考','心法','阅读'], ['personal-growth']),
    (['ocr-'], ['needs-review']),
]

def infer_domain(name, body, path_rel):
    combined = (name + ' ' + body[:500] + ' ' + path_rel).lower()
    domains = []
    for person, dms in PERSON_RULES.items():
        if person in combined:
            domains.extend(dms)
    if 'decisions' in path_rel or 'systems' in path_rel or 'projects' in path_rel:
        domains.append('kdo')
    if 'plan_2026' in name or 'proposal-' in name or 'improvement-plan' in name:
        domains.append('kdo')
    if 'kdo-' in name or 'kdo_' in name:
        domains.append('kdo')
    if 'skill-' in name.lower():
        domains.append('yitang')
    for keywords, dms in KW_MAP:
        for kw in keywords:
            if kw.lower() in combined:
                domains.extend(dms)
                break
    if not domains:
        domains = ['needs-review']
    return list(set(domains))

fixed = 0
for sub in card_dirs:
    d = root / sub
    if not d.is_dir(): continue
    for f in sorted(d.glob('*.md')):
        if f.name in ('index.md','log.md','contradictions.md'): continue
        try: c = f.read_text(encoding='utf-8')
        except: continue
        if not c.startswith('---'): continue
        end = c.find('---', 3)
        if end == -1: continue
        fm_raw = c[3:end]
        try: fm = yaml.safe_load(fm_raw)
        except: continue
        if not fm or not isinstance(fm, dict): continue
        domain = fm.get('domain')
        if domain and domain != [] and domain != '' and (isinstance(domain, list) and any(str(d).strip() for d in domain)):
            continue

        body = c[end+3:]
        rel_path = str(f.relative_to(root))
        inferred = infer_domain(f.stem, body, rel_path)

        new_lines = []
        inserted = False
        for line in fm_raw.split('\n'):
            lstripped = line.strip()
            if not inserted and lstripped.startswith('domain:'):
                indent = ' ' * (len(line) - len(line.lstrip()))
                new_lines.append(f'{indent}domain:')
                for dm in inferred:
                    new_lines.append(f'{indent}  - {dm}')
                inserted = True
            elif inserted and (lstripped.startswith('- ') or lstripped.startswith('  - ')):
                continue
            else:
                new_lines.append(line)
                if not inserted and (lstripped.startswith('type:') or lstripped.startswith('status:')):
                    indent = ' ' * (len(line) - len(line.lstrip()))
                    new_lines.append(f'{indent}domain:')
                    for dm in inferred:
                        new_lines.append(f'{indent}  - {dm}')
                    inserted = True

        if not inserted:
            new_lines.insert(1, 'domain:')
            for dm in reversed(inferred):
                new_lines.insert(2, f'  - {dm}')

        new_fm = '\n'.join(new_lines)
        new_c = '---\n' + new_fm + c[end:]
        f.write_text(new_c, encoding='utf-8')
        fixed += 1

print(f'Round 2 fixed: {fixed} cards')
