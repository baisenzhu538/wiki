---
updated: 2026-05-25
active_branch: main
active_task: 黄药师 Sprint 2-4 完成，Sprint 5 暂缓。待欧阳锋审查 Sprint 3 交付 + 给定方向。Token 暴涨排查完成 → [[70_product/tasks/token-spike-investigation-20260525]]。
blockers: []
---

> ⚠️ **角色中立文件** — 只放共享状态。不写 "你是谁" 类身份描述。
> 各角色的身份定义、SOP、启动指令在 `.agent/<role>-context.md`。
> 看到 "你是谁" 段落 → 删掉，移到对应角色文件。不要在这里写。

## 角色部署

| 角色 | 运行位置 | 工具 |
|------|---------|------|
| 欧阳锋（Architect） | Obsidian Claudian 插件 | 协调/审查/拍板 |
| 黄药师（Builder） | WSL tmux `claude` | KDO CLI 开发 |
| 老顽童（Producer） | Hermes agent → 飞书 | 卡片/文章量产 |
| 洪七公（Multimodal） | Hermes agent → 飞书 | 视觉/设计/prompt |
| 段王爷（Publisher） | Hermes agent → 飞书 | 发布/反馈/版本 |

> 角色专属 context 见 `.agent/ouyangfeng-context.md`、`.agent/huangyaoshi-context.md`、`.agent/laowantong-context.md`、`.agent/hongqigong-context.md`、`.agent/duanwangye-context.md`。

## 关键路径

| 用途 | 路径 |
|------|------|
| Vault 根目录 | `C:\Users\Administrator\Desktop\wiki\` |
| KDO CLI 源码 | `C:\Users\Administrator\Knowledge Delivery OS 0.0.1\kdo\` |

## 模型与环境

- **模型**：DeepSeek V4 Pro（直连 `api.deepseek.com/anthropic`）
- **飞书 WebSocket**：cc-connect 和 Hermes 均出现 keepalive ping timeout。重启即修复。P-6 已记录。
- **切模型**：涉及五层配置（`.bashrc` / 注册表 / systemd drop-in / `cc-connect config.toml` / session 缓存）。详见 `pitfalls.md`

## 当前共享状态

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

### 2026-05-24：Sprint 3 传送带 — Produce预填 完成
- 5项任务全部完成：produce读wiki预填Body Structure + Source Lineage自动填充 + post-produce advisory验证 + validate改读frontmatter为真相源 + artifact-registry降级
- 354 tests pass。老顽童跑 `kdo produce` 不再产出TODO空模板
- Sprint 5暂缓等体验沉淀

### 2026-05-24：上下文瘦身
- dashboard.md 772→~120 行，context.md 461→~100 行。历史审查记录归档，旧决策移除。

### 2026-05-23：OCR 136卡管线全面启动
- 136 张 OCR 卡完成 Condense，完全跳过 Critique 和 Synthesis。老顽童做内容，洪七公做 VA 前置。洪七公 VA → 老顽童 Batch 4 依赖链。

### 2026-05-21：黄药师 Task 15-17 video CLI 完整交付
- 5 子命令 + 3 次迭代修复（散文体 + TTS + compose 动态帧时长）。36 tests，321 total。视频管线完整闭环。

更早决策见 `decisions.md`

## ⚠️ 会话结束前（MUST）

- [ ] 更新 `updated:` 日期
- [ ] 更新 `active_task` 和 `blockers`
- [ ] 有新坑？追加到 `pitfalls.md`
- [ ] **禁止用 `/memory` 替代上述更新**
