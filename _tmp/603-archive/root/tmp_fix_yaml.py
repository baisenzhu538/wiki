#!/usr/bin/env python3
"""Fix YAML frontmatter issues: aliases inserted at wrong positions, encoding issues."""
import os, re, yaml, sys

WIKI = "/mnt/c/Users/Administrator/Desktop/wiki/30_wiki"
DIRS = ["tools", "concepts", "dark-knowledges", "dk", "cases"]

def read_file(filepath):
    for enc in ['utf-8-sig', 'utf-8', 'gbk', 'latin-1']:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                return f.read()
        except:
            continue
    return None

def parse_fm_lines(text):
    """Manually parse frontmatter into key=raw_value pairs, preserving order."""
    text = text.lstrip('\ufeff')
    # Find --- boundaries
    if not text.startswith('---'):
        return None, text, None
    rest = text[3:]
    # Find closing ---
    end = rest.find('\n---')
    if end == -1:
        # Try just --- without leading newline
        end = rest.find('---')
        if end == -1:
            return None, None, None
    fm_text = rest[:end].strip()
    body = rest[end:].lstrip('---').lstrip('\n')
    
    lines = fm_text.split('\n')
    entries = []  # [(key, raw_value_str)]
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        # Check if this is a key: value line
        m = re.match(r'^(\w[\w_-]*):\s*(.*)', line)
        if m:
            key = m.group(1)
            value = m.group(2)
            if value.strip():
                # Inline value
                entries.append((key, value.strip()))
                i += 1
            else:
                # Multi-line: collect indented continuation lines
                raw_lines = []
                i += 1
                while i < len(lines) and (lines[i].startswith('  ') or lines[i].strip() == ''):
                    raw_lines.append(lines[i])
                    i += 1
                entries.append((key, '\n'.join(raw_lines) if raw_lines else ''))
        else:
            i += 1
    return entries, body

def entries_to_yaml(entries):
    """Convert entries list back to YAML string."""
    result = []
    for key, val in entries:
        if not val.strip():
            result.append(f'{key}:')
        elif '\n' in val:
            result.append(f'{key}:')
            for line in val.split('\n'):
                if line.strip():
                    result.append(line)
        else:
            result.append(f'{key}: {val}')
    return '\n'.join(result)

def fix_file(filepath):
    text = read_file(filepath)
    if not text:
        return False, "encoding error"
    
    entries, body = parse_fm_lines(text)
    if entries is None:
        return False, "no frontmatter"
    
    # Check if YAML parses
    yaml_str = entries_to_yaml(entries)
    try:
        yaml.safe_load(yaml_str)
        return False, "already OK"
    except:
        pass
    
    # Try fixing: remove aliases field and re-insert at end of frontmatter
    # The most common issue: aliases inserted mid-frontmatter breaks structure
    
    # Remove all aliases entries
    aliases_vals = []
    clean_entries = []
    for key, val in entries:
        if key == 'aliases':
            if val.strip():
                for line in val.split('\n'):
                    stripped = line.strip().lstrip('- ').strip().strip('"').strip("'")
                    if stripped:
                        aliases_vals.append(stripped)
            continue
        clean_entries.append((key, val))
    
    # Find insertion point: after related blocks, before closing
    # Check existing aliases content
    has_related = any(k == 'related' for k, _ in clean_entries)
    
    # Insert aliases as the last field
    alias_block = '\n'.join(f'  - {a}' for a in aliases_vals) if aliases_vals else '  - placeholder'
    clean_entries.append(('aliases', alias_block))
    
    new_yaml = entries_to_yaml(clean_entries)
    
    # Verify
    try:
        yaml.safe_load(new_yaml)
    except Exception as e:
        # Try without aliases entirely
        clean_entries.pop()  # remove aliases
        new_yaml = entries_to_yaml(clean_entries)
        try:
            yaml.safe_load(new_yaml)
        except:
            return False, f"still broken: {e}"
    
    new_text = '---\n' + new_yaml + '\n---\n' + body
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_text)
    return True, "fixed"

def main():
    fixed = 0
    ok = 0
    failed = 0
    
    for d in DIRS:
        dp = os.path.join(WIKI, d)
        if not os.path.isdir(dp):
            continue
        for fn in sorted(os.listdir(dp)):
            if not fn.endswith('.md'):
                continue
            fp = os.path.join(dp, fn)
            
            # Quick YAML parse check
            text = read_file(fp)
            if not text:
                continue
            parts = text.split('---', 2)
            if len(parts) < 2:
                continue
            try:
                yaml.safe_load(parts[1])
                ok += 1
            except:
                pass  # Will be fixed below
    
    print(f"Pre-check: {ok} cards OK")
    
    # Now fix broken ones
    for d in DIRS:
        dp = os.path.join(WIKI, d)
        if not os.path.isdir(dp):
            continue
        for fn in sorted(os.listdir(dp)):
            if not fn.endswith('.md'):
                continue
            fp = os.path.join(dp, fn)
            
            text = read_file(fp)
            if not text:
                continue
            parts = text.split('---', 2)
            if len(parts) < 2:
                print(f"  NOFM: {d}/{fn}")
                failed += 1
                continue
            try:
                yaml.safe_load(parts[1])
                continue  # Already OK
            except:
                pass
            
            success, msg = fix_file(fp)
            if success:
                fixed += 1
                print(f"  FIXED: {d}/{fn}")
            else:
                failed += 1
                print(f"  FAIL: {d}/{fn}: {msg}")
    
    print(f"\nFixed: {fixed}, Failed: {failed}")

if __name__ == '__main__':
    main()
