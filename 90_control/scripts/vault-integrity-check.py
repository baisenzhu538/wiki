#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#592 R3 vault integrity self-check (wiki resilience trio).

Daily light checks:
  1. vault working tree: file count + git status sanity (repo readable)
  2. newest bundle in D:\\KDO-memory: exists + mtime fresh + git bundle verify
  3. offsite copy in Nutstore dir: exists (rolling 3)

Any anomaly -> append to 90_control/gate-blocked.log (#472 probe format:
ts | task | reason | detail | source) so the duty channel (wangyuyan clock)
consumes it. Exit 0 = all OK, 1 = anomaly found (still writes log).

Called by: scheduled task kdo-health-daily via kdo-tools/run-kdo-health.cmd
Standalone: python vault-integrity-check.py [--inject-test]
"""
import argparse
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

GIT = r"C:\Program Files\Git\cmd\git.exe"
VAULT = Path(r"C:\Users\Administrator\Desktop\wiki")
BUNDLE_DIR = Path(r"D:\KDO-memory")
OFFSITE_DIR = Path(r"C:\Users\Administrator\Nutstore\1\我的坚果云\kdo-backup")
GATE_LOG = VAULT / "90_control" / "gate-blocked.log"
TASK_TAG = "vault-integrity"  # appears in gate-blocked line field 2
STALE_HOURS = 26  # daily bundle; allow one missed run


def gate_block(reason: str, detail: str):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{ts}｜{TASK_TAG}｜{reason}｜{detail[:200]}｜vault-integrity-check\n"
    try:
        with open(GATE_LOG, "a", encoding="utf-8") as f:
            f.write(line)
        print(f"[GATE-BLOCKED] {reason}: {detail}")
    except OSError as e:
        print(f"[GATE-BLOCKED-WRITE-FAIL] {e}: {reason}: {detail}")


def git(*args, cwd=None):
    p = subprocess.run([GIT] + list(args), cwd=cwd, capture_output=True,
                       text=True, encoding="utf-8", errors="replace", timeout=600)
    return p.returncode, (p.stdout or "") + (p.stderr or "")


def newest_bundle():
    cands = sorted(BUNDLE_DIR.glob("wiki-bundle-2*.bundle"),
                   key=lambda p: p.stat().st_mtime, reverse=True)
    return cands[0] if cands else None


def read_last_result():
    """Main backup writes last-result.txt (OK/FAIL). FAIL/missing = anomaly."""
    p = BUNDLE_DIR / "wiki-bundle-daily.last-result.txt"
    try:
        return p.read_text(encoding="utf-8", errors="replace").strip()
    except OSError:
        return "MISSING"


def check_vault():
    issues = []
    lr = read_last_result()
    if lr != "OK":
        issues.append(("每日备份上次结果异常", f"last-result={lr}"))
    rc, out = git("rev-parse", "HEAD", cwd=str(VAULT))
    if rc != 0:
        issues.append(("仓库不可读", f"git rev-parse rc={rc} {out[:120]}"))
        return issues, 0
    rc, out = git("status", "--porcelain", cwd=str(VAULT))
    if rc != 0:
        issues.append(("git status 失败", out[:120]))
    n_files = sum(len(fn) for _, dn, fn in os_walk(VAULT))
    if n_files < 10000:
        issues.append(("工作树文件数骤降", f"count={n_files} (expected >=10000)"))
    return issues, n_files


def os_walk(root: Path):
    for dp, dn, fn in root.walk():
        if ".git" in dn:
            dn.remove(".git")
        yield dp, dn, fn


def check_bundle():
    issues = []
    b = newest_bundle()
    if b is None:
        issues.append(("bundle 缺失", f"no wiki-bundle-2*.bundle in {BUNDLE_DIR}"))
        return issues, None
    age_h = (time.time() - b.stat().st_mtime) / 3600
    if age_h > STALE_HOURS:
        issues.append(("bundle 过期", f"{b.name} mtime {age_h:.1f}h ago > {STALE_HOURS}h"))
    rc, out = git("bundle", "verify", str(b))
    if rc != 0:
        issues.append(("bundle verify 失败", f"{b.name}: {out[:150]}"))
    return issues, b


def check_offsite():
    issues = []
    copies = sorted(OFFSITE_DIR.glob("wiki-bundle-2*.bundle"),
                    key=lambda p: p.stat().st_mtime, reverse=True)
    if not copies:
        issues.append(("异机副本缺失", f"no bundle in {OFFSITE_DIR}"))
        return issues
    latest = newest_bundle()
    if latest is not None and copies[0].name != latest.name:
        issues.append(("异机副本落后", f"offsite={copies[0].name} vs main={latest.name}"))
    return issues


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--inject-test", action="store_true",
                    help="self-test: pretend bundle missing, verify gate-blocked fires, exit 2")
    args = ap.parse_args()

    issues = []

    v_issues, n_files = check_vault()
    print(f"[1] vault: files={n_files}, issues={len(v_issues)}")
    issues += v_issues

    if args.inject_test:
        # simulated anomaly: newest bundle invisible -> checks 2 & 3 must fire
        b = newest_bundle()
        if not b:
            print("inject-test: no bundle to hide, cannot run")
            return 2
        tmp = b.with_suffix(".hidden")
        b.rename(tmp)
        try:
            b_issues, _ = check_bundle()
            print(f"[inject] bundle check fired: {len(b_issues)}")
            issues += [(r, d) for r, d in b_issues]
            o_issues = check_offsite()
            print(f"[inject] offsite check fired: {len(o_issues)}")
        finally:
            tmp.rename(b)
            print(f"[inject] bundle restored: {b.name}")
    else:
        b_issues, b = check_bundle()
        print(f"[2] bundle: {b.name if b else 'NONE'}, issues={len(b_issues)}")
        issues += b_issues
        o_issues = check_offsite()
        print(f"[3] offsite: issues={len(o_issues)}")
        issues += o_issues

    for reason, detail in issues:
        gate_block(reason, detail)

    if issues:
        print(f"[RESULT] FAIL: {len(issues)} anomaly(ies) -> gate-blocked.log")
        return 1
    print("[RESULT] OK: vault+bundle+offsite all healthy")
    return 0


if __name__ == "__main__":
    sys.exit(main())
