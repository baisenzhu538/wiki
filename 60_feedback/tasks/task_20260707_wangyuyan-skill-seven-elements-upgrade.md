---
id: task_20260707_wangyuyan-skill-seven-elements-upgrade
type: task
status: pending_review
assignee: hermes
reviewer: 欧阳锋
priority: P2
created_at: 2026-07-07
updated_at: '2026-07-06T18:55:05.579127+00:00'
source_refs:
- C:/Users/Administrator/Desktop/从知识库到agent.txt
related:
- '[[agent-spec-dual-triangle-canvas-filler]]'
- '[[method-kdo-agent-design-meta]]'
---

# 任务 #129：Skill/Agent-spec 七要素升级 dk 卡

## 来源

蓝鱼分享：Skill ≠ Prompt。完整 Skill 含七要素——Process/Standard/Example Output/Error Correction/Mini Loop/Trust Boundary/Known Pitfalls + 额外质量门控(Gating)。

## 核心内容

### KDO agent-spec 当前 vs 蓝鱼框架

| 要素 | KDO agent-spec v3 | 蓝鱼框架 | 缺口 |
|:---|:---|:---|:---|
| Process（流程） | ✅ 九层深挖流程 | ✅ | — |
| Standard（输出标准） | ✅ 输出门 | ✅ | — |
| Example（示范输出） | ✅ Few-shot 示例 | ✅ | — |
| Error Correction（纠错） | ❌ 缺失 | ✅ | **缺**：Agent输出错误时如何纠正 |
| Mini Loop（小循环） | ❌ 缺失 | ✅ | **缺**：小范围自我迭代机制 |
| Trust Boundary（边界） | 部分（不该用Agent清单） | ✅ | 需独立章节 |
| Known Pitfalls（已知坑） | 部分（失败模式） | ✅ | 需独立章节 |

### 升级内容

在 `agent-native-card-design.md` 中新增"Skill 七要素标准"章节，KDO 所有新 Agent/Skill 必须包含七要素。

## 验收

- dk 卡含七要素对照表（KDO vs 蓝鱼）
- `kdo pre-submit` PASS
