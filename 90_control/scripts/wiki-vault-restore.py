#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#592 R2 wiki vault restore drill script (wiki resilience trio).

Usage:
    python wiki-vault-restore.py --bundle D:\\KDO-memory\\wiki-bundle-20260901.bundle ^
        --target D:\\_restore_test [--keep]

Flow: git bundle verify -> git clone from bundle -> count files ->
compare vs current vault (tracked files + working-tree files + git status
snapshot). Exit 0 = drill PASS, 1 = any check failed.

Never touches the source vault (read-only against it). Never deletes the
target unless --keep is omitted AND the target was created by this script.
"""
import argparse
import os
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

GIT = r"C:\Program Files\Git\cmd\git.exe"
DEFAULT_VAULT = Path(r"C:\Users\Administrator\Desktop\wiki")


def run(cmd, cwd=None, timeout=1800):
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=timeout,
                       shell=False)
    return p.returncode, (p.stdout or "") + (p.stderr or "")


def git(*args, cwd=None, timeout=1800):
    return run([GIT] + list(args), cwd=cwd, timeout=timeout)


def count_files(root: Path, skip_git=True):
    n = 0
    for dp, dn, fn in os.walk(root):
        if skip_git and ".git" in dn:
            dn.remove(".git")
        n += len(fn)
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bundle", required=True, help="path to .bundle file")
    ap.add_argument("--target", required=True, help="restore target dir")
    ap.add_argument("--vault", default=str(DEFAULT_VAULT), help="reference vault for comparison")
    ap.add_argument("--keep", action="store_true", help="keep target dir after drill")
    args = ap.parse_args()

    bundle = Path(args.bundle)
    target = Path(args.target)
    vault = Path(args.vault)
    ok = True

    if not bundle.is_file():
        print(f"[FAIL] bundle not found: {bundle}")
        return 1
    print(f"[1] bundle: {bundle} ({bundle.stat().st_size:,} bytes)")

    if target.exists():
        print(f"[FAIL] target already exists (refusing to touch): {target}")
        return 1

    # step 1: bundle verify
    rc, out = git("bundle", "verify", str(bundle))
    print(f"[2] git bundle verify: rc={rc}")
    print("    " + "\n    ".join(out.strip().splitlines()[:6]))
    if rc != 0:
        return 1

    # step 2: clone from bundle
    target.parent.mkdir(parents=True, exist_ok=True)
    rc, out = git("clone", str(bundle), str(target), "--quiet")
    print(f"[3] git clone -> {target}: rc={rc}")
    if rc != 0:
        print("    " + out[:500])
        return 1

    # step 3: restored repo checks
    rc, out = git("rev-parse", "HEAD", cwd=str(target))
    head_restored = out.strip()
    print(f"[4] restored HEAD: {head_restored[:12]} rc={rc}")
    if rc != 0:
        ok = False

    rc, out = git("status", "--porcelain", cwd=str(target))
    dirty_restored = len(out.strip().splitlines()) if out.strip() else 0
    print(f"[5] restored git status dirty lines: {dirty_restored} (clone from bundle should be 0)")

    n_restored = count_files(target)
    n_vault_tracked = int(git("ls-files", cwd=str(vault))[1].strip().count("\n")) + 1
    rc, out = git("status", "--porcelain", cwd=str(vault))
    n_vault_dirty = len([l for l in out.splitlines() if l.strip()])
    head_vault = git("rev-parse", "HEAD", cwd=str(vault))[1].strip()
    n_vault_worktree = count_files(vault)

    print("[6] comparison (restored vs current vault):")
    print(f"    restored worktree files : {n_restored}")
    print(f"    vault tracked files     : {n_vault_tracked}")
    print(f"    vault worktree files    : {n_vault_worktree} (incl {n_vault_dirty} untracked/modified lines)")
    print(f"    HEAD equal              : {head_restored == head_vault}")

    # bundle snapshot == vault HEAD => restored files should equal vault tracked files
    if head_restored != head_vault:
        print("    [WARN] HEAD differs (bundle older than current vault) - expected if commits made after bundle")
        delta_note = "bundle-is-older"
    else:
        delta_note = "same-head"
        if n_restored != n_vault_tracked:
            print(f"    [FAIL] restored {n_restored} != tracked {n_vault_tracked} at same HEAD")
            ok = False
        else:
            print(f"    [OK] file count matches tracked set exactly ({n_restored})")

    print(f"[7] drill verdict: {'PASS' if ok else 'FAIL'} ({delta_note})")

    if not args.keep:
        import shutil
        shutil.rmtree(target, ignore_errors=True)
        print(f"[8] drill dir cleaned: {target}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
