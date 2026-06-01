---
title: "Pilot 20 标注分析报告"
type: evaluation
status: draft
domain: master
created_at: 2026-06-02
author: 黄药师
reviewer: 欧阳锋
---

# Pilot 20 标注分析报告

> **范围**：20 张卡、320 chunk、9 维全量标注
> **模型**：kimi-for-coding (DeepSeek V4)
> **日期**：2026-06-02

## 一、管线完整性：✅ 通过

320/320 chunk 全 9 维有值，不再有 `<missing>`。断裂点 1（enrich+label 串联）的代码路径已验证可跑通。

## 二、Bug 发现与修复

### Bug 1：chunk_type 组合值（已修复）

`reference/example/use_case/process_data/error_data` 作为单一值出现了 40 次（12.5%）。根因：prompt 中五行用 `/` 连写成一行，LLM 将整行理解为一个值。

**修复**：拆为独立行，每行一个值 + 简短描述。重跑后消失。

## 三、标注分布分析

### 3.1 分布合理的维度

| 维度 | 分布特征 | 判断 |
|------|------|:--:|
| chunk_type | procedure 16% + critique 13% + constraint 11% | ✅ 没有单一值垄断 |
| method_family | thinking-tool 41% + knowledge-engineering 35% | ✅ 与 KDO 卡片实际构成一致 |
| platform | general 100% | ✅ 合理——KDO 卡片几乎不涉及特定平台 |
| usage_depth | feed 77% + retrieval 13% + packaged 10% | ✅ 合理——大部分卡片目前是检索级 |

### 3.2 需要关注的维度

**audience：general 56.6%**

Gold Standard 中 general 占 53%（8/15），Pilot 中 56.6%。**差距仅 3.6 个百分点——不是 LLM 偷懒，是 KDO 卡片真实的受众分布。** 知识卡片天然面向通用受众，只有当内容明确涉及管理决策/技术实现时才会有 manager/developer 信号。

**结论**：不调 prompt。56% general 是合理的。

**perspective：general 64.5%**

Gold Standard 中 general 占 53%（8/15），Pilot 中 64.5%。差 11.5 个百分点。可能原因：Pilot 卡片中非专业视角的内容比例确实高于 Gold Standard 选卡。

**结论**：暂不调 prompt。等更多 Gold Standard 标注后再判断。

### 3.3 需要修复的维度

**confidence：0.70 占 59.7% —— 有效分辨率仅两档**

```
0.70: 59.7% ██████████████████████  ← 过度聚集
0.85: 21.2% ████████
0.90: 12.8% █████
0.50:  2.5% █
0.80:  1.2%                        ← 0.80 不是有效值（设计了 0.90/0.70/0.50/0.30）
```

问题：
1. LLM 生成了不在候选值的 `0.80`（4 次）——prompt 里的描述不够严格
2. `0.70`（单源强证据）被过度使用——LLM 倾向于选安全答案
3. `0.30`（假说/推测）完全没被使用——说明 KDO 卡片质量确实较高

**建议**：
- 在 prompt 中明确列出有效值：`0.90 / 0.70 / 0.50 / 0.30`
- 加一个 confidence 示例（展示什么时候标 0.90，什么时候标 0.50）
- 或者：接受 confidence 只有两档的现状，简化设计为三档（高/中/低）

**expiry：current 61.3% vs stable 37.8%**

```
current: 61.3% ████████████████████████
stable:  37.8% ███████████████
volatile: 0.9%
```

LLM 倾向于标 `current`（2-3 年需审查），可能因为 card_hint 里没有明确说"这是基础原理"还是"这是当前实践"。

**建议**：card_hint 增加时效性提示（如 `（基础原理，长期有效）`）。

## 四、对飞轮的反馈

Pilot 数据回答了"三个更深问题"中的两个：

| 问题 | 答案 |
|------|------|
| Pilot 选卡标准？ | 按 domain×type 分层抽样，优先高 chunk 密度卡 ✅ |
| 飞轮如何代码实现？ | `kdo label --card` 已可独立运行 → Sprint 6 串入 enrich |

还有一个待实验验证：
- confidence 简化 → 需要欧阳锋确认"两档够不够"
- expiry card_hint 增强 → 需要重跑 Pilot 看分布是否改善

## 五、下一步

| 行动 | 负责 |
|------|:--:|
| 确认 confidence 是否接受两档简化 | 欧阳锋 |
| card_hint 加时效性提示 → 重跑 expiry 维度 | 黄药师 |
| 修 chunk_type bug → 已修 ✅ |
| Pilot 数据作为 Sprint 6 断裂点 1 的输入 | 黄药师 |

---

*黄药师 · 2026-06-02*
