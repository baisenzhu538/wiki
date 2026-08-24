---
id: diag_20260824_fengqingyang-proposal-frontmatter-gate
title: 建议书：frontmatter 三元组校验前置（治「建议书未登记」静默失效）
type: proposal
author: 风清扬（观察者 / 审计者）
created_at: 2026-08-24
status: pending_orchestration
audience: 王语嫣
---

# 一、结论先行

- 建议书登记依赖 conveyor_probe 的 frontmatter 三元组 `audience: 王语嫣` + `status: pending_orchestration`（+ 惯例 `type: proposal`）；字段漂移时探针**静默跳过**，建议书落在盘上、王语嫣队列与飞书通知都看不见。
- 实证：本会话 4 份建议书写成 `to: 王语嫣` + `status: pending`，探针零告警、登记 0 份——靠手动验「新登记」回执才捞回。
- 建议：把「三元组校验」前置成门禁 + 模板单点化 + 写后自检，让「写错 frontmatter」当场可见，而非事后捞。

# 二、实证（非转述）

| 项 | 值 |
|:--|:--|
| 探针登记契约 | `audience` 含「王语嫣」且 `status == pending_orchestration`（`_scan_proposals()` 源码） |
| 本会话漂移写法 | `to: 王语嫣` + `status: pending` + `type: diagnosis` |
| 后果 | 4 份建议书（feishu-huangyaoshi / capsule-audit-08-24 / daily-audit-round / l1-date-archive）盘上有、队列 0 条 |
| 探针行为 | 不命中即 `continue`，**无 stderr、无日志、无通知** |
| 已处置 | 4 份 frontmatter 改正 + 补登（23:28 队列齐）；friction-log 记一行 |

# 三、根因

- 契约漂移：建议书 frontmatter 从 `audience / status:pending_orchestration / type:proposal` 漂移成 `to / status:pending / type:diagnosis`，无模板约束。
- 探针静默：登记失败不报警——机制依赖契约，契约破时机制静默失效，无人知道「建议书没送达」。
- 与今日胶囊审计 F1/F2 同族：都是「覆盖缺口 / 基于旧契约行动前不复核」，治本是门禁化而非靠自觉。

# 四、方案（三件套）

## 1. 探针 near-miss 报警（门禁化，P1，黄药师）

`conveyor_probe._scan_proposals()` 增加「疑似建议书但三元组不完整」检测：凡 `diag_*.md` 有 `author` + `title`（或 `type: proposal`）却缺 `audience` 或 `status != pending_orchestration` 的，显式输出 stderr + 落一条 gate-blocked 式记录（或 friction 线索），**不再静默 continue**。让作者当场看到「这份没登记成」。

## 2. frontmatter 模板单点化（P1，王语嫣裁口径 + 黄药师落模板）

模板收敛为：`type: proposal` / `status: pending_orchestration` / `audience: 王语嫣`；`to:` 与 `status: pending` 标注 deprecated。建议书样例与 agent-os 相关说明同步，禁止双轨。

## 3. 写后自检纪律（P2，全角色，agent-os §10 修订窗口）

建议书作者写完即跑 `python kdo-tools/conveyor_probe.py`，验证自己文件名出现在「新登记 N」回执里；不在 = 未登记 = 当场改 frontmatter 重登。此为纪律补强，非新工具。

# 五、验收标准

- 故意写一份三元组错误的建议书 → 探针报警（非静默），王语嫣能收到「未登记」信号。
- 模板与探针契约一致，`to:` / `status: pending` 不再出现于新建议书。
- 作者有一条「写完即验回执」的可执行动作（写进 agent-os 或各角色交付纪律）。

# 六、建议汇总

| # | 动作 | 对象 | 优先级 |
|:--|:--|:--|:--|
| 1 | 探针 near-miss 报警（门禁化） | 黄药师 | P1 |
| 2 | frontmatter 模板单点化 + 废弃双轨 | 王语嫣裁口径 / 黄药师落模板 | P1 |
| 3 | 写后自检纪律入 agent-os | 全角色（老朱拍板窗口） | P2 |