---
id: 445
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-23T04:39:31.132210+00:00'
instance: huangyaoshi
---
# #445 KDO 一键启动脚本（右键启动 + 角色菜单）

- **任务号**：#445
- **状态**：queued
- **assignee**：huangyaoshi（基建单一实例；终审=欧阳锋；编排=王语嫣）
- **优先级**：P2（体验优化；B/C 文档收敛部分先行止血，本单为脚本体验层）
- **立项**：2026-08-23 王语嫣（风清扬建议书 `diag_20260822_fengqingyang-coldstart-oneclick-recovery.md` 三件套之 A 项裁定采纳；老朱原诉求=降启动 token 损耗）

## 任务目标

老朱三步内从桌面到 agent 会话：右键 wiki 文件夹 → 菜单选角色 → 自动 cd wiki 目录并拉起对应 CLI 工具，无需手动敲路径与工具命令。

## 范围

1. 产出 `启动agent.ps1`（或等价右键菜单集成）：Windows Terminal 拉起，菜单列出 CLI 类角色（王语嫣/欧阳锋/黄药师/老顽童/段王爷/洪七公），选中后自动 `cd C:\Users\Administrator\Desktop\wiki` + 拉起对应 CLI 工具。
2. 飞书类角色不进菜单（gateway 常驻，飞书直接聊）。
3. 脚本入 `kdo-tools/` 或 `90_control/scripts/`（黄药师定，说明理由）。

## 验收（验证分层声明按 #444 口径）

- L2 狗粮：每个角色菜单项实际拉起一次，终端落在 wiki 目录。
- L3 活体：**老朱亲手三步完成一次启动并确认**——用户确认才算「真了」（黄药师建议书铁律 4：外部依赖验证双保险）。

## 边界

- 只做启动体验，不做冷启动自恢复（B 项归 #419 追加）/不做口令收敛（C 项王语嫣自办）。
- 不碰各角色 context（context 归各自维护）。
- 交付五字段（F-034）+ 验证分层声明 + 审查意见落盘（F-035）+ commit 入档。

## 关联

- 建议书：`diag_20260822_fengqingyang-coldstart-oneclick-recovery.md`（三件套 A 项）
- 同族：#443 探针路由（通知投递面）/ 黄药师验证分层建议书（L3 活体验收口径）
