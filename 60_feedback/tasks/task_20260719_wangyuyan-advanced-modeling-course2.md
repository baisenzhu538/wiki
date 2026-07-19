---
id: task_20260719_wangyuyan-advanced-modeling-course2
title: 高阶建模第二课卡片化（修订版）——流程建模实践：18组件·关系探索·三案例
type: task
status: in_progress
priority: P1
assignee: hermes
reviewer: 欧阳锋
created_at: 2026-07-19
updated_at: '2026-07-19T16:45:20.742797+00:00'
expected_cards: 4（新卡）+ 6（已有卡enrich）+ 2（暗知识卡）+ 3（Phase 2解压资产）
source_refs:
- 60_feedback/diagnosis/diag_20260719_wangyuyan-advanced-modeling-course2.md
- 60_feedback/diagnosis/diag_20260719_advanced-modeling-process-modeling.md
- 00_inbox/Advanced modeling/（57张VLM+OCR全量）
- 00_inbox/Advanced modeling/洪七公-给王语嫣的任务编排建议-高阶建模流程建模.md
related:
- modeling-three-stages
- modeling-level-map
- modeling-weapon-library
- process-modeling
- modeling-capability-system
- framework-kdo-modeling-methodology
- concept-kdo-component-library
- framework-TCPR皇冠模型
- yt-decision-y-model
---

# 高阶建模第二课卡片化（修订版）——流程建模实践

> **来源**：王语嫣两份诊断报告
>   - `diag_20260719_wangyuyan-advanced-modeling-course2.md`（初版）
>   - `diag_20260719_advanced-modeling-process-modeling.md`（独立复核修订版）
> **素材**：一堂 Truman《高阶建模实践1 — 流程建模》4096行口述 + 57张VLM/OCR
> **域归属**：高阶建模域（modeling domain）——第一课已入库，本课为实践层补充
> **修订说明**：本任务单于 2026-07-19 根据独立诊断复核结果修订。取消与同日新建卡重复的新建项，改为enrich已有卡；新增Truman原18组件源框架卡。

---

## 一、域结构理解（生产前必读）

```
高阶建模域（modeling domain）
├── 理论层（第一课·已入库）
│   ├── modeling-three-stages          # 三段论
│   ├── modeling-level-map             # 段位图 L1-L6（本课enrich）
│   ├── modeling-weapon-library        # 武器库
│   ├── process-modeling               # 流程建模SOP（本课enrich）
│   └── modeling-capability-system     # 总纲
│
├── 方法论层（本课·关键增量）★
│   ├── framework-kdo-modeling-methodology  # Truman四步法→KDO映射（已存在，本课enrich）
│   ├── concept-truman-18-component-cards   # Truman原18组件源框架（新建P0）
│   ├── concept-kdo-component-library       # KDO17组件改编版（已存在，本课enrich）
│   └── framework-modeling-relation-exploration  # 拆解×完备×依赖关系（新建P0）
│
├── 案例层（本课·新建）
│   ├── case-modeling-ai-image-workflow     # AI文生图流程演进
│   ├── case-modeling-gongjianhui-facilitation # 共建会/攻坚会流程设计
│   └── case-modeling-TCPR-evolution        # TCPR建模过程（反向enrich TCPR皇冠模型）
│
└── 暗知识层（跨课）
    ├── dk-process-is-scar-tissue           # 流程是业务的疤痕
    ├── dk-modeling-jump-step-cost          # 跳步代价
    └── dk-ai-makes-you-stronger-or-lazier  # AI双面性（P2可暂缓）
```

### 解压路径（Phase 2·本课后启动）

> **欧阳锋铁律**：1 framework 应配套 ≥3 解压资产。

| # | 解压资产 | 类型 | 说明 |
|:--|:---|:---|:---|
| D1 | `skill-modeling-domain-iteration` | skill | 建模域专用工作流：诊断→生产→验证→复盘→迭代 |
| D2 | `tool-kdo-modeling-checklist` | tool | KDO Agent建模自检清单，引用18组件/17组件 |
| D3 | `agent-spec-modeling-coach` | agent-spec | 建模教练Agent——引导用户走完四步法+匹配组件卡牌 |

> **生产时序**：Phase 1（4新卡+6enrich+2dk）→ 老顽童提交 → 欧阳锋终审 → Phase 2（D1/D2/D3解压）

---

## 二、生产清单

### 2.1 新建卡片（4张P0/P1）

| # | 卡ID | 类型 | 优先级 | 核心内容 | 主要来源 |
|:--|:---|:---|:---|:---|:---|
| 1 | `concept-truman-18-component-cards` | concept | **P0** | Truman原18组件：五维度（事实/目标/方案/过程/协作）×18张牌，每张=「先X后Y」依赖对+适用信号+反例+来源案例；与KDO17组件明确区分 | 口述L2934-L3010，批注2026-07-19-204445 VLM |
| 2 | `framework-modeling-relation-exploration` | framework | **P0** | 拆解×完备×依赖关系：五类关系分类+规律筛选五标准+几何形态与逻辑形态匹配+典型跳步错误 | 口述L1916-L1970，批注2026-07-19-204145 VLM |
| 3 | `case-modeling-ai-image-workflow` | case | P1 | v1抽卡→v2讨论→v3五张→v4四要素→v5攻坚会最终版；8里程碑；九张翻牌子机制；内容→风格→精准度顺序 | 口述§3.1，批注2026-07-19-203816 VLM |
| 4 | `case-modeling-gongjianhui-facilitation` | case | P1 | 共建会/攻坚会8-9步流程：对齐目标→对齐出口→背景热身→多轮加法→交换想法→分类建模→逐项论证→硬伤检查→现场分工；成功率30-50%→80-100% | 口述§3.2，攻坚会的流程VLM+OCR |

### 2.2 已有卡 enrich（6张）

| # | 目标卡 | 补充内容 | 来源 |
|:--|:---|:---|:---|
| 5 | `modeling-level-map` | 新增§时间维度：见识提升（天单位）/实操提升（月单位）/迁移创新（年单位）；补充L1-L6「能练什么」细节 | 批注2026-07-19-202929，口述L50-L70 |
| 6 | `framework-kdo-modeling-methodology` | 新增§Step2展开：关系vs规律、五类关系、几何形态匹配、典型跳步错误；新增失败模式：压缩过度/不解压 | 口述L1916-L1970, L2103-L2188 |
| 7 | `concept-kdo-component-library` | 新增§与Truman 18组件对照：维度映射、组件对应、改编rationale、KDO新增/省略的牌 | 口述L2934-L3010 |
| 8 | `framework-TCPR皇冠模型` | 新增§建模过程：1.0三分法→2.0 TCP→3.0加R→4.0皇冠图→5.0训练清单；修正R与TCP关系为「映射/影子/兼容」，非单纯底座 | 口述§3.3 |
| 9 | `process-modeling` | 新增§组件思维应用：如何用18组件拼装SOP；新增「流程是业务的疤痕」引用 | 口述L2618-L2706 |
| 10 | `dk-modeling-logical-cleanliness-root` 或 `framework-logic-cleanliness-five-levels` | 新增§逻辑洁癖与四步法Step2「探索关系」的联动：审美驱动如何发现关系和规律 | 口述L54-L58, L1702-L1722 |

> **注**：第10项由老顽童根据已有卡结构二选一，优先 `dk-modeling-logical-cleanliness-root`。

### 2.3 TCPR案例处理（不单独建卡，并入enrich）

`case-TCPR四角色建模演进` **不单独成卡**。其内容（1.0三分法→5.0训练清单）并入 `framework-TCPR皇冠模型` 的「建模过程」章节，避免与定义卡分裂。

### 2.4 暗知识卡（2张P1 + 1张P2）

| # | 卡ID | 类型 | 优先级 | 核心内容 | 来源 |
|:--|:---|:---|:---|:---|:---|
| 11 | `dk-process-is-scar-tissue` | dk | P1 | 金句级暗知识：流程节点来自流血后的痂；组件是疤痕的最小单位 | 口述L2617-L2624 |
| 12 | `dk-modeling-jump-step-cost` | dk | P1 | 依赖关系不可逆：跳步=前置输入为空；「埋的雷在后半段十倍百倍惩罚」 | 口述L2718-L2728, L2378-L2384 |
| 13 | `dk-ai-makes-you-stronger-or-lazier` | dk | P2 | AI双面性：先练人类三角，否则判断不了AI产出好坏 | 口述L3760-L3868 |

> P2暗知识卡可延后，不阻塞Phase 1验收。

---

## 三、关键规则

### 3.1 与已有卡的关系声明

- `concept-truman-18-component-cards` 必须注明：「本卡是Truman原18组件源框架；KDO域内改编版见 `concept-kdo-component-library`」。
- `framework-kdo-modeling-methodology` enrich 后必须注明：「Truman四步法原始操作定义见 `framework-modeling-relation-exploration`；KDO映射版见本卡」。
- `framework-TCPR皇冠模型` enrich 后必须修正：R不是C的MECE子集，而是TCP的映射/影子/兼容底座。

### 3.2 术语规范

- 「组件」≠「流程」：组件是最小可复用依赖单元，流程是组件的排列顺序。
- 18张牌命名统一为「X优先」格式（如「客观优先」「输入优先」）。
- 「触贯」：一堂专用术语（触类旁通+融会贯通），首次出现需注释。
- 「逻辑洁癖」：核心驱动概念，不可省略。

### 3.3 链接规则

- 每张新卡 related ≥ 5 条，至少 1 条链接到第一课已有卡。
- `concept-truman-18-component-cards` 必须双向链接 `concept-kdo-component-library`。
- `framework-modeling-relation-exploration` 必须双向链接 `framework-kdo-modeling-methodology`。
- `case-modeling-ai-image-workflow` / `case-modeling-gongjianhui-facilitation` 必须链接 `concept-truman-18-component-cards` 和 `framework-modeling-relation-exploration`。

### 3.4 enrich卡规范

- 所有enrich内容必须标注 source_refs 到口述稿原始行号。
- 不得在已有卡中删除原有内容，只能新增section或补充related。
- 若enrich导致卡片过长（>400行），应拆分新增子卡，而非无限追加。

---

## 四、生产顺序建议

| 阶段 | 卡片 | 理由 |
|:---|:---|:---|
| **Phase 1.1** | `concept-truman-18-component-cards` + `framework-modeling-relation-exploration` | 方法论核心，为案例卡提供上游连接 |
| **Phase 1.2** | `case-modeling-ai-image-workflow` + `case-modeling-gongjianhui-facilitation` | 案例卡依赖方法论卡 |
| **Phase 1.3** | 6张已有卡enrich | 确保跨域链接完整 |
| **Phase 1.4** | `dk-process-is-scar-tissue` + `dk-modeling-jump-step-cost` | 暗知识卡可在案例卡完成后提炼 |
| **Phase 2** | D1/D2/D3解压资产 | 等Phase 1终审通过后启动 |

---

## 五、验收标准

- [ ] 4张新卡通过 `kdo pre-submit`
- [ ] 6张enrich卡 `kdo lint` 无新增ERROR
- [ ] 2张P1暗知识卡通过 `kdo pre-submit`
- [ ] 每张新卡 related ≥ 5 条，含 ≥1 条链接到第一课已有卡
- [ ] `concept-truman-18-component-cards` 与 `concept-kdo-component-library` 有明确对照说明
- [ ] `framework-TCPR皇冠模型` 修正R与TCP关系描述，并补充建模过程章节
- [ ] 所有enrich内容标注口述稿行号
- [ ] 欧阳锋抽检 ≥2 张新卡 + 2 项已有卡enrich

---

## 六、欧阳锋抽检重点

1. `concept-truman-18-component-cards`：18张牌是否每张都有「先X后Y+适用信号+反例」？与KDO17组件的对照是否清晰？
2. `framework-modeling-relation-exploration`：Step2是否足够重？是否呈现了「关系vs规律」和「几何形态匹配」？
3. `framework-TCPR皇冠模型` enrich：R的角色描述是否从「底座」修正为「映射/影子」？建模过程章节是否标注了source行号？
4. `concept-kdo-component-library` enrich：是否解释了为什么把Truman的「事实/目标/方案/过程/协作」改编为「素材/边界/结构/过程/质量」？

---

## 七、队列位置

- **入队编号**：#194（保持原编号）
- **状态**：`queued` → 待老顽童领取
- **阻塞/依赖**：无
- **预计工期**：2个老顽童实例周期（4新卡+6enrich+2dk）

---

*王语嫣 · 2026-07-19 · 基于独立诊断复核修订*
*修订依据：diag_20260719_advanced-modeling-process-modeling.md*
