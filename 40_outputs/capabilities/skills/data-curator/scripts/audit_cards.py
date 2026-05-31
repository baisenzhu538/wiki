#!/usr/bin/env python3
"""Phase 1: Data Quality Audit Scanner.

Scans all concept cards in 30_wiki/concepts/ and produces a structured
data quality report. Read-only — never modifies files.

Usage:
  python audit_cards.py --scope all --output 60_feedback/data-quality/audit-YYYY-MM-DD.json
  python audit_cards.py --card master-systems-thinking
  python audit_cards.py --domain yitang
"""

import json
import os
import re
import sys
from datetime import date
from pathlib import Path
from collections import Counter, defaultdict

# --- Configuration ---

VAULT_ROOT = Path(r"C:\Users\Administrator\Desktop\wiki")
CONCEPTS_DIR = VAULT_ROOT / "30_wiki" / "concepts"
OUTPUT_DIR = VAULT_ROOT / "60_feedback" / "data-quality"

# Expected enum values from schema
VALID_STATUS = {"draft", "reviewed", "stable", "needs-review", "enriched"}
VALID_TYPE = {"concept", "entity", "comparison", "decision", "improvement-plan",
              "system", "trend", "tool", "framework"}
VALID_DOMAIN = {"master", "ai-saas", "healthcare", "yitang"}
VALID_DIFFICULTY = {"foundational", "intermediate", "advanced"}
VALID_TRUST_LEVEL = {"low", "medium", "high"}

# Fields expected to be present in every card
CORE_FIELDS = {"title", "type", "status", "source_refs", "created_at", "updated_at"}
ENRICHMENT_FIELDS = {"domain", "tags", "difficulty", "confidence", "trust_level",
                     "reviewed_by", "related", "prerequisites", "component_of",
                     "contradicts", "language", "version", "query_triggers"}
ALL_KNOWN_FIELDS = CORE_FIELDS | ENRICHMENT_FIELDS | {"id", "review_date",
    "estimated_tokens", "yitang", "visual_analysis", "entity_type", "aliases",
    "url", "location", "component_of", "supersedes", "based_on"}

# Standard date pattern
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ISO_DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}")


def parse_frontmatter(text: str) -> tuple[dict, str, str]:
    """Parse YAML frontmatter from markdown text.

    Returns (metadata_dict, body_text, raw_frontmatter_string).
    Handles both Gen A (YAML multi-line arrays) and Gen B (JSON-style inline arrays).
    """
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

    # Parse line by line, handling YAML multi-line arrays
    metadata = {}
    lines = raw_fm.split("\n")
    current_key = None
    current_list = []

    for line in lines:
        stripped = line.strip()

        # Skip empty lines and comments
        if not stripped or stripped.startswith("#"):
            continue

        # Multi-line list continuation (  - value)
        if current_key and stripped.startswith("- "):
            val = stripped[2:].strip().strip('"').strip("'")
            current_list.append(val)
            continue

        # Multi-line nested object continuation (  key: value)
        if current_key and line.startswith("  ") and ":" in stripped:
            # Store previous list if any
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

        # New key-value pair — flush previous list
        if current_key and current_list:
            metadata[current_key] = current_list
            current_list = []
            current_key = None

        if ":" not in stripped:
            continue

        key, raw_val = stripped.split(":", 1)
        key = key.strip()
        val = raw_val.strip()

        # JSON-style arrays and objects
        if val and val[0] in ("[", "{") or val in ("true", "false", "null"):
            try:
                metadata[key] = json.loads(val)
                current_key = None
                continue
            except json.JSONDecodeError:
                pass

        # Quoted strings
        if val and val[0] == '"' and val[-1] == '"':
            metadata[key] = val[1:-1]
            current_key = None
            continue
        if val and val[0] == "'" and val[-1] == "'":
            metadata[key] = val[1:-1]
            current_key = None
            continue

        # Numbers
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

        # Could be start of multi-line list (empty value after colon)
        if val == "" or val == "[]":
            current_key = key
            current_list = []
            continue

        # Plain scalar
        metadata[key] = val
        current_key = None

    # Flush final list
    if current_key and current_list:
        metadata[current_key] = current_list

    return metadata, body, raw_fm


def detect_format_issues(raw_fm: str, metadata: dict) -> list[dict]:
    """Detect formatting and value issues in a card's frontmatter."""
    issues = []

    # --- Curly quotes ---
    curly_quote_positions = []
    for i, line in enumerate(raw_fm.split("\n"), 1):
        if "“" in line or "”" in line:
            curly_quote_positions.append(i)
    if curly_quote_positions:
        issues.append({
            "type": "curly_quotes",
            "severity": "error",
            "lines": curly_quote_positions,
            "message": f"Curly quotes found on {len(curly_quote_positions)} line(s)"
        })

    # --- Inconsistent quoting in YAML values ---
    quoted_count = 0
    unquoted_count = 0
    for line in raw_fm.split("\n"):
        if ":" in line and not line.strip().startswith(("#", "-")):
            _, val = line.split(":", 1)
            val = val.strip()
            if val and val[0] == '"' and val[-1] == '"':
                quoted_count += 1
            elif val and val[0] != "[" and val[0] != "{":
                unquoted_count += 1
    if quoted_count > 0 and unquoted_count > 0:
        issues.append({
            "type": "mixed_quoting",
            "severity": "warning",
            "quoted": quoted_count,
            "unquoted": unquoted_count,
            "message": f"Mixed quoting: {quoted_count} quoted, {unquoted_count} unquoted values"
        })

    # --- Date format ---
    for field in ("created_at", "updated_at", "review_date"):
        if field in metadata:
            val = str(metadata[field])
            if ISO_DATE_PATTERN.match(val) and not DATE_PATTERN.match(val):
                issues.append({
                    "type": "date_iso_format",
                    "severity": "warning",
                    "field": field,
                    "value": val,
                    "message": f"{field} uses ISO timestamp, expected YYYY-MM-DD"
                })
            elif not DATE_PATTERN.match(val):
                issues.append({
                    "type": "date_unrecognized",
                    "severity": "warning",
                    "field": field,
                    "value": val,
                    "message": f"{field} has unrecognized date format"
                })

    # --- Decimal places on confidence ---
    if "confidence" in metadata:
        conf = metadata["confidence"]
        if isinstance(conf, (int, float)):
            conf_str = str(conf)
            if "." in conf_str:
                decimals = len(conf_str.split(".")[1])
                if decimals != 2:
                    issues.append({
                        "type": "decimal_places",
                        "severity": "warning",
                        "field": "confidence",
                        "value": conf_str,
                        "message": f"confidence has {decimals} decimal places, expected 2"
                    })

    # --- Domain as scalar instead of list ---
    if "domain" in metadata and metadata["domain"]:
        domain_val = metadata["domain"]
        if isinstance(domain_val, str):
            issues.append({
                "type": "domain_scalar",
                "severity": "warning",
                "value": domain_val,
                "message": "domain is a scalar, should be a list"
            })

    return issues


def detect_value_issues(metadata: dict) -> list[dict]:
    """Detect value-level issues (enum violations, dead fields, etc.)."""
    issues = []

    # --- Status enum ---
    if "status" in metadata:
        status = str(metadata["status"]).strip('"').strip("'")
        if status not in VALID_STATUS:
            issues.append({
                "type": "status_invalid",
                "severity": "warning",
                "value": status,
                "message": f"status '{status}' not in valid enum"
            })

    # --- Type enum ---
    if "type" in metadata:
        typ = str(metadata["type"]).strip('"').strip("'")
        if typ not in VALID_TYPE:
            issues.append({
                "type": "type_invalid",
                "severity": "warning",
                "value": typ,
                "message": f"type '{typ}' not in valid enum"
            })

    # --- Difficulty enum ---
    if "difficulty" in metadata and metadata["difficulty"]:
        diff = str(metadata["difficulty"]).strip('"').strip("'")
        if diff not in VALID_DIFFICULTY:
            issues.append({
                "type": "difficulty_invalid",
                "severity": "warning",
                "value": diff,
                "message": f"difficulty '{diff}' not in valid enum"
            })

    # --- Trust level enum ---
    if "trust_level" in metadata and metadata["trust_level"]:
        tl = str(metadata["trust_level"]).strip('"').strip("'")
        if tl not in VALID_TRUST_LEVEL:
            issues.append({
                "type": "trust_level_invalid",
                "severity": "warning",
                "value": tl,
                "message": f"trust_level '{tl}' not in valid enum"
            })

    # --- Domain enum ---
    if "domain" in metadata and metadata["domain"]:
        domain_val = metadata["domain"]
        if isinstance(domain_val, list):
            for d in domain_val:
                d_clean = str(d).strip('"').strip("'")
                if d_clean not in VALID_DOMAIN:
                    issues.append({
                        "type": "domain_invalid",
                        "severity": "warning",
                        "value": d_clean,
                        "message": f"domain value '{d_clean}' not in valid enum"
                    })
        elif isinstance(domain_val, str):
            if domain_val not in VALID_DOMAIN:
                issues.append({
                    "type": "domain_invalid",
                    "severity": "warning",
                    "value": domain_val,
                    "message": f"domain value '{domain_val}' not in valid enum"
                })

    # --- Contradicts is always empty (dead field) ---
    if "contradicts" in metadata:
        val = metadata["contradicts"]
        if isinstance(val, list) and len(val) == 0:
            issues.append({
                "type": "contradicts_dead_field",
                "severity": "info",
                "message": "contradicts field exists but is always empty"
            })

    # --- Tags not using hashtag convention ---
    if "tags" in metadata and metadata["tags"]:
        tags = metadata["tags"]
        if isinstance(tags, list):
            for tag in tags:
                tag_str = str(tag).strip('"').strip("'")
                if not tag_str.startswith("#"):
                    issues.append({
                        "type": "tag_no_hash",
                        "severity": "info",
                        "value": tag_str,
                        "message": f"tag '{tag_str}' missing # prefix"
                    })

    return issues


def detect_missing_fields(metadata: dict) -> list[dict]:
    """Detect missing expected fields."""
    issues = []

    for field in CORE_FIELDS:
        if field not in metadata or metadata[field] is None or metadata[field] == "":
            issues.append({
                "type": "missing_field",
                "severity": "error",
                "field": field,
                "message": f"Required field '{field}' is missing or empty"
            })

    for field in ENRICHMENT_FIELDS:
        if field not in metadata:
            issues.append({
                "type": "missing_field",
                "severity": "warning",
                "field": field,
                "message": f"Enrichment field '{field}' not present"
            })
        elif metadata[field] is None or metadata[field] == "" or metadata[field] == []:
            issues.append({
                "type": "empty_field",
                "severity": "warning",
                "field": field,
                "message": f"Enrichment field '{field}' is present but empty"
            })

    # id is not in schema but expected by convention
    if "id" not in metadata:
        issues.append({
            "type": "missing_field",
            "severity": "warning",
            "field": "id",
            "message": "id field is missing (convention, not schema-required)"
        })

    return issues


def classify_card_format(raw_fm: str, metadata: dict) -> str:
    """Classify card as Gen A (YAML multi-line) or Gen B (JSON-style inline)."""
    has_multiline_list = False
    for line in raw_fm.split("\n"):
        if line.startswith("  - "):
            has_multiline_list = True
            break

    has_json_array = False
    for line in raw_fm.split("\n"):
        if ":" in line:
            _, val = line.split(":", 1)
            val = val.strip()
            if val.startswith("[") and val.endswith("]"):
                has_json_array = True
                break

    if has_multiline_list:
        return "gen_a_yaml"
    elif has_json_array:
        return "gen_b_json"
    elif "domain" in metadata or "difficulty" in metadata or "confidence" in metadata:
        return "gen_a_yaml"
    else:
        return "gen_b_json"


def audit_card(filepath: Path) -> dict:
    """Run full audit on a single card."""
    try:
        text = filepath.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return {
            "file": str(filepath.relative_to(VAULT_ROOT)),
            "error": f"Failed to read: {e}",
            "issues": [{"type": "read_error", "severity": "error", "message": str(e)}]
        }

    metadata, body, raw_fm = parse_frontmatter(text)

    if not metadata:
        return {
            "file": str(filepath.relative_to(VAULT_ROOT)),
            "format": "no_frontmatter",
            "issues": [{"type": "no_frontmatter", "severity": "error",
                        "message": "No YAML frontmatter found"}]
        }

    format_type = classify_card_format(raw_fm, metadata)

    issues = []
    issues.extend(detect_missing_fields(metadata))
    issues.extend(detect_format_issues(raw_fm, metadata))
    issues.extend(detect_value_issues(metadata))

    # Count severity
    errors = sum(1 for i in issues if i["severity"] == "error")
    warnings = sum(1 for i in issues if i["severity"] == "warning")
    infos = sum(1 for i in issues if i["severity"] == "info")

    return {
        "file": str(filepath.relative_to(VAULT_ROOT)),
        "format": format_type,
        "fields_present": sorted(metadata.keys()),
        "fields_missing": sorted(ALL_KNOWN_FIELDS - set(metadata.keys())),
        "error_count": errors,
        "warning_count": warnings,
        "info_count": infos,
        "issues": issues
    }


def build_summary(results: list[dict]) -> dict:
    """Build aggregate statistics from per-card results."""
    total = len(results)
    format_counts = Counter(r.get("format", "unknown") for r in results)
    error_cards = sum(1 for r in results if r.get("error_count", 0) > 0)
    warning_cards = sum(1 for r in results if r.get("warning_count", 0) > 0)

    # Aggregate missing field counts
    missing_counts = Counter()
    empty_counts = Counter()
    for r in results:
        for issue in r.get("issues", []):
            if issue["type"] == "missing_field":
                missing_counts[issue["field"]] += 1
            elif issue["type"] == "empty_field":
                empty_counts[issue["field"]] += 1

    # Count issue types
    issue_type_counts = Counter()
    for r in results:
        for issue in r.get("issues", []):
            issue_type_counts[issue["type"]] += 1

    # Status distribution
    status_dist = Counter()
    for r in results:
        for field_info in r.get("fields_present", []):
            pass  # We need actual values, not just presence

    # Get actual status values from the issues/have to re-parse
    # For the summary, use issue-based counts

    return {
        "total_cards": total,
        "format_distribution": dict(format_counts),
        "cards_with_errors": error_cards,
        "cards_with_warnings": warning_cards,
        "cards_clean": total - error_cards - warning_cards,
        "top_missing_fields": dict(missing_counts.most_common(15)),
        "top_empty_fields": dict(empty_counts.most_common(10)),
        "issue_type_distribution": dict(issue_type_counts.most_common(20)),
    }


def get_field_value_distribution(results: list[dict], field: str) -> dict:
    """Get actual value distribution for a field across all cards."""
    dist = Counter()
    for r in results:
        filepath = VAULT_ROOT / r["file"]
        if filepath.exists():
            text = filepath.read_text(encoding="utf-8", errors="replace")
            metadata, _, _ = parse_frontmatter(text)
            if field in metadata:
                val = metadata[field]
                if isinstance(val, list):
                    for v in val:
                        dist[str(v).strip('"').strip("'")] += 1
                else:
                    dist[str(val).strip('"').strip("'")] += 1
            else:
                dist["<missing>"] += 1
    return dict(dist.most_common())


def scan_concept_cards() -> list[Path]:
    """Find all concept card files."""
    cards = []
    for filepath in CONCEPTS_DIR.glob("*.md"):
        cards.append(filepath)
    return sorted(cards)


def main():
    scope = "all"
    card_id = None
    output_path = None

    # Parse args
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--scope" and i + 1 < len(args):
            scope = args[i + 1]
            i += 2
        elif args[i] == "--card" and i + 1 < len(args):
            card_id = args[i + 1]
            i += 2
        elif args[i] == "--output" and i + 1 < len(args):
            output_path = args[i + 1]
            i += 2
        else:
            i += 1

    # Find cards to audit
    if card_id:
        filepath = CONCEPTS_DIR / f"{card_id}.md"
        if not filepath.exists():
            print(f"ERROR: Card not found: {filepath}")
            sys.exit(1)
        cards = [filepath]
    else:
        cards = scan_concept_cards()

    print(f"Auditing {len(cards)} card(s)...")

    # Run audit
    results = []
    for card_path in cards:
        result = audit_card(card_path)
        results.append(result)

    # Build report
    summary = build_summary(results)

    # Add value distributions for key fields
    value_distributions = {}
    for field in ("status", "type", "domain", "difficulty", "trust_level", "language"):
        value_distributions[field] = get_field_value_distribution(results, field)

    report = {
        "generated_at": date.today().isoformat(),
        "scope": scope,
        "card_count": len(results),
        "summary": summary,
        "value_distributions": value_distributions,
        "results": results
    }

    # Output
    if output_path:
        output_file = VAULT_ROOT / output_path if not os.path.isabs(output_path) else Path(output_path)
    else:
        today = date.today().isoformat()
        output_file = OUTPUT_DIR / f"audit-{today}.json"

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    # Print summary to stdout
    print(f"\n=== AUDIT SUMMARY ===")
    print(f"Total cards: {summary['total_cards']}")
    print(f"Format: Gen A (YAML) = {summary['format_distribution'].get('gen_a_yaml', 0)}, "
          f"Gen B (JSON) = {summary['format_distribution'].get('gen_b_json', 0)}")
    print(f"Cards with errors: {summary['cards_with_errors']}")
    print(f"Cards with warnings: {summary['cards_with_warnings']}")
    print(f"Cards clean: {summary['cards_clean']}")
    print(f"\nTop missing fields:")
    for field, count in summary["top_missing_fields"].items():
        print(f"  {field}: {count}")
    print(f"\nTop empty fields:")
    for field, count in summary["top_empty_fields"].items():
        print(f"  {field}: {count}")
    print(f"\nStatus distribution:")
    for status, count in value_distributions.get("status", {}).items():
        print(f"  {status}: {count}")
    print(f"\nFull report: {output_file}")


if __name__ == "__main__":
    main()
