"""能力注册表——发现 + 查询 + 列表。"""

import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Windows GBK 终端强制切到 UTF-8 code page，避免中文乱码
if sys.platform == "win32":
    try:
        import ctypes
        ctypes.windll.kernel32.SetConsoleOutputCP(65001)
    except Exception:
        pass

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

    fw_dir = WIKI_ROOT / "30_wiki" / "frameworks"
    wf_dir = WIKI_ROOT / "40_outputs" / "capabilities" / "workflows"
    sk_dir = WIKI_ROOT / "40_outputs" / "capabilities" / "skills"

    if not any(d.exists() for d in [fw_dir, wf_dir, sk_dir]):
        import sys
        print(f"⚠️  警告：WIKI_ROOT ({WIKI_ROOT}) 下未找到说明书目录，请检查 WIKI_ROOT 环境变量或 wiki 路径",
              file=sys.stderr)
        return []

    manuals = []
    if fw_dir.exists():
        manuals.append({"type": "frameworks", "count": len(list(fw_dir.glob("*.md"))), "path": "30_wiki/frameworks/", "how": 'kdo query "<关键词>"'})

    if wf_dir.exists():
        manuals.append({"type": "workflows", "count": len(list(wf_dir.glob("*.md"))), "path": "40_outputs/capabilities/workflows/", "how": "Read workflows/"})

    if sk_dir.exists():
        manuals.append({"type": "skills", "count": sum(1 for _ in sk_dir.rglob("SKILL.md")), "path": "40_outputs/capabilities/skills/", "how": "Read <skill>/SKILL.md"})

    # Agent Specs — scan both tools/ and agent-specs/ directories
    seen_specs = set()
    for spec_dir_name in ["tools", "agent-specs"]:
        spec_dir = WIKI_ROOT / "30_wiki" / spec_dir_name
        if spec_dir.exists():
            for f in spec_dir.glob("agent-spec-*.md"):
                if f.stem not in seen_specs:
                    seen_specs.add(f.stem)
                    manuals.append({"type": "agent-spec", "name": f.stem, "path": f"30_wiki/{spec_dir_name}/{f.name}", "how": f"Read 30_wiki/{spec_dir_name}/{f.name}"})

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
