#!/usr/bin/env python3
"""shared_file_guard.py — 共享文件写前 stale 检测（#505）。

适用文件：production-queue.md / parking-lot-*.md / .agent/context.md /
.kdo/CAPSULE_STARTUP.md 等多实例共享文件的手工/编排侧写操作。

约定（90_control/file-flow-protocol-amend-shared-file-write.md）：
  ① 写前 snapshot 记录基线（git HEAD + 文件内容 hash）——防旧快照插入错位（#488）
  ② 写前 verify 比对——HEAD 已移动或文件已变 = 快照过期，报警退出 1，重读最新态再写
  ③ 落盘即 path-scoped commit（git commit -- <path>），message 标 by <instance>（E050 反向变体）

用法：
  python 90_control/scripts/shared_file_guard.py snapshot <file>
      → 打印基线串 "<HEAD>|<hash16>"，写操作前记录
  python 90_control/scripts/shared_file_guard.py verify <file> <baseline>
      → 新鲜 exit 0（打印 FRESH）/ 过期 exit 1（打印 STALE 原因）

退出码：0=FRESH / 1=STALE 或用法错误。小工具零依赖（仅 stdlib），不引新子系统。
"""

import hashlib
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # Windows GBK 控制台兼容

WIKI_ROOT = Path(__file__).resolve().parent.parent.parent

SEPARATOR = "|"  # ASCII——基线串要经 shell 变量传递，全角分隔符会被 GBK 捕获层破坏


def _git_head() -> str:
    """当前 git HEAD（失败返回 'unknown'——fail-open 不阻断，verify 时按基线比对）。"""
    try:
        out = subprocess.run(
            ["git", "-C", str(WIKI_ROOT), "rev-parse", "HEAD"],
            capture_output=True, text=True, timeout=15,
        )
    except (OSError, subprocess.TimeoutExpired):
        return "unknown"
    return out.stdout.strip() if out.returncode == 0 else "unknown"


def _file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def snapshot(path: Path) -> str:
    """记录写前基线：git HEAD + 文件内容 hash。"""
    if not path.exists():
        raise FileNotFoundError(f"文件不存在: {path}")
    return f"{_git_head()}{SEPARATOR}{_file_hash(path)}"


def verify(path: Path, baseline: str) -> tuple[bool, str]:
    """比对基线与当前态。返回 (fresh, message)。"""
    try:
        head, h = baseline.split(SEPARATOR)
    except ValueError:
        return False, f"基线格式错误（期望 '<HEAD>{SEPARATOR}<hash>'）: {baseline!r}"
    if not path.exists():
        return False, f"STALE：{path.name} 已不存在——现场与基线根本不符，停止写入（#505 约定①）"
    cur_head = _git_head()
    if head != "unknown" and cur_head != "unknown" and cur_head != head:
        return False, (
            f"STALE：git HEAD 已移动（基线 {head[:9]} → 当前 {cur_head[:9]}）——"
            f"你看到的是旧快照，重新读取 {path.name} 最新态再写（#505 约定①，#488 行错位教训）"
        )
    cur_h = _file_hash(path)
    if cur_h != h:
        return False, (
            f"STALE：{path.name} 内容自基线后已变化（并发写窗口，E050 反向变体同族）——"
            f"重新读取最新态再写（#505 约定①）"
        )
    return True, "FRESH"


def main() -> int:
    args = sys.argv[1:]
    if len(args) < 2 or args[0] not in ("snapshot", "verify"):
        print(__doc__, file=sys.stderr)
        return 1
    cmd = args[0]
    path = Path(args[1])
    if not path.is_absolute():
        path = WIKI_ROOT / path
    if cmd == "snapshot":
        try:
            print(snapshot(path))
        except (FileNotFoundError, OSError) as e:
            print(f"ERROR: {e}", file=sys.stderr)
            return 1
        return 0
    if len(args) < 3:
        print("verify 需要 <file> <baseline>", file=sys.stderr)
        return 1
    fresh, msg = verify(path, args[2])
    print(msg)
    return 0 if fresh else 1


if __name__ == "__main__":
    sys.exit(main())
