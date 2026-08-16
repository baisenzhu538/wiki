#!/usr/bin/env python3
"""MCP 配置单一真相源分发（#326 补充任务 2）。

模板: agents/hermes-mcp-template.yaml（mcp_servers.kdo 定义一次）
分发: 按平台渲染到 16 个 Hermes profile 的 config.yaml
  - Windows 侧: C:\\Users\\Administrator\\.hermes\\profiles\\<name>\\config.yaml
  - WSL 侧:    ~/.hermes/profiles/<name>/config.yaml（经 `wsl -e` 桥接读写）

原则:
  - 只更新 mcp_servers 节内的 `kdo` 子节——**其他 MCP（feishu_doc/wechat/openmontage 等）
    逐字保留**（#325 边界：不改变既有挂载语义）
  - 无 mcp_servers 节则整节追加
  - 写前备份 .bak-mcp-sync-<date>
  - 改模板重跑脚本 = 全量更新（漂移根治）

用法:
  python kdo-tools/sync-hermes-mcp.py            # dry-run
  python kdo-tools/sync-hermes-mcp.py --apply    # 写入
  python kdo-tools/sync-hermes-mcp.py --verify   # 全量验证已分发
"""
import argparse
import datetime
import os
import re
import shutil
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WIKI = r"C:\Users\Administrator\Desktop\wiki"
TEMPLATE = os.path.join(WIKI, "agents", "hermes-mcp-template.yaml")
WSL_WIKI = "/mnt/c/Users/Administrator/Desktop/wiki"
WSL_HOME = subprocess.run(["wsl", "-e", "bash", "-c", "echo $HOME"], capture_output=True, timeout=30).stdout.decode().strip()

WINDOWS_PROFILES = [
    "basic-skills-coach", "coaching-leadership-assistant", "duanwangye",
    "hongqigong", "laowantong", "meeting-assistant", "note-coach", "wangyuyan",
]
WSL_PROFILES = [
    "beikai", "duan", "duanwangye", "kimi-test",
    "laowantong", "laowantong-feishu", "ouyangfeng", "wangyuyan",
]

WINDOWS_PY = r"C:\Program Files\Python312\python.exe"
WSL_PY = "/home/dministrator/.hermes/hermes-agent/venv/bin/python"  # 系统 python3 无 mcp 包（狗粮实测）；Hermes venv 含 mcp
WINDOWS_KDO_SRC = r"C:\Users\Administrator\Knowledge Delivery OS 0.0.1"
WSL_KDO_SRC = "/mnt/c/Users/Administrator/Knowledge Delivery OS 0.0.1"

# 渲染后的 kdo 子节（4 空格缩进字段，2 空格缩进 kdo 键）
def render_kdo(platform: str) -> str:
    if platform == "windows":
        py, server, wiki, kdo_src = WINDOWS_PY, os.path.join(WIKI, "kdo-tools", "mcp", "server.py"), WIKI, WINDOWS_KDO_SRC
    else:
        py, server, wiki, kdo_src = WSL_PY, WSL_WIKI + "/kdo-tools/mcp/server.py", WSL_WIKI, WSL_KDO_SRC
    return (
        "  kdo:\n"
        f"    command: {py}\n"
        "    args:\n"
        f"    - {server}\n"
        f"    cwd: {wiki}\n"
        "    env:\n"
        f"      WIKI_ROOT: {wiki}\n"
        f"      KDO_SRC: {kdo_src}\n"
        "    enabled: true\n"
    )


def read_wsl(path: str) -> str:
    r = subprocess.run(["wsl", "-e", "bash", "-c", f"cat \"{path}\""], capture_output=True, timeout=30)
    if r.returncode != 0:
        raise FileNotFoundError(path)
    return r.stdout.decode("utf-8", errors="replace")


def write_wsl(path: str, content: str):
    subprocess.run(["wsl", "-e", "bash", "-c", f"cat > \"{path}\""], input=content.encode("utf-8"), timeout=30, check=True)


def profile_path(platform: str, name: str) -> str:
    if platform == "windows":
        return os.path.join(r"C:\Users\Administrator\.hermes\profiles", name, "config.yaml")
    return f"{WSL_HOME}/.hermes/profiles/{name}/config.yaml"


def exists(platform: str, path: str) -> bool:
    if platform == "windows":
        return os.path.exists(path)
    r = subprocess.run(["wsl", "-e", "bash", "-c", f"test -f \"{path}\" && echo yes"], capture_output=True, timeout=30)
    return r.stdout.decode().strip() == "yes"


def replace_kdo_section(src: str, kdo_block: str) -> str:
    """文本级替换 mcp_servers 节内的 kdo 子节；无则整节追加。其他 MCP 逐字保留。"""
    lines = src.splitlines(keepends=True)
    mcp_idx = None
    for i, line in enumerate(lines):
        if re.match(r"^mcp_servers:\s*$", line):
            mcp_idx = i
            break

    if mcp_idx is None:
        return src.rstrip("\n") + "\n\nmcp_servers:\n" + kdo_block

    # 找 kdo 子节：在 mcp_servers 下找 "  kdo:" 开头的行
    kdo_start = None
    for i in range(mcp_idx + 1, len(lines)):
        if re.match(r"^  [a-zA-Z_][a-zA-Z0-9_]*:", lines[i]):
            if lines[i].strip().startswith("kdo:"):
                kdo_start = i
                break
            # 遇到其他子键且尚未找到 kdo → kdo 不存在
            if kdo_start is None and re.match(r"^  \S", lines[i]):
                break
    # 简化：直接找 "  kdo:" 行
    kdo_start = None
    for i in range(mcp_idx + 1, len(lines)):
        if re.match(r"^  kdo:\s*$", lines[i]):
            kdo_start = i
            break
        if re.match(r"^  \S", lines[i]) and not re.match(r"^  kdo:", lines[i]):
            break

    if kdo_start is None:
        # 在 mcp_servers 下第一个子键前插入 kdo（若无子键则追加到 mcp_servers 后）
        insert_at = mcp_idx + 1
        for i in range(mcp_idx + 1, len(lines)):
            if re.match(r"^  \S", lines[i]):
                insert_at = i
                break
        return "".join(lines[:insert_at]) + kdo_block + "".join(lines[insert_at:])

    # kdo 子节结束 = 下一个 2 空格缩进键
    kdo_end = len(lines)
    for i in range(kdo_start + 1, len(lines)):
        if re.match(r"^  \S", lines[i]):
            kdo_end = i
            break
    return "".join(lines[:kdo_start]) + kdo_block + "".join(lines[kdo_end:])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--verify", action="store_true")
    args = ap.parse_args()

    targets = [("windows", n) for n in WINDOWS_PROFILES] + [("wsl", n) for n in WSL_PROFILES]

    if args.verify:
        ok = 0
        for platform, name in targets:
            path = profile_path(platform, name)
            if not exists(platform, path):
                print(f"[MISS] {platform}/{name}: 无 config.yaml（未部署）")
                continue
            src = read_wsl(path) if platform == "wsl" else open(path, encoding="utf-8", errors="replace").read()
            if re.search(r"^  kdo:\s*$", src, re.M) and "server.py" in src and "enabled: true" in src:
                ok += 1
            else:
                print(f"[FAIL] {platform}/{name}")
        print(f"验证: {ok}/{len(targets)} 已挂 kdo")
        return

    for platform, name in targets:
        path = profile_path(platform, name)
        if not exists(platform, path):
            print(f"[SKIP] {platform}/{name}: 无 config.yaml（未部署）")
            continue
        src = read_wsl(path) if platform == "wsl" else open(path, encoding="utf-8", errors="replace").read()
        new_src = replace_kdo_section(src, render_kdo(platform))
        if new_src == src:
            print(f"[SAME] {platform}/{name}: 已是最新")
            continue
        # yaml 完整性验证
        try:
            import yaml
            yaml.safe_load(new_src)
        except Exception as e:
            print(f"[FAIL] {platform}/{name}: 渲染后 yaml 解析失败 {e}")
            continue
        print(f"[DIFF] {platform}/{name}: 将更新 kdo 子节")
        if args.apply:
            if platform == "wsl":
                subprocess.run(["wsl", "-e", "bash", "-c",
                                f"cp '{path}' '{path}.bak-mcp-sync-{datetime.date.today():%Y%m%d}'"],
                               timeout=30, check=True)
                write_wsl(path, new_src)
            else:
                shutil.copy2(path, path + f".bak-mcp-sync-{datetime.date.today():%Y%m%d}")
                open(path, "w", encoding="utf-8", newline="").write(new_src)
            print(f"  [APPLIED] {platform}/{name}（已备份）")

    if not args.apply:
        print("\n[dry-run] 未写入。加 --apply 执行。")


if __name__ == "__main__":
    main()
