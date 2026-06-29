#!/usr/bin/env python3
"""
Hermes Profile Guard — config snapshot, rollback, and safe switch.

Usage:
  python hermes-profile-guard.py snapshot [--profile <name>]
  python hermes-profile-guard.py rollback <profile>
  python hermes-profile-guard.py switch <profile> --provider <p> --model <m> [--dry-run]
  python hermes-profile-guard.py doctor [--profile <name>]

Placement: kdo-tools/ — accessible from both Windows (PowerShell) and WSL (bash).
Hermes root: ~/.hermes/ (WSL path); also reachable via \\wsl$\<distro>\home\<user>\.hermes\
"""

import argparse
import os
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

import yaml


def find_hermes_roots() -> list[Path]:
    """Locate all Hermes root directories (Windows + WSL)."""
    roots = []
    home = Path.home()

    # Windows-side .hermes
    win_hermes = home / ".hermes"
    if win_hermes.exists():
        roots.append(win_hermes)

    # WSL-side .hermes (UNC path)
    wsl_hermes = Path(r"\\wsl$\Ubuntu-22.04\home\dministrator\.hermes")
    if wsl_hermes.exists():
        roots.append(wsl_hermes)

    return roots if roots else [win_hermes]  # fallback


def list_all_profiles(roots: list[Path]) -> list[tuple[Path, str]]:
    """Return [(hermes_root, profile_name), ...] for all profiles across all roots."""
    result = []
    for root in roots:
        profiles_dir = root / "profiles"
        if not profiles_dir.exists():
            continue
        for d in profiles_dir.iterdir():
            if d.is_dir() and (d / "config.yaml").exists():
                result.append((root, d.name))
    return result


def find_profile(roots: list[Path], profile: str) -> tuple[Path, str] | None:
    """Find a specific profile across all roots."""
    for root in roots:
        cfg = root / "profiles" / profile / "config.yaml"
        if cfg.exists():
            return (root, profile)
    return None


def snapshot(roots: list[Path], profile: str | None = None):
    """Create config.yaml.bak for one or all profiles."""
    if profile:
        found = find_profile(roots, profile)
        if not found:
            print(f"ERROR: Profile '{profile}' not found")
            return
        profiles = [(found[0], profile)]
    else:
        profiles = list_all_profiles(roots)

    results = []
    for root, pname in profiles:
        cfg = root / "profiles" / pname / "config.yaml"
        bak = root / "profiles" / pname / "config.yaml.bak"
        if not cfg.exists():
            results.append((pname, "SKIP", "no config.yaml"))
            continue
        shutil.copy2(cfg, bak)
        ts = datetime.now().isoformat()[:19]
        results.append((pname, "OK", f"{cfg.stat().st_size} bytes @ {ts}"))

    print(f"Snapshot: {len([r for r in results if r[1]=='OK'])}/{len(results)} profiles")
    for name, status, detail in results:
        print(f"  [{status}] {name}: {detail}")


def rollback(roots: list[Path], profile: str):
    """Restore config.yaml from config.yaml.bak."""
    found = find_profile(roots, profile)
    if not found:
        print(f"ERROR: Profile '{profile}' not found")
        sys.exit(1)

    root, _ = found
    cfg = root / "profiles" / profile / "config.yaml"
    bak = root / "profiles" / profile / "config.yaml.bak"

    if not bak.exists():
        print(f"ERROR: No backup found for {profile}")
        print(f"  Run 'snapshot' first to create config.yaml.bak")
        sys.exit(1)

    # Keep a pre-rollback copy just in case
    if cfg.exists():
        pre_rollback = root / "profiles" / profile / f"config.yaml.pre_rollback_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        shutil.copy2(cfg, pre_rollback)

    shutil.copy2(bak, cfg)
    print(f"ROLLBACK: {profile} restored from config.yaml.bak")

    # Show what changed
    try:
        with open(bak) as f:
            bak_data = yaml.safe_load(f)
        old_provider = bak_data.get("provider", "?")
        old_model = bak_data.get("model", {}).get("default", "?") if isinstance(bak_data.get("model"), dict) else "?"
        print(f"  Restored to: provider={old_provider}, model={old_model}")
    except Exception:
        pass


def switch(roots: list[Path], profile: str, provider: str, model: str, dry_run: bool = False):
    """Safely switch a profile's provider/model with snapshot before change."""
    found = find_profile(roots, profile)
    if not found:
        print(f"ERROR: Profile '{profile}' not found")
        sys.exit(1)

    root, _ = found
    cfg = root / "profiles" / profile / "config.yaml"

    # 1. Snapshot current config
    snapshot(roots, profile)

    # 2. Read and modify
    with open(cfg) as f:
        config = yaml.safe_load(f) or {}

    old_provider = config.get("provider", "none")
    old_model = config.get("model", {}).get("default", "?") if isinstance(config.get("model"), dict) else config.get("model", "?")

    if dry_run:
        print(f"DRY-RUN: {profile}: provider {old_provider} -> {provider}, model {old_model} -> {model}")
        print(f"  Config at: {cfg}")
        print(f"  Backup at: {root}/profiles/{profile}/config.yaml.bak")
        return

    # Apply changes
    if isinstance(config.get("model"), dict):
        config["model"]["default"] = model
    else:
        config["model"] = model
    config["provider"] = provider

    with open(cfg, "w") as f:
        yaml.dump(config, f, default_flow_style=False, allow_unicode=True)

    print(f"SWITCH: {profile}: provider {old_provider} -> {provider}, model {old_model} -> {model}")
    print(f"  Snapshot saved to config.yaml.bak")
    print(f"  To rollback: python kdo-tools/hermes-profile-guard.py rollback {profile}")


def doctor(roots: list[Path], profile: str | None = None):
    """Check profile health."""
    if profile:
        found = find_profile(roots, profile)
        profiles = [(found[0], profile)] if found else []
        if not profiles:
            print(f"Profile '{profile}' not found")
            return
    else:
        profiles = list_all_profiles(roots)

    print("Hermes Profile Doctor")
    print("=" * 50)
    if not profiles:
        print("  No profiles found!")
        return

    for root, pname in profiles:
        cfg = root / "profiles" / pname / "config.yaml"
        bak = root / "profiles" / pname / "config.yaml.bak"

        issues = []
        if not cfg.exists():
            issues.append("MISSING config.yaml")
            print(f"  {pname}: BROKEN - {', '.join(issues)}")
            continue

        cfg_size = cfg.stat().st_size
        bak_size = bak.stat().st_size if bak.exists() else 0

        if not bak.exists():
            issues.append("NO SNAPSHOT")

        try:
            with open(cfg) as f:
                data = yaml.safe_load(f) or {}
        except Exception as e:
            issues.append(f"YAML PARSE ERROR: {e}")

        provider = data.get("provider", "no provider field")
        model = data.get("model", {}).get("default", "?") if isinstance(data.get("model"), dict) else data.get("model", "?")
        loc = "WSL" if "wsl" in str(root) else "WIN"

        status = "HEALTHY" if not issues else "ISSUES"
        print(f"  [{loc}] {pname}: {status} | provider={provider} model={model} | cfg={cfg_size}B bak={bak_size}B")
        for issue in issues:
            print(f"    - {issue}")


def main():
    parser = argparse.ArgumentParser(description="Hermes Profile Guard")
    sub = parser.add_subparsers(dest="command", required=True)

    snap = sub.add_parser("snapshot")
    snap.add_argument("--profile", "-p", help="Specific profile (default: all)")

    roll = sub.add_parser("rollback")
    roll.add_argument("profile", help="Profile to rollback")

    sw = sub.add_parser("switch")
    sw.add_argument("profile", help="Profile to switch")
    sw.add_argument("--provider", required=True, help="New provider (e.g. deepseek, kimi-coding)")
    sw.add_argument("--model", required=True, help="New model (e.g. deepseek-v4-pro)")
    sw.add_argument("--dry-run", action="store_true", help="Preview only, no changes")

    doc = sub.add_parser("doctor")
    doc.add_argument("--profile", "-p", help="Specific profile (default: all)")

    args = parser.parse_args()

    roots = find_hermes_roots()

    if args.command == "snapshot":
        snapshot(roots, args.profile)
    elif args.command == "rollback":
        rollback(roots, args.profile)
    elif args.command == "switch":
        switch(roots, args.profile, args.provider, args.model, args.dry_run)
    elif args.command == "doctor":
        doctor(roots, args.profile)


if __name__ == "__main__":
    main()
