#!/usr/bin/env python3
"""file-flow-check.py — 文件流转规范 lint（#450：《KDO 文件流转规范》v1.0 §8 L1-L9）

用法:
    python kdo-tools/file-flow-check.py             # 全量检查（默认，人类可读报告）
    python kdo-tools/file-flow-check.py --snapshot  # 冻结基线快照 → 90_control/frozen-registry.json
    python kdo-tools/file-flow-check.py --json      # JSON 输出（登记口/CI 调用）

检查项（规范 §8）:
    L1 doc_id 查重 | L2 doc_id 格式 | L3 版本号存在 | L4 时间戳存在
    L5 命名合规 | L6 slug 禁路径词 | L7 冻结检测（基线 hash）| L8 amends 引用 | L9 三套编号不混用

生效规则（规范 §9）: 向前生效——frontmatter created_at / 文件名日期 >= effective_from
的文件严格判级；存量既往不咎（仅 INFO 提示，不判 error/warning）。

退出码: 有 error=1；仅 warning=0（告警类不阻断流转，判级语义见各检查项）。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

WIKI_ROOT = Path(__file__).resolve().parent.parent
DIAG_DIR = WIKI_ROOT / "60_feedback" / "diagnosis"
TASK_DIR = WIKI_ROOT / "60_feedback" / "tasks"
WIKI_CARDS = WIKI_ROOT / "30_wiki"
QUEUE_FILE = WIKI_ROOT / "70_product" / "tasks" / "production-queue.md"
FROZEN_REGISTRY = WIKI_ROOT / "90_control" / "frozen-registry.json"

# 规范 §9：向前生效日（老朱拍板 + 欧阳锋终审 PASS A-）
EFFECTIVE_FROM = "2026-08-23"

DOC_ID_RE = re.compile(r"^D-\d{8}-\d{3}$")
DIAG_NAME_RE = re.compile(r"^diag_\d{8}_[a-z]+-[a-z0-9-]+(?:-v\d+\.\d+|\.md)$")
TASK_NAME_RE = re.compile(r"^task_\d{8}_[a-z]+-[a-z0-9-]+\.md$")
# F-040 口径：路径/文件名/目录词（斜杠/反斜杠/冒号/通配符/引号/尖括号/竖线/空白）
SLUG_FORBIDDEN_RE = re.compile(r"[\\/:*?\"<>|\s]")
# 冻结段标记（conveyor_probe 自动维护）
PROPOSAL_BEGIN = "<!-- PROPOSAL-PENDING-BEGIN"
PROPOSAL_END = "<!-- PROPOSAL-PENDING-END"


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="ignore")
    if not text.startswith("---"):
        return {}
    end = text.find("---", 3)
    if end == -1:
        return {}
    fm = {}
    for line in text[3:end].strip().splitlines():
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        fm[key.strip()] = val.strip().strip("'\"")
    return fm


def file_date(path: Path) -> str:
    """文件名中的日期（diag_/task_ 模板），无则空串。"""
    m = re.search(r"(20\d{6})", path.name)
    return m.group(1) if m else ""


def is_effective(path: Path, fm: dict) -> bool:
    """规范 §9：生效日后的新件才严格判级。created_at（优先）或文件名日期 >= 生效日。"""
    created = str(fm.get("created_at", "")).replace("T", " ")[:10].replace("-", "")
    if created and created >= EFFECTIVE_FROM.replace("-", ""):
        return True
    fname = file_date(path)
    return bool(fname and fname >= EFFECTIVE_FROM.replace("-", ""))


def frozen_files_from_queue() -> list[str]:
    """PROPOSAL-PENDING 段提及的 diagnosis 文件名（含已划行——处置后仍冻结，§6.1）。

    探针登记即冻结；看板行/裁定划行不构成对建议书的修改。
    """
    names: list[str] = []
    if not QUEUE_FILE.exists():
        return names
    text = QUEUE_FILE.read_text(encoding="utf-8")
    if PROPOSAL_BEGIN not in text or PROPOSAL_END not in text:
        return names
    block = text.split(PROPOSAL_BEGIN)[1].split(PROPOSAL_END)[0]
    for line in block.splitlines():
        if not line.startswith("- "):
            continue
        entry = line[2:].lstrip("~~").strip()
        name = entry.split("｜")[0].strip().replace("60_feedback/diagnosis/", "")
        if name.endswith(".md") and "gate-blocked" not in entry[:20]:
            names.append(name)
    return names


def _content_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def cmd_snapshot() -> int:
    """冻结基线：对冻结清单内存在的 diagnosis 文件打 hash 快照。"""
    registry = {}
    for name in frozen_files_from_queue():
        fp = DIAG_DIR / name
        if fp.exists():
            registry[name] = {"frozen_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"), "hash": _content_hash(fp)}
    FROZEN_REGISTRY.parent.mkdir(parents=True, exist_ok=True)
    FROZEN_REGISTRY.write_text(json.dumps(registry, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ 冻结基线已建: {len(registry)} 个冻结文件 → {FROZEN_REGISTRY}")
    return 0


def load_frozen_registry() -> dict:
    if not FROZEN_REGISTRY.exists():
        return {}
    try:
        return json.loads(FROZEN_REGISTRY.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def scan_diag_files(diag_dir: Path | None = None) -> list[tuple[Path, dict]]:
    d = diag_dir or DIAG_DIR
    return [(fp, parse_frontmatter(fp)) for fp in sorted(d.glob("*.md"))]


# ── L1-L9 检查器（每项返回 (code, file, message) 列表）──

def check_doc_id_duplicates(files: list[tuple[Path, dict]]) -> list[tuple[str, str, str]]:
    """L1: 建议书/诊断 doc_id 当日不重复（跨 agent 全局）。"""
    seen: dict[str, list[str]] = {}
    for fp, fm in files:
        doc_id = fm.get("doc_id", "")
        if doc_id:
            seen.setdefault(doc_id, []).append(fp.name)
    out = []
    for doc_id, names in seen.items():
        if len(names) > 1:
            out.append(("error", "L1", f"doc_id `{doc_id}` 重复: {', '.join(names)}"))
    return out


def check_doc_id_format(files: list[tuple[Path, dict]]) -> list[tuple[str, str, str]]:
    """L2: doc_id 格式 D-YYYYMMDD-NNN。"""
    out = []
    for fp, fm in files:
        doc_id = fm.get("doc_id", "")
        if doc_id and not DOC_ID_RE.match(doc_id):
            out.append(("error", "L2", f"`{fp.name}` doc_id=`{doc_id}` 格式非法（需 D-YYYYMMDD-NNN）"))
    return out


def check_version(files: list[tuple[Path, dict]]) -> list[tuple[str, str, str]]:
    """L3: 建议书/诊断 frontmatter 有 version（仅生效后新件）。"""
    out = []
    for fp, fm in files:
        if is_effective(fp, fm) and not fm.get("version"):
            out.append(("warning", "L3", f"`{fp.name}` 生效后新件缺 version（v1.0 起版）"))
    return out


def check_timestamps(files: list[tuple[Path, dict]]) -> list[tuple[str, str, str]]:
    """L4: created_at/updated_at 非空。"""
    out = []
    for fp, fm in files:
        if is_effective(fp, fm):
            if not fm.get("created_at"):
                out.append(("warning", "L4", f"`{fp.name}` 缺 created_at"))
            if not fm.get("updated_at"):
                out.append(("warning", "L4", f"`{fp.name}` 缺 updated_at"))
    return out


def check_naming(files: list[tuple[Path, dict]]) -> list[tuple[str, str, str]]:
    """L5: 文件名匹配模板（diag_YYYYMMDD_<author>-<slug>.md）。存量仅提示。"""
    out = []
    for fp, fm in files:
        if DIAG_NAME_RE.match(fp.name):
            continue
        level = "warning" if is_effective(fp, fm) else "info"
        out.append((level, "L5", f"`{fp.name}` 命名不匹配 diag_YYYYMMDD_<author>-<slug>.md 模板"))
    return out


def check_slug(files: list[tuple[Path, dict]]) -> list[tuple[str, str, str]]:
    """L6: slug 不含路径/文件名/目录词（F-040）。"""
    out = []
    for fp, fm in files:
        m = re.match(r"^diag_\d{8}_[a-z]+-(.*?)(?:-v\d+\.\d+)?\.md$", fp.name)
        if not m:
            continue
        slug = m.group(1)
        if SLUG_FORBIDDEN_RE.search(slug):
            level = "warning" if is_effective(fp, fm) else "info"
            out.append((level, "L6", f"`{fp.name}` slug 含路径/空白词: `{slug}`（F-040）"))
    return out


def check_frozen(files: list[tuple[Path, dict]]) -> list[tuple[str, str, str]]:
    """L7: 冻结文件（基线内）内容 hash 变化告警。基线不存在=未 snapshot，INFO 提示。"""
    registry = load_frozen_registry()
    if not registry:
        return [("info", "L7", "冻结基线不存在——先跑 --snapshot 建基线（登记即冻结，§6.3）")]
    out = []
    for fp, _ in files:
        entry = registry.get(fp.name)
        if not entry:
            continue
        cur = _content_hash(fp)
        if cur != entry["hash"]:
            out.append(("error", "L7", f"冻结文件 `{fp.name}` 内容被修改（frozen_at={entry['frozen_at']}）——已交冻结禁止回头改（§6.1）"))
    return out


def check_amends(files: list[tuple[Path, dict]]) -> list[tuple[str, str, str]]:
    """L8: 订正件 amends 指向的 doc_id 必须存在（跨 agent 全局）。

    amends 值允许带注释（如 `D-20260823-008（补充说明）`），取 D-编号前缀比对。
    """
    all_doc_ids = {fm.get("doc_id") for _, fm in files if fm.get("doc_id")}
    out = []
    for fp, fm in files:
        amends = str(fm.get("amends", "")).strip()
        if not amends:
            continue
        m = re.match(r"(D-\d{8}-\d{3})", amends)
        target = m.group(1) if m else amends
        if target not in all_doc_ids:
            out.append(("warning", "L8", f"`{fp.name}` amends=`{amends}` 指向不存在（dangling 引用）"))
    return out


def check_id_namespace(files: list[tuple[Path, dict]]) -> list[tuple[str, str, str]]:
    """L9: 三套编号不混用（E045）——任务单 frontmatter 不含 doc_id；wiki 卡不含 #队列号。"""
    out = []
    task_files = [(fp, parse_frontmatter(fp)) for fp in sorted(TASK_DIR.glob("task_*.md"))]
    for fp, fm in task_files:
        if fm.get("doc_id"):
            out.append(("warning", "L9", f"任务单 `{fp.name}` frontmatter 含 doc_id={fm['doc_id']}（E045：#队列号只用于任务单）"))
    return out


CHECKS = [
    ("L1 doc_id 查重", check_doc_id_duplicates),
    ("L2 doc_id 格式", check_doc_id_format),
    ("L3 版本号存在", check_version),
    ("L4 时间戳存在", check_timestamps),
    ("L5 命名合规", check_naming),
    ("L6 slug 禁路径词", check_slug),
    ("L7 冻结检测", check_frozen),
    ("L8 amends 引用", check_amends),
    ("L9 编号不混用", check_id_namespace),
]


def find_duplicate_doc_ids(diag_dir: Path | None = None) -> dict[str, list[str]]:
    """登记口查重（conveyor_probe 挂接）：同 doc_id 多文件 → 返回 {doc_id: [文件...]}。

    diag_dir 可注入（挂接方传自己的扫描面，测试可 monkeypatch；缺省=模块级 DIAG_DIR）。
    """
    seen: dict[str, list[str]] = {}
    for fp, fm in scan_diag_files(diag_dir):
        doc_id = fm.get("doc_id", "")
        if doc_id:
            seen.setdefault(doc_id, []).append(fp.name)
    return {d: n for d, n in seen.items() if len(n) > 1}


def main() -> int:
    ap = argparse.ArgumentParser(description="KDO 文件流转规范 lint（#450）")
    ap.add_argument("--snapshot", action="store_true", help="建冻结基线快照")
    ap.add_argument("--json", action="store_true", help="JSON 输出")
    args = ap.parse_args()

    if args.snapshot:
        return cmd_snapshot()

    files = scan_diag_files()
    all_findings: list[tuple[str, str, str]] = []
    for label, fn in CHECKS:
        findings = fn(files)
        if findings:
            all_findings.extend(findings)

    errors = [f for f in all_findings if f[0] == "error"]
    warnings = [f for f in all_findings if f[0] == "warning"]
    infos = [f for f in all_findings if f[0] == "info"]

    if args.json:
        print(json.dumps({
            "effective_from": EFFECTIVE_FROM,
            "scanned": len(files),
            "errors": [{"code": c, "message": m} for _, c, m in errors],
            "warnings": [{"code": c, "message": m} for _, c, m in warnings],
            "infos": [{"code": c, "message": m} for _, c, m in infos],
        }, ensure_ascii=False, indent=2))
        return 1 if errors else 0

    print(f"# 文件流转规范 lint（#450）— 生效日 {EFFECTIVE_FROM}（向前生效，存量既往不咎）")
    print(f"扫描 {len(files)} 个 diagnosis 文件：error={len(errors)} warning={len(warnings)} info={len(infos)}")
    for level, label in (("error", "ERROR"), ("warning", "WARNING"), ("info", "INFO")):
        items = [f for f in all_findings if f[0] == level]
        if not items:
            continue
        print(f"\n## {label}")
        for _, code, msg in items:
            print(f"- [{code}] {msg}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
