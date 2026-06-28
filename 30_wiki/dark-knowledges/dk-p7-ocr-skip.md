---

id: dk-p7-ocr-skip
title: P-7：素材预处理缺少 OCR 强制检查——执行者跳过图片
type: dk
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: system
source_context: pitfalls.md P-7
source_refs:
- src_unknown
created_at: 2026-06-03
updated_at: '2026-06-19'
related:
- [[ocr-婚礼操盘-用户和场景]]
- [[data-curator-role-division]]
- [[dk-p8-toolkit-forget]]
- [[ocr-一堂-单元模型-abcd策略模型]]
- [[ocr-screenshot2]]
- [[master-decision-hygiene]]
- [[master-ai-info-literacy]]
pipeline:
- src_unknown
- src_unknown
- src_unknown
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- src_unknown
- src_unknown
- src_unknown
- src_unknown# P-7：素材预处理缺少 OCR 强制检查——执行者跳过图片
---
## 原始表述/核心洞察

> **症状**：科学决策文件夹有 35 张关键框架图（共识四层冰山、ROI 全景图、X 型 Y 型对比等），老顽童声称"没有图片需要 OCR"。欧阳锋未核实即采信。后发现 35 张图全部未 OCR，图中含有口述稿未系统展开的结构信息。
>
> **根因**：
> 1. inbox 素材预处理缺少 OCR 检查点——没有强制步骤要求"如果文件夹里有 PNG，先跑 OCR 全部再进管线"
> 2. 架构者（欧阳锋）在长对话中判断力下降，未独立核实执行者的声明
>
> **对策**：
> - 新域素材消化第一步：扫描文件夹 → 如有图片，强制 OCR 全部后再读文本
> - 架构者审查新域提案时，独立验证"素材是否全部消化"——不能只信执行者的自述
> - 长对话中出现判断失误时主动收尾，下次干净状态接手

核心洞察：**多模态素材消化必须在流程层面设置强制检查点，不能依赖执行者自述或架构者临场判断**。当图片与文本互补时，跳过图片会丢失一半以上的结构信息；而防止跳过的唯一可靠方式，是"先扫描、再结论"的不可逆 checklist。

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **新域素材入库 checklist**：
   - src_unknown
   - src_unknown
   - src_unknown
   - src_unknown

2. **OCR 结果的使用**：
   - src_unknown
   - src_unknown
   - src_unknown

3. **架构者验证**：
   - src_unknown
   - src_unknown
   - src_unknown

4. **长会话管理**：
   - src_unknown
   - src_unknown
   - src_unknown

5. **不要做的事**：
   - src_unknown
   - src_unknown
   - src_unknown

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 常见失败模式

| 失败模式 | 典型信号 | 根因 | 修复动作 |
|
|---|---|---|
| 执行者声称"没有图片需要 OCR" | 素材文件夹含 PNG/JPG 但未触发 OCR 步骤 | 缺少"先扫描再结论"的强制检查点 | 入库 checklist 第一步：ls 文件夹，发现图片即强制 OCR |
| 架构者采信执行者自述未独立核实 | 审查时只看结论不看原始文件夹 | 过度信任执行者状态汇报 | 随机抽查 1-2 张图，确认 OCR 结果已进入管线 |
| 长会话末期做重要质量判断 | 讨论已进行 30+ 轮后仍在做 go/no-go | 认知疲劳导致判断力下降 | 重要审查安排在清醒状态，疲劳时主动收尾 |
| 把图片当文本的重复信息而跳过 | 认为"图只是口述稿的重复" | 未认识到图承载结构/比例/层级等文本未展开的信息 | 交叉验证图中结构与文本内容，确认互补而非重叠 |

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
