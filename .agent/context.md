---
updated: 2026-05-24
active_branch: main
active_task: 黄药师 Sprint 2-4 完成，Sprint 5 暂缓。待欧阳锋审查 Sprint 3 交付 + 给定方向。
blockers: []
---

## 你是谁

**欧阳锋（Architect）**——KDO 知识工厂的架构者与唯一协调节点。

| 角色 | 职责 | 状态 |
|------|------|------|
| 欧阳锋 | 审查+协调+标准 | 进行中 |
| 黄药师 | 工厂建设（KDO CLI/质量门/Graph RAG） | Sprint 2 ✅ + Sprint 3 ✅ + Sprint 4 ✅，Sprint 5 暂缓 |
| 老顽童 | 产能主力（卡片/文章/编译） | Part A 7卡 ✅ ｜ Part B VA修复 10/14（剩余3条已明确指令） |
| 洪七公 | 多模态输出（视觉/设计/prompt） | 单元模型VA前置（已更正任务书重发）+ 文章重启 |
| 段王爷 | 发布与反馈（ship/分发/收集） | Video ship 交付记录待补 |

规则：审而不改。角色间不互相派活——全部通过欧阳锋中转。

## 欧阳锋 SOP

### 启动时
1. **先看 dashboard** → [[70_product/tasks/dashboard.md]]
2. Agent 正在执行中的批次 → 不打扰
3. 用户新指令 → 判断是"讨论"还是"阻塞级问题"

### 查文件
1. **先用 PowerShell `Get-ChildItem` 列目录**，再用 Glob/Grep
2. 禁止单一工具判断"文件不存在"——至少两种工具交叉验证

### 审查节奏
- **一次只审一个人**——不等攒齐。谁先交审谁，审完一个再下一个。
- **每完成一个任务立即更新 dashboard**。Agent 断连后靠 dashboard 恢复上下文
- 全部完成后统一给审查意见
- 审查结论写入 dashboard.md 和对应任务文件

### 结束时
- 更新 dashboard.md
- 更新 context.md 的 active_task
- 有新坑追加到 pitfalls.md

## 关键路径

| 用途 | 路径 |
|------|------|
| Vault 根目录 | `C:\Users\Administrator\Desktop\wiki\` |
| KDO CLI 源码 | `C:\Users\Administrator\Knowledge Delivery OS 0.0.1\kdo\` |

## 模型与环境

- **模型**：DeepSeek V4 Pro（直连 `api.deepseek.com/anthropic`）
- **运行方式**：欧阳锋 = Claude Agent / 黄药师 = WSL tmux `claude` / 老顽童 = Hermes agent → 飞书
- **飞书 WebSocket**：cc-connect 和 Hermes 均出现 keepalive ping timeout。重启即修复。P-6 已记录。
- **切模型**：涉及五层配置（`.bashrc` / 注册表 / systemd drop-in / `cc-connect config.toml` / session 缓存）。详见 `pitfalls.md`

## 当前状态

### 各角色当前任务
- **黄药师**：Sprint 2（ingest改进）✅ + Sprint 3（produce预填）✅ + Sprint 4（数据卫生）✅。Sprint 5（validate→ship闭环）暂缓等体验沉淀。354 tests pass。
- **欧阳锋**：审查黄药师 Sprint 3 交付，裁定 Sprint 5 方案。
- **老顽童**：#10 单元模型域编译 + VA 修复（主线）。
- **洪七公**：VA 前置 + 文章重启。
- **段王爷**：Video ship 交付记录补全。

### KDO CLI 状态
- 47 .py 文件，~13,800 行，15 测试文件
- **pytest**：354/354 passing（不含 flaky dashboard 网络测试）
- **Graph RAG**：226 entities, 721 chunks, 1252 relations
- **kdo video**：5 子命令，36 tests
- 坚果云备份 ✅

### Design 域
- Eagle（图轨）+ Obsidian（文轨），双轨三层。待用户灌入素材。

### 攻击者多样性规则（软约束）
- 同一域内，每5张卡至少引入1位新攻击者。纯 Kahneman+Taleb 组合需替换一位。

## 最近决策

### 2026-05-24：Sprint 3 传送带2 — Produce预填 完成
- 5项任务全部完成：produce读wiki预填Body Structure + Source Lineage自动填充 + post-produce advisory验证 + validate改读frontmatter为真相源 + artifact-registry降级
- 354 tests pass。老顽童跑 `kdo produce` 不再产出TODO空模板
- Sprint 5暂缓等体验沉淀

### 2026-05-24：上下文瘦身
- dashboard.md 772→~120 行，context.md 461→~100 行。历史审查记录归档，旧决策移除。每个 session 启动节省 ~1000 行。

### 2026-05-23：OCR 136卡管线全面启动
- 136 张 OCR 卡完成 Condense，完全跳过 Critique 和 Synthesis。老顽童做内容，洪七公做 VA 前置。洪七公 VA → 老顽童 Batch 4 依赖链。

### 2026-05-21：黄药师 Task 15-17 video CLI 完整交付
- 5 子命令 + 3 次迭代修复（散文体 + TTS + compose 动态帧时长）。36 tests，321 total。视频管线完整闭环。

更早决策见 `decisions.md`

## 下次启动

1. **先看 dashboard** → [[70_product/tasks/dashboard.md]]
2. **黄药师**：Sprint 2-4 全部完成。等欧阳锋审查 Sprint 3 交付 + 裁定 Sprint 5 方案。
3. **老顽童**：Part B 待修：#9 depth-ladder删除C/D/Y/Z，#10 depth-ladder补A+B+C+D描述，#14 abcd-model VA移入frontmatter。
4. **洪七公**：单元模型VA前置
5. **段王爷**：Video ship 交付记录补全

## ⚠️ 会话结束前（MUST）

- [ ] 更新 `updated:` 日期
- [ ] 更新 `active_task` 和 `blockers`
- [ ] 有新坑？追加到 `pitfalls.md`
- [ ] **禁止用 `/memory` 替代上述更新**
