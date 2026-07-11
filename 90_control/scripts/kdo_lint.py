#!/usr/bin/env python3
"""
Lint KDO vault pages against JSON Schemas.
Pure stdlib. No external dependencies.

Usage:
  python kdo_lint.py                          # 全量 lint
  python kdo_lint.py --baseline               # 记录当前错误为基线
  python kdo_lint.py --incremental            # 只报基线之外的新增错误
  python kdo_lint.py --incremental --baseline # 更新基线（修完一批卡后）
  python kdo_lint.py 30_wiki/frameworks/      # scoped 抽检（指定目录/文件）
"""

import argparse
import fnmatch
import json
import re
import sys
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
WIKI_DIR = VAULT_ROOT / "30_wiki"
SCHEMAS_DIR = VAULT_ROOT / "90_control" / "schemas"
BASELINE_FILE = VAULT_ROOT / "90_control" / ".lint_baseline.json"
EXCEPTIONS_FILE = VAULT_ROOT / "90_control" / ".lint_exceptions.json"

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


def lint(target: Path) -> dict:
    schemas = load_schemas()
    all_errors = []
    file_count = 0
    card_ids: set[str] = set()
    related_map: dict[str, list[str]] = {}  # card_id → list of related card_ids

    if target.is_file():
        md_files = [target]
    elif target.is_dir():
        md_files = [f for f in target.rglob("*.md") if "raw" not in f.parts and "_archive" not in f.parts]
    else:
        # 可能是多个路径（shell glob 展开）
        return {"files_checked": 0, "errors": [], "passed": True}
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


# ── 基线 / 增量 / 例外 ──────────────────────────────────────

def error_signature(error: str) -> str:
    """提取错误的稳定签名——用于跨基线去重。
    F2: "F2 BROKEN LINK: A → B (...)" → "F2_BROKEN: A→B"
    F1: "path: F1 VIOLATION: ..." → "F1: path"
    其他: 取前 120 字符归一化空白。
    """
    e = " ".join(error.split())  # normalize whitespace
    m = re.match(r"^(F2 (?:BROKEN LINK|MISSING BACKLINK)):\s*(\S+)\s*→\s*(\S+)", e)
    if m:
        return f"{m.group(1).replace(' ', '_')}: {m.group(2)}→{m.group(3)}"
    m = re.match(r"^(\S+):\s*(F1 VIOLATION:.*)", e)
    if m:
        return f"F1: {m.group(1)}"
    return e[:120]


def save_baseline(errors: list[str], file_count: int):
    """保存当前全量错误为基线。"""
    sigs = sorted(set(error_signature(e) for e in errors))
    BASELINE_FILE.write_text(
        json.dumps({
            "created_at": __import__("datetime").datetime.now().isoformat(),
            "file_count": file_count,
            "error_count": len(sigs),
            "signatures": sigs,
        }, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Baseline saved: {len(sigs)} unique error signatures from {file_count} files → {BASELINE_FILE}")


def load_baseline() -> set[str]:
    """加载基线签名集合。"""
    if not BASELINE_FILE.exists():
        return set()
    try:
        data = json.loads(BASELINE_FILE.read_text(encoding="utf-8"))
        return set(data.get("signatures", []))
    except Exception:
        return set()


def load_exceptions() -> dict[str, list[dict]]:
    """加载例外清单。
    格式: {"f2_broken": [{"from": "glob", "to": "glob", "reason": "..."}],
            "f2_missing": [...],
            "f1": [{"card": "glob", "reason": "..."}],
            "source_refs": [{"card": "glob", "reason": "..."}]}
    如果文件不存在，返回空规则并创建模板文件。
    """
    if not EXCEPTIONS_FILE.exists():
        template = {
            "_doc": "例外清单——匹配的 lint 错误不被报告。glob 用 fnmatch 语法（* 通配）。",
            "f2_broken": [],
            "f2_missing": [
                {"from": "*-domain-digest", "to": "*", "reason": "digest 卡为导航索引，不要求域内卡片回链"},
                {"from": "*", "to": "xingangwan-*", "reason": "EC 线独立域，王语嫣裁定不互链"},
                {"from": "concept-card-index-*", "to": "*", "reason": "总索引→全部内容，不要求回链"},
            ],
            "f1": [],
            "source_refs": [],
        }
        EXCEPTIONS_FILE.write_text(
            json.dumps(template, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        return {k: v for k, v in template.items() if not k.startswith("_")}

    try:
        data = json.loads(EXCEPTIONS_FILE.read_text(encoding="utf-8"))
        return {k: v for k, v in data.items() if not k.startswith("_")}
    except Exception:
        return {}


def match_glob(pattern: str, value: str) -> bool:
    """fnmatch 包装——空 pattern 匹配一切。"""
    if not pattern or pattern == "*":
        return True
    return fnmatch.fnmatch(value, pattern)


def is_exempted(error: str, exceptions: dict) -> bool:
    """判断一条错误是否命中例外规则。"""
    e = " ".join(error.split())

    # F2 BROKEN LINK: path: F2 BROKEN LINK: A → B (...)
    m = re.match(r".*F2 BROKEN LINK:\s*(\S+)\s*→\s*(\S+)", e)
    if m:
        frm, to = m.group(1), m.group(2)
        for rule in exceptions.get("f2_broken", []):
            if match_glob(rule.get("from", "*"), frm) and match_glob(rule.get("to", "*"), to):
                return True

    # F2 MISSING BACKLINK
    m = re.match(r".*F2 MISSING BACKLINK:\s*(\S+)\s*→\s*(\S+)", e)
    if m:
        frm, to = m.group(1), m.group(2)
        for rule in exceptions.get("f2_missing", []):
            if match_glob(rule.get("from", "*"), frm) and match_glob(rule.get("to", "*"), to):
                return True

    # F1 VIOLATION
    m = re.match(r"^(\S+):\s*F1 VIOLATION:", e)
    if m:
        card_path = m.group(1)
        for rule in exceptions.get("f1", []):
            if match_glob(rule.get("card", "*"), card_path):
                return True

    # source_refs dead file
    m = re.match(r"^(\S+):\s*source_refs dead file:", e)
    if m:
        card_path = m.group(1)
        for rule in exceptions.get("source_refs", []):
            if match_glob(rule.get("card", "*"), card_path):
                return True

    return False


def filter_errors(errors: list[str], baseline: set[str], exceptions: dict, incremental: bool) -> tuple[list[str], int, int, int]:
    """过滤错误：先应用例外，再（可选）去基线。
    返回: (filtered_errors, exempted_count, baseline_count, new_count)
    """
    exempted = 0
    post_exceptions = []
    for e in errors:
        if is_exempted(e, exceptions):
            exempted += 1
        else:
            post_exceptions.append(e)

    if not incremental or not baseline:
        return post_exceptions, exempted, 0, len(post_exceptions)

    new_errors = []
    baseline_hits = 0
    for e in post_exceptions:
        if error_signature(e) in baseline:
            baseline_hits += 1
        else:
            new_errors.append(e)

    return new_errors, exempted, baseline_hits, len(new_errors)


# ── main ─────────────────────────────────────────────────────

def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="KDO Lint — vault page quality checker")
    parser.add_argument("target", nargs="?", default=None,
                        help="目标目录或文件（默认 30_wiki）")
    parser.add_argument("--baseline", action="store_true",
                        help="记录当前全量错误为基线（覆盖旧基线）")
    parser.add_argument("--incremental", action="store_true",
                        help="只报告基线之外的新增错误")
    args = parser.parse_args()

    target = Path(args.target).resolve() if args.target else WIKI_DIR
    result = lint(target)

    # 加载基线 & 例外
    baseline = load_baseline() if args.incremental else set()
    exceptions = load_exceptions() if not args.baseline else {}

    filtered, exempted, baseline_hits, new_count = filter_errors(
        result["errors"], baseline, exceptions,
        incremental=args.incremental,
    )

    # ── 保存基线 ──
    if args.baseline:
        save_baseline(result["errors"], result["files_checked"])
        print()
        # baseline 模式下也输出正常报告
        args.incremental = False  # 不减，展示全貌

    # ── 报告 ──
    total = len(result["errors"])
    mode = []
    if exempted:
        mode.append(f"{exempted} exempted")
    if args.incremental and baseline:
        mode.append(f"{baseline_hits} in baseline")
    if args.incremental:
        mode.append("INCREMENTAL")
    mode_str = f"  ({', '.join(mode)})" if mode else ""

    print("=" * 50)
    print("KDO Lint Report" + mode_str)
    print("=" * 50)
    print(f"Files checked: {result['files_checked']}")
    print(f"Total errors:  {total}")
    if exempted:
        print(f"Exempted:      {exempted}")
    if args.incremental and baseline:
        print(f"In baseline:   {baseline_hits}")
    print(f"New errors:    {new_count}")
    print(f"Status:        {'PASS' if new_count == 0 else 'FAIL'}")
    print()

    if filtered:
        for err in filtered:
            print(f"  [ERROR] {err}")
        sys.exit(1)
    else:
        if args.incremental and baseline:
            print("No new errors since baseline.")
        elif exempted and not filtered:
            print("All errors exempted or in baseline.")
        else:
            print("All checks passed.")
        sys.exit(0)


if __name__ == "__main__":
    main()
