---
updated: 2026-05-18
active_branch: main
active_task: 黄药师 Batch C（concept 卡：20/30 v1.5 升级完成 + pytest ✅ + 坚果云备份 ✅）+ 老顽童补 related 边 → 出文章 → 提案新域
blockers: []
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
- **Sprint 12 Batch B** → entrepreneur 23/23 + panproduct-execution 18/18 + demand 11/11 + personal/pitch/aesthetic/prompt 全部完成 ✅
- **Batch C**（~30 concept 卡）→ **15/30 v1.5 升级完成**
  - ✅ yt-concept-weapon-arsenal（master — Dreyfus+Polanyi, 跨 3 域）
  - ✅ yt-concept-ai-guard-brain（yitang+ai — Carr+Stiegler, 跨 4 域）
  - ✅ yt-concept-context-engineering（yitang+ai — Simon+Shannon/Weaver+Scott, 跨 4 域）
  - ✅ yt-management-scientific-decision（yitang — Klein+Taleb, 跨 3 域）
  - ✅ yt-management-basic-skills（yitang — Mintzberg+Argyris, 跨 3 域）
  - ✅ yt-management-business-formula（yitang — Hayek+Weick, 跨 3 域）
  - ✅ yt-management-founder-role（yitang — Pfeffer+Drucker, 跨 3 域）
  - ✅ yt-management-goal-management（yitang — Deming+Muller, 跨 3 域）
  - ✅ yt-management-leadership-levels（yitang — Kegan+Kellerman, 跨 3 域）
  - ✅ yt-management-company-culture（yitang — Schein+Martin, 跨 3 域）
  - ✅ yt-management-conversion-hacking（yitang — Sutherland+Ariely, 跨 3 域）
  - ✅ yt-management-finance-basics（yitang — Johnson&Kaplan+Jensen, 跨 3 域）
  - ✅ yt-management-scientific-hiring（yitang — Gladwell+Bohnet, 跨 3 域）
  - ✅ yt-management-strategy-meeting（yitang — Rumelt+Porter, 跨 3 域）
  - ✅ yt-management-team-knowledge（yitang — Nonaka&Takeuchi+Snowden, 跨 3 域）
  - ✅ yt-management-onboarding（yitang — Van Maanen&Schein+Edmondson, 跨 3 域）
  - ✅ yt-management-partnership-equity（yitang — Coase+Williamson, 跨 3 域）
  - ✅ yt-management-project-management（yitang — Flyvbjerg+Goldratt, 跨 3 域）
  - ✅ yt-management-scientific-meetings（yitang — Useem+Doyle&Straus, 跨 3 域）
  - ✅ yt-concept-peas-insight（master — Berlin+Klein 已有，补跨域引用）
  - 待续：~10 张 concept 卡（KF-022 每会话 ≤5）
  - 全部 20 张通过 `kdo lint --baseline HEAD`
- **老顽童后续** → 已分配：[[70_product/tasks/laowantong-next-tasks.md]]（①补related边 ②双三角文章v2 ③提案新域）

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
- **pytest ✅**：182/182 passing。修复 7 个测试（smoke test / security ship tests + --skip-validation / improve_apply 加 feedback / validation `or` pattern 空 list bug）
- **备份 ✅**：KDO 源码 zip（删 .git/__pycache__/build）→ `C:\Users\Administrator\Nutstore\1\我的坚果云\kdo-source-backup-20260517.zip`（272.6 KB）

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

### 2026-05-18：黄药师 Batch C 会话（Batch 5）

- **Batch 5（5 张）**：新人落地（Van Maanen&Schein+Edmondson）、合伙股权（Coase+Williamson）、项目管理（Flyvbjerg+Goldratt）、科学开会（Useem+Doyle&Straus）、PEAS核心洞察（Berlin+Klein 已有，补跨域引用）
- **累计 20/30**：学者阵容 40 位，0 稻草人
- **管理域 16 张全部完成** ✅
- **学者新增**：Van Maanen, Schein (again, role-specific), Edmondson, Coase, Williamson, Flyvbjerg, Goldratt, Useem, Doyle, Straus

### 2026-05-18：黄药师 Batch C 会话（Batch 3-4）

- **Batch 3（5 张）**：业务公式（Hayek+Weick）、一号位（Pfeffer+Drucker）、目标管理（Deming+Muller）、管理段位（Kegan+Kellerman）、公司文化（Schein+Martin）
- **Batch 4（5 张）**：转化率黑客（Sutherland+Ariely）、财务入门（Johnson&Kaplan+Jensen）、科学招聘（Gladwell+Bohnet）、战略会（Rumelt+Porter）、团队知识管理（Nonaka&Takeuchi+Snowden）
- **累计 15/30**：学者阵容 30 位，0 稻草人。每卡 ≥2 不要用场景、≥3 Action Triggers、≥3 跨域引用、estimated_tokens ≤3500
- **学者新增**：Rory Sutherland, Dan Ariely, H. Thomas Johnson, Robert S. Kaplan, Michael C. Jensen, Malcolm Gladwell, Iris Bohnet, Richard Rumelt, Michael Porter, Ikujiro Nonaka, Hirotaka Takeuchi, Dave Snowden

### 2026-05-17：黄药师 Batch C 会话（晚上）

- **concept 卡 v1.5 升级 5/30**：武器库（Dreyfus+Polanyi）、守脑如玉（Carr+Stiegler）、上下文工程（Simon+Shannon+Scott）、科学决策（Klein+Taleb）、基本功认知（Mintzberg+Argyris）。学者阵容 12 位，0 稻草人。每卡 ≥3 跨域引用、≥2 不要用场景、≥3 Action Triggers。
- **pytest ⚡ 182/182 all green**：fix 7 tests。Ship validation gate → smoke/security tests 加 `--skip-validation`；validation.py `or` 链 `[]` 视为 falsy → 改用 `is not None` 判断；improve_apply tests 缺 feedback entries → 补 `corrections` kind feedback。
- **坚果云备份**：KDO 源码（去 .git/__pycache__/build）→ zip 272 KB → `Nutstore\1\我的坚果云\`。坚果云实际同步 `C:\Users\Administrator\Knowledge Delivery OS 0.0.1` 本身（已配置为 sandbox），zip 是额外快照。
- **concept 卡跨域引用策略**：master 域有 `yt-concept-weapon-arsenal`，personal 域有 `yt-model-personal-pitch-toolkit`——作为跨域桥梁卡使用。每张 yitang-only concept 卡至少追加这 2 张的关联引用即可满足 ≥3 域要求。

### 2026-05-17：欧阳锋会话（上午）

- **Graph RAG 跑通**：依赖安装 + 索引重建 + 查询验证全完成。三个 bug 修复：embedding 从 PyTorch/sentence-transformers 换 sklearn HashingVectorizer（Windows Python 3.12 DLL 不兼容）、LLM 从 Kimi 换 DeepSeek API、relation 字段名修正（src_id/tgt_id + relationships key）。索引：219 entities / 626 chunks / 920 relations / 396 nodes / 1188 edges。
- **`kdo query` 已合并为 Graph RAG 默认引擎**：`kdo query "..."` 现在走 LightRAG 语义+图检索 → BM25 → 关键词三层回退。`kdo graph query` 保留为调试/脚本用（--json）。代码改在 `delivery.py`。
- **Agent 入职必须先消化全库**：不是读讲香方法论，是读完 `30_wiki/concepts/` 下全部卡片。肚子里有货，写卡才有魂。CLAUDE.md Step 1 已更新。
- **老顽童全面评估**：消化前 B+，消化后三道考试全部 A/A+。知识广度 D→B+，独立判断 C+→A-，学术品味 A+ 维持。**Blocker 已解除，可接新编译任务。**
- **老顽童考试 Q3 金句**："人脑不是计算器，是模式匹配器。你逼它做 Excel 分析，它就偷偷用偏见替你填答案。——Kahneman" 传播力+准确性双高，建议收入卡中。
- **Design 域路线图**：Eagle（图轨）+ Obsidian（文轨），双轨三层。Agent 管方法论和 prompt 迭代，不管审美判断。
- **Design Prompt Iteration skill**：人描述视觉问题 → agent 翻译为 prompt 修改。四维反馈协议（画面内容/光影/构图/色彩）。
- **飞书 WebSocket 僵尸连接**：cc-connect 和 Hermes 同一天相继出现 keepalive ping timeout。重启即修复。P-6 已补复现记录。
- **双三角模型修正**：人类三角=创造力/体系/审美，AI 三角=场景/数据/基本功。初稿写反了。
- **黄药师 Batch B all done / 老顽童消化全库 done / Graph RAG done / blockers 全部清除**
- **新任务已写**：[[70_product/tasks/sprint-12-batch-c-concept-cards.md]] + [[70_product/tasks/laowantong-next-tasks.md]]

见 `decisions.md`

## 下次启动

1. 读 `pitfalls.md`
2. 继续 Batch C concept 卡 — 下个会话从第 16 张开始（KF-022 ≤5/会话），待升级 ~15 张
3. pytest 182/182 ✅ — 后续修改代码后必须重跑
4. 坚果云备份 ✅ — KDO 源码已在坚果云（sandbox + zip 快照）
5. 核查老顽童进度（补 related 边 / 双三角文章 v2 / 提案新域）
6. 用户是否灌入了设计 prompt 素材到 `00_inbox/design/`

## ⚠️ 会话结束前（MUST）

- [x] 更新 `updated:` 日期
- [x] 更新 `active_task` 和 `blockers`
- [x] 更新 ## 当前状态
- [x] 有新坑？追加到 `pitfalls.md`（P-6 复现记录已补）
- [x] 有决策？追加到 `decisions.md`（Agent 入职消化全库 + Design 域 + 老顽童评估）
- [ ] **禁止用 `/memory` 替代上述更新**
