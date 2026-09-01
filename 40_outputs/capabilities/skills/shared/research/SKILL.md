---
name: research
title: 商业调研入口（#594 已并入 research-core，本卡为兼容薄壳）
description: 商业调研入口（已并入 research-core 统一入口，本卡为兼容薄壳——加载 research-core 获取三层完整路由：OSCAR 意图路由→核心纪律→专项武器库）
version: 1.1.0
author: 黄药师 / Skills 助理（#594 薄壳化）
adapted_from: business-research-skill-oscar-13-weapon-system
status: enriched
reviewed_by: 待审（欧阳锋，#594 提审后终审）
updated_at: 2026-09-02
license: MIT
platforms: [linux, macos, windows]
tags:
  - audience:executor
  - scene:research
  - research
  - 调研
metadata:
  hermes:
    tags: [research, 调研, OSCAR, 尽调, 行业分析, 竞品分析]
    related_skills: [research-core, research-financial-report, research-industry-report, research-web-scraping, research-cross-validation, research-expert-interview, research-osint]
---

# 商业调研入口（已并入 research-core）

> **#594（2026-09-02）整合**：本 skill 已并入 `research-core` 统一入口——调研能力升格为全 agent 基础能力层（老朱 09-02 拍板），三层结构：第一层 OSCAR 意图路由 / 第二层核心纪律（交叉验证+质量门禁+深挖引擎）/ 第三层专项武器库按需载。

**请加载 `research-core` 获取完整执行流程**（本卡保留仅为兼容旧引用，不承载新逻辑）。

- 触发词、OSCAR 定目标、武器库路由 → 见 `research-core`
- 原 KDO 工具链适配（`kdo-tools/research_adapter.py` OSCAR 流程） → 仍在，按 research-core 纪律层执行
