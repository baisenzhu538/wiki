---
id: task_20260630_community-knowledge-failure-modes
type: task
status: pending_review
assignee: kimi
priority: P2
created_at: 2026-06-30
updated_at: '2026-06-30T16:15:41.948878+00:00'
reviewed_by: 欧阳锋
reviewer: 欧阳锋
source_refs:
- 00_inbox/AI-study/0071Vikki战队-2群 · 认知精华提炼.md
- 00_inbox/AI-study/0017大馨战队 · 短视频内容拆解方法论精华提炼.md
related:
- task_20260629_vikki-open-source-knowledge-boundary
- framework-community-knowledge-production-failure-modes
---

# 社群知识生产失败模式库（Vikki + 大馨融合）

## 目标

融合 Vikki 战队与大馨战队两个微信群聊的实战经验，沉淀一张 `framework-community-knowledge-production-failure-modes` 框架卡，为 KDO 多 Agent 协作、社群运营、知识众包提供失败模式清单和早期预警信号。

## 输入来源

### Vikki 战队 5 个失败模式

| 模式 | 信号 | 影响 |
|:---|:---|:---|
| F1 静默衰减 | 群超过 7 天无实质讨论 | 知识生产停滞 |
| F2 中心化瓶颈 | 核心人物不在则群停转 | 单点故障 |
| F3 信号退化 | 文字占比下降，图片/表情包上升 | 信息密度降低 |
| F4 搭便车 | 多数人只消费不生产 | 贡献者流失 |
| F5 知识外泄争议 | 外部人士「蒸馏」引发信任危机 | 开源信用受损 |

### 大馨战队 5 个失败模式

| 模式 | 信号 | 影响 |
|:---|:---|:---|
| F1 死亡螺旋 | 在线人数逐次下降 | 社群濒临解散 |
| F2 模板筋肉疲劳 | 长期使用同一框架导致厌倦 | 参与度下降 |
| F3 搭便车 | 只看不做，「感谢分享」但不参与拆解 | 训练效果差 |
| F4 讲师烧尽 | 每次准备时间远超过分享时间 | 核心产出者流失 |
| F5 平台依赖风险 | 方法论绑定特定平台算法 | 平台改版即失效 |

## 融合后的失败模式库结构

### 第一层：参与度衰竭

- 静默衰减 / 死亡螺旋
- 搭便车占多数
- 信号退化

### 第二层：生产结构脆弱

- 中心化瓶颈 / 讲师烧尽
- 模板筋肉疲劳
- 平台依赖风险

### 第三层：信任与边界危机

- 知识外泄争议
- 「抄作业」式边界试探的反噬
- AI 替代思考导致的内化缺失

## 待产出卡片

### 1. framework-community-knowledge-production-failure-modes（framework）

- **title**: 社群知识生产失败模式库
- **核心主张**: 社群/众包式知识生产有 10 种常见失败模式，可分为参与度衰竭、生产结构脆弱、信任边界危机三类，每类都有早期信号和修复动作。
- **必须包含**:
  - 10 个失败模式，每个包含：信号、原因、修复动作、案例来源
  - 早期预警指标清单
  - 与 KDO 五绝 Agent 协作的映射：
    - 静默衰减 → 段王爷跨角色简报缺失
    - 中心化瓶颈 → 欧阳锋成为唯一审查节点
    - 讲师烧尽 → 老顽童单实例过载
    - 搭便车 → Agent 只消费上下文不贡献产出
  - 与 `concept-open-source-knowledge-usage-boundary` 的链接

### 2. 可选配套：case-daxin-vikki-community-contrast（case）

- 对比 Vikki 群（自由讨论型）与大馨群（结构化训练型）的成败得失
- 作为 framework 的落地案例

## 执行要求

1. 每个失败模式必须有真实案例支撑（Vikki 或大馨群聊中的具体现象）。
2. 修复动作必须可执行，不能是「加强管理」这类空话。
3. 与 KDO 五绝架构的映射必须具体，能指导实际运维。
4. 跑 `kdo pre-submit` 通过。

## 验收标准

- framework 卡正文 ≥120 行
- 10 个失败模式全部包含信号 + 原因 + 修复动作
- `kdo pre-submit` 通过
- related ≥6，包含 concept-open-source-knowledge-usage-boundary、case-daxin-team-content-training-camp
- 欧阳锋终审：失败模式具体、修复动作可执行、与 KDO 映射合理

## 执行结果

### 已完成产出

| 卡片 ID | 类型 | 路径 | 状态 |
|---|---|---|---|
| framework-community-knowledge-production-failure-modes | framework | `30_wiki/frameworks/framework-community-knowledge-production-failure-modes.md` | enriched，pre-submit PASS |
| case-daxin-vikki-community-contrast | case | `30_wiki/cases/case-daxin-vikki-community-contrast.md` | enriched，pre-submit PASS |

### 质量验证

```text
Pre-Submit Gate Report
Files checked: 2
Passed:        2
Failed:        0
All gates passed. Ready for human review.
```

### 关联工作

- `30_wiki/index.md` 已补录 2 张新卡片条目。
- framework 卡与 case 卡之间已建立双向 related 链接。
- framework 卡包含 10 个失败模式（参与度衰竭 4 个 + 生产结构脆弱 4 个 + 信任与边界危机 2 个），每个模式包含信号、原因、修复动作、案例来源。
- 已补充早期预警指标清单、KDO 五绝映射、与 `concept-open-source-knowledge-usage-boundary` 的链接。

### 待欧阳锋终审事项

1. 10 个失败模式的分类是否合理，是否需要调整层级。
2. 修复动作是否足够具体可执行。
3. KDO 五绝映射是否贴切。
4. 可选 case 卡是否有价值，还是应合并到 framework 卡中。

### 已知问题

- KDO CLI (`python -m kdo`) 在 pre-submit 阶段触发 `SyntaxError: expected 'except' or 'finally' block`（`kdo/commands/delivery.py:686`），可能由代码中的不完整 try/except 块导致。本次 pre-submit 通过直接调用 `kdo.pre_submit.run_pre_submit()` 完成，结果与 CLI 等价。建议黄药师修复 KDO CLI。
