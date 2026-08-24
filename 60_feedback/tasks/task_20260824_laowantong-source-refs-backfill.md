---
id: 495
assignee: laowantong
status: in_progress
updated_at: '2026-08-24T14:56:55.785789+00:00'
version: v0.1
instance: hermes
---

# #495 存量 source_refs: null 补字段（332 张）

- **任务号**：#495
- **状态**：queued
- **assignee**：laowantong（执行补字段；王语嫣出迁移规则/复核；欧阳锋终审）
- **优先级**：P2（不阻塞 #426 当前批次；补字段是溯源链修复，随 #493 归域模式）
- **立项**：2026-08-24 王语嫣（欧阳锋建议书 `diag_20260824_ouyangfeng-source-refs-null-gate-misfire.md` 裁定采纳方案 A）

## 背景

#426 第十六批验收发现：framework-一堂-关键假设 因 `source_refs: null` 被 pre-submit 机械判 FAIL 排除，但正文「## 来源与口径」段引用详实（主课口述行号 10+ 处 + 孔源口述 + 2 份 OCR）——**字段空 ≠ 来源无**，门禁打错了对象。

存量实测：**332 张** `source_refs: null`（其中 frameworks 125 张）；`related: null`/`aliases: null`/`quality_labels: null` 同族占位（历史批量建卡/早期字段规范不严时期）。

## 任务

- 参照 #493 归域模式：**扫描清单 → 批量执行 → 抽验**
- 332 张 null 卡补 `source_refs`：
  - 正文有「来源与口径」段的：来源段信息机械迁移进 frontmatter `source_refs`（保留行号引用原文格式）
  - 正文也无来源的：单独标记待补源清单（数量应为少数），不硬编造
- **同族 null 一并清**（方案 C 采纳并入本单）：`related: null`/`quality_labels: null`——同源占位习惯，随本单扫出后置空或补（aliases 部分已在 #494 治理，不重复）
- 来源信息以正文「## 来源与口径」段为一等锚（协议：事实断言挂锚点，无锚点不断言）

## 验证（验证分层）

- L1：补字段后 `source_refs: null` 残留归零（grep/脚本校验，活跃卡口径注明）
- L2 狗粮：抽查补字段卡，source_refs 与正文来源段一致（读正文核对，抽样≥3 张）
- L3 待活体：#426 后续批次不再因 source_refs null 机械排除

## 边界

- 只改 frontmatter `source_refs`（+同族 null），不动正文
- 无来源的卡不编造来源——标记待补源清单，交王语嫣复核
- 不阻塞 #426 当前批次（第十六批进行中）

## 关联

- 欧阳锋建议书 `diag_20260824_ouyangfeng-source-refs-null-gate-misfire.md`（本单裁定来源）
- #217（质量门禁 source_refs 判定——门禁语义由 #496 修）
- #493（归域模式参照：扫描清单→批量执行→抽验）
- #494（aliases null 同族已治理）
- #449（卡规范 §4 frontmatter 规范）

## 需要谁动作

- **王语嫣**：迁移规则（本单已含）+ 复核无来源标记卡
- **老顽童**：执行补字段（读正文来源段→迁 frontmatter）
- **欧阳锋**：终审本单（抽补字段准确性 + null 残留归零）

## 执行报告（F-034 五字段，complete 前必填）
