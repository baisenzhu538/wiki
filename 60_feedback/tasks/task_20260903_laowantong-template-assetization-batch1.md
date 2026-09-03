---
id: task_20260903_laowantong-template-assetization-batch1
title: 模板资产化批1：Agent 白皮书模板文件化 + 复盘画布/私董会SOP/双三角画布/回款playbook/产品画布族抽模板（落 capabilities/templates/）
seq: 632
status: in_progress
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-03
decision_source: 老朱 09-03 直令「模板是重要资产，按同标准排查全库同样处理」+ 王语嫣全库扫描（子代理严标准：可直接填空/照做才算）
reviewer: 欧阳锋
instance: laowantong
updated_at: '2026-09-03T02:10:18.624670+00:00'
---

# #632 模板资产化批1（老顽童）

## 标准（老朱口径）

模板=可直接使用的资产（填空即产出），落 `40_outputs/capabilities/templates/`（已有先例：template-article/checklist-proposal 等 6 件同目录）。每个模板文件：占位符驱动 + 头部注明来源卡 wikilink（回链知识层）+ 尾部使用说明三行。

## 本批范围（6+3 件）

1. **agent-whitepaper-template.md**（主令）：从 `tool-agent-whitepaper-full-lifecycle-template` 卡抽 11 节填空模板（五要素/权限三层/初始化 16 步/灵魂校验占位符化）。⚠️ 密级：kinda「不要外传」——模板文件头部继承传播限制标注
2. **retrospective-canvas.md** ← `tool-yitang-retrospective-canvas`（项目复盘画布，含 5Why 三层根因填空行）
3. **private-board-facilitation-sop.md** ← `tool-private-board-facilitation-sop`（90 分钟七步+主持人话术+收敛句式）
4. **dual-triangle-canvas.md** ← `tool-yihang-dual-triangle-canvas`（空版六宫格+每格引导问题）
5. **payment-collection-playbook.md** ← `tool-yitang-payment-collection-playbook`（决策表+9条催款 Checklist+关单确认表）
6. **产品画布族三件套**：product-kernel-canvas / business-model-canvas / demand-segmentation-canvas ← `yt-product-kernel-canvas` / `yt-business-model-canvas` / `yt-demand-segmentation-canvas`

## 不在本批（裁决留痕）

- #5 agent 生产检查单 vs 白皮书模板：互补不合并——检查单留卡层，模板文件化时在其「初始化 16 步」节末尾加「配套检查单见 [[tool-kdo-agent-production-checklist]]」引用
- #6 双三角 filler 的 System Prompt/自评表、#9 股权清单、#11 ROI 画布、#12 需求盲区（均有 src_unknown 空洞或重叠）——先补空洞再化，挂下批
- #15 视觉 prompt 模板族（inbox 素材层）——挂下批评估
- 不模板化清单（子代理判定我复核同意）：课程创作 11 步（价值在判断力不在骨架）、反脆弱五问（心智模型优先）、山西调研清单（一次性项目）、行业分析画布（内容不足先回源）

## 交付

- 9 个模板文件落 40_outputs/capabilities/templates/ + 每文件与源卡双向互链 + 执行报告（含逐件占位符可填性自检：假装自己是使用者填一遍关键位）
- claim/complete 走 queue_transition（complete 632）
