---
id: task_20260906_huangyaoshi-graph-index-stall-rootfix
title: "graph_index 停拍根因+重建+哨兵复查（infra-liveness 六拍连续增长实证，#622 复发）"
seq: 648
status: reviewed
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-06
decision_source: 王语嫣值守拍立项（infra-liveness 09-04 23:47→09-05 04:17 六拍 48h→53h 连续增长，真实故障非回声）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-05T18:59:47.663938+00:00'
reviewed_by: 欧阳锋
review_date: '2026-09-05'
grade: A-
---

# #648 graph_index 停拍根因+重建+哨兵复查（黄药师）

## 背景
infra-liveness 报警（conveyor_probe）：graph_index 陈旧（落后 search_index）从 09-04 23:47 起六拍连续增长 48h→49h→50h→51h→52h→53h。此前五拍被值守划销为「回声」（09-06 王语嫣复核：误判——回声是同一事件重复登记，这是持续恶化的单一故障）。#622 曾做 graph_index 重建+哨兵，本次为复发或哨兵未覆盖此面。

## 任务
1. **根因**：graph_index 生成/刷新链路为何停摆 53h+（计划任务没跑？跑了失败？哨兵为何没自愈没升级？）——结论落执行报告，附证据（日志/时间戳）。
2. **重建**：graph_index 重建至最新（落后 search_index 回落到阈值内）。
3. **哨兵复查**：#622 哨兵为何没拦住本次停摆；修复为「停拍超阈值→自动重建或升级报警」二选一，想犯错也犯不了。

## 验证
- 重建后 infra-liveness 下一拍不再报 graph-index 陈旧（或时差回落 <阈值）。
- 哨兵回归：模拟停拍场景验证自动重建/升级路径。

## 交付
- 根因结论+重建 diff/日志+哨兵修复+回归证据+执行报告（F-034 五字段全）。
- claim/complete 走 `queue_transition.py`（claim 648 / complete 648）。

## 边界
- 依赖 #646 终审后开工（同角色排队，不并行施工）；根因若指向 #622 交付缺陷，如实记入（不甩锅不隐匿）。

## 执行报告

**交付物**：
- `kdo-tools/conveyor_probe.py`（哨兵 `_scan_graph_index_health` 陈旧分支改造：超阈值先自愈 `_graph_index_selfheal`（增量重建）失败才报警；成功判据=graphml mtime 前跳；6h 最小重试间隔防乒乓；自愈台账 `logs/graph-selfheal.log`）
- `kdo-tools/tests/test_conveyor_probe.py`（自愈回归 4 条新增 + 陈旧用例改造，共 53 passed）
- `.kdo/graph_index/` 重建产物（增量 24 页/68 chunks/19 relations，02:08 落盘）

**完成内容**：①根因三层——(L1 设计层)`kdo graph rebuild` 从无自动刷新载体：schtasks 全量核查无 graph 任务，toolkit/decisions 明文「内容变更后手动跑」，#622 09-02 23:29 手动重建后无人再跑，停摆=结构性必然，不存在「计划任务没跑/跑了失败」（根本没有任务可失败）；(L2 阈值层)#622 定 48h 相对阈值时假设的重建节奏未制度化，阈值 < 实际手动间隔（#358 08-18→#622 09-02 = 15 天），09-04 23:29 触线与首报 09-04 23:37 精确吻合；(L3 响应层)lag 每小时 +1 使幂等失效（issue 串逐拍变化→每拍重报），告警长得像回声→值守五拍误划销，09-06 复核才立项；哨兵按 #622 红线只告警不动作，无自愈无升级。#622 交付本身无缺陷（哨兵按设计正常工作），缺陷在「重建节奏无制度化载体+告警只走台账无行动出口」。②重建——`kdo graph rebuild`（增量默认）14 秒完成，lag 73.9h→-0.78h（graphml 反超 search_index），Entities 2428→增量更新。③哨兵修复（二选一取「自动重建」）——陈旧超阈值分支自动跑增量重建（真机实测 14s，#622 式 `--full` 重操作永不自动触发）；真机二轮模拟揪出「rc=0 但 mtime 未前跳」假成功（内容无变化时增量返回 No changes 也算成功），改为 mtime 前跳为成功判据，未前跳转 FAIL 升级人工；失败路径含原因可读报警；6h 防乒乓不空转重建。

**验证**：`python -m pytest kdo-tools/tests/ 90_control/scripts/tests/ -q` → **517 passed**（探针 53：#622 原有断言不红 + 自愈 4 条：成功无告警/失败升级含原因/6h 内不重试防乒乓/健康态零调用）；真机模拟两轮——第一轮（mtime 拨回 50h）自愈触发并落台账 `logs/graph-selfheal.log`，暴露假成功缺陷；第二轮（同状态+修复后）正确判 FAIL 并产出升级告警「自动增量重建失败: rc=0 但 graphml 未前跳——需人工判断」；收尾真机复核：lag -0.89h、`_scan_graph_index_health({})` 返回 `[]`（下一拍 infra-liveness 不再报 graph-index 陈旧）。

**边界**：空目录/0 records/graphml 缺失分支维持 #622 只告警不动作（本单只修「停拍超阈值」面——任务书原文口径）；lag 的度量语义仍是 mtime 差而非内容差（search_index.json 周期性重写即使无内容变更也推大 lag——增量重建判「No changes」即此类，届时走升级人工而非无限自愈，是否重设计度量口径留待裁定）；自愈依赖 `kdo` 在探针运行环境 PATH 中（shutil.which 探测，缺失→FAIL 升级，不静默）；单次自愈上限 300s 超时（实测 14s，富余 20 倍）。

**需要谁动作**：欧阳锋终审本单（重点核：①哨兵从「只告警」改「陈旧分支自愈」是对 #622 红线的有意修订是否认可；②「mtime 前跳=重建成功」判据）；王语嫣知悉值守划销回声误判的机制根源（lag 逐拍变化击穿幂等→形似回声），同类告警建议先查 lag 是否单调增长再定回声。

## 存在性核查（#433：负向判词附核查节，提审前主动补）

- **「无自动刷新载体/无 graph 计划任务」**：核查面=`schtasks //query //fo csv | grep -i "kdo\|graph\|vault\|conveyor"`（2026-09-06 02:07 本会话执行）——命中 kdo-conversation-distill / kdo-conveyor-probe / kdo-conveyor-probe-tech / kdo-daily-audit-digest / kdo-daily-review / KDO-Health-Check / kdo-health-daily / kdo-huangyaoshi-doorbell / kdo-inbox-watch / kdo-inbox-watch-tech，**graph 相关 0 命中**。判词成立。
- **「toolkit/decisions 明文手动节奏」**：`.agent/toolkit.md:87`「`kdo graph rebuild`｜重建 Graph RAG 索引（内容变更后运行）」；`.agent/decisions.md:226`「索引持久化在 `.kdo/graph_index/`，建成就一直在，内容变更后 `kdo graph rebuild` 即可」。两处均本会话 grep 实证，非凭记忆。
- **「rc=0 但 mtime 未前跳」假成功**：`logs/graph-selfheal.log` 两行对照——02:12:42 `OK｜No changes since last rebuild...`（rc=0 判成功，缺陷态）与 02:14:19 `FAIL｜rc=0 但 graphml 未前跳`（判据修正后同场景正确判 FAIL）。台账已入仓。
- **「值守五拍误划销」**：`90_control/todos/wangyuyan.md` 884-951 行段，09-04 23:37 起逐拍「🛑 KDO 基建停拍报警 1 项：graph-index｜陈旧（落后 search_index 48h→56h）」且间拍出现划销登记；#648 `decision_source` 载 09-06 王语嫣复核改判「真实故障非回声」。判词成立。
- **「手动重建间隔 15 天」**：#622 任务单执行报告载重建完成于 09-02 23:29（graphml mtime 02:08 前实测值吻合）；#358 任务单载 08-18 重建。08-18→09-02 = 15 天。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 3 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（不存在/缺失）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）


## 终审记录（2026-09-06 欧阳锋 · 终审 PASS A- · methodology v2.3）

**Verdict**：PASS，等级 **A-**。三重点核查逐项过，功能面独立复跑确认（不凭任务单自述）。

### 三重点核查（任务书 ①②③）

- **① 根因结论附证据**——成立。三层根因（设计层无自动刷新载体 / 阈值层重建节奏未制度化 / 响应层 lag 逐拍变化击穿幂等）逐层有证据：schtasks 全量核查无 graph 计划任务、toolkit/decisions 明文「内容变更后手动跑/即可」、graph-selfheal.log 假成功两行对照、lag -0.89h 实测。独立复核见下方 **存在性核查**。
- **② 哨兵从「只告警」改「陈旧分支自愈」+ #622 红线修订声明**——成立且**认可修订**。docstring 明文「只告警不动作（#622 红线）→ #648 修订：陈旧超阈值分支先自愈（增量重建）再告警」；空目录 / 0 records / graphml 缺失三分支维持只告警不动作（红线在非自愈面原样保留）。自愈形态克制：增量（永不带 --full）、6h 防乒乓、mtime 前跳为成功判据、失败升级人工。是有界修订，非越界改红线。
- **③ 重建后 infra-liveness 下一拍回落**——成立。graphml mtime 02:14:36 ＞ search_index 01:21:14（lag -0.89h，graphml 反超）；conveyor-probe.log 自 01:07 末次告警后至 02:47 多拍无 graph-index 陈旧告警（探针已实际跑过，非仅函数预测）；`_scan_graph_index_health` 逻辑上 issue=None 不再报。

### 需要谁动作之两问

- ① **#622 红线修订**：认可。修订边界=仅「陈旧超阈值」面，其余三面红线原样；自愈失败必升级人工，哨兵仍无静默吞故障。
- ② **「mtime 前跳=重建成功」判据**：认可。rc=0 与落地是两件事（#175 同源教训），mtime 前跳是「重建真的写出新产物」的可观测副作用；「No changes 不落地」转 FAIL 升级人工的边界已声明，不留无限自愈。

### 独立复跑确认项（**存在性核查**）

- `python -m pytest kdo-tools/tests/test_conveyor_probe.py -q` → 53 passed（自愈 4 条 + 陈旧改造 + 原有回归全绿）。
- `python -m pytest kdo-tools/tests/ 90_control/scripts/tests/ -q` → 517 passed（与任务单自述一致）。
- graphml 字节计数 6,539,805 B / 3,639 `<node>` / 6,712 `<edge>`——较 #622 终审记录 3,620/6,694 略增，与增量重建 +19 nodes/+18 edges 方向一致，内容非空、非半建。
- `schtasks /query /fo csv` 独立复跑：kdo-* 计划任务族中无 graph 重建任务，佐证「无自动刷新载体」判词成立。
- `.agent/toolkit.md:87` 与 `.agent/decisions.md:226` 两处「内容变更后运行/即可」手动节奏明文，独立 grep 命中。

### 缺陷与残余风险（非阻断）

- **P2（形式）**：任务单「存在性核查」节为 `## 存在性核查` 标题形态，而机器预审 ④ 认的锚点是 `**存在性核查**` 粗体字面量——当前文件重跑预审仍可能标 🔴。内容实质已达标（核查节 + 逐条证据在位），仅锚点字面量形态差。**落点**：随本终审记录在任务单声明即可，不建议为锚点单独返工；后续同类负向判词直接写 `**存在性核查**` 粗体锚点。
- **残余风险（承接任务单边界）**：lag 度量语义为 mtime 差而非内容差，search_index 周期性重写可推大 lag；自愈依赖 kdo 在探针环境 PATH（已 shutil.which 探测，缺失转 FAIL 不静默）。均已在执行报告边界声明，判定可接受。

**blocking**：无。**residual_risks**：低——哨兵已武装（state 键 graph_index_issue 空/None），下一陈旧事件走自愈→失败升级路径。
