---
id: task_20260707_wangyuyan-judge-skill-meta-evaluation.md
type: task
status: reviewed
assignee: hermes
reviewer: 欧阳锋
priority: P1
created_at: 2026-07-07
updated_at: '2026-07-06T18:36:51.099768+00:00'
source_refs:
- C:/Users/Administrator/Desktop/从知识库到agent.txt
related:
- '[[agent-spec-dual-triangle-canvas-filler]]'
- '[[method-kdo-agent-design-meta]]'
- '[[framework-yihang-dual-triangle-weapon-library]]'
reviewed_by: 欧阳锋
review_date: '2026-07-06'
---

# 任务 #128：Judge Skill——KDO Agent/Skill 元评估 method 卡

## 来源

蓝鱼分享：做了评判 Skill 的 Skill（Judge Skill），按五维度打分——输出标准/信任边界/已知坑/提示词约束/质量门控。30分→52分→84分→95分，3 轮迭代。

## 核心内容

### 五维度评估标准

借鉴蓝鱼框架，适配 KDO Agent/Skill 评估：

| 维度 | 检查什么 | KDO 对应 |
|:---|:---|:---|
| 输出标准 | 是否定义了期望输出格式与质量要求 | agent-spec 输出门 |
| 信任边界 | 适用领域 vs 不可迁移场景 | agent-spec When NOT to Use |
| 已知坑 | 列出常见失效情形 + 诊断信号 | agent-spec 失败模式 |
| 约束 | 提示词/规则约束，防止跑偏 | agent-spec 反幻觉规则 |
| 质量门控 | 内置自检机制 | agent-spec Action Triggers |

### 打分量表

| 分数 | 含义 |
|:---|:---|
| 30分 | 初版，有基本框架但缺标准/边界/坑/约束 |
| 50-60分 | 补了输出标准 + 边界 |
| 80+分 | 四维度齐（标准/边界/坑/约束） |
| 95分 | 五维度全齐 + 有真实测试验证 |

### 迭代流程

初版生成 → Judge Skill 评分→按反馈修改→重新评分→通常 3 轮从 30→90+

## 验收

- method 卡含五维度评估标准 + 打分表 + 迭代流程
- 含蓝鱼 30→95 迭代数据
- `kdo pre-submit` PASS
