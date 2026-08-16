---
name: stage-5-assetize
description: 域资产化——Workflow串联+模板固化+域索引更新+发布（全厂模式）
version: 1.0.0
author: 黄药师
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [KDO, 资产化, 发布, Workflow, 模板, Ship]
    related_skills: [domain-iteration, stage-4-validate]
---

# Stage 5: 域资产化

将验证通过的域卡片体系转化为可复用的最终资产。

## 触发词

资产化、发布域、做workflow、建模板、ship domain、收工发布

## 约束

- 阶段4验证报告必须显示 ≥60% 检索命中率
- Workflow 必须可由 Agent 按步骤执行
- Ship 前必须通过 `kdo validate`

## 执行步骤

### Step 1: 构建 Workflow
从域索引入口卡的"建议阅读路径"升级为完整 Workflow
路径：`30_wiki/systems/<域>-workflow.md`

### Step 2: 固化模板
分析报告模板 → `40_outputs/content/templates/`
检查清单模板 → `30_wiki/tools/`

### Step 3: 更新域索引入口卡
补充验证期间新增卡片，更新"待产"表

### Step 4: 更新全库索引
在 `30_wiki/index.md` 登记

### Step 5: Ship
```bash
kdo ship <域>-domain-digest --channel <channel>
```

## 完成标准
- [ ] Workflow 可由 Agent 执行
- [ ] 域索引入口卡已更新
- [ ] 全库 index.md 已登记
- [ ] `kdo ship` 完成

## 域生命周期
发布后域进入持续演化：新素材→阶段1 / 新案例→追加 / Agent反馈→阶段4循环
