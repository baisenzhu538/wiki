---
title: "Auto-Labeling Pipeline 工作流"
type: capability
subtype: workflow
status: ready
target_user: 黄药师（执行）+ 欧阳锋（审查）+ 老顽童（消费标注结果）
delivery_channel: local
source_refs:
  - labeling-final-consolidation
  - label-prompt-v10-final
wiki_refs:
  - gold-standard-manual-labels
  - kdo-15-dimension-label-spec
created_at: 2026-06-01
updated_at: 2026-06-01
definition_of_done:
  - 每阶段输入输出明确
  - 每个人职责清晰
  - 失败路径有回滚方案
---

# Auto-Labeling Pipeline 工作流

> 从原始 wiki 卡片到 9 维标注结果的端到端流程。

## 架构

```
┌─────────────┐     ┌──────────────┐     ┌──────────────┐     ┌─────────────┐
│  黄药师      │────→│  Labeler     │────→│  欧阳锋       │────→│  老顽童      │
│  准备卡片     │     │  Agent 标注   │     │  审查 + 抽检  │     │  消费标注结果 │
└─────────────┘     └──────────────┘     └──────────────┘     └─────────────┘
                          │                      │
                          ▼                      ▼
                   ┌──────────────┐     ┌──────────────┐
                   │ label-results│     │ Gold Standard │
                   │ .json        │     │ 比对验证       │
                   └──────────────┘     └──────────────┘
```

## Stage 0：准备（黄药师）

**输入**：待标注的卡片列表（card_id 或 batch size）

**操作**：
```bash
# 单卡
kdo label --card master-decision-hygiene --dry-run

# 批量 5 张
kdo label --batch 5 --dry-run
```

**输出**：dry-run 报告（每 chunk 的标注结果 + 路由决策）

**门禁**：
- [ ] tag-registry.yaml v1.1 存在且可解析
- [ ] LLM 配置有效（`kdo llm-check` PASS）
- [ ] card_hint 已为每张目标卡准备好

## Stage 1：自动标注（Labeler Agent）

**输入**：chunk 文本 + card_hint

**操作**：
```bash
kdo label --batch 5 --write
```

**输出**：`60_feedback/data-quality/label-results/{card_id}-labels.json`

每条标注含：
- 9 维标签值
- 置信度分数（0.0-1.0）
- 路由决策（auto_accept / review_pool / human_required）

**失败处理**：
- LLM 调用失败 → retry 1 次 → 仍失败则标记为 `human_required`
- JSON 解析失败 → 记录 raw response → 人工处理
- 写入失败 → 检查磁盘空间和权限

## Stage 2：质量审查（欧阳锋）

**输入**：标注结果 JSON + Gold Standard

**操作**：
```bash
# 跑 Gold Standard 比对
python _verify_gold_standard.py

# 抽检 20% 的 chunk（人工核对）
```

**审查清单**：
- [ ] Gold Standard 比对：总准确率 ≥ 85%？
- [ ] 每维度准确率 ≥ 70%？
- [ ] `human_required` 的路由比例 < 30%？
- [ ] 抽检 20% chunk 人工核对，误标率 < 15%？

**不通过处理**：
- 准确率 < 85% → 走 `label-accuracy-recovery` playbook
- 某维度 < 70% → 针对该维度调 prompt
- LLM 大量返回空 → 检查 API 配置或模型可用性

## Stage 3：回写 + 消费（黄药师 → 老顽童）

**操作**：
```bash
# 回写标注到卡片的 frontmatter 或 chunk registry
kdo label --card <id> --write --apply
```

**输出**：
- 卡片 frontmatter 更新（新增 `auto_labels` 或 chunk 注册表条目）
- 标注完成通知 → 老顽童

## 完整示例：Pilot 20 张卡

```bash
# Step 1: 准备 card_hints（黄药师）
python -c "
hints = {
  'master-decision-hygiene': '决策卫生（认知思维工具卡）',
  'yt-decision-y-model': 'Y模型决策框架（决策工具卡）',
  ...
}
"

# Step 2: 跑标注
kdo label --batch 20 --write

# Step 3: 质量审查（欧阳锋）
python _verify_gold_standard.py

# Step 4: 达标后全量
kdo label --batch 424 --write
```

## 关联资产

| 资产 | 路径 |
|------|------|
| Labeler Agent 定义 | `40_outputs/capabilities/agents/labeler-agent/AGENT.md` |
| Prompt (v10) | `40_outputs/capabilities/prompts/label-prompt-v10-final.md` |
| Gold Standard eval | `40_outputs/capabilities/evals/label-gold-standard/README.md` |
| 准确率恢复 playbook | `40_outputs/capabilities/playbooks/label-accuracy-recovery.md` |
| 管线代码 | `kdo/commands/label.py` |
| 标签规格 | `30_wiki/decisions/kdo-15-dimension-label-spec.md` |

---

*黄药师 · 2026-06-01*
