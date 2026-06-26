#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""P0-A 单元模型域 YAML 与 broken link 复核脚本"""
import yaml
import glob
import re
import os
import sys

VAULT_ROOT = r"C:\Users\Administrator\Desktop\wiki\30_wiki"

# P0-A 单元模型域 15 张卡 + 额外修复的 yt-tob-unit-model
CARD_IDS = [
    "tool-单元模型-单商圈",
    "tool-单元模型-单城市",
    "tool-单元模型-象限分析法",
    "framework-单元模型-外部对抗地图",
    "tool-单元模型-壁垒预判",
    "framework-TCPR底层网络协议",
    "dk-单元模型-找全成本实操难点",
    "dk-单元模型-找单元模型实操难点",
    "dk-单元模型-找基准值实操难点",
    "dk-单元模型-规模对抗实操难点",
    "dk-单元模型-对抗小抄",
    "concept-单元模型-学练用",
    "concept-最简单元模型",
    "case-unit-model-gashapon",
    "yt-unit-model-overview",
    "yt-tob-unit-model",
]

# 构建 30_wiki 下所有 md 文件路径索引（用于检查 wikilink 目标是否存在）
all_files = set()
all_ids = set()
for root, dirs, files in os.walk(VAULT_ROOT):
    for f in files:
        if f.endswith(".md"):
            full = os.path.join(root, f)
            rel = os.path.relpath(full, VAULT_ROOT).replace("\\", "/")
            all_files.add(rel)
            # id 是去掉 .md 的文件名
            cid = f[:-3]
            all_ids.add(cid)


def find_card_path(cid):
    patterns = [
        os.path.join(VAULT_ROOT, "tools", f"{cid}.md"),
        os.path.join(VAULT_ROOT, "frameworks", f"{cid}.md"),
        os.path.join(VAULT_ROOT, "dk", f"{cid}.md"),
        os.path.join(VAULT_ROOT, "concepts", f"{cid}.md"),
        os.path.join(VAULT_ROOT, "cases", f"{cid}.md"),
    ]
    for p in patterns:
        if os.path.exists(p):
            return p
    # fallback glob
    matches = glob.glob(os.path.join(VAULT_ROOT, "**", f"{cid}.md"), recursive=True)
    return matches[0] if matches else None


def extract_wikilinks(text):
    # 匹配 [[id]] 和 [[id|alias]]
    return re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", text)


yaml_failures = []
broken_links = []
domain_typos = []
missing_files = []

for cid in CARD_IDS:
    path = find_card_path(cid)
    if not path:
        missing_files.append(cid)
        print(f"MISSING FILE: {cid}")
        continue

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # YAML 解析
    try:
        parts = text.split("---", 2)
        if len(parts) >= 3:
            fm_text = parts[1]
            data = yaml.safe_load(fm_text)
            if data is None:
                data = {}
        else:
            yaml_failures.append((cid, "no frontmatter"))
            print(f"YAML FAIL: {cid} -> no frontmatter")
            continue
        print(f"YAML OK: {cid}")
    except Exception as e:
        yaml_failures.append((cid, str(e)))
        print(f"YAML FAIL: {cid} -> {e}")
        continue

    # 检查 id 与文件名一致
    if data.get("id") != cid:
        print(f"ID MISMATCH: {cid} frontmatter id={data.get('id')}")

    # domain typo 检查
    domains = data.get("domain", [])
    if isinstance(domains, str):
        domains = [domains]
    for d in domains:
        if d and str(d).count("-") > 1 and "yitang" in str(d):
            # 检查是否有类似 yitang- 开头但异常
            if "yitang-" in str(d) and not str(d).endswith("yitang"):
                domain_typos.append((cid, d))

    # broken link 检查
    links = extract_wikilinks(text)
    for link in links:
        # 去掉别名
        target = link.strip()
        if target not in all_ids:
            # 检查是否是文件路径
            target_rel = target + ".md"
            if target_rel not in all_files:
                broken_links.append((cid, target))

print("\n" + "=" * 60)
print(f"总卡片数: {len(CARD_IDS)}")
print(f"YAML 失败: {len(yaml_failures)}")
print(f"Broken link: {len(broken_links)}")
print(f"Domain typo: {len(domain_typos)}")
print(f"缺失文件: {len(missing_files)}")

if yaml_failures:
    print("\nYAML 失败详情:")
    for cid, err in yaml_failures:
        print(f"  - {cid}: {err}")

if broken_links:
    print("\nBroken link 详情:")
    for cid, link in broken_links:
        print(f"  - {cid} -> [[{link}]]")

if domain_typos:
    print("\nDomain typo 详情:")
    for cid, d in domain_typos:
        print(f"  - {cid}: domain='{d}'")

sys.exit(1 if yaml_failures or broken_links or missing_files else 0)
