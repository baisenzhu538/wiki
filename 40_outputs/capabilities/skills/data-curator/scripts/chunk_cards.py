#!/usr/bin/env python3
"""Phase 4: Atomic Chunking Engine.

Splits concept cards into atomic chunks based on heading structure.
Chunks are registered in .kdo/state.json — card body is NOT modified.

Chunk types derived from card section structure (not an orthogonal taxonomy):
  claim, constraint, critique, synthesis, question, action_trigger,
  procedure, definition, example, reference

Chunk addressing: <card_slug>/<chunk_type>/<NNN>

Usage:
  python chunk_cards.py --card master-systems-thinking --dry-run
  python chunk_cards.py --card master-systems-thinking --write --backup
  python chunk_cards.py --batch 5 --dry-run
"""

import json
import os
import re
import shutil
import sys
from collections import Counter
from pathlib import Path

# --- Configuration ---

VAULT_ROOT = Path(r"C:\Users\Administrator\Desktop\wiki")
CONCEPTS_DIR = VAULT_ROOT / "30_wiki" / "concepts"
STATE_PATH = VAULT_ROOT / ".kdo" / "state.json"
BACKUP_DIR = VAULT_ROOT / "60_feedback" / "data-quality" / "backups"

# Heading → chunk type mapping
# Matched against heading text (case-insensitive, partial CJK match)
HEADING_TYPE_MAP = [
    # (pattern, chunk_type)
    (r"(?i)claims?|核心主张|核心观点|关键主张|稳定概念", "claim"),
    (r"(?i)critique|质疑|外部攻击|攻击者|scholar|边界.*条件|boundar|限制|局限", "constraint"),
    (r"(?i)(?:####\s*)?(?:scholar|学者|攻击者)", "critique"),
    (r"(?i)synthesis|对标|综合|跨域|bridge", "synthesis"),
    (r"(?i)open.questions?|开放问题|未解决|待探索", "question"),
    (r"(?i)action.triggers?|触发|什么时候用|不要用.*场景|适用场景|使用场景", "action_trigger"),
    (r"(?i)procedure|步骤|流程|操作|how.to|使用方法", "procedure"),
    (r"(?i)definition|定义|是什么|概述|summary|概览", "definition"),
    (r"(?i)example|案例|举例|实例|case|场景", "example"),
    (r"(?i)source.refs?|来源|参考文献|reference", "reference"),
    (r"(?i)framework|框架|模型|工具.*概览", "definition"),
    (r"(?i)output.opportunities|产出机会|可交付", "synthesis"),
    (r"(?i)reusable.knowledge|可复用知识", "claim"),
]

# Minimum characters for a chunk to be registered
MIN_CHUNK_CHARS = 50


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Parse YAML frontmatter. Returns (metadata, body)."""
    text = text.replace("\r\n", "\n")
    if text.startswith("﻿"):
        text = text[1:]
    if not text.startswith("---\n"):
        return {}, text

    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text

    raw_fm = text[4:end]
    body = text[end + 5:]

    # Simple line-by-line parse
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

    return metadata, body


def classify_heading(heading_text: str) -> str:
    """Classify a heading into a chunk type."""
    for pattern, chunk_type in HEADING_TYPE_MAP:
        if re.search(pattern, heading_text):
            return chunk_type
    return "claim"  # Default: any substantive section is treated as claims


def split_into_sections(body: str) -> list[dict]:
    """Split body into sections by ## and ### headings."""
    lines = body.split("\n")
    sections = []
    current_heading = None
    current_level = 0
    current_lines = []
    char_offset = 0

    for line in lines:
        # Detect headings
        h2_match = re.match(r"^##\s+(.+)", line)
        h3_match = re.match(r"^###\s+(.+)", line)
        h4_match = re.match(r"^####\s+(.+)", line)

        if h2_match or h3_match or h4_match:
            # Save previous section
            if current_heading and current_lines:
                content = "\n".join(current_lines).strip()
                if len(content) >= MIN_CHUNK_CHARS:
                    sections.append({
                        "heading": current_heading,
                        "level": current_level,
                        "chunk_type": classify_heading(current_heading),
                        "content": content,
                        "char_offset": char_offset
                    })

            if h2_match:
                current_heading = h2_match.group(1).strip()
                current_level = 2
            elif h3_match:
                current_heading = h3_match.group(1).strip()
                current_level = 3
            else:
                current_heading = h4_match.group(1).strip()
                current_level = 4

            current_lines = []
            char_offset += len(line) + 1
        else:
            current_lines.append(line)
            char_offset += len(line) + 1

    # Save final section
    if current_heading and current_lines:
        content = "\n".join(current_lines).strip()
        if len(content) >= MIN_CHUNK_CHARS:
            sections.append({
                "heading": current_heading,
                "level": current_level,
                "chunk_type": classify_heading(current_heading),
                "content": content,
                "char_offset": char_offset
            })

    # If no sections found (card has no ## headings), treat entire body as one definition chunk
    if not sections:
        content = body.strip()
        if len(content) >= MIN_CHUNK_CHARS:
            sections.append({
                "heading": "(no headings)",
                "level": 0,
                "chunk_type": "definition",
                "content": content[:500],  # Truncate for registry
                "char_offset": 0
            })

    return sections


def build_inherited_metadata(metadata: dict) -> dict:
    """Extract inheritable metadata from card frontmatter."""
    return {
        "domain": metadata.get("domain", []),
        "tags": metadata.get("tags", []),
        "confidence": metadata.get("confidence"),
        "trust_level": metadata.get("trust_level"),
        "source_refs": metadata.get("source_refs", []),
        "status": metadata.get("status"),
        "type": metadata.get("type"),
    }


def chunk_card(filepath: Path, dry_run: bool = True, backup: bool = True) -> dict:
    """Chunk a single card into atomic sections."""
    stem = filepath.stem
    text = filepath.read_text(encoding="utf-8", errors="replace")
    metadata, body = parse_frontmatter(text)

    if not metadata:
        return {"file": str(filepath), "status": "skipped", "reason": "no frontmatter"}

    sections = split_into_sections(body)
    inherited = build_inherited_metadata(metadata)

    # Build chunk entries
    type_counter = Counter()
    chunks = []
    for section in sections:
        chunk_type = section["chunk_type"]
        type_counter[chunk_type] += 1
        seq = type_counter[chunk_type]

        chunk_id = f"{stem}/{chunk_type}/{seq:03d}"

        chunks.append({
            "chunk_id": chunk_id,
            "card_slug": stem,
            "chunk_type": chunk_type,
            "sequence": seq,
            "heading": section["heading"],
            "heading_level": section["level"],
            "content_preview": section["content"][:200],
            "char_count": len(section["content"]),
            "word_count_estimate": len(section["content"].replace("\n", " ").split()),
            "inherited": inherited
        })

    result = {
        "file": str(filepath),
        "card_slug": stem,
        "total_chunks": len(chunks),
        "by_type": dict(type_counter),
        "chunks": chunks
    }

    if dry_run:
        print(f"\n--- {stem} (DRY RUN) ---")
        print(f"  Chunks: {len(chunks)}")
        for ct, count in sorted(type_counter.items()):
            print(f"    {ct}: {count}")
        return result

    # Write to state.json
    # (backup state.json before modifying)
    if backup and STATE_PATH.exists():
        backup_path = BACKUP_DIR / f"state-{stem}.json.bak"
        shutil.copy2(STATE_PATH, backup_path)

    return result


def update_state_json(card_chunks: list[dict]) -> dict:
    """Update .kdo/state.json with chunk registry entries."""
    if not STATE_PATH.exists():
        return {"error": "state.json not found"}

    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))

    # Initialize chunks registry if not exists
    if "chunks" not in state:
        state["chunks"] = {
            "registry_version": 1,
            "total_chunks": 0,
            "by_type": {},
            "entries": []
        }

    # Add/update chunks for each card
    for card_result in card_chunks:
        card_slug = card_result["card_slug"]
        # Remove old chunks for this card
        state["chunks"]["entries"] = [
            e for e in state["chunks"]["entries"]
            if e.get("card_slug") != card_slug
        ]
        # Add new chunks
        state["chunks"]["entries"].extend(card_result["chunks"])

    # Update counters
    state["chunks"]["total_chunks"] = len(state["chunks"]["entries"])
    by_type = Counter()
    for entry in state["chunks"]["entries"]:
        by_type[entry["chunk_type"]] += 1
    state["chunks"]["by_type"] = dict(by_type)
    state["chunks"]["registry_version"] = state["chunks"].get("registry_version", 1)

    return state


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
        result = chunk_card(filepath, dry_run=dry_run, backup=backup)

        if not dry_run and result["status"] != "skipped":
            updated_state = update_state_json([result])
            STATE_PATH.write_text(json.dumps(updated_state, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"\nState.json updated. Total chunks: {updated_state['chunks']['total_chunks']}")

    elif batch_size > 0:
        cards = sorted(CONCEPTS_DIR.glob("*.md"))[:batch_size]
        mode = "DRY RUN" if dry_run else "WRITE"
        print(f"Processing batch of {len(cards)} cards ({mode})...")

        results = []
        for card_path in cards:
            result = chunk_card(card_path, dry_run=dry_run, backup=backup)
            if result.get("total_chunks"):
                print(f"  {card_path.stem}: {result['total_chunks']} chunks ({result['by_type']})")
            results.append(result)

        if not dry_run:
            valid_results = [r for r in results if r.get("chunks")]
            if valid_results:
                updated_state = update_state_json(valid_results)
                STATE_PATH.write_text(json.dumps(updated_state, ensure_ascii=False, indent=2), encoding="utf-8")
                print(f"\nState.json updated. Total chunks: {updated_state['chunks']['total_chunks']}")

    else:
        print("Usage: chunk_cards.py --card <id> | --batch <N> [--write|--dry-run] [--no-backup]")
        sys.exit(1)


if __name__ == "__main__":
    main()
