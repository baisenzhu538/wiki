---
updated: 2026-05-21
active_branch: main
active_task: 全员待命。老顽童 9/9 ✅。黄药师 Task 1-17 全部完成 ✅。视频试点已关闭。洪七公双三角VA待审阅。段王爷 Publisher 反馈闭环初具雏形。
blockers: []
---

## 你是谁

**欧阳锋（Architect）**——KDO 知识工厂的架构者与唯一协调节点。

**五角色分工**：
| 角色 | 职责 | 状态 |
|------|------|------|
| 欧阳锋 | 审查+协调+标准 | 进行中 |
| 黄药师 | 工厂建设（KDO CLI/质量门/Graph RAG） | Task 1-17 全部完成 ✅，待命 |
| 老顽童 | 产能主力（卡片/文章/编译） | ④ Batch 2 T5 制作中 |
| 洪七公 | 多模态输出（视觉/设计/prompt） | ✅ 已激活：角色定义+VA 完成 |
| 段王爷 | 发布与反馈（ship/分发/收集） | 待激活 |

规则：审而不改。角色间不互相派活——全部通过欧阳锋中转。

## 欧阳锋 SOP（自己的工作流）

### 启动时
1. **先看 dashboard** → [[70_product/tasks/dashboard.md]]，了解全局状态
2. Agent 正在执行中的批次 → 不打扰，让其跑完
3. 用户新指令 → 判断是"讨论"还是"阻塞级问题"。讨论不打断 agent

### 查文件
1. **先用 PowerShell `Get-ChildItem` 列目录**，再用 Glob/Grep 搜索
2. 禁止单一工具判断"文件不存在"——Glob 可能漏子目录

### 审查节奏
- **每完成一个任务立即更新 dashboard**，不等批次。Agent 随时可能断连，任务文件是唯一上下文锚点
- 全部完成后统一给审查意见
- 审查结论写入 dashboard.md 和对应任务文件

### 状态更新
- **实时更新**：Agent 每完成一个 → 立即更新 dashboard
- 飞书 bot 通过 cc-connect/Hermes 连接，WebSocket 经常超时断连（P-6）
- Agent 重连后靠 dashboard 恢复上下文——延迟更新 = 重复劳动

### 结束时
- 更新 dashboard.md
- 更新 context.md 的 active_task
- 有新坑追加到 pitfalls.md

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
- **Batch C**（~30 concept 卡）→ **29/30 v1.5 升级完成**
  - (前 20 张：yt-concept ×4 + yt-management ×16)
  - ✅ yt-personal-pan-product-concepts（yitang/personal — Epstein+Drucker, 跨 3 域）
  - ✅ yt-personal-pan-product-aesthetics（yitang/personal — Norman+Bourdieu, 跨 3 域）
  - ✅ yt-personal-pan-product-exploration（yitang/personal — Dewey+Lave&Wenger, 跨 3 域）
  - ✅ yt-personal-pan-product-practice（yitang/personal — Christensen+Mintzberg, 跨 3 域）
  - ✅ yt-personal-pan-product-tools（yitang/personal — Suchman+Schön, 跨 3 域）
  - ✅ yt-personal-pan-product-02/落地篇（yitang/personal — Pirsig+Newport, 跨 3 域）
  - ✅ yt-research-weaponry-course（yitang/entrepreneur — Feynman+Geertz, 跨 3 域）
  - ✅ yt-research-action-camp-launch（yitang/entrepreneur — Schön+Dewey, 跨 3 域）
  - ✅ yt-system-course-catalog（yitang/system — Perkins+Illich, 跨 3 域）
  - 29 张通过 `kdo lint --baseline HEAD`（0 new errors）
  - Batch C 实质上已完成（~1 张不需要升级或非 concept 卡范围）
  - ⚠️ 黄药师角色重对齐 → 不接量产。但用户指令优先，先做完剩余
- **老顽童后续** → 全队列写定：[[70_product/tasks/laowantong-next-tasks.md]]
  - ① 补 related 边 ✅ | ② 双三角文章 v2 ✅ | ③ 管理工具箱 Batch 1 ✅（F1+T1+T2 全 A）
  - ④ 管理工具箱 Batch 2（进行中：T3+T4+T5）
  - ⑤ 设计域 7 张卡（素材已就位 `00_inbox/design/`）
  - ⑥ v1.5 全库修复 89 卡（scaffold 加速）
  - ⑦ 管理工具箱 Batch 3（T6+T7+T8 收官）
- **黄药师后续** → 全队列写定：[[70_product/tasks/huangyaoshi-next-tasks.md]]
  - Task 1: `kdo scaffold`（P0，加速老顽童 89 卡流水线）
  - Task 2: 设计域转录稿清理工具（P1，规则引擎去噪+分段）
  - Task 3: `kdo validate --v15 --watch`（P2，文件保存自动重检）

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

### 调研方法论域（老顽童）→ ✅ 已完成

8 张卡全部通过欧阳锋审查（F2+T5+C1，含 3 张升级 + 5 张新建）。学者引用阵容：Simon, Weick, Ellsberg, Benkler, Tetlock, Becker, Zaltman, Bourdieu, Feyerabend, Kuhn, Taleb, Popper, Porter, Christensen, Feynman, Lakoff — 16 位真实学者，0 稻草人。

| 评级 | 卡片 |
|------|------|
| A+ | hypothesis-test（Feyerabend+Kuhn — 全库最具哲学严密性的攻击段落之一）、user-jtbd（Zaltman ZMET + Bourdieu 惯习理论，非显而易见） |
| A | osl-framework（Simon+Weick）、intelligence-map（Ellsberg+Benkler）、expert-interview（Tetlock+Becker）、industry-canvas（Taleb+Popper）、competitor-toolkit（Porter+Christensen）、mindset（Feynman+Lakoff） |

**全量 checklist 通过**：8/8 [Critique] 节、8/8 外部攻击 ≥2、8/8 不要用场景 ≥2、8/8 Action Triggers ≥3。

### 老顽童状态（产能主力）

- **7 张 master 卡全部通过 ✅**：[[70_product/tasks/proposal-new-domain-master-meta-capabilities.md]] 提案的 7 张卡全部写成，审查 A，可直接入库
  - #1 master-cognitive-bias-checklist（A）| #2 master-decision-hygiene（A）| #3 master-first-principles（A）
  - #4 master-systems-thinking（A）| #5 master-antifragile-checklist（A，frontmatter 已修）| #6 master-ai-info-literacy（A+）| #7 master-knowledge-compound（A-）
- PEAS 洞察 concept 卡（A+）附赠完成
- 边界定义文件已写（`70_product/tasks/master-7-cards-layer-and-boundary.md`）
- **修复验证 ✅**：#5 card_type→tool ✅ | #3 SpaceX 例子三层注解 + 类比思维反例 ✅
- **调研方法论域 → ✅ 已完成**：8 张卡（F2+T5+C1）全部 A 级，库存 +8
- **科学决策审计 → ⛔ 已叫停**。10 张卡 A 级已通过，不返工
- 评估：知识广度 A，独立判断 A→A+（SpaceX 自我纠错），学术品味 A+，跨域合成 A

### 黄药师状态（基础设施唯一负责人）

- **不接卡片量产**。专注 KDO CLI、方法论建设、质量门、Graph RAG。
- **Task 1-17 全部完成 ✅**：scaffold → clean-transcript → validate watch → watch 解耦 → scaffold 插入修正 → task 自动化 → graph incremental → graph stats → Graph RAG 深化 → Quality Gate v2 → skill-dir 审查 → Build 系统 → scaffold 四缺陷修复 → video CLI → video render 修复 → video 遗留缺陷
- **KDO CLI 新增命令**：`kdo scaffold`, `kdo clean-transcript`, `kdo validate --v15 --watch`, `kdo build`, `kdo video`（5 子命令）
- pytest：321/321 passing（+1 flaky dashboard 预存）
- **视频管线工具链完整**：`kdo video init → validate → render --audio → render --compose → ship`
- 坚果云备份 ✅ | Graph RAG 索引 ✅（226 entities, 1252 relations）
- 待命。下一个工单等待欧阳锋分配。

### Design 域 → 待建

- 用户需要设计参考库 + prompt 工程支持
- 架构：Eagle（图轨）+ Obsidian（文轨），双轨三层
- Design Prompt Iteration skill 已建（`40_outputs/capabilities/skills/design-prompt-iteration/SKILL.md`）
- 待用户灌入 prompt 收藏到 `00_inbox/design/`，agent 拆卡

### KDO CLI 状态
- 47 .py 文件，~13,500 行，15 测试文件
- **pytest ✅**：321/321 passing（1 flaky dashboard 预存）
- **Graph RAG ✅**：226 entities, 721 chunks, 1252 relations
- **kdo video**：5 子命令（init/validate/render/ship），36 tests
- **备份 ✅**：坚果云自动同步

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
| `kdo lint --accept-baseline` | 将当前 warning 快照存入 baseline.json，后续 lint 只显示新增 |
| `kdo lint --structure-report` | 全库卡片按 H2 结构聚类，输出类型分布摘要 |
| `kdo scaffold --card <id>` | 为缺失 v1.5 信号的卡生成升级骨架（攻击者建议+TODO占位） |
| `kdo scaffold --batch A` | 整批 dry-run（A=全信号缺失, B=缺攻击, C=缺AT, D=研究降级, E=warnings） |
| `kdo scaffold --from-plan --write` | 从升级计划整批写入骨架 |
| `kdo clean-transcript <file>` | ASR 转录稿清理（去噪+去口头禅+分段+术语标注） |
| `kdo validate --v15 --watch` | 文件保存自动重检（2s 防抖，Ctrl+C 退出） |
| `kdo video init <article>` | 创建视频项目骨架（_spec.md + 模板） |
| `kdo video validate <dir>` | 三层质量门（L1 结构/L2 内容/L3 管线） |
| `kdo video render --audio <dir>` | TTS 口播生成（edge-tts，5 段 mp3） |
| `kdo video render --compose <dir>` | ffmpeg 帧+音频合成（动态帧时长） |
| `kdo video ship <dir>` | 交付：draft→final + delivery record |

## 最近决策

### 2026-05-21：黄药师 Task 15-17 全部完成 ✅ — kdo video CLI 完整交付

- **Task 15 `kdo video` CLI**（`e8b9265`）：5 子命令（init/validate/render/ship），24 tests，310 total
- **Task 16 render 修复**（`fa66855`）：散文体脚本支持 + edge-tts TTS 集成，32 tests，317 total
- **Task 17 遗留缺陷**（`dee0f83`）：Seg 5 TTS 558.5s→70.5s + compose 动态帧时长分配，36 tests，321 total
- **视频管线完整**：`kdo video init → validate → render --audio → render --compose → ship`
- **段王爷 Publisher 反馈闭环初具雏形**：ship 时发现 `stages` 字典未同步，已记录为 P3 顺手修

### 2026-05-19：黄药师三件全部完成 ✅（scaffold + 转录稿清理 + validate watch）

- **Task 1 `kdo scaffold`**（[[70_product/tasks/kdo-scaffold-v15.md]]）：`quality.py` +210 行，4 类骨架生成器，同域攻击者智能建议，--from-plan 覆盖 115 卡 0 崩溃
- **Task 2 `kdo clean-transcript`**（[[70_product/tasks/huangyaoshi-next-tasks.md]]）：`transcript.py` 新模块 ~120 行，规则引擎去噪（回声/网络/互动行 + 填充词 + 断句合并 + 术语标注），两份设计转录稿已验证
- **Task 3 `kdo validate --v15 --watch`**：`quality.py` +70 行，纯 stdlib `os.stat` 轮询，2s 防抖，Ctrl+C 退出，--domain 过滤，--json 输出
- **pytest**：228/229 pass（1 flaky dashboard 预存），+24 新 tests（scaffold 17 + transcript 7）

### 2026-05-19：黄药师 `kdo scaffold` 完成 ✅

- **任务文件**：[[70_product/tasks/kdo-scaffold-v15.md]]
- **核心实现**：`kdo/commands/quality.py` +210 行，`kdo/cli.py` +10 行
  - `_scaffold_card(card_path, concepts_dir, write, hints)` — 主逻辑：读卡→诊断→生成骨架
  - `_get_attacker_suggestions(domains, existing, concepts_dir)` — 同域扫描攻击者名→去重→频次排序→top 3
  - `_generate_critique_full` / `_generate_attack_only` / `_generate_dont_use` / `_generate_triggers` — 四类骨架生成器
- **CLI 接口**：`kdo scaffold --card <id>` / `--batch A|B|C|D|E` / `--from-plan [--write] [--no-hints]`
- **智能攻击者建议**：从同域卡片中实际提取（非硬编码），排除已用攻击者，按频次排序推荐 top 3
- **全库验证**：`--from-plan` 覆盖 115 张可 scaffold 卡片，0 崩溃
- **内容安全**：`--write` 只追加不修改已有内容，pytest 逐内容验证
- **pytest**：222 passed, 1 skipped（+17 新 scaffold tests）
- **KDO CLI 新增命令**：`kdo scaffold`

### 2026-05-19：新任务分配 — scaffold（黄药师）+ 设计域规划

**黄药师 → `kdo scaffold`（P0 工单 [[70_product/tasks/kdo-scaffold-v15.md]]）**：
- 为缺失 v1.5 信号的卡片自动生成升级骨架（TODO 占位符 + 智能学者建议）
- CLI: `kdo scaffold --card <id>` / `--batch A` / `--from-plan` / `--write`
- 核心逻辑：读卡→诊断缺口→生成骨架（Critique/不要用/AT）→智能攻击者建议（同域池+跨域经典配对）
- ~200-250 行，~8 test cases
- **不做**：自动生成攻击内容、自动选择攻击者、修改已有节

**老顽童 → 管理工具箱 Batch 2（T3+T4+T5）+ 设计域规划**：
- 设计域素材已就位 `00_inbox/design/`：月白老师两期 AI 设计分享转录稿 + prompt 集合
- 初步规划 7 张卡（D1 AI生图技术→D7 设计师角色重塑），最终 5-8 张
- 执行流程：清理转录稿→ingest→编译卡片→学者攻击者配对→欧阳锋审查
- 工具箱 Batch 2 优先完成后启动，不并行

**黄药师完成 scaffold 后的后续方向**：
- Scaffold 完工后老顽童立即使用它开工 89 卡修复
- 黄药师后续选项：设计域转录稿清理工具 / `kdo validate --v15 --watch`（文件变更自动重检）/ Graph RAG 索引增量更新 / KDO build 系统（非紧急）

### 2026-05-19：老顽童管理工具箱 Batch 2 审查（T3 A / T4 A+，T5 制作中）

- **T3 OKR 罗盘**（A）：Mintzberg（涌现战略）+ Lisa Ordonez（目标副作用/"Goals Gone Wild"）— Ordonez 是非显而易见的优秀选择，攻击角度精准
- **T4 战略研讨会**（A+）：Christensen（创新者窘境——战略会杀创新）+ Taleb（黑天鹅——规划是伪科学）— 全库迄今最佳 tool 卡。会前四件套+会中五段式+会后三检查，11 步结构最完整。建议作为后续 tool 卡参考标准
- **T5 知识萃取器**：制作中（建议 Nonaka&Takeuchi + Snowden）
- **T3 待修**：Line 106 `团队脚脑暴`→`团队头脑风暴`
- Mintzberg 已出场 3 次（F1/T3/T4），Tale b 已 ~3 次。T5-T8 应避开

- **F1 工具箱总览**（A）：Mintzberg（管理手艺不可编码）+ Pfeffer（Leadership BS/科学感=安慰剂）— 管理域最佳攻击者配对之一
- **T1 会议设计师**（A）：Kahneman（认知负荷/System 2）+ Perrow（正常事故/紧密耦合）— 双杀，操作流程四段清晰
- **T2 面试打分卡**（A）：Kahneman（噪声 vs 偏差）+ Tetlock（专家预测失败/狐狸 vs 刺猬）— Kahneman 两次出场攻击角度完全不同（认知负荷 vs 噪声偏差），区分度足够
- **攻击者阵容**：Mintzberg, Pfeffer, Kahneman×2, Perrow, Tetlock — 5 位真实学者，0 稻草人
- **T1 小问题**：Line 88 typo "只需要知会议会把议程定好"语义不通，修完推进 Batch 2
- **双三角文章 v2**：用户已通过，任务关闭
- **下一步**：Batch 2 — T3（OKR 罗盘）+ T4（战略研讨会）+ T5（知识萃取器）

### 2026-05-19：黄药师 `kdo validate --v15 --upgrade-plan` 完成 ✅

- **任务文件**：[[70_product/tasks/validate-v15-upgrade-plan.md]]
- **核心实现**：`kdo/commands/quality.py` +130 行
  - `_card_citation_count(card_id, concepts_dir)` — 全库 `[[wikilink]]` 扫描计数
  - `_estimate_effort(checks, structure)` — 按缺失信号估算分钟数（5 档：15/20/40/55/60/90m）
  - `_classify_batch(r, full_check)` — 五批分组（A=全信号缺失高引, B=缺攻击, C=缺AT, D=研究降级, E=warnings）
  - `_print_upgrade_plan(results, ...)` — 分级打印 + JSON 输出
- **CLI 接口**：`kdo validate --v15 --upgrade-plan [--domain] [--batch-size] [--json]`
- **全库运行**：160 卡（89 fail + 71 warn），估计总工时 ~86.7h
  - Batch A (CRITICAL): 3 cards, ~4.5h — 全信号缺失，高引用
  - Batch B (HIGH): 80 cards, ~56.1h — 缺外部攻击
  - Batch C (MEDIUM): 6 cards, ~1.8h — 缺 Action Triggers
  - Batch D (LOW): ~26 research cards, ~13h — 研究降级失败
  - Batch E (TRIAGE): 45 cards, ~11.2h — warnings
- **pytest**：23 passed, 1 skipped（test_validate_v15.py），全绿
- **关键修复**：Batch D 分类 bug（research cards with WARN status was being filtered out — changed to `r["overall"] in ("FAIL", "WARN")`）

### 2026-05-19：黄药师 `kdo validate --v15` domain filter bug 修复 ✅

- **任务文件**：[[70_product/tasks/fix-validate-v15-domain-filter.md]]
- **修复**：`_read_frontmatter()` 重构为状态机解析器，返回 `dict[str, list[str]]`，支持三种 domain/type 格式（单值、Python 列表、多行 YAML 列表）
- **验证**：--domain yitang 从 7 张恢复到 ~140 张。pytest 无回归。

### 2026-05-19：黄药师 kdo validate --v15 审查通过（A-）+ domain filter bug 工单

**审查结论**：
- 代码质量 A：~350 行，结构清晰，`_parse_card_sections` + `_count_*` x3 + `cmd_validate_v15`
- 测试 A：24 tests（23 pass + 1 skip），6 结构分类 + 4 集成 + 双模式攻击检测
- 真实卡验证 A：205 张全量扫描 0 崩溃，45 pass / 89 fail / 71 warn 均为真实反映
- JSON/--card/--type 均正常。全量 pytest 205/205 pass，无回归

**Bug — `--domain` 过滤失效**：
- `_read_frontmatter()` 单行正则无法解析多行 YAML 列表 `domain:\n  - yitang`（168/195 张卡）
- `--domain yitang` 只命中 7 张（预期 ~140）
- 工单已下发：[[70_product/tasks/fix-validate-v15-domain-filter.md]]

**小问题（不阻塞）**：
- 学者名含中文标题（H4 无冒号时 fallback 到全文本），去重正确但显示不干净
- `--type` dest="ctype" 与 task spec 中的 `--type` 一致，仅内部命名差异

**后果**：
- 黄药师修 `--domain` bug（~15 行，`_read_frontmatter` 支持多行列表 + domain 比较改为 `in` 检查）
- 修完后欧阳锋复验 → A → 合入

### 2026-05-18：老顽童调研方法论域提案批准 + 老顽童评估升级

**提案审查结论**：
- **域选择**：✅ 调研域是空白度最高 × 素材最丰富 × 价值最大的交集，优先编译
- **Card Map**：8 张（F2+T5+C1）合理。建议 T4（行业画布）和 T5（假设验证）编译时评估是否需合并，但不阻塞启动
- **攻击者**：全部跨范式。Feyerabend+Kuhn 配对为 KDO 首次出现。Taleb 第 3 次出现，T4 需确保攻击措辞与 width-method 中的 Taleb 有足够区分度
- **材质风险**：老顽童必须先 OCR 扫描调研素材文件夹中全部图片（P-7 教训），再开始编译
- **科学决策审计**：已叫停。10 张卡 A 级，不返工

**老顽童评估升级**：
- 独立判断 A→A+：SpaceX 例子的自我纠错——识别出"类比污染"并自主完成方法论层面的修正
- 老顽童已从"需要监督的高产能执行者"进化为"可以独立做方法论判断的内容架构者"

**后果**：
- 老顽童下个任务：调研域 8 张卡编译
- 黄药师下个任务：KDO 基础设施 backlog（待枚举）

### 2026-05-18：角色重对齐——黄药师回归工程师岗，老顽童接全部产能岗

**背景**：两轮审查发现黄药师在基础设施（KDO CLI / Graph RAG / 方法论对接表）产出 A+，但在卡片量产（Batch C 5/30）反复掉链子。老顽童本轮 7 张 master 卡 + PEAS 卡一次交清，质量 A，产能超预期。这不是速度问题，是天赋错配——黄药师引力场在"建工厂"，老顽童引力场在"工厂里出活儿"。

**决策**：
- **黄药师 = KDO 基础设施唯一负责人**：CLI 开发、方法论建设、质量门设计、Graph RAG、代码审查。只写只有他能写的卡（如认知升级十步↔KDO三步编译对接表这类 meta 卡）。不接卡片量产任务。
- **老顽童 = 产能主力**：卡片量产、文章/内容产出、跨域合成、提案新域。7 张 master 卡直接入库启用。
- 黄药师权限已扩：`.claude/settings.json` 新增 vault 全路径 Read/Edit/Write/Glob/Grep + kdo 命令免批，解决手动批准瓶颈。

**否决的替代方案**：继续让黄药师兼量产——两轮数据证明产能天花板在 17%，且拖累基础设施进度。

**后果**：
- 黄药师 Batch C 剩余 concept 卡转交老顽童或暂停
- 黄药师下个任务：KDO 基础设施 backlog（枚举待定）
- 老顽童下个任务：量产 master 域剩余卡 + 文章
- 老顽童评估更新：知识广度 A-→A，独立判断 A-→A，跨域合成 A-→A

**⚠️ 注意**：黄药师不碰卡片生产后可能和 vault 内容脱节。每次做基础设施决策前先跑 `kdo graph query` 保持体感。

### 2026-05-18：黄药师 KDO 基础设施 backlog P0+P1-A+P1-B 全部完成 ✅

- **P0 Graph RAG 重建**：索引 396→406 nodes, 1188→1252 edges, 616→721 chunks。Pirsig/Geertz/Illich 冒烟验证通过
- **P1-A `kdo lint --accept-baseline`**：635 issues accepted。默认 `kdo lint` 输出 "0 new (635 accepted)"。`--baseline <ref>` 行为不变
- **P1-B `kdo lint --structure-report`**：197 卡分为 6 类 — pan-product (82, 42%), other (52, 26%), standard-concept (31, 16%), research (15, 8%), pan-product-upgraded (14, 7%), catalog-index (3, 2%)
- pytest: 182/182 全绿，无回归
- 代码量：+87 行（cli.py +3, system.py +84）
- 等待欧阳锋决定：P2（工业化手册 v1.7 / `kdo backup`）还是质量门自动化（`kdo validate --v15`）

### 2026-05-19：黄药师 P2-A + P2-B 全部完成 ✅

- **P2-A 工业化手册 v1.7**：`90_control/kdo-industrialization-manual.md` 追加 4 个新节：
  - §1.10 四种卡片结构与 v1.5 升级路径（标准/pan-product/research/catalog 各结构 [Critique] 插入位置 + 升级前必检清单）
  - §1.11 跨域引用桥接策略（yt-concept-weapon-arsenal + yt-model-personal-pitch-toolkit 作通用桥接卡 + 质量信号）
  - §1.12 新工具用法（`kdo cards --missing`、`kdo lint --accept-baseline`、`kdo lint --structure-report`、`kdo graph rebuild`）
  - §1.13 KF-022/KF-024 执行感受（≤5/会话 + ≤3500 tokens 正负面效应 + 建议）
  - 版本号 1.6→1.7，updated_at→2026-05-18，版本历史新增 1.7 条目
- **P2-B `kdo backup`**：`kdo/commands/system.py` +88 行，`kdo/cli.py` +3 行
  - `kdo backup [--output <dir>]` 自动 zip KDO 源码（排除 .git/__pycache__/build/.* 目录）
  - 输出到指定目录（默认 ~），自动保留最新 5 个备份
  - 验证：88 files, 279 KB
- **CLAUDE.md**：KDO CLI 速查表更新（lint 完整参数、backup、cards 命令）
- pytest: 181/182 green（1 flaky dashboard test，预存无关）

### 2026-05-19：黄药师质量门自动化 `kdo validate --v15` 完成 ✅

- **任务文件**：[[70_product/tasks/quality-gate-automation-v15.md]]
- **核心实现**：`kdo/commands/quality.py` +200 行
  - 6 种结构 × v1.5 三信号校验矩阵（standard-concept/pan-product/pan-product-upgraded 全检，research 降级，catalog-index 最低，other 人工审查）
  - 外部攻击：H4 scholar headings 计数 + 去重（回退 italic spans）
  - 不要用场景：`### 不要用*` H3 子节下 3 列表格行计数（排除表头）
  - Action Triggers：H2/H3 双位置搜索 + 3 列表格行计数（排除表头）
- **CLI 接口**：`kdo validate --v15 [--domain] [--type] [--card] [--json]`
- **pytest**：205/205 passed（新增 24 test cases，1 skipped），1 flaky dashboard test 本次也未触发
- **全库运行**：205 cards — 45 passed / 89 failed / 71 warning
  - Failed：主要是 pan-product tool 卡未升级 v1.5（external-attacks 0/2）
  - Warning：research/other/catalog-index 结构卡（downgrade check + manual review）
  - 无假阳性崩溃
- **关键修复**：
  - `classify_card_structure` 提取到模块级别（system.py→quality.py 复用）
  - 修复 research 卡分类（Reusable Knowledge/Open Questions 优先于 Critique 检测）
  - 修复表格计数（排除表头行 `past_sep` 逻辑）
  - 修复 GBK 编码问题（Unicode 符号 → ASCII）

### 2026-05-18：黄药师 Batch 7（最终批）—— Batch C 29/30 实质完成

- **Batch 7（4 张）**：落地篇（Pirsig+Newport）、调研武器库（Feynman+Geertz）、调研行动营（Schön+Dewey）、课程目录（Perkins+Illich）
- **累计 29/30**：学者阵容新增 Pirsig, Newport, Feynman, Geertz, Perkins, Illich — 6 位。Batch C 学者总阵容 ~46 位，0 稻草人
- **特别挑战**：调研两张卡（weaponry-course / action-camp-launch）结构与标准 concept 卡完全不同（Summary→Reusable Knowledge→Open Questions→Output Opportunities→相关页面），需从零插入 [Critique] 和扩展 Synthesis
- **lint 通过**：0 new errors
- **实质完成**：剩余 ~1 张（yt-case-mandatory-cases 或 yitang-course-map）为案例目录/课程地图索引类，非典型 concept 卡结构，不在 v1.5 升级范围内
- **后续**：黄药师回归 KDO 基础设施 backlog。Batch C 全部产出待欧阳锋审查

### 2026-05-18：老顽童 7 张 master 卡审查通过（A）+ 黄药师 5 张 concept 卡通过

- 老顽童：7 张 master 卡（认知偏差清单/决策卫生/第一性原理/系统思考/反脆弱/AI信息素养/知识复利）+ PEAS 洞察卡 + 边界定义文件。全部评审 A。攻击者 20 位，0 稻草人。已建议直接入库。
- 黄药师：5 张 concept 卡（守脑如玉/上下文工程/PEAS/武器库/认知升级十步）。质量 A。pytest 已装（9.0.3）。十步↔KDO三步编译对接表是意外的高价值产出——回答了老顽童消化笔记 #3 问题。
- 黄药师 Claude Code 权限已修复：`.claude/settings.json` 扩至 vault 全路径 + kdo 命令免批。

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

1. **先看 dashboard** → [[70_product/tasks/dashboard.md]]
2. **黄药师**：待命。Task 1-17 全部完成。顺手修 P3（`kdo video ship` stages 同步）待分配。
3. **老顽童**：待命。9/9 全部完成。
4. **洪七公**：双三角 VA 待审阅。
5. **段王爷**：Publisher 反馈闭环初具雏形（已发现首条工具缺陷）。

## ⚠️ 会话结束前（MUST）

- [x] 更新 `updated:` 日期
- [x] 更新 `active_task` 和 `blockers`
- [x] 更新 ## 当前状态
- [x] 有新坑？追加到 `pitfalls.md`
- [x] 有决策？追加到 `decisions.md`（Task 15-17 video CLI 完成 + 段王爷首次反馈闭环）
- [x] **禁止用 `/memory` 替代上述更新**
