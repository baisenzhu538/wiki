from pathlib import Path
import sys
root = Path('C:/Users/Administrator/Desktop/wiki/30_wiki/concepts')
for f in ['yt-decision-ai-partner.md','yt-decision-canvas.md']:
    text = (root / f).read_bytes()
    # find the failure modes table by looking for the heading bytes
    marker = '### 常见失败模式'.encode('utf-8')
    idx = text.find(marker)
    if idx == -1:
        print(f, 'marker not found')
        continue
    snippet = text[idx:idx+900]
    print('---', f)
    print(repr(snippet))
