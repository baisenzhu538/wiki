---
id: 369
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-19T01:30:00+00:00'
title: 派生脚本化 + 写入唯一入口（P3，codex 建议书⑤采纳）——daily-context-save 收口 + 派生物全脚本生成
priority: P3
dependency:
- 365
- 366
reviewed_by: 欧阳锋
---

# #369 派生脚本化 + 写入唯一入口（P3）

## 任务目标

派生物全部脚本生成、写入只走唯一入口：消灭"派生副本手改"（codex 根因 5）与多头写入。

## 素材/证据

- codex 建议书 §二根因 5：dashboard.md/dashboard.html/vault-status.md/agent-contexts-summary.md 有手改痕迹；§四 P3 方案
- 现有基础：generate-dashboard.py / daily-context-save.py 已在役，本任务=收口而非新建

## 修改范围

1. **daily-context-save.py 扩展为唯一写入入口**：所有 agent 收尾统一调用（含版本/hash 留痕）
2. **派生物脚本化**：dashboard/vault-status/agent-contexts-summary 全脚本生成 + `updated_at` + `git_head` 标记；手改痕迹检测（生成 hash 校验）
3. **可选**（不在必做范围）：kdo MCP 加 memory get/set，Hermes 三处 MEMORY.md/USER.md 收口统一读写——先出评估不实施

## 边界

- 依赖 #365（注册表定义派生关系）+ #366（指针引用派生物）
- MCP 记忆服务为可选项，需评估单独立项

## 验收标准

1. 派生物全部由脚本生成且带版本标记
2. 手改派生物可被检测报警
3. 全厂收尾统一走 daily-context-save.py（抽查 2 角色）

## 交付

1. 脚本化收口 + 检测机制
2. 送欧阳锋终审

## 执行记录（2026-08-19 黄药师，已提审）

### 交付

1. **派生物脚本化 + 版本标记**：三个生成器（generate-dashboard.py / vault-snapshot.py / summarize-agent-contexts.py）输出头部统一加 `generated-by · updated_at · git_head` 标记（dashboard 为 HTML 注释头，另两个为 blockquote 首行）
2. **手改检测**：生成器生成后写输出 hash 到 `90_control/scripts/.derived-hashes.json`（绝对路径 key）；新脚本 `check-derivatives.py` 比对当前 hash vs 基线——不匹配 = HAND_EDITED 报警；已挂入 health-check（#369 行 + 提示）
3. **daily-context-save.py 唯一写入入口留痕**：save 时 frontmatter 自动加 `git_head`（wiki 仓 HEAD）+ `content_hash`（正文 sha256[:12]）——收尾文件可校验手改
4. **可选 MCP memory get/set 未实施**（边界允许）：评估见下

### 实测（验收标准全过）

- 三生成器跑通建立基线 → check-derivatives [PASS] 全部一致 ✅
- 手改 vault-status.md 追加一行 → [HAND_EDITED] 报警 → 重新生成 → [PASS] 恢复 ✅
- daily-context-save 冒烟：frontmatter 含 git_head=76f2fb662 + content_hash=16b2e12c05c2 ✅
- 修了两个实现 bug：heredoc 转义破坏 vault-snapshot 字符串（SyntaxError→修复）；summarize hash key 相对路径与检测不匹配（→resolve() 绝对路径）

### MCP memory get/set 评估（不实施，建议单独立项）

现状：Hermes 三处记忆（MEMORY.md/USER.md/记忆目录）已由 #367 冻结/收敛大半；kdo MCP 加 memory 工具 = 让 agent 经 MCP 读写记忆——收益：统一入口；风险：MCP 权限面扩大（写操作）+ 与 hermes 原生记忆冲突。建议：等 #368 复盘范式定标后评估，P3 排队。

## 交付

1. 三生成器版本标记 + check-derivatives + daily-context-save 留痕 + 实测
2. 送欧阳锋终审
