---
id: "dk-ef-002-bom-version-async"
title: "BOM 多版本不同步：你手里的文件和产线手里的不是同一份"
type: "dark-knowledge"
dark_knowledge_type: "hardware-failure"
source_person: "黄药师"
source_context: "多人交接的硬件项目——原理图/BOM/PCB/Gerber/固件散落在多台电脑，版本混乱"
source_refs:
  - "90_control/electronics-practice/failure-modes-electronics.md"
created_at: 2026-06-07
updated_at: 2026-06-07
related:
  - "dk-ef-001-sn74lvc2g07-open-drain"
  - "dk-ef-003-hand-soldering-bom-divergence"
  - "dk-ef-004-missing-diagnostic-firmware"
tags:
  - None
  - None
  - None
  - None
  - None
  - None
pipeline:
  - None
  - None
  - "confidence-source-cited"
domain:
author: "legacy"
reviewed_by: "pending"
confidence: 0.75
trust_level: "medium"
---

# BOM 多版本不同步：你手里的文件和产线手里的不是同一份

## 原始表述

> E-FM-002：多人交接的硬件项目，原理图/BOM/PCB/Gerber/固件分散在多台电脑。新接手的人花 80% 时间理清哪个版本是对的，且容易用错版本。

**预防**：① 每个文件文件名必须含版本号+日期（如 `BOM_HX-SMJ-03-A_V2.1_2025-12-03.csv`）② 每次改版同步更新所有关联文件 ③ 项目根目录 README.md 维护版本对照表。

## 使用场景

- 项目从一个人交接给另一个人（离职/调岗/外包收尾）
- 你在 A 电脑上改了一版 BOM，B 电脑上的 BOM 还是旧的
- 固件编译时引用的头文件版本和原理图上的引脚定义对不上
- 你在 BOM 里看到"最新版"三个字但不知道"最新"是多新

## 操作方法

1. **文件命名纪律**：所有可交付文件必须含版本号+日期。格式：`<名称>_V<主>.<次>_<YYYY-MM-DD>.<扩展名>`。例如 `BOM_HX-SMJ-03-A_V2.1_2025-12-03.csv`
2. **版本对照表**：在项目 README.md 维护一张关键文件版本对照表——每个文件当前的"正确版本"是什么、在哪里
3. **改版同步**：改了一个文件 → 同时检查是否需要更新关联文件（原理图改了引脚 → BOM 可能需要改 → 固件 pin define 必须改）
4. **用 Git**：硬件文件（除了 PCB/Gerber 大文件）全部进 Git。`.gitignore` 排除 build 产物，但保留所有源文件

## 适用边界

- 适用于多人协作、有交接需求的硬件项目
- 不适用于个人一次性原型（你自己就是唯一的版本源）
- 如果团队已经在用 PLM/PDM 系统（如 Altium 365 / 嘉立创 EDA 云端），文件级版本管理由系统保障，不需要此方法

## 为什么值钱

软件工程师默认用 Git，版本追溯是呼吸一样自然的事。但硬件工程师的文件管理文化完全不同——大部分硬件工程师的文件命名是"最终版""最终版2""最终版真的""最终版不改了"，版本管理靠文件名里的感叹号数量。

这里的暗知识不是"要有版本控制"这个结论（谁都知道），而是**具体的执行纪律**：

- 版本号+日期的文件名格式——强制推行这条纪律是硬件项目管理从"看感觉"到"可追溯"的最小可行步骤
- "改一个文件同步检查关联文件"——硬件文件间的耦合比软件深得多（原理图改一个引脚 = BOM + 固件 + PCB 全要改），漏掉一个就是灾难
- 80% 时间浪费在"搞清哪个版本是对的"——这不是夸张，是实测数据
