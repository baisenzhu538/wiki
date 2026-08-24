---
id: 506
assignee: huangyaoshi
status: queued
updated_at: '2026-08-24T16:00:00+00:00'
version: v0.1
---

# #506 建议书 frontmatter 三元组 near-miss 门禁 + 模板单点化

- **任务号**：#506
- **状态**：queued
- **assignee**：huangyaoshi（探针扩展 + 模板落地；口径王语嫣已裁；欧阳锋终审）
- **优先级**：P1（建议书通道静默失效实证——4 份建议书盘上有、队列 0 条、零告警）
- **立项**：2026-08-24 王语嫣（风清扬建议书 `diag_20260824_fengqingyang-proposal-frontmatter-gate.md` 裁定采纳建议 1+2）

## 背景

建议书登记依赖 conveyor_probe frontmatter 三元组 `audience: 王语嫣` + `status: pending_orchestration`（+惯例 `type: proposal`）。08-24 风清扬 4 份建议书写成 `to: 王语嫣` + `status: pending`，探针不命中即 `continue`——**无 stderr、无日志、无通知**，靠手动验回执才捞回（E052 同族：机制依赖契约，契约破时静默失效）。4 份已改正补登（23:28 队列齐）。

**口径已裁（王语嫣 08-24）**：建议书 frontmatter 单轨 = `type: proposal` / `status: pending_orchestration` / `audience: 王语嫣`；`to:` 与 `status: pending` 标注 deprecated，禁止双轨。

## 任务

1. **探针 near-miss 报警**：`conveyor_probe._scan_proposals()` 增加「疑似建议书但三元组不完整」检测——凡 `diag_*.md` 有 `author`+`title`（或 `type: proposal`）却缺 `audience` 或 `status != pending_orchestration` 的，显式 stderr + 落 gate-blocked 式记录（或 friction 线索），不再静默 continue
2. **模板单点化**：建议书模板/样例收敛到单轨三元组（探针契约同改一处定义，模板与契约不漂移）；`to:`/`status: pending` 写 deprecated 注记；agent-os 相关说明同步（修订窗口内只做 deprecated 标注，新纪律条文待老朱拍板——见停车场）
3. 回归用例：故意写三元组错误的建议书 → 探针报警（非静默）

## 验证（验证分层）

- L1：单测——near-miss 样本（`to:`/`status: pending`/`type: diagnosis` 变体）全部触发报警；正常三元组不误报
- L2 狗粮：拿 08-24 漂移的 4 份原件（git 历史版本）回放到探针，确认能检出
- L3 待活体：下一份 frontmatter 漂移建议书当场可见，不靠事后捞

## 边界

- 只加 near-miss 报警，不改正常登记链路（探针只通知只登记纪律不动）
- 写后自检纪律（作者写完即跑 probe 验回执）入 agent-os §10 属老朱拍板窗口，不在本单施工
- 不强制存量历史建议书回改 frontmatter

## 关联

- 风清扬建议书 `diag_20260824_fengqingyang-proposal-frontmatter-gate.md`（实证表完整）
- E052（定期扫+扫 pattern 全两层）；F-034/F-035 门禁家族同族（想犯错也犯不了，B2-4）
- #421（建议书自动登记+到达即时通知，登记通知同源）

## 需要谁动作

- **黄药师**：探针 near-miss + 模板单点化
- **王语嫣**：口径已裁（本单），agent-os 纪律条挂修订窗口
- **欧阳锋**：终审本单
