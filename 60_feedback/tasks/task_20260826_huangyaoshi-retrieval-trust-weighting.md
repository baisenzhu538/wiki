---
id: 541
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-26T15:02:02.801340+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- kdo-tools/mcp/
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
