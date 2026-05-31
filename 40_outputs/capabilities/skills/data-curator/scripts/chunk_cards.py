#!/usr/bin/env python3
"""Phase 4: True Atomic Chunking Engine (v1.3).

Splits cards into atomic chunks at claim/fact/rule level (30-200 chars target).
Supports product track (concept cards) and process track (dark-knowledge cards).
Chunks registered in .kdo/state.json — card body is NOT modified.

Chunk types (product track):
  claim, constraint, critique, synthesis, question, action_trigger,
  procedure, definition, example, reference, process_data, error_data

Chunk types (process track / dark-knowledge 6-field):
  original_quote, use_case, operation, boundary, why_valuable, cross_reference

Meta type: extraction_guide — methodology summary across a group of related chunks

Chunk addressing: <card_slug>/<chunk_type>/<NNN>

True atomic standard: each chunk = one independently citable, independently
verifiable, independently falsifiable unit.

Usage:
  python chunk_cards.py --card master-decision-hygiene --dry-run
  python chunk_cards.py --card dk-c10-batch-tool-no-dry-run --dry-run
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

# Heading → chunk type mapping (product track)
HEADING_TYPE_MAP = [
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
    # v1.3: process/error data recognition
    (r"(?i)修改|改前|改后|review|评审|决策理由|为什么.*改", "process_data"),
    (r"(?i)bad.?case|反例|不要用|not.?do|犯错|纠偏|踩坑|修正", "error_data"),
    # v1.3: dark-knowledge 6-field mapping
    (r"原始表述|原话|症状", "original_quote"),
    (r"使用场景|什么时候用|触发条件", "use_case"),
    (r"操作方法|具体做法|怎么做|步骤", "operation"),
    (r"适用边界|什么时候不|反例|前提|边界", "boundary"),
    (r"为什么值钱|为什么.*AI|暗知识价值", "why_valuable"),
    (r"与其他知识|关联|链接", "cross_reference"),
]

# Dark-knowledge card heading patterns
DK_HEADING_PATTERNS = {
    "原始表述": "original_quote",
    "使用场景": "use_case",
    "操作方法": "operation",
    "适用边界": "boundary",
    "为什么值钱": "why_valuable",
    "与其他知识的关联": "cross_reference",
}

# Chunk size targets for true atomic
MIN_ATOMIC_CHARS = 20
TARGET_MAX_CHARS = 200
MIN_CHUNK_CHARS_LEGACY = 50


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
    metadata = {}
    lines = raw_fm.split("\n")
    current_key = None
    current_list = []
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if current_key and stripped.startswith("- "):
            current_list.append(stripped[2:].strip().strip('"').strip("'"))
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


def is_dark_knowledge_card(metadata: dict) -> bool:
    """Check if this card is a dark-knowledge card."""
    return metadata.get("type") == "dark-knowledge"


def classify_heading(heading_text: str) -> str:
    """Classify a heading into a chunk type."""
    for pattern, chunk_type in HEADING_TYPE_MAP:
        if re.search(pattern, heading_text):
            return chunk_type
    return "claim"


def split_content_into_atoms(text: str, base_type: str) -> list[str]:
    """Split a section's content into atomic units at sentence/paragraph boundaries."""
    if not text.strip():
        return []

    # If already short enough, return as single atom
    if len(text) <= TARGET_MAX_CHARS:
        return [text.strip()]

    atoms = []

    # Try splitting by numbered list items first (1. / 1) / - / Step)
    if re.search(r"(?:^|\n)\s*(?:\d+[\.\)、]|[-•]\s|Step\s*\d)", text, re.MULTILINE):
        parts = re.split(r"\n\s*(?=\d+[\.\)、]|[-•]\s|Step\s*\d)", text)
    # Then try paragraph boundaries (double newline)
    elif "\n\n" in text:
        parts = text.split("\n\n")
    # Then try sentence boundaries (Chinese/English period + space or newline)
    else:
        parts = re.split(r"(?<=[。！？\.\!\?])\s*(?=[^\s])", text)

    for part in parts:
        part = part.strip()
        if not part:
            continue
        if len(part) < MIN_ATOMIC_CHARS:
            # Merge with previous atom
            if atoms:
                atoms[-1] = atoms[-1] + " " + part
            else:
                atoms.append(part)
        elif len(part) > TARGET_MAX_CHARS:
            # Recursively split further at CJK sentence boundaries
            sub_atoms = re.split(r"(?<=[。；])\s*", part)
            for sa in sub_atoms:
                sa = sa.strip()
                if sa and len(sa) >= MIN_ATOMIC_CHARS:
                    atoms.append(sa)
        else:
            atoms.append(part)

    return atoms


def chunk_card(filepath: Path, dry_run: bool = True, backup: bool = True) -> dict:
    """Chunk a single card at true atomic granularity."""
    stem = filepath.stem
    text = filepath.read_text(encoding="utf-8", errors="replace")
    metadata, body = parse_frontmatter(text)
    if not metadata:
        return {"file": str(filepath), "status": "skipped", "reason": "no frontmatter"}

    card_type = metadata.get("type", "concept")
    is_dk = is_dark_knowledge_card(metadata)

    # Split body into sections by headings
    sections = []
    current_heading = None
    current_lines = []
    for line in body.split("\n"):
        h_match = re.match(r"^(#{2,4})\s+(.+)", line)
        if h_match:
            if current_heading and current_lines:
                content = "\n".join(current_lines).strip()
                if content:
                    sections.append({"heading": current_heading, "content": content})
            current_heading = h_match.group(2).strip()
            current_lines = []
        else:
            current_lines.append(line)
    if current_heading and current_lines:
        content = "\n".join(current_lines).strip()
        if content:
            sections.append({"heading": current_heading, "content": content})
    if not sections:
        content = body.strip()
        if content:
            sections.append({"heading": "(no headings)", "content": content})

    # Build chunks
    type_counter = Counter()
    chunks = []
    inherited = {
        "domain": metadata.get("domain", []),
        "tags": metadata.get("tags", []),
        "confidence": metadata.get("confidence"),
        "trust_level": metadata.get("trust_level"),
        "source_refs": metadata.get("source_refs", []),
        "status": metadata.get("status"),
        "type": card_type,
    }
    if is_dk:
        inherited["dark_knowledge_type"] = metadata.get("dark_knowledge_type")
        inherited["source_person"] = metadata.get("source_person")

    for section in sections:
        heading = section["heading"]
        content = section["content"]

        # For dark-knowledge cards, use 6-field mapping
        if is_dk:
            for dk_heading, dk_type in DK_HEADING_PATTERNS.items():
                if dk_heading in heading:
                    chunk_type = dk_type
                    break
            else:
                chunk_type = classify_heading(heading)
        else:
            chunk_type = classify_heading(heading)

        # Split content into atomic units
        atoms = split_content_into_atoms(content, chunk_type)

        for atom in atoms:
            type_counter[chunk_type] += 1
            seq = type_counter[chunk_type]
            chunk_id = f"{stem}/{chunk_type}/{seq:03d}"

            # Build block-level tags (v1.3: multi-perspective placeholder)
            block_tags = list(inherited.get("tags", []))
            if chunk_type in ("error_data", "process_data"):
                if "#source_type/error" not in block_tags:
                    block_tags.append("#source_type/error")
            if chunk_type in ("original_quote",):
                if "#source_type/diverse" not in block_tags:
                    block_tags.append("#source_type/diverse")

            chunks.append({
                "chunk_id": chunk_id,
                "card_slug": stem,
                "chunk_type": chunk_type,
                "sequence": seq,
                "heading": heading,
                "content": atom,
                "char_count": len(atom),
                "inherited": dict(inherited),
                "block_tags": block_tags,
                # v1.3: reserved fields for multi-perspective tagging
                "perspectives": {},
            })

    result = {
        "file": str(filepath),
        "card_slug": stem,
        "card_type": card_type,
        "is_dark_knowledge": is_dk,
        "total_chunks": len(chunks),
        "by_type": dict(type_counter),
        "chunks": chunks,
    }

    if dry_run:
        print(f"\n--- {stem} ({card_type}) ---")
        print(f"  Chunks: {len(chunks)} (true atomic)")
        for ct, count in sorted(type_counter.items()):
            avg_len = sum(c["char_count"] for c in chunks if c["chunk_type"] == ct) // max(count, 1)
            print(f"    {ct}: {count} (avg ~{avg_len} chars)")
        return result

    # Write to state.json
    if backup and STATE_PATH.exists():
        backup_path = BACKUP_DIR / f"state-{stem}.json.bak"
        shutil.copy2(STATE_PATH, backup_path)
    return result


def update_state_json(card_chunks_list: list[dict]) -> dict:
    """Update .kdo/state.json with chunk registry entries."""
    if not STATE_PATH.exists():
        return {"error": "state.json not found"}
    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    if "chunks" not in state:
        state["chunks"] = {
            "registry_version": 2,
            "total_chunks": 0,
            "by_type": {},
            "entries": [],
        }
    for card_result in card_chunks_list:
        card_slug = card_result["card_slug"]
        state["chunks"]["entries"] = [
            e for e in state["chunks"]["entries"]
            if e.get("card_slug") != card_slug
        ]
        state["chunks"]["entries"].extend(card_result["chunks"])
    state["chunks"]["total_chunks"] = len(state["chunks"]["entries"])
    by_type = Counter()
    for entry in state["chunks"]["entries"]:
        by_type[entry["chunk_type"]] += 1
    state["chunks"]["by_type"] = dict(by_type)
    state["chunks"]["registry_version"] = 2
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
            card_id = args[i + 1]; i += 2
        elif args[i] == "--batch" and i + 1 < len(args):
            batch_size = int(args[i + 1]); i += 2
        elif args[i] == "--write":
            dry_run = False; i += 1
        elif args[i] == "--dry-run":
            dry_run = True; i += 1
        elif args[i] == "--no-backup":
            backup = False; i += 1
        else:
            i += 1

    if card_id:
        filepath = CONCEPTS_DIR / f"{card_id}.md"
        if not filepath.exists():
            print(f"ERROR: Card not found: {filepath}")
            sys.exit(1)
        result = chunk_card(filepath, dry_run=dry_run, backup=backup)
        if not dry_run and result.get("chunks"):
            updated_state = update_state_json([result])
            STATE_PATH.write_text(
                json.dumps(updated_state, ensure_ascii=False, indent=2), encoding="utf-8")
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
                STATE_PATH.write_text(
                    json.dumps(updated_state, ensure_ascii=False, indent=2), encoding="utf-8")
                print(f"\nState.json updated. Total chunks: {updated_state['chunks']['total_chunks']}")
    else:
        print("Usage: chunk_cards.py --card <id> | --batch <N> [--write|--dry-run] [--no-backup]")
        sys.exit(1)


if __name__ == "__main__":
    main()
