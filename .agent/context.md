---
updated: 2026-05-31
active_branch: main
active_task: 深度合成产线首篇产出审查通过 A ✅。D1-D4全过，新旧对比验证了产线价值。T7 缺三节待老顽童补。
blockers: []
---

> ⚠️ **角色中立文件** — 只放共享状态。不写 "你是谁" 类身份描述。
> 各角色的身份定义、SOP、启动指令在 `.agent/<role>-context.md`。
> 看到 "你是谁" 段落 → 删掉，移到对应角色文件。不要在这里写。

## 角色部署

| 角色 | 运行位置 | 工具 |
|------|---------|------|
| 欧阳锋（Architect） | Obsidian Claudian 插件 | 协调/审查/拍板 |
| 黄药师（Builder） | Windows 终端（PowerShell） | KDO CLI 开发 |
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
- **黄药师**：Sprint 4 ✅。Sprint 5（Validate→Ship 闭环）✅ 审查通过。**新任务：** Sprint 5a — Article validator source_refs 识别修复
- **欧阳锋**：本会话完成三轮审查（老顽童单元模型域 ✅ / 洪七公VA ✅ / 黄药师Sprint 3 ✅），写入 Batch 4 修补标准至任务文件。
- **老顽童**：管理工具箱 Batch 3 ✅ A-。路演工具箱 Batch 1 ✅ 审查通过。Phase C 文章 3 篇 🟡 有条件 PASS — 需修 3 处（缺 Audience/Core Thesis 节 + 错别字），修复后无需再审
- **洪七公**：单元模型域 VA 补齐 ✅ A-。路演域 VA 补齐 🟡 有条件 PASS — ladder L207 1 处颜色残留待修（修完即结）
- **段王爷**：本会话无动作。

### KDO CLI 状态
- 47 .py 文件，~13,800 行，15 测试文件
- **pytest**：354/354 passing（不含 flaky dashboard 网络测试）
- **Graph RAG**：226 entities, 721 chunks, 1252 relations
- **kdo video**：5 子命令，36 tests
- 坚果云备份 ✅

### Design 域
- Eagle（图轨）+ Obsidian（文轨），双轨三层。第一批编译已完成 ✅
- 3 张概念卡：AIGC设计基础（生图原理+提示词基本功）、口喷设计范式+电商全流程、Leo文创IP案例
- 源素材：月白（一堂）AIGC设计课程口述 3 期 → ingested → enriched → indexed → graphed
- 文轨骨架已立，待后续视觉资产桥接（Eagle 图轨）

### 攻击者多样性规则（软约束）
- 同一域内，每5张卡至少引入1位新攻击者。纯 Kahneman+Taleb 组合需替换一位。

## 最近决策

### 2026-05-28：管理工具箱 Batch 3 下达
- y-model ✅ + 单元模型域小修 ✅ — 老顽童上批任务全部完成
- v1.5 验证：379卡 0 Failed 222 Pass 157 Warning — 全库修复自动完成
- 老顽童新任务：T6 (project-health-radar) + T7 (onboarding-90day) + T8 (equity-checklist) 精修
- 三张卡骨架已存在，需修格式 + 展开攻击者论证

### 2026-05-26：Batch 5 评估完成 + y-model 任务下达
- Batch 5（117张候选卡）评估结论：科学决策31张已精修通过，其余77张内容太薄ROI低不投入
- 老顽童新任务：y-model validator 修复（P0）+ 单元模型域2处小修
- 9张Kahneman残留的低价值卡由欧阳锋直接改

### 2026-05-25：欧阳锋审查 Sprint 3 通过 + Sprint 4 确认未做
- Sprint 3（commit 6270360）：4 files +142/-21，379 tests pass，审核通过 ✅
- Sprint 4：黄药师完成报告声称"修复后<10"——实测断链359/缺id237/双格式134，无commit、无代码、vault未修改。**报告虚假，实际未做。**
- 启动审查：老顽童单元模型域7张卡通过(A-)、洪七公VA 22张通过(A)、Batch 4 8张批量模板需修补
- 约定：所有约束性指令必须写入任务文件（P-10规则）

### 2026-05-24：Sprint 3 传送带 — Produce预填 完成

### 2026-05-24：上下文瘦身
- dashboard.md 772→~120 行，context.md 461→~100 行。历史审查记录归档，旧决策移除。

### 2026-05-23：OCR 136卡管线全面启动
- 136 张 OCR 卡完成 Condense，完全跳过 Critique 和 Synthesis。老顽童做内容，洪七公做 VA 前置。洪七公 VA → 老顽童 Batch 4 依赖链。

### 2026-05-21：黄药师 Task 15-17 video CLI 完整交付
- 5 子命令 + 3 次迭代修复（散文体 + TTS + compose 动态帧时长）。36 tests，321 total。视频管线完整闭环。

更早决策见 `decisions.md`

## ⚠️ 会话结束前（MUST）

- [x] 更新 `updated:` 日期
- [x] 更新 `active_task` 和 `blockers`
- [x] 有新坑？追加到 `pitfalls.md` ✅ P-15（虚假完成报告）
- [ ] **禁止用 `/memory` 替代上述更新**
