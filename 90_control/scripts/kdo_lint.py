#!/usr/bin/env python3
"""
Lint KDO vault pages against JSON Schemas.
Pure stdlib. No external dependencies.
Usage: python 90_control/scripts/kdo_lint.py [path_to_wiki]
"""

import json
import re
import sys
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
WIKI_DIR = VAULT_ROOT / "30_wiki"
SCHEMAS_DIR = VAULT_ROOT / "90_control" / "schemas"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
SOURCE_REF_RE = re.compile(r"^src_[0-9]{8}_[a-f0-9]{8}$")
WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")


def parse_yaml_frontmatter(text: str) -> dict:
    """Parse YAML frontmatter using stdlib yaml if available, else simple parser."""
    try:
        import yaml
        return yaml.safe_load(text) or {}
    except ImportError:
        # Fallback: simple parser for envs without PyYAML
        result = {}
        current_key = None
        current_list = []
        in_list = False
        for line in text.splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            if stripped.startswith("-"):
                item = stripped[1:].strip().strip('"').strip("'")
                current_list.append(item)
                in_list = True
            else:
                if in_list and current_key:
                    result[current_key] = current_list
                    current_list = []
                    in_list = False
                if ":" in stripped:
                    key, val = stripped.split(":", 1)
                    key = key.strip()
                    val = val.strip().strip('"').strip("'")
                    if val == "":
                        val = None
                    current_key = key
                    result[key] = val
        if in_list and current_key:
            result[current_key] = current_list
        return result


def load_schemas() -> dict:
    schemas = {}
    if not SCHEMAS_DIR.exists():
        return schemas
    for fp in SCHEMAS_DIR.glob("*.yaml"):
        # Since we can't parse YAML natively, we do a best-effort
        # Read the file and extract enums and required fields via regex
        text = fp.read_text(encoding="utf-8")
        schema_name = fp.stem
        schemas[schema_name] = parse_schema(text)
    return schemas


def parse_schema(text: str) -> dict:
    schema = {"required": [], "enums": {}, "patterns": {}, "types": {}}

    # Extract required fields
    req_match = re.search(r"required:\s*\n((?:\s*-\s*\S+\s*\n)+)", text)
    if req_match:
        for line in req_match.group(1).splitlines():
            m = re.match(r"\s*-\s*(\S+)", line)
            if m:
                schema["required"].append(m.group(1))

    # Split by field blocks (2-space indent)
    field_blocks = re.findall(r"^  (\w+):\s*\n((?:    .*\n)+)", text, re.MULTILINE)
    for field_name, block in field_blocks:
        # Check enum
        enum_match = re.search(r"enum:\s*\[([^\]]+)\]", block)
        if enum_match:
            values = [v.strip().strip('"').strip("'") for v in enum_match.group(1).split(",")]
            schema["enums"][field_name] = values

        # Check pattern
        pat_match = re.search(r'pattern:\s*"([^"]+)"', block)
        if pat_match:
            schema["patterns"][field_name] = pat_match.group(1)

    return schema


def check_source_refs_exist(fm: dict, rel: str) -> list:
    """检查 source_refs 指向的文件是否真实存在。（新增 2026-06-21）"""
    errors = []
    refs = fm.get("source_refs", [])
    if not refs:
        return errors
    if isinstance(refs, str):
        refs = [refs]

    for ref in refs:
        s = str(ref).strip()
        # 只检查文件路径类型的 source_ref
        if "/" not in s:
            continue
        # 跳过 wikilink 和 URL
        if s.startswith("[[") or s.startswith("http"):
            continue
        # 剥离行号锚点和括号注释后再验路径（欧阳锋 2026-07-12 bug report）
        # 三种格式: "路径.txt L240-L300（注释）" / "路径.txt:L2512-2891（注释）" / "路径.txt L240"
        clean = re.sub(r":L\d+[-–\d]*.*$", "", s)       # 冒号直连: .txt:L2512-2891（注释）
        clean = re.sub(r"\s+:?L\d+[-–\d]*.*$", "", clean)  # 空格+可选冒号
        clean = re.sub(r"\s+L\d+[-–\d]*.*$", "", clean)    # 纯空格:  L240-L300
        clean = re.sub(r"\s*[（(][^)）]*[)）]\s*$", "", clean)
        clean = clean.strip()
        candidate = VAULT_ROOT / clean
        if not candidate.exists():
            errors.append(f"{rel}: source_refs dead file: {s}")

    # 检查已知污染模式
    CONTAMINATION = "src_20260503_52ae08ba"
    for ref in refs:
        if CONTAMINATION in str(ref):
            errors.append(f"{rel}: source_refs contaminated: {str(ref)[:80]}")

    return errors


def validate_file(fp: Path, schemas: dict) -> list:
    errors = []
    rel = fp.relative_to(VAULT_ROOT).as_posix()
    try:
        content = fp.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        content = fp.read_text(encoding="utf-8", errors="replace")

    m = FRONTMATTER_RE.match(content)
    if not m:
        errors.append(f"{rel}: missing frontmatter")
        return errors

    try:
        fm = parse_yaml_frontmatter(m.group(1))
    except Exception as e:
        errors.append(f"{rel}: frontmatter parse error: {e}")
        return errors

    # 自审检测——"牲口而非宠物"原则（Harness Engineering 落地）
    author = str(fm.get("author", "")).strip().strip('"')
    reviewed_by = str(fm.get("reviewed_by", "")).strip().strip('"')
    if author and reviewed_by and author == reviewed_by and author not in ("黄药师", "欧阳锋"):
        errors.append(f"{rel}: SELF-REVIEW BLOCKED: author==reviewed_by=={author}. 写审必须分离——产卡Agent不得审查自己的卡片。")

    page_type = fm.get("type", "unknown")
    if isinstance(page_type, list):
        page_type = page_type[0] if page_type else "unknown"
    if not isinstance(page_type, str):
        page_type = str(page_type)
    schema = schemas.get(page_type) or schemas.get("concept")
    if not schema:
        return errors  # No schema to validate against

    # Check required fields
    for field in schema.get("required", []):
        if field not in fm or fm[field] is None:
            errors.append(f"{rel}: missing required field '{field}'")

    # Check enums
    for field, allowed in schema.get("enums", {}).items():
        val = fm.get(field)
        if val is not None and val not in allowed:
            errors.append(f"{rel}: field '{field}' has invalid value '{val}' (allowed: {allowed})")

    # 🆕 Check: enriched cards must have related links (Harness Engineering: 出链是知识可检索的基础)
    status = fm.get("status", "")
    related = fm.get("related", [])
    if isinstance(related, str):
        related = [related] if related.strip() else []
    if status == "enriched" and (not related or related == []):
        errors.append(f"{rel}: WARN: status=enriched but related is empty — card has no outgoing links")

    # 🆕 Check: agent-spec cards should declare TCPR role fields
    if isinstance(page_type, str) and "agent-spec" in page_type:
        for field in ("tcp_role", "tcp_default_mode", "tcp_switch_trigger", "tcp_session_opening"):
            if field not in fm or not fm[field]:
                errors.append(f"{rel}: WARN: agent-spec card missing TCPR field '{field}'")
        tcp_role = fm.get("tcp_role")
        if tcp_role is not None and tcp_role not in ("", "T", "C", "P", "R"):
            errors.append(f"{rel}: WARN: agent-spec tcp_role '{tcp_role}' invalid (must be T/C/P/R)")
        if "## TCPR 身份声明" not in content:
            errors.append(f"{rel}: WARN: agent-spec System Prompt missing TCPR identity declaration")

    # source_refs 文件存在性检查
    errors.extend(check_source_refs_exist(fm, rel))

    # F1: updated_at 必填（欧阳锋 F1 扣分项 — 2026-07-12 系统化 enforce）
    updated_at = fm.get("updated_at", "")
    if not updated_at or not str(updated_at).strip().strip("'\""):
        errors.append(f"{rel}: F1 VIOLATION: missing updated_at")

    return errors


def lint(wiki_dir: Path) -> dict:
    schemas = load_schemas()
    all_errors = []
    file_count = 0
    card_ids: set[str] = set()
    related_map: dict[str, list[str]] = {}  # card_id → list of related card_ids

    md_files = [f for f in wiki_dir.rglob("*.md") if "raw" not in f.parts and "_archive" not in f.parts]
    for fp in md_files:
        file_count += 1
        errs = validate_file(fp, schemas)
        all_errors.extend(errs)

        # Collect card metadata for F2 cross-check
        try:
            try:
                content = fp.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                content = fp.read_text(encoding="utf-8", errors="replace")
            m = FRONTMATTER_RE.match(content)
            if m:
                fm = parse_yaml_frontmatter(m.group(1))
                cid = fm.get("id", "")
                if not cid:
                    cid = fp.stem  # fallback: 用文件名作 id
                if cid:
                    card_ids.add(cid)
                    # 同时注册文件名（解决中文文件名引用）
                    card_ids.add(fp.stem)
                    related = fm.get("related", [])
                    if isinstance(related, str):
                        related = [related.strip().strip("'\"")] if related.strip() else []
                    elif isinstance(related, list):
                        related = [str(r).strip().strip("'\"") for r in related if r]
                    else:
                        related = []
                    # 清理 wikilink 格式: [[target|alias]] → target
                    cleaned_related = []
                    for r in related:
                        r = r.strip()
                        r = re.sub(r"^\[\[|\]\]$", "", r)  # 去 [[ 和 ]]
                        if "|" in r:
                            r = r.split("|")[0].strip()     # 去 alias
                        if r:
                            cleaned_related.append(r)
                    if cleaned_related:
                        related_map[cid] = cleaned_related
        except Exception:
            pass

    # F2: 双向 wikilink 完整性检查（欧阳锋 F2 扣分项 — 2026-07-12 系统化 enforce）
    f2_errors = []
    for cid, related_list in related_map.items():
        for target in related_list:
            # 跳过悬空占位符
            if target.startswith("<<") or not target:
                continue
            if target not in card_ids:
                # 断链：引用了不存在的卡
                f2_errors.append(f"F2 BROKEN LINK: {cid} → {target} (target card not found)")
            elif target in related_map:
                # 存在，检查回链
                target_related = related_map[target]
                if cid not in target_related:
                    f2_errors.append(f"F2 MISSING BACKLINK: {cid} → {target} (target has no backlink to {cid})")
    all_errors.extend(f2_errors)

    return {
        "files_checked": file_count,
        "errors": all_errors,
        "passed": len(all_errors) == 0,
    }


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    target = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else WIKI_DIR
    result = lint(target)

    print("=" * 50)
    print("KDO Lint Report")
    print("=" * 50)
    print(f"Files checked: {result['files_checked']}")
    print(f"Errors found:  {len(result['errors'])}")
    print(f"Status:        {'PASS' if result['passed'] else 'FAIL'}")
    print()

    if result["errors"]:
        for err in result["errors"]:
            print(f"  [ERROR] {err}")
        sys.exit(1)
    else:
        print("All checks passed.")
        sys.exit(0)


if __name__ == "__main__":
    main()
