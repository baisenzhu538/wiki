import os, re, yaml

vault = "30_wiki"
# Exclude meta/log/index files that don't need frontmatter id
skip_dirs = {"90_control", "70_product", "60_feedback", "50_archive", "40_outputs", "20_memory", "10_raw", "00_inbox"}
skip_files = {"log.md", "index.md", "dashboard.md", "README.md", "contradictions.md", "contradictions-todo.md"}

total = 0
missing_fm = 0
missing_id = 0
missing_type = 0
missing_status = 0
new_fmt = 0
old_fmt = 0
both_fmt = 0
broken_links = 0
total_links = 0
garbled_broken = 0  # broken links that are encoding garbage

# Build valid targets
valid_targets = set()
for root, dirs, files in os.walk(vault):
    for f in files:
        if f.endswith(".md"):
            name = f[:-3]
            valid_targets.add(name)
            rel = os.path.relpath(os.path.join(root, name), vault).replace("\\", "/")
            valid_targets.add(rel)

def is_garbled(s):
    """Detect garbled Chinese encoding artifacts"""
    import unicodedata
    garbled_count = 0
    for ch in s:
        if unicodedata.category(ch) == 'So':  # Symbols
            continue
        try:
            name = unicodedata.name(ch, '')
            if 'CJK' in name:
                pass  # proper Chinese
            elif 'LATIN' in name:
                pass  # normal Latin
            else:
                garbled_count += 1
        except:
            garbled_count += 1
    # If more than 30% of chars are unusual, it's likely garbled
    if len(s) == 0:
        return False
    return garbled_count / max(len(s), 1) > 0.3

for root, dirs, files in os.walk(vault):
    # Skip non-wiki dirs
    rel_root = os.path.relpath(root, vault)
    if any(rel_root.startswith(s) or rel_root == s for s in skip_dirs):
        continue

    for f in files:
        if not f.endswith(".md"):
            continue
        # Skip meta files
        if f in skip_files:
            continue

        path = os.path.join(root, f)
        total += 1
        content = open(path, "r", encoding="utf-8", errors="replace").read()

        # Frontmatter
        fm_match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        valid_fm = False
        if fm_match:
            try:
                fm = yaml.safe_load(fm_match.group(1))
                if isinstance(fm, dict):
                    valid_fm = True
                    if not fm.get("id"): missing_id += 1
                    if not fm.get("type"): missing_type += 1
                    if not fm.get("status"): missing_status += 1
            except yaml.YAMLError:
                pass
        if not valid_fm:
            missing_fm += 1

        # Format
        has_critique = "## Critique" in content
        has_constraints = "## Constraints & Boundaries" in content
        if has_critique: new_fmt += 1
        if has_constraints: old_fmt += 1
        if has_critique and has_constraints: both_fmt += 1

        # Broken wikilinks
        links = re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", content)
        for link in links:
            total_links += 1
            target = link.strip()

            if is_garbled(target):
                garbled_broken += 1
                continue

            if target in valid_targets:
                continue
            if target + ".md" in valid_targets:
                continue

            found = False
            for vt in valid_targets:
                if vt.endswith("/" + target) or vt == target:
                    found = True
                    break
            if not found:
                broken_links += 1
                if broken_links <= 15:
                    print(f"  BROKEN: [[{target}]] in {rel_root}/{f}")

print(f"\nFiles scanned: {total}")
print(f"--- Sprint 4 metrics ---")
print(f"Broken wikilinks (real):     {broken_links} / {total_links}")
print(f"  - Garbled encoding links:  {garbled_broken} (excluded)")
print(f"Missing/invalid frontmatter: {missing_fm}")
print(f"  - missing id:              {missing_id}")
print(f"  - missing type:            {missing_type}")
print(f"  - missing status:          {missing_status}")
print(f"Format:")
print(f"  - Has ## Critique (new):   {new_fmt}")
print(f"  - Has ## Constraints (old): {old_fmt}")
print(f"  - Has BOTH:                {both_fmt}")
