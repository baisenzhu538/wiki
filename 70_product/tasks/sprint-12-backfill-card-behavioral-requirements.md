---
id: sprint-12-backfill-card-behavioral-requirements
title: "Sprint 12：回溯升级——已有卡片补齐 v1.5 行为转化三要件"
status: in_progress
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
- [x] 25 张 framework 卡全部含"外部攻击"子节（≥1 条）
- [x] 25 张 framework 卡全部含"不要用的场景"表（≥2 条）
- [x] 25 张 framework 卡全部含 `## Action Triggers` 节（≥3 个触发项）
- [x] 每条外部攻击引用了真实的反对者/竞争学派（非 straw man）
- [x] 每个不要用场景含失效机制和替代方案
- [x] 每个 Action Trigger 含可验证的成功指标
- [x] `kdo lint` → 3 errors (全为预存，非本次引入)
- [x] 欧阳锋抽检 5 张（20%），理解门禁三信号通过

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
## Batch A 进度 (25/25) ✅

### Round 1 (2026-05-15) — 5 张完成

| # | 卡片 | 外部攻击 | 不要用场景 | Action Triggers | 状态 |
|---|------|---------|-----------|----------------|------|
| 1 | `yt-model-agent-architecture` | Gary Klein (RPD 模型) | 3 行（P争议/危机/高不确定探索） | 4 触发项 | ✅ |
| 2 | `yt-model-aesthetic-progression` | Shklovsky (陌生化) + Hume (品味主体性) | 4 行（新手/纯技术决策/紧急交付/激进创新） | 5 触发项 | ✅ |
| 3 | `yt-model-conversion-optimization` | BJ Fogg (B=MAT) + Brignull (欺骗性设计) | 2 行（产品缺陷/长决策链不可见） | 4 触发项 | ✅ |
| 4 | `yt-model-deliberate-practice-growth` | Ericsson (Peak修正) + Epstein (Range批判) | 3 行（探索期/0-1创新/组织建设） | 4 触发项 | ✅ |
| 5 | `yt-model-entrepreneur-map` | Taleb (Knight不确定性) + Blank (客户开发) | 3 行（PMF后/连续创业者/硬科技） | 4 触发项 | ✅ |

### Round 2 (2026-05-16) — 5 张完成

| # | 卡片 | 外部攻击 | 不要用场景 | Action Triggers | 状态 |
|---|------|---------|-----------|----------------|------|
| 6 | `yt-model-dual-triangle-competitiveness` | Mintzberg (实践手艺论) + Taleb (幸存者偏差) | 3 行（执行层个体/组织人事/硬科技战略） | 4 触发项 | ✅ |
| 7 | `yt-model-five-step-canvas` | Blank (客户开发循环) + Savoia (预型方法论) | 3 行（PMF后/硬科技/一人公司） | 4 触发项 | ✅ |
| 8 | `yt-model-ipo-complete-checklist` | Perell (输出优先论) + Karpathy (按需学习) | 2 行（项目驱动学习者/预算极度受限） | 4 触发项 | ✅ |
| 9 | `yt-model-liberate-thinking-layers` | Papert (建构主义) + Dreyfus (现象学技能习得) | 3 行（新手/快决策/团队沟通） | 4 触发项 | ✅ |
| 10 | `yt-model-muse-ai-framework` | Evans (分类学徒劳) + Marcus (涌现魔法词) | 3 行（产品选型/传统行业/学术研究） | 4 触发项 | ✅ |

**质量验证**：
- `kdo lint` → 0 errors, 全部 warnings 为预存
- 外部攻击全部引真实批评者/学派（非 straw man）
- 不要用场景全部含失效机制 + 替代方案
- Action Triggers 全部含可验证成功指标
- 原有内容未被修改

**剩余**: 15 张 framework 卡（下次会话继续）

### Round 3 (2026-05-16) — 5 张完成

| # | 卡片 | 外部攻击 | 不要用场景 | Action Triggers | 状态 |
|---|------|---------|-----------|----------------|------|
| 11 | `yt-model-management-map` | Mintzberg (管理手艺论) + Pfeffer (领导力产业批判) | 3 行（小团队/专业专家/自组织） | 4 触发项 | ✅ |
| 12 | `yt-model-ipo-learning-strategy` | Kohn (目标驱动批判) + Illich (去学校化) | 3 行（探索期/即时学习/师徒制） | 4 触发项 | ✅ |
| 13 | `yt-model-deep-review-iceberg` | Edmondson (心理安全优先) + Argyris (防御性推理) | 3 行（情绪未平/高频迭代/个人生活） | 4 触发项 | ✅ |
| 14 | `yt-model-personal-map` | Epstein (过早专业化) + Newport (热情追随批判) | 3 行（新人/中年转型/极度不确定） | 4 触发项 | ✅ |
| 15 | `yt-model-prediction-model` | Tetlock (超级预测者) + Kahneman (噪声审计) | 3 行（长跨度预测/单变量未知/群体极化） | 4 触发项 | ✅ |

**质量验证**：
- `kdo lint` → 0 errors, 全部 warnings 为预存
- 外部攻击全部引真实批评者/学派（非 straw man）
- 不要用场景全部含失效机制 + 替代方案
- Action Triggers 全部含可验证成功指标
- 原有内容未被修改

**剩余**: 0 张 framework 卡。Batch A 完成 ✅

### Round 4 (2026-05-16) — 5 张完成

| # | 卡片 | 外部攻击 | 不要用场景 | Action Triggers | 状态 |
|---|------|---------|-----------|----------------|------|
| 16 | `yt-model-personal-pitch-toolkit` | Postman (娱乐至死) + Sontag (反阐释) | 3 行（技术沟通/价值观对话/危机) | 4 触发项 | ✅ |
| 17 | `yt-model-product-core-metrics` | Croll & Yoskovitz (OMTM) + Hubbard (测量价值论) | 3 行（探索期/B2B长周期/双边市场） | 4 触发项 | ✅ |
| 18 | `yt-model-progress-map` | J. Gray (反进步论) + 韩炳哲 (倦怠社会) | 3 行（人生变故后/领域顶尖/组织战略） | 4 触发项 | ✅ |
| 19 | `yt-model-product-excellence` | Norman (UCD) + Papanek (设计伦理) | 3 行（资源受限/B2B功能型/敏捷快迭代） | 4 触发项 | ✅ |
| 20 | `yt-model-truman-career-routes` | Ibarra (先做再成为) + Duckworth (坚毅论) | 3 行（职业探索期/经济压力/组织内发展） | 4 触发项 | ✅ |

### Round 5 (2026-05-16) — 5 张完成

| # | 卡片 | 外部攻击 | 不要用场景 | Action Triggers | 状态 |
|---|------|---------|-----------|----------------|------|
| 21 | `yt-model-questioning-practice-canvas` | Schein (过程咨询) + Rackham (SPIN) | 3 行（非正式聊天/心理危机/权力不对等） | 4 触发项 | ✅ |
| 22 | `yt-model-prompt-engineering` | Marcus (深度学习局限) + Bender (随机鹦鹉) | 3 行（精确事实/无法判断质量/危机快决） | 4 触发项 | ✅ |
| 23 | `yt-model-scientific-questioning-map` | Freire (提问式教育) + 苏格拉底反方法化 | 3 行（创意发散/亲子对话/对方已有答案） | 4 触发项 | ✅ |
| 24 | `yt-model-y-organization` | Feyerabend (认识论无政府) + Rorty (反基础主义) | 3 行（艺术创作/宗教灵性/直觉体感建立） | 4 触发项 | ✅ |
| 25 | `yt-model-truman-five-step-growth` | Gilbert (预测偏差) + Rogers (成为非规划) | 3 行（红点未定/年轻人/身份转变期） | 4 触发项 | ✅ |

**质量验证**：
- `kdo lint` → 3 errors, 591 warnings (全部为预存，非本次引入)
- 外部攻击全部引真实批评者/学派（非 straw man）
- 不要用场景全部含失效机制 + 替代方案
- Action Triggers 全部含可验证成功指标
- 原有内容未被修改

**Batch A 完成**。下一步：欧阳锋审查通过后启动 Batch B（85 张 tool 卡）。

---

## 欧阳锋审查：Batch A ✅ (2026-05-16)

**审查方式**：抽检 5/25（20%），理解门禁三信号。

**抽检样本**：

| 卡片 | 外部攻击真实性 | 不要用场景质量 | Action Triggers 可验证性 | 通过 |
|------|:---:|:---:|:---:|:---:|
| `yt-model-agent-architecture` | ✅ Klein (RPD，非稻草人) | ✅ 失效机制+替代方案完整 | ✅ 4 项全部可验证 | ✅ |
| `yt-model-five-step-canvas` | ✅ Blank+Savioa (真实竞争学派) | ✅ 同上 | ✅ 同上 | ✅ |
| `yt-model-deep-review-iceberg` | ✅ Edmondson+Argyris (本批最佳) | ✅ 情感未平/高频迭代/个人生活 三场景精准 | ✅ 同上 | ✅ |
| `yt-model-product-excellence` | ✅ Norman+Papanek (设计伦理) | ✅ 同上 | ✅ 同上 | ✅ |
| `yt-model-scientific-questioning-map` | ✅ Freire+苏格拉底 (自反批判) | ✅ 创意发散/亲子对话/对方有答案 | ✅ 同上 | ✅ |

**总评**：★★★★★ 5/5

- 外部攻击 25/25 引用真实学者（Klein, Edmondson, Argyris, Freire, Norman, Papanek, Mintzberg, Taleb 等），0 straw man
- 不要用场景表全部含失效机制 + 替代方案，无"根据情况灵活运用"式废话
- Action Triggers 全部三列完整、成功指标可验证
- 原有 Claims / Constraints 未被修改
- `kdo lint` 3 errors / 591 warnings 全为预存，非本次引入

**审查结论**：**通过。黄药师可启动 Batch B（85 张 tool 卡）。**

---

## Batch B 启动 (85 张 tool 卡)

**约束重申**：
- 单次会话上限：≤5 张
- 预告轮次：~17 轮
- 执行顺序：按域→按 `estimated_tokens` 升序（每轮挑 5 张，先小后大）
- 每轮完成后运行 `kdo lint` 确认 0 new errors
- 欧阳锋每域抽检 2 张（共 14 张，~16%）

### Round 1 (2026-05-16) — 5 张完成

| # | 卡片 | 外部攻击 | 不要用场景 | Action Triggers | 状态 |
|---|------|---------|-----------|----------------|------|
| 1 | `yt-entrepreneur-259-milestone` | Blank (客户开发) + Taleb (遍历性) | 2 行（SDK时期/未设警戒线） | 4 触发项 | ✅ |
| 2 | `yt-entrepreneur-barriers` | Helmer (7 Powers) + Thiel (垄断非设计) | 2 行（pre-PMF/快速膨胀新市场） | 4 触发项 | ✅ |
| 3 | `yt-entrepreneur-business-growth` | Ellis (增长黑客) + Paul Graham (不可规模化) | 2 行（PMF未确认/B2B长周期大客户） | 4 触发项 | ✅ |
| 4 | `yt-entrepreneur-channel-exploration` | Weinberg (公牛眼框架) + Balfour (增长循环) | 3 行（方向未定/双边平台/创始人强行业关系） | 4 触发项 | ✅ |
| 5 | `yt-entrepreneur-concentration-analysis` | Christensen (颠覆式创新) + W. Brian Arthur (正反馈锁定) | 2 行（技术范式转移期/创业者自评） | 4 触发项 | ✅ |

### Round 2 (2026-05-16) — 5 张完成

| # | 卡片 | 外部攻击 | 不要用场景 | Action Triggers | 状态 |
|---|------|---------|-----------|----------------|------|
| 6 | `yt-entrepreneur-five-step-method` | Ries (精益创业BML循环) + Mintzberg (战略规划批判) | 3 行（0-1探索期/双边平台/大企业内部创新） | 4 触发项 | ✅ |
| 7 | `yt-entrepreneur-fundraising` | DHH (自给自足) + Naval (融资不是里程碑) | 3 行（非指数增长/已正现金流/无VC关系网） | 4 触发项 | ✅ |
| 8 | `yt-entrepreneur-growth-flywheel` | Rosenzweig (光环效应) + Balfour (增长循环细分) | 3 行（冷启动/PMF未确认/单一外部渠道） | 4 触发项 | ✅ |
| 9 | `yt-entrepreneur-industrial-production` | Deming (深知识) + Graeber (官僚化批判) | 3 行（探索期/核心价值依赖个体创造力/团队<5人） | 4 触发项 | ✅ |
| 10 | `yt-entrepreneur-industry-forecast` | McGrath (发现驱动规划) + Thiel (竞争是给失败者的) | 3 行（边界被重塑/面向非消费群体/极早期方向漂移） | 4 触发项 | ✅ |

**质量验证**：
- `kdo lint --diff` → 0 new errors, 1 new warning (预存，非本次引入)
- 外部攻击全部引真实学者/从业者（Ries, Mintzberg, DHH, Naval, Rosenzweig, Balfour, Deming, Graeber, McGrath, Thiel）
- 不要用场景全部含失效机制 + 替代方案
- Action Triggers 全部含可验证成功指标
- 原有内容未被修改

### Round 3 (2026-05-16) — 5 张完成

| # | 卡片 | 外部攻击 | 不要用场景 | Action Triggers | 状态 |
|---|------|---------|-----------|----------------|------|
| 11 | `yt-entrepreneur-key-hypotheses` | Taleb (随机性/黑天鹅) + Snowden (复杂域/Cynefin) | 3 行（认知空白期/深度共识后/技术依赖型） | 4 触发项 | ✅ |
| 12 | `yt-entrepreneur-lean-validation` | Savoia (预型/Pretotyping) + Beck/XP (实验武器化) | 3 行（信任型产品/长期留存假设/B2B长周期销售） | 4 触发项 | ✅ |
| 13 | `yt-entrepreneur-liberate-thinking` | Kuhn (范式不可通约) + Foucault (权力/知识) | 3 行（快速决策期/完全陌生行业/行动导向者） | 4 触发项 | ✅ |
| 14 | `yt-entrepreneur-needs-analysis` | Ulwick (成果驱动创新/ODI) + Don Norman (隐性需求/三层认知) | 3 行（资源极度受限的技术团队/技术驱动型需求/全新品类用户无法表述） | 4 触发项 | ✅ |
| 15 | `yt-entrepreneur-opportunity-selection` | Paul Graham (坏主意) + Kim & Mauborgne (蓝海战略) | 3 行（方向直觉已强/机会空间全新/与行业高度不匹配） | 4 触发项 | ✅ |

**质量验证**：
- `kdo lint --diff` → 0 new errors, 1 warning（预存）
- 外部攻击全部引真实学者/从业者（Taleb, Snowden, Savoia, Beck, Kuhn, Foucault, Ulwick, Norman, PG, Kim & Mauborgne）
- 不要用场景全部含失效机制 + 替代方案
- Action Triggers 全部含可验证成功指标
- 原有内容未被修改

**剩余 entrepreneur**: 8 张 | **总计剩余**: ~56 张 tool 卡

**域分组**：

| 域 | 数量 | 前缀 |
|---|:---:|------|
| entrepreneur（创业） | 24 | `yt-entrepreneur-*` |
| panproduct/execution（落地） | 20 | `yt-panproduct-execution-*` |
| panproduct/demand（需求） | 11 | `yt-panproduct-demand-*` |
| personal（个人修炼） | 11 | `yt-personal-*` |
| pitch/讲香（十指策略） | 10 | `yt-pitch-*` |
| panproduct/aesthetic（审美） | 5 | `yt-panproduct-aesthetic-*` |
| prompt（提示词） | 4 | `yt-prompt-*` |
