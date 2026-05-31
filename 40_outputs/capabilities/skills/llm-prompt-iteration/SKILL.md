---
title: "LLM Prompt 迭代方法论"
type: capability
subtype: skill
status: ready
target_user: AI agent or human optimizing LLM prompts for classification tasks
delivery_channel: local
source_refs:
  - sprint-20260531-retrospective
wiki_refs:
  - gold-standard-manual-labels
  - labeling-final-consolidation
created_at: 2026-05-31
updated_at: 2026-05-31
---

# LLM Prompt 迭代方法论

## Purpose

系统性地迭代优化LLM分类/标注prompt，用Gold Standard做基准测量，每次只改一个变量，记录delta，避免回退。

## When to Use

- 需要让LLM对文本做多维度分类/标注
- 初始准确率 < 50%，目标 > 85%
- 有手工标注的Gold Standard（15+条）

## When NOT to Use

- 没有Gold Standard——没有基准的优化是盲调
- 单次prompt就达到90%+——不需要迭代
- 开放生成任务（如写文章）——本方法论针对分类任务

## Protocol

### Step 1：建 Gold Standard（5%工作量，95%价值）

- 手工标注15-30条样本，覆盖主要类别
- 标注维度3-5个，每维度5-20个值
- 存储为可程序化读取的格式（Markdown表格+JSON皆可）
- 每位标注者记录理由，便于争议时回溯

### Step 2：测基线

```
1. 最简prompt（英文+基本描述）
2. 跑全量Gold Standard比对
3. 记录每维度准确率 + 总准确率
```

### Step 3：迭代循环

每轮只改**一个**变量：

| 变量 | 典型提升 | 何时用 |
|------|:--:|------|
| 英→中翻译prompt | +20-40% | 标注内容是中文时必做 |
| 多标签→单选 | +20-30% | 候选值>10个时必做 |
| 加3-5个few-shot示例 | +10-20% | 基线<50%时 |
| 对比区分描述 | +5-10% | 相似类别混淆时 |
| card/文档级上下文 | +5-15% | 标注粒度是chunk但类别依赖card属性时 |
| 降温(0.05→0.01) | +2-5% | 输出不稳定时 |

### Step 4：停止条件

- 准确率 ≥ 85%
- 连续2轮提升 < 2%
- 剩余错误全是"人也会犹豫"的边界case

### 每轮记录模板

```
v{N}: 改了什么 → 总准确率: X% (diff: +/-Y%)
  chunk_type: X%  method_family: X%  audience: X%  perspective: X%
  关键错误模式: [2-3条]
```

## Examples

### 完整迭代轨迹（2026-05-31 标注管线）

见 `20_memory/sprint-20260531-retrospective.md`

## 关键原则

1. **Gold Standard是唯一真相源**——没有它，prompt优化就是盲调
2. **一次只改一个变量**——否则不知道哪个改动起了作用
3. **保存每轮结果**——看不到退步就是最大的浪费
4. **区分"模型错了"vs"标注有争议"**——剩余error rate中有一部分是标注本身的不确定性
5. **中文few-shot > 英文描述 > 无示例**——这个顺序几乎总是成立
