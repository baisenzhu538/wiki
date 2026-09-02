---
id: task_20260902_huangyaoshi-graph-index-rebuild-sentinel

title: graph_index 归零重建 + 健康哨兵机制化（08-31 整树事故清空后语义腿空转 2 天无人发现）

seq: 622

status: in_progress
assignee: huangyaoshi

created_by: wangyuyan

created_at: 2026-09-02

decision_source: 外部审计建议书 diag_20260902_external-audit-graph-index-empty-recur（P1）+ 王语嫣 09-02 裁定（存在性核查：.kdo/graph_index 0 字节，mtime 08-31 02:11 正落在整树事故窗口）

reviewer: 欧阳锋
instance: huangyaoshi-kimi
updated_at: '2026-09-02T16:19:04.058073+00:00'
evidence: _tmp/622-graph-rebuild.log
rework: true
---

# #622 graph_index 重建 + 哨兵（黄药师，P1）

## 背景（已核实）

- `.kdo/graph_index/` = 0 字节空目录，mtime 08-31 02:11——正落在整树事故窗口（02:00-02:09），清空根因大概率=事故本身（无任务记录因为不是任务干的）
- #358（08-19 PASS A）曾重建至 2349 页/5080 chunks，事故后归零，**hybrid RRF 语义腿空转 2 天**全厂静默降级（口语化检索实测全跑偏，关键词检索 BM25 兜底正常）
- 引擎层 #358 已修好不用动，本单=重建数据 + 补哨兵

## 任务

1. **重建**：按 #358 已验证流程全量重建 graph_index（先删后建，30-60min，挂后台低峰跑），重建后实测口语化查询（「我卖护肤品的，怎么让犹豫的客户快点下单」应命中转化率案例卡）
2. **哨兵机制化（本单关键增量）**：graph_index 空目录 / 0 records / 陈旧超 48h → 探针面显式告警（复用既有探针/门禁通道，不新建扫描器）——「修完没加哨兵=同类事故必再发」是 #357/#358 两轮打过的模式，这次闭环
3. 根因注记落执行报告：08-31 02:11 事故窗口归因的证据链（目录 mtime vs 事故时间线）

## 红线

- 重建挂后台，不占前台；先删后建流程按 #358 来
- 哨兵只告警不动作

## 交付

- 重建产物记录（页数/chunks 数）+ 口语化查询前后对照 + 哨兵上线实证 + 执行报告
- claim/complete 走 `python 90_control/scripts/queue_transition.py`（complete 622）

## 执行报告（2026-09-02 黄药师）

**交付物**：① `.kdo/graph_index/` 全量重建产物（graphml 6.5MB + vdb_entities/relationships/chunks + kv_store，共 ~79MB）② conveyor_probe.py 第十一信号 `_scan_graph_index_health`（kdo-tools/conveyor_probe.py，挂第九信号 infra_alerts 同通道）③ 回归测试 4 条（kdo-tools/tests/test_conveyor_probe.py）④ notification-coverage-matrix.md 行 27 同步登记（§3.19）⑤ 重建日志 `_tmp/622-graph-rebuild.log`

**完成内容**：① 重建——先删后建按 #358 流程：claim 前实测口语化查询确认 0 chunks/0 entities（空转实证），`rm -rf .kdo/graph_index` 后 `kdo graph rebuild --full` 挂后台跑完：**2428 页 / 5267 chunks / 6705 relations**（对比 #358 重建时 2349 页/5080 chunks，增量来自期间新卡）② 哨兵机制化——三档检测：空目录/缺失 → 报；graphml `<node` 字节扫描 0 节点 → 报 0 records；graphml mtime 落后 search_index.json 超 48h → 报陈旧（陈旧取 #356 双索引同步相对口径，规避手动重建节奏下绝对 48h 的常态误报——search_index 随卡片写入增量更新，是基准钟；search_index 读不出则跳过陈旧项）。沿触发幂等、恢复重新武装、原因切换重报、只告警不动作 ③ 根因注记——`.kdo/graph_index` 清空态 mtime/birth = 2026-08-31 02:11:44（stat 实证，claim 前取样），落 08-31 整树事故窗口（02:00-02:09）尾段 2 分钟内，无任何任务单/工单记录指向该目录操作，归因=事故连带清空（与王语嫣存在性核查一致）

**验证**：① 前后对照——重建前 `kdo graph query "我卖护肤品的，怎么让犹豫的客户快点下单"` = Found: 0 chunks/0 entities/0 relations（空转）；重建后同查询命中转化率域案例卡（优秀触点案例合集、棋牌室新客办卡率1%→5% 等 12 条实体），语义腿复明 ② 哨兵单测 4 条全过（空目录告警+幂等 / 0 records / 陈旧 50h 告警+10h 不告 / 恢复重新武装重报），探针全量回归 47 passed ③ 真机 dry-run：`conveyor_probe.py --dry-run --json` 健康态无告警、state 键 `graph_index_issue=None`（武装态）正常落位 ④ 健康函数对真实 ROOT 调用返回 [] 且状态键正确

**边界**：哨兵只告警不动作（本单红线）；哨兵挂探针 10 分钟拍，非实时；陈旧判定依赖 search_index.json 存在且增量更新正常（该文件自身停更是另一信号面，不在本单）；claim 走 --force 留痕（#621 挂审期间并行，台账 force-exceptions.log 可查）

**需要谁动作**：欧阳锋终审（重点核：哨兵陈旧口径取相对 search_index 而非绝对 mtime 的判断是否认可；matrix 行 27 登记口径）。无需老朱/王语嫣动作

## 返工记录（2026-09-03 黄药师 · 终审 FAIL 收口）

**P0 入仓实证**：终审 FAIL 时点 HEAD=6d22f0f92 确未含本单代码（终审证据成立）；随后老顽童 push 修复提交 `20ac959eb`（2026-09-02 23:44）将工作区四件交付全部扫入仓——`kdo-tools/conveyor_probe.py`（+40）、`kdo-tools/tests/test_conveyor_probe.py`（+68）、`90_control/notification-coverage-matrix.md`（行 27）、`90_control/scripts/.derived-hashes.json`（见该 commit --stat）。本轮回复核实证：`git show HEAD:kdo-tools/conveyor_probe.py | grep -c _scan_graph_index_health` = 2（HEAD 含第十一信号）；HEAD 版测试文件 graph_index 相关断言 25 处；HEAD 版 matrix 行 27 在位（`git show HEAD:90_control/notification-coverage-matrix.md` grep 命中）；`git diff HEAD` 对四件均为空（工作区=HEAD，无残留未提交变更）。「未入仓=不存在」FAIL 点已消除。

**存在性核查**（补 P1：负向判词「无任何任务单/工单记录指向该目录清空操作」的核查节）：检索面 = `grep -rli graph_index 60_feedback/tasks/ 70_product/tasks/`，命中 11 个文件，逐一核查清空/删除指向——仅 2 处相关：① `60_feedback/tasks/task_20260818_huangyaoshi-graph-embedding-pipeline.md`（#358，08-18）载「`--full` 前先删 graph_index」——属**重建标准流程**的先删后建步骤，时间 08-18，与 08-31 02:11 清空窗口无关；② 本任务单（#622）自身 09-02 重建时的 `rm -rf`——发生在发现空目录**之后**，是修复动作而非清空原因。其余 9 个命中文件均为提及（队列行 / dashboard / 本单上下文），无清空或删除指向。结论：无任何任务单/工单记录指向 08-31 02:11 对 `.kdo/graph_index` 的清空操作，负向判词成立，归因维持 = 整树事故连带清空。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ①-补 划痕路径提示

- ⚠️ 交付物节含划痕路径 `_tmp/622-graph-rebuild.log`（中间产物非交付物，按约定豁免三态检查；如属误写请清理交付物节）
### ① 声称-交付差集

⚪ 无路径级交付物声明（纯文档/诊断类或未用反引号标注路径）——差集无检查面
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（缺失/「无任何任务单/工单记录」）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）

## 终审记录（2026-09-02 欧阳锋 · FAIL · methodology v2.3）

**Verdict**：FAIL（退回收口）——#362 版本对齐门禁第一问「入仓了吗」= 否，不予通过。

### P0/P1/P2 清单

- 🔴 P0：**交付核心变更全部未入仓**。`kdo-tools/conveyor_probe.py`（+40）、`kdo-tools/tests/test_conveyor_probe.py`（+68）、`90_control/notification-coverage-matrix.md`（行 27 登记）、`90_control/scripts/.derived-hashes.json` 均停留在 git 工作区未提交。未提交=不存在（#362/#357 08-18 教训）：工作区代码可被 vault backup 回滚或清理操作静默带走，「哨兵已上线」结论不成立。
- 🟡 P1：执行报告根因注记含负向判词「无任何任务单/工单记录指向该目录操作」但无 `**存在性核查**` 锚点（#433：「我没看到」≠「不存在」；机器预审 🔴 已同判提示）。我独立 grep `60_feedback/tasks/` + `70_product/tasks/`（graph_index 清空/删除指向）确认判词本身成立——是形式缺口，非事实错误。
- P2：无。

### 字段级定位

- P0：任务单「交付物」②④（L49）对应文件在 `git status` 中均为 M 未提交态。
- P1：执行报告「完成内容」③ 根因注记段（L51）。

### 证据

- `git show HEAD:kdo-tools/conveyor_probe.py | grep -c _scan_graph_index_health` = 0（HEAD=6d22f0f92，23:38 编排提交，不含本单代码；23:36 的 claim/complete 两个 chore 提交仅动队列台账）。
- 任务单全文 grep `存在性核查` 仅命中 decision_source 引用王语嫣对「0 字节态」的核查，未覆盖「无工单记录」这一新负向判词。

### 期望形态

1. 将本单全部交付变更（代码 + 测试 + matrix + 派生哈希）提交为独立 commit，然后重走 complete → 提审。
2. 执行报告根因注记段补「存在性核查」小节：声明检索面（如 `grep -rl graph_index 60_feedback/tasks 70_product/tasks`，逐命中文件确认无清空/删除指向）+ 结论。

### 已独立复跑确认成立项（重报时引用本节即可，无需重复证明）

- **重建产物实测**：graphml 3620 nodes / 6694 edges（字节计数复核），与日志「2428 页 / 5267 chunks / 6705 relations」一致；`.kdo/graph_index/` 82MB 五件齐全。
- **口语化查询复明**：`kdo graph query "我卖护肤品的，怎么让犹豫的客户快点下单"` mix 模式 Found 5 chunks / 24 entities / 61 relations，命中内容经营六步闭环等转化相关卡——语义腿复明确认（重建前 0 chunks 空转态以任务单记录为据）。
- **哨兵实证**：`pytest tests/test_conveyor_probe.py` 47 passed（含新增 4 条：空目录告警+幂等 / 0 records / 陈旧 50h 告 10h 不告 / 恢复重新武装）；`--dry-run --json` 健康态无告警；`.kdo/conveyor_state.json` 键 `graph_index_issue: null`（武装态）落位。
- **陈旧相对口径认可**：回答任务单「需要谁动作」之问——graphml mtime 落后 search_index.json >48h 的相对基准钟口径，规避手动重建节奏下绝对 48h 常态误报，判断合理，认可。
- matrix 行 27 登记内容（工作区版）与实际信号行为一致，登记口径无问题。

**blocking**：P0（未入仓）。**residual_risks**：修复仅一步 commit + 补核查节，预计分钟级收口。

