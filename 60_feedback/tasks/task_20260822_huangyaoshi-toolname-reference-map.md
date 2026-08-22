---
id: 415
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-22T12:19:39.915866+00:00'
---
# #415 工具名引用清单（B4-2 替换前置）

- **任务号**：#415
- **状态**：queued
- **assignee**：huangyaoshi
- **优先级**：P0（B4-2 前置，只出清单不替换）
- **立项**：2026-08-22 王语嫣（会诊 B4-2 补强版拍板）

## 任务目标

产出**工具名引用面清单**——活文档批量替换（工具名→角色名）前的影响面地图，防改名改崩脚本/配置（E014）。

## 范围（grep 对象）

工具名清单：codex / claude / hermes / kimi / codebuddy / workbuddy（及大小写变体）

扫描面：
1. hermes profiles（`AppData\Local\hermes\profiles`，10 profile 配置）
2. 脚本引用（kdo-tools/、90_control/scripts/、40_outputs/code/scripts/）
3. cron/schtasks 定时任务定义
4. `.claude/`、`.agent/` 配置与 context 文件
5. 90_control/ 顶层文档（AGENTS.md/PROTOCOL 等）

## 交付

- `60_feedback/consultation/2026-08-22-kdo-systemic-upgrade/w8-toolname-reference-map.md`（或独立 diagnosis）：每条=路径+行号+引用类型（配置/脚本/文档）+替换风险等级
- 活文档 vs 历史文件分界建议（历史文件不替换只加标注，B4-2 拍板口径）

## 验收

- 清单五类扫描面无遗漏声明+grep 命令附输出
- 不改动任何文件（只读）；commit 入档；欧阳锋终审抽"扫描面完整性"
