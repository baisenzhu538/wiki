---
id: sprint-12-backfill-card-behavioral-requirements
title: "Sprint 12：回溯升级——已有卡片补齐 v1.5 行为转化三要件"
status: pending
priority: P0
assigned_to: 黄药师
reviewer: 欧阳锋
domain: master
created: 2026-05-15
target: 2026-05-18
---

## 背景

工业化手册 v1.5 新增了卡片层行为转化三要件（§1.7），适用于方法/工具/框架类卡片：

1. **Critique → 外部攻击子节**：≥1 条真实外部批评（不带 straw man）
2. **Synthesis → "不要用的场景"表**：≥2 条（场景 + 失效机制 + 替代方案）
3. **Action Triggers 节**：≥3 个触发场景 + 第一动作 + 成功指标

Sprint 11 产出的 2 张新卡将是第一批 v1.5 实例。本 Sprint 将已有 ~140 张 yt-* 卡回溯升级，避免两套标准并存破坏库内一致性。

## 分批策略

KF-022 规定单次会话质量修复 ≤5 张卡。按卡片类型和影响面分三批，每批走完整 KDO 管线。

### Batch A：framework 卡（25 张）— P0，优先交付

**范围**：所有 `type: framework` 的 yt-* 卡

**升级内容**：三个新节全部追加
- `[Critique]` → 新增"外部攻击"子节
- `[Synthesis]` → 新增"不要用的场景"表
- body → 新增 `## Action Triggers` 节（Synthesis 之后）

**卡片列表**（25 张）：
```
yt-model-aesthetic-progression
yt-model-conversion-optimization
yt-model-agent-architecture
yt-model-deliberate-practice-growth
yt-model-entrepreneur-map
yt-model-dual-triangle-competitiveness
yt-model-five-step-canvas
yt-model-ipo-complete-checklist
yt-model-liberate-thinking-layers
yt-model-muse-ai-framework
yt-model-management-map
yt-model-ipo-learning-strategy
yt-model-deep-review-iceberg
yt-model-personal-map
yt-model-prediction-model
yt-model-personal-pitch-toolkit
yt-model-product-core-metrics
yt-model-progress-map
yt-model-product-excellence
yt-model-truman-career-routes
yt-model-questioning-practice-canvas
yt-model-prompt-engineering
yt-model-scientific-questioning-map
yt-model-y-organization
yt-model-truman-five-step-growth
```

**验收标准**：
- [ ] 25 张 framework 卡全部含"外部攻击"子节（≥1 条）
- [ ] 25 张 framework 卡全部含"不要用的场景"表（≥2 条）
- [ ] 25 张 framework 卡全部含 `## Action Triggers` 节（≥3 个触发项）
- [ ] 每条外部攻击引用了真实的反对者/竞争学派（非 straw man）
- [ ] 每个不要用场景含失效机制和替代方案
- [ ] 每个 Action Trigger 含可验证的成功指标
- [ ] `kdo lint` → 0 errors
- [ ] 欧阳锋抽检 5 张（20%），理解门禁三信号通过

### Batch B：tool 卡（85 张）— P0

**范围**：所有 `type: tool` 的 yt-* 卡

**升级内容**：三个新节全部追加（同 Batch A）

**卡片分类**：
| 域 | 数量 | 示例 |
|-----|:--:|------|
| entrepreneur（创业） | 24 | `yt-entrepreneur-*` |
| panproduct/execution（落地） | 20 | `yt-panproduct-execution-*` |
| panproduct/demand（需求） | 11 | `yt-panproduct-demand-*` |
| personal（个人修炼） | 11 | `yt-personal-*` |
| pitch/讲香（十指策略） | 10 | `yt-pitch-*` |
| prompt（提示词） | 4 | `yt-prompt-*` |
| panproduct/aesthetic（审美） | 5 | `yt-panproduct-aesthetic-*` |

**验收标准**：
- [ ] 85 张 tool 卡全部含三个新节（同 Batch A 标准）
- [ ] `kdo lint` → 0 errors
- [ ] 欧阳锋每域抽检 2 张（共 14 张，~16%），理解门禁通过

### Batch C：concept 卡（~30 张 yt-* concept）— P1

**范围**：所有 `type: concept` 的 yt-* 卡

**升级内容（精简）**：
- ❌ **不加**"外部攻击"子节——纯概念卡不承载操作指令，外部攻击对她意义不大
- ✅ 加"不要用的场景"表（≥2 条）
- ✅ 加 `## Action Triggers` 节（≥3 个触发项）

**注意**：部分 concept 卡偏索引/课程目录（如 `yt-system-course-catalog`、`yt-system-course-map-lecture`）——这些是纯导航页，可豁免全部三个新节。黄药师逐张判断，在 Phase 3 执行记录中标注豁免理由。

**验收标准**：
- [ ] 非豁免 concept 卡含"不要用的场景"表和 Action Triggers 节
- [ ] 豁免卡有明确的豁免理由记录
- [ ] `kdo lint` → 0 errors
- [ ] 欧阳锋抽检 5 张

## 执行约束

- **单次会话上限**：≤5 张卡（KF-022）
- **执行顺序**：Batch A → Batch B → Batch C，前一批通过审查后才能启动下一批
- **审而不改**：黄药师执行升级，欧阳锋逐批审查。欧阳锋不直接编辑卡片
- **标准文件**：`90_control/kdo-industrialization-manual.md` §1.7

## 不做

- ❌ 不新建卡——本 Sprint 只回溯已有卡
- ❌ 不改 frontmatter 字段——只追加 body 节
- ❌ 不修改 Claims / Constraints 已有内容——只追加新节

## 质量门禁（通用）

- [ ] `kdo lint` → 0 errors（每批完成后）
- [ ] 追加内容不破坏原有结构
- [ ] 外部攻击为真实外部批评（非自己想象的假反驳）
- [ ] 不要用场景含失效机制 + 替代方案（非"根据情况灵活运用"式废话）
- [ ] Action Triggers 三列完整（触发场景 + 第一动作 + 成功指标），成功指标可验证
- [ ] project-continuity.md 记录每批完成状态

---
## Batch A 进度 (5/25)

### Round 1 (2026-05-15) — 5 张完成

| # | 卡片 | 外部攻击 | 不要用场景 | Action Triggers | 状态 |
|---|------|---------|-----------|----------------|------|
| 1 | `yt-model-agent-architecture` | Gary Klein (RPD 模型) | 3 行（P争议/危机/高不确定探索） | 4 触发项 | ✅ |
| 2 | `yt-model-aesthetic-progression` | Shklovsky (陌生化) + Hume (品味主体性) | 4 行（新手/纯技术决策/紧急交付/激进创新） | 5 触发项 | ✅ |
| 3 | `yt-model-conversion-optimization` | BJ Fogg (B=MAT) + Brignull (欺骗性设计) | 2 行（产品缺陷/长决策链不可见） | 4 触发项 | ✅ |
| 4 | `yt-model-deliberate-practice-growth` | Ericsson (Peak修正) + Epstein (Range批判) | 3 行（探索期/0-1创新/组织建设） | 4 触发项 | ✅ |
| 5 | `yt-model-entrepreneur-map` | Taleb (Knight不确定性) + Blank (客户开发) | 3 行（PMF后/连续创业者/硬科技） | 4 触发项 | ✅ |

**质量验证**：
- `kdo lint` → 0 errors, 359 warnings (全为预存)
- 外部攻击全部引真实批评者/学派（非 straw man）
- 不要用场景全部含失效机制 + 替代方案
- Action Triggers 全部含可验证成功指标
- 原有内容未被修改

**剩余**: 20 张 framework 卡（下次会话继续）
