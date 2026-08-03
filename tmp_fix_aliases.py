#!/usr/bin/env python3
"""Fix dual aliases: merge multiple aliases blocks into one, add missing aliases."""
import os, re, sys, yaml

WIKI = "/mnt/c/Users/Administrator/Desktop/wiki/30_wiki"
DIRS = ["tools", "concepts", "dark-knowledges", "dk", "cases"]

def read_file_raw(filepath):
    for enc in ['utf-8-sig', 'utf-8', 'gbk', 'latin-1']:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                return f.read(), enc
        except:
            continue
    return None, None

def split_frontmatter(text):
    """Split into (pre_fm, fm_yaml_str, body). Handles --- boundaries."""
    text = text.lstrip('\ufeff')
    # Find first ---
    first = text.find('---')
    if first == -1:
        return None, None, None
    # Find second ---
    start = first + 3
    second = text.find('---', start)
    if second == -1:
        return None, None, None
    fm_str = text[start:second].strip()
    body = text[second + 3:]
    return fm_str, body

def merge_aliases_in_fm(fm_str):
    """Parse frontmatter as raw lines, merge all aliases entries."""
    lines = fm_str.split('\n')
    result = []
    all_aliases = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if re.match(r'^aliases:', line):
            # Check if inline: "aliases: [a, b]" or multi-line
            inline_val = line.split(':', 1)[1].strip()
            if inline_val and inline_val not in ('', '[]'):
                # Inline list
                if inline_val.startswith('[') and inline_val.endswith(']'):
                    vals = [v.strip().strip('"').strip("'") for v in inline_val[1:-1].split(',') if v.strip()]
                    all_aliases.extend(vals)
                else:
                    all_aliases.append(inline_val)
                i += 1
                # Skip any continuation lines (indented list items)
                while i < len(lines) and (lines[i].startswith('  -') or lines[i].startswith('  #') or lines[i].strip() == ''):
                    if lines[i].startswith('  -'):
                        val = lines[i].strip()[2:].strip().strip('"').strip("'")
                        if val:
                            all_aliases.append(val)
                    i += 1
            else:
                # Multi-line: "aliases:\n  - a\n  - b"
                i += 1
                while i < len(lines) and (lines[i].startswith('  -') or lines[i].startswith('  #')):
                    if lines[i].startswith('  -'):
                        val = lines[i].strip()[2:].strip().strip('"').strip("'")
                        if val:
                            all_aliases.append(val)
                    i += 1
        else:
            result.append(line)
            i += 1
    
    # Deduplicate while preserving order
    seen = set()
    unique = []
    for a in all_aliases:
        if a not in seen:
            seen.add(a)
            unique.append(a)
    
    # Insert single aliases block before the first non-aliases key after where we removed them
    # Find insertion point: typically before 'related:' or end of frontmatter
    insert_at = len(result)
    for j, line in enumerate(result):
        if line.startswith('related:') or line.startswith('tags:') or line.startswith('quality_labels:'):
            insert_at = j
            break
    
    alias_block = "aliases:\n" + '\n'.join(f"  - {a}" for a in unique)
    if unique:
        result.insert(insert_at, alias_block)
    
    return '\n'.join(result)

def get_missing_aliases_count(filepath):
    text, enc = read_file_raw(filepath)
    if not text:
        return None
    fm_str, body = split_frontmatter(text)
    if fm_str is None:
        return None
    # Check if aliases exists with content
    if not re.search(r'^aliases:', fm_str, re.MULTILINE):
        return True  # missing
    aliases_section = re.findall(r'^aliases:.*(?:\n(?:  -.*\n?)*)?', fm_str, re.MULTILINE)
    for sec in aliases_section:
        if re.search(r'  - ', sec):
            return False  # has content
        inline = sec.split(':', 1)[1].strip()
        if inline and inline != '[]':
            return False
    return True  # has aliases: but empty

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else 'list'
    target_dir = sys.argv[2] if len(sys.argv) > 2 else None
    
    dirs_to_process = [target_dir] if target_dir else DIRS
    
    for d in dirs_to_process:
        dirpath = os.path.join(WIKI, d)
        if not os.path.isdir(dirpath):
            continue
        
        files = sorted([f for f in os.listdir(dirpath) if f.endswith('.md')])
        dual_count = 0
        missing_count = 0
        fixed = 0
        
        for filename in files:
            filepath = os.path.join(dirpath, filename)
            text, enc = read_file_raw(filepath)
            if not text:
                continue
            
            # Count dual aliases
            alias_count = len(re.findall(r'^aliases:', text.split('---')[1] if '---' in text else '', re.MULTILINE))
            
            if alias_count > 1:
                dual_count += 1
                if mode == 'fix':
                    fm_str, body = split_frontmatter(text)
                    if fm_str is None:
                        continue
                    new_fm = merge_aliases_in_fm(fm_str)
                    new_text = '---\n' + new_fm + '\n---' + body
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_text)
                    fixed += 1
                    print(f"  FIXED dual: {d}/{filename} ({alias_count}→1)")
            
            # Count missing
            is_missing = get_missing_aliases_count(filepath)
            if is_missing:
                missing_count += 1
        
        print(f"\n{d}/: total={len(files)} dual={dual_count} missing={missing_count}" + (f" fixed={fixed}" if mode == 'fix' else ''))

if __name__ == '__main__':
    main()
