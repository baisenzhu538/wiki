#!/usr/bin/env python3
"""Batch add Chinese aliases to KDO cards. Generates aliases from title, source_person, and source_refs."""
import os, re, sys

WIKI = "/mnt/c/Users/Administrator/Desktop/wiki/30_wiki"

def extract_frontmatter(text):
    text = text.lstrip('\ufeff')
    lines = text.split('\n')
    if not lines or lines[0].strip() != '---':
        return None, text, None
    fm_lines = []
    end_idx = None
    for i, line in enumerate(lines[1:], 1):
        if line.strip() == '---':
            end_idx = i
            break
        fm_lines.append(line)
    if end_idx is None:
        return None, text, None
    body = '\n'.join(lines[end_idx+1:])
    return fm_lines, body, end_idx

def has_aliases(fm_lines):
    for line in fm_lines:
        if line.startswith('aliases:'):
            after = line.split(':', 1)[1].strip()
            if after and after != '[]':
                return True
    return False

def get_field(fm_lines, field):
    for line in fm_lines:
        if line.startswith(f'{field}:'):
            val = line.split(':', 1)[1].strip().strip('"').strip("'")
            return val
    return None

def get_source_names(fm_lines):
    """Extract meaningful source names from source_refs."""
    names = set()
    for line in fm_lines:
        if line.startswith('source_refs:'):
            continue
        if line.startswith('  - '):
            src = line.strip()[4:]
            # Extract filename-like parts
            for part in src.split('/'):
                part = part.replace('.md', '').replace('.txt', '').replace('.png', '')
                # If has Chinese characters, keep short phrases
                chinese_only = re.findall(r'[\u4e00-\u9fff]+', part)
                if chinese_only:
                    for c in chinese_only:
                        if 3 <= len(c) <= 15:
                            names.add(c)
    return names

def smart_chinese_phrases(text):
    """Extract meaningful Chinese phrases from text, avoiding junk substrings."""
    if not text:
        return []
    # Remove markdown, punctuation, English
    clean = text.strip().strip('#').strip()
    clean = re.sub(r'[「」""''\[\]（）()]', '', clean)
    
    phrases = []
    
    # Strategy 1: Split on common delimiters to get phrases
    parts = re.split(r'[·\-—、，,\s:：]+', clean)
    for p in parts:
        p = p.strip()
        # Must have Chinese chars, no standalone English single words
        ch = re.findall(r'[\u4e00-\u9fff]', p)
        if len(ch) >= 2:
            # Remove trailing junk like "v4" "2.0"
            p = re.sub(r'\s*[vV]\d+(\.\d+)*\s*$', '', p)
            p = re.sub(r'\s*\([^)]*\)\s*$', '', p).strip()
            if 2 <= len(p) <= 25:
                phrases.append(p)
    
    # Strategy 2: Full title as one alias (cleaned)
    full = re.sub(r'[·\-—\s]+', '', clean)
    full_cn = re.findall(r'[\u4e00-\u9fff]', full)
    if len(full_cn) >= 3 and len(full) <= 40 and full not in phrases:
        phrases.insert(0, full)
    
    return phrases

def generate_aliases(title, source_person, fm_lines):
    aliases = []
    seen = set()
    
    # From title
    if title:
        for p in smart_chinese_phrases(title):
            if p not in seen and len(p) >= 2:
                aliases.append(p)
                seen.add(p)
    
    # From source person (if specific, not "一堂"/"pending")
    if source_person and source_person not in ('待查', 'pending', 'unknown', '一堂', '待审', 'pending_archive'):
        # If source_person has Chinese like "崔磊" or "Truman"
        if source_person not in seen:
            aliases.append(source_person)
            seen.add(source_person)
    
    # From source_refs filenames (important for search like "创新者的窘境")
    for n in get_source_names(fm_lines):
        if n not in seen and len(n) >= 2:
            aliases.append(n)
            seen.add(n)
    
    # Deduplicate and limit
    return aliases[:6]

def find_insert_point(fm_lines):
    """Find where to insert aliases: after the last metadata field before body content."""
    # We want aliases near the end of frontmatter, before ---
    # Look for the line after 'related:' block or similar
    for i in range(len(fm_lines)-1, -1, -1):
        line = fm_lines[i].strip()
        if line.startswith('related:') or line.startswith('tags:') or line.startswith('diagnostic_signals:'):
            # Skip the block
            j = i + 1
            while j < len(fm_lines) and fm_lines[j].startswith(('  ', '\t', ' -')):
                j += 1
            return j
    # Insert at end of frontmatter
    return len(fm_lines)

def process_file(filepath):
    # Try multiple encodings
    text = None
    for enc in ['utf-8-sig', 'utf-8', 'gbk', 'gb2312', 'latin-1']:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                text = f.read()
            break
        except (UnicodeDecodeError, UnicodeError):
            continue
    if text is None:
        return None, f"encoding error"
    
    fm_lines, body, end_idx = extract_frontmatter(text)
    if fm_lines is None:
        return None, "no frontmatter"
    
    if has_aliases(fm_lines):
        return None, "has aliases"
    
    title = get_field(fm_lines, 'title')
    source_person = get_field(fm_lines, 'source_person')
    
    aliases = generate_aliases(title, source_person, fm_lines)
    if not aliases:
        return None, "no alias generated"
    
    insert_idx = find_insert_point(fm_lines)
    
    alias_yaml = "aliases:\n" + '\n'.join(f"  - {a}" for a in aliases) + '\n'
    fm_lines.insert(insert_idx, alias_yaml.rstrip('\n'))
    
    new_text = '---\n' + '\n'.join(fm_lines) + '\n---\n' + body
    return new_text, aliases

def main():
    if len(sys.argv) < 2:
        print("Usage: python add_aliases.py <dir> [limit] [--dry]")
        sys.exit(1)
    
    target_dir = sys.argv[1]
    limit = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 100
    dry_run = '--dry' in sys.argv
    dirpath = os.path.join(WIKI, target_dir)
    
    files = sorted([os.path.join(dirpath, f) for f in os.listdir(dirpath) if f.endswith('.md')])
    print(f"{target_dir}/: {len(files)} files, processing up to {limit}")
    
    processed = 0
    skipped_has = 0
    skipped_noalias = 0
    results = []
    
    for filepath in files[:limit]:
        result, info = process_file(filepath)
        if result:
            if not dry_run:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(result)
            processed += 1
            results.append((os.path.basename(filepath), info))
        elif info == "has aliases":
            skipped_has += 1
        else:
            skipped_noalias += 1
    
    print(f"\nProcessed: {processed} | Has aliases: {skipped_has} | No alias: {skipped_noalias}")
    for name, aliases in results[:15]:
        alias_str = ', '.join(aliases[:4])
        print(f"  {name}: [{alias_str}]")
    if len(results) > 15:
        print(f"  ... +{len(results)-15} more")
    
    if dry_run:
        print("\n*** DRY RUN — no files modified ***")

if __name__ == '__main__':
    main()
