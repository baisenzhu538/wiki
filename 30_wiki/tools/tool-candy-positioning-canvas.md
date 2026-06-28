---

id: tool-candy-positioning-canvas
title: Candy差异化定位画布：回答"这篇东西凭什么存在"
type: tool
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.88
trust_level: high
language: zh-CN
domain:
- yitang
- content-production
source_refs:
- 10_raw/sources/src_20260621_candy-transcript-workflow.md
related:
  - [[yitang-domain-digest]]
  - [[framework-candy-transcript-workflow]]
  - [[tool-马易-知识库-回答技巧双建设]]
  - [[concept-candy-ai-as-collaborator]]
  - [[case-candy-problem-os-vpn]]
  - [[tool-candy-oral-polish]]
---

# 差异化定位画布

> Candy的Step 2核心工具——在动笔之前回答：这篇内容凭什么存在？

## 四象限画布

```
           相同点
             ↑
  已有的内容  |  我的内容
   ←—————————+—————————→
             |
             ↓
           差异点
```

## 使用方法

1. **左上**：市场上已有的同类内容，在哪些方面做得不错？
2. **左下**：已有的内容，在哪些方面有缺失？（这是你的机会）
3. **右上**：你的内容，在哪些方面和已有内容一致？（不是差异化）
4. **右下**：**你要做的差异化是什么？（核心）**

## 核心命名原则

不要只讲材料，给它一个课程级概念。

| 材料堆砌（差） | 课程级概念（好） |
|:---|:---|
| "ESR聪明提问拆书会" | "Problem OS——问题操作系统" |
| "AI写作技巧分享" | "逐字稿九步法" |

**自检**：如果听众只记住一句话，应该是哪句？这句话就是你的定位。

## Agent执行指令

```python
prompt = """用差异化定位画布分析以下内容：

1. 左上（已有内容做得好的是什么）：
2. 左下（已有内容的缺口在哪）：
3. 右上（你的内容与已有内容一致的部分）：
4. 右下（你要做的差异化——核心）：

然后，为你的内容提炼一个"课程级概念"名称。规则：
- src_unknown
- src_unknown
- src_unknown
"""
```

## 失败模式

| 失败 | 症状 | 修复 |
|:---|:---|:---|
| 伪差异 | 差异点其实是"我更详细"而非真正的不同 | 追问：如果别人也写得详细，你的差异还在吗？ |
| 定位太窄 | 只有3个人关心这个话题 | 找"这个人群的共同痛点"而非"这个具体事件" |
| 命名太大 | "AI时代的内容革命"——什么都想涵盖 | 能在一句话里讲清楚吗？ |

## 适用边界

- src_unknown
- src_unknown

---

*卡片类型：tool | 审核状态：待审*

## 目的

> 待补充：这个工具解决什么问题？适用于什么场景？

## 操作步骤

1. **步骤一**：待补充
2. **步骤二**：待补充
3. **步骤三**：待补充

## 不要用的场景

> 待补充：什么情况下这个工具效果有限或不应该使用？

## 质疑

> 待补充：这个工具的内在局限是什么？外部反对者会怎么批评？
