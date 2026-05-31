---
title: "Auto-Label Gold Standard 评估基准"
type: capability
subtype: eval
status: ready
target_user: 任何需要验证标注管线准确率的 Agent
delivery_channel: local
source_refs:
  - gold-standard-manual-labels
  - labeling-final-consolidation
  - kdo-15-dimension-label-spec
wiki_refs: []
created_at: 2026-06-01
updated_at: 2026-06-01
definition_of_done:
  - 15条 chunk 覆盖 4 domain × 8 chunk_type
  - 每维度标注含理由说明
  - 比对脚本可独立复现
  - 准确率 ≥ 85% 为通过
---

# Auto-Label Gold Standard 评估基准

## Purpose

为 `auto_label_chunk()` 标注管线提供标准化的准确性评估。任何人修改 prompt 或管线后，跑一次本评估即可知道是否引入退步。

## 评估数据集

**来源**：`30_wiki/decisions/gold-standard-manual-labels.md`

| 属性 | 值 |
|------|----|
| 标注者 | 欧阳锋（Architect） |
| 标注日期 | 2026-05-31 |
| 样本数 | 15 chunk |
| 来源卡片 | 5 张（master-decision-hygiene, yt-decision-y-model, master-cognitive-bias-checklist, ai时代判断力口述-3） |
| domain 覆盖 | master(7) + yitang(8) |
| chunk_type 覆盖 | definition(3), procedure(2), critique(3), constraint(4), claim(2), question(1), action_trigger(1) |

## 评估维度

| 维度 | 值数 | 激活条件 |
|------|:--:|------|
| chunk_type | 19 | 必标 |
| method_family | 11 | 必标 |
| audience | 8 | 必标 |
| perspective | 6 | 必标 |
| confidence | 5 | 条件必标 |
| platform | 6 | 条件必标 |
| expiry | 5 | 条件必标 |
| prerequisite_knowledge | 5 | 条件必标 |
| usage_depth | 5 | 必标 |

## 使用方法

### 运行评估

```powershell
cd C:\Users\Administrator\Desktop\wiki
python _verify_gold_standard.py
```

输出写入 `60_feedback/data-quality/label-results/gold-standard-verify.json`。

### 评估通过标准

```
总准确率 ≥ 85%
且每维度准确率 ≥ 70%
```

### 评估脚本模板

```python
# _verify_gold_standard.py
from kdo.commands.label import llm_label_chunk, flatten_dimensions, load_tag_registry
from kdo.llm import LLMConfig

CORE = ["chunk_type","method_family","audience","perspective",
        "confidence","platform","expiry","prerequisite_knowledge","usage_depth"]

# 1. 读 Gold Standard
chunks = parse_gold("30_wiki/decisions/gold-standard-manual-labels.md")

# 2. 逐 chunk 比对
cfg = LLMConfig.from_yaml()
dims = {k:v for k,v in flatten_dimensions(load_tag_registry(root)).items() if k in CORE}
for chunk in chunks:
    decisions = llm_label_chunk(chunk["text"], dims, config=cfg, card_hint=chunk_card_hint(chunk))
    # 比对 decisions vs chunk["gold"]

# 3. 输出准确率矩阵
```

## 当前基线

| 维度 | 准确率 | 日期 | 模型 |
|------|:--:|------|------|
| chunk_type | 93% | 2026-05-31 | kimi-for-coding (DeepSeek V4) |
| method_family | 93% | 2026-05-31 | kimi-for-coding |
| audience | 87% | 2026-05-31 | kimi-for-coding |
| perspective | 80% | 2026-05-31 | kimi-for-coding |
| **总(4维)** | **88.3%** | 2026-05-31 | kimi-for-coding |

> 质量/价值 5 维（confidence/platform/expiry/prerequisite/usage_depth）2026-05-31 新增，首次基线待测。

## 变更记录

| 日期 | 版本 | 变更 |
|------|------|------|
| 2026-06-01 | v1.0 | 初始版本，含 15 chunk 基准 + 比对脚本模板 |
