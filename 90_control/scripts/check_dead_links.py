#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全库死链扫描脚本"""
import re
import os
import glob
import sys

VAULT_ROOT = r"C:\Users\Administrator\Desktop\wiki\30_wiki"

# 构建所有卡片 id 索引
all_ids = set()
all_files = {}
for root, dirs, files in os.walk(VAULT_ROOT):
    for f in files:
        if f.endswith(".md"):
            full = os.path.join(root, f)
            rel = os.path.relpath(full, VAULT_ROOT).replace("\\", "/")
            cid = f[:-3]
            all_ids.add(cid)
            all_files[cid] = rel


def extract_wikilinks(text):
    # [[id]] 或 [[id|alias]] 或 [[path/id|alias]]
    return re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", text)


def resolve_link(link):
    """尝试解析链接目标"""
    link = link.strip()
    # 去掉路径前缀
    if "/" in link:
        link = link.split("/")[-1]
    # 去掉 .md 后缀
    if link.endswith(".md"):
        link = link[:-3]
    return link


def main():
    dead_links = {}
    total_links = 0
    total_dead = 0

    files = glob.glob(os.path.join(VAULT_ROOT, "**", "*.md"), recursive=True)
    for path in files:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        links = extract_wikilinks(text)
        basename = os.path.basename(path)
        cid = basename[:-3]

        for link in links:
            total_links += 1
            target = resolve_link(link)
            if target not in all_ids:
                total_dead += 1
                if cid not in dead_links:
                    dead_links[cid] = []
                dead_links[cid].append((link, target))

    print(f"扫描文件数: {len(files)}")
    print(f"总 wikilink 数: {total_links}")
    print(f"死链数: {total_dead}")
    print(f"死链率: {total_dead/total_links*100:.2f}%")
    print(f"涉及文件数: {len(dead_links)}")
    print("=" * 70)

    # 按死链数量排序
    sorted_files = sorted(dead_links.items(), key=lambda x: -len(x[1]))
    print("\n死链最多的 20 个文件：")
    for cid, links in sorted_files[:20]:
        print(f"  {cid}: {len(links)} 个死链")
        for original, target in links[:5]:
            print(f"    - [[{original}]] -> 目标不存在: {target}")
        if len(links) > 5:
            print(f"    ... 还有 {len(links)-5} 个")

    # 特别检查 index.md
    if "index" in dead_links:
        print(f"\nindex.md 死链详情（共 {len(dead_links['index'])} 个）：")
        for original, target in dead_links["index"][:20]:
            print(f"  - [[{original}]] -> {target}")

    # 特别检查 concept-card-index-latest
    if "concept-card-index-latest" in dead_links:
        print(f"\nconcept-card-index-latest.md 死链详情（共 {len(dead_links['concept-card-index-latest'])} 个）：")
        for original, target in dead_links["concept-card-index-latest"][:20]:
            print(f"  - [[{original}]] -> {target}")

    return total_dead


if __name__ == "__main__":
    sys.exit(0 if main() == 0 else 1)
