#!/usr/bin/env python3
"""
Agent Prompt Compiler: build injectable system prompts for Kimi/Hermes agents.

Usage:
  python kdo-tools/agent-prompt-compiler.py <agent-id> [--dry-run]

Reads an agent-spec card's frontmatter fields (os_sources, domain_sources,
user_sources) and compiles them into a single system prompt file at
.agent/prompts/<agent-id>.md.  Handles both Claude-native agents (that can
Read files) and Kimi/Hermes agents (that need static prompt injection).
"""

import argparse
import hashlib
import sys
from datetime import datetime, timezone
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent
PROMPTS_DIR = WIKI / ".agent" / "prompts"
TOOLS_DIR = WIKI / "30_wiki" / "tools"
SYSTEMS_DIR = WIKI / "30_wiki" / "systems"

# Default OS-level sources loaded for every agent
DEFAULT_OS_SOURCES = [
    "30_wiki/systems/system-yitang-Y-model-os.md",
    "agents/agent-os.md",
]


def parse_frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    import yaml
    return yaml.safe_load(parts[1]) or {}, parts[2]


def read_content(path: Path) -> str:
    """Read a source file, returning body only for .md cards."""
    text = path.read_text(encoding="utf-8", errors="ignore")
    if path.suffix == ".md" and text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[2].strip()
    return text


def hash_content(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def estimate_tokens(text: str) -> int:
    # Rough: Chinese ~1.5 chars/token, English ~4 chars/token
    return len(text) // 2


def find_agent_card(agent_id: str) -> Path | None:
    """Find an agent-spec card by id in tools/ or systems/."""
    for d in (TOOLS_DIR, SYSTEMS_DIR):
        for p in d.glob("*.md"):
            fm, _ = parse_frontmatter(p)
            if fm.get("id") == agent_id:
                return p
    return None


def compile_prompt(agent_id: str, dry_run: bool = False) -> str | None:
    """Compile a system prompt for an agent. Returns the compiled text."""
    card_path = find_agent_card(agent_id)
    if card_path is None:
        print(f"ERROR: Agent card not found: {agent_id}", file=sys.stderr)
        return None

    fm, body = parse_frontmatter(card_path)
    title = fm.get("title", agent_id)
    tcp_role = fm.get("tcp_role", "C")

    # Gather sources
    os_sources = fm.get("os_sources", DEFAULT_OS_SOURCES)
    domain_sources = fm.get("domain_sources", [])
    user_sources = fm.get("user_sources", [])

    sections = []
    total_tokens = 0

    # ── Header ──
    now = datetime.now(timezone.utc).isoformat()
    sections.append(f"# {title} — 编译后 System Prompt\n")
    sections.append(f"> 编译时间: {now}")
    sections.append(f"> Agent ID: {agent_id}")
    sections.append(f"> TCPR 默认身份: {tcp_role}\n")

    # ── OS Layer ──
    sections.append("---\n## 元层：共享 OS\n")
    for src_rel in os_sources:
        src_path = WIKI / src_rel
        if not src_path.exists():
            print(f"WARNING: OS source not found: {src_rel}", file=sys.stderr)
            continue
        content = read_content(src_path)
        h = hash_content(content)
        tk = estimate_tokens(content)
        total_tokens += tk
        sections.append(f"<!-- source: {src_rel} hash:{h} -->\n")
        sections.append(content)
        sections.append("")

    # ── Domain Layer ──
    sections.append("---\n## 域层：领域专业知识\n")
    # Always include the agent-spec card itself
    domain_content = read_content(card_path)
    h = hash_content(domain_content)
    tk = estimate_tokens(domain_content)
    total_tokens += tk
    sections.append(f"<!-- source: {card_path.relative_to(WIKI)} hash:{h} -->\n")
    sections.append(domain_content)
    sections.append("")

    for src_rel in domain_sources:
        src_path = WIKI / src_rel
        if not src_path.exists():
            print(f"WARNING: Domain source not found: {src_rel}", file=sys.stderr)
            continue
        content = read_content(src_path)
        h = hash_content(content)
        tk = estimate_tokens(content)
        total_tokens += tk
        sections.append(f"<!-- source: {src_rel} hash:{h} -->\n")
        sections.append(content)
        sections.append("")

    # ── User Layer ──
    if user_sources:
        sections.append("---\n## 用户层：个人上下文\n")
        for src_rel in user_sources:
            src_path = WIKI / src_rel
            if not src_path.exists():
                print(f"WARNING: User source not found: {src_rel}", file=sys.stderr)
                continue
            content = read_content(src_path)
            h = hash_content(content)
            tk = estimate_tokens(content)
            total_tokens += tk
            sections.append(f"<!-- source: {src_rel} hash:{h} -->\n")
            sections.append(content)
            sections.append("")

    compiled = "\n".join(sections)

    if dry_run:
        print(f"DRY-RUN: {agent_id}")
        print(f"  Sources: {len(os_sources)} OS + 1 agent + {len(domain_sources)} domain + {len(user_sources)} user")
        print(f"  Estimated tokens: {total_tokens}")
        print(f"  Output: .agent/prompts/{agent_id}.md")
        return compiled

    # Write output
    PROMPTS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = PROMPTS_DIR / f"{agent_id}.md"
    out_path.write_text(compiled, encoding="utf-8")
    print(f"Compiled: .agent/prompts/{agent_id}.md")
    print(f"  {len(os_sources)} OS + 1 agent + {len(domain_sources)} domain + {len(user_sources)} user")
    print(f"  ~{total_tokens} tokens")
    return compiled


def main():
    parser = argparse.ArgumentParser(description="Agent Prompt Compiler")
    parser.add_argument("agent_id", help="Agent spec card id (e.g. tool-opc-sales-dialogue-assistant)")
    parser.add_argument("--dry-run", action="store_true", help="Preview only, do not write")
    args = parser.parse_args()

    result = compile_prompt(args.agent_id, args.dry_run)
    if result is None:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
