#!/usr/bin/env python3
"""
Process VLM description in batches for P0 domains.
Copies up to BATCH_SIZE images from _temp_<domain> to _batch_<domain>,
runs describe-images-minimax.py, then moves processed images to _done_<domain>.
Processes both domains concurrently.
"""
import os
import sys
import shutil
import subprocess
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed

WIKI = Path('C:/Users/Administrator/Desktop/wiki')
SCRIPT = WIKI / '40_outputs/code/scripts/describe-images-minimax.py'
BASE = WIKI / '00_inbox/_vlm_reprocess'
BATCH_SIZE = 4
IMAGE_EXTS = {'.png', '.jpg', '.jpeg', '.webp', '.gif', '.bmp'}


def process_domain(domain: str):
    temp_dir = BASE / f'_temp_{domain}'
    done_dir = BASE / f'_done_{domain}'
    batch_dir = BASE / f'_batch_{domain}'
    out_dir = BASE / domain
    done_dir.mkdir(parents=True, exist_ok=True)
    out_dir.mkdir(parents=True, exist_ok=True)

    # remaining images = in temp but not in done
    done_names = {p.name for p in done_dir.iterdir() if p.is_file()}
    remaining = sorted([p for p in temp_dir.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_EXTS and p.name not in done_names])

    if not remaining:
        return {'domain': domain, 'processed': 0, 'status': 'no more images'}

    batch = remaining[:BATCH_SIZE]

    # prepare batch dir
    if batch_dir.exists():
        shutil.rmtree(batch_dir)
    batch_dir.mkdir(parents=True, exist_ok=True)
    for img in batch:
        shutil.copy2(img, batch_dir / img.name)

    # run VLM script
    env = os.environ.copy()
    cmd = ['python', str(SCRIPT), '-i', str(batch_dir), '-o', str(out_dir)]
    log_path = BASE / f'log_{domain}.txt'
    try:
        with open(log_path, 'a', encoding='utf-8') as logf:
            logf.write(f"\n--- batch {domain}: {[p.name for p in batch]} ---\n")
            result = subprocess.run(cmd, env=env, stdout=logf, stderr=subprocess.STDOUT, timeout=300)
            rc = result.returncode
    except subprocess.TimeoutExpired:
        return {'domain': domain, 'processed': 0, 'status': 'timeout', 'batch': [p.name for p in batch]}

    if rc != 0:
        return {'domain': domain, 'processed': 0, 'status': f'script exit {rc}', 'batch': [p.name for p in batch]}

    # mark processed
    for img in batch:
        shutil.move(img, done_dir / img.name)

    # cleanup batch dir
    shutil.rmtree(batch_dir)

    return {'domain': domain, 'processed': len(batch), 'status': 'ok', 'batch': [p.name for p in batch]}


def main():
    domains = ['单元模型', '科学决策']
    results = []
    with ProcessPoolExecutor(max_workers=2) as executor:
        futures = {executor.submit(process_domain, d): d for d in domains}
        for future in as_completed(futures):
            res = future.result()
            results.append(res)
            print(res)
    return results


if __name__ == '__main__':
    main()
