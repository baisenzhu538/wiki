#!/usr/bin/env python3
"""Phase 2: Data Cleaning — Frontmatter Normalizer.

Normalizes YAML frontmatter across all concept cards:
  - Curly quotes → straight quotes
  - YAML values: strip unnecessary quoting
  - Date formats: normalize to YYYY-MM-DD
  - Decimal places: confidence → 2 decimal places
  - Enum standardization: domain → YAML list format
  - Missing field inference: type, id, status
  - Dead field removal: contradicts (always empty)
  - Frontmatter key sorting

Usage:
  python clean_cards.py --card master-systems-thinking --dry-run
  python clean_cards.py --card master-systems-thinking --write --backup
  python clean_cards.py --batch 5 --dry-run
"""

import json
import os
import re
import shutil
import sys
from datetime import date, datetime
from pathlib import Path
from collections import OrderedDict

# --- Configuration ---

VAULT_ROOT = Path(r"C:\Users\Administrator\Desktop\wiki")
CONCEPTS_DIR = VAULT_ROOT / "30_wiki" / "concepts"
BACKUP_DIR = VAULT_ROOT / "60_feedback" / "data-quality" / "backups"

# Standard enum values
VALID_STATUS = {"draft", "reviewed", "stable", "needs-review", "enriched"}
VALID_TYPE = {"concept", "entity", "comparison", "decision", "improvement-plan",
              "system", "trend", "tool", "framework"}
VALID_DOMAIN = {"master", "ai-saas", "healthcare", "yitang"}

# Fields to remove (dead fields)
REMOVE_FIELDS = {"contradicts"}  # 0/384 cards have non-empty contradicts

# Field key sort order (alphabetical)
# id first for readability, then alphabetical

# Date fields to normalize
DATE_FIELDS = {"created_at", "updated_at", "review_date"}

# Domain inference by filename prefix
DOMAIN_PREFIX_MAP = {
    "yt-": "yitang",
    "master-": "master",
    "ocr-一堂-": "yitang",
    "his-": "healthcare",
    "kdo-": "master",
    "design-": "yitang",  # AIGC design from 一堂
}

# Domain inference by content keywords
DOMAIN_KEYWORD_MAP = {
    "healthcare": ["HIS", "医院", "诊所", "医疗", "病人", "处方", "健康"],
    "ai-saas": ["AI", "LLM", "DeepSeek", "Claude", "GPT", "prompt", "embedding", "RAG"],
    "yitang": ["一堂", "创业", "Truman", "周伯通"],
    "master": ["KDO", "知识管理", "方法论", "框架", "铁律"],
}


def parse_frontmatter(text: str) -> tuple[dict, str, str]:
    """Parse YAML frontmatter. Returns (metadata, body, raw_frontmatter)."""
    text = text.replace("\r\n", "\n")
    if text.startswith("﻿"):
        text = text[1:]
    if not text.startswith("---\n"):
        return {}, text, ""

    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text, ""

    raw_fm = text[4:end]
    body = text[end + 5:]

    metadata = {}
    lines = raw_fm.split("\n")
    current_key = None
    current_list = []

    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        if current_key and stripped.startswith("- "):
            val = stripped[2:].strip().strip('"').strip("'")
            current_list.append(val)
            continue

        if current_key and line.startswith("  ") and ":" in stripped:
            if current_list:
                metadata[current_key] = current_list
                current_list = []
            sub_key, sub_val = stripped.split(":", 1)
            sub_key = sub_key.strip()
            sub_val = sub_val.strip().strip('"').strip("'")
            if current_key not in metadata or not isinstance(metadata[current_key], dict):
                metadata[current_key] = {}
            metadata[current_key][sub_key] = sub_val
            continue

        if current_key and current_list:
            metadata[current_key] = current_list
            current_list = []
            current_key = None

        if ":" not in stripped:
            continue

        key, raw_val = stripped.split(":", 1)
        key = key.strip()
        val = raw_val.strip()

        if val and val[0] in ("[", "{") or val in ("true", "false", "null"):
            try:
                metadata[key] = json.loads(val)
                current_key = None
                continue
            except json.JSONDecodeError:
                pass

        if val and val[0] == '"' and val[-1] == '"':
            metadata[key] = val[1:-1]
            current_key = None
            continue
        if val and val[0] == "'" and val[-1] == "'":
            metadata[key] = val[1:-1]
            current_key = None
            continue

        if val:
            try:
                metadata[key] = int(val)
                current_key = None
                continue
            except ValueError:
                pass
            try:
                metadata[key] = float(val)
                current_key = None
                continue
            except ValueError:
                pass

        if val == "" or val == "[]":
            current_key = key
            current_list = []
            continue

        metadata[key] = val
        current_key = None

    if current_key and current_list:
        metadata[current_key] = current_list

    return metadata, body, raw_fm


def infer_missing_fields(metadata: dict, filename_stem: str, body: str) -> dict:
    """Infer missing fields from filename and content."""
    updated = dict(metadata)

    # id: from filename stem
    if "id" not in updated or not updated.get("id"):
        updated["id"] = filename_stem

    # type: default to concept
    if "type" not in updated or not updated.get("type"):
        updated["type"] = "concept"

    # status: if has Critique section → enriched, otherwise draft
    if "status" not in updated or not updated.get("status"):
        if "## Critique" in body or "## 质疑" in body or "## Constraints" in body:
            updated["status"] = "enriched"
        else:
            updated["status"] = "draft"

    # domain: from prefix + content
    if "domain" not in updated or not updated.get("domain"):
        inferred = None
        # Check prefix
        for prefix, domain in DOMAIN_PREFIX_MAP.items():
            if filename_stem.startswith(prefix):
                inferred = domain
                break
        # Check content keywords if no prefix match
        if inferred is None:
            for domain, keywords in DOMAIN_KEYWORD_MAP.items():
                for kw in keywords:
                    if kw.lower() in body.lower() or kw.lower() in filename_stem.lower():
                        inferred = domain
                        break
                if inferred:
                    break
        if inferred:
            updated["domain"] = [inferred]

    # created_at / updated_at: leave empty if missing (cannot safely infer without git)
    if "created_at" not in updated:
        updated["created_at"] = date.today().isoformat()
    if "updated_at" not in updated:
        updated["updated_at"] = date.today().isoformat()

    # tags: leave empty for Phase 3
    # difficulty, confidence, trust_level: leave empty if missing

    return updated


def normalize_metadata(metadata: dict, filename_stem: str, body: str) -> tuple[dict, list[str]]:
    """Normalize a card's metadata. Returns (normalized_dict, change_log)."""
    changes = []
    normalized = {}

    for key, value in metadata.items():
        # Skip dead fields
        if key in REMOVE_FIELDS:
            changes.append(f"removed dead field: {key}")
            continue

        # Clean key (strip curly quotes)
        clean_key = key.strip().replace(""", '"').replace(""", '"').replace("'", "'").replace("'", "'")

        # Clean value
        if isinstance(value, str):
            clean_val = value.strip().replace(""", '"').replace(""", '"').replace("'", "'").replace("'", "'")

            # Normalize date format
            if clean_key in DATE_FIELDS and clean_val:
                clean_val = normalize_date(clean_val)
                if clean_val != value:
                    changes.append(f"{key}: date normalized '{value}' → '{clean_val}'")

            # Normalize status enum values
            if clean_key == "status":
                old = clean_val
                clean_val = clean_val.strip('"').strip("'")
                if clean_val != old:
                    changes.append(f"{key}: unquoted '{old}' → '{clean_val}'")
                if clean_val not in VALID_STATUS:
                    changes.append(f"{key}: non-standard status preserved '{clean_val}'")

            # Normalize type enum
            if clean_key == "type":
                old = clean_val
                clean_val = clean_val.strip('"').strip("'")
                if clean_val != old:
                    changes.append(f"{key}: unquoted '{old}' → '{clean_val}'")

            normalized[clean_key] = clean_val

        elif isinstance(value, (int, float)):
            # Normalize decimal places on confidence
            if clean_key == "confidence" and isinstance(value, float):
                old = value
                clean_val = round(value, 2)
                if clean_val != old:
                    changes.append(f"{key}: rounded {old} → {clean_val}")
                normalized[clean_key] = clean_val
            else:
                normalized[clean_key] = value

        elif isinstance(value, list):
            # Clean array values
            clean_list = []
            for item in value:
                if isinstance(item, str):
                    clean_item = item.strip().strip('"').strip("'")
                    clean_list.append(clean_item)
                else:
                    clean_list.append(item)
            if clean_list != value:
                changes.append(f"{key}: cleaned {len(value)} array items")
            normalized[clean_key] = clean_list

        elif isinstance(value, dict):
            # Clean nested dict values (yitang block, visual_analysis)
            clean_dict = {}
            for k, v in value.items():
                if isinstance(v, str):
                    clean_dict[k] = v.strip().strip('"').strip("'")
                else:
                    clean_dict[k] = v
            normalized[clean_key] = clean_dict

        else:
            normalized[clean_key] = value

    # Domain: ensure list format
    if "domain" in normalized and normalized["domain"]:
        domain_val = normalized["domain"]
        if isinstance(domain_val, str):
            normalized["domain"] = [domain_val]
            changes.append("domain: scalar → list")

    # source_refs: ensure list format
    if "source_refs" in normalized and normalized["source_refs"]:
        if isinstance(normalized["source_refs"], str):
            normalized["source_refs"] = [normalized["source_refs"]]
            changes.append("source_refs: scalar → list")

    # tags: ensure list format
    if "tags" in normalized and normalized["tags"]:
        if isinstance(normalized["tags"], str):
            normalized["tags"] = [normalized["tags"]]
            changes.append("tags: scalar → list")

    return normalized, changes


def normalize_date(date_str: str) -> str:
    """Normalize a date string to YYYY-MM-DD."""
    date_str = date_str.strip().strip('"').strip("'")
    # Already YYYY-MM-DD
    if re.match(r"^\d{4}-\d{2}-\d{2}$", date_str):
        return date_str
    # ISO timestamp: 2026-05-03T13:36:55+00:00
    iso_match = re.match(r"^(\d{4}-\d{2}-\d{2})T", date_str)
    if iso_match:
        return iso_match.group(1)
    # Try to parse other formats
    for fmt in ["%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%S", "%Y/%m/%d"]:
        try:
            dt = datetime.strptime(date_str, fmt)
            return dt.strftime("%Y-%m-%d")
        except ValueError:
            continue
    return date_str


def sort_frontmatter_keys(metadata: dict) -> OrderedDict:
    """Sort frontmatter keys: id first, then alphabetical."""
    ordered = OrderedDict()
    # id always first
    if "id" in metadata:
        ordered["id"] = metadata["id"]
    # Then alphabetical for everything else
    for key in sorted(metadata.keys()):
        if key != "id":
            ordered[key] = metadata[key]
    return ordered


def render_frontmatter(metadata: dict) -> str:
    """Render metadata dict back to YAML frontmatter string."""
    lines = ["---"]
    ordered = sort_frontmatter_keys(metadata)

    for key, value in ordered.items():
        if isinstance(value, list):
            if len(value) == 0:
                lines.append(f"{key}: []")
            else:
                lines.append(f"{key}:")
                for item in value:
                    # Quote strings that contain special YAML chars
                    if isinstance(item, str) and (":" in item or "#" in item or item.startswith("[")):
                        lines.append(f'  - "{item}"')
                    elif isinstance(item, str):
                        lines.append(f"  - {item}")
                    else:
                        lines.append(f"  - {item}")
        elif isinstance(value, dict):
            lines.append(f"{key}:")
            for k, v in value.items():
                if isinstance(v, str):
                    lines.append(f"  {k}: {v}")
                else:
                    lines.append(f"  {k}: {v}")
        elif isinstance(value, str):
            if ":" in value or "#" in value or value.startswith("["):
                lines.append(f'{key}: "{value}"')
            else:
                lines.append(f"{key}: {value}")
        elif isinstance(value, float):
            lines.append(f"{key}: {value:.2f}")
        else:
            lines.append(f"{key}: {value}")

    lines.append("---")
    return "\n".join(lines)


def clean_card(filepath: Path, dry_run: bool = True, backup: bool = True) -> dict:
    """Clean a single card's frontmatter."""
    stem = filepath.stem
    original_text = filepath.read_text(encoding="utf-8", errors="replace")
    metadata, body, raw_fm = parse_frontmatter(original_text)

    if not metadata:
        return {"file": str(filepath), "status": "skipped", "reason": "no frontmatter"}

    # Infer missing fields
    enriched = infer_missing_fields(metadata, stem, body)

    # Normalize
    normalized, changes = normalize_metadata(enriched, stem, body)

    if not changes:
        return {"file": str(filepath), "status": "clean", "changes": []}

    new_fm = render_frontmatter(normalized)
    new_text = new_fm + "\n" + body

    if dry_run:
        # Print diff
        print(f"\n--- {stem} (DRY RUN) ---")
        print(f"Changes: {len(changes)}")
        for c in changes:
            print(f"  - {c}")
        return {"file": str(filepath), "status": "dry_run", "changes": changes}

    # Write
    if backup:
        backup_path = BACKUP_DIR / f"{stem}.md.bak"
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(filepath, backup_path)

    filepath.write_text(new_text, encoding="utf-8")
    return {"file": str(filepath), "status": "written", "changes": changes}


def get_batch_cards(limit: int) -> list[Path]:
    """Get the next batch of cards to clean (prioritizing Gen B cards)."""
    all_cards = sorted(CONCEPTS_DIR.glob("*.md"))
    # Prioritize cards that haven't been cleaned yet
    # For now, just return first N
    return all_cards[:limit]


def main():
    dry_run = True
    card_id = None
    batch_size = 0
    backup = True

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--card" and i + 1 < len(args):
            card_id = args[i + 1]
            i += 2
        elif args[i] == "--batch" and i + 1 < len(args):
            batch_size = int(args[i + 1])
            i += 2
        elif args[i] == "--write":
            dry_run = False
            i += 1
        elif args[i] == "--dry-run":
            dry_run = True
            i += 1
        elif args[i] == "--no-backup":
            backup = False
            i += 1
        else:
            i += 1

    if card_id:
        filepath = CONCEPTS_DIR / f"{card_id}.md"
        if not filepath.exists():
            print(f"ERROR: Card not found: {filepath}")
            sys.exit(1)
        result = clean_card(filepath, dry_run=dry_run, backup=backup)
        print(f"\nStatus: {result['status']}")
        if result.get("changes"):
            print(f"Changes: {len(result['changes'])}")
            for c in result["changes"]:
                print(f"  - {c}")

    elif batch_size > 0:
        cards = get_batch_cards(batch_size)
        mode = "DRY RUN" if dry_run else "WRITE"
        print(f"Processing batch of {len(cards)} cards ({mode})...")

        for card_path in cards:
            result = clean_card(card_path, dry_run=dry_run, backup=backup)
            status_symbol = "✓" if result["status"] == "clean" else "○" if result["status"] == "dry_run" else "●"
            changes_count = len(result.get("changes", []))
            print(f"  {status_symbol} {card_path.stem}: {result['status']} ({changes_count} changes)")

    else:
        print("Usage: clean_cards.py --card <id> | --batch <N> [--write|--dry-run] [--no-backup]")
        sys.exit(1)


if __name__ == "__main__":
    main()
