---
id: 540
assignee: huangyaoshi
status: queued
updated_at: '2026-08-26T11:00:00+00:00'
version: v0.1
instance: huangyaoshi
code_files:
  - 90_control/schemas/
  - 90_control/scripts/
---

# #540 VLM/OCR 卡两段式结构改造：原文与 AI 推断隔离（小昭事故根因 1）

- **任务号**：#540
- **状态**：queued
- **assignee**：huangyaoshi（schema+lint+存量批次；欧阳锋终审）
- **优先级**：P1（小昭误诊事故根因 1——VLM 臆测与 OCR 原文混在一个 confidence 下被当事实采信）
- **立项**：2026-08-26 王语嫣（小昭复盘改进 1 裁定采纳）

## 背景

`case-yihang-dual-triangle-AI三角-数据.md` 类 VLM 卡：整卡单一 confidence 0.7，OCR 原文（相对可靠）与「VLM 深度解析」（LLM 推断，含幻觉表）被同等对待。读者（人/Agent）无从分辨哪段能信。

## 任务

1. **两段式结构规范**：VLM/OCR 类卡正文必须分「OCR 原文」段（可引用）与「VLM 解析」段（首行 `> ⚠️ 以下为 AI 推断，未经交叉验证，不得作为事实引用`）；frontmatter 拆 `ocr_confidence` / `llm_analysis_confidence`（原 confidence 保留兼容=取低者）
2. **lint**：pre-submit/审查 checklist 增检——VLM 提取类卡（author 含 VLM/OCR 或有解析段）无两段式 → WARNING 起步
3. **存量批次**：扫描 30_wiki 全部 VLM/OCR 提取卡，出清单（数量/分布），批量挂警示段（内容不改，只加隔离标记）——批次方案报王语嫣裁定后执行
4. 矩阵登记纪律适用（lint 新检查项 → 同步通知覆盖矩阵/质量门禁相关台账，§3.19）

## 边界

- 只做结构隔离，不逐张审 VLM 解析内容对错（那是终审/draft 治理的事）
- 个案修复（双三角 case 卡）走 #539，不重复动

## 验收

- schema+lint 落地+回归；存量清单交王语嫣；欧阳锋终审
