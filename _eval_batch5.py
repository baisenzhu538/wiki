import os, re, sys, glob

sys.stdout.reconfigure(encoding='utf-8')

wiki = r'C:\Users\Administrator\Desktop\wiki\30_wiki\concepts'
files = sorted(glob.glob(os.path.join(wiki, 'ocr-*.md')))

# Cards known to be in Batch 1-4 (already reviewed/refined)
done_cards = {
    # Batch 1 (5)
    'ocr-泛产品设计落地篇', 'ocr-预判模型',
    'ocr-一堂-个人修炼-全景图muse模型', 'ocr-一堂-个人修炼-科学学习ipo-全景策略',
    'ocr-一堂-个人修炼-表达力火箭模型-执行武器库',
    # Batch 4 手写 (7)
    'ocr-一堂y模型-科学成事道理', 'ocr-一堂y模型实操工作流',
    # Batch 4 批量模板 (8)
    'ocr-一堂-地图-个人地图', 'ocr-一堂-地图-创业地图', 'ocr-一堂-地图-管理地图',
    'ocr-一堂进步大地图', 'ocr-一堂个人地图高潜力成长者修炼全景图',
    'ocr-一堂泛产品设计-十年修炼爬山地图', 'ocr-一堂泛产品设计36计-全套地图',
    'ocr-萃取总结',
}
# Batch 2+3 = 科学决策 domain - all have been refined with diverse attackers
# We'll detect these by checking if they have non-Kahneman attackers

# Variant files (not main cards)
variants = {}

batch5 = []
batch5_with_kahneman_only = []
batch5_no_va = []
batch5_small_content = []
batch5_likely_junk = []

for f in files:
    name = os.path.splitext(os.path.basename(f))[0]

    # Skip variant files
    if name.endswith('_conv') or name.endswith('_compressed'):
        base = name.replace('_conv', '').replace('_compressed', '')
        variants.setdefault(base, []).append(name)
        continue

    # Skip known done cards
    if name in done_cards:
        continue

    content = open(f, 'r', encoding='utf-8', errors='replace').read()
    body = content.split('---', 2)[2] if content.startswith('---') else content

    # Check for Kahneman
    has_kahneman = 'Kahneman' in content
    has_simon = 'Simon' in content
    has_new_attackers = any(x in content for x in ['Bowker', 'Langlois', 'Dewey', 'Schön', 'Sontag',
                                                     'Popper', 'Christensen', 'Mintzberg', 'Snowden',
                                                     'Klein', 'Gigerenzer', 'Thaler', 'Sterman',
                                                     'March', 'Orwell', 'Dennett', 'Postman', 'Pye',
                                                     'Duke', 'Morozov', 'Hogarth', 'Tetlock',
                                                     'Norman', 'Papert', 'Page', 'Meehl', 'Sen'])

    # Check for Visual Analysis
    has_va = '## Visual Analysis' in content

    # Check content size (condense section)
    condense_match = re.search(r'## (?:Condense|Reusable Knowledge)(.*?)(?=^## |\Z)', body, re.DOTALL | re.MULTILINE)
    condense_words = len(condense_match.group(1).split()) if condense_match else 0

    # Check if Critique is substantive
    crit_match = re.search(r'## Critique(.*?)(?=^## |\Z)', body, re.DOTALL | re.MULTILINE)
    crit_words = len(crit_match.group(1).split()) if crit_match else 0

    attacks = re.findall(r'#### (.+)', body)

    info = {
        'name': name,
        'has_kahneman': has_kahneman,
        'has_simon': has_simon,
        'has_new_attackers': has_new_attackers,
        'has_va': has_va,
        'condense_words': condense_words,
        'crit_words': crit_words,
        'attacks': [a.split('—')[0].strip()[:25] for a in attacks],
    }

    # Domain classification
    if '科学决策' in name or name.startswith('ocr-一堂-科学决策'):
        info['domain'] = '科学决策'
    elif '泛产品设计' in name and ('落地' in name or '用户' in name or '审美' in name):
        info['domain'] = '泛产品设计-子卡'
    elif '个人修炼' in name:
        info['domain'] = '个人修炼'
    elif '课程清单' in name:
        info['domain'] = '课程清单'
    elif name.startswith('ocr-truman'):
        info['domain'] = 'Truman'
    elif name.startswith('ocr-一堂-'):
        info['domain'] = '一堂其他'
    elif name.startswith('ocr-泛产品设计'):
        info['domain'] = '泛产品设计'
    elif name.startswith('ocr-项目'):
        info['domain'] = '项目方法'
    else:
        info['domain'] = '其他'

    batch5.append(info)

# Add variant info
for info in batch5:
    if info['name'] in variants:
        info['variants'] = variants[info['name']]

# Sort by domain then name
batch5.sort(key=lambda x: (x['domain'], x['name']))

print(f'Batch 5 candidates (not in Batch 1-4): {len(batch5)}')
print()

# Summary by domain
from collections import Counter
domain_counts = Counter(i['domain'] for i in batch5)
print('=== Domain distribution ===')
for d, c in domain_counts.most_common():
    print(f'  {d}: {c}')
print()

# Cards with Kahneman still
print(f'=== Still have Kahneman: {sum(1 for i in batch5 if i["has_kahneman"])} ===')
for i in batch5:
    if i['has_kahneman']:
        print(f'  {i["name"]}  domain={i["domain"]}  attacks={i["attacks"]}')

print()
print(f'=== Have new attackers (likely Batch 2+3 refined): {sum(1 for i in batch5 if i["has_new_attackers"])} ===')
for i in batch5:
    if i['has_new_attackers'] and not i['has_kahneman']:
        print(f'  {i["name"]}  attacks={i["attacks"]}')

print()
print(f'=== No new attackers, no Kahneman: {sum(1 for i in batch5 if not i["has_new_attackers"] and not i["has_kahneman"])} ===')
for i in batch5:
    if not i['has_new_attackers'] and not i['has_kahneman']:
        print(f'  {i["name"]}  domain={i["domain"]}  condense={i["condense_words"]}w  crit={i["crit_words"]}w')

print()
print(f'=== Has VA: {sum(1 for i in batch5 if i["has_va"])} ===')
print(f'=== No VA: {sum(1 for i in batch5 if not i["has_va"])} ===')

print()
print('=== Small condense (< 30 words, likely OCR junk) ===')
for i in batch5:
    if i['condense_words'] < 30:
        print(f'  {i["name"]}  condense={i["condense_words"]}w  crit={i["crit_words"]}w  domain={i["domain"]}')
