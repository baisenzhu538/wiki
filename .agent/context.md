---

updated: 2026-06-30
updated_at: 2026-06-30T15:23:37+00:00
status: active
reviewed_by: 欧阳锋
active_branch: main
active_task: "#33 大馨战队核心方法论卡片化（reviewed 2026-06-30）：欧阳锋终审通过；5 张目标卡 status 更新为 reviewed；审查中修正 case-daxin-team-content-training-camp 的 quality_labels；老顽童(Kimi)可继续领取 #28 lint 内容债（2656 WARNING）或 #34 社群知识生产失败模式库"
blockers:
  - "🟡 #33 大馨战队核心方法论卡片化（2026-06-30）：老顽童(Kimi)已完成 5 张卡生产并提交欧阳锋终审；待欧阳锋审查 framework 边界、case 证据链、tool 可操作性、related 分层"
  - "🟡 #28 lint 内容债按 domain 分批清理（2026-06-29）：老顽童(Kimi)已处理 28 文件，copy-paste 清零（76→0），lint 从 3255 降至 2656 WARNING；当前实例切换至 #30，#28 已释放回 queued；后续继续处理 strategy 域 body 过短，然后批量补 L2 Critique 外部反对者"

  - "✅ Batch 2-A/B/C reviewed（2026-06-28）：A 130 case + B 57 dk + C source_refs 数据层清理；`kdo lint` 总 ERROR 清零"
  - "✅ B1 frontmatter related 占位清理 reviewed（2026-06-28）：欧阳锋终审确认 256 文件真实修改，1947 src_unknown 清零，1190 pending_unknown 补入符合分层标准；`kdo lint` 0 ERROR"
  - "✅ B2 Synthesis section 清理 reviewed（2026-06-28）：235 张初处理 + 66 张补充清理，66 文件 body src_unknown 全部清零；kdo lint 140 ERROR 全为历史遗留，无新增；frontmatter src_unknown 另开任务处理"
  - "✅ B3 孤岛卡片补链 reviewed（2026-06-28）：1042 张处理、孤岛卡片清零；2014 YAML引号修复 + 163 bare id加括号 + 119 句子删除 + 33张孤岛补真实wikilink + pending_unknown.md移到system/；lint 140 ERROR全为历史遗留无新增；pre-submit抽检5/5 PASS；55张仍全pending为已知限制"
  - "✅ Wave 6 诊断通过（2026-06-28）：欧阳锋终审确认决策科学域 14 reviewed + 需求分析域 10-20 reviewed，盲区识别合理；#21 决策科学域系统化、#22 需求分析域深化可入队生产；决策科学 index 改为升级现有 `decision-science-domain-digest` 而非新建"
  - "✅ Wave 6 生产完成（2026-06-28）：#21 Wave 6-A 决策科学域系统化 reviewed（升级 digest + 4 张新卡），#22 Wave 6-B 需求分析域深化 reviewed（5 张新卡）；10 张新卡无新增 lint ERROR；历史遗留 140 ERROR 为 8 空 source_refs + 132 case section 缺失"
  - "✅ A1 空 source_refs 清理 reviewed（2026-06-29）：黄药师完成 8 文件修复，全部补为 pending_archive；`kdo lint` empty source_refs ERROR 清零；pre-submit 8/8 PASS"
  - "🟡 A2 case section 缺失补全 reviewed（2026-06-29）：Hermes 老顽童完成 frontmatter 修复，但欧阳锋实测仍有 132 个 `Case card missing section` ERROR（33 文件），任务单基线判断错误；需另开任务处理 132 section 缺失"
  - "🆕 #25 AI 工具学习方法论扩展卡已入队（2026-06-29）：用户要求把 YAI T/C 角色资料拆成原子概念卡；欧阳锋已创建 6 张核心卡，剩余 7 张扩展卡由老顽童补充"
  - "🆕 黄药师上线 `--expect-changes` 门禁（2026-06-28）：`kdo pre-submit -f <清单> --expect-changes <数量>`，若 git 实际变更文件数小于声称数直接 FAIL；Batch 2-A/B/C 任务单、production-queue.md、dashboard.md 已同步该门禁"
  - "🆕 老顽童(WorkBuddy) 完成 wave3 阶段 B 3.1 建模 5 张内容返工（2026-06-28）：capability-system/three-stages/level-map/weapon-library/process-modeling；每张 Claims 6 条+Critique+Visual+Reusable+OpenQuestions+Sources 全填；内容区 src_unknown 全清零（36/30/37/45/51→0）；pre-submit 5 passed/0 failed；3.2 综合卡 9 张格式转换未启动（重活，每张 283-353 行+47-97 src_unknown）"
  - "🆕 老顽童(WorkBuddy) 完成 wave3 阶段 A 门禁清零（2026-06-28）：5 张建模卡 CRLF + diagnostic_signals 断行 + 
next_session_hint: "下一步：① 欧阳锋终审 #33 大馨战队核心方法论卡片化（5 张目标卡 kdo pre-submit 5/5 PASS）；② 老顽童(Kimi)释放 #33 后，可继续领取 #34 社群知识生产失败模式库或 #28 lint 内容债（2656 WARNING）；③ 用户可随时用 .agent/amnesia-recovery-one-liners.md 中的口令让 Agent 失忆恢复。"---# 粘连修复，pre-submit 5 passed/0 failed"
  - "✅ 欧阳锋子代理完成 wave2 终审（2026-06-28）：16/16 张卡 `kdo pre-submit` 通过，status 更新为 reviewed，`reviewed_by: 欧阳锋`，`review_date: 2026-06-28`；已知遗留：frontmatter domain/related/tags/query_triggers `src_unknown` 占位（系统性债务）+ `yt-business-formula-parameter-iceberg` 与 B2 部分卡内容区占位 + `ai-short-drama-platform-policy-comparison` 缺 Critique/反事实，建议后续清理任务补齐"
  - "✅ 欧阳锋完成 wave1 终审（2026-06-28）：18/18 张卡通过审查，`kdo pre-submit` 抽查 6/6 通过，`kdo lint` 无新增 ERROR；全部卡片 status 更新为 reviewed，reviewed_by: 欧阳锋，review_date: 2026-06-28；`production-queue.md` 任务 #1 状态更新为 reviewed，`dashboard.md` Summary Review Done +1"
  - "✅ 欧阳锋完成刻意练习域 11 张卡终审：11/11 通过 `kdo pre-submit`、无 src_unknown、无死链、自攻击 🟡 问题已修复；全部卡片 status 更新为 reviewed，reviewed_by: 欧阳锋，review_date: 2026-06-28；任务 #2 状态更新为 reviewed"
  - "✅ 欧阳锋完成渠道增长域 25 张卡终审（2026-06-28）：25/25 通过；已知遗留清理已全部完成：13 张 case 卡 section 标准化 + 1 张 dk 目录/section 调整 + 1 张 concept 目录移动，2026-06-28 全部验收通过，11/11 文件 lint 0 ERROR"
  - "✅ 欧阳锋完成兰毅泛产品组织化 12 张卡终审（2026-06-28）：12/12 通过，`kdo pre-submit` 全量通过，4 张 P0 卡自攻击报告 status: fixed；全部卡片 status 更新为 reviewed，reviewed_by: 欧阳锋，review_date: 2026-06-28；审查中修复 3 张 case 卡 section 标题（关键证据/可迁移场景/教训/失败模式）、5 个文件目录移动（dk→dark-knowledges/，concept→concepts/，3 个 framework 从 concepts/→frameworks/）；全库 lint ERROR 从 618 降至 557"
  - "🆕 王语嫣已写渠道增长域遗留问题清理任务单（2026-06-28）：`60_feedback/tasks/task_20260628_wangyuyan-cleanup-channel-growth-residuals.md`，含 13 张 case section 标准化 + dk/concept 目录对齐；已入 `production-queue.md` 队列第 10 项，状态 queued，P2 优先级；已分配给黄药师执行"
  - "🆕 人员调整更新（2026-06-28）：Kimi 老顽童临时实例已完成全部任务（兰毅泛产品组织化 12 张卡 + 渠道增长域 25 张卡 + 刻意练习域 11 张卡 + 跨域桥接卡 + 10 张 case + 1 张 dk section 标准化），可关闭；Hermes 老顽童已领取 wave4（P2 清理）；WorkBuddy 老顽童负责第八批 dk 清零 pending_review；黄药师已完成渠道增长域遗留清理"
  - "✅ 欧阳锋完成 wave3 终审（2026-06-28）：14/14 张卡通过，`kdo pre-submit` 14/14 通过，`kdo lint` 无新增 ERROR；审查中清理 14 张卡 frontmatter 中 domain/related/tags 的 src_unknown 占位，并移动 3 个 framework 卡从 concepts/ 到 frameworks/；全库 lint ERROR 降至 533；全部卡片 status 更新为 reviewed，reviewed_by: 欧阳锋，review_date: 2026-06-28；已解锁 wave4 正式生产和第八批 dk 清零终审"
  - "✅ 欧阳锋完成第八批 dk 清零终审（2026-06-28）：10/10 张 dk 卡通过，`kdo pre-submit` 10/10 通过；`dark-knowledges/` 目录 lint ERROR 从 14 降至 0；审查中修复 4 张卡格式问题；全部卡片 status 更新为 reviewed，reviewed_by: 欧阳锋，review_date: 2026-06-28；全库 lint ERROR 降至 519；wave4 已完全解锁"
  - "✅ 欧阳锋完成渠道增长域 case section 标准化终审（2026-06-28）：11/11 文件通过，`kdo lint` 0 ERROR；1 处标题序号问题已现场修复；任务单 assignee 已修正为 Kimi 老顽童（实际完成）"
  - "✅ 欧阳锋确认 O-1 工作模式调整提案（2026-06-28）：审查角色有条件同意（低风险维持通过/退回，高风险/新域用风险标记+对比视图）；卡片三层化同意（先接口层后上下文层）；找老的干小的同意（P0 机械检查优先，P2 判断后置）；先投放再精修原则同意从 wave5 试点 `deploy_status: live`；O-1 已内化至 `.agent/ouyangfeng-context.md`，成为欧阳锋后续审查的默认工作模式"
  - "✅ 欧阳锋完成 wave5 终审（2026-06-28）：12/12 张卡 deep 通过，`kdo pre-submit` 12/12 通过；审查中修复 12 张卡 frontmatter（补 `status: reviewed`、统一 `reviewed_by: 欧阳锋`、更新 `updated_at`）；`production-queue.md` 任务 #9 状态更新为 reviewed；wave5 已完全解锁"
  - "✅ 欧阳锋完成 wave4 终审（2026-06-28）：15/15 张卡通过，`kdo pre-submit` 15/15 通过，`kdo lint` 目标卡无新增 ERROR；4.1 调研方法论域 8 张新卡 status 更新为 reviewed，reviewed_by: 欧阳锋，review_date: 2026-06-28；4.2 Master 域 7 张卡 domain 修正为 master，正文 src_unknown 占位清理；`production-queue.md` 任务 #8、`dashboard.md`、`60_feedback/tasks/review_20260628_ouyangfeng-wave4.md` 状态同步更新为 reviewed；wave5 已解锁"
  - "✅ WorkBuddy 完成 wave5 生产（2026-06-28）：12/12 张卡（CI 框架 3 + SATs 5 + 多智能体 4）`kdo pre-submit` 全部通过（12 passed/0 failed）；修复 wikilink 错误 4 处（`skill-半肥猫` → `tool-半肥猫`、`concepts/kimi-...` → `kimi-...`）；欧阳锋审查任务单已创建（`review_20260628_ouyangfeng-wave5.md`），状态 pending_review"
  - "✅ Hermes 老顽童完成 lint 基线清理 Batch 1（2026-06-28）：实际修复 784 个文件 frontmatter 机械错误（659 + 复查追加 125），frontmatter parse 类 ERROR 从 697 清零；`kdo lint` 剩余 890 个 ERROR 均为内容/section/source_refs/URL 类，需后续任务处理；`production-queue.md` / `dashboard.md` / 任务单已同步为 pending_review"
  - "✅ 洪七公修复 Hermes 老顽童 CLI Kimi API Key + thinking 400（2026-06-28/29）：WSL `~/.hermes/.env` + `~/.hermes/profiles/laowantong/.env` 同步更新新 key；清除 `~/.hermes/auth.json` kimi-coding 缓存；全局与 laowantong profile 的 `agent.reasoning_effort` 置空；清理所有 profile state.db 中 189 个会话的 `reasoning_config` 缓存；防御性补丁 `agent/anthropic_adapter.py` 强制所有 `kimi-*` 模型跳过 Anthropic `thinking` 参数；laowantong/default gateway 因 Feishu app_id 冲突无法与其他 gateway 并存，已停止并禁用 service，老顽童 CLI 模式可用"
  - "🟡 Hermes 全角色 WSL 实例因 WSL interop 损坏停摆（2026-06-30）：修复老顽童 thinking 400 过程中执行 `wsl --shutdown` 后，WSL2 的 Windows 程序互操作（binfmt_misc/WSLInterop）未恢复，导致 WSL 内无法执行任何 Windows 程序（cmd.exe/powershell.exe/notepad 均报 Exec format error）；影响范围：老顽童 CLI 自动跳转 Windows Terminal 失效、王语嫣/段王爷/洪七公/北丐 gateway 无响应、wechat MCP server 启动失败；已杀掉僵死的 gateway 进程；需重启 Windows 恢复 WSL interop"
  - "🆕 角色停车场机制上线（2026-06-28）：黄药师的'停车场清单'工作方式推广到全角色；已创建 `parking-lot-huangyaoshi.md` 和 `parking-lot-ouyangfeng.md`；`dashboard.md` 增加'角色停车场'汇总区块；P-1/P-6 已移入当前任务清单"
  - "✅ 黄药师完成 P0 任务（2026-06-28）：M-确认检测器稳定运行；KF-021 完成 188 个 source_refs hash 前缀→完整文件名（0 歧义，lint 522→519）；Task Q 出链门禁上线（Synthesis <2 links WARN + 跨域检测 WARN）"
  - "✅ 黄药师完成 P-1 query 分层排序（2026-06-28）：`kdo query` 实现 Core→Extended→Reference 三层排序；Core 为 domains/frameworks/systems 目录卡，Extended 为 tools/concepts/cases/dk，Reference 为 raw/_archive/trust_low；Graph RAG 和 BM25 两条路径及 `--save` 输出均生效"
  - "🆕 黄药师开始 P-6 research skill 适配（2026-06-28）：将 WebSearch/WebFetch/Agent 工具调用层翻译为 kdo-tools，让 Hermes Agent 也能使用；黄药师当前最后一项 P1 任务"
  - "🆕 lint Batch 2 子任务拆分并入队（2026-06-28）：A case section（130 文件）、B dk section（43 文件）由 WorkBuddy 老顽童负责，C source_refs（约 107 文件 / 176 错误）由黄药师负责；890 ERROR 中 690 为 Batch1 修复后基线、200 为 frontmatter 修复后暴露的内容级错误；Hermes 老顽童 Batch1 完成后待命"
  - "🆕 125 个原 `colon_in_scalar_other` 文件已确认无 YAML 解析错误，按当前错误类型归入 Batch 2-A/B/C，不单独建 YAML 解析任务"
  - "✅ 黄药师完成 Batch 2-C（2026-06-28）：URL 跳过补丁上线，source_refs 类 ERROR 清零；合并路径拆分 9 / URL/dict 降级 3 / pending_archive 272 / 空 source_refs→src_unknown 30，合计 314；lint ERROR 从 537 降至 425（↓112）；任务单已更新执行报告，production-queue.md 状态为 done/pending_review"
  - "🆕 Wave 6 新盲区诊断任务已入队（2026-06-28）：王语嫣负责基于周报和对话记录识别 1-2 个新盲区并拆任务入队"
  - "🆕 dark-knowledges 第八批清零任务已创建（2026-06-28）：`60_feedback/tasks/task_20260628_laowantong-dark-knowledges-batch8.md`，10 张问题 dk 卡，WorkBuddy 老顽童负责，目标使 `dark-knowledges/` 目录 lint ERROR 归零"
  - "✅ 黄药师完成渠道增长域遗留清理（2026-06-28）：`30_wiki/dk/dk-yitang-channel-exploration-traps.md` 移至 `30_wiki/dark-knowledges/`，`30_wiki/frameworks/concept-yitang-channel-lean-validation-bridge.md` 移至 `30_wiki/concepts/`，全库 related wikilink 已更新，顺手修复 amazon/novel-app/topcity 3 张 case 卡 section；P1 剩余 10 张 case + 1 张 dk section 调整已由 Kimi 老顽童完成并通过欧阳锋终审"
  - "🆕 队列锁已上线（2026-06-28）：黄药师实现 `90_control/scripts/queue_lock.py`，锁目录 `90_control/.queue-locks/`，超时 300s 自动过期，已登记到 `.agent/toolkit.md` 第〇条；多老顽童实例可安全并行更新 `production-queue.md` / `dashboard.md` / `.agent/context.md`；`.agent/laowantong-context.md` 已加入加锁/释放口令"
  - "✅ 欧阳锋完成 `framework-kdo-self-attack` 终审：正文 174 行、结构完整、失败模式具体、related 全部有效、`kdo pre-submit` 通过；status 更新为 reviewed，reviewed_by: 欧阳锋"
  - "✅ 洪七公：00_inbox/一堂五步法之增长 59张高密度知识图已完成OCR(PaddleOCR v5)+VLM(MiniMax-M3)处理；59/59成功，平均置信度0.94，19张双层JSON已修复；产出见目录下 *_paddle_ocr.txt、*_vlm_desc.md、README-VLM描述汇总.md、README-素材处理总汇总.md"
  - "✅ P0-A 单元模型域已封版：全16张卡yaml.safe_load通过、0 broken link、0 domain typo；王语嫣复核通过；欧阳锋最终审查dk-单元模型-对抗小抄通过，status更新为reviewed；报告见 audit_20260627_ouyangfeng-p0a-final-review.md"
  - "✅ P0-B 科学决策域：前17张核心卡已验收通过，剩余14张(2 dk+11 case+1 enrich)已全部审查通过；欧阳锋最终审查发现 ROI案例01 仍为27行薄卡，已九层深挖重写；其余13张结构达标，status 已更新为 reviewed；报告见 audit_20260626_ouyangfeng-p0b-final-review.md"
  - "✅ case-科学决策-深度案例01：已由老顽童九层深挖重写，欧阳锋最终审查通过，status 更新为 reviewed"
  - "✅ 泛产品设计35张卡：19张落地卡旧→新迁移(concept→tool，引用替换，归档)，14张需求/审美卡frontmatter升级，20张新卡related补全至≥8；kdo lint零新增错误"
  - "🆕 角色再调整(2026-06-27)：王语嫣升级为 Content Consultant + Direction Gatekeeper + Dashboard Maintainer + Task Annotator，负责内容咨询、任务标注、方向把关、production-queue.md / dashboard.md / kb-evolution-direction.md 维护；欧阳锋全面负责所有卡片审查终审与抽查；王语嫣不再做卡片审查/验收"
  - "🆕 临时生产分流(2026-06-27)：Hermes 老顽童负责历史批量工单 waves 1-5；启动 Kimi 老顽童临时实例负责 2026-06-27 新标注任务（刻意练习域、渠道增长域、兰毅泛产品组织）及跨域桥接卡；欧阳锋/黄药师无感知"
  - "✅ 九层深挖+六层交叉验证→Skill双桥接(Claude Code+Hermes)；laowantong-context加质量闸门(100行底线/素材消费率/六段齐全/失败模式具体)"
  - "✅ Hermes老顽童API从DeepSeek切至Kimi(kimi-for-coding)"
  - "🟢 王语嫣/欧阳锋/老顽童不再自己跑kdo lint或kdo index --rebuild——全库扫描由黄药师维护"
  - "🟡 决策域(66卡)待建domain digest；需求分析域待建；五步法子域待建"
  - "🟢 王语嫣完成刻意练习域+渠道增长域九层深挖/六层交叉验证；产出 diag_20260627_wangyuyan-deliberate-practice-nine-layer.md + diag_20260627_wangyuyan-channel-growth-nine-layer.md"
  - "🆕 王语嫣补做跨域桥接深挖：渠道增长×单元模型、渠道增长×精益创业、刻意练习×AI协作；产出 diag_20260627_wangyuyan-cross-domain-bridge-supplement.md"
  - "🆕 任务单已追加3张跨域桥接卡：framework-yitang-channel-unit-economics、concept-yitang-channel-lean-validation-bridge、framework-ai-deliberate-practice-loop；待老顽童生产"
  - "🆕 王语嫣与用户共同提炼方法论模型：method-dialogue-driven-kb-evolution（对话驱动知识库进化五环模型），已写入 60_feedback/methods/"
  - "🆕 王语嫣与用户共同提炼第二方法论模型：method-systematic-dialogue-kb-evolution-hybrid（冷热混合进化模型），明确系统扫描负责发现机会、对话负责创造高价值桥接"
  - "🆕 每周一 9:07 定时任务已创建（cron id: 011ab8b1），自动生成 kb-evolution-signals-weekly.md"
  - "🆕 共享文件已创建：.agent/kb-evolution-direction.md（所有角色必读）"
  - "🆕 统一生产队列已创建：70_product/tasks/production-queue.md；老顽童按队列顺序领取，欧阳锋按队列顺序审核；当前队列前3项：wave1 门禁清理 / 刻意练习域 / 渠道增长域"
  - "🆕 失忆恢复口令文件已创建：.agent/amnesia-recovery-one-liners.md；用户可用一句话让任何 Agent 快速进入状态，无需搜索数据库"
  - "🆕 用户明确长期原则（2026-06-28）：追求知识库深度、扩宽边界、无限追求健壮和发展、提高 Agent 咨询能力边界；若用户急功近利，Agent 应阻止并给正确建议。已写入 .agent/kb-evolution-direction.md 和 20_memory/operating-principles.md"
  - "🆕 wave1 审查任务单已创建（2026-06-28）：`60_feedback/tasks/review_20260628_ouyangfeng-wave1.md`，18 张卡清单+审查标准+判定规则；`production-queue.md` 第 1 项来源文件已指向该任务单；`ouyangfeng-context.md` 已提醒欧阳锋 wave 类任务读专门审查任务单，不要读 `laowantong-batch-2026-06-20.md` 全文"
  - "✅ 羊奶「卖地图」跨域桥接卡生产 reviewed（2026-06-29）：欧阳锋终审通过；3 张目标卡 `kdo lint` 0 ERROR/WARNING、`kdo pre-submit` 无错误；修复索引补录、section 标题、Critique 外部反对者/关键术语、相邻域 related 回链；status 更新为 reviewed，reviewed_by: 欧阳锋，review_date: 2026-06-29"
  - "🆕 Kimi 从 YAI 对话中沉淀咨询技能（2026-06-29）：用户追问是否会遗忘，已将 9 项可迁移咨询技能写入 `20_memory/kimi-consulting-skills-from-yai-20260629.md`；包含诉求翻译、冷热分离、案例抽象、元反馈识别、队列管理、跨域桥接、验证汇报、基线接受、持久化认知"
  - "🆕 Vikki-human-speech（讲人话/去 AI 味）skill 角色归属确认（2026-06-29）：该 skill 为文案写作/内容润色类，位于 `.claude/skills/content-production-polish/` 和 `40_outputs/capabilities/skills/shared/content-production-polish/`；洪七公（多模态/视觉）不学；老顽童（Producer）学基础版用于卡片/文章生产去 AI 味；段王爷（Publisher）学完整版用于 ship 阶段渠道改写（口播稿/小红书/公众号/直播话术）"
  - "🆕 Vikki + 大馨战队群聊认知提炼任务已有机融合并入队（2026-06-30）：#30 content-production-polish skill 2.0 升级（Vikki 信息×情绪 + 大馨 6 维度/4 模板/5 人性开关，老顽童）；#31 KDO 卡片质量标签体系（Vikki 五标签 + 大馨品牌三度，黄药师）；#32 开源知识使用边界概念卡（Vikki 蒸馏事件 + 大馨 抄作业/AI 拆解边界，老顽童）；#33 大馨核心方法论卡片化（5-6 张卡，老顽童）；#34 社群知识生产失败模式库（Vikki 5 + 大馨 5 融合，老顽童）；来源文件 `0071Vikki战队-2群 · 认知精华提炼.md` + `0017大馨战队 · 短视频内容拆解方法论精华提炼.md`"
  - "🆕 素材文件命名规范工具卡已创建（2026-06-30）：`30_wiki/tools/tool-asset-file-naming-convention.md`，提出素材七要素命名法（类型_项目_场景_来源_版权状态_技术参数_日期_序号），区别于月白设计成品八要素命名法；pre-submit PASS"
  - "📝 本次会话复盘已写入（2026-06-30）：`20_memory/session-retro-20260630-vikki-daxin-asset-naming.md`；关键决策：Vikki/大馨 5 任务融合入队、素材七要素命名法、AI 自动打标签采用半自动工作流"
  - "📝 Kimi Code CLI 专项能力复盘已同步（2026-06-30）：`20_memory/kimi-capability-retro-20260630.md` + `agent复盘/Kimi/2026-06-30.md`；平均分 7.6/10；新增 5 条错误模式库记录；Keep/Improve/Add/Stop 四象限已沉淀；Kimi 启动时应自动读取本复盘"


---

## 📢 全厂通知（2026-06-19）

- **`.agent/startup.md` 已上线**：每个 Agent 启动后、领任务前必须先读此文件，3 分钟了解工厂全局与当前状态。
- **`.agent/infrastructure-bulletin.md` 同步生效**：新增“工具登记四步法”——新工具/脚本必须 ① 放入 `40_outputs/code/scripts/` ② 登记到 `README.md` ③ 复杂逻辑写 skill ④ skill 之间互引。不登记 = 不存在。

> 请各角色在下次启动时确认已阅读以上两个文件。已同步更新 `.agent/<role>-context.md` 中各角色启动步骤，将两文件列为第 0 步必读。

## 2026-06-12 变更

### Hermes 全貌（最终态）
| Agent | WSL Service | Feishu Channel | Model |
|:--|:--|:--|:--|
| 洪七公 | hermes-gateway-beikai | oc_71fc... | deepseek-v4-pro |
| 段王爷 | hermes-gateway-duanwangye | oc_f3a9... | deepseek-v4-pro |
| 王语嫣 | hermes-gateway-wangyuyan 🆕 | oc_b8bf... | deepseek-v4-pro |
| 老顽童 | CLI `hermes` | 无 | deepseek-v4-pro |

### 关键教训
- P-27: Provider迁移先查 models_dev_cache 确认 SDK 协议
- P-28: API大规模异常先查公告再调参
- 黄药师铁律: 先诊断后动手，用户说别改就冻结

> ⚠️ **角色中立文件** — 只放共享状态。不写 "你是谁" 类身份描述。
> 各角色的身份定义、SOP、启动指令在 `.agent/<role>-context.md`。
> 看到 "你是谁" 段落 → 删掉，移到对应角色文件。不要在这里写。

## 角色部署

| 角色 | 运行位置 | 工具 |
|------|---------|------|
| 欧阳锋（Architect） | Kimi Code CLI | 审查/深挖重写/协调/拍板 |
| 黄药师（Builder） | Claude Code（Windows 终端） | KDO CLI 开发/基建/lint |
| 王语嫣（Content Consultant + Direction Gatekeeper + Dashboard Maintainer + Task Annotator） | Kimi Code CLI | 内容咨询/方向把关/队列看板维护/任务标注 |
| 老顽童（Producer） | **Hermes CLI（Kimi API）** | 卡片/文章量产 |
| 洪七公（Multimodal） | Hermes agent → 飞书 | 视觉/设计/prompt |
| 段王爷（Publisher） | Hermes agent → 飞书 | 发布/反馈/版本 |

> 角色专属 context 见 `.agent/ouyangfeng-context.md`、`.agent/huangyaoshi-context.md`、`.agent/wangyuyan-context.md`、`.agent/laowantong-context.md`、`.agent/hongqigong-context.md`、`.agent/duanwangye-context.md`。

## 关键路径

| 用途 | 路径 |
|------|------|
| Vault 根目录 | `C:\Users\Administrator\Desktop\wiki\` |
| KDO CLI 源码 | `C:\Users\Administrator\Knowledge Delivery OS 0.0.1\kdo\` |

## 模型与环境

- **模型**：DeepSeek（deepseek-v4-pro，老顽童/洪七公/段王爷/王语嫣共用）；欧阳锋仍用 Kimi 订阅
- **飞书 WebSocket**：cc-connect 和 Hermes 均出现 keepalive ping timeout。重启即修复。P-6 已记录。
- **切模型**：涉及五层配置（`.bashrc` / 注册表 / systemd drop-in / `cc-connect config.toml` / session 缓存）。详见 `pitfalls.md`

## 当前共享状态

### 各角色当前任务
- **黄药师**：KF-020+021全修 + S4-1 aliases + kdo_lint(2344→85) + 决策域研究(2卡A级)
- **老顽童**：战略域 PPT 补强 3/3 验收通过；待命接新任务
- **王语嫣**：完成角色边界调整；负责内容咨询、任务标注、方向把关；维护 production-queue.md / dashboard.md / kb-evolution-direction.md；完成自攻击方法论框架卡并已入队待欧阳锋审核；跟踪 wave1 / 刻意练习域 / 渠道增长域生产进度
- **欧阳锋**：月度抽检模式
- **洪七公**：待命
- **段王爷**：待命

### 2026-06-18 里程碑
- **全库首次 P0=P1=YAML=0**（6/13 以来第一次三项同时归零）
- 老顽童 index/log 元页面 source_refs 从 760→2（`system-index`/`system-log`）
- 全库 clean=1175

### 2026-06-17/18 关键结果
- 决策域研究完成：Value-ROI dk + Y模型哲学根基(欧阳锋A级)
- KF-020 全修：45张 enriched/reviewed 卡 00_inbox→10_raw/sources
- KF-021 95%：681张 hash 前缀→完整文件名
- S4-1 aliases：schema + Graph RAG 搜索索引
- kdo_lint：2344→85 (96%误报清零)
- 王语嫣复盘：P0=P1=0 clean=1193
- 470 skill 重分类为 tool/concept（欧阳锋 taxonomy 裁决执行）
- 231 张 draft 精修池已识别（conf≥0.7+related 非空）
- MinerU 文档化入 wiki + toolkit
- 决策域第一张 dk 卡产出（Value-overrides-ROI）
- 决策域 KF-020 违规报告送审王语嫣

### 2026-06-16 关键结果
- 全库 P0=0, YAML=0, Clean=586
- 老顽童全域案例回溯 35 张（主动执行 KF-025 三问自检）
- OCR 368 张 → raw/ocr/ 分层隔离
- 14 对重复卡片去重, 6 张 deprecated 归档
- kdo query --trust/--view/--save/--template book 上线
- KF-025 + S4 上线
  - `60_feedback/itingnao/medical-cabinet-longterm/method-medical-cabinet-hospital-scene-model.md`
  - `60_feedback/itingnao/medical-cabinet-longterm/method-medical-cabinet-scale-model.md`
- **待验证重点**：单设备真实流水、医院准入政策、合规成本、资金来源、团队产能、供应链授权
- **下一步**：用户/团队线下完成验证任务后，把结果写回 task 文件或 60_feedback/comments/，Kimi 据此更新模型卡片

### KDO CLI 状态
- 47 .py 文件，~13,800 行，15 测试文件
- **pytest**：526/528 passing + 2 pre-existing CSRF failures + 1 skip
- **Graph RAG**：226 entities, 721 chunks, 1252 relations
- **kdo stale**：25 tests pass，待欧阳锋审查后 commit
- 坚果云备份 ✅

### Design 域
- Eagle（图轨）+ Obsidian（文轨），双轨三层。第一批编译已完成 ✅
- 3 张概念卡：AIGC设计基础（生图原理+提示词基本功）、口喷设计范式+电商全流程、Leo文创IP案例
- 源素材：月白（一堂）AIGC设计课程口述 3 期 → ingested → enriched → indexed → graphed
- 文轨骨架已立，待后续视觉资产桥接（Eagle 图轨）

### 攻击者多样性规则（软约束）
- 同一域内，每5张卡至少引入1位新攻击者。纯 Kahneman+Taleb 组合需替换一位。

## 🆕 2026-06-07：黄药师审查老顽童清单体笔记批次

### 交付物
- 新增：`yt-note-checklist-concept` / `yt-note-ai-human-division` / `yt-note-five-levels-training` / `yt-note-live-field-skill` / `dk-yt-checklist-max-common-divisor`
- 更新：`yt-personal-checklist-notes`（v1→v2）
- 文章：`从清单体到AI时代的认知重构——一堂Truman笔记法的三个核心洞察`

### 自动门结果
- V1.5：2 张 concept 卡 PASS，2 张 tool 卡未覆盖
- Lint：1 warning（dk 卡未入 index）
- Wikilink：文章 6/6 有效，Synthesis 3 个死链

### 技术债务（P0-P2）
- P0：article 未注册 kdo state.json → validate 不可用；article 缺 source_refs → 溯源链断
- P1：3 个 Synthesis 死链；dk 卡未入 index；source_refs 中"请单"→应为"清单"
- P2：文章与 dk 卡内容重叠未区分；yt-personal-checklist-notes status 仍是 enriched

### 深度不足（待与用户探讨）
1. **文章是"读后感"而非"知识合成"**——第一人称体验（"听完后我的感觉是"）占主导，缺少结构化知识创造。读者知道作者感受深，不知道怎么做
2. **暗知识与概念卡重叠未桥接**——文章第四节与 dk-yt-checklist-max-common-divisor 主题相同（最大公约数/AI分工），但无相互引用或层次区分
3. **攻击者论证在文章中降级为"提及"**——卡片 Critique 有真正的 Kahneman/Taleb 对话，文章只写"Kahneman在卡片中提醒我们"——是引用卡片而非与攻击者对话
4. **Synthesis 有免责式死链**——"如果存在这张卡片"是免责声明，不是负责任的 Synthesis。写卡时不验证目标存在，等于画空中楼阁
5. **文章缺少"边界与反例"**——概念卡有 Critique（内部局限+外部攻击+不要用），文章只有正面论证，变成推广文

### Infra 暴露的系统性缺口
1. Tool 卡 v1.5 校验缺失
2. Synthesis wikilink 无自动死链检测
3. Article 可绕过 kdo produce 管线创建
4. 暗知识卡（dk-*）无标准结构校验
5. source_refs 文件名无 fuzzy match 检测

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
- [ ] P-25：Claude Code 2.1.168 viewport 初始化 bug（(0/0) 不可滚动，鼠标键盘均失效） — 待确认是否已修复
- [ ] **禁止用 `/memory` 替代上述更新**
