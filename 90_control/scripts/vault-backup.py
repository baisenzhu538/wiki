#!/usr/bin/env python3
"""
KDO Vault 备份与恢复工具

备份:  python vault-backup.py backup [--output <dir>]
恢复:  python vault-backup.py restore <card-id> [--date YYYY-MM-DD]
列表:  python vault-backup.py list-deleted [--since YYYY-MM-DD]
健康:  python vault-backup.py health
"""

import os, subprocess, sys, zipfile, json
from datetime import datetime, timedelta
from pathlib import Path

VAULT = Path(r"C:\Users\Administrator\Desktop\wiki")
NUTSTORE = Path(r"C:\Users\Administrator\Nutstore\1\我的坚果云\kdo-backups")
NUTSTORE.mkdir(parents=True, exist_ok=True)

# ── 备份 ──

def backup(output_dir: Path = None):
    """创建 timestamped 完整备份到坚果云 + 本地（仅在有 git 变更时）。"""
    # 检查自上次备份以来是否有 git 变更
    os.chdir(VAULT)
    existing = sorted(NUTSTORE.glob("kdo-vault-*.zip"))
    if existing:
        last_ts = existing[-1].stem.replace("kdo-vault-", "")
        try:
            last_dt = datetime.strptime(last_ts, "%Y%m%d-%H%M%S")
            r = subprocess.run(
                ["git", "log", "--oneline", "--since", last_dt.strftime("%Y-%m-%d %H:%M:%S"), "--", "."],
                capture_output=True, text=True
            )
            if not r.stdout.strip():
                print(f"跳过备份：自 {last_ts} 以来无 git 变更")
                return
        except ValueError:
            pass

    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    out = (output_dir or NUTSTORE) / f"kdo-vault-{ts}.zip"

    count = 0
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(VAULT):
            dirs[:] = [d for d in dirs if d not in (".git", ".tmp", "_tmp", "__pycache__", "node_modules", ".trash")]
            for f in files:
                fp = Path(root) / f
                arcname = fp.relative_to(VAULT)
                zf.write(fp, arcname)
                count += 1

    sz_mb = out.stat().st_size / 1024 / 1024
    print(f"备份完成: {out}")
    print(f"  {count} 文件, {sz_mb:.1f} MB")

    # 清理旧备份（保留最近 7 天，从 14 天缩短以减少流量）
    for old in sorted(NUTSTORE.glob("kdo-vault-*.zip")):
        try:
            date_str = old.stem.replace("kdo-vault-", "")
            d = datetime.strptime(date_str, "%Y%m%d-%H%M%S")
            if d < datetime.now() - timedelta(days=7):
                old.unlink()
                print(f"  清理旧备份: {old.name}")
        except ValueError:
            pass

# ── 恢复 ──

def list_deleted(since: str = None):
    """列出 git 历史中被删除的 .md 文件。"""
    os.chdir(VAULT)
    cmd = ["git", "log", "--diff-filter=D", "--name-only", "--pretty=format:%h %ad", "--date=short"]
    if since:
        cmd.append(f"--since={since}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    print("最近删除的卡片:")
    for line in result.stdout.strip().split("\n"):
        if line.strip() and not line.startswith("commit"):
            print(f"  {line.strip()}")

def restore_card(card_id: str, date: str = None):
    """从 git 历史恢复指定卡片。"""
    os.chdir(VAULT)
    # 搜索文件名
    if not card_id.endswith(".md"):
        card_id += ".md"
    # Find in git history
    cmd = ["git", "log", "--all", "--full-history", "--pretty=format:%H", "--", f"*/{card_id}"]
    if date:
        cmd.append(f"--since={date}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    hashes = [h for h in result.stdout.strip().split("\n") if h]

    if not hashes:
        # Try broader search
        cmd2 = ["git", "log", "--all", "--diff-filter=D", "--name-only", "--pretty=format:%H", f"--since={date or '2026-05-01'}"]
        result2 = subprocess.run(cmd2, capture_output=True, text=True)
        print(f"未在 git 历史中找到 '{card_id}'")
        print("最近删除列表：")
        list_deleted(since=date or "2026-05-01")
        return

    # Restore from most recent commit that had it
    commit = hashes[0]
    # Find the file path
    cmd3 = ["git", "show", "--name-only", "--pretty=format:", commit, "--", f"*/{card_id}"]
    result3 = subprocess.run(cmd3, capture_output=True, text=True)
    paths = [p.strip() for p in result3.stdout.strip().split("\n") if p.strip() and card_id in p]
    if not paths:
        print(f"在 commit {commit[:8]} 中找到了但无法确定路径")
        return
    filepath = paths[0]
    dest = VAULT / filepath
    dest.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["git", "checkout", commit, "--", filepath], cwd=VAULT, check=True)
    print(f"已恢复: {dest}")

# ── 健康 ──

def health():
    """快速健康检查。"""
    os.chdir(VAULT)
    issues = []
    # Git status
    r = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    changed = len([l for l in r.stdout.split("\n") if l.strip()])
    # Card count
    wiki = VAULT / "30_wiki"
    cards = len([f for f in wiki.rglob("*.md") if "raw" not in str(f) and "_archive" not in str(f)])
    # Backup age
    backups = sorted(NUTSTORE.glob("kdo-vault-*.zip"), reverse=True)
    last_backup = backups[0].stem.replace("kdo-vault-", "") if backups else "无"
    backup_hours = None
    if backups:
        try:
            d = datetime.strptime(last_backup, "%Y%m%d-%H%M%S")
            backup_hours = (datetime.now() - d).total_seconds() / 3600
        except: pass

    # Trash check
    trash = VAULT / ".trash"
    in_trash = len(list(trash.rglob("*.md"))) if trash.exists() else 0

    print("=" * 50)
    print("KDO Vault 健康快检")
    print("=" * 50)
    print(f"  Wiki 卡片: {cards}")
    print(f"  Git 未提交变更: {changed}")
    print(f"  最近备份: {last_backup} ({backup_hours:.1f}h 前)" if backup_hours else f"  最近备份: {last_backup}")
    print(f"  回收站 (.trash): {in_trash} 文件")
    issues.append("超过 24h 无备份！" if backup_hours and backup_hours > 24 else "")
    issues.append("有未提交变更，git 未同步" if changed > 0 else "")
    active = [i for i in issues if i]
    if active:
        print(f"\n  !! {len(active)} issues:")
        for i in active: print(f"    - {i}")
    else:
        print(f"\n  OK: Healthy")

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(description="KDO Vault 备份与恢复")
    sp = p.add_subparsers(dest="cmd")
    sp.add_parser("backup")
    r = sp.add_parser("restore")
    r.add_argument("card", help="卡片 ID 或文件名")
    r.add_argument("--date", help="日期范围")
    l = sp.add_parser("list-deleted")
    l.add_argument("--since", help="起始日期")
    sp.add_parser("health")
    args = p.parse_args()
    if args.cmd == "backup":
        backup()
    elif args.cmd == "restore":
        restore_card(args.card, args.date)
    elif args.cmd == "list-deleted":
        list_deleted(args.since)
    elif args.cmd == "health":
        health()
    else:
        p.print_help()
