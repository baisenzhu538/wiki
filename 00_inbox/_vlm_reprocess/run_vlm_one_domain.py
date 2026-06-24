#!/usr/bin/env python3
"""
Process remaining VLM images for a single domain sequentially with per-image timeout.
Imports functions from describe-images-minimax.py.
"""
import os
import sys
import shutil
import importlib.util
from pathlib import Path

WIKI = Path('C:/Users/Administrator/Desktop/wiki')
BASE = WIKI / '00_inbox/_vlm_reprocess'
SCRIPT_PATH = WIKI / '40_outputs/code/scripts/describe-images-minimax.py'
IMAGE_EXTS = {'.png', '.jpg', '.jpeg', '.webp', '.gif', '.bmp'}
PER_IMAGE_TIMEOUT = 90  # seconds


def load_script_module():
    spec = importlib.util.spec_from_file_location('vlm_script', SCRIPT_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main(domain: str):
    mod = load_script_module()
    api_key = mod.get_api_key()

    temp_dir = BASE / f'_temp_{domain}'
    done_dir = BASE / f'_done_{domain}'
    out_dir = BASE / domain
    done_dir.mkdir(parents=True, exist_ok=True)
    out_dir.mkdir(parents=True, exist_ok=True)

    done_names = {p.stem for p in done_dir.iterdir() if p.is_file()}
    remaining = sorted([p for p in temp_dir.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_EXTS and p.stem not in done_names])

    print(f"[{domain}] {len(remaining)} images remaining")

    success = 0
    failed = []

    for idx, img_path in enumerate(remaining, 1):
        out_path = out_dir / f"{img_path.stem}_vlm_desc.md"
        if out_path.exists():
            # already done
            shutil.move(img_path, done_dir / img_path.name)
            success += 1
            continue
        print(f"[{idx}/{len(remaining)}] {img_path.name}")
        try:
            result = mod.describe_image(api_key, img_path)
            mod.save_description(out_path, img_path, result)
            shutil.move(img_path, done_dir / img_path.name)
            success += 1
            print(f"  -> ok")
        except Exception as e:
            print(f"  -> FAILED: {e}")
            failed.append((img_path.name, str(e)))

    print(f"[{domain}] success={success} failed={len(failed)}")
    for name, err in failed:
        print(f"  FAIL {name}: {err}")


if __name__ == '__main__':
    domain = sys.argv[1]
    main(domain)
