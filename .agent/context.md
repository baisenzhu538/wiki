---
updated: 2026-05-16_2
active_branch: main
active_task: Sprint 12 Batch B — 85 张 yt-tool 卡 v1.5 行为转化三要件回溯
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

- **模型**：DeepSeek V4 Pro（通过 Kimi Code API `/anthropic` 兼容层）
- **运行方式**：WSL2 Ubuntu-22.04 终端 → `claude`（tmux session `claude`）
- **关键教训**：WSL 里不要试图切 Kimi 模型。WSL → Windows exe 的环境变量传递不可靠，Kimi env vars 会被忽略。

## 当前状态

- v1.5 工业化手册已定案，新增卡片层三要件：
  1. **Critique 外部攻击**（找反例/边界/失效条件）
  2. **Synthesis 不要写场景**（写跨域同构关系，不写应用场景）
  3. **Action Triggers**（何时触发该知识的可观测信号）
- Sprint 11（认知升级框架）→ completed ✅
- **Sprint 12 Batch A** → completed ✅ (25/25 framework 卡已升级，欧阳锋审查通过)
- **Sprint 12 Batch B** → pending (85 张 tool 卡，待启动)
- Batch C（~30 张 concept 卡）待 Batch B 完成后启动
- 346 条 inbox 积压未清理，591 条 lint 警告待处理

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
