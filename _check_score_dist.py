import json, os

root = r'C:\Users\Administrator\Desktop\wiki\60_feedback\data-quality\dk-candidates'
files = ['AI设计-AI设计基础01-dk-candidates.json',
         'AI设计-AI设计师实操培训01-dk-candidates.json',
         'AI设计-文创案例设计课口述-dk-candidates.json']

all_scores = []
for f in files:
    path = os.path.join(root, f)
    with open(path, 'r', encoding='utf-8') as fh:
        data = json.load(fh)
    scores = sorted([d.get('score',0) for d in data], reverse=True)
    all_scores.extend(scores)
    print(f'\n{f}:')
    for threshold in [0.80, 0.75, 0.70, 0.65, 0.60]:
        count = sum(1 for s in scores if s >= threshold)
        print(f'  score >= {threshold}: {count} candidates')

print(f'\n=== All 3 files combined ===')
for threshold in [0.85, 0.80, 0.75, 0.70, 0.65, 0.60]:
    count = sum(1 for s in all_scores if s >= threshold)
    print(f'  score >= {threshold}: {count} candidates')
