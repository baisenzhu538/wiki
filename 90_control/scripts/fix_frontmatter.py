#!/usr/bin/env python3
"""Fix frontmatter status field warnings."""
import re
import os
from pathlib import Path
from datetime import date

WIKI_ROOT = Path(r"C:\Users\Administrator\Desktop\wiki\30_wiki")
today = date.today().isoformat()

def fix_reviewed_files():
    """Add review_date to files with status=reviewed."""
    list_file = Path("/tmp/review_date_files.txt")
    if not list_file.exists():
        list_file = Path(os.environ.get('TEMP', r'C:\Users\Administrator\AppData\Local\Temp')) / "review_date_files.txt"
    
    if not list_file.exists():
        print("review_date_files.txt not found")
        return
    
    files = [l.strip() for l in list_file.read_text().splitlines() if l.strip()]
    success = 0
    
    for filepath in files:
        if filepath.startswith("30_wiki/"):
            filepath = filepath[8:]
        full_path = WIKI_ROOT / filepath
        
        if not full_path.exists():
            print(f"  SKIP (not found): {filepath}")
            continue
        
        content = full_path.read_text(encoding='utf-8')
        
        if re.search(r'^review_date:', content, re.MULTILINE):
            continue
        
        # Try to insert after reviewed_by
        match = re.search(r'^(reviewed_by:\s*.+)$', content, re.MULTILINE)
        if match:
            insert_after = match.group(0)
            new_content = content.replace(insert_after, insert_after + f'\nreview_date: "{today}"', 1)
        else:
            # Insert after status line
            match = re.search(r'^(status:\s*reviewed)', content, re.MULTILINE)
            if match:
                insert_after = match.group(0)
                new_content = content.replace(insert_after, insert_after + f'\nreview_date: "{today}"', 1)
            else:
                print(f"  SKIP (no status): {filepath}")
                continue
        
        full_path.write_text(new_content, encoding='utf-8')
        success += 1
    
    print(f"Fixed {success} reviewed files with review_date")

def fix_enriched_files():
    """Add source_refs to files with status=enriched."""
    list_file = Path("/tmp/enriched_files.txt")
    if not list_file.exists():
        list_file = Path(os.environ.get('TEMP', r'C:\Users\Administrator\AppData\Local\Temp')) / "enriched_files.txt"
    
    if not list_file.exists():
        print("enriched_files.txt not found")
        return
    
    files = [l.strip() for l in list_file.read_text().splitlines() if l.strip()]
    success = 0
    
    for filepath in files:
        if filepath.startswith("30_wiki/"):
            filepath = filepath[8:]
        full_path = WIKI_ROOT / filepath
        
        if not full_path.exists():
            print(f"  SKIP (not found): {filepath}")
            continue
        
        content = full_path.read_text(encoding='utf-8')
        
        if re.search(r'^source_refs:', content, re.MULTILINE):
            continue
        
        match = re.search(r'^(status:\s*enriched)', content, re.MULTILINE)
        if match:
            insert_after = match.group(0)
            new_content = content.replace(insert_after, insert_after + '\nsource_refs:\n- pending_archive: src_unknown', 1)
        else:
            print(f"  SKIP (no status): {filepath}")
            continue
        
        full_path.write_text(new_content, encoding='utf-8')
        success += 1
    
    print(f"Fixed {success} enriched files with source_refs")

if __name__ == "__main__":
    fix_reviewed_files()
    fix_enriched_files()
