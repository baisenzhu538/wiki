import json, sys, re

def blocks_to_md(src, out, doc_title):
    with open(src, encoding='utf-8') as f:
        blocks = json.load(f)
    lines = [f"# {doc_title}", ""]
    for b in blocks:
        t = b['text'].strip()
        t = t.replace('\u200b', '').replace('\u00a0', ' ')
        if not t:
            continue
        typ = b['type']
        if typ == 'page':
            continue
        elif re.match(r'heading(\d+)', typ):
            lvl = int(re.match(r'heading(\d+)', typ).group(1))
            lines.append('#' * min(lvl + 1, 6) + ' ' + t)
            lines.append('')
        elif typ == 'bullet':
            lines.append('- ' + t)
        elif typ == 'ordered':
            lines.append('1. ' + t)
        elif typ == 'code':
            lines.append('```')
            lines.append(t)
            lines.append('```')
            lines.append('')
        elif typ == 'quote':
            lines.append('> ' + t)
            lines.append('')
        elif typ == 'divider':
            lines.append('---')
            lines.append('')
        else:
            lines.append(t)
            lines.append('')
    md = '\n'.join(lines)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(md)
    print(f"blocks={len(blocks)} chars={len(md)} saved={out}")
    print("---- HEAD ----")
    print(md[:600])
    print("---- TAIL ----")
    print(md[-600:])

if __name__ == '__main__':
    blocks_to_md(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "逐字稿")
