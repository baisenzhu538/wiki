"""能力注册表——发现 + 查询 + 列表。"""

_registry: dict[str, "Capability"] = {}


def register(cap: "Capability"):
    """注册一个能力。通常在 capability 的 __init__.py 中调用。"""
    _registry[cap.name] = cap


def get(name: str) -> "Capability | None":
    """按名称获取能力。"""
    return _registry.get(name)


def list_all() -> list["Capability"]:
    """列出所有已注册能力。"""
    return sorted(_registry.values(), key=lambda c: c.name)


def list_tools() -> list["Capability"]:
    return [c for c in list_all() if c.category == "tool"]


def list_manuals() -> list[dict]:
    """扫描 wiki 目录，列出可参考的说明书（frameworks/workflows/skills/agent-specs）。"""
    from pathlib import Path
    from .config import WIKI_ROOT

    manuals = []

    # Frameworks
    fw_dir = WIKI_ROOT / "30_wiki" / "frameworks"
    if fw_dir.exists():
        count = len(list(fw_dir.glob("*.md")))
        manuals.append({"type": "frameworks", "count": count, "path": "30_wiki/frameworks/", "how": 'kdo query "<关键词>"'})

    # Workflows
    wf_dir = WIKI_ROOT / "40_outputs" / "capabilities" / "workflows"
    if wf_dir.exists():
        count = len(list(wf_dir.glob("*.md")))
        manuals.append({"type": "workflows", "count": count, "path": "40_outputs/capabilities/workflows/", "how": 'Read 40_outputs/capabilities/workflows/'})

    # Skills
    sk_dir = WIKI_ROOT / "40_outputs" / "capabilities" / "skills"
    if sk_dir.exists():
        count = sum(1 for _ in sk_dir.rglob("SKILL.md"))
        manuals.append({"type": "skills", "count": count, "path": "40_outputs/capabilities/skills/", "how": 'Read <skill>/SKILL.md'})

    # Agent Specs
    ag_dir = WIKI_ROOT / "30_wiki" / "tools"
    if ag_dir.exists():
        specs = sorted([f.stem for f in ag_dir.glob("agent-spec-*.md")])
        for s in specs:
            manuals.append({"type": "agent-spec", "name": s, "path": f"30_wiki/tools/{s}.md", "how": f"Read 30_wiki/tools/{s}.md"})

    return manuals


def print_list():
    """输出能力列表（python -m capability_hub list）。"""
    print("=" * 55)
    print("  KDO 能力中台")
    print("=" * 55)

    tools = list_tools()
    print(f"\n  📦 可调用的工具（{len(tools)}）：")
    if tools:
        for t in tools:
            print(f"     {t.name:<20} {t.description}")
            print(f"       from capability_hub.{t.name} import process")
    else:
        print("     （暂无）")

    manuals = list_manuals()
    print(f"\n  📖 可参考的说明书（{len(manuals)} 类）：")
    for m in manuals:
        if m["type"] == "agent-spec":
            print(f"     🤖 {m['name']}")
            print(f"       {m['how']}")
        else:
            print(f"     {m['type']:<18} {m['count']} 个  →  {m['how']}")

    print()
