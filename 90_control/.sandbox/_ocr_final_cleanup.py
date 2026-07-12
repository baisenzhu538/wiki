"""#163 最终清理 — 全库扫 [[ocr-*]] 残留，related摘除 + body去括号"""
import re, json, sys
from pathlib import Path
from collections import defaultdict

VAULT = Path(__file__).resolve().parent.parent.parent
SANDBOX = VAULT / "90_control" / ".sandbox"

def cleanup_file(filepath):
    """Remove ocr-* from related lines, strip [[ocr-*]] brackets from body. Returns (changed, new_content, details)."""
    try:
        content = filepath.read_text(encoding="utf-8")
    except:
        return False, "", []

    original = content
    details = []

    # Find frontmatter boundary
    fm_match = re.match(r"^(---\s*\n.*?\n---)", content, re.DOTALL)
    if not fm_match:
        return False, "", []

    fm_block = fm_match.group(1)
    rest = content[len(fm_block):]

    # 1. Remove related lines containing [[ocr-*
    lines = fm_block.splitlines()
    new_lines = []
    ocr_related_removed = []
    for line in lines:
        if re.search(r'\[\[ocr-', line) and line.strip().startswith('-'):
            ocr_related_removed.append(line.strip()[:80])
            continue
        new_lines.append(line)

    if ocr_related_removed:
        details.append(f"related: removed {len(ocr_related_removed)} ocr-* line(s)")

    new_fm = "\n".join(new_lines)
    content = new_fm + rest

    # 2. Body: strip [[ocr-*]] -> keep text
    body_ocr_count = len(re.findall(r'\[\[ocr-[^\]]+\]\]', content))
    if body_ocr_count > 0:
        content = re.sub(r'\[\[(ocr-[^\]]+)\]\]', r'\1', content)
        details.append(f"body: stripped {body_ocr_count} ocr-* brackets")

    if content == original:
        return False, "", []

    return True, content, details


def main():
    apply_flag = "--apply" in sys.argv

    manifest = defaultdict(list)
    touched = 0

    for d in ["concepts", "frameworks", "tools", "cases", "methods", "systems",
              "operations", "dark-knowledges", "domains", "dk", "decisions", "skills", "links"]:
        dpath = VAULT / "30_wiki" / d
        if not dpath.is_dir():
            continue
        for f in sorted(dpath.rglob("*.md")):
            # SKIP raw/ocr/ files — OCR cards referencing each other is expected
            if 'raw/ocr' in str(f):
                continue
            # Quick check: does file contain [[ocr-
            try:
                quick = f.read_text(encoding="utf-8")
            except:
                continue
            if '[[ocr-' not in quick:
                continue

            changed, new_content, details = cleanup_file(f)
            if not changed:
                continue

            rel = str(f.relative_to(VAULT))
            touched += 1

            # Count what was removed
            ocr_targets = set()
            for line in quick.splitlines():
                m = re.search(r'\[\[(ocr-[^\]]+)\]\]', line)
                if m:
                    ocr_targets.add(m.group(1))

            for t in ocr_targets:
                manifest[t].append(rel)

            if apply_flag:
                f.write_text(new_content, encoding="utf-8")

            print(f"  [{rel}]")
            for d in details:
                print(f"    {d}")

    # Save manifest
    flat = [{"ocr_target": k, "from_files": v} for k, v in sorted(manifest.items())]
    manifest_path = SANDBOX / "ocr_final_cleanup_manifest.json"
    manifest_path.write_text(json.dumps({
        "description": "#163 final ocr cleanup — all [[ocr-*]] references removed",
        "total_targets": len(flat),
        "total_files": touched,
        "targets": flat,
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    mode = "APPLY" if apply_flag else "DRY-RUN"
    print(f"\n{mode}: {touched} files, {len(flat)} unique ocr targets")
    print(f"Manifest: {manifest_path}")

if __name__ == "__main__":
    main()
