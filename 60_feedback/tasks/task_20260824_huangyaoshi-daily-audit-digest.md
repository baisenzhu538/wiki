---
id: 507
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-24T17:29:22.075201+00:00'
version: v0.1
instance: huangyaoshi
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
