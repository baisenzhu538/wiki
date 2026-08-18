#!/usr/bin/env python3
"""把 .agent/*-context.md 汇总成一页摘要，避免一次性读多个 agent context 时 token 爆炸。"""
import re
from pathlib import Path
import yaml

AGENT_DIR = Path(".agent")
OUTPUT = AGENT_DIR / "agent-contexts-summary.md"

HEADINGS = re.compile(r"^##\s+(.+)$", re.MULTILINE)

def extract_sections(text: str):
    """按 ## 标题切分，返回 {标题: 内容}。"""
    matches = list(HEADINGS.finditer(text))
    sections = {}
    for i, m in enumerate(matches):
        title = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        sections[title] = body
    return sections

def first_lines(text: str, n: int = 3):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return " ".join(lines[:n])

def bullet_summary(text: str, max_items: int = 6):
    """提取列表项或短句作为 bullet。"""
    lines = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        # 去掉 markdown 列表标记
        if line.startswith(("- ", "* ", "1. ", "2. ", "3. ", "4. ", "5. ", "6. ")):
            line = re.sub(r"^[-*\d.]\s+", "", line)
        if line and len(line) > 8:
            lines.append(line)
    # 去重并限制数量
    seen = set()
    result = []
    for line in lines:
        if line not in seen and len(result) < max_items:
            seen.add(line)
            result.append(line)
    return result

def main():
    context_files = sorted(AGENT_DIR.glob("*-context.md"))
    summary_lines = [
        "---",
        "id: agent-contexts-summary",
        "type: agent_briefing",
        f"updated_at: {__import__('datetime').datetime.now(__import__('datetime').timezone.utc).strftime('%Y-%m-%dT%H:%M:%S')}",
        "---",
        "",
        "# Agent 启动摘要（一页纸）",
        "",
        "> 本文件由 `90_control/scripts/summarize-agent-contexts.py` 自动生成。",
        "> 需要某个角色的完整上下文时，再去读对应的 `.agent/<角色>-context.md`。",
        "",
    ]

    for path in context_files:
        text = path.read_text(encoding="utf-8")
        # frontmatter
        fm = {}
        if text.startswith("---\n"):
            end = text.find("\n---\n", 4)
            if end != -1:
                try:
                    fm = yaml.safe_load(text[4:end]) or {}
                except Exception:
                    pass

        role = fm.get("role", path.stem.replace("-context", ""))
        updated = fm.get("updated", "")
        sections = extract_sections(text)

        who = sections.get("你是谁", "")
        status = sections.get("当前状态", "")
        startup = sections.get("启动步骤", "") or sections.get("SOP", "")
        rules = sections.get("铁律", "")

        summary_lines.append(f"## {role}")
        summary_lines.append("")
        summary_lines.append(f"- **文件**: `{path.as_posix()}`")
        summary_lines.append(f"- **更新**: {updated}")
        if who:
            summary_lines.append(f"- **定位**: {first_lines(who)}")
        summary_lines.append("")

        if status:
            summary_lines.append("**当前状态**")
            for line in bullet_summary(status, max_items=4):
                summary_lines.append(f"- {line}")
            summary_lines.append("")

        if startup:
            summary_lines.append("**启动动作**")
            for line in bullet_summary(startup, max_items=4):
                summary_lines.append(f"- {line}")
            summary_lines.append("")

        if rules:
            summary_lines.append("**核心铁律**")
            for line in bullet_summary(rules, max_items=4):
                summary_lines.append(f"- {line}")
            summary_lines.append("")

    import hashlib, json, subprocess as _sp
    try:
        head = _sp.run(["git", "-C", str(AGENT_DIR.parent), "rev-parse", "--short", "HEAD"],
                       capture_output=True, text=True, timeout=10).stdout.strip()
    except Exception:
        head = "unknown"
    from datetime import datetime as _dt
    stamp = f"> generated-by: summarize-agent-contexts.py · updated_at: {_dt.now():%Y-%m-%d %H:%M} · git_head: {head}"
    OUTPUT.write_text("\n".join([stamp] + summary_lines), encoding="utf-8")
    hash_file = Path(__file__).resolve().parent / ".derived-hashes.json"
    hashes = {}
    if hash_file.exists():
        try:
            hashes = json.loads(hash_file.read_text(encoding="utf-8"))
        except Exception:
            pass
    hashes[str(OUTPUT)] = hashlib.sha256(OUTPUT.read_bytes()).hexdigest()
    hash_file.write_text(json.dumps(hashes, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"Summary written to {OUTPUT}")

if __name__ == "__main__":
    main()
