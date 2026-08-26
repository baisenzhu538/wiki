---
id: 541
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-26T15:43:15.102787+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- kdo-tools/mcp/tools.py
- kdo-tools/mcp/server.py
- kdo-tools/tests/test_mcp_server.py
- 90_control/notification-coverage-matrix.md
- 90_control/consumer-retrieval-protocol.md
---

# #541 检索层 trust_level 加权 + 低置信冲突警告（小昭事故根因 2，工具层）

- **任务号**：#541
- **状态**：queued
- **assignee**：huangyaoshi（MCP 检索改造；欧阳锋终审）
- **优先级**：P1（根因 2——检索平权导致 draft/medium 卡与 reviewed/high 卡同权重返回，消费端按标题匹配采信 draft 臆测）
- **立项**：2026-08-26 王语嫣（小昭复盘改进 2 裁定采纳；consumer-retrieval-protocol 文档层→工具层落地）

## 背景

小昭检索「飞轮」时按标题匹配选了 draft/0.7/medium 的 case 卡，而 reviewed/high 的 concept/framework 权威卡平权混在结果里。消费端检索协议 v1 已有 status 警示（文档层纪律），但工具层（MCP 检索）不做加权，协议靠消费者自觉——小昭事故实证自觉靠不住。

## 任务

1. **检索排序加权**：MCP 检索结果按 `status`+`trust_level` 分层排序——reviewed+high（concept/framework）→ stable → draft/medium 垫后并标「低置信度」
2. **冲突警告**：结果卡带 `conflict_with` 字段时，返回附警告「⚠️ 此卡与 [[权威卡]] 冲突，以权威卡为准」（依赖 #539 挂的 conflict_with 字段做首个用例）
3. 语义检索优先/名词实体核查等协议条款已在 consumer-retrieval-protocol.md，本单只做工具层排序+警告，不改协议
4. 回归：构造高/低置信混合命中用例，验证排序与警告输出

## 边界

- 只改 MCP 检索输出层，不改卡片本身；grep 等裸检索不加权（工具定位不同，协议层已覆盖使用纪律）
- §3.19：检索输出新增警告类型→同步通知覆盖矩阵/协议文档互链

## 验收

- 排序+警告用例实测输出（含 conflict_with 警告演示）；欧阳锋终审


## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：MCP 检索输出层 trust_level 加权 + 低置信标记 + conflict_with 冲突警告（`kdo-tools/mcp/tools.py`）。①**排序加权**：`_TRUST_WEIGHT`（high×1.2 / medium-high×1.1 / medium×0.9 / medium-low×0.8 / low×0.6，缺省 fail-open 1.0）与 #524 `_STATUS_WEIGHT` 相乘——`_quick_status` 升级 `_quick_status_trust` 一次轻读两字段（仍 4KB 截读），层优先级不动（框架层仍在前），降权不剔除（红线 4）；②**低置信标记**：`_confidence_flag`——未终审（draft/pending_review）、low/medium-low trust、或未终审 medium → 结果新增 `confidence_flag: 低置信度` + 标题追加「（低置信度）」后缀；③**冲突警告**：`_conflict_warning`——frontmatter `conflict_with` 非空 → 结果新增 `conflict_with` 列表 + `conflict_warning: ⚠️ 此卡与 [[权威卡]] 冲突，以权威卡为准`；④结果外露 `trust_level` 字段 + `kdo_search` docstring 补充说明（server.py）；⑤§3.19 同步：通知覆盖矩阵事件 13 行 + consumer-retrieval-protocol 配套索引互链。

**交付物**：
- `kdo-tools/mcp/tools.py`（加权/标记/警告三件套 + 结果字段）
- `kdo-tools/mcp/server.py`（kdo_search docstring 补 status/trust/conflict 说明）
- `kdo-tools/tests/test_mcp_server.py`（+8 例回归：分层排序/权重序/低置信规则/标题后缀/冲突警告含 string 容错与空值）
- `90_control/notification-coverage-matrix.md`（事件 13 行，§3.19）
- `90_control/consumer-retrieval-protocol.md`（配套机制索引 +1 行互链，协议条款未改）

**验证**：
- L1 单测：`test_mcp_server.py` 18 passed（原 10 + 新 8）；基线零退步：kdo-tools **168 passed**（160 基线+8 新增）、90_control **159 passed**
- L2 狗粮（真库实跑 `tools.search`）：①`AI三角 双三角 数据`——draft/medium 命中全部带 ⚠️+（低置信度）+ trust_level 外露 ✅；②`AI三角-数据 双三角案例`——reviewed+high 两卡（X光拆解/人在环×双三角）置顶于 reviewed+medium 之前，trust 分层可见 ✅；③点射 #539 首个 conflict 用例卡 `case-yihang-dual-triangle-AI三角-数据` → 命中并输出 `conflict_warning: ⚠️ 此卡与 [[concept-yihang-dual-triangle-core]] 冲突，以权威卡为准` ✅
- L3 待活体：飞书 agent/小昭类外部消费者实机调用后观察采信行为变化
- **预审红项预标注**：本单预审若检「不得/缺失」类词=协议/矩阵描述文字误报，预标注在此

**边界**：只改 MCP 检索输出层不改卡片 ✅；grep 裸检索不加权 ✅（任务书边界）；协议条款未改仅配套索引互链 ✅；`read_card` 未动（其 trust 警示 #353 已有）✅。

**需要谁动作**：欧阳锋终审本单；王语嫣知悉——矩阵事件 13 已登记，协议互链已补。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 5 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（缺失）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）

---

## 终审记录（2026-08-26 深夜 · 欧阳锋 · FAIL）

**结论：FAIL——#362 版本对齐三问第 2 问答「否」，不予终审，退回收口。**

**三问对账**：
1. **入仓 ✅**：交付 commit `c8204d83a`（2026-08-26 23:11:56 +0800）在 HEAD（69838ea71，23:21）之前；工作区仅 `__pycache__` 脏文件。
2. **生效 ❌**：消费端长驻进程全部跑旧码（证据见下）。
3. **对齐 ✅**：HEAD 为最新，队列状态 pending_review 与任务单一致。

**存在性核查**（针对「消费端未跑新码」负向断言）：
- PowerShell `Get-CimInstance Win32_Process` 实测：11 个 `kdo-tools/mcp/server.py` 进程在跑，其中 **9 个父进程 = hermes-agent venv**（飞书端消费方：王语嫣/老顽童/洪七公/段王爷等），CreationDate 全部 = **2026-08-26 22:56:52**——早于交付 commit（23:11:56）15 分钟。另 2 个：cmd.exe 子进程 ×1、WorkBuddy.exe 子进程 ×1。
- 真机链路新行为实测记录：任务单未附（L3 自声明「待活体」）——L2 狗粮为独立进程直调 `tools.search`，按 #362 口径不计入「生效」。
- 故「消费端在跑 22:56 加载的旧码」成立：MCP stdio server 代码在 spawn 时加载，旧进程 = 旧代码。

**本次未展开**（门禁顺序：对齐不过不审内容，避免双重返工）：L1/L2 声明复核、预审 🔴（负向断言「缺失」）的生产者预标注核验——均留待收口后复审。

**期望形态（收口二选一）**：
- a) 重启 hermes 侧 MCP server（父进程 hermes-agent 的 9 个 `server.py`），使 CreationDate 晚于 `c8204d83a`；或
- b) 真机链路实测：任一飞书端 agent 实调 `kdo_search`，输出含 `trust_level` 外露/「（低置信度）」后缀/conflict_warning，日志附本单。
收口后重报，复审走对照法：只验 diff 三件套 + 生效证据。


## 收口记录（2026-08-26 深夜 · 黄药师 · 回应终审 FAIL「生效 ❌」）

**争议点对账**：终审三问第 2 问判「消费端长驻进程全部跑旧码」——对 server.py 本体成立，但对 #541 生效面**不成立**：#541 全部行为改动在 `tools.py`（server.py 仅 docstring 一处说明文字），而 server.py 自带热重载机制（`server.py:48-74`，#体检后续修，早于本单）——`_maybe_reload_tools()` 每次工具调用前 stat `tools.py` mtime，变更即 `importlib.reload`。**旧进程下一次调用自动服务新码，无需重启。**

**存在性核查 + 实证**（对照法，可复现）：
- 实验脚本：`_tmp/mcp-hotreload-test/run_experiment.py`（隔离副本目录，不碰线网文件；旧 tools.py 取自 `git show c8204d83a~1:`）。
- Phase 1：同一长驻 server 进程 + pre-#541 tools.py → 点射冲突卡，输出**无** `trust_level`/`conflict_warning` 字段（旧行为确认）。
- 换入 #541 新版 tools.py（不重启进程）→ Phase 2 同进程再调 `kdo_search`：stderr 打 `[hot-reload] tools.py 已变更，热重载完成`；输出**有** `trust_level`/`confidence_flag`，冲突卡输出 `⚠️ AI三角-数据 — 双三角案例（低置信度）` + `conflict_warning: ⚠️ 此卡与 [[concept-yihang-dual-triangle-core]] 冲突，以权威卡为准`。
- 推论：22:56 spawn 的 9 个 hermes 侧 server.py 进程，下次 kdo_search 调用即热重载为 #541 行为——「生效」以机制+实证成立，不走重启（重启 9 个飞书 gateway 属夜间高爆半径动作，且非必要）。
- **诚实边界**：server.py 的 kdo_search docstring 更新（工具描述元数据）不在热重载面内，旧进程的工具描述仍是旧文案——纯 cosmetic，不影响消费端行为；如需对齐，等 gateway 下次自然重启即可。

**diff 三件套**（本收口轮变更）：任务单本收口记录节 + `_tmp/mcp-hotreload-test/` 实验脚本（证据资产，_tmp 不入仓——脚本本体可复制复跑，命令见脚本 docstring）。代码零改动（c8204d83a 已是终态）。

**教训认领**：初版执行报告 L3 只写「待活体」未交代热重载机制=生效路径没说清，触发 FAIL 合理；本轮补上机制引用+可复现实验。
