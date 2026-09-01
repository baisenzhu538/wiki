# -*- coding: utf-8 -*-
import re
parts = []
for i in [1, 2, 3]:
    with open(f'BV1kp4y1v7p9_p{i}-逐字稿.md', 'r', encoding='utf-8') as f:
        content = f.read()
    # 去掉每个文件的头部（标题/元信息/---），保留时间戳正文
    lines = content.split('\n')
    body_start = 0
    for idx, l in enumerate(lines):
        if l.strip() == '---':
            body_start = idx + 1
            break
    body = '\n'.join(lines[body_start:]).strip()
    parts.append(f'### 第 {i} 部分\n\n{body}')
merged = '# 🎬 大卫·布鲁克斯 TED演讲：当代文化的3个主流谎言——以及更好的生活方式\n\n> 视频逐字稿（faster-whisper-small）| 语言：en | 来源：B站 BV1kp4y1v7p9\n\n---\n\n' + '\n\n'.join(parts)
with open('TED-大卫布鲁克斯-3个主流谎言-逐字稿.md', 'w', encoding='utf-8') as f:
    f.write(merged)
print('MERGED_CHARS:', len(merged))
