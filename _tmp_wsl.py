import os
from pathlib import Path

# Check Windows-side .hermes
win_hermes = Path.home() / ".hermes"
print(f"Windows .hermes: {win_hermes} exists={win_hermes.exists()}")
if win_hermes.exists():
    prof_dir = win_hermes / "profiles"
    if prof_dir.exists():
        for d in prof_dir.iterdir():
            if d.is_dir():
                print(f"  WIN profile: {d.name}")

# Check WSL-side .hermes
wsl_hermes = Path(r"\\wsl$\Ubuntu-22.04\home\dministrator\.hermes")
print(f"\nWSL .hermes: {wsl_hermes} exists={wsl_hermes.exists()}")
if wsl_hermes.exists():
    prof_dir = wsl_hermes / "profiles"
    if prof_dir.exists():
        for d in prof_dir.iterdir():
            if d.is_dir():
                cfg = d / "config.yaml"
                bak = d / "config.yaml.bak"
                print(f"  WSL profile: {d.name} cfg={cfg.exists()} bak={bak.exists()}")
