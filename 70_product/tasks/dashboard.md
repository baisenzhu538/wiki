---
updated: 2026-07-07
---

> ⚠️ **2026-06-27 重要更新**：老顽童生产任务已统一进入 `70_product/tasks/production-queue.md`，按队列顺序领取和审核。本 dashboard 仍保留历史任务全景，但**当前待生产/待审核任务请以 production-queue.md 为准**。
> 🆕 **2026-07-04 更新**：王语嫣已开 #62/#63 任务单并入队。#62 黄药师处理 Agent Prompt 设计规范微债务；#63 老顽童补产一行双三角第二批 4 张 case 卡。

# Task Dashboard

Generated: 2026-06-26T21:00:00+00:00

| ID | Title | Status | Assigned | Priority | File |
|----|-------|--------|----------|----------|------|
| p0a-unit-model-final-review | P0-A 单元模型域补产卡最终审查 | review_done | 欧阳锋 | P0 | audit_20260627_ouyangfeng-p0a-final-review.md |
| p0b-decision-science-final-review | P0-B 科学决策域剩余 14 张卡最终审查 | review_done | 欧阳锋 | P0 | audit_20260626_ouyangfeng-p0b-final-review.md |
| panproduct-35-cards | 泛产品设计 35 张卡：老顽童生产完成 | review_done | 欧阳锋 | P0 | audit_20260626_ouyangfeng-panproduct-review.md |
| panproduct-migrate-19 | 19 张落地卡旧→新迁移（concept→tool，引用替换，归档） | done | 黄药师 | P0 | — |
| panproduct-upgrade-14 | 14 张需求/审美概念卡 frontmatter 升级 | done | 黄药师 | P0 | — |
| panproduct-related-fix | 20 张新卡 related 补全（≥5条） | done | 黄药师 | P0 | — |
| nine-layer-skill | 九层深挖 Skill 双桥接（Claude Code + Hermes） | done | 黄药师 | P0 | — |
| six-layer-skill | 六层交叉验证 Skill 双桥接（Claude Code + Hermes） | done | 黄药师 | P0 | — |
| ouyangfeng-context | 欧阳锋 context 重写（Obsidian Claude → Kimi Code CLI） | done | 黄药师 | P0 | — |
| wangyuyan-context | 王语嫣 context 精简（370→103行，砍跨域职责） | done | 黄药师 | P0 | — |
| s4-1-aliases-field | S4-1：卡片增加 aliases 字段，提升搜索体验 | done | 黄药师 | P0 | huangyaoshi-next-tasks.md |
| kf-021-source-refs-hash-completion | KF-021：705 张 source_refs hash 前缀补全为完整文件名 | done | 黄药师 | P1 | kf021-spot-check-report-2026-06-15.md |
| section-22-30-cards | 第二十二节 30 张卡深度精修 | A- 通过 | 老顽童 | P0 | section-22-laowantong-acceptance-2026-06-17.md |
| section-22-source-cleanup | 第二十二节：13 张卡 source_refs 残留清理 | done | 老顽童 | P1 | section-22-laowantong-acceptance-2026-06-17.md |
| section-23-30-cards | 第二十三节：精修池 30 张 draft 卡深度精修 | A 通过 | 老顽童 | P0 | section-23-laowantong-acceptance-2026-06-18.md |
| section-24-30-cards | 第二十四节：再精修 30 张 draft 卡 | A- 通过 | 老顽童 | P0 | section-24-laowantong-acceptance-2026-06-18.md |
| kf-021-cleanup-content-cards | KF-021 收尾：33 张 content 卡 source 缺失处理 | done | 老顽童 | P1 | laowantong-next-tasks.md |
| kf-021-cleanup-meta-pages | KF-021 收尾：清理 index / log 元页面 source_refs | done | 老顽童 | P2 | laowantong-next-tasks.md |
| quality-gate-automation-v15 | 质量门自动化 — kdo validate --v15 | pending | 黄药师 | P1 | quality-gate-automation-v15.md |
| domain-digest-cards | 按域摘要卡——agent 入职加速层 | pending | 黄药师 | P3 | domain-digest-cards.md |
| kdo-scaffold-v15 | kdo scaffold — 为缺失 v1.5 信号的卡片自动生成升级骨架 | done | 黄药师 | P0 | kdo-scaffold-v15.md |
| sprint-12-backfill-card-behavioral-requirements | Sprint 12：回溯升级——已有卡片补齐 v1.5 行为转化三要件 | done | 黄药师 | P0 | sprint-12-backfill-card-behavioral-requirements.md |
| fix-validate-v15-domain-filter | 修复 kdo validate --v15 的 --domain 过滤失效 | done | 黄药师 | P1 | fix-validate-v15-domain-filter.md |
| validate-v15-upgrade-plan | kdo validate --v15 --upgrade-plan：从诊断到可行动的升级路线图 | done | 黄药师 | P1 | validate-v15-upgrade-plan.md |
| huangyaoshi-codex-lessons-review | 审查请求：Codex 调试复盘 → KDO 系统改进 4 条建议 | reviewed | 欧阳锋 | - | huangyaoshi-codex-lessons-review.md | 欧阳锋确认：建议 2 做 P0、建议 4 做 P1、建议 1 暂缓 P2、建议 3 本阶段不做 P3；黄药师执行建议 2 和 4 |
| proposal-ouyangfeng-2026-06-14 | 建议书：欧阳锋工作模式调整与知识库三层化 | 已确认，待实施 | 欧阳锋 | P1 | proposal-ouyangfeng-workmode-2026-06-14.md | 欧阳锋已逐条确认：审查角色有条件同意、卡片三层化同意、找老的干小的同意、先投放再精修原则同意从 wave5 试点；O-1 已升级为实施阶段，待拆分为 production-queue 任务 |
| laowantong-batch-2026-06-20 | 老顽童批量工单：全库待办一次性打包（5 波） | in_progress (wave2 reviewed, wave3 reviewed, 第八批 reviewed, wave4 reviewed, wave5 queued for WorkBuddy) | 老顽童 | P0-P2 | review_20260628_ouyangfeng-wave4.md | wave2 16/16 欧阳锋子代理终审通过；wave3 14/14 欧阳锋终审通过；第八批 10/10 dk 卡欧阳锋终审通过；wave4 15/15 欧阳锋终审通过（4.2 Master 域 7 张规范化 + 4.1 调研方法论域 8 张新建），status 更新为 reviewed；wave5 预分配给 WorkBuddy，已解锁 |
| review_20260628_ouyangfeng-wave1 | 欧阳锋审核：wave1 门禁快速清理 18 张卡 | reviewed | 欧阳锋 | P0 | review_20260628_ouyangfeng-wave1.md | 欧阳锋终审通过：18/18 卡 status 更新为 reviewed |
| task_20260627-deliberate-practice-cards | 元能力-刻意练习域卡片化（含 AI 协作桥接） | reviewed | 欧阳锋 | P1 | task_20260627_laowantong-deliberate-practice-cards.md |
| task_20260627-channel-growth-cards | 渠道增长域卡片化（含 2 张跨域桥接卡） | reviewed | 欧阳锋 | P1 | review_20260628_ouyangfeng-channel-growth.md | 欧阳锋终审通过：25/25 卡 status 更新为 reviewed；遗留 case section / dk 目录 / concept 目录债务已记录 |
| task_20260627-lanyi-panproduct-organization | 兰毅泛产品组织化 + 泛产品设计域升级 | reviewed | 欧阳锋 | P0-P1 | task_20260627_laowantong-lanyi-panproduct-organization.md | 欧阳锋终审通过：12/12 张卡 status 更新为 reviewed；审查中修复 3 张 case section + 5 个目录移动 |
| task_20260628_laowantong-dark-knowledges-batch8 | dark-knowledges 第八批清零：补齐 10 张问题 dk 卡 | reviewed | 欧阳锋 | P0 | task_20260628_laowantong-dark-knowledges-batch8.md | 欧阳锋终审通过：10/10 张 dk 卡 status 更新为 reviewed；dark-knowledges 目录 lint ERROR 归零；审查中修复 4 张卡格式问题 |
| task_20260628_wangyuyan-cleanup-channel-growth-residuals | 渠道增长域终审遗留问题清理（已完成） | done | 黄药师 | P2 | task_20260628_wangyuyan-cleanup-channel-growth-residuals.md | 黄药师已完成 dk/concept 目录移动 + 全库 related 链接更新 + 顺手修复 3 张 case 卡；P1 已拆分 |
| task_20260628_laowantong-case-section-standardization | 渠道增长域 10 张 case + 1 张 dk section 标准化 | reviewed | 欧阳锋 | P1 | task_20260628_laowantong-case-section-standardization.md | 欧阳锋终审通过：11/11 文件 `kdo lint` 0 ERROR；1 处标题序号问题已现场修复 |
| master-7-cards-layer-and-boundary | Master 域 7 张卡规范化 | reviewed | 欧阳锋 | P1 | master-7-cards-layer-and-boundary.md | Hermes 老顽童完成规范化；欧阳锋终审通过：7/7 卡 `kdo pre-submit` + `kdo lint` 通过；审查中修复 20 个缺失 source_refs 为 pending_archive 占位 |
| task_20260628_hermes-lint-baseline-cleanup-batch1 | Hermes lint 基线清理 Batch 1：机械性 frontmatter 修复 | reviewed | Hermes 老顽童 | P1 | task_20260628_hermes-lint-baseline-cleanup-batch1.md | 欧阳锋终审通过：783/784 safe batch 文件 frontmatter 可解析，`kdo lint` 无 frontmatter parse 类 ERROR；1 个 `_archive/plan_20260531_data-curator-v1.1.md` 历史残余 YAML 缩进未修复，已记录在任务单 |
| task_20260628_laowantong-lint-batch2-case-sections | lint Batch 2-A：case section 标准化补全 | reviewed | WorkBuddy 老顽童 | P1 | task_20260628_laowantong-lint-batch2-case-sections.md | 欧阳锋终审通过：130/130 case 文件已真实修改，`kdo lint` Case section ERROR 清零；vault backup 自动 commit 导致 `git diff HEAD` 失效的根因已记录 |
| task_20260628_laowantong-lint-batch2-dk-sections | lint Batch 2-B：dk section 标准化补全 | reviewed | WorkBuddy 老顽童 | P1 | task_20260628_laowantong-lint-batch2-dk-sections.md | 欧阳锋终审通过：57/57 dk 文件已真实修改，`kdo lint` DK section ERROR 清零；原 43 清单 + 14 个 extra 文件均处理 |
| task_20260628_huangyaoshi-lint-batch2-source-refs | lint Batch 2-C：source_refs 真实存在性清理 | reviewed | 黄药师/老顽童 | P1 | task_20260628_huangyaoshi-lint-batch2-source-refs.md | 欧阳锋终审通过：黄药师修复 workspace.py 三项 skip 规则 + 中文乱码匹配；老顽童真实修改 90 个文件添加 `10_raw/sources/` 前缀；`kdo lint` source_refs ERROR 清零；Batch 2 机械性 lint 清零 |
| task_20260628_wangyuyan-wave6-blindspot-diagnosis | Wave 6 新盲区探索诊断 | reviewed | 王语嫣 | P2 | task_20260628_wangyuyan-wave6-blindspot-diagnosis.md | 欧阳锋终审通过：识别决策科学域系统化 + 需求分析域深化两个新盲区；产出诊断报告并拆分为 #21/#22 |
| task_20260628_wangyuyan-next-phase-orchestration | 下一阶段任务编排建议 | confirmed | 王语嫣 | P1 | task_20260628_wangyuyan-next-phase-orchestration.md | 王语嫣已拍板：补链拆为 B1/B2/B3，#18/#19/#20 入队；related 分层标准不按 ≥8 一刀切 |
| task_20260628_laowantong-link-repair-b1-frontmatter-related | B1：frontmatter related 字段 src_unknown 占位清理 | reviewed | 老顽童(WorkBuddy) | P1 | task_20260628_laowantong-link-repair-b1-frontmatter-related.md | 欧阳锋终审通过：274 文件真实修改，related 字段 src_unknown 剩余 0，pending_unknown 1190 与报告一致，`kdo lint` 0 ERROR |
| task_20260628_laowantong-link-repair-b2-synthesis-section | B2：Synthesis section 死链/占位清理 | reviewed | 老顽童(WorkBuddy) | P1 | task_20260628_laowantong-link-repair-b2-synthesis-section.md | 欧阳锋终审通过：66 文件 body src_unknown 清零，替换 1056 处；kdo lint 140 ERROR 为历史遗留（case section/tool-concept 空 source_refs），无新增；额外修复 2 个 YAML 格式 |
| task_20260628_laowantong-link-repair-b3-island-cards | B3：孤岛卡片 kdo link-suggest 批量推荐 | reviewed | 老顽童(WorkBuddy) | P2 | task_20260628_laowantong-link-repair-b3-island-cards.md | 欧阳锋终审通过：2014 YAML 引号修复 + 163 bare id 包裹 + 119 句子删除 + 33 张孤岛补真实 wikilink + pending_unknown.md 移到 system/；孤岛卡片清零；lint 140 ERROR 全为历史遗留无新增；pre-submit 抽检 5/5 PASS |
| task_20260628_laowantong-wave6-decision-science-systematization | Wave 6-A：决策科学域系统化 | reviewed | 老顽童(Hermes) | P1 | task_20260628_laowantong-wave6-decision-science-systematization.md | 欧阳锋终审通过：升级现有 digest + 新建 2 framework + 1 dk + 1 case；5 张新卡无新增 ERROR；决策科学域系统化完成 |
| task_20260628_laowantong-wave6-demand-analysis-deepening | Wave 6-B：需求分析域深化 | reviewed | 老顽童(Hermes) | P1 | task_20260628_laowantong-wave6-demand-analysis-deepening.md | 欧阳锋终审通过：建 1 index + 2 case + 1 framework + 1 dk；修复 2 张英文 section 标题、5 张卡 enriched→reviewed、index.md 追加新卡；需求分析域深化完成 |
| task_20260629_huangyaoshi-lint-a1-empty-source-refs | A1：空 source_refs 清理 | queued | 黄药师 | P1 | task_20260629_huangyaoshi-lint-a1-empty-source-refs.md | 修复 8 个 concept/tool 空 source_refs；找不到真实源文件的用 pending_archive 占位；使 source_refs 类 ERROR 清零 |
| task_20260629_laowantong-lint-a2-case-section-completion | A2：case section 缺失补全 | queued | 老顽童(Hermes) | P1 | task_20260629_laowantong-lint-a2-case-section-completion.md | 补齐 132 张 case 卡的 4 个标准 section；没素材用 src_unknown + 待补占位；批量提交 `--expect-changes 132` |
| review_20260627_ouyangfeng-self-attack-framework | 欧阳锋审核：自攻击方法论框架卡 | reviewed | 欧阳锋 | P1 | 30_wiki/frameworks/framework-kdo-self-attack.md |
| auto-label-accuracy-baseline-vs-gold-standard | Auto-label 准确率基线 vs Gold Standard：34.8%（47/135） | draft | - | - | task-20260531-huangyaoshi-label-accuracy-fix.md |
| domain-prompt-engineering-andre-ng | 提示词工程域：吴恩达课程消化 + 人机协作技能内化 | completed | 黄药师 | P0 | domain-prompt-engineering-andre-ng.md |
| domain-xiang-jiang-deep-digestion | 讲香域深度消化 + 架构重建 | completed | 黄药师 | P0 | domain-xiang-jiang-deep-digestion.md |
| sprint-10-fill-remaining-related-edges | Sprint 10：填剩余 related 图边 + 收尾管理域 | completed | 黄药师 | P0 | sprint-10-fill-remaining-related-edges.md |
| sprint-11-cognitive-upgrade-framework | Sprint 11：AI思维卡素材 ingest + 认知升级十步框架萃取 | completed | 黄药师 | P0 | sprint-11-cognitive-upgrade-framework.md |
| sprint-6-agent-native-upgrade-all-cards | Sprint 6：全量卡片 Agent-Native 格式升级 | completed | 黄药师 | P0 | sprint-6-agent-native-upgrade-all-cards.md |
| sprint-7-fill-related-edges | Sprint 7：填充 panproduct 域图边 + 清理残留 00_inbox | closed_incomplete | 黄药师 | P0 | sprint-7-fill-related-edges.md |
| sprint-8-finish-related-edges | Sprint 8：完成 panproduct 图边 + 收尾 00_inbox | completed | 黄药师 | P0 | sprint-8-finish-related-edges.md |
| sprint-9-cleanup-source-refs-query-triggers | Sprint 9：修复 source_refs 空值 + query_triggers 污染 | completed | 黄药师 | P0 | sprint-9-cleanup-source-refs-query-triggers.md |
| kdo-infrastructure-backlog-proposal | 黄药师 KDO 基础设施 backlog 提案 | approved | 黄药师 | P0-P2 | kdo-infrastructure-backlog-proposal.md |
| calibration-understanding-gate-motivation-peakend | 校准任务：用两张旧卡建立理解深度标尺 | completed | 黄药师 | P1 | calibration-understanding-gate-motivation-peakend.md |
| sprint-13-kdo-mechanism-iterations | Sprint 13：KDO 机制迭代——lint 基线、卡片清册、变更 diff、理解门禁辅助 | completed | 黄药师 | P1 | sprint-13-kdo-mechanism-iterations.md |
| task_20260701_kdo-index-lint-wikilink-format-alignment | KDO index/lint wikilink 格式对齐 | queued | 黄药师 | P1 | task_20260701_kdo-index-lint-wikilink-format-alignment.md | 欧阳锋建议、王语嫣入队：修复 `kdo index --rebuild` 与 `kdo lint` 的 wikilink 格式不一致，使 strategy 148 个 / 全库约 700+ WARNING 误报清零；阻塞 #28 strategy 域真实清零验证 |
| task_20260701_design-domain-encoding-diagnosis | design domain 编码损坏诊断 | queued | 老顽童(Kimi) | P1 | task_20260701_design-domain-encoding-diagnosis.md | 欧阳锋建议、王语嫣入队：只读诊断 design 域编码损坏根因，分类 healthy/display-only/recoverable/corrupted；诊断完成前禁止批量修改 design 文件；阻塞 #28 design 域清理 |
| task_20260701_wangyuyan-wobeirushen-pilot-orchestration | 《吾辈如神》条件性纳入 + 3 张卡 | reviewed | 老顽童(Kimi) | P1 | task_20260701_wangyuyan-wobeirushen-pilot-orchestration.md | 欧阳锋终审通过：3 张卡（认知卸载/AI 杠铃策略/富足悖论）kdo pre-submit PASS、0 新增 ERROR；纠偏 BMW 85%/AGI 2029/AI 无法创造；其余概念本次不纳入，封账 |
| task_20260701_wangyuyan-time-management-domain-orchestration | 时间管理域升级：3 张高密度桥接卡 | reviewed | 老顽童(Kimi) | P2 | task_20260701_wangyuyan-time-management-domain-orchestration.md | 欧阳锋终审通过：3 张卡（framework-yitang-five-step-to-time-management / tool-personal-time-audit-loop / dk-time-management-common-mistakes）kdo pre-submit PASS、0 新增 ERROR、related ≥5 且跨域、反向更新 9 张已有卡；按实际产出范围封账 |
| task_20260702_laowantong-vikki-daxin-dark-knowledge-pilot-production | 暗知识补挖试点生产：Vikki + 大馨战队 | queued | 老顽童(Kimi) | P1 | task_20260702_laowantong-vikki-daxin-dark-knowledge-pilot-production.md | 黄药师试点建议书：王语嫣用第6步「一句话金矿扫描」产出 22 条暗知识清单，建议 4 张新 dk + 7-9 张已有卡补充；欧阳锋抽检 ≥3 张验证有效性；有效则推广为 SOP |
| task_20260702_laowantong-live81-ai-trademark-design-production | Live81 AI 赋能商标设计：1 case + 2 tool + 1 dk | queued | 老顽童(Kimi) | P1 | task_20260702_laowantong-live81-ai-trademark-design-production.md | 王语嫣九层深挖诊断：Live81 是「一堂方法论+AI协作+调研+决策卫生」在 AI 交付物打磨场景的实例化；核心产出 1 case + 2 tool + 1 dk（case-live81 / tool-ai-deliverable-polish-loop / tool-scene-design-language-translation / dk-ai-design-pitfalls）；60 分起盘、模型选择、一页纸上下文、黑盒/白盒/池子审美判断等概念已有 KDO 卡覆盖，本次通过 related 关联而非新建；反向更新 20 张已有卡 related |
| task_20260702_laowantong-yitang-scientific-sales-methodology-production | 一堂科学销售方法论：1 framework + 5 tool + 1 framework + 3 case + 1 dk + 1 tool（OPC 智能体） | reviewed | - | P1 | task_20260702_laowantong-yitang-scientific-sales-methodology-production.md | 王语嫣九层深挖诊断：本专题是「一堂方法论+假设驱动+工具化」在销售管理场景的完整实例化；经用户挑战深度后扩展为 10 张，再按黄药师建议+王语嫣判断扩展为 12 张；新增 `case-yitang-sales-transformation-tuliaogongsi`（涂料公司/10 万->20 S 级）和 `tool-opc-sales-dialogue-assistant`（读对话->想策略->给话术的 MVP 智能体规格卡，可直接当 system prompt）；12 张目标卡均已生产并通过欧阳锋终审；反向更新 >=28 张已有卡 related；OPC 架构由 `opc-ai-sales-agent-architecture.md` 承接并补充 MVP 启动路径 |
| task_20260702_laowantong-opc-sales-agent-specs-production | OPC 销售智能体军团首批规格卡：从 #44 方法论卡片编译 4 张 agent-spec | reviewed | - | P1 | task_20260702_laowantong-opc-sales-agent-specs-production.md | 欧阳锋终审通过：4/4 agent-spec 卡 pre-submit PASS，lint 0 新增 ERROR，schema 扩展通过，方法论溯源/输入门/迭代日志齐全；可改进点：System Prompt 尚未在真实模型运行、仅覆盖医药零售 B2B 场景、opc-ai-sales-agent-architecture.md 正文映射可细化 |
| task_20260702_laowantong-opc-sales-agent-incremental-specs | OPC 销售智能体军团增量：开场/异议/自我驱动 3 张 agent-spec | reviewed | - | P2 | task_20260702_laowantong-opc-sales-agent-incremental-specs.md | 欧阳锋终审通过：3/3 agent-spec 卡 pre-submit PASS，lint 0 新增 ERROR，输入门/输出/触发条件/边界/方法论溯源/迭代日志/示例修正均齐全；opc-ai-sales-agent-architecture.md 正文新增 7 张 agent-spec 调用关系图；可改进点：System Prompt 尚未在真实模型运行、场景仍以医药零售 B2B 为主、self-motivation 可补充个人节律输入门 |
| task_20260702_laowantong-opc-sales-agent-testing-wave1 | OPC 销售智能体实测 Wave 1：7 张 agent-spec 真实模型验证 | reviewed | 老顽童(Kimi) | P1 | task_20260702_laowantong-opc-sales-agent-testing-wave1.md | 欧阳锋终审通过：deepseek-v4-pro 14 个首轮场景 + 2 个 v1.1 复测；P0 阻塞 0、P1 截断已修复并复测、P2 优化项已升级 System Prompt；Trace 归档 17 个文件；KDO 回流清单 9 项完成；新建 case-opc-agent-wave1-real-model-testing.md；自攻击报告 0 致命；同意封账；可改进点进入 Wave 2 / 停车场 |
| task_20260703_laowantong-yitang-Y-model-foundation-production | 一堂底层逻辑域：Y模型 + 实事求是 + 解放思想（1 重写 + 2 新建 framework + 1 tool + 1 dk + 2 case） | reviewed | 老顽童(Kimi) | P1 | task_20260703_laowantong-yitang-Y-model-foundation-production.md | 欧阳锋终审通过：7 张完整卡 + 3 张旧卡迁移；17 张已有卡反向补链；全库 lint 0 ERROR；yt-decision-y-model degree 100 / top 0.24% |
| task_20260703_huangyaoshi-yitang-Y-model-root-infrastructure | Y模型根节点化：GraphRAG rebuild + 索引维护 + pipeline 监控 | queued | 黄药师 | P1 | task_20260703_huangyaoshi-yitang-Y-model-root-infrastructure.md | 王语嫣裁定：本周不做 schema 改造、不新增 lint 规则、不创建文档；只做 #51 完成后的 kdo index --rebuild，验证 yt-decision-y-model 成为查询中心，并用 kdo pipeline 监控 Agent 反馈信号 |
| task_20260703_laowantong-case-backfill-wobeirushen-time-management | 案例卡补挖：吾辈如神 + 时间管理域缺失 companion case（4 张） | reviewed | 老顽童(Kimi) | P2 | task_20260703_laowantong-case-backfill-wobeirushen-time-management.md | 欧阳锋终审通过：新增 4 张 case 卡 + 反向更新 8 张锚定卡 related；pre-submit 12/12 PASS；lint 0 新增 ERROR |
| task_20260703_wangyuyan-retroactive-case-scan-pilot | 已消化素材案例卡补扫试点：科学决策 / 泛产品设计 / 战略 | reviewed | 老顽童(Kimi) | P2 | task_20260703_wangyuyan-retroactive-case-scan-pilot.md | 欧阳锋终审通过（pass with reservations）：3 个域候选清单结构完整，数量超额满足，lint/pre-submit PASS；建议修正统计不一致与评级跨域漂移，立即投产 7 条 A 级候选 |
| task_20260703_laowantong-yitang-Y-model-os | Y模型 OS：所有 Agent 的共享底层 prompt + 可选 Coach 模式 | reviewed | 老顽童(Kimi) | P1 | task_20260703_laowantong-agent-spec-yitang-Y-model-coach.md | 欧阳锋终审通过：system-yitang-Y-model-os.md / Coach agent-spec / agent-native-card-design.md 三层结构 / OPC 集成示例 / 2 个真实场景测试 / 自攻击 0 致命；status: reviewed |
| task_20260703_laowantong-yitang-Y-model-stub-completion | #51 收尾：实事求是 / 解放思想 framework 卡补全 | closed_cancelled | — | P1 | task_20260703_laowantong-yitang-Y-model-stub-completion.md | 取消：#51 已全部完成，无需单独收尾任务 |
| task_20260703_laowantong-graphrag-orphan-reduction | GraphRAG 健康度提升：跨域 related 补链降低 orphan 比例 | reviewed | 老顽童(Kimi) | P2 | task_20260703_laowantong-graphrag-orphan-reduction.md | 欧阳锋终审通过：orphan 18% (621/3468)、components 669、health 90/100，三项指标均达标；578 张卡 pre-submit 全部 PASS；日志 `60_feedback/diagnosis/diag_20260704_graphrag-orphan-linking-log.json` |
| task_20260703_huangyaoshi-agent-tcpr-role-layer | Agent 能力分层引入 TCPR 角色模型：所有 Agent 协作前必须选定 T/C/P/R 身份 | reviewed | 老顽童(Kimi) | P1 | `60_feedback/tasks/task_20260703_huangyaoshi-agent-tcpr-role-layer.md` | 欧阳锋终审通过：agent-os.md 升级为运行时 OS；agent-native-card-design.md 新增 TCPR 章节；7 张 OPC agent-spec 补全 TCPR 字段与 System Prompt 身份声明；Y模型 OS 第 0 步对齐；kdo_lint.py 新增 WARNING 级 TCPR 校验；13 个改动文件 pre-submit 全部 PASS |
| task_20260703_huangyaoshi-agent-prompt-compiler | Agent Prompt 编译器：把 agent-os.md + 域卡编译为可注入的 system prompt | reviewed | 黄药师 | P1 | `60_feedback/tasks/task_20260703_huangyaoshi-agent-prompt-compiler.md` | 欧阳锋终审通过：编译器代码通过，3 个试点编译产物 pre-submit PASS；产生 2 项微债务待 #62 跟进 |
| task_20260703_huangyaoshi-fix-queue-transition-review-lookup | 修复 queue_transition.py review 按 frontmatter id 查找任务单 | queued | 黄药师 | P2 | `60_feedback/tasks/task_20260703_huangyaoshi-fix-queue-transition-review-lookup.md` | 欧阳锋重审通过：7 条改进全部满足，7/7 tests passed，#55 场景验证正确，claim/complete/release 未破坏；待 #61 释放后 queue_transition.py 正式更新为 reviewed |
| task_20260704_laowantong-case-production-54-pilot-A-candidates | #54 试点 A 级候选投产：7 张 companion case 卡 | claimed-kimi | 老顽童(Kimi) | P2 | `60_feedback/tasks/task_20260704_laowantong-case-production-54-pilot-A-candidates.md` | 老顽童(Kimi) 已领取；产出 7 张 companion case 卡；正在执行 |
| task_20260704_huangyaoshi-agent-prompt-compiler-micro-debt | #59 微债务：Agent Prompt 设计规范补全与 source 字段标准化 | queued | 黄药师 | P2 | `60_feedback/tasks/task_20260704_huangyaoshi-agent-prompt-compiler-micro-debt.md` | 欧阳锋终审 #59 提出的 2 项微债务；补充 agent-native-card-design.md 三层编译章节与 os_sources/domain_sources/user_sources 字段规范；P2 |
| task_20260704_wangyuyan-dual-triangle-degradation-spiral | #76 双三角死亡飞轮：人机协作退化螺旋 dk 卡 | queued | 老顽童(Kimi) | P1 | `60_feedback/tasks/task_20260704_wangyuyan-dual-triangle-degradation-spiral.md` | 王语嫣独立判断：补全双三角失败模式缺口。两种退化螺旋（互相糊弄+判断力退化）口述稿 L1680-1688/L3942-3992，KDO 无卡覆盖；1 张 dk，P1 |
| task_20260704_wangyuyan-hITL-dual-triangle-supplement | #77 #66 追补：人在环历史定位 | queued | 老顽童(Kimi) | P2 | `60_feedback/tasks/task_20260704_wangyuyan-hITL-dual-triangle-supplement.md` | 口述稿 L4557"人在环也不是为了AI准备的"未纳入 #66 原始素材；单点追补，改一处不返工 |
| task_20260704_laowantong-truman-feishu-to-slide-case | #64 Truman 飞书 To slide PPT 迭代案例卡 | reviewed | 欧阳锋 | P0 | `60_feedback/tasks/task_20260704_laowantong-truman-feishu-to-slide-case.md` | 2026-07-04 终审通过：242 行，失败模式/Critique/外部攻击/Synthesis/Action Triggers 齐全 |
| task_20260704_laowantong-y-model-dual-triangle-bridge-framework | #65 Y模型×双三角协同工作法 framework | reviewed | 欧阳锋 | P0 | `60_feedback/tasks/task_20260704_laowantong-y-model-dual-triangle-bridge-framework.md` | 2026-07-04 终审通过：287 行，引擎层循环图完整，gold standard 级卡片 |
| task_20260704_laowantong-human-in-the-loop-dual-triangle-relation | #66 人在环×双三角 concept | reviewed | 欧阳锋 | P1 | `60_feedback/tasks/task_20260704_laowantong-human-in-the-loop-dual-triangle-relation.md` | 2026-07-04 终审通过：192 行，3 外部攻击者，5 失败模式，国际框架对齐 |
| task_20260704_laowantong-y-model-engine-layer-method | #67 Y模型引擎层操作法 method | reviewed | 欧阳锋 | P1 | `60_feedback/tasks/task_20260704_laowantong-y-model-engine-layer-method.md` | 2026-07-04 终审通过：275+ 行，10 步含预估时间，9 陷阱，Truman 元攻击 |
| task_20260704_laowantong-cross-domain-framework-iteration-audit | #68 跨域框架静态化审计 | reviewed | 欧阳锋 | P2 | `60_feedback/tasks/task_20260704_laowantong-cross-domain-framework-iteration-audit.md` | 2026-07-04 终审通过：10 张卡 6 维评分，发现两代分化，P0 修复任务单已产出 |
| task_20260704_laowantong-fix-staticization-yt-decision-y-model | #68-P0 yt-decision-y-model 引擎化升级 | reviewed | 欧阳锋 | P0 | `60_feedback/tasks/task_20260704_laowantong-fix-staticization-yt-decision-y-model.md` | 2026-07-04 终审通过：5 项改动，审计评分 4/12→9/12 |
| task_20260704_laowantong-yitang-underlying-logic-case-method-cards | #71 底层逻辑三课程补产 33 张卡 | reviewed | 欧阳锋 | P1 | `60_feedback/tasks/task_20260704_laowantong-yitang-underlying-logic-case-method-cards.md` | 2026-07-04 终审通过：case 强/dk+concept+principle 偏薄，P2 追补债务已记录 |
| task_20260704_wangyuyan-framework-staticization-repair | #79 框架卡静态化修复 4 张卡 | reviewed | 欧阳锋 | P2 | `60_feedback/tasks/task_20260704_wangyuyan-framework-staticization-repair.md` | 2026-07-04 终审通过：实事求是/解放思想/冰山/BRM 纯追加边界声明 |
| task_20260704_laowantong-ai-feature-thinking-concept | #74 AI 基本功 Feature 思维 concept + 2 tool 重写 | reviewed | 欧阳锋 | P1 | `60_feedback/tasks/task_20260704_laowantong-ai-feature-thinking-concept.md` | 2026-07-04 终审通过：3 案例 + FeatureSet 六层 + 9 类 Feature，🟡 related 不足 |
| task_20260704_laowantong-aesthetic-library-method-tool-cards | #72 审美工作法 + 审美库工具 + case 3 张卡 | reviewed | 欧阳锋 | P1 | `60_feedback/tasks/task_20260704_laowantong-aesthetic-library-method-tool-cards.md` | 2026-07-04 终审通过：审美三边界约束 + 5161→244 数字密度 + 五子命令可执行 |
| task_20260704_wangyuyan-patch-canvas-risk-judgment | #81 画布 Agent 风险判断输出 | reviewed | 欧阳锋 | P2 | `60_feedback/tasks/task_20260704_wangyuyan-patch-canvas-risk-judgment.md` | 2026-07-04 终审通过：[确认]/[假设]/[空白] 三级标注 + 风险摘要 + agent-spec 行为规则 |
| task_20260704_wangyuyan-dual-triangle-canvas-agent-cli | #69 双三角画布 Agent CLI 交付 | reviewed | 欧阳锋 | P1 | `60_feedback/tasks/task_20260704_wangyuyan-dual-triangle-canvas-agent-cli.md` | 2026-07-04 终审通过：canvas-agent.py + agent-spec v2 多轮迭代交付（TCPR/风险判断），KDO Agent 化首个试点 |
| task_20260704_wangyuyan-agent-card-skill-execution-pattern | #73 Agent 执行模式设计 Phase 1 | reviewed | 欧阳锋 | P1 | `60_feedback/tasks/task_20260704_wangyuyan-agent-card-skill-execution-pattern.md` | 2026-07-04 终审通过：design doc + framework 卡，三种执行模式+六步循环+工具边界声明；agent-solver.py Phase 2 依赖 #72/#59 |
| task_20260704_laowantong-dual-triangle-vlm-case-enrichment | #93 双三角 VLM 案例批量 enrichment 10 张 | reviewed | 欧阳锋 | P1 | `60_feedback/tasks/task_20260704_laowantong-dual-triangle-vlm-case-enrichment.md` | 2026-07-04 终审通过：抽检 3 张 PASS，六要素标注/Critique/Triggers 结构统一 |
| task_20260707_wangyuyan-project-management-domain-production | 管项目域卡片化：12 张卡 + 项目管理助手 agent-spec | queued | 老顽童 | P1 | `70_product/tasks/task_20260707_wangyuyan-project-management-domain-production.md` | 王语嫣九层深挖诊断已完成；新任务入队 #131 |

---

## Summary

> **当前任务状态见 `production-queue.md`（唯一真相源）。本 dashboard 保留历史任务全景，日常领任务不读这个文件。**

- **Production Queue**: #60-#131；#131 queued（2026-07-07）
- **Active Tasks**: #131 管项目域卡片化（等待老顽童领取）
- **黄药师**: P-10 跨域模式层完成；管道碎片化清理中
- **王语嫣**: 任务编排建议书已提交（OSCAR 卡补齐 / external-exploration-sop 补写）
- **老顽童**: 待命，production-queue 无 queued 任务
- **欧阳锋**: 月度抽检模式
- **洪七公/段王爷**: 待命

> **管道收拢（2026-07-07）**：以下旧文件已废弃——`laowantong-next-tasks.md`、`laowantong-batch-2026-06-20.md`、`laowantong-assignment-2026-06-20.md`、`hongqigong-next-tasks.md`、`duanwangye-next-tasks.md`、`wangyuyan-next-tasks.md`。Agent 启动后只读 `production-queue.md`。

---

## 角色停车场

> 各角色在主线任务中产生的不阻塞当前主线的洞察、改进点、待讨论方案。
> 机制说明：每月清理一次，P1/P2 超过 30 天未动强制 review，长期不做的标记 `已拒绝`。

| 角色 | 停车场文件 | 总数 | P0 | P1 | P2 | 最近更新 |
|:---|:---|---:|---:|---:|---:|:---|
| 黄药师 | `parking-lot-huangyaoshi.md` | 4 | 0 | 1 | 3 | 2026-06-28 |
| 欧阳锋 | `parking-lot-ouyangfeng.md` | 1 | 0 | 1 | 0 | 2026-06-28 | O-1 已确认，待升级实施 |
| 王语嫣 | — | 0 | 0 | 0 | 0 | — |
| 老顽童 | `task_20260628_hermes-lint-baseline-cleanup-batch1.md` | 1 | 0 | 1 | 0 | 2026-06-30 | lint 基线清理 Batch 1：欧阳锋终审通过；783/784 文件 frontmatter 可解析，1 个 `_archive` 历史残余待后续清理 |
| 王语嫣 | `task_20260628_wangyuyan-wave6-blindspot-diagnosis.md` | 1 | 0 | 1 | 0 | 2026-06-28 | Wave 6 新盲区诊断：基于周报和对话记录识别 1-2 个新盲区并拆任务入队 |
| 洪七公 | — | 0 | 0 | 0 | 0 | — |
| 段王爷 | — | 0 | 0 | 0 | 0 | — |

> 新停车场任务由各角色自行维护。王语嫣每月组织一次 5 分钟停车场 review，决定是否升级进入 `production-queue.md`。
