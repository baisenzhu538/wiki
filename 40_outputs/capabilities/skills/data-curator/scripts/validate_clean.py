#!/usr/bin/env python3
"""Phase 5: Post-Cleaning Validation.

Validates all cleaned/tagged/chunked cards against quality dimensions:
  - domain non-empty
  - tags non-empty and in controlled vocabulary
  - chunks registered in state.json
  - chunk IDs unique and traceable
  - source_refs non-empty on all chunks

Outputs a pass/fail matrix: rows=cards, columns=dimensions, cells=PASS/FAIL.

Usage:
  python validate_clean.py --all --output 60_feedback/data-quality/validate-YYYY-MM-DD.json
  python validate_clean.py --card master-systems-thinking
"""

import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

# --- Configuration ---

VAULT_ROOT = Path(r"C:\Users\Administrator\Desktop\wiki")
CONCEPTS_DIR = VAULT_ROOT / "30_wiki" / "concepts"
STATE_PATH = VAULT_ROOT / ".kdo" / "state.json"
TAG_REGISTRY_PATH = VAULT_ROOT / "90_control" / "tag-registry.yaml"
OUTPUT_DIR = VAULT_ROOT / "60_feedback" / "data-quality"

# Validation dimensions
DIMENSIONS = [
    "frontmatter_exists",
    "core_fields_present",
    "domain_nonempty",
    "domain_valid_enum",
    "tags_nonempty",
    "tags_in_registry",
    "source_refs_nonempty",
    "status_valid",
    "type_valid",
    "chunks_exist",
    "chunk_ids_unique",
    "chunk_source_refs_inherited",
]


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Parse YAML frontmatter."""
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


def load_valid_tags() -> set[str]:
    """Load valid tags from registry."""
    if not TAG_REGISTRY_PATH.exists():
        return set()

    text = TAG_REGISTRY_PATH.read_text(encoding="utf-8")
    valid_tags = set()
    in_values = False

    for line in text.split("\n"):
        stripped = line.strip()
        if stripped.startswith("values:"):
            in_values = True
            continue
        if in_values:
            if stripped.startswith("- ") and stripped[2:].startswith("#"):
                valid_tags.add(stripped[2:].strip())
            elif not stripped.startswith("- ") and ":" in stripped and not stripped.startswith("#"):
                in_values = False

    return valid_tags


def load_chunk_registry() -> dict:
    """Load chunk registry from state.json."""
    if not STATE_PATH.exists():
        return {"entries": []}
    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    return state.get("chunks", {"entries": []})


def validate_card(filepath: Path, valid_tags: set[str], chunk_registry: dict) -> dict:
    """Validate a single card against all dimensions."""
    stem = filepath.stem

    try:
        text = filepath.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return {"file": stem, "error": str(e), "results": {}}

    metadata, body = parse_frontmatter(text)
    results = {}

    # D1: Frontmatter exists
    results["frontmatter_exists"] = "PASS" if metadata else "FAIL"

    if not metadata:
        return {"file": stem, "results": results, "overall": "FAIL"}

    # D2: Core fields present
    core = {"title", "type", "status", "source_refs", "created_at", "updated_at"}
    missing_core = [f for f in core if f not in metadata or not metadata.get(f)]
    results["core_fields_present"] = "PASS" if not missing_core else f"FAIL (missing: {missing_core})"

    # D3: Domain non-empty
    domain = metadata.get("domain", [])
    if isinstance(domain, str):
        domain = [domain]
    results["domain_nonempty"] = "PASS" if domain and len(domain) > 0 else "FAIL"

    # D4: Domain valid enum
    valid_domains = {"master", "ai-saas", "healthcare", "yitang"}
    if domain:
        invalid = [d for d in domain if str(d).strip('"').strip("'") not in valid_domains]
        results["domain_valid_enum"] = "PASS" if not invalid else f"FAIL (invalid: {invalid})"
    else:
        results["domain_valid_enum"] = "SKIP (no domain)"

    # D5: Tags non-empty
    tags = metadata.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    tags = [str(t).strip('"').strip("'") for t in tags if t]
    results["tags_nonempty"] = "PASS" if tags else "FAIL"

    # D6: Tags in registry
    if tags and valid_tags:
        invalid_tags = [t for t in tags if t not in valid_tags and not t.startswith("#")]
        results["tags_in_registry"] = "PASS" if not invalid_tags else f"FAIL (invalid: {invalid_tags})"
    elif tags and not valid_tags:
        results["tags_in_registry"] = "SKIP (no registry)"
    else:
        results["tags_in_registry"] = "SKIP (no tags)"

    # D7: Source refs non-empty
    source_refs = metadata.get("source_refs", [])
    if isinstance(source_refs, str):
        source_refs = [source_refs]
    source_refs = [s for s in source_refs if s]
    results["source_refs_nonempty"] = "PASS" if source_refs else "FAIL"

    # D8: Status valid
    valid_status = {"draft", "reviewed", "stable", "needs-review", "enriched"}
    status = str(metadata.get("status", "")).strip('"').strip("'")
    results["status_valid"] = "PASS" if status in valid_status else f"FAIL ('{status}')"

    # D9: Type valid
    valid_types = {"concept", "entity", "comparison", "decision", "improvement-plan",
                   "system", "trend", "tool", "framework"}
    typ = str(metadata.get("type", "")).strip('"').strip("'")
    results["type_valid"] = "PASS" if typ in valid_types else f"FAIL ('{typ}')"

    # D10: Chunks exist in registry
    card_chunks = [e for e in chunk_registry.get("entries", []) if e.get("card_slug") == stem]
    results["chunks_exist"] = "PASS" if card_chunks else "FAIL"

    # D11: Chunk IDs unique
    if card_chunks:
        chunk_ids = [c["chunk_id"] for c in card_chunks]
        duplicates = [cid for cid, count in Counter(chunk_ids).items() if count > 1]
        results["chunk_ids_unique"] = "PASS" if not duplicates else f"FAIL (dupes: {duplicates})"
    else:
        results["chunk_ids_unique"] = "SKIP (no chunks)"

    # D12: Chunk source_refs inherited
    if card_chunks:
        missing_refs = [c["chunk_id"] for c in card_chunks
                        if not c.get("inherited", {}).get("source_refs")]
        results["chunk_source_refs_inherited"] = "PASS" if not missing_refs else f"FAIL ({len(missing_refs)} chunks)"
    else:
        results["chunk_source_refs_inherited"] = "SKIP (no chunks)"

    # Overall
    fails = sum(1 for v in results.values() if str(v).startswith("FAIL"))
    overall = "PASS" if fails == 0 else "FAIL"

    return {"file": stem, "results": results, "overall": overall, "fail_count": fails}


def main():
    card_id = None
    output_path = None

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--card" and i + 1 < len(args):
            card_id = args[i + 1]
            i += 2
        elif args[i] == "--all":
            card_id = None
            i += 1
        elif args[i] == "--output" and i + 1 < len(args):
            output_path = args[i + 1]
            i += 2
        else:
            i += 1

    valid_tags = load_valid_tags()
    chunk_registry = load_chunk_registry()
    print(f"Tag registry: {'loaded' if valid_tags else 'NOT FOUND'} ({len(valid_tags)} tags)")
    print(f"Chunk registry: {chunk_registry.get('total_chunks', 0)} total chunks\n")

    if card_id:
        filepath = CONCEPTS_DIR / f"{card_id}.md"
        if not filepath.exists():
            print(f"ERROR: Card not found: {filepath}")
            sys.exit(1)
        cards = [filepath]
    else:
        cards = sorted(CONCEPTS_DIR.glob("*.md"))

    print(f"Validating {len(cards)} card(s)...\n")

    results = []
    for card_path in cards:
        result = validate_card(card_path, valid_tags, chunk_registry)
        results.append(result)

        # Print summary line
        status_icon = "✓" if result["overall"] == "PASS" else "✗"
        fails_detail = ""
        if result["overall"] == "FAIL":
            failing_dims = [k for k, v in result["results"].items() if str(v).startswith("FAIL")]
            fails_detail = f" [{', '.join(failing_dims[:3])}]"
        print(f"  {status_icon} {result['file']}: {result['overall']}{fails_detail}")

    # Summary statistics
    total = len(results)
    passed = sum(1 for r in results if r["overall"] == "PASS")
    failed = total - passed
    pass_rate = (passed / total * 100) if total > 0 else 0

    # Dimension-level pass rates
    dim_counts = defaultdict(lambda: {"pass": 0, "fail": 0, "skip": 0})
    for r in results:
        for dim, val in r["results"].items():
            if str(val).startswith("FAIL"):
                dim_counts[dim]["fail"] += 1
            elif str(val).startswith("PASS"):
                dim_counts[dim]["pass"] += 1
            else:
                dim_counts[dim]["skip"] += 1

    print(f"\n=== VALIDATION SUMMARY ===")
    print(f"Total cards: {total}")
    print(f"Passed: {passed} ({pass_rate:.1f}%)")
    print(f"Failed: {failed} ({100 - pass_rate:.1f}%)")
    print(f"\nDimension pass rates:")
    for dim in DIMENSIONS:
        counts = dim_counts[dim]
        applicable = counts["pass"] + counts["fail"]
        if applicable > 0:
            dim_rate = counts["pass"] / applicable * 100
            print(f"  {dim}: {dim_rate:.1f}% ({counts['pass']}/{applicable})")
        else:
            print(f"  {dim}: N/A (all skipped)")

    # Output report
    if output_path:
        output_file = VAULT_ROOT / output_path
    else:
        today = date.today().isoformat()
        output_file = OUTPUT_DIR / f"validate-{today}.json"

    report = {
        "generated_at": date.today().isoformat(),
        "total_cards": total,
        "passed": passed,
        "failed": failed,
        "pass_rate": round(pass_rate, 1),
        "dimension_summary": {
            dim: {
                "pass": dim_counts[dim]["pass"],
                "fail": dim_counts[dim]["fail"],
                "skip": dim_counts[dim]["skip"],
                "pass_rate": round(
                    dim_counts[dim]["pass"] / (dim_counts[dim]["pass"] + dim_counts[dim]["fail"]) * 100, 1
                ) if (dim_counts[dim]["pass"] + dim_counts[dim]["fail"]) > 0 else None
            }
            for dim in DIMENSIONS
        },
        "results": results
    }

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nFull report: {output_file}")


if __name__ == "__main__":
    main()
