---

id: "ocr-一堂产品内核-十大典型指标"
created_at: 2026-05-21
domain:
  - src_unknown
source_refs:
  - src_20260522_32e4318a
status: draft
title: "OCR: 一堂产品内核-十大典型指标"
type: concept
updated_at: 2026-05-22
pipeline:
  - src_unknown
author: unknown
reviewed_by: pending
confidence: 0.6
trust_level: low
related:
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
---

# OCR: 一堂产品内核-十大典型指标

## Summary

原图: `00_inbox/一堂产品内核-十大典型指标.

png` 一堂产品内核・十大典型指标 环节 指标 一句话说明 销转率 看潜在客户转化为实际购买客户的比例 获客环节 动销率 看有销售的商品品种数与所有商品总品种数的比例 捕获率 看进店消费人数占总经过人流量的比例 留存率 看使用产品的用户，N天/周/月后还在持续使用的比例 完课率 看用户是不是能完成履约和最后学习 服务环节 退款率 看服务履约中，用户退款的比例 满意率 看用户接受完服务，满意度的比例和打分 复购率 看消费购买后，会继续购买的比例 复购环节 续费率 看续费用户数占现有用户数的比例 推荐率 看用户是否愿意主动推荐的比率 - 本文件由 PaddleOCR ONNX pipeline 自动提取 - 可能存在连字/误识，需要人工校对 - 视觉结构信息（标题/正文/表格分块）未在 OCR 中体现，需要结合原图理解

## Source Refs

- src_unknown

## Reusable Knowledge

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## Open Questions

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown


## Critique

### 内部局限

- src_unknown
- src_unknown
- src_unknown

### 外部攻击

#### Don Norman — “设计需要深度理解，不是通用模板”

Don Norman 在《设计心理学》中证明：好的设计需要深度理解特定用户、特定场景、特定约束。Norman 会质疑：**当你用"泛产品设计"的通用模板去处理具体问题时，你是否在用"产品术语重新包装一个你没有专业判断力的东西"？**

#### David Pye — “确定性手艺与风险性手艺的分野”

David Pye 在《手艺的本质与艺术》中区分了两种手艺形式。Pye 会质疑：**软件产品设计偏向"确定性手艺"，但泛产品设计指向的很多对象——制度设计、职业路径、个人知识体系——本质上是"风险性手艺"。** 把确定性手艺的"快速验证"方法论迁移到风险性手艺上，等于在拿手术刀切豆腐。

### 不要用的场景

- src_unknown
- src_unknown

## Synthesis

### 与本库其他概念的关联

- src_unknown
- src_unknown

### 可迁移场景

- src_unknown
- src_unknown

## Output Opportunities

Content: <article: "一堂产品指标诊断手册——从十大典型指标到增长飞轮设计" — 系统解析获客/服务/复购三环节指标的因果关系与计算口径，针对留存率周期模糊、满意率测量方式矛盾、复购与续费边界重叠等开放问题建立标准化定义框架，并输出各环节指标联动的诊断模板>
Code: <tool: `yitang-metrics-calculator.html` — 交互式单页应用，输入各环节原始数据后自动计算十大指标、可视化漏斗转化与环比趋势，内置"指标冲突检测"模块（如标记同一用户续费行为是否重复计入复购率）、支持导出KDO格式的分析报告YAML>
Capability: <playbook: "OCR-结构化知识生产流水线" — 整合PaddleOCR ONNX本地推理、视觉结构重建（表格/层级标题识别）、人工校对触发规则与KDO source YAML自动生成，解决OCR输出中视觉信息丢失、连字误识、指标分类层级模糊等系统性问题，形成从图片→结构化知识→指标诊断的闭环工作流>
