---
updated: 2026-05-16_4
active_branch: main
active_task: Sprint 12 Batch B — 86 张 yt-tool 卡 v1.6 行为转化三要件回溯
blockers: []
---

## 你是谁

**黄药师（Builder）**——KDO 知识工作空间的执行者。负责内容提炼、卡片编译、质量门禁、Sprint 执行。

## 关键路径

| 用途 | 路径 |
|------|------|
| Vault 根目录 | `C:\Users\Administrator\Desktop\wiki\` |
| KDO CLI 源码 | `C:\Users\Administrator\Knowledge Delivery OS 0.0.1\kdo\` |

## 模型与环境

- **模型**：DeepSeek V4 Pro（直连 `api.deepseek.com/anthropic`）
- **运行方式**：WSL2 Ubuntu-22.04 终端 → `claude`（tmux session `claude`）
- **关键教训**：切模型时涉及五层配置（`.bashrc` / 注册表 / systemd drop-in `env.conf` / `cc-connect config.toml` / cc-connect session 缓存）。2026-05-16 切 Kimi 再切回 DeepSeek 后，漏了 env.conf + config.toml work_dir + session 缓存，导致飞书黄药师 401 + 找不到 wiki + 空响应。已修复。详见 `pitfalls.md` P-5/P-6。

## 当前状态

- v1.6 工业化手册已定案，新增卡片层三要件
- Sprint 11（认知升级框架）→ completed ✅
- Sprint 12 Batch A → completed ✅ (25/25 framework 卡已升级，欧阳锋审查通过)
- **Sprint 13** → completed ✅ (4 个 KDO 工具：lint --baseline/--diff, cards list, card-diff, review)
- **Sprint 12 Batch B** → 进行中 (23/23 entrepreneur ✅，欧阳锋抽检 2/2 通过)
- 下一域：panproduct/execution（20 张）→ demand（11）→ personal（11）→ pitch（10）→ aesthetic（5）→ prompt（4）
- 总计: 23/86 tool 卡已完成 | 剩余: 62 张（含 1 张已有 Action Triggers）
- Batch C（~30 张 concept 卡）待 Batch B 完成后启动
- 346 条 inbox 积压未清理
- Hermes 五绝全部在线（老顽童/洪七公/段王爷 Kimi API 认证修复）

## 新增工具

| 命令 | 用途 |
|------|------|
| `kdo lint --diff` | 只报告 HEAD~1 之后新增的 lint 问题 |
| `kdo lint --baseline <ref>` | 只报告指定 ref 之后新增的 lint 问题 |
| `kdo cards --type <t> --domain <d>` | 按类型/域查询卡片 |
| `kdo cards --type tool --missing "Action Triggers"` | 找出缺失指定节的卡片 |
| `kdo cards --count` | 只出数量 |
| `kdo card-diff <id> --since <ref>` | 节级别变更摘要（新增/删除/修改） |
| `kdo review --sample 5 --domain yitang` | 随机抽检卡片，输出理解门禁摘要 |

## 最近决策

见 `decisions.md`

## 下次启动

1. 读 `pitfalls.md`
2. 读 `70_product/tasks/sprint-12-backfill-card-behavioral-requirements.md`
3. 继续 active_task

## ⚠️ 会话结束前（MUST）

- [ ] 更新 `updated:` 日期
- [ ] 更新 `active_task` 和 `blockers`
- [ ] 更新 ## 当前状态（完成数、剩余数、新发现的问题）
- [ ] 有新坑？追加到 `pitfalls.md`
- [ ] 有决策？追加到 `decisions.md`
- [ ] **禁止用 `/memory` 替代上述更新**——`/memory` 不是项目公共记忆。
