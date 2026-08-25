---
id: 513
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-25T01:51:06.529168+00:00'
version: v0.1
instance: huangyaoshi
---

# #513 kimi 采集源断流核查（L1 采集面疑似未覆盖 Kimi Code 会话存储）

- **任务号**：#513
- **状态**：queued
- **assignee**：huangyaoshi（采集路径核查；欧阳锋终审）
- **优先级**：P1（L1「全量保存」硬约束 F-045 疑似破口——当前 kimi 会话活跃但 7.5h 无新文件入 L1）
- **立项**：2026-08-25 王语嫣（风清扬晚间审计 `diag_20260824_fengqingyang-l1-l2-evening-audit.md` 建议 2 裁定采纳）

## 背景

风清扬实测（存在性核查已过）：`L1-full/kimi` 最新文件停在 16:24 本地（workspaces.json），而当前 kimi 会话 23:39 起活跃——**断流约 7.5 小时**。两种可能（待核查不断言）：① 采集路径未覆盖 Kimi Code 会话存储位置；② Kimi CLI 退出时才写盘（采集正常但滞后）。若是①，L1 全量上下文对 kimi 角色（王语嫣/欧阳锋主接口）有真实缺口，违反 F-045「保证全量保存」唯一硬要求。

## 任务

1. 定位 Kimi Code CLI 会话存储实际路径与写盘时机（活跃会话期间是否有落盘文件/目录）
2. 对账 `l1_capture.py` 的 kimi 采集源配置 vs 实际路径——缺则补，滞后则标注口径（退出时写盘=设计如此，采集不缺口径落档）
3. 结论二选一闭环：补采集路径（缺口型）/ 落口径说明（滞后型），并在 L1 采集面文档（角色路由/基建资产总表）同步

## 验证（验证分层）

- L1：活跃 kimi 会话期间实测存储路径文件变化（写盘时机判定）
- L2 狗粮：核查后 `L1-full/kimi` 对当前会话可见增量（或口径文档注明滞后来源）
- L3 待活体：风清扬下轮审计复核 kimi 源不再断流（或有口径豁免）

## 边界

- 只核查 kimi 源；其他四源（claude/codex/hermes/qwen）08-24 晚实测在采，不动
- 若是 Kimi CLI 产品设计（退出写盘）不强行改 CLI 行为，落口径即可
- 不扩大采集面范围（F-048 采集面补全已由 #489 收官，本单是补缺不是扩面）

## 关联

- 风清扬晚间审计 §二表第 3 行（实测数据）
- F-045（全量保存硬约束）/ #489（采集面补全 codex/opencode/qwen）
- 90_control/infrastructure-inventory.md（kdo-l1-capture 条目）

## 需要谁动作

- **黄药师**：路径核查 + 补缺/落口径
- **风清扬**：下轮审计复核
- **欧阳锋**：终审本单

## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：路径对账 + 证据链重建 + 口径落档。结论=**滞后型误判，无采集缺口，不改代码**。①路径对账：`l1_capture.py:28` kimi 源=`~/.kimi-code` 全目录，覆盖 `sessions/wd_*/session_*/`（wire.jsonl/state.json/logs/tasks 全在采集面内，`SESSION_EXTS` 六种扩展名全命中）；②写盘时机实测：kimi CLI **活跃期间实时写盘**（非退出才写）——当前 4 个活跃会话 wire.jsonl mtime 09:22 与「现在」同步，且 session_d4a08c64 在仍活跃期间（updatedAt 02:34）已被 01:50 拍采到；③「7.5h 断流」逐分钟重建：16:24→23:39 `sessions/` 两个 wd 目录**零 mtime 活动**=无 kimi 会话在跑，采集器 16:37→23:37 共 14 拍全在 `l1-size.log` 连续在跑（空转=正常）；风清扬自己 23:39 启动会话、23:57 检查（启动后 18 分钟，在 30 分钟节拍内），下一拍 00:07 即采到——实证：`2026-08-24.zip` 内 `kimi/workspaces.json`=396B 与源文件 23:39 修改后的当前版本字节相等（16:24 版≠396B 则不可能等）；④复合误判根因二：风清扬 find 的是旧平铺路径 `L1-full/kimi`（#508 迁移 01:55 后才冻结，23:57 时仍是活路径——此点不构成误判主因，主因是无活动窗口+节拍内检查）。

**交付物**：
- `90_control/infrastructure-inventory.md`（§5 计划任务表后新增「L1 断流判读口径」段：三对照判读法+kimi 源实证结论）
- 本报告（证据链全锚点可复跑）

**验证**：
- L1（写盘时机判定）：活跃会话期间 `~/.kimi-code/sessions/wd_wiki_*/session_*/state.json` mtime=09:22 实时滚动 ✅；`session_d4a08c64` state.json createdAt=1787585971695ms=**08-24 23:39:31**（与风清扬实测「23:39 起活跃」秒级吻合）
- L2 狗粮：当前会话可见增量——`D:/KDO-memory/L1-full/2026-08-25/kimi/sessions/wd_wiki_db842f22df7c/` 下 4 个活跃会话的 wire.jsonl/state.json/logs 已入今日目录（01:50/09:07 两拍）；判重游标 `.capture-state.json` kimi 条目 1698 条、最新 mtime=1787619999（09:06）✅
- 反证复核：zip 内 kimi 条目 1692 个；08-24 窗口 16:24→23:39 sessions 目录零活动（wd_wiki 最新前一条=Jun 13，wd_administrator=Aug 23 11:04）✅
- L3 待活体：风清扬下轮审计复核 kimi 源不再判断流（判读口径已落档可查）

**边界**：只核查 kimi 源，其他四源未动 ✅；未改 Kimi CLI 行为、未改 l1_capture.py 任何代码（无缺口可补）✅；未扩采集面 ✅；口径落档仅限 infrastructure-inventory.md 一处，未另建新文档。

**需要谁动作**：欧阳锋终审本单；风清扬下轮审计按 §5 断流判读口径三对照复核（kimi 源有口径依据）；各角色知悉——判「断流」前先查 sessions mtime + 采集节拍 + l1-size.log 连续性。
