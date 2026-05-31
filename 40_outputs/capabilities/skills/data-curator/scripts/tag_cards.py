#!/usr/bin/env python3
"""Phase 3: Multi-Dimensional Tagging.

Applies controlled vocabulary tags from 90_control/tag-registry.yaml to concept cards.
Uses filename prefix + domain + content inference rules.
Always requires human confirmation before write.

Usage:
  python tag_cards.py --card master-systems-thinking --dry-run
  python tag_cards.py --card master-systems-thinking --write --backup
  python tag_cards.py --batch 5 --dry-run
"""

import json
import os
import re
import shutil
import sys
from pathlib import Path
from collections import OrderedDict

# --- Configuration ---

VAULT_ROOT = Path(r"C:\Users\Administrator\Desktop\wiki")
CONCEPTS_DIR = VAULT_ROOT / "30_wiki" / "concepts"
BACKUP_DIR = VAULT_ROOT / "60_feedback" / "data-quality" / "backups"
TAG_REGISTRY_PATH = VAULT_ROOT / "90_control" / "tag-registry.yaml"

# Tag inference map: filename prefix → suggested tags
PREFIX_TAG_MAP = {
    "yt-": ["#domain/entrepreneurship", "#method/product-design"],
    "master-": ["#domain/knowledge-management"],
    "ocr-一堂-": ["#domain/entrepreneurship", "#quality/ocr-card"],
    "ocr-": ["#quality/ocr-card"],
    "design-": ["#domain/design"],
    "kdo-": ["#domain/knowledge-management", "#domain/software-engineering"],
    "graph-rag": ["#domain/ai-engineering", "#domain/knowledge-management"],
    "deepseek-": ["#domain/ai-engineering"],
    "kimi-": ["#domain/ai-engineering"],
    "anthropic-": ["#domain/ai-engineering"],
    "ai-native": ["#domain/ai-engineering"],
    "aigc": ["#domain/design"],
    "his-": ["#domain/healthcare-it"],
    "ec-": ["#domain/knowledge-management", "#method/evaluation-method"],
    "business-": ["#domain/entrepreneurship"],
}

# Domain → additional tags
DOMAIN_TAG_MAP = {
    "yitang": ["#domain/entrepreneurship"],
    "master": ["#domain/knowledge-management", "#method/thinking-tool"],
    "healthcare": ["#domain/healthcare-it"],
    "ai-saas": ["#domain/ai-engineering"],
}

# Content keyword → tag hints
KEYWORD_TAG_MAP = {
    "决策": ["#method/decision-framework"],
    "ROI": ["#method/evaluation-method"],
    "产品": ["#method/product-design"],
    "学习": ["#method/learning-method"],
    "管理": ["#method/management-tool"],
    "执行": ["#method/execution-method"],
    "表达": ["#method/communication-method"],
    "prompt": ["#method/prompt-engineering"],
    "提示词": ["#method/prompt-engineering"],
    "创业": ["#domain/entrepreneurship"],
    "HIS": ["#domain/healthcare-it"],
    "医院": ["#domain/healthcare-it"],
    "AI": ["#domain/ai-engineering"],
    "LLM": ["#domain/ai-engineering"],
    "RAG": ["#domain/ai-engineering"],
    "知识管理": ["#domain/knowledge-management"],
    "KDO": ["#domain/knowledge-management"],
    "设计": ["#domain/design"],
    "AIGC": ["#domain/design"],
}


def load_tag_registry() -> set[str]:
    """Load all valid tag values from the tag registry."""
    if not TAG_REGISTRY_PATH.exists():
        print(f"WARNING: Tag registry not found at {TAG_REGISTRY_PATH}")
        return set()

    text = TAG_REGISTRY_PATH.read_text(encoding="utf-8")
    valid_tags = set()

    # Simple YAML parsing (avoid dependency on PyYAML)
    in_values = False
    for line in text.split("\n"):
        stripped = line.strip()
        if stripped.startswith("values:"):
            in_values = True
            continue
        if in_values:
            if stripped.startswith("- ") and stripped[2:].startswith("#"):
                tag_val = stripped[2:].strip()
                valid_tags.add(tag_val)
            elif not stripped.startswith("- ") and ":" in stripped and not stripped.startswith("#"):
                in_values = False

    return valid_tags


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


def infer_tags(filename_stem: str, metadata: dict, body: str) -> list[str]:
    """Infer tags for a card based on prefix, domain, and content."""
    tags = set()

    # Rule 1: Filename prefix
    for prefix, suggested in PREFIX_TAG_MAP.items():
        if filename_stem.lower().startswith(prefix.lower()):
            tags.update(suggested)
            break  # First prefix match wins

    # Rule 2: Domain field
    domain_val = metadata.get("domain", [])
    if isinstance(domain_val, str):
        domain_val = [domain_val]
    for d in domain_val:
        d_clean = d.strip('"').strip("'")
        if d_clean in DOMAIN_TAG_MAP:
            tags.update(DOMAIN_TAG_MAP[d_clean])

    # Rule 3: Content keywords (only if < 3 tags so far)
    if len(tags) < 3:
        # Sample first 2000 chars of body to avoid false positives from index sections
        body_sample = body[:2000].lower() + " " + filename_stem.lower()
        for keyword, suggested in KEYWORD_TAG_MAP.items():
            if keyword.lower() in body_sample:
                tags.update(suggested)
                if len(tags) >= 5:
                    break

    # Ensure at least one domain tag
    if not any(t.startswith("#domain/") for t in tags):
        tags.add("#domain/knowledge-management")  # Default fallback

    # Ensure at least one method tag for non-entity cards
    if metadata.get("type") != "entity" and not any(t.startswith("#method/") for t in tags):
        tags.add("#method/thinking-tool")

    # Add quality tag for OCR cards
    if filename_stem.startswith("ocr-"):
        tags.add("#quality/ocr-card")

    return sorted(tags)


def validate_tags(tags: list[str], valid_tags: set[str]) -> tuple[list[str], list[str]]:
    """Validate tags against registry. Returns (valid, invalid)."""
    valid = []
    invalid = []
    for tag in tags:
        if tag in valid_tags:
            valid.append(tag)
        else:
            invalid.append(tag)
    return valid, invalid


def render_frontmatter(metadata: dict) -> str:
    """Render metadata dict back to YAML frontmatter string."""
    # Sort keys: id first, then alphabetical
    ordered = OrderedDict()
    if "id" in metadata:
        ordered["id"] = metadata.pop("id")

    for key in sorted(metadata.keys()):
        ordered[key] = metadata[key]

    # Restore id
    if "id" not in ordered and "id" in metadata:
        ordered["id"] = metadata["id"]

    lines = ["---"]
    for key, value in ordered.items():
        if isinstance(value, list):
            if len(value) == 0:
                lines.append(f"{key}: []")
            else:
                lines.append(f"{key}:")
                for item in value:
                    if isinstance(item, str) and (":" in item or "#" in item):
                        lines.append(f'  - "{item}"')
                    elif isinstance(item, str):
                        lines.append(f"  - {item}")
                    else:
                        lines.append(f"  - {item}")
        elif isinstance(value, dict):
            lines.append(f"{key}:")
            for k, v in value.items():
                lines.append(f"  {k}: {v}")
        elif isinstance(value, str):
            if ":" in value or "#" in value:
                lines.append(f'{key}: "{value}"')
            else:
                lines.append(f"{key}: {value}")
        elif isinstance(value, float):
            lines.append(f"{key}: {value:.2f}")
        else:
            lines.append(f"{key}: {value}")

    lines.append("---")
    return "\n".join(lines)


def tag_card(filepath: Path, valid_tags: set[str], dry_run: bool = True, backup: bool = True) -> dict:
    """Tag a single card."""
    stem = filepath.stem
    original_text = filepath.read_text(encoding="utf-8", errors="replace")
    metadata, body, raw_fm = parse_frontmatter(original_text)

    if not metadata:
        return {"file": str(filepath), "status": "skipped", "reason": "no frontmatter"}

    # Get existing tags
    existing_tags = metadata.get("tags", [])
    if isinstance(existing_tags, str):
        existing_tags = [existing_tags]
    existing_tags = [t.strip('"').strip("'") for t in existing_tags if t]

    # Infer new tags
    proposed_tags = infer_tags(stem, metadata, body)

    # Merge: keep existing valid tags, add new ones
    merged = set(existing_tags) | set(proposed_tags)
    merged = sorted(merged)

    # Validate
    valid, invalid = validate_tags(merged, valid_tags)

    if invalid and valid_tags:
        print(f"  WARNING: {len(invalid)} tags not in registry: {invalid}")

    # Check if anything changed
    if set(valid) == set(existing_tags):
        return {"file": str(filepath), "status": "clean", "tags": valid}

    if dry_run:
        print(f"\n--- {stem} (DRY RUN) ---")
        print(f"  Existing: {existing_tags}")
        print(f"  Proposed: {proposed_tags}")
        print(f"  Invalid:  {invalid}")
        print(f"  Final:    {valid}")
        return {"file": str(filepath), "status": "dry_run", "tags": valid, "existing": existing_tags}

    # Write
    metadata["tags"] = valid

    if backup:
        backup_path = BACKUP_DIR / f"{stem}.md.bak"
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(filepath, backup_path)

    new_fm = render_frontmatter(metadata)
    new_text = new_fm + "\n" + body
    filepath.write_text(new_text, encoding="utf-8")

    added = set(valid) - set(existing_tags)
    removed = set(existing_tags) - set(valid)
    return {"file": str(filepath), "status": "written", "tags": valid,
            "added": sorted(added), "removed": sorted(removed)}


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

    valid_tags = load_tag_registry()
    if valid_tags:
        print(f"Loaded {len(valid_tags)} valid tags from registry")
    else:
        print("WARNING: No tag registry found — all tags will be accepted")

    if card_id:
        filepath = CONCEPTS_DIR / f"{card_id}.md"
        if not filepath.exists():
            print(f"ERROR: Card not found: {filepath}")
            sys.exit(1)
        result = tag_card(filepath, valid_tags, dry_run=dry_run, backup=backup)
        print(f"\nStatus: {result['status']}")
        if result.get("tags"):
            print(f"Tags: {result['tags']}")

    elif batch_size > 0:
        cards = sorted(CONCEPTS_DIR.glob("*.md"))[:batch_size]
        mode = "DRY RUN" if dry_run else "WRITE"
        print(f"Processing batch of {len(cards)} cards ({mode})...")

        for card_path in cards:
            result = tag_card(card_path, valid_tags, dry_run=dry_run, backup=backup)
            status_symbol = "✓" if result["status"] == "clean" else "○" if result["status"] == "dry_run" else "●"
            tags_count = len(result.get("tags", []))
            print(f"  {status_symbol} {card_path.stem}: {result['status']} ({tags_count} tags)")

    else:
        print("Usage: tag_cards.py --card <id> | --batch <N> [--write|--dry-run] [--no-backup]")
        sys.exit(1)


if __name__ == "__main__":
    main()
