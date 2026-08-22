---
id: 431
assignee: hermes
status: reviewed
updated_at: '2026-08-22T17:26:21.666367+00:00'
reviewed_by: 欧阳锋
review_date: '2026-08-22'
grade: A-
---
# #431 角色专场第一场：老顽童岗位说明书定稿

- **任务号**：#431
- **状态**：queued
- **assignee**：laowantong（生产/起草；编排=王语嫣；终审=欧阳锋；终稿=老朱）
- **优先级**：P1（F-028 角色专场开场；一角色一张过，不六角色齐跑）
- **立项**：2026-08-23 王语嫣（老朱点名开场；顺序：老顽童→欧阳锋→黄药师→风清扬→王语嫣→老朱）

## 任务目标

产出老顽童岗位说明书定稿稿，作为《KDO 基本法》角色章 v1.0 的第一块。不是泛职责表，是五要素可执行卡：内核/职责/边界/工作流/Trigger+Interface。

## 必读底本（先读再写）

- `60_feedback/diagnosis/diag_20260822_fengqingyang-5role-spec-workflow.md`（角色专场过卡底本）
- `90_control/kdo-charter-v0.1-draft.md` §2.1/§2.2/§2.4/§3.13（入宪口径）
- `60_feedback/consultation/2026-08-22-kdo-systemic-upgrade/positions/ouyangfeng.md` B2-3 两条血泪：批次验收≠整单终审；审查者不直接编排
- `60_feedback/consultation/2026-08-22-kdo-systemic-upgrade/positions/laowantong.md` B2-3 两条：领取前置=精做笔记落盘；claimed→pending_review 加 in_progress 中间态
- 现有 `30_wiki/agent-specs/agent-spec-laowantong-producer.md`（只升级，不推倒重写）

## 动作

1. 用五要素模板重写/升级老顽童 spec：内核、职责、边界、工作流、Trigger+Interface。
2. 必写两条通用铁律：G1 每日自进化；G2 洞察第一时间上浮王语嫣。
3. 必写老顽童专属门禁：领取前置=精做笔记/素材消费率≥80%；产卡状态细分含 in_progress；批次验收≠整单终审；审查者不直接编排。
4. `kdo pre-submit -f` 过；相关回链只增不改；commit 入档。

## 验收

- 五要素齐全；Trigger+Interface 不再是缺口；与 charter §2.1 不冲突。
- 欧阳锋终审抽：是否真含 B2-3 两条血泪 + 老顽童两条补充。
- 老朱终稿拍板后，才开下一场（欧阳锋）。

## 边界

- 只定老顽童这一场；其余角色不得提前拆单。
- 不改《KDO 基本法》正文；定稿稿经老朱拍板后才由王语嫣并入角色章。

---

## 终审记录（欧阳锋 · 2026-08-23 凌晨）

**结论：PASS / A-**

**对齐核验**：commit e52627bf8（01:23 spec v1.0）在 HEAD；审查对象=最新真相源。

**O0 逐条溯源**：
1. **五要素齐全** ✅：内核（L60）/职责（L66）/边界（L74）/工作流（L82）/Trigger+Interface（L92）+基线用例 4 条
2. **B2-3 欧阳锋两条血泪** ✅：批次验收≠整单终审（L89 工作流 6，禁走 review 脚本语义明确）/审查者不直接编排（L79，报告王语嫣裁定不自行立项）
3. **老顽童两条补充** ✅：领取前置=精做笔记落盘（L84，素材消费率≥80% 是领取门禁非写卡时的事）/claimed→in_progress 中间态（L72，缺中间态队列行不动误判卡死）——与 positions/laowantong.md L9 原文逐条吻合
4. **G1/G2 两铁律** ✅（L99-102，与 #428 风清扬 spec 同款文案）
5. **与 charter §2.1/§2.5 不冲突** ✅：多实例+队列约束（L58/L64，charter §2.5 实例策略实存 L65）
6. **只升级不推倒** ✅：created_at 08-19 保留 + updated_at 08-23；KF-024 结构门禁（dk 七段/framework Synthesis+Action Triggers/case 四段）已写入 L68——今日 #189 教训即时吸收
7. **source_refs 6 条全存在** ✅（charter/建议书/positions×2/context/amnesia）；pre-submit 独立复现 PASS（0 errors）

**发现问题**：
- 🟠 **aliases 路径污染（与 #428 同族）**：12 条 aliases 中 8 条为文件名/路径（kdo-charter-v0.1-draft.md/consultation/positions/ouyangfeng.md/laowantong-context.md/20_memory 等）——检索噪声，`positions`/`consultation` 命中本卡。**#428 已记 TODO 现在又现——升级为批量清理**：建议王语嫣立 aliases 规范清理批（同族一次清完，不做逐卡 TODO）

**魔鬼代言人**：3 个月后最可能出问题——aliases 路径词造成检索污染（查"positions"命中生产者卡）；或 B2-3 角色专场后续场次（欧阳锋/黄药师/王语嫣）口径与本卡漂移（专场顺序推进时需互相参照）。

**存在性核查**（本意见书负向断言证据）：
- 「charter §2.5 实存非死引用」→ 核查：grep `^### 2\.` charter 文件——2.1~2.6 连续存在（2.5 实例策略 L65）
- 「positions/laowantong.md 底本吻合」→ 核查：grep "精做笔记\|in_progress" positions 文件——L9 原文逐条对照一致
- 「pre-submit 0 errors」→ 核查：kdo pre-submit -f 独立复现 PASS 输出

**残余风险**：aliases 批量清理待王语嫣立项；角色专场下一场（欧阳锋）待老朱拍板本场后开。

*欧阳锋 · 2026-08-23 · A-*
