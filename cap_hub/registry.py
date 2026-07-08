"""能力注册表——发现 + 查询 + 列表。"""

from pathlib import Path

_registry: dict[str, "Capability"] = {}


def register(cap: "Capability"):
    _registry[cap.name] = cap


def get(name: str) -> "Capability | None":
    return _registry.get(name)


def list_all() -> list["Capability"]:
    return sorted(_registry.values(), key=lambda c: c.name)


def list_tools() -> list["Capability"]:
    return [c for c in list_all() if c.category == "tool"]


def list_manuals() -> list[dict]:
    """扫描 wiki 目录，列出可参考的说明书。"""
    from .config import WIKI_ROOT

    manuals = []
    fw_dir = WIKI_ROOT / "30_wiki" / "frameworks"
    if fw_dir.exists():
        manuals.append({"type": "frameworks", "count": len(list(fw_dir.glob("*.md"))), "path": "30_wiki/frameworks/", "how": 'kdo query "<关键词>"'})

    wf_dir = WIKI_ROOT / "40_outputs" / "capabilities" / "workflows"
    if wf_dir.exists():
        manuals.append({"type": "workflows", "count": len(list(wf_dir.glob("*.md"))), "path": "40_outputs/capabilities/workflows/", "how": "Read workflows/"})

    sk_dir = WIKI_ROOT / "40_outputs" / "capabilities" / "skills"
    if sk_dir.exists():
        manuals.append({"type": "skills", "count": sum(1 for _ in sk_dir.rglob("SKILL.md")), "path": "40_outputs/capabilities/skills/", "how": "Read <skill>/SKILL.md"})

    ag_dir = WIKI_ROOT / "30_wiki" / "tools"
    if ag_dir.exists():
        for s in sorted(ag_dir.glob("agent-spec-*.md")):
            manuals.append({"type": "agent-spec", "name": s.stem, "path": f"30_wiki/tools/{s.name}", "how": f"Read 30_wiki/tools/{s.name}"})

    return manuals


def print_list():
    """输出能力列表。"""
    print("=" * 55)
    print("  KDO 能力中台")
    print("=" * 55)

    tools = list_tools()
    print(f"\n  可调用的工具 ({len(tools)})：")
    if tools:
        for t in tools:
            print(f"     {t.name:<20} {t.description}")
            print(f"       from cap_hub.{t.name} import process")
    else:
        print("     （暂无）")

    manuals = list_manuals()
    print(f"\n  可参考的说明书 ({len(manuals)} 类)：")
    for m in manuals:
        if m["type"] == "agent-spec":
            print(f"     {m['name']}")
            print(f"       {m['how']}")
        else:
            print(f"     {m['type']:<18} {m['count']} 个  ->  {m['how']}")

    print()
