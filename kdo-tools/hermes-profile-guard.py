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


def find_hermes_root() -> Path:
    """Locate Hermes root directory."""
    home = Path.home()
    candidates = [
        home / ".hermes",
        # WSL path from Windows
        Path("/mnt/c/Users") / os.environ.get("USER", "Administrator") / ".hermes",
    ]
    # Try WSL UNC path
    wsl_base = Path(os.environ.get("WSL_HERMES", ""))
    if not wsl_base.exists():
        wsl_base = Path(f"\\\\wsl$\\Ubuntu-22.04\\home\\{os.environ.get('WSL_USER', 'dministrator')}\\.hermes")

    for c in candidates:
        if c.exists():
            return c
    if wsl_base.exists():
        return wsl_base

    # Try to detect from WSL
    try:
        result = subprocess.run(
            ["wsl", "-d", "Ubuntu-22.04", "-e", "bash", "-c", "echo $HOME/.hermes"],
            capture_output=True, text=True, timeout=10
        )
        detected = Path(result.stdout.strip())
        if detected.exists():
            return detected
    except Exception:
        pass

    raise FileNotFoundError("Cannot find Hermes root. Set WSL_HERMES or WSL_USER env vars.")


def list_profiles(hermes_root: Path) -> list[str]:
    profiles_dir = hermes_root / "profiles"
    if not profiles_dir.exists():
        return []
    return [d.name for d in profiles_dir.iterdir() if d.is_dir() and (d / "config.yaml").exists()]


def snapshot(hermes_root: Path, profile: str | None = None):
    """Create config.yaml.bak for one or all profiles."""
    profiles = [profile] if profile else list_profiles(hermes_root)
    results = []
    for p in profiles:
        cfg = hermes_root / "profiles" / p / "config.yaml"
        bak = hermes_root / "profiles" / p / "config.yaml.bak"
        if not cfg.exists():
            results.append((p, "SKIP", "no config.yaml"))
            continue
        shutil.copy2(cfg, bak)
        ts = datetime.now().isoformat()[:19]
        results.append((p, "OK", f"{cfg.stat().st_size} bytes @ {ts}"))

    print(f"Snapshot: {len([r for r in results if r[1]=='OK'])}/{len(results)} profiles")
    for name, status, detail in results:
        print(f"  [{status}] {name}: {detail}")


def rollback(hermes_root: Path, profile: str):
    """Restore config.yaml from config.yaml.bak."""
    cfg = hermes_root / "profiles" / profile / "config.yaml"
    bak = hermes_root / "profiles" / profile / "config.yaml.bak"

    if not bak.exists():
        print(f"ERROR: No backup found for {profile}")
        print(f"  Run 'snapshot' first to create config.yaml.bak")
        sys.exit(1)

    # Keep a pre-rollback copy just in case
    if cfg.exists():
        pre_rollback = hermes_root / "profiles" / profile / f"config.yaml.pre_rollback_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        shutil.copy2(cfg, pre_rollback)

    shutil.copy2(bak, cfg)
    print(f"ROLLBACK: {profile} restored from config.yaml.bak")

    # Show what changed
    try:
        with open(bak) as f:
            bak_data = yaml.safe_load(f)
        with open(cfg) as f:
            cfg_data = yaml.safe_load(f)
        old_provider = bak_data.get("provider", "?")
        old_model = bak_data.get("model", {}).get("default", "?") if isinstance(bak_data.get("model"), dict) else "?"
        print(f"  Restored to: provider={old_provider}, model={old_model}")
    except Exception:
        pass


def switch(hermes_root: Path, profile: str, provider: str, model: str, dry_run: bool = False):
    """Safely switch a profile's provider/model with snapshot before change."""
    cfg = hermes_root / "profiles" / profile / "config.yaml"
    if not cfg.exists():
        print(f"ERROR: Profile '{profile}' not found at {cfg}")
        sys.exit(1)

    # 1. Snapshot current config
    snapshot(hermes_root, profile)

    # 2. Read and modify
    with open(cfg) as f:
        config = yaml.safe_load(f) or {}

    old_provider = config.get("provider", "none")
    old_model = config.get("model", {}).get("default", "?") if isinstance(config.get("model"), dict) else config.get("model", "?")

    if dry_run:
        print(f"DRY-RUN: {profile}: provider {old_provider} -> {provider}, model {old_model} -> {model}")
        print(f"  Config at: {cfg}")
        print(f"  Backup at: {hermes_root}/profiles/{profile}/config.yaml.bak")
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
    print(f"  To rollback: python hermes-profile-guard.py rollback {profile}")


def doctor(hermes_root: Path, profile: str | None = None):
    """Check profile health."""
    profiles = [profile] if profile else list_profiles(hermes_root)

    print("Hermes Profile Doctor")
    print("=" * 50)

    for p in profiles:
        cfg = hermes_root / "profiles" / p / "config.yaml"
        bak = hermes_root / "profiles" / p / "config.yaml.bak"

        issues = []
        if not cfg.exists():
            issues.append("MISSING config.yaml")
            print(f"  {p}: BROKEN - {', '.join(issues)}")
            continue

        cfg_size = cfg.stat().st_size
        bak_size = bak.stat().st_size if bak.exists() else 0

        if not bak.exists():
            issues.append("NO SNAPSHOT (config.yaml.bak missing)")

        try:
            with open(cfg) as f:
                data = yaml.safe_load(f) or {}
        except Exception as e:
            issues.append(f"YAML PARSE ERROR: {e}")

        provider = data.get("provider", "?")
        model = data.get("model", {}).get("default", "?") if isinstance(data.get("model"), dict) else data.get("model", "?")

        status = "HEALTHY" if not issues else "ISSUES"
        print(f"  {p}: {status} | provider={provider} model={model} | config={cfg_size}B bak={bak_size}B")
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

    hermes_root = find_hermes_root()

    if args.command == "snapshot":
        snapshot(hermes_root, args.profile)
    elif args.command == "rollback":
        rollback(hermes_root, args.profile)
    elif args.command == "switch":
        switch(hermes_root, args.profile, args.provider, args.model, args.dry_run)
    elif args.command == "doctor":
        doctor(hermes_root, args.profile)


if __name__ == "__main__":
    main()
