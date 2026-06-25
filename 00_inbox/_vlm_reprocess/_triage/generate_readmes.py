import json, re
from pathlib import Path

def extract_meta(text):
    # try first json block
    m = re.search(r'```json\s*(.*?)\s*```', text, re.S)
    data = {}
    if m:
        try:
            data = json.loads(m.group(1))
        except Exception:
            pass
    if not data:
        # fallback
        title = re.search(r'"title"\s*:\s*"([^"]*)"', text)
        category = re.search(r'"category"\s*:\s*"([^"]*)"', text)
        confidence = re.search(r'"confidence"\s*:\s*([0-9.]+)', text)
        data = {
            'title': title.group(1) if title else '',
            'category': category.group(1) if category else '',
            'confidence': float(confidence.group(1)) if confidence else 0.0
        }
    return data

for domain in ['单元模型','科学决策','泛产品设计','个人修炼','其他']:
    files = sorted(Path(domain).glob('*_vlm_desc.md'))
    lines = [f'# {domain} - VLM 描述汇总\n']
    lines.append(f'模型: `MiniMax-M3`\n')
    lines.append(f'图片数: {len(files)}')
    lines.append(f'成功: {len(files)}')
    lines.append(f'失败: 0\n')
    lines.append('## 描述清单\n')
    lines.append('| 图片 | 类型 | 标题 | 置信度 | 描述文件 |')
    lines.append('|---|---|---|---|---|')
    for f in files:
        text = f.read_text(encoding='utf-8')
        meta = extract_meta(text)
        img_name = f.stem.replace('_vlm_desc', '')
        # try infer extension from source path in text
        ext = '.png'
        src_m = re.search(r'原图\*:\s*`.*\\([^`]+)`', text)
        if src_m:
            src = src_m.group(1)
            if '.' in src:
                ext = Path(src).suffix
        img_file = img_name + ext
        lines.append(f'| {img_file} | {meta.get("category","")} | {meta.get("title","")} | {meta.get("confidence",0)} | `{f}` |')
    out = Path(domain) / 'README-VLM描述汇总.md'
    out.write_text('\n'.join(lines), encoding='utf-8')
    print('wrote', out)
