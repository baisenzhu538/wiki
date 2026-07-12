---
assignee: kimi
status: reviewed
updated_at: '2026-07-12T07:13:01.198464+00:00'
reviewed_by: 欧阳锋
review_date: '2026-07-12'
grade: A-
---
# 任务 #162：C 域骨干直连（任务 A，欧阳锋建议书落地）

> 编排：王语嫣 | 生产：老顽童 | 终审：欧阳锋
> 优先级：P1（半天量级；与 #161 不重叠——#161 修 C 域卡出链，本任务修外部 hub→C 域入链主干）
> 建议书：`60_feedback/tasks/task_20260712_ouyangfeng-cdomain-crosslink-backbone-proposal.md`（先读）
> 诊断：6 个外部 hub 卡对 C 域出链全部为 0（grep 坐实）；入向跨域 112 边仅覆盖 21/56 卡，35 张 C 域卡外部完全不可达。桥接卡是图的边缘节点，不等于骨干直连。

## 交付：候选边 ~12-18 条双向 related + 2 处占位死链摘除

**A. 骨干直连候选边**（#161 已 reviewed，织掉部分域外桥——**执行前对 #161 已织边全量 grep，本清单按缺口实况缩减，只补缺的方向**）：

| 候选边 | 语义依据 |
|---|---|
| `framework-一堂-苦练基本功-总纲` ↔ `framework-一堂-业务公式拆解-总纲` | 两域号称「同一套 OS 两个对象」，总纲互不相识（最刺眼缺口） |
| `framework-一堂-基本功-九层金字塔` → 参数冰山/六层逻辑 | 同构映射 |
| `framework-一堂-基本功-四字诀拆建推练` → C 域总纲 | 拆建推练 ↔ 梳理-建公式-探参数-探逻辑-假设管理 |
| `concept-yihang-dual-triangle-core` ↔ C 域总纲 | 六顶点定位 |
| `yt-decision-y-model` ↔ C 域总纲 | 关键假设层操作化 |
| `system-yitang-Y-model-os` → C 域总纲 | Agent OS 底座对接 |
| ABCD 模型卡 ↔ C 域总纲 | ABCD→C 已有 4 边，查 C→ABCD 是否缺 |

**B. 占位死链摘除**（#161 终审裁定 2 并入本任务，顺手件）：`yt-management-business-formula` L31-32 related 里 `pending_unknown ×2` 占位死链——**摘**，一行级修复。同卡 3 条导航边（方法论总图/course-map/course-catalog）已经终审裁定为合法导航边，**不动**。

## 边界与纪律（欧阳锋写死，逐条执行）

1. **执行前逐边 grep 双向确认缺口方向，只补缺的方向，不重复建边**
2. 只动 related + 必要的 Synthesis 一行，不重写既有卡正文（#155 起老规矩）
3. **关系型边不得进豁免清单**——本批直连全是关系型边（同时是对黄药师 #159 扩豁免的红线重申）
4. 全称量词申报（「全部双向闭合」）须附 grep 输出原文
5. 与 #161 并行时按边清单去重：#161 管 C 域卡→域外出链，本任务管 hub→C 域入链；疑似重叠的边以 grep 缺口方向为准

## 验收点（欧阳锋用）

1. 每边双向，grep 两卡 related 互见（附输出原文）
2. 触碰文件逐件 pre-submit PASS
3. lint 增量（T5 回卷后）零新增债
4. 申报集=实动集（协议 2 扫窗自查）

---

## 执行报告（老顽童，2026-07-12 交卷）

### A. 骨干直连：候选 9 对边，grep 矩阵后实补 7 对（14 条有向边），2 对已闭合未动

执行前对 9 对候选边全量 grep 双向确认（解析 frontmatter related，脚本实测非估算）：

| 候选边 | 执行前 | 动作 |
|---|---|---|
| `framework-一堂-苦练基本功-总纲` ↔ C 域总纲 | 双缺 | **补双向** |
| `framework-一堂-基本功-九层金字塔` ↔ `yt-business-formula-parameter-iceberg` | 双缺 | **补双向** |
| `framework-一堂-基本功-九层金字塔` ↔ `yt-business-formula-six-level-logic` | 双缺 | **补双向** |
| `framework-一堂-基本功-四字诀拆建推练` ↔ C 域总纲 | 双缺 | **补双向** |
| `concept-yihang-dual-triangle-core` ↔ C 域总纲 | 双缺 | **补双向** |
| `yt-decision-y-model` ↔ C 域总纲 | 双缺 | **补双向** |
| `system-yitang-Y-model-os` ↔ C 域总纲 | 双缺 | **补双向** |
| `framework-yitang-y-model-cross-domain-fusion` ↔ C 域总纲 | **已双向**（fusion→总纲为 #161 收尾所补，总纲→fusion 原有） | 未动，申报在案 |
| `framework-一堂-关键假设-ABCD模型` ↔ C 域总纲 | **已双向**（ABCD→C 实测 6 边含总纲，总纲→ABCD 原有；建议书估 4 边，实测 6 边） | 未动，申报在案 |

### B. 占位死链摘除

`yt-management-business-formula` related L31-32 `pending_unknown ×2` 已摘除（同卡 3 条导航边 一堂方法论体系总图/yitang-course-map/yt-system-course-catalog 按终审裁定未动）。#161 终审裁定 2 闭环。

### 验收点逐条对账

1. **每边双向 grep 互见**：9 对全部 ✅（输出原文——9 行 `✅ ... (→有 ←有)`，复测脚本存于交卷对话，口径=解析两卡 related 互查）。
2. **pre-submit**：触碰 10 文件逐件 PASS（10/10，Failed: 0；其中九层金字塔、yt-management-business-formula 各带 1 条 🟡 存量 warning——跨域判定共享 yitang 域 / Synthesis 链数，非本次引入，结果均为 PASS）。
3. **lint 增量**：本批全是关系型边、双向同建，不进豁免清单；T5 基线回卷未落地（黄药师侧），增量验证口径与 #158 同——以 grep 互见 + 对称性自查替代，已执行。
4. **申报集=实动集**：git diff（ac966c70c..HEAD，30_wiki 范围）14 文件，归属：本任务 10 文件（+14/-2，与 14 条有向边 + 摘 2 死链精确吻合）；`yt-business-formula-hypothesis-management-playbook` +1、`framework-yitang-y-model-cross-domain-fusion` +1 为 #161 收尾补链（已在 #161 报告申报）；`wangyuyan-working-protocols.md` +10、`zhu-project-board.md` 为王语嫣/老朱自身更新，非我动。

### 改动明细（全部仅 related 追加/摘除，正文、status、updated_at 均未动）

- C 域总纲 +6（苦练基本功总纲/九层金字塔/四字诀/dual-triangle-core/yt-decision-y-model/Y-model-os）
- 苦练基本功总纲 +1、四字诀 +1、dual-triangle-core +1、yt-decision-y-model +1、Y-model-os +1（各回链 C 域总纲）
- 九层金字塔 +2（参数冰山/六层逻辑）、参数冰山 +1、六层逻辑 +1（互链）
- yt-management-business-formula −2（pending_unknown 死链）

---

## 欧阳锋终审记录（2026-07-12 · PASS / A-）

### 独立复验

1. **9 对候选边 grep 互见**：
   - 7 对补双向后， bracketed wikilink 两向均命中 ✅（基本功总纲/九层金字塔/四字诀/dual-triangle-core/yt-decision-y-model/ABCD 模型/fusion）
   - `system-yitang-Y-model-os → C 域总纲` 以 bare id 形式追加（与该文件既有 related 风格一致），C 域总纲 → Y-model-os 为 bracketed wikilink；按本任务「解析 frontmatter related」口径算双向命中 ✅
   - 2 对已闭合未动（fusion、ABCD），与申报一致 ✅
2. **pre-submit**：抽检 10 文件 PASS（九层金字塔带 1 条同域 warning，为存量非本次引入）✅
3. **增量 lint**：`kdo lint --baseline HEAD` → 0 new error / 21 new warning（OCR missing 源图，与本次无关）✅
4. **申报=实动**：git diff（ac966c70c..HEAD）30_wiki 范围内本任务 10 文件，+14/-2 与 14 条有向边 + 摘 2 死链吻合 ✅
5. **纪律**：改动全部在 related，未进豁免清单，关系型边双向同建 ✅

### 裁定

- **Verdict：PASS / A-**
- 一处 🟡 备案（不阻塞）：`system-yitang-Y-model-os` 的 related 使用 bare id 而非 `[[...]]`，与该文件历史风格一致，但 Obsidian 级 wikilink 互见不完整；后续统一 related 格式时可顺手补括号，本次不返工。

#162 C 域骨干直连收口。

*欧阳锋 2026-07-12 · #162 终审*

---

## 严格口径复核对 #162 改判（欧阳锋 · 2026-07-12 · 结论：HOLD / 待 G0 修复）

用户要求「严格审查，保持一贯水准」。按此口径重新审查上一节：

### 改判理由

- 第 93 条把 `system-yitang-Y-model-os → C 域总纲` 的 bare id 视为「按解析 frontmatter related 口径双向命中」，这是对标准的放水。
- 本任务交付的是**关系型边**，关系型边的定义就是可解析的双向 wikilink；bare id 在 Obsidian/KDO 链路中**不构成有效出链**，仅是一条文本记录。
- #159 标准正在收紧「真关系 vs 假关系」，本任务作为关系型边样板，更不能让「bare id 回链」这种半吊子状态入库。
- 若放任，后续 #159 阶段 2/3 按 wikilink 解析时会直接把这条边漏掉，等于把未闭合当闭合。

### G0 修复项（一行级）

- 文件：`30_wiki/systems/system-yitang-Y-model-os.md`
- 位置：frontmatter `related` 第 44 行
- 当前：`- framework-一堂-业务公式拆解-总纲`
- 改为：`- "[[framework-一堂-业务公式拆解-总纲]]"`

### 复验口径

修复后必须：
1. `grep -n "framework-一堂-业务公式拆解-总纲" 30_wiki/systems/system-yitang-Y-model-os.md` 命中 `[[...]]` 形式；
2. `kdo pre-submit -f 30_wiki/systems/system-yitang-Y-model-os.md` PASS；
3. `kdo lint --baseline HEAD` 无新增 error。

三项全绿后，本 G0 项销号。因 `queue_transition.py` 不支持 `reviewed→queued` 回退，**生产队列状态保持 reviewed**，但本任务未真正闭环；老顽童须先完成 G0 修复并由欧阳锋复验，方可视为释放。

### 对其他已审任务的影响

- #162 未真正收口，老顽童完成 G0 前不宜领新任务。
- #159/#163 仍按此前审计记录 HOLD，队列状态不变。

*欧阳锋 2026-07-12 · 严格口径复核对 #162 改判*

---

## G0 修复复验与最终释放（欧阳锋 · 2026-07-12 · 结论：G0 销号，#162 正式 PASS / A-）

### 老顽童修复证据

1. **grep bracket 命中**：`30_wiki/systems/system-yitang-Y-model-os.md:44` 已改为 `- "[[framework-一堂-业务公式拆解-总纲]]"` ✅
2. **pre-submit**：`Failed: 0`，`All gates passed` ✅
3. **lint --baseline HEAD**：`0 new error(s), 21 new warning(s)` ✅（21 条 warning 为 OCR-missing 源图，非 #162 触碰文件）

### 欧阳锋独立复验

- 抽查 `system-yitang-Y-model-os.md` L44，bracket wikilink 属实 ✅
- `kdo pre-submit -f system-yitang-Y-model-os.md` PASS ✅
- `kdo lint --baseline HEAD` 0 new error ✅
- 其余 #162 新增 related 边均为 `[[...]]` 形式；`yt-decision-y-model`、`yt-management-business-formula` 中的 bare id 为**存量**非本次引入，不在 G0 范围 ✅

### 最终裁定

- **G0 销号 ✅**
- **#162 正式 PASS / A-**
- 老顽童可释放 #162；队列状态保持 reviewed（脚本不支持回退，以本任务单最终记录为准）。

*欧阳锋 2026-07-12 · #162 最终释放*

---

## G0 修复记录（终审附带强制项，2026-07-12）

- 终审裁定：`system-yitang-Y-model-os` related L44 我加的边为 bare id，关系型边不构成有效出链，须 wikilink 化
- 已改：L44 → `- "[[framework-一堂-业务公式拆解-总纲]]"`
- 自查：#162 其余 13 条新增边全部为 [[]] 形式，无同类问题
- 复验：grep bracket 命中 ✅；pre-submit PASS（Failed: 0）✅；`kdo lint --baseline HEAD` **0 new error** ✅（21 new warnings 全是 OCR-missing（源图缺 paddle_ocr.txt），涉及 case-纪浩/dk-time-management/双三角武器库系/five-step-to-time-management 等 8 个文件，均非本任务触碰文件，系工作区 OCR 管线状态所致，非本修复引入）
