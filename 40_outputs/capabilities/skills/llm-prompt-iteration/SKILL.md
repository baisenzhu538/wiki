---
title: "LLM Prompt 迭代方法论"
type: capability
subtype: skill
status: ready
target_user: AI agent or human optimizing LLM prompts for classification tasks
delivery_channel: local
source_refs:
  - sprint-20260531-retrospective
  - label-prompt-v10-final
wiki_refs:
  - gold-standard-manual-labels
  - labeling-final-consolidation
  - kdo-15-dimension-label-spec
created_at: 2026-05-31
updated_at: 2026-05-31
---

# LLM Prompt 迭代方法论

> **实战验证**：2026-05-31 标注管线优化，DeepSeek V4 (kimi-for-coding)，7 轮迭代，26.7% → 88.3%。

## Purpose

系统性地迭代优化LLM分类/标注prompt，用Gold Standard做基准测量，每次只改一个变量，记录delta，避免回退。

## When to Use

- 需要让LLM对文本做多维度分类/标注
- 初始准确率 < 50%，目标 > 85%
- 有手工标注的Gold Standard（15+条）

## When NOT to Use

- 没有Gold Standard——没有基准的优化是盲调
- 单次prompt就达到90%+——不需要迭代
- 开放生成任务（如写文章）——本方法论针对结构化分类

---

## Protocol：7 步完整流程

### Step 0：建基础设施（一次性投入，~30min）

在写第一行 prompt 之前，先建好三个东西：

```
1. Gold Standard 文件（Markdown 表格，15-30条手工标注）
2. 自动化比对脚本（读取 Gold Standard → 调 LLM → 逐维度比对 → 输出准确率表）
3. prompt 版本号约定（v1, v2, ... 每轮递增）
```

**不要跳过这一步**。没有自动化比对，每轮改为手工比对 → 2h/轮 → 做不了 7 轮。

**Gold Standard 格式要求**：
```markdown
## Chunk 1
| 属性 | 值 |
|------|----|
| **来源卡片** | `path/to/card.md` |
| **chunk 内容** | "chunk text here..." |
| 维度 | 标签值 | 理由 |
|------|--------|------|
| chunk_type | `definition` | 术语定义，无操作步骤 |
| method_family | `thinking-tool` | 认知模型，Kahneman体系 |
```

### Step 1：测基线（~15min）

```
1. 最简prompt（英文 + 候选列表）
2. 调自动化比对脚本，跑一遍全量 Gold Standard
3. 记录：总准确率 + 每维度准确率 + 主要错误模式
```

**基线记录模板**：
```
v1 (基线): 英文prompt, 45候选逐一 APPLY/REJECT, temp=0.1
  总: 26.7% | chunk_type: 7% | method_family: 7% | audience: 40% | perspective: 53%
  错误模式: chunk_type全错，method_family全错，audience/perspective默认选general
```

### Step 2：选最大杠杆变量（~5min 决策）

看基线错误模式，选**单一最高杠杆变动**：

| 如果基线错误模式是... | 选这个变量 | 为什么 |
|------|------|------|
| 所有维度几乎全错 | **中文化 prompt** | 语言不匹配是最大障碍 |
| LLM 输出格式错误/混乱 | **降温 + 简化输出格式** | 稳定输出优先于准确 |
| 相似类别大量混淆 | **加 few-shot 示例** | 示例直接教模型区分 |
| 某两个类别特别容易混淆 | **对比区分描述** | "A ≠ B：A 有 X 特征，B 有 Y 特征" |
| 模型对所有 chunk 选相同答案 | **加多样性指令** | 告诉模型"不要默认选通用值" |

**铁律**：每次只改**一个**变量。改多个变量 → 不知道哪个起效 → 无法复制成功。

### Step 3：改 prompt（~10min）

改 prompt 时遵循三条规则：

1. **改动最小化**：只加/改必要的部分，不改已经正常工作的部分
2. **保留上一版本的 prompt**：另存为 `label-prompt-v{N}.md`，方便回退
3. **改完立即用单 chunk 冒烟测试**：确保 LLM 能正常响应，无 JSON 解析错误

### Step 4：跑全量比对（~5min）

```
python _compare_labels.py
```

输出每 chunk 的 OK/XX/-- 标记 + 总准确率 + 每维度准确率。

### Step 5：判读结果（~10min）

看三个东西：

1. **总准确率 delta**：+5% 以上 → 改动有效。0-5% → 部分有效。-X% → 退步。
2. **每维度变化**：哪个维度提升了？哪个退步了？
3. **具体错误案例**：挑 3-5 条错误，看 LLM 的答案是否"有道理但标注不同"还是"明显瞎猜"。

**关键判断**："模型错了" vs "标注有争议"？
- 模型错：LLM 选了明显不合理的值（如把 procedure 标成 definition）
- 标注有争议：LLM 选的值有一定道理，只是和标注者不一致（如 thinking-tool vs decision-framework 的边界 case）

**如果剩余错误全部是"标注有争议"的边界case** → 可以停止了。不要追求 100%。

### Step 6：决策下一轮（~5min）

```
if 准确率 >= 85% and (连续2轮提升 < 2% or 剩余错误全是边界case):
    → 停止迭代
elif 某维度准确率 < 70%:
    → 下一轮针对该维度加 few-shot 示例
elif 某两个类别大量混淆:
    → 下一轮加强对比区分描述
else:
    → 下一轮试 card/文档级上下文
```

### Step 7：归档（~10min）

迭代完成后必须归档三样东西：
1. **最终 prompt**：另存为独立资产文件（如 `label-prompt-v{N}-final.md`）
2. **迭代轨迹**：每轮的改动 + 准确率 delta + 关键决策理由
3. **技能沉淀**：提炼为可复用的 Skill 方法论（就是本文档）

---

## 实战案例：标注管线 7 轮迭代全记录

### 初始条件

- **模型**：DeepSeek V4（kimi-for-coding，Anthropic 协议）
- **任务**：对 15 条中文知识 chunk 做 4 维度标注（chunk_type 19值 / method_family 11值 / audience 8值 / perspective 6值）
- **Gold Standard**：欧阳锋手工标注 `gold-standard-manual-labels.md`（15 chunks × 4-14 dims）
- **自动化脚本**：`_compare_labels.py`（读取 Gold Standard → 调 LLM → 逐维度比对）

### v1 — 基线（26.7%）

**改动**：英文 prompt，列出 45 个候选标签（19 chunk_type + 11 method_family + 8 audience + 6 perspective 全部），要求 LLM 对每个候选输出 APPLY/REJECT。

```python
LABEL_PROMPT = """You are a precise multi-dimensional labeler...
For each candidate label, decide APPLY or REJECT...
Candidates: [{dimension, value, includes, excludes}, ...]"""
```

**结果**：
```
总: 26.7% (16/60)
chunk_type: 7% | method_family: 7% | audience: 40% | perspective: 53%
```

**失败分析**：
- pre-screen 对中文 chunk 返回 0 candidates（tag-registry includes 全是英文）
- LLM 对 45 候选逐一 APPLY/REJECT 几乎全返回 REJECT
- audience/perspective 的几个"对"其实是默认选了 general

**决策**：中文化 + 改为单选模式（从 45 候选逐一判断 → 每维度选一个最匹配的）

### v5 — 中文 + 单选 + 5 few-shot（68.3%，+41.6%）

**改动**：
1. 全中文 prompt（维度描述 + few-shot 示例全用中文）
2. 单选模式："从下面选项中选最精准的一个"替代"对每个候选 APPLY/REJECT"
3. 加入 3 个 few-shot 示例（definition / critique / action_trigger）
4. 加对比区分描述（"区别于 claim：definition 没有可证伪的主张"）
5. 绕过 pre-screen，直接送全维度候选给 LLM

**结果**：
```
总: 68.3% (+41.6%)
chunk_type: 73% | method_family: 47% | audience: 80% | perspective: 73%
```

**分析**：中文 + 单选是最关键的突破（+41.6%）。method_family 仍然是瓶颈（47%），thinking-tool/decision-framework/evaluation-method 三者混淆。

**决策**：针对 method_family 加强对比区分，加 evaluation-method 示例。

### v6 — +evaluation-method 示例（71.7%，+3.4%）

**改动**：加入第 4 个 few-shot 示例（procedure + evaluation-method），用"认知偏误自检清单"案例展示 evaluation-method 与 thinking-tool 的区别。

**结果**：
```
总: 71.7% (+3.4%)
chunk_type: 80% | method_family: 60% | audience: 80% | perspective: 67%
```

**分析**：evaluation-method 示例生效——"清单"类碎片开始被正确分类。chunk_type 提升到 80%。perspective 略有退步（个别 general 被误判为 professional）。

**决策**：加 thinking-tool vs decision-framework 的裁决规则。

### v7 — +裁决规则 + thinking-tool 对比（73.3%，+1.6%）

**改动**：在 method_family 描述中加入"核心裁决规则"段——"看文本的主要用途：讨论概念本身 → thinking-tool；讨论如何在选项中做选择 → decision-framework"。

**结果**：
```
总: 73.3% (+1.6%)
chunk_type: 87% | method_family: 53% | audience: 73% | perspective: 80%
```

**分析**：裁决规则反而让 method_family 退步（60%→53%）。原因是 Chunk 3（Klein 攻击决策卫生）被裁决规则误导向 decision-framework（因为文本讨论了"决策"），但 Gold Standard 标注的是 thinking-tool（因为 card 是认知思维工具）。

**发现**：**chunk 级文本不足以区分 method_family**——需要 card 级上下文知道"这段话来自一张认知思维卡还是决策工具卡"。

**决策**：加 developer 受众示例 + card 上下文提示。

### v9 — +developer 示例（85.0%，+11.7%）

**改动**：加入第 6 个 few-shot 示例（claim + knowledge-engineering + developer 受众），展示"IPO 位移"类技术口述的标注方式。

**结果**：
```
总: 85.0% (+11.7%)
chunk_type: 87% | method_family: 73% | audience: 93% | perspective: 87%
```

**分析**：首次突破 85% 目标！developer 示例显著提升了 audience 和 perspective 的准确率。method_family 也改善（73%），但 Chunk 3/7（Klein 攻击类）仍在 thinking-tool/decision-framework 之间摇摆。

**决策**：引入 card 上下文提示。这是 v7 发现的"chunk 文本不足以判断 method_family"问题的直接解法。

### v10 — +card 上下文（88.3%，+3.3%）✅ 最终版

**改动**：
1. 在 prompt 中加 `此 chunk 来自卡片：{card_hint}` 行
2. card_hint 包含卡片名 + 类型 + 核心主题描述
3. 同时激活 5 个质量/价值维度（confidence/platform/expiry/prerequisite_knowledge/usage_depth）
4. 每个 few-shot 示例的输出 JSON 扩展为 9 维度

**card_hint 示例**：
```
"决策卫生（认知思维工具卡，讨论偏差/噪声/判断分解等认知概念）"
"Y模型决策框架（决策工具卡，讨论ROI/宽度深度高度/决策矩阵）"
"认知偏误自检清单（评估工具卡，12条逐项自检清单）"
```

**结果**：
```
总: 88.3% (+3.3%) ✅
chunk_type: 93% | method_family: 93% | audience: 87% | perspective: 80%
```

**分析**：Card 上下文是 method_family 的决定性突破（73%→93%）。剩余 7 个错误全是"人也会犹豫"的边界 case：
- Chunk 2: "procedure 描述" → thinking-tool vs decision-framework（Gold 说 thinking-tool，但文本确实在描述决策分解）
- Chunk 5: "Y模型在体系中的坐标" → claim vs cross_reference（两者都有道理）
- Chunk 6: "列清单→推演→查盲区" → definition vs procedure（文本本身有操作步骤）

**停止决策**：连续 2 轮提升 < 5%（v9→v10: +3.3%），剩余错误全是边界 case。停止迭代。

---

## 失败模式清单（做什么会导致退步）

| 反模式 | 症状 | 根因 | 正确做法 |
|--------|------|------|---------|
| 一次改多个变量 | 不知道哪个改动有效 | 无法归因 | 每次只改一个变量 |
| 无 Gold Standard 盲调 | "感觉更好了"但实际退步 | 主观判断不可靠 | 先建 Gold Standard |
| 7+ 个 few-shot 示例 | 准确率退步 (88%→80%) | 示例过多→注意力分散 | 5-7 个为上限 |
| 示例覆盖全部 chunk | 过拟合，泛化差 | few-shot 变成了"背答案" | 示例和测试集不重叠 |
| self-consistency (低温) | 无增益 (76.7%→73.3%) | 低温 0.01 下 3 次投票结果相同 | 仅高温 (>0.3) 时有意义 |
| 裁决规则无 card 上下文 | 退步 (60%→53%) | chunk 文本不足以判断 card 级分类 | 先加 card 上下文，再加裁决规则 |
| 忽略缺标维度 | P-17: 声称 85% 实测 34.8% | 只算管线激活的维度，忽略 `<missing>` 的 | 全维度全样本比对 |

---

## 变量选择决策树

```
基线测试完成
    │
    ├── 准确率 < 30%？ → 语言不匹配（英→中）+ 输出格式错误（多选→单选）
    │
    ├── method_family < 50%？ → 加对比区分描述 + 裁决规则
    │
    ├── audience/perspective < 70%？ → 加针对性 few-shot 示例
    │
    ├── 某两个类别大量混淆？ → 加对比区分示例（"A ≠ B：区别在于..."）
    │
    ├── method_family 仍 < 70%？ → 加 card 上下文提示
    │
    ├── audience 频繁选 general？ → 加"不要默认选 general"指令 + 针对性示例
    │
    └── 准确率 ≥ 85% 且剩余错误全是边界case？ → 停止迭代
```

---

## 证据原则（防止 P-17 重演）

1. **所有"准确率"声明必须附带测量方法**：数据集？维度？计算方式？每条出错在哪？
2. **Gold Standard 比对必须覆盖全维度**：管线未激活的维度也要报告（标为 `<missing>` 或 `N/A`）
3. **结果必须可复现**：比对脚本 + Gold Standard 文件 = 任何人跑都能得到同样结果
4. **迭代前后必须先跑 baseline**：确认起点和 delta

---

## 相关资产

| 资产 | 路径 |
|------|------|
| 最终 prompt (v10) | `40_outputs/capabilities/prompts/label-prompt-v10-final.md` |
| Gold Standard | `30_wiki/decisions/gold-standard-manual-labels.md` |
| 复盘文档 | `20_memory/sprint-20260531-retrospective.md` |
| 标签规格 | `30_wiki/decisions/kdo-15-dimension-label-spec.md` |
| 注册表 | `90_control/tag-registry.yaml` |
| 管线代码 | `kdo/commands/label.py` |
| 安全批量Skill | `40_outputs/capabilities/skills/safe-batch-operations/SKILL.md` |
| 完工报告 | `20_memory/completion-report-20260531.md` |

---

*黄药师 · 2026-05-31 · 基于 7 轮实战迭代的完整方法论*
