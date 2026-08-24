---
id: 507
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-24T17:29:22.075201+00:00'
version: v0.2
instance: huangyaoshi
code_files:
  - kdo-tools/daily-audit-digest.py
  - kdo-tools/run-daily-audit-digest.cmd
  - 90_control/infrastructure-inventory.md
---

# #507 每日审计轮段①：daily-audit-digest.py + kdo-daily-audit-digest 定时（06:00）

- **任务号**：#507
- **状态**：queued
- **assignee**：huangyaoshi（抽数脚本+定时任务；审计判断层归风清扬不占本单；欧阳锋终审）
- **优先级**：P1（老朱 08-24 已拍板抽数锚点 06:00）
- **立项**：2026-08-24 王语嫣（风清扬建议书 `diag_20260824_fengqingyang-daily-audit-round.md` 裁定采纳）

## 背景

L1 采集已 30min 定时（kdo-l1-capture）；但风清扬 L2 审计（洞察/资产/建议）按需触发无定时，审计要翻全量原文——慢且烧 token。方案两段：段①脚本定时抽数（零 LLM token）归黄药师=本单；段②风清扬每日一审由老朱一句话触发（暂不 headless，判断层需在场），不占队列。

## 任务

1. 新建 `kdo-tools/daily-audit-digest.py`，每日一次聚合四样原料落一份 digest：
   - 胶囊事件增量：`activity_log.db` 自上次审计以来新事件
   - 各角色 daily-context：当日/最新文件清单 + 差异摘要
   - friction-log：新增行
   - production-queue：状态变更（领单/提审/终审/新立项）
2. 落盘 `D:\KDO-memory\L2-digest\YYYY-MM-DD.md`（D 盘，与 L1-full/L1-backup 同区；**不落 60_feedback/diagnosis**，避免被误扫成建议书）
3. 挂 scheduled task `kdo-daily-audit-digest`，每日 **06:00**（已拍板锚点，覆盖凌晨场），Ready 态，失败可见 stderr 不静默（沿用 #471/#434 口径）
4. 增量正确性：不重不漏（自上次 digest 以来），重跑幂等

## 验证（验证分层）

- L1：脚本跑通，digest 含四样原料；增量对账（手工核一天的事件数）
- L2 狗粮：连跑两日，第二日 digest 只含增量不重复
- L3 待活体：风清扬只读 digest 能出审（不再翻全量），不额外烧 LLM token

## 边界

- 段②（风清扬审）不在本单——本单只产原料
- 06:00 同锚点还有 #508（L1 每日 zip 归档）——两任务同窗口协同，脚本各自独立
- digest 是审计原料不是建议书，不进 PROPOSAL-PENDING 通道

## 关联

- 风清扬建议书 `diag_20260824_fengqingyang-daily-audit-round.md`（含验收标准原文）
- #471（常驻调度+体积红线）/ #434（L0 自动写入端）/ #432（记忆胶囊 L0）
- #508（L1 日期归档，同 06:00 锚点）

## 需要谁动作

- **黄药师**：脚本 + 定时任务
- **风清扬**：段②每日审（老朱触发，不占队列）
- **欧阳锋**：终审本单

## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：每日审计轮段①落地——新建 `kdo-tools/daily-audit-digest.py`（零 LLM token 纯机械抽数），每日一次聚合四样原料落 `D:\KDO-memory\L2-digest\YYYY-MM-DD.md`：①胶囊事件增量（主库 `~/.kdo-memory/L1/activity_log.db`，ts 游标）②各角色 daily-context 最新文件+差异栏摘要（按 文件名+hash 签名判更新）③friction-log 新增行（共享+7 角色，行 hash 去重截尾）④production-queue 状态变更（新立项/流转/出队 diff，首次跑只给计数基线防全量 dump）。增量正确性双向验证（不重+不漏）；同日重跑覆盖同名 digest 不 append 重复；dry-run 零副作用（不落盘不存游标——08-24 探针事故同纪律）。计划任务 `kdo-daily-audit-digest` 每日 06:00 已注册（cmd 包装+内部日志，TR 不经过 shell 教训应用），真机 /run 实测 LastResult=0+Ready 态+run.log 落盘。不落 60_feedback/diagnosis（不误扫成建议书）；总表+计划任务表已登记（infra-status 27 项全绿 0 未登记）。

**交付物**：
- `kdo-tools/daily-audit-digest.py`（四原料抽数+增量游标+幂等）
- `kdo-tools/run-daily-audit-digest.cmd`（纯 ASCII 计划任务包装）
- 计划任务 `kdo-daily-audit-digest`（每日 06:00，Ready，真机 result=0）
- `D:\KDO-memory\L2-digest\2026-08-25.md`（首份 digest 已落）
- `90_control/infrastructure-inventory.md`（工具族+计划任务表登记）

**验证**：
- L1：脚本跑通，digest 含四样原料（首跑：事件 27 / 上下文 11 角色 / friction 108 / 队列基线 1）；增量对账——首跑 24h 窗口 27 事件与主库 SELECT 一致（max_ts=2026-08-24T17:24Z）
- L2 狗粮：连跑两次——第二跑 事件 0/上下文 0/friction 0/队列 0（**不重复**✅）；游标回拨 1 小时重跑——13 条事件重捕（**不漏**✅）；dry-run 后首跑仍全量捕获（dry-run 零副作用✅）；定时任务真机 /run result=0（计划任务改动真机验证纪律）
- L3 待活体：风清扬只读 digest 出审（不翻全量）；明早 06:00 首次定时自动跑

**边界**：段②（风清扬每日审）不在本单；脚本与 #508（同 06:00 锚点 L1 zip 归档）各自独立无共享状态；digest 不进 PROPOSAL-PENDING 通道；friction 行去重按内容 hash（同行重复记录归一为一条——与探针 #458 同口径）；daily-context 首次跑含全部 11 角色最新件（基线性质，次跑起只报更新）。

**需要谁动作**：欧阳锋终审本单；风清扬知悉——明早 06:00 起 digest 每日落 `D:\KDO-memory\L2-digest\`，段②每日审只读当天文件即可；王语嫣知悉计划任务表新增一行。
