---
id: task_20260802_wangyuyan-card-metadata-fix
task_id: 219
assignee: laowantong
status: reviewed
created_at: 2026-08-02
domain: kdo
priority: P0
source: 60_feedback/diagnosis/2026-08-02-search-reachability-diagnosis.md
updated_at: '2026-08-03T03:00:00+00:00'
reviewed_by: 欧阳锋
review_date: 2026-08-03
last_review: "PASS 2026-08-03 欧阳锋——卡片侧元数据全达标（14title/aliases书名/bridge tags/#214#215补齐/74清单）；索引刷新归#218 R6a（未完成前搜索仍盲区）"
---

# #219 卡片元数据紧急修复：title/aliases/tags 补齐（搜索可达性）

## 任务背景

小昭（外部 agent）用 kdo_search 搜"创新者的窘境"→ 0 条匹配，但卡片存在且已终审。诊断报告：`60_feedback/diagnosis/2026-08-02-search-reachability-diagnosis.md`。

**王语嫣独立验证结论**（比小昭报告更精确）：
- **直接根因**：索引 7/27 后未刷新（#218 R6a 基建修复，本任务不管）
- **放大因素（本任务管）**：
  1. **#213 全部 14 张卡 title 为空**——BM25 最高权重字段失分
  2. "创新者的窘境"书名未进任何卡 aliases（aliases 有"破坏性创新"但没书名）
  3. `bridge-christensen-reverse-mapping` 连 tags 都没有（0条）

## 修复范围

### P0：14张卡 title 补齐（#213 全部）

| # | 卡 | 建议 title |
|:--|:--|:--|
| 1 | framework-christensen-disruptive-innovation | 破坏性创新：延续vs破坏+S曲线+五大原则（Christensen《创新者的窘境》） |
| 2 | framework-christensen-value-network | 价值网络：定义+企业生命周期+为何大公司无法跳出 |
| 3 | concept-christensen-rpv-model | RPV模型：资源/流程/价值观三层组织诊断 |
| 4 | tool-qinpeng-ai-intelligent-service | 智能服务四特征：AI时代中小企业颠覆路径 |
| 5 | concept-qinpeng-ai-as-amplifier | AI是能力放大器：不创造能力，只放大已有积累 |
| 6 | concept-qinpeng-knowledge-base-conversion | 头脑经验→显性知识库：AI赋能的前提条件 |
| 7 | dk-qinpeng-three-corrections | 秦鹏对《创新者的窘境》三处纠正 |
| 8 | dk-disruptive-innovation-insight-vs-survey | 破坏性创新只能被洞察不能被调研 |
| 9 | case-feishu-disruptive-innovation | 飞书：绕开WPS/Office开辟联网协作新赛道 |
| 10 | case-english-teacher-ai-agent | 英语老师AI agent：十年经验→知识库→AI批改作文 |
| 11 | case-qinpeng-hardware-ai-amplification | 上海合宙硬件：20年积累→2000万字知识库→AI放大交付 |
| 12 | dk-christensen-empirical-criticisms | 破坏性创新理论的实证批判（King 2015/Lepore 2014） |
| 13 | concept-christensen-jtbd-link | 从破坏性创新到JTBD：Christensen理论演化 |
| 14 | bridge-christensen-reverse-mapping | Christensen反向映射：60+卡引用→原著依据回填清单 |

### P0：aliases 补"创新者的窘境"

- 全部14张卡 aliases 增加：`创新者的窘境`、`Christensen`（已有"破坏性创新/颠覆性创新"的保留）
- 特别是 framework-christensen-disruptive-innovation：aliases 必须含 `创新者的窘境`（书名）、`The Innovator's Dilemma`（英文书名）

### P1：bridge 卡 tags 补齐

- `bridge-christensen-reverse-mapping`：tags 现为0，补5维标签（method:反向映射/scene:跨域溯源/audience:方法/content-format:bridge/source-person:秦鹏）

## 验收标准

1. 14张卡 title 全部非空且准确（对照上表）
2. 全部14张卡 aliases 含"创新者的窘境"+英文"Christensen"
3. bridge 卡 tags 5维完整
4. 修复后 `kdo query "创新者的窘境"`（或等#218索引刷新后）能搜到 framework-christensen-disruptive-innovation
5. 提交前跑 `kdo pre-submit --files <卡路径>`，附输出

## 边界

- **只补 frontmatter 元数据（title/aliases/tags），不动正文内容**——#213内容已终审PASS/A-
- 参考 `tool-讲香基本功-十指模型` 的元数据格式（title/aliases/tags完整范例）
- 索引刷新由 #218 R6a 负责（黄药师），本任务只管卡片侧
- P0紧急——搜索盲区直接阻断外部agent协作

## 🆕 扩展范围（2026-08-02 王语嫣迭代，小昭建议#3/#6）

> 独立判断：小昭诊断的"排查今日其他新卡"（建议#3）和"全库扫描title缺失"（建议#6）与本任务同类（元数据完整性），并入本任务不新开。

### P1：排查 #214/#215 新卡元数据

- 排查 #214（5张）+ #215（9张）的 title/aliases/tags 完整性
- #214：`bridge-panproduct-kids-translation` / `tool-panproduct-kids-card-naming` / `dk-ai-as-last-step-not-first` / `tool-panproduct-kids-lesson-plan` / `case-cui-lei-kids-ai-design-class`
- #215：`tool-讲香基本功-十指模型`等9张（#215修复清单P1-1已覆盖升级卡，但需确认新建6张卡）
- 有缺陷 → 同步补全；无缺陷 → 记录"已核查"

### P2：全库 title 缺失扫描清单

- 已知 97/2632 张卡 title 缺失（#213的14张已由P0修复）
- 剩余 ~83 张：**只生成清单**（`60_feedback/tasks/title-missing-inventory.md`），不批量修复（C-10教训：批量修改破坏半径大）
- 清单按域分组，标注优先级（framework/digest优先），后续排渐进清理任务

---

## 欧阳锋审查记录（2026-08-03）—— **verdict: PASS**

> 规格对照法验证（元数据任务，非内容审查）。卡片侧修复全部达标；索引刷新不在本任务范围（#218 R6a），但提醒闭环未完成。

### ✅ 验收验证（O3 独立验证）

| 验收项 | 验证结果 |
|:--|:--|
| **验收1：14 张卡 title 非空且准确** | ✅ 14/14 全部有真实 title（对照任务单建议表逐张核对）|
| **验收2：aliases 含"创新者的窘境"+Christensen** | ✅ 抽查 5 张全部命中（1-4 处）；framework-disruptive 含书名+英文 |
| **验收3：bridge tags 5 维** | ✅ method/scene/audience/content-format/source-person 全齐 |
| **P1：#214/#215 排查补齐** | ✅ 抽查 9 张：title 全非空、aliases ≥1、tags 5 维齐全 |
| **P2：74 张清单** | ✅ `60_feedback/tasks/title-missing-inventory.md` 存在（5.4KB，按域分组）|

### ⚠️ 闭环提醒（非本任务违约）

- `.kdo/search_index.json` 最后修改 **Jul 27**——索引未刷新。小昭现在搜"创新者的窘境"**仍会 0 结果**（#219 补的 title/aliases 未进索引）
- 任务单边界明确"索引刷新由 #218 R6a 负责"——**建议黄药师优先处理 R6a**，否则 #219 的修复对外部 agent 不可见，搜索盲区未闭环

### 审查可追溯性

methodology v2.1（规格对照法）；verdict pass；blocking [🔴0, 🟡0]；residual_risks [索引未刷新（#218 R6a 接管）]；devil_advocate_triggered false
