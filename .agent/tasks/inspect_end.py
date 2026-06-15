from pathlib import Path
root = Path('C:/Users/Administrator/Desktop/wiki/30_wiki/concepts')
for f in ['yt-decision-ai-partner.md','yt-decision-canvas.md']:
    text = (root / f).read_bytes()
    # find the last row of failure modes table (template/decision) and following bytes
    if 'ai-partner' in f:
        marker = '模板化决策'.encode('utf-8')
    else:
        marker = '过度分析症'.encode('utf-8')
    idx = text.find(marker)
    snippet = text[idx-20:idx+300]
    print('---', f)
    print(repr(snippet))
