#!/usr/bin/env python3
"""Batch add discoverable_by to KDO cards from titles."""
import os, re, sys, yaml

WIKI = "/mnt/c/Users/Administrator/Desktop/wiki/30_wiki"

def read_frontmatter(filepath):
    for enc in ['utf-8-sig', 'utf-8', 'gbk', 'latin-1']:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                text = f.read()
            break
        except:
            continue
    else:
        return None, {}
    
    parts = text.split('---', 2)
    if len(parts) < 2:
        return text, {}
    try:
        fm = yaml.safe_load(parts[1])
        return text, fm, parts
    except:
        return text, None, parts

def has_discoverable_by(fm):
    return fm and fm.get('discoverable_by') and len(fm['discoverable_by']) > 0

def smart_discoverable(title_text):
    """Generate discoverable search phrases from title."""
    if not title_text:
        return []
    
    clean = title_text.strip().strip('#').strip()
    # Remove quotes, brackets
    clean = re.sub(r'[「」""''\[\]（）()【】]', '', clean)
    
    phrases = []
    seen = set()
    
    # 1. Full title as one alias
    full_cn = re.sub(r'[^\u4e00-\u9fff]', '', clean)
    if 4 <= len(full_cn) <= 30:
        short = clean[:30].strip()
        if short not in seen:
            phrases.append(short)
            seen.add(short)
    
    # 2. Extract phrases split by meaningful delimiters
    parts = re.split(r'[·\-—\s*]+', clean)
    parts = [p.strip() for p in parts]
    # Also try split by ： or ：
    all_parts = []
    for p in parts:
        sub = re.split(r'[：:]', p)
        all_parts.extend([s.strip() for s in sub if s.strip()])
    
    for p in all_parts:
        p = p.strip().rstrip('，,。.')
        # Must be Chinese-dominant, 3+ chars, not too long
        ch = re.findall(r'[\u4e00-\u9fff]', p)
        en = re.findall(r'[a-zA-Z]', p)
        if len(ch) >= 3 and 3 <= len(p) <= 30 and p not in seen:
            # Filter out connector fragments
            if p not in ('从答案', '到效率', '到作品', '到产品', '到系统', '从新手', '到管理者'):
                phrases.append(p)
                seen.add(p)
    
    return phrases[:5]

def insert_discoverable(text, fm, phrases):
    """Insert discoverable_by into frontmatter."""
    parts = text.split('---', 2)
    if len(parts) < 2:
        return text
    
    fm_str = parts[1]
    body = parts[2] if len(parts) > 2 else ''
    
    # Build discoverable_by YAML
    disc_block = "discoverable_by:\n" + '\n'.join(f"  - {p}" for p in phrases)
    
    # Insert before related: or tags: at the end of frontmatter
    fm_lines = fm_str.rstrip('\n').split('\n')
    
    # Find insertion point
    insert_at = len(fm_lines)
    for j, line in enumerate(fm_lines):
        if line.startswith('related:') or line.startswith('tags:') or line.startswith('quality_labels:'):
            insert_at = j
            break
    
    fm_lines.insert(insert_at, disc_block)
    new_fm = '\n'.join(fm_lines)
    return '---\n' + new_fm + '\n---' + body

def main():
    target_dir = sys.argv[1] if len(sys.argv) > 1 else 'concepts'
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 50
    dry_run = '--dry' in sys.argv
    
    dp = os.path.join(WIKI, target_dir)
    files = sorted([f for f in os.listdir(dp) if f.endswith('.md')])
    
    processed = 0
    skipped_has = 0
    skipped_noalias = 0
    
    for fn in files[:limit]:
        fp = os.path.join(dp, fn)
        text, fm, parts = read_frontmatter(fp)
        
        if fm is None:
            print(f"  SKIP {fn}: YAML broken")
            continue
        
        if has_discoverable_by(fm):
            skipped_has += 1
            continue
        
        title = fm.get('title', fn)
        phrases = smart_discoverable(title)
        
        if not phrases:
            skipped_noalias += 1
            continue
        
        new_text = insert_discoverable(text, fm, phrases)
        
        if not dry_run:
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(new_text)
        
        processed += 1
        if processed <= 15:
            print(f"  {fn}: {phrases[:3]}")
    
    print(f"\n{target_dir}/: total={len(files[:limit])} processed={processed} skipped_has={skipped_has} skipped_nogen={skipped_noalias}")
    if dry_run:
        print("*** DRY RUN ***")

if __name__ == '__main__':
    main()
