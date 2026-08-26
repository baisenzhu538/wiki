---
id: 541
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-26T15:02:02.801340+00:00'
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
