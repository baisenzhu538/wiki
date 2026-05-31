---
title: "标注准确率恢复 Playbook"
type: capability
subtype: playbook
status: ready
target_user: 黄药师（Builder）— 当 auto_label_chunk 准确率低于 85% 时执行
delivery_channel: local
source_refs:
  - sprint-20260531-retrospective
  - llm-prompt-iteration
wiki_refs:
  - gold-standard-manual-labels
  - label-prompt-v10-final
created_at: 2026-06-01
updated_at: 2026-06-01
---

# 标注准确率恢复 Playbook

> **触发条件**：Gold Standard 比对准确率 < 85%，或某维度 < 70%。
> **目标**：2 小时内恢复到 85%+。

## Step 1：确认基线（5min）

```bash
python _verify_gold_standard.py
```

记录 4 个关键数字：
- 总准确率
- 每维度准确率
- `auto=<missing>` 的维度数（可能是管线未激活）
- 退步最多的 3 条 chunk

## Step 2：诊断根因（10min）

按症状匹配根因表：

| 症状 | 最可能的根因 | 修复方向 |
|------|-------------|---------|
| **全维度 < 30%** | prompt 语言不匹配 / 模型切换后未适配 | 检查 prompt 语言与 chunk 语言是否一致；确认模型仍为 kimi-for-coding |
| **某维度 < 40%** | 该维度的 few-shot 示例缺失或不匹配 | 为该维度加 1-2 个针对性 few-shot 示例 |
| **某两个值大量混淆** | 对比区分描述不够清晰 | 加强对比描述："A ≠ B：A 有 X，B 有 Y" |
| **全部选 `general`** | LLM 保守策略，不敢选具体值 | 加"不要默认选 general"指令 + 降低 temperature |
| **大量 `<missing>`** | 管线未激活该维度 | 检查 `CORE_DIMS` 列表 + tag-registry 注册 |
| **method_family < 50%** | thinking-tool/decision-framework 边界模糊 | 加 card 上下文提示（最有效！） |
| **JSON 解析失败** | LLM 输出格式不稳定 | 简化输出格式，加"只输出 JSON"强调 |
| **准确率上下波动大** | temperature 太高 | 降到 0.01 |
| **比上次退步 > 10%** | prompt 改动引入副作用 / 模型变更 | 回退到上一个已验证版本，逐变量排查 |

## Step 3：执行修复（按优先级）

### 优先级 1：回退（5min）— 如果上次是好的

```bash
# prompt 有版本号备份
cp label-prompt-v{N-1}-final.md label-prompt-current.md
python _verify_gold_standard.py  # 确认恢复
```

### 优先级 2：加 card 上下文（15min）— 最有效

给每个待标注 chunk 加上 card_hint：
```python
CARD_HINTS = {
    "master-decision-hygiene.md": "决策卫生（认知思维工具卡，讨论偏差/噪声/判断分解等认知概念）",
    "yt-decision-y-model.md": "Y模型决策框架（决策工具卡，讨论ROI/宽度深度高度/决策矩阵）",
    ...
}
```

**验证**：card 上下文对 method_family 的提升通常 > +10%。

### 优先级 3：针对性 few-shot（20min）

1. 找出退步最多的 3 条 chunk
2. 手写它们的正确标注
3. 作为新的 few-shot 示例加入 prompt（总数 ≤7 个）
4. 跑比对验证 delta > +3%

### 优先级 4：加强对比区分（15min）

对混淆最多的两个值，改写描述：
```
- **A**：特征1、特征2。区别于 B：A 不包含 X。
- **B**：特征3、特征4。区别于 A：B 核心是 Y。
```

## Step 4：验证 + 归档（10min）

```
1. python _verify_gold_standard.py  → 确认 ≥ 85%
2. 全量 pytest → 确认无回归
3. 保存新 prompt 版本号
4. 更新 evals/label-gold-standard/ 的基线数据
```

## 无法恢复时的升级路径

| 尝试 | 仍 < 85% 时 |
|------|------------|
| 7 个 few-shot 全部重写 | 考虑切换模型（DeepSeek V4 → Claude Opus） |
| card 上下文已加 | 考虑标注维度简化（9→5，去掉最难的质量/价值维） |
| temperature 已降到 0 | 考虑 two-pass 策略（先粗分后细分） |
| 所有变量都试过 | **接受当前准确率为实用天花板**，记录边界case，标注为 `human_required` |

## 决策树速查

```
准确率 < 85%
    │
    ├── 上次 ≥ 85%？ → YES → 回退到上一版 prompt
    │
    ├── method_family < 50%？ → YES → 加 card 上下文
    │
    ├── 某维度全选 general？ → YES → 加针对性 few-shot + "不要默认选 general"
    │
    ├── 某两个值大量混淆？ → YES → 加强对比区分描述
    │
    ├── 大量 JSON 解析失败？ → YES → 简化输出格式 + 加解析容错
    │
    └── 全试过仍 < 85%？ → 评估剩余错误 → 全是边界case？ → 接受为天花板
```

## 关联资产

| 资产 | 路径 |
|------|------|
| Prompt 迭代方法论 | `40_outputs/capabilities/skills/llm-prompt-iteration/SKILL.md` |
| Gold Standard | `30_wiki/decisions/gold-standard-manual-labels.md` |
| 最终 prompt | `40_outputs/capabilities/prompts/label-prompt-v10-final.md` |
| 复盘文档 | `20_memory/sprint-20260531-retrospective.md` |

---

*黄药师 · 2026-06-01*
