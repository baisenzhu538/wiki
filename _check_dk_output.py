import json
root = r'C:\Users\Administrator\Desktop\wiki\60_feedback\data-quality\dk-candidates'
files = [
    'AI设计-AI设计基础01-dk-candidates.json',
    'AI设计-AI设计师实操培训01-dk-candidates.json',
    'AI设计-文创案例设计课口述-dk-candidates.json',
]
for f in files:
    path = f'{root}\\{f}'
    with open(path, 'r', encoding='utf-8') as fh:
        data = json.load(fh)
    count = len(data)
    has_scores = sum(1 for d in data if d.get('score', 0) > 0)
    has_ops = sum(1 for d in data if '[OPERATION_NEEDS_HUMAN]' not in str(d.get('操作步骤草稿', '')))
    print(f'{f}: {count} candidates, {has_scores} with scores, {has_ops} with ops')
    for d in sorted(data, key=lambda x: x.get('score', 0), reverse=True)[:3]:
        title = d.get('title', '?')[:50]
        score = d.get('score', 0)
        dk_type = d.get('dk_type', '?')
        print(f'  [{dk_type}] {title} score={score:.2f}')
