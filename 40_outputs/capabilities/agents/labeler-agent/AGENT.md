---
title: "Labeler Agent"
type: capability
subtype: agent
status: ready
target_user: AI agent performing auto-labeling on KDO wiki chunks
delivery_channel: local
source_refs:
  - label-prompt-v10-final
  - labeling-final-consolidation
wiki_refs:
  - gold-standard-manual-labels
  - kdo-15-dimension-label-spec
created_at: 2026-06-01
updated_at: 2026-06-01
definition_of_done:
  - task boundary explicit
  - inputs and outputs explicit
  - tool permissions declared
  - eval cases present
  - feedback path declared
---

# Labeler Agent

> 角色：KDO 知识工厂的自动标注员。对 wiki chunk 做 9 维度分类标注。

## Capability Type

agent

## Mission

接收知识 chunk 文本 + card 上下文，返回 9 维度标签（chunk_type / method_family / audience / perspective / confidence / platform / expiry / prerequisite_knowledge / usage_depth），含置信度分数和路由决策。

## Inputs

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `chunk_text` | string | yes | — | 待标注的知识 chunk 文本（≤3000 chars） |
| `card_hint` | string | yes | — | 卡片上下文描述，格式：`"{卡片名}（{类型}，{主题}"` |
| `dimensions` | list | no | 全部9维 | 需要标注的维度列表 |
| `model` | string | no | kimi-for-coding | LLM 模型 |

## Outputs

```json
{
  "labels": [
    {"dimension": "chunk_type", "value": "definition", "confidence": 0.80},
    {"dimension": "method_family", "value": "thinking-tool", "confidence": 0.80}
  ],
  "routing": "auto_accept | review_pool | human_required",
  "min_confidence": 0.70,
  "label_count": 9,
  "summary": "9 labels, min_conf=0.70 → review_pool"
}
```

## Tool Permissions

| Permission | Reason |
|------------|--------|
| Read `90_control/tag-registry.yaml` | 加载标签值池和 includes/excludes 描述 |
| Read `30_wiki/concepts/*.md` | 提取 card 上下文和 chunk 文本 |
| Call LLM API (kimi-for-coding) | Stage 2 推理 |
| Write `60_feedback/data-quality/label-results/` | 输出标注结果 |

## System Prompt

使用 `40_outputs/capabilities/prompts/label-prompt-v10-final.md` 中的 v10 prompt。

核心配置：
- temperature: 0.01
- max_tokens: 512
- 语言：中文
- 策略：9 维单选 + 7 few-shot + card 上下文

## Eval Cases

| Case | Input | Expected | Verified |
|------|-------|----------|:--:|
| Chunk 1 (偏差定义) | "偏差是系统性倾向..." + card_hint="决策卫生" | chunk_type=definition | ✅ |
| Chunk 3 (Klein 攻击) | "Gary Klein 对决策卫生提出根本性质疑..." | chunk_type=critique | ✅ |
| Chunk 9 (触发条件) | "触发场景：投入 ≥10 万元..." | chunk_type=action_trigger, perspective=roi | ✅ |

完整 eval 见 `40_outputs/capabilities/evals/label-gold-standard/`

## Feedback Path

- 标注结果写入 `60_feedback/data-quality/label-results/{card_id}-labels.json`
- 准确率对比写入 `60_feedback/data-quality/label-results/gold-standard-verify.json`
- 如有标注争议 → `kdo feedback --kind eval-results --title "Label Dispute: {card_id}"`

## Invocation

### CLI
```bash
kdo label --card master-decision-hygiene --dry-run
kdo label --batch 5 --write
```

### Python API
```python
from kdo.commands.label import llm_label_chunk, flatten_dimensions, load_tag_registry
from kdo.llm import LLMConfig

dims = {k:v for k,v in flatten_dimensions(load_tag_registry(root)).items()
        if k in CORE_DIMS}
cfg = LLMConfig.from_yaml()
decisions = llm_label_chunk(chunk_text, dims, config=cfg,
                            card_hint="决策卫生（认知思维工具卡）")
```

## Owner

黄药师（Builder）— KDO CLI 开发与维护。

## Change Log

| Date | Version | Change |
|------|---------|--------|
| 2026-06-01 | v1.0 | Initial agent definition |
