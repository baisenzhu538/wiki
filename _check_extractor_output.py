import json, os, sys

root = r'C:\Users\Administrator\Desktop\wiki\60_feedback\data-quality\dk-candidates'
files = ['AI设计-AI设计基础01-dk-candidates.json',
         'AI设计-AI设计师实操培训01-dk-candidates.json',
         'AI设计-文创案例设计课口述-dk-candidates.json']

for f in files:
    path = os.path.join(root, f)
    with open(path, 'r', encoding='utf-8') as fh:
        data = json.load(fh)
    total = len(data)
    with_title = sum(1 for d in data if d.get('title','').strip())
    with_ops = sum(1 for d in data if 'OPERATION_NEEDS_HUMAN' not in str(d.get('operation','')))
    with_boundary = sum(1 for d in data if d.get('boundary','').strip())
    with_why = sum(1 for d in data if d.get('why_valuable','').strip())
    scores = [d.get('score',0) for d in data]
    types = {}
    for d in data:
        t = d.get('dark_knowledge_type','?')
        types[t] = types.get(t,0) + 1

    print(f'\n=== {f} ===')
    print(f'  Total: {total}')
    print(f'  Title rate: {with_title}/{total} = {with_title/total*100:.0f}%')
    print(f'  Operation filled: {with_ops}/{total} = {with_ops/total*100:.0f}%')
    print(f'  Boundary filled: {with_boundary}/{total} = {with_boundary/total*100:.0f}%')
    print(f'  Why_valuable filled: {with_why}/{total} = {with_why/total*100:.0f}%')
    print(f'  Score range: {min(scores):.2f}-{max(scores):.2f}')
    print(f'  Top 5 scores: {sorted(scores, reverse=True)[:5]}')
    print(f'  Types: {types}')

    # Sample top 3 titles
    top = sorted(data, key=lambda x: x.get('score',0), reverse=True)[:3]
    for d in top:
        print(f'    [{d.get("score",0):.2f}] {d.get("title","?")[:60]}')
