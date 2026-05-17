---
updated: 2026-05-17
active_branch: main
active_task: 黄药师 Sprint 12 Batch B（personal 域待检查）+ 老顽童消化全库 + design 域待建 + Graph RAG ✅
blockers: [老顽童消化全库中—消化完前不接新编译任务]
---

## 你是谁

**欧阳锋（Architect）**——KDO 知识工作空间的架构者。负责规则设计、审查产出、任务分配、技术决策。审而不改。

## 关键路径

| 用途 | 路径 |
|------|------|
| Vault 根目录 | `C:\Users\Administrator\Desktop\wiki\` |
| KDO CLI 源码 | `C:\Users\Administrator\Knowledge Delivery OS 0.0.1\kdo\` |
| Design Prompt Iteration | `40_outputs/capabilities/skills/design-prompt-iteration/SKILL.md` |

## 模型与环境

- **模型**：DeepSeek V4 Pro（直连 `api.deepseek.com/anthropic`）
- **运行方式**：欧阳锋 = Claude Agent（本会话）/ 黄药师 = WSL tmux `claude` / 老顽童 = Hermes agent → 飞书
- **飞书 WebSocket 僵尸连接**：cc-connect 和 Hermes 均出现过 keepalive ping timeout 导致飞书无响应。重启服务即修复。注意网络中断后 WebSocket 可能不会自动恢复。P-6 已记录复现条件。
- **关键教训**：切模型时涉及五层配置（`.bashrc` / 注册表 / systemd drop-in `env.conf` / `cc-connect config.toml` / cc-connect session 缓存）。详见 `pitfalls.md`

## 当前状态

### Sprint 进度
- v1.6 工业化手册定案，卡片层三要件
- Sprint 11 / 12 Batch A / A-2 / 13 → 全部 completed ✅
- **Sprint 12 Batch B** → entrepreneur 23/23 + panproduct-execution 18/18 + demand 11/11 完成 ✅
- **剩余**：personal(~15) / pitch(10) / aesthetic(4) / prompt(4) — 黄药师待继续
- Batch C（~30 concept 卡）待 Batch B 完成后

### 科学决策域（老顽童）→ ✅ 已完成

10 张卡全部通过欧阳锋审查。学者引用阵容：Kahneman×3, Simon×2, Taleb×2, Klein×2, Hayek, Keynes, Foucault, Janis, March, Popper, Mintzberg, Gigerenzer, Bender, Marcus — 14 位真实学者，0 稻草人。

| 评级 | 卡片 |
|------|------|
| A | width-method, consensus-iceberg, review, full-process, depth-ladder(修后), height-toolkit(修后) |
| A- | habit-shift, y-model |
| B+→A- | canvas, ai-partner |

**已发现的问题**：双三角模型在初稿中被搞反（人类三角=创造力/体系/审美，AI三角=场景/数据/基本功）。卡片内容偏"精炼搬运"，缺讲香式消化再表达。根因：老顽童入职时只读了规则，未消化全库。

### 讲香域 → ✅ 已完成（黄药师 2026-05-13）

1 framework + 10 tool + 1 concept（武器库元概念），12 张卡全部通过。

### 老顽童当前任务：消化全库

按 framework → tool → concept 顺序读完 `30_wiki/concepts/` 下 ~150 张卡。不求速成，求真懂。消化完欧阳锋出题考。消化完前不接新编译任务。

### Design 域 → 待建

- 用户需要设计参考库 + prompt 工程支持
- 架构：Eagle（图轨）+ Obsidian（文轨），双轨三层
- Design Prompt Iteration skill 已建（`40_outputs/capabilities/skills/design-prompt-iteration/SKILL.md`）
- 待用户灌入 prompt 收藏到 `00_inbox/design/`，agent 拆卡

### KDO CLI 状态
- 42 .py 文件，11,635 行，11 测试文件
- `kdo cards/lint/card-diff/review` 正常
- **Graph RAG ✅ — `kdo query` 默认引擎**：
  - `kdo query "..."` 现在默认走 LightRAG 语义+图检索（不再是关键词 grep）
  - 回退链：Graph RAG → BM25 SearchIndex → 关键词 grep
  - `kdo graph rebuild` 增量重建索引（内容变更后运行）
  - `kdo graph query "..."` 保留为调试/脚本用（支持 `--json`）
  - 219 entities, 626 chunks, 920 relations, 396 nodes, 1188 edges
  - Embedding: sklearn HashingVectorizer（char n-gram 2-4，纯 Python，零外部 API 调用）
  - LLM: 查询时不调用（keywords 已预填）；只在 `kdo enrich --llm` 时走 DeepSeek API
  - 索引持久化在 `.kdo/graph_index/`，纯本地，无 daemon，无外部依赖
- pytest 仍未安装
- 备份：KDO 源码放坚果云（单机灾备，非 git）— 待执行

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

### 2026-05-17：欧阳锋会话

- **Graph RAG 跑通**：依赖安装 + 索引重建 + 查询验证全完成。三个 bug 修复：embedding 从 PyTorch/sentence-transformers 换 sklearn HashingVectorizer（Windows Python 3.12 DLL 不兼容）、LLM 从 Kimi 换 DeepSeek API、relation 字段名修正（src_id/tgt_id + relationships key）。索引：189 entities / 529 chunks / 1095 relations / 363 nodes / 1092 edges。查询返回 chunks + entities + relationships。
- **Agent 入职必须先消化全库**：不是读讲香方法论，是读完 `30_wiki/concepts/` 下全部卡片。肚子里有货，写卡才有魂。CLAUDE.md Step 1 已更新。
- **老顽童全面评估**：B+。学术品味 A+，格式纪律 B+→A，独立判断 C+（最大短板：等指令不预判），知识广度 D（消化全库中，提到 B 就能从编译者升级到合成者）。
- **Design 域路线图**：Eagle（图轨）+ Obsidian（文轨），双轨三层。Agent 管方法论和 prompt 迭代，不管审美判断。
- **Design Prompt Iteration skill**：人描述视觉问题 → agent 翻译为 prompt 修改。四维反馈协议（画面内容/光影/构图/色彩）。
- **飞书 WebSocket 僵尸连接**：cc-connect 和 Hermes 同一天相继出现 keepalive ping timeout。重启即修复。P-6 已补复现记录。
- **双三角模型修正**：人类三角=创造力/体系/审美，AI 三角=场景/数据/基本功。初稿写反了。

见 `decisions.md`

## 下次启动

1. 读 `pitfalls.md`
2. 核查黄药师 demand 域 + personal 域进度（是否继续 Batch B）
3. 核查老顽童全库消化进度（消化完可出题考）
4. KDO Graph RAG ✅ — `kdo graph query "..."` 可用
5. 用户是否灌入了设计 prompt 素材到 `00_inbox/design/`
6. 老顽童是否修正了双三角文章初稿

## ⚠️ 会话结束前（MUST）

- [x] 更新 `updated:` 日期
- [x] 更新 `active_task` 和 `blockers`
- [x] 更新 ## 当前状态
- [x] 有新坑？追加到 `pitfalls.md`（P-6 复现记录已补）
- [x] 有决策？追加到 `decisions.md`（Agent 入职消化全库 + Design 域 + 老顽童评估）
- [ ] **禁止用 `/memory` 替代上述更新**
