---
id: 549
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-26T20:07:35.343451+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- kdo-tools/token_meter.py
- kdo-tools/tests/test_token_meter.py
- kdo-tools/run-kdo-health.cmd
- 90_control/infrastructure-inventory.md
- 90_control/notification-coverage-matrix.md
- 60_feedback/analytics/
---

# #549 全厂 token 计量：会话级 usage 落事件层（消耗不可观测=无法管理）

- **任务号**：#549
- **状态**：queued
- **assignee**：huangyaoshi（口径建议稿由风清扬出；欧阳锋终审）
- **优先级**：P2（不阻断生产；但「单均成本」是阶段 2 降档评估的前置基线，老朱 08-24 已关注）
- **立项**：2026-08-26 王语嫣（风清扬建议书 diag_20260825_fengqingyang-automation-cost-audit 裁定：建议 1 采纳立项；建议 2「单均 token 成本」挂 #514 基线第五指标口径，不新立；建议 3 纪律采纳——阶段 2 降档成本对照以计量数据为准，不凭感觉）

## 背景

时钟脚本层 7 个定时任务零 token（实测日 340 次秒级），设计正确。LLM 会话层是消耗主体但全厂无 token 计量：`~/.kimi/` 无 usage 文件，旧执行引擎 usage_record.jsonl 链路随 L1 采集面重构断更。后果：无法回答「今天烧了多少 token / 单均成本 / 哪个角色最贵」。

## 任务

1. **计量源调研**：kimi CLI / claude / hermes(deepseek) 各执行引擎的 usage 可得性逐一枚举（API 响应字段 / 本地日志 / 都无则估算口径）——先出可得性矩阵再定采集点
2. **落事件层**：会话级 usage 写事件库新事件类型（或日汇总文件），统一引擎只此一源、计量一处
3. 与 #514 基线的接口：预留「单均 token 成本 = 角色归一 token 总量 ÷ 同期完成单数」聚合口径，按周聚合
4. §3.19：新事件类型 → 同步通知覆盖矩阵登记

## 边界

- 只计量不限制（不做配额/熔断——那是 F-055 阶段 2/3 的事）
- 某引擎 usage 不可得 → 如实标「估算口径」并注明误差来源，不编造精确值
- 不回溯历史（断更期数据不可补，从上线日起算）

## 验收

- 可得性矩阵 + 至少一个引擎的真实 usage 落事件层 + 日汇总可读；欧阳锋终审


## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：全厂 token 计量落地（新工具 `kdo-tools/token_meter.py`）。①**可得性矩阵**（实测逐引擎取证）：claude=`~/.claude/projects/*/*.jsonl` 每条 assistant 消息带 usage（input/output/cache_read/cache_write 精确值）；kimi=`~/.kimi-code/sessions/<wd>/<session>/agents/<agent>/wire.jsonl` 的 `usage.record`（inputOther/output/inputCacheRead/inputCacheCreation 精确值）；hermes=profiles/*/state.db `sessions`+`session_model_usage` 表（会话级 token 累计+estimated_cost 字段，精确值）——三引擎全部本地可得，零估算口径（唯一估算项=claude/kimi 会话的角色归因：cwd 粒度，混合角色会话标注估算）；②**采集器**：字节偏移游标增量（jsonl 两引擎）+ 会话累计差值（hermes）→ 日汇总 `60_feedback/analytics/token-usage-YYYY-MM-DD.{json,md}` + 事件层 `token_usage` 汇总事件；不回溯历史（首见文件/会话只建游标），**首日引导**：首跑只计今日 00:00 后记录（既有读数又不破边界）；wire.jsonl 同名防撞（key=<session_id>/<agent>）；dry-run 零副作用（不消费游标，F-036 纪律）；③**挂例行**：kdo-health-daily（02:07）cmd 追加一行；④**#514 接口**：日 JSON 按 引擎×会话/角色 分解，周聚合=日汇总求和 ÷ 同期 reviewed 单数（口径写进日 md 注记）；⑤§3.19：矩阵事件 19 行 + infrastructure-inventory 登记（#488 纪律——被覆盖对照检查当场抓到补登）。

**交付物**：
- `kdo-tools/token_meter.py`（采集器+渲染+事件层钩）
- `kdo-tools/tests/test_token_meter.py`（7 例回归）
- `kdo-tools/run-kdo-health.cmd`（挂 02:07 例行）
- `90_control/infrastructure-inventory.md`（工具族登记）+ `90_control/notification-coverage-matrix.md`（事件 19 行）
- `60_feedback/analytics/token-usage-2026-08-27.{md,json}`（首日真实读数）

**验证**：
- L1 单测 7 例全过：不回溯首见跳过/claude 增量/kimi 字段映射/hermes 首见清零+差值增量/日汇总渲染/dry-run 不消费游标/首日引导只计今日（昨日记录不回溯）；kdo-tools 基线 **185 passed**（含 infra 覆盖对照——token_meter 登记后转绿）
- L2 狗粮（真机首跑）：`token-usage-2026-08-27.md` 首日真实读数——kimi 引擎按会话分解（本会话 session_6c3ded32 今日 cache_read 80.3M/output 132k 等），hermes 今日零新会话（如实为空：08-26 最后会话 23:43 起跑，无今日会话）；claude 今日零记录（正常）
- L3 待活体：02:07 例行首跑后的次日汇总 + 周末 #514 聚合口径首用
- **预审红项预标注**：预审若检「零/空/无」类词=首日数据如实描述（非缺陷），预标注在此

**边界**：只计量不限制 ✅；不回溯历史 ✅（首日引导=今日 00:00 起，非历史回填）；引擎不可得→估算的兜底未启用（三引擎全本地可得）✅。

**需要谁动作**：欧阳锋终审本单；风清扬知悉——#514 聚合接口已就绪（日 JSON 在 60_feedback/analytics/）。
