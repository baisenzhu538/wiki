# -*- coding: utf-8 -*-
"""#583 狗粮测试 · 语料写入 Mnemosyne
用法：
  python ingest_mnemosyne.py probe   # 只写前2张，测单卡耗时
  python ingest_mnemosyne.py full    # 全量50张写入（幂等：先清空项目空间）
"""
import json, os, shutil, sys, time

from mnemosyne import MnemosyneMemory

WS = r"C:\Users\Administrator\Desktop\wiki"
HERE = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(HERE, "mnemo_store")  # 实验独立存储，不碰 ~/.mnemosyne
MANIFEST = os.path.join(HERE, "corpus_manifest.json")
PROJECT = "kdo-dogfood-583"


def build_memory():
    return MnemosyneMemory(base_dir=DB_DIR, k=5)


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "probe"
    manifest = json.load(open(MANIFEST, encoding="utf-8"))
    cards = manifest["cards"]
    if mode == "probe":
        cards = cards[:2]

    # 幂等：每次重建独立实验库（避免 probe+full 双写造成重复记录污染排名）
    if os.path.isdir(DB_DIR):
        shutil.rmtree(DB_DIR)

    memory = build_memory()
    total_chars = 0
    t0 = time.perf_counter()
    per_card = []
    for m in cards:
        p = os.path.join(WS, m["path"])
        text = open(p, encoding="utf-8", errors="replace").read()
        tc = time.perf_counter()
        memory.remember(
            text,
            project=PROJECT,
            source="wiki_card",
            meta={"wiki_path": m["path"], "card_id": m["path"].split("/")[-1][:-3], "stratum": m["stratum"]},
        )
        dt = time.perf_counter() - tc
        per_card.append(round(dt, 2))
        total_chars += len(text)
    wall = time.perf_counter() - t0
    print(f"mode={mode} cards={len(cards)} wall={wall:.1f}s avg={wall/len(cards):.2f}s/card chars={total_chars}")
    print("per_card_s:", per_card)


if __name__ == "__main__":
    main()
