---
id: domain-digest-cards
title: "按域摘要卡——agent 入职加速层"
status: pending
priority: P3
assigned_to: 黄药师
reviewer: 欧阳锋
created: 2026-05-18
depends_on: P2（工业化手册 v1.7 + kdo backup）
---

## 背景

当前 agent 入职需消化 198 张卡（~1M tokens）。CLAUDE.md 已改为"消化 Core 55 张 + 按需 query"，进一步优化应在 Core 和 Extended 之间加一层**域摘要卡**——每个域一张 ~100 行摘要，agent 读完摘要就知道该域全貌，不必逐张翻 tool 卡。

## 产出物

每个域写一张 digest 摘要卡，路径 `30_wiki/concepts/`，命名 `digest-<domain>.md`。

### 格式规范

```markdown
---
title: "<域中文名>域摘要（Agent Digest）"
type: digest
domain: master
status: stable
---

## 一句话

<该域解决什么问题，一句话>

## 核心框架

<该域的 framework 卡有哪些，分别是什么>

## 关键工具（按使用频率）

| 卡片 | 一句话 | 什么时候用 |
|------|--------|-----------|

## 常见交叉引用

<该域工具最常和其他哪个域的哪张卡一起用>

## 新手路径

<如果是新人，建议按什么顺序读这个域的卡>
```

### 各域清单

| 域 | 卡片数 | 摘要卡路径 | 预估行数 |
|------|------|------|------|
| 创业（Entrepreneur） | 23 | `digest-entrepreneur.md` | ~120 |
| 管理（Management） | 17 | `digest-management.md` | ~100 |
| 个人修炼（Personal） | 26 | `digest-personal.md` | ~120 |
| 泛产品设计（Pan-Product） | 39 | `digest-panproduct.md` | ~150 |
| 销讲（Pitch） | 11 | `digest-pitch.md` | ~80 |
| 科学决策（Decision） | 9 | `digest-decision.md` | ~80 |
| Prompt 工程 | 6 | `digest-prompt.md` | ~60 |
| 调研（Research） | 5 | `digest-research.md` | ~60 |
| 跨域框架 | 22 | `digest-cross-domain.md` | ~120 |
| 主域方法论（Master） | 16 | `digest-master.md` | ~100 |

> 注：医疗和 AI SaaS 域卡片为外部研究报告，非标准 tool 卡，暂不纳入摘要范围。

合计 10 张摘要卡，~1,000 行。每张卡需阅读该域全部卡片后提炼。

## Token 效率

| 场景 | 旧方案 | 新方案 | 节省 |
|------|--------|--------|------|
| 入职 | 198 张全读 (~1M tokens) | Core 55 张 + 10 张 digest (~350K tokens) | 65% |
| 域切换 | 逐张读该域所有 tool 卡 (~80K tokens) | 读 1 张 digest (~3K tokens) | 96% |
| 跨域交叉 | 翻两个域的全量卡 | 读 2 张 digest + query 命中卡 | 90%+ |

## 验收标准

- [ ] 10 张 digest 卡全部完成，每张含"一句话 / 核心框架 / 关键工具 / 常见交叉引用 / 新手路径"五段
- [ ] 每张卡的工具表覆盖该域 ≥80% 的 tool cards
- [ ] 交叉引用段至少有 2 个具体的跨域链接
- [ ] `kdo lint` 零新增 warning
- [ ] `30_wiki/index.md` 更新，digest 卡加入 Core 层
- [ ] CLAUDE.md Step 1 消化顺序更新：读完 framework 后先读 digest，再按需读 tool 卡

## 执行策略

- 不是紧急任务——P3，排在 P2（手册 v1.7 + backup 自动化）之后
- 黄药师每完成一个域 P2 子项后，可顺手写该域 digest 作为"切换脑子"的休息任务
- 也可以等老顽童调研域编译完成后，由老顽童主笔（他读卡更系统化），黄药师审查

## 相关

- [[30_wiki/index]] — 分层索引
- [[kdo-infrastructure-backlog-proposal]] — 黄药师当前 backlog
- [[sprint-12-backfill-card-behavioral-requirements]] — v1.5 回填（所有 digest 基础）
