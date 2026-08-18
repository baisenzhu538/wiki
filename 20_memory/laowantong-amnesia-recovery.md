---
title: 老顽童失忆恢复记录
created_at: 2026-07-24
updated_at: 2026-08-18
type: memory/role-recovery
---

# 老顽童失忆恢复记录

> 触发：用户说"你是老顽童，去队列领任务生产卡片"
> 工作目录：`C:\Users\Administrator\Desktop\wiki\`

---

## 1. 我是谁

**老顽童（Producer）**——KDO 知识工厂的卡片/文章产能主力。

- **主业**：按生产队列领取任务 → 读素材 → 生产 wiki 卡 / Skill / 文章 → 跑 pre-submit → 提交 pending_review
- **运行接口**：Claude Code / Kimi Code / Hermes CLI
- **任务来源**：`70_product/tasks/production-queue.md` 中排在前面的 `queued` 任务
- **协调节点**：一次只领一件；不准并行、不准跳队；状态变更必须走 `queue_transition.py`

---

## 2. 失忆恢复最小路径

| 优先级 | 文件 | 作用 |
|:---|:---|:---|
| **P0** | `.agent/laowantong-context.md` | 身份、启动四件事、**行为牌组 L1-L8**、产出标准 |
| **P0** | `.agent/context.md` | 全厂共享状态、active_task、blockers |
| **P0** | `70_product/tasks/production-queue.md` | 按顺序领取最前面的 `queued` 任务 |
| **P1** | `.agent/toolkit.md` | 本地武器库、命令速查 |
| **P1** | `.agent/pitfalls.md` | 全厂踩坑记录 |
| **P1** | `桌面/agent复盘/laowantong/daily-context/` | 最近 Truman 10章复盘 |
| **P1** | `python -m cap_hub list` | 能力中台——知道现在有什么工具可用 |
| **P2** | `90_control/AGENTS.md` | 全厂角色分工、禁止清单 |
| **P2** | `20_memory/laowantong-amnesia-recovery.md` | 本文件 |

---

## 3. 我的行为牌组（L1-L8）

| 牌号 | 句式 | 一句话触发 |
|:---|:---|:---|
| L1 | 先出牌再动手 | "开始写卡" |
| L2 | 先消费全量素材再写卡 | "图片不重要" |
| L3 | 先深挖达标再提交 | "差不多了" |
| L4 | 先 pre-submit 再交卷 | "写完了" |
| L5 | 先跑脚本确认再声称完成 | "这批完成了" |
| L6 | 先 WebSearch 再命名 | "叫它XX吧" |
| L7 | 先查已有卡再新建 | "建张新卡" |
| **L8** | **子卡先写定位再写内容** | **"这是某框架的子卡"** |

> L8 核心：生产任何属于更大框架的 tool/concept/case/dk 子卡时，标题下第一行必须写"本卡属于 `framework-xxx` 的第 Y 步"，再展开正文。

---

## 4. 当前状态（截至 2026-08-18）

- **2026-08-18 恢复会话（hermes 实例）+ 欧阳锋编排者核验**：全链恢复第 4 次走通——队列实测（重跑）queued=5（#343/#344/#346 codex 迁移 T1/T2/T4 已解冻 + #345 黄药师 T3 挂起 + #358 黄药师 graph 引擎层新增）/ claimed=0 / pending_review=1（#359 黄药师登记副本收口）；#342 已终审 PASS A（欧阳锋）；#354 已 closed_no_action 并入 #356；**老顽童名下无活待命**。三问核验：①我是谁 ✅（小口径修正：王语嫣=编排者派单/核验/队列维护，素材验收是前置一环）②当前任务 ❌ 首次队列快照过时（报 335/#342 为会话早期旧态，E034 实证：汇报前必须紧邻重跑 status）③生产纪律 14 条 ✅——三问回答作为 **#344 记忆继承子项验收证据**（本体过、队列态过时=未刷新运行时，非记忆丢失）。context.md active_task（08-18 上午"pending_review=0"）vs 实测 pending_review=1——共享状态滞后半天，以实测为准（锚点同步纪律第 4 次实证）。工厂全局（王语嫣 08-18 交叉验证）：六单终审全闭环（#347 洪七公迁 Windows PASS A / #348 R 型 Partner 部署 PASS A / #350 kdo MCP UTF-8 修复 PASS A- / #351 段王爷检索启用 PASS A- 738s→8.6s / #337 照镜子审计 PASS 条件 A-）；小昭 MCP 审查 16 条→codex 复审发现冷加载 300s 死循环→#355 止血/#356 治本；E025 第三次复发被批、E034 新增（幽灵修改误判）。复盘双写裂缝仍在推动裁定，不自行改动。

- **2026-08-17 恢复会话（hermes 实例）**：全链恢复完成——队列实测 queued=6（#337 codex 审计 + #342-#346 迁移 T0-T4 全归 codex/黄药师）/ claimed=0 / pending_review=2（#347 洪七公迁移 codex + #348 R 型部署 codex），**老顽童名下无活待命**。**#349 已终审 PASS A-**（2026-08-17 欧阳锋：转卡保真+related 8 死链 0+覆盖事故裁定认可）——锚点此前写 pending_review 属落后实际，本次同步（双真相源纪律第 3 次实证）。工厂全局（王语嫣 08-17 交叉验证）：迁移收官+全量 Windows 决策反转（洪七公不再留 WSL）；E030 platforms 语义修复（51+2 处）；kdo_search 进程级缓存 O-15（617→537MB，首次 5.5s/二次 0.000s）；9 gateway 错峰重启；R 型首战（#348）→ #349 转卡 → Y-AI 对标 R 型自迭代 v2。复盘路径三套并行裂缝活体证据（laowantong/daily-context vs 老顽童/daily_cognitive_review 同源双写）已推动王语嫣/欧阳锋裁定，不自行改动。

- **2026-08-16 生产批次 #349（hermes 实例，R 型首战资产转卡）**：视频号→逐字稿自动化工作流 tool 卡 1 张（`tool-wechat-transcript-automation-workflow`）——四环节×双路线矩阵+12 工具全景+反爬情报+DataPack 四要件全含；verified 分级（实测/引用/推演）保留不抹平、未实证 4 项如实列卡、frontmatter `time_valid: 2027-02` 时效标注；素材已资产化跳过诊断直接生产（半天活模式）；pre-submit PASS 一次通过（0 issues）+ related 8/死链 0/跨域≥2；已 pending_review 待欧阳锋终审。队列：queued=6 / claimed=0 / pending_review=3（#347/#348/#349，前两个为洪七公/黄药师任务）。
- **2026-08-16 技能体检+自修复（hermes 实例，Windows 侧）**：迁移体检确认技能体系无丢失——①三类"缺失"误报识别：a) 会话启动快照早于 19:16 批量补拷（pre-submit-self-check/agent-infrastructure/business-research/guizang-ppt/kdo-operational-runbook/knowledge-delivery-os 均为 19:16:38-42 补拷），当前会话系统提示看不到但注册表全在、skill_view 实测可加载；b) KDO 技能真实家在 `wiki/40_outputs/capabilities/skills/shared/`（71 个，Hermes 直接扫描加载，不必复制进 profile）；c) platforms/environments 过滤≠丢失（5 个 [linux,macos] 官方技能 vllm/lm-eval/research-paper/xitter/xurl + kanban-orchestrator environments:[kanban] + infinite-canvas-prezi platforms:[cli] 均为设计行为，Windows/飞书侧本就不该加载）。②**真缺失并已修复**：CLI profile（laowantong，190 技能）比飞书 profile（laowantong-feishu，152 技能）多 44 个——其中 22 个 KDO 生产核心（note-taking/kdo-* 系列 20 个+kdo-domain-tag-audit+hermes-skill-registry-diagnostics+mineru-env-repair）已补拷到飞书 profile，注册表 145→166 全 enabled；其余为官方技能（apple-3 个 macos 过滤不注册、github-*、claude-code/codex/opencode、sketch 等无害冗余）。③体检命令链：`COLUMNS=500 hermes skills list --profile laowantong-feishu --source {local,builtin,all}`（防表格长名截断）+ `--enabled-only`（零禁用验证）+ 双 profile os.walk diff + platforms 过滤判定四步。详见技能进化日志 2026-08-16 两行。

- **2026-08-16 深夜：迁移决策（老板拍板，WSL → Windows 侧启动）**：
  - 状态：Windows 侧已就绪——laowantong profile 记忆已同步（MEMORY/USER，2189/786 字节，内容一致仅行尾差异）、技能已补拷（kdo-domain-tag-audit/yuanbao 补齐，其余一致）、status.py WinError 87 补丁已确认（3 处 except OSError）、config.yaml 无路径陷阱（prefill_messages_file 为空）
  - 知识资产在 Windows 盘天然共享（wiki/桌面复盘），迁移零影响；kdo CLI Windows 侧完整（Knowledge Delivery OS 0.0.1）；洪七公迁移先例已验证
  - **Windows 侧首次启动恢复口令**：①读本锚点 §4 ②`queue_transition.py status` 实测队列 ③检查 gateway 状态（飞书 WebSocket connected）④若记忆未加载→查 `C:/Users/Administrator/AppData/Local/hermes/profiles/laowantong/memories/`；若技能缺失→对比 WSL `~/.hermes/profiles/laowantong/skills/` 补拷
  - 注意：WSL 侧 gateway 需先停（双开会冲突）；default profile 记忆（CLI 会话）在 WSL `~/.hermes/memories/` 若需迁移需另行拷贝

- **2026-08-16 生产批次 #336/#340/#341（hermes 实例，AI×知识管理三批 21 卡）**：楚门探索营全域——**#336（P0）6 卡**：framework×5（knowledge-compound-rocket-six 火箭六要素【周期×数量质量×自动化协作化×可掌控】/knowledge-five-leaps 五次飞跃【2013→2026 编年+AI 周期变短】/multi-agent-collab-chain-six 协作链六环节【管理读写关系】/dual-center-feishu-obsidian 双中心【飞书给人 Obsidian 给 AI】/truman-agent-team-architecture 三团队×10 Agent 负责人制）+ concept×1（session-vs-memory-vs-document 降 Session 依赖）；**#340（P1）9 卡**：tool×4（knowledge-cheatsheet-sab 小抄 S/A/B/top-level-document 顶层文档/skill-packaging-eight-steps Skill 八步/autoclassify-seven-steps 分类 7 步）+concept×1（ai-style-knowledge-docs 10-11 种）+case×2（vibecoding-one-week-delivery 一周 900 页 PPT/ new-year-insight-relay 四棒接力）+framework×2（serendipity-five-channels 偶遇五通道/patrolkit-radar 资产雷达）；**#341（P2）6 卡 dk**（tool-adoption-by-force 硬推/research-saturation-quota-ai-km 饱和话术【与爆炸式 W3-1 互链】/extract-then-merge 先萃取再合并/one-sentence-handover 一句话交接/model-demystification 模型祛魅【kdo-context-design 待建，纯文本标注】/three-context-formula 三上下文公式）。素材锚点区间逐字精读+OCR 图核验（25 图）；pre-submit 21/21 PASS 零 warning；related 7-8/死链 0/跨域≥2。**三任务均已 pending_review 待欧阳锋终审**。今日累计交付 49 卡（#319+#320+#322+#332+#333+#334+#336+#340+#341）。
- **2026-08-16 生产批次 #333/#334（hermes 实例，爆炸式调研 Wave 2+3）**：**#333（P1）7 卡**——case×5（leo-lubricant-dealer-research【三轮 60 家+因果三参数+生存状况图+70% 改善，脱敏 A 品牌】/4000-titles-ten-strategies【3000 收敛+十大策略+数据包】/ai-learning-series-modeling【编程四级+龙虾五级+2000 视频+Top10】/design-principles-90【5×3×90+四轮打样】/opc-128-directions【4×16×128+时间锚定+201 饱和】）+ framework×2（ai-report-value-ladder-l1-l6【每级×10】/ai-human-70-30-division【AI 排+人排】）；**#334（P2）8 卡 dk**（saturation-self-proof 记数自证/classification-mece-table 3-5 套方案/ranklist-replaces-model 排行榜替代/total-anchor-private-library 总量锚定/sampling-correction-three-rounds 打样纠偏/scavenger-vs-architect 拾荒者 vs 建筑师/important-things-must-do 应做必做/ai-no-time-concept 时间锚定）。素材锚点区间逐字精读，精做笔记追加 W2/W3 节；pre-submit 15/15 PASS 零 warning；related 9-11/死链 0/跨域≥2（补 bridge/cross-xingangwan/dk-ai-builder-illusion 三跨域卡）。**终审 PASS A-**（爆炸式调研三波 20 卡全部入库收官）：O0 溯源抽查 3 锚点逐字命中（总量锚定 L3770-3774/应做必做 L4022-4030/时间锚定 L3552-3556）；15 卡结构全绿（dk 七段+定位声明/related 7-8 死链 0）；OCR 冲突处理纪律获认可（W2-6 L6 以 OCR_003832 图为准并注明）；#320 教训即时应用（首轮零 warning）。今日累计交付 28 卡全 PASS A-（#320 六卡+#322 一卡+#332 五卡+#333 七卡+#334 八卡+补链）。队列：queued=5（含 #335 王语嫣 R 型 spec）/pending_review=0 全清。
- **2026-08-16 生产批次 #332（hermes 实例，爆炸式调研 Wave 1）**：P0 框架主线 5 卡完成并提交 pending_review——framework×2（baozhashidiaochan-five-step 五步法【目标→范围→搜索⇄建模→交付+规律基本稳定终止+借假修真+交付三做厚】/ r-type-research-partner-five-state R 型五状态机【定边界→规划信息源→饱和送→分类人拍板→资产报告】）+ concept×2（research-saturation-coverage 饱和覆盖【量级观+规律收敛+流浪地球类比】/ open-a-document 开一篇文档【研究：顶级作品建模】）+ tool×1（nine-character-mantra-14-strategies 九字诀【定目标4/控节奏4/做纠偏6】）。素材 6718 行（上 2336+下 4382）结构扫描+锚点区间逐字精读，精做笔记 `_tmp/baozhashidiaochan-wave1-精做笔记.md`；pre-submit 5/5 PASS 零 warning（W1-3 死链 tool-agent-spec-basic-skills-coach→agent-spec-basic-skills-coach 已修）；related 9-11/死链 0/跨域≥2；**补链完成**（4 张已有卡 related 各+5 回补+选课口令 478/480/479/570 登记）。已 pending_review 待欧阳锋终审。队列：queued=0/claimed=0/pending_review=1（#332）。
- **2026-08-16 终审闭环（#319/#320/#322 全部 reviewed）**：
  - #319 O-14 domain 清扫：**PASS A-**（domain 9/9 达标）；**目录迁移方案 A 被驳回**——欧阳锋 hash 实测：tools/ 版（08-04）与 agent-specs/ 版（08-03）md5 不同且 tools/ 版更新，我方案"以 agent-specs/ 版为准"会丢 08-04 更新。裁定：保持 tools/ 接受 WARN，目录统一另立项（迁移前先双份 diff 合并）。教训已入技能日志（重复文件以谁为准=hash+mtime+diff 三证）。
  - #320 SPIN 六卡 + #322 Candy 一卡（合计 7 张）：队列实测均 reviewed（queue_transition.py status + 队列行双确认）——终审通过。
  - 队列：pending_review=0 全清，queued=2（#330 黄药师/#331 王语嫣）。
- **2026-08-16 生产批次 #319（hermes 实例，O-14 agent-spec domain 清扫）**：9 张 agent-spec 卡 domain 全补齐（2 张 None 修复：meeting-assistant→[management,decision,yitang]、coaching-leadership→[human,management,yitang]；7 张已有列表实测确认），pre-submit 9/9 Failed 0，lint 零 issues。**目录迁移方案已建议先行写入任务单**（方案 A 被驳回：重复文件 hash 不同、tools/ 版 08-04 为权威，迁移另立项先双份 diff）。已 reviewed（PASS A-）。注：kdo lint 偶发 state.sqlite disk I/O error（WAL 在 drvfs 挂载上的已知问题，重试即过）——与 #327 质疑的 kdo 基建问题同家族。
- **队列实测（2026-08-16）**：queued=0 / claimed=0 / pending_review=3（#319 老顽童 + #321/#328 黄药师）——**全队清空，老顽童名下无活待命**。
- **2026-08-15 生产批次 #320/#322（hermes 实例，销售域）**：SPIN 实践篇+AI 销售协同卡组完成——**#320（P1）6 张卡**：framework×2（ai-sales-collaboration 双条件框架【sales+decision 双向归集，related 含 yt-decision-ai-partner/科学决策三角形/dk-decision-value-overrides-roi】/sales-funnel-full 正梯形复购裂变）+ tool×1（sales-objection-dilution 承认→稀释→调动，笔记 L58 量化话术并入）+ dk×3（demand-mining-is-company-task 痛点库/big-deal-vs-small-deal 非 ToB/ToC/customers-hate-ai 人情味边界）；**#322（P2）1 张**：tool-candy-sales-recruiting（星巴克结论一致+Cosmos 跑楼验证，**传播限制标注已加**）。两任务合计 7 张。素材 2400 行逐字通读精做笔记 `_tmp/spin-sales-精做笔记.md`；pre-submit 6/6+1/1 PASS 零 warning；related 死链=0 跨域≥2（全库 2763 卡脚本实测）。**两任务均已终审 reviewed（PASS A-）。全网调研外网被审批拦截，已用知识库内部交叉验证替代并如实标注**。
- **2026-08-15 失忆恢复会话（hermes 实例）**：全链校准完成——队列实测 queued=1（#319 agent-spec domain cleanup，assignee=wangyuyan，生产阶段才交老顽童/黄药师）/ claimed=0 / pending_review=0，**老顽童名下无活，待命**。Live258 三连批终态：#312 case 4 张 reviewed（A-）/ #313 dk 2+1 reviewed（B+）/ #314 tool 1 张 reviewed（A-）——看板 297/297 全清（欧阳锋 08-15 复审确认 #304 终审有效 A-、#298 已 E019 对齐，两单均无需重审）。交叉验证：codex 08-15（内存 32GB 实测、P-31 已解决、8 gateway 全 active）。停车场：O-13 已执行（8GB/4核/wsl --shutdown 解锁真机冒烟）、O-14 已立项（agent-spec domain 清扫=#319）、O-12 待扩容评估、P-31 待拍板。
- **锚点同步纪律（08-15 新增）**：锚点 §4 曾落后于 context.md active_task（#314 已终审 vs 锚点写 pending_review）——两处真相源会话收尾都要刷，恢复时以"目录内最新"为准，不信写死日期（欧阳锋/黄药师 08-15 同构教训）。
- **恢复全流程实证**：`.agent/laowantong-context.md` 再次被 read_file 报 binary（UTF-8-SIG BOM 误判）→ utf-8-sig 回退链一次解码成功；双实例复盘全扫无乱序/缺行（错误模式库 E001-E009、技能进化日志 kimi 至 08-12/hermes 至 08-15、用户反馈档案完整）。
- **#312/#313/#314 交付锚点（2026-08-12，hermes 实例）**：Live258 内容域三连批——case 4 张（zhihu-content-acquisition/livestream-prompt-v1-v5/fact-spread-18-bridges/europe-cold-email）+ dk 2 张+1 修补（ai-does-not-question-your-mistake/feature-pieces-not-recognized-as-cards + demand-feature-stacking 修补回填证据）+ tool 1 张（feature-review-five-step）。精做笔记=领取前置 P0（3025 行逐字通读→行号索引落盘 `_tmp/live258-excellent-homework-精做笔记.md`，一次提取三次消费）；批内互链按依赖序解锁（case→dk→tool）；全批实测/推演标注，O0 溯源零编造；欧阳锋 TODO（related 重复）已修复。终审：#312 A-（08-13）、#313 B+（08-13）、#314 A-（08-15）。
- **#255/#257**：Feature 周期表收尾已终审通过（reviewed），R2 退回 2 项已修复（F045 补口述行号 L472-474 / F057、F087 降 verified=False / missing 字段改名 inferred_from_oral）
- **队列**：无老顽童可领任务——4 个 queued 全归黄药师（#241 master-moc、#260/#261/#262 agent-*），#252 王语嫣已领取（claimed-wangyuyan）
- **遗留提示**：F078/F079 与 F057/F087 同构（KDO 实践引用 #256/#230 无口述行号），已在 #255 任务单 R2 记录注明，留待欧阳锋裁定
- **parking lot**：`tool-泛产品设计-出牌指南 缺 frontmatter` 已验证过时（pre-submit PASS），标记 ✅ 已解决
- **2026-08-09 技能进化**：全网调研（Anthropic/agentskills.io/Eugene Yan/Matuschak）→ 新建 `skill-authoring-standards`（开放标准）；kdo-single-card-production v2.1.0（坑目录移 references + evals）；kdo-skill-card-c-to-a-refinement 746→355 行；wiki-batch-audit 737→415 行；wujue-architecture 623→205 行；kdo-knowledge-iteration-system 补上下文工程实证；self-evolution 补纠错即技能输入。**全部 23 个技能 SKILL.md <500 行达标**。调研报告存 `40_outputs/research/调研报告-2026-08-09-*.md`（2 份）
- **当前（2026-08-12 生产批次）**：Live258 内容域三连批完成——**#312 case 4 张 → reviewed（欧阳锋 A-）**、**#313 dk 2 张+1 修补 → reviewed（欧阳锋 B+）**、**#314 tool 1 张 → pending_review（待终审）**。素材 3025 行逐字通读，精做笔记落盘 `_tmp/live258-excellent-homework-精做笔记.md`（领取前置+验收 P0 门禁）。全部 pre-submit PASS、实测/推演标注、回链双向闭合。欧阳锋 TODO（dk-demand-feature-stacking related 重复）已修复。队列实测：queued=0 / claimed=0 / pending_review=1（#314）。#314 终审通过后本批收官，无后续可领任务。
- **2026-08-12 agent复盘 补充**：双目录活文档已全扫——laowantong/（kimi 实例技能进化日志，08-04 YAML 引号/08-05 dk Critique 复发/08-09 证据库模式+教练域六连批）+ 老顽童/（hermes 实例错误模式库 E001-E009、技能进化日志、用户反馈档案、能力雷达图、每日复盘 08-09）。交叉验证：欧阳锋 08-09（E013 候选工具故障不诊断绕过 + NUL 字节排查法）、段王爷 08-11（cron 清理/Bitable 补录）、AI基本功教练 08-09 v2（#252 试点五步闭环）。新增认知已入 Hermes memory：E009 归因谬误 / 工具故障四查 / NUL 排查法 / 口述稿第一 / 证据库模式。

## 4.2 科学开会批次交付锚点（2026-08-09 kimi 实例）

- **#285（pending_review）**：科学开会 9 卡——concept 升级 `yt-management-scientific-meetings`（source_refs 补齐+冰山三层/三层价值/非必要不开会/深度化简四节）+ framework×2（`framework-meeting-iceberg-canvas`/`framework-meeting-ten-principles`）+ case×3（`case-meeting-roi-awakening`/`case-meeting-scene-mastery`/`case-truman-meeting-leadership`）+ tool×3（`tool-meeting-basic/execution/result-principles`）
- **#286（pending_review）**：bridge×1（`bridge-meeting-leadership-coaching`，10 原则×5 阶梯完整映射）+ dk×6（`dk-meeting-roi-first`/`principle-over-process`/`rederive`/`borrow-false-repair-true`/`asset-harvest`/`pressure-ignition`）+ 已有卡补链 25 条
- **证据库（#287 王语嫣直接复用）**：`_tmp/scientific-meeting-evidence/`——evidence-认知篇/上篇/下篇.md（6990 行逐字提取+行号+ASR 还原表）、CARD-WRITING-SPEC.md、self-attack-285/286.md
- **关键勘误**："新手都在执行流程，高手都在把控原则"实出下篇 L426（非认知篇）；私董会收手机实在上篇 L98-144（非下篇）；认知篇 L2148+/下篇 L2602+ 为重复段；上篇 L146-176 燕窝广告段/下篇 L1146-1196 红豆歌词段为 ASR 噪声
- **队列基建**：production-queue.md 注释块夹表内导致 parse break（#285-288 不可见）已修复（移至文件末尾）；claim 跨 pending_review 用 `--force`（多实例并行合法通道，不同 assignee）
- **门禁口径**：pre-submit 跨域判定按 frontmatter domain 差集（复盘域卡也是 [yitang,management] 不算跨域）；kdo_lint.py 单文件模式 F2 断链全是误报，以 pre-submit 为准

## 4.3 教练域批次交付锚点（2026-08-09 hermes 实例）

- **#280（reviewed PASS A）**：教练式领导力 P0 十卡——framework×3（core/five-ladders/coin-model）+ tool×6（listening/questioning/feedback/three-stubborn-subordinates/consensus-goal-escalation）+ case×1（yitang-leadership-culture）+ case×1（communication-failures）
- **#281（reviewed）**：P1 四卡——bridge×1（coaching-leadership-feature-layered，五阶梯×Feature L5 同构映射）+ tool×1（exit-consulting 出口式咨询）+ dk×1（trust-coin-sensitivity）+ **dk-14 反馈冰山合并入 tool6**（口述/VLM 均无"冰山"表述，任务单"二选一"条款，合并判断已记录在案）
- **#288（reviewed PASS A 93 分）**：逐字深挖七卡——case×2（morfei-semiconductor 莫非半导体完整故事【#280 边界排除项证据已补足】/dialogue-three-versions 三版本对话）+ tool×2（four-layers 四层级×21卡牌矩阵【层级维，与 #280 类型维双维互补】/segments 段位清单 9 格【VLM 主锚+口述次锚】）+ dk×3（boundary-conditions/monkey-theory/y-model-communication）
- **#293（pending_review）**：#213 补链 9 卡 related ≥5 且 ≥2 跨域（含死链修复：framework-yt-oscar-research → framework-yitang-oscar-research；framework-decision-science-triangle → framework-科学决策三角形；dk-ai-capability-not-magic 不存在 → dk-ai-builder-illusion 语义替代）
- **#294（pending_review）**：#216 Christensen 补链（bridge 映射表建议链接全补，9/9 related 6-10/跨域 3-6/死链 0）
- **#301（pending_review）**：13 个 skill 触发词节补齐（#278 C3 拆分，E026 单角色铁律）——验证脚本 `scripts/verify-related.py`（pre-submit-self-check skill 自带）
- **队列基建复发**：表格内注释导致 parse break **两次**（#280 领前 + #301 complete 前，#282 行后注释"终态：spec已过审"）——已入 skill 排障速查 + 前后行检测法；**其他角色加状态备注时别写表格内**
- **#282 终态**：王语嫣 spec 已 reviewed（条件 PASS B+），C1/C2 全关闭（#288 PASS A 满足数据源完整性 15/15）——老顽童无需任何动作，部署承接 #300（王语嫣 spec → 黄药师三件套）

## 4.1 快速恢复口令（2026-08-16 更新）

用户说"继续"时按此顺序执行（<2 分钟恢复）：
1. `queue_transition.py status` → 看 queued/claimed/pending_review 分布
2. 有老顽童可领的 queued → `claim`；没有 → 跑维护义务清单（parking lot 实测清理 / 锚点 §4 更新 / 复盘补写）
3. 上次会话遗留 → 先查 `60_feedback/tasks/` 最新任务单的审查结论（识别"reviewed+条件项"分支），再决定是否补修复
4. **技能体检（2026-08-16 后必做）**：`skills_list` 抽查——注册表 189 全绿（51 个 platforms:[cli,feishu] 已被黄药师修为 [linux,macos,windows]，kdo-self-attack 等全部 available）；仍缺 → 四层排查 skill：hermes-skill-registry-diagnostics
5. **MCP 体检（2026-08-16 后必做）**：mcp SDK 2.0.0 已装进 Hermes venv（`hermes-agent/venv`）；`hermes mcp test kdo` → ✓ Connected + 4 tools；若 mcp_kdo_* 工具不可见 → 需重启 Hermes 让 discovery 重新注入
6. 收尾四件套是 todo 显式条目：技能进化日志 / 锚点 §4 / Truman 复盘 / `daily-context-save.py save`

---

## 5. 我现在的待命能力

队列/欧阳锋可以直接派：

1. 按任务单生产 framework/concept/tool/dk/case 卡
2. 部署 Skill / 写 system-prompt / manifest
3. 跑 `kdo pre-submit` 并贴输出
4. 跑 `kdo-self-attack` 并修复攻击发现的问题
5. 批量精修已有卡片
6. 按队列状态变更规则 claim / complete / release 任务

---

## 6. 产出存放规则

- **新卡**：`30_wiki/<type>/<id>.md`
- **Skill**：`40_outputs/capabilities/skills/<skill-name>/SKILL.md` + manifest.yaml + system-prompt.md
- **诊断/任务单**：按王语嫣任务单指定路径
- **状态变更**：只用 `python 90_control/scripts/queue_transition.py`
- **每日复盘**：`桌面/agent复盘/laowantong/daily-context/YYYY-MM-DD.md`

---

## 7. 关联文件

- `.agent/laowantong-context.md` — 角色上下文（活注册表）
- `.agent/context.md` — 共享状态
- `.agent/toolkit.md` — 本地武器库
- `.agent/pitfalls.md` — 踩坑记录
- `70_product/tasks/production-queue.md` — 生产队列
- `70_product/tasks/dashboard.md` — 任务仪表盘
- `framework-kdo-self-attack` — 自攻击方法论
