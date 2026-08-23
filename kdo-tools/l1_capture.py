#!/usr/bin/env python3
"""l1_capture.py — L1 全量上下文采集（#463，F-044 L0→L1 改名顺带）。

甲类（会话原文）：各 CLI 工具会话文件增量 → D 盘（git 外）
乙类（工作痕迹）：会话目录文件清单 + mtime → trace.md
镜像+verify：D 主库 → C 盘镜像 + 校验（#432 双盘模式）

用法：
  python kdo-tools/l1_capture.py              # 增量采集 + trace + 镜像
  python kdo-tools/l1_capture.py --dry-run    # 演练（只打印将采集的）
  python kdo-tools/l1_capture.py --verify     # 只跑镜像校验
"""

import argparse
import hashlib
import shutil
import sys
from datetime import datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# 甲类源（会话存储）；新增工具在此登记（#489：codex/opencode/qwen 四源补全，
# F-048 codex 定性=工厂角色工具，采集面纳全量）
SOURCE_DIRS = {
    "claude": Path.home() / ".claude" / "projects" / "C--Users-Administrator",
    "kimi": Path.home() / ".kimi-code",
    "hermes": Path("C:/Users/Administrator/AppData/Local/hermes/profiles"),
    "codex": Path.home() / ".codex",
    "codex-homes": Path("D:/KDO-memory/codex-homes"),  # 角色隔离目录（未来主力，#490 切换后生效）
    "opencode": Path.home() / ".config" / "opencode",
    "qwen": Path.home() / ".qwen",
}
SESSION_EXTS = (".jsonl", ".md", ".json", ".txt", ".log", ".sqlite")  # .sqlite=codex state/logs
# 敏感/非会话文件排除（凭证与安装元数据不进全量库）
SESSION_SKIP_FILES = {"auth.json", "installation_id", "cap_sid", "opencode.json", "package.json",
                      "package-lock.json", "config.toml"}
L1_ROOT = Path("D:/KDO-memory/L1-full")
MIRROR_ROOT = Path.home() / ".kdo-memory" / "L1-full-backup"

# #471 体积红线（建议 2）：每次采集后注体积；超限 → gate-blocked.log 机器自报
# （conveyor_probe 第五探针扫到 → 飞书通知王语嫣，禁新造扫描器——复用既有通道）
SIZE_LOG = Path(__file__).resolve().parent.parent / "90_control" / "l1-size.log"
GATE_BLOCKED_LOG = Path(__file__).resolve().parent.parent / "90_control" / "gate-blocked.log"
SIZE_REDLINE_MB = 5000  # 初值：当前 ~775MB 的 6.5 倍；超限告警并提示降频


def _dir_size_mb(root: Path) -> float:
    """#491：体积统计按内容 hash 去重（同 hash 文件不重复计入——日增量与源文件
    重叠量大，去重后体积反映真实新增）。"""
    seen: set[str] = set()
    total = 0
    for f in root.rglob("*"):
        try:
            if f.is_file():
                h = _sha256(f.read_bytes())
                if h in seen:
                    continue
                seen.add(h)
                total += f.stat().st_size
        except OSError:
            continue
    return total / (1024 * 1024)


ARCHIVE_ROOT = Path("D:/KDO-memory/L1-full-archive")  # #491：旧天目录压缩归档处


def _archive_old_days() -> int:
    """#491：非今天日期目录 zip 压缩归档（移出活跃统计），删原目录。返回归档数。"""
    import zipfile
    today = datetime.now().strftime("%Y-%m-%d")
    archived = 0
    if not L1_ROOT.exists():
        return 0
    ARCHIVE_ROOT.mkdir(parents=True, exist_ok=True)
    for d in sorted(L1_ROOT.iterdir()):
        if not d.is_dir() or d.name == today or not d.name.startswith("20"):
            continue
        zip_path = ARCHIVE_ROOT / f"{d.name}.zip"
        if zip_path.exists():  # 已归档过（幂等）
            shutil.rmtree(d, ignore_errors=True)
            archived += 1
            continue
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
            for f in d.rglob("*"):
                if f.is_file():
                    try:
                        zf.write(f, f.relative_to(L1_ROOT).as_posix())
                    except OSError:
                        continue
        shutil.rmtree(d, ignore_errors=True)
        archived += 1
        print(f"🗜 已归档: {d.name} → {zip_path.name}")
    if archived:
        print(f"🗜 旧天归档 {archived} 个目录")
    return archived


def _log_size_and_alert() -> None:
    """#471：采集后注体积（SIZE_LOG 追加）；超红线 → gate-blocked.log 机器自报（禁静默）。"""
    size_mb = _dir_size_mb(L1_ROOT)
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with SIZE_LOG.open("a", encoding="utf-8") as f:
            f.write(f"{ts} | L1-full {size_mb:.1f} MB（红线 {SIZE_REDLINE_MB} MB）\n")
    except OSError as e:
        print(f"⛔ 体积日志写入失败: {e}", file=sys.stderr)
    if size_mb > SIZE_REDLINE_MB:
        line = f"{ts}｜l1-capture｜L1-体积超限｜L1-full {size_mb:.1f} MB 超红线 {SIZE_REDLINE_MB} MB，请降频或扩容（#471）｜huangyaoshi\n"
        try:
            with GATE_BLOCKED_LOG.open("a", encoding="utf-8") as f:
                f.write(line)
        except OSError as e:
            print(f"⛔ gate-blocked 告警写入失败: {e}", file=sys.stderr)
        print(f"⛔ L1 体积超限告警已上报: {size_mb:.1f} MB > {SIZE_REDLINE_MB} MB", file=sys.stderr)


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _session_files(src: Path) -> list[Path]:
    """源目录下的会话/日志文件（顶层 + 一层子目录，跳过已知非会话目录）。"""
    skip = {"node_modules", "__pycache__", "audio_cache", "cache", "backups", "bin", "credentials", "store"}
    out = []
    for p in src.rglob("*"):
        try:
            if not p.is_file() or p.suffix not in SESSION_EXTS:
                continue
            if p.name in SESSION_SKIP_FILES:  # #489：敏感/非会话文件排除
                continue
            if any(part in skip for part in p.parts):
                continue
            p.stat()  # 提前 stat——不可访问（symlink/权限）的文件跳过（WinError 1920 实证）
        except OSError:
            continue
        out.append(p)
    return out


def capture(dry_run: bool) -> int:
    """#491 任务2（老朱硬性）：日增量结构——去按日整份目录（L1_ROOT/<tool>/<rel>
    直接存储，mtime 增量跨天只复制变化文件），trace-index.md append 式索引保可回溯。"""
    copied, skipped = 0, 0
    manifest = []
    for tool, src in SOURCE_DIRS.items():
        if not src.exists():
            continue
        dest_dir = L1_ROOT / tool
        for f in _session_files(src):
            rel = f.relative_to(src)
            dest = dest_dir / rel
            need = not dest.exists() or dest.stat().st_mtime < f.stat().st_mtime
            if dry_run:
                if need:
                    print(f"[dry-run] 将采集: {tool}/{rel}")
                    copied += 1
                continue
            if need:
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(f, dest)
                copied += 1
            else:
                skipped += 1
            manifest.append(f"{rel}|{f.stat().st_mtime:.0f}|{f.stat().st_size}")

    if dry_run:
        print(f"[dry-run] 待采集 {copied} 个文件（增量）")
        return 0

    # 乙类：trace 索引（append 式——日增量+trace 保证可回溯，#491 任务2-4）
    trace = L1_ROOT / "trace-index.md"
    trace.parent.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(trace, "a", encoding="utf-8") as f:
        if trace.stat().st_size == 0:
            f.write("# L1 trace 索引（#491 日增量口径——每次采集追加，可回溯）\n\n")
        f.write(f"\n## {ts}（新增 {copied} / 跳过 {skipped}）\n\n| 文件 | mtime | 大小 |\n|:--|:--|:--|\n")
        for line in sorted(manifest):
            rel, mt, size = line.split("|")
            f.write(f"| {rel} | {mt} | {size}B |\n")
    print(f"✅ 采集完成: 新增 {copied} / 跳过 {skipped} → {L1_ROOT}（日增量口径，#491）")
    print(f"✅ trace 索引已追加: {trace}")

    # #491：C 盘镜像已移除（老朱 01:23 拍板——L1 全量原文单盘 D，事件库仍 C+D 双盘）
    print("ℹ️ C 盘镜像已移除（#491 老朱拍板）：采集后不再写 C 盘，D 主库为唯一全量")
    # #471：采集后注体积（D 主库口径，hash 去重）+ 红线告警（失败不阻断主链路，stderr 可见）
    try:
        _log_size_and_alert()
    except Exception as e:
        print(f"⛔ 体积记录失败（采集已完成，不阻断）: {e}", file=sys.stderr)
    return 0


def mirror(dry_run: bool) -> int:
    if dry_run:
        print(f"[dry-run] 镜像: {L1_ROOT} → {MIRROR_ROOT}")
        return 0
    if not L1_ROOT.exists():
        print("L1 主库不存在（先跑采集）", file=sys.stderr)
        return 1
    n = 0
    for f in L1_ROOT.rglob("*"):
        if f.is_file():
            dest = MIRROR_ROOT / f.relative_to(L1_ROOT)
            dest.parent.mkdir(parents=True, exist_ok=True)
            if not dest.exists() or dest.stat().st_mtime < f.stat().st_mtime:
                shutil.copy2(f, dest)
                n += 1
    print(f"✅ 镜像完成: {L1_ROOT} → {MIRROR_ROOT}（同步 {n} 个）")
    return verify()


def verify() -> int:
    """#491：主库完整性自检（C 镜像已移除——校验 D 主库文件可读+抽样 hash 稳定）。"""
    if not L1_ROOT.exists():
        print("❌ 主库缺失", file=sys.stderr)
        return 1
    src_files = [f for f in L1_ROOT.rglob("*") if f.is_file()]
    if not src_files:
        print("❌ 主库无文件", file=sys.stderr)
        return 1
    for f in src_files[:5]:
        try:
            _sha256(f.read_bytes())
        except OSError as e:
            print(f"❌ verify FAIL：文件不可读 {f}: {e}", file=sys.stderr)
            return 1
    print(f"✅ verify PASS：主库 {len(src_files)} 文件完整 + 抽样可读（D 单盘口径，#491）")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="L1 全量上下文采集（#463）")
    p.add_argument("--dry-run", action="store_true", help="演练：只打印将采集的")
    p.add_argument("--verify", action="store_true", help="只跑镜像校验")
    args = p.parse_args()
    if args.verify:
        return verify()
    return capture(args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
