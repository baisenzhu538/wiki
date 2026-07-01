---
id: production-queue
type: queue
status: active
updated_at: 2026-06-30T15:23:37+00:00
reviewed_by: 欧阳锋
owner: 王语嫣
audience: 老顽童 / 欧阳锋 / 黄药师 / 用户
---

# 生产队列：老顽童领取 / 欧阳锋审核

> 本文件是 KDO 知识工厂的**统一生产队列**。
> 老顽童按队列顺序领取任务，一次只做一件；欧阳锋按队列顺序审核。
> 任务来源：历史批量工单、新域诊断任务、跨域桥接任务。

---

## 队列规则

1. **单实例单线程领取**：每个老顽童实例每次只能领取一个 `queued` 任务，把状态改为 `claimed-<实例标识>`（如 `claimed-hermes`、`claimed-kimi`）。`pending_review` 状态的条目为审阅项，由欧阳锋直接审核，老顽童不领取。
2. **多实例并行**：当队列中存在 ≥2 个无依赖的 `queued` 任务时，可启动多个老顽童实例并行领取。同一任务默认由单实例完成；如需多实例协作同一任务，由用户或王语嫣在任务单中明确拆分。
3. **完成后提交**：老顽童完成生产并把 `kdo pre-submit` 输出贴到任务文件后，将状态改为 `pending_review`。
4. **按序审核**：欧阳锋按队列顺序审核 `pending_review` 任务，通过后改为 `reviewed`；王语嫣跟踪任务状态，必要时改为 `done`。
5. **阻塞处理**：若任务被阻塞，在「状态」列标注 `blocked` 并写明阻塞原因；阻塞解决后恢复为 `queued`。
6. **优先级调整**：用户可随时调整队列顺序；调整时由王语嫣更新本文件，并在 `.agent/context.md` 中同步。
7. **新任务入队**：王语嫣诊断完成后，新任务默认进入队列末尾；用户可指定插队。
8. **🆕 所有状态变更必须通过 `queue_transition.py`**：
   - 老顽童领取：`python 90_control/scripts/queue_transition.py claim <task-id> --instance <实例标识>`
   - 老顽童完成提交：`python 90_control/scripts/queue_transition.py complete <task-id> --instance <实例标识>`
   - 老顽童释放：`python 90_control/scripts/queue_transition.py release <task-id> --instance <实例标识>`
   - 欧阳锋终审通过：`python 90_control/scripts/queue_transition.py review <task-id> --verdict pass --reviewer 欧阳锋`
   - 欧阳锋终审不通过：`python 90_control/scripts/queue_transition.py review <task-id> --verdict fail --reviewer 欧阳锋`
9. **🆕 禁止手动修改状态**：任何角色不得直接编辑本文件或任务单 frontmatter 中的 `status` / `reviewed_by` / `review_date`。所有状态变更由脚本自动完成，脚本内置 gate、锁、状态机校验，防止抢跑和状态不一致。

---

## 当前队列

| 队列序号 | 任务 ID | 任务名称 | 状态 | 领取人 | 预计卡数 | 阻塞/依赖 | 来源文件 | 备注 |
|:---:|:---|:---|:---:|:---:|---:|:---|:---|:---|
| 1 | `laowantong-batch-2026-06-20-wave1` | 老顽童批量工单第 1 波：门禁快速清理 | reviewed | 老顽童(WorkBuddy) | 18 | 无 | `review_20260628_ouyangfeng-wave1.md` | 欧阳锋终审通过：18/18 张卡 status 更新为 reviewed，reviewed_by: 欧阳锋，review_date: 2026-06-28 |
| 2 | `task_20260627_laowantong-deliberate-practice-cards` | 元能力-刻意练习域卡片化（含 AI 协作桥接卡） | reviewed | - | 11 | 无（可与 wave1 并行） | `60_feedback/tasks/task_20260627_laowantong-deliberate-practice-cards.md` | 欧阳锋终审通过，11 张卡 status 更新为 reviewed，frontmatter 已补 review_date |
| 3 | `task_20260627_laowantong-channel-growth-cards` | 渠道增长域卡片化（含 2 张跨域桥接卡） | reviewed | - | 25 | 无（可与 wave1 并行） | `review_20260628_ouyangfeng-channel-growth.md` | 欧阳锋终审通过：25/25 张卡 status 更新为 reviewed，reviewed_by: 欧阳锋，review_date: 2026-06-28；已知遗留：13 张 case 卡缺 lint 标准 section（全局 case section 债务）、1 张 dk 目录未对齐、1 张 concept 目录未对齐，已记录为后续清理任务 |
| 4 | `task_20260627_laowantong-lanyi-panproduct-organization` | 兰毅泛产品组织化 + 泛产品设计域升级 | reviewed | - | 12 | 无 | `task_20260627_laowantong-lanyi-panproduct-organization.md` | 欧阳锋终审通过：12/12 张卡 status 更新为 reviewed，reviewed_by: 欧阳锋，review_date: 2026-06-28；审查中修复 3 张 case section + 5 个目录移动 |
| 5 | `laowantong-batch-2026-06-20-wave2` | 老顽童批量工单第 2 波：P0 返工 | reviewed | 老顽童(WorkBuddy) | 16 | 无 | `laowantong-batch-2026-06-20.md` | 欧阳锋子代理终审通过：16/16 张卡 `kdo pre-submit` 通过，status 更新为 reviewed，`reviewed_by: 欧阳锋`，`review_date: 2026-06-28`；仍有 frontmatter domain/related/tags/query_triggers `src_unknown` 占位及少量内容区占位，已记录为 wave2 残留项，建议由王语嫣/老顽童在后续清理任务中补齐 |
| 6 | `laowantong-batch-2026-06-20-wave3` | 老顽童批量工单第 3 波：P1 深度补全 | reviewed | 欧阳锋 | 14 | 依赖 wave2 完成（已 reviewed，解锁） | `review_20260628_ouyangfeng-wave3.md` | 欧阳锋终审通过：14/14 张卡 status 更新为 reviewed；审查中清理 14 张卡 frontmatter 中 domain/related/tags 的 src_unknown 占位；全库 lint ERROR 降至 533；已解锁 wave4 和第八批 dk 清零 |
| 7 | `task_20260628_laowantong-dark-knowledges-batch8` | dark-knowledges 第八批清零：补齐 10 张问题 dk 卡 | reviewed | 欧阳锋 | 10 | 依赖 wave3 完成（已 reviewed，解锁） | `task_20260628_laowantong-dark-knowledges-batch8.md` | 欧阳锋终审通过：10/10 张 dk 卡 status 更新为 reviewed；`dark-knowledges/` 目录 lint ERROR 归零；审查中修复 4 张卡格式问题；wave4 已完全解锁 |
| 8 | `laowantong-batch-2026-06-20-wave4` | 老顽童批量工单第 4 波：新域建设 | reviewed | Hermes 老顽童 | 15 | 已解锁（wave3 + 第八批均 reviewed） | `review_20260628_ouyangfeng-wave4.md` | 欧阳锋终审通过：15/15 张卡 status 更新为 reviewed，reviewed_by: 欧阳锋，review_date: 2026-06-28；审查中修复 4.1 source_refs 18 处、4.2 domain 占位 7 处及正文 src_unknown 占位 30+ 处；wave4 已解锁 wave5 |
| 9 | `laowantong-batch-2026-06-20-wave5` | 老顽童批量工单第 5 波：外部探索三个新盲区 | reviewed | WorkBuddy 老顽童 | 12 | 依赖 wave4 完成（已 reviewed，解锁） | `review_20260628_ouyangfeng-wave5.md` | 欧阳锋终审通过：12/12 张卡 `kdo pre-submit` 通过；审查中修复 12 张卡 frontmatter（补 `status: reviewed`、统一 `reviewed_by: 欧阳锋`、更新 `updated_at`）；wave5 已解锁 |
| 10 | `task_20260628_hermes-lint-baseline-cleanup-batch1` | Hermes lint 基线清理 Batch 1：机械性 frontmatter 修复 | reviewed | Hermes 老顽童 | 784（安全机械修复，含复查追加 125） | 无 | `60_feedback/tasks/task_20260628_hermes-lint-baseline-cleanup-batch1.md` | Hermes 已完成：frontmatter parse 类 ERROR 清零；`kdo lint` 从 690→890 是因为 frontmatter 修好后原被压制的卡片暴露更多 section/source_refs 错误；890 个内容级错误由 Batch 2-A/B/C 承接；Hermes 老顽童待命 |
| 11 | `review_20260627_ouyangfeng-self-attack-framework` | 欧阳锋审核：自攻击方法论框架卡 | reviewed | 欧阳锋 | 1 | 无 | `30_wiki/frameworks/framework-kdo-self-attack.md` | review-only；pre-submit 已通过；欧阳锋审查结论：deep 通过 |
| 11 | `task_20260628_wangyuyan-cleanup-channel-growth-residuals` | 渠道增长域终审遗留问题清理（P2+P3 已完成，P1 已拆分） | done | 黄药师 | 0（清理任务） | 无 | `task_20260628_wangyuyan-cleanup-channel-growth-residuals.md` | 黄药师已完成 dk/concept 目录移动 + 全库 related 链接更新 + 顺手修复 3 张 case 卡；P1 剩余 10 张 case + 1 张 dk section 调整已拆分为独立任务 #12 |
| 12 | `task_20260628_laowantong-case-section-standardization` | 渠道增长域 10 张 case + 1 张 dk section 标准化 | reviewed | 欧阳锋 | 11 | 无 | `task_20260628_laowantong-case-section-standardization.md` | 欧阳锋终审通过：11/11 文件 `kdo lint` 0 ERROR；1 处标题序号问题已现场修复 |
| 13 | `task_20260628_laowantong-lint-batch2-case-sections` | lint Batch 2-A：case section 标准化补全（130 文件） | reviewed | WorkBuddy 老顽童 | 130 | 无 | `60_feedback/tasks/task_20260628_laowantong-lint-batch2-case-sections.md` | 欧阳锋复核通过：申诉成立，130/130 case 文件已真实修改并 commit，`kdo lint` Case section ERROR 清零；之前 `git diff HEAD` 检查失效根因是 vault backup 自动 commit |
| 14 | `task_20260628_laowantong-lint-batch2-dk-sections` | lint Batch 2-B：dk section 标准化补全（43+14 文件） | reviewed | WorkBuddy 老顽童 | 57 | 无 | `60_feedback/tasks/task_20260628_laowantong-lint-batch2-dk-sections.md` | 欧阳锋复核通过：申诉成立，57/57 dk 文件已真实修改并 commit，`kdo lint` DK section ERROR 清零；原 43 清单 + 14 个 extra 文件均处理 |
| 15 | `task_20260628_huangyaoshi-lint-batch2-source-refs` | lint Batch 2-C：source_refs 真实存在性清理（175 ERROR / 90 文件） | reviewed | WorkBuddy 老顽童 | 90 | 无 | `60_feedback/tasks/task_20260628_huangyaoshi-lint-batch2-source-refs.md` | 用户复核发现规则层补丁已上线但数据层清理未完成；任务转交老顽童；已真实修改 90 个文件，为 175 个 bare source_refs 添加 `10_raw/sources/` 前缀，`kdo lint` source_refs ERROR 清零，`kdo pre-submit` 90/90 通过；待欧阳锋终审 |
| 16 | `task_20260628_wangyuyan-wave6-blindspot-diagnosis` | Wave 6 新盲区探索诊断 | reviewed | 王语嫣 | 0 | 无 | `60_feedback/tasks/task_20260628_wangyuyan-wave6-blindspot-diagnosis.md` | 欧阳锋终审通过：决策科学域 14 reviewed + 需求分析域 10-20 reviewed，两个盲区识别合理；建议卡片 ID 无冲突；#21/#22 可入队生产 |
| 17 | `task_20260628_wangyuyan-next-phase-orchestration` | 下一阶段任务编排建议：Wave 6 + 补链并行 | confirmed | 王语嫣 | 0 | 无 | `60_feedback/tasks/task_20260628_wangyuyan-next-phase-orchestration.md` | 王语嫣已拍板：Wave 6 继续 #16，补链拆为 B1/B2/B3 作为 #18/#19/#20 入队；B1 自动写入+抽检，B2 必须人工审核，B3 半自动；related 分层标准不按 ≥8 一刀切 |
| 18 | `task_20260628_laowantong-link-repair-b1-frontmatter-related` | B1：frontmatter `related` 字段 src_unknown 占位清理 | reviewed | 老顽童(WorkBuddy) | 256 | 无 | `60_feedback/tasks/task_20260628_laowantong-link-repair-b1-frontmatter-related.md` | 欧阳锋终审通过：256 文件真实修改，related src_unknown 清零，1190 pending_unknown 补入符合分层标准；`kdo lint` 0 ERROR；抽检 4 张卡 OK |
| 19 | `task_20260628_laowantong-link-repair-b2-synthesis-section` | B2：Synthesis section 死链/占位清理 | reviewed | 老顽童(WorkBuddy) | 235 + 66 补充 | 无 | `60_feedback/tasks/task_20260628_laowantong-link-repair-b2-synthesis-section.md` | 欧阳锋终审通过：235 张初处理 + 66 张补充清理，66 文件 body src_unknown 全部清零；kdo lint 140 ERROR 全为历史遗留，无新增；frontmatter src_unknown 另开任务处理 |
| 20 | `task_20260628_laowantong-link-repair-b3-island-cards` | B3：孤岛卡片 `kdo link-suggest` 批量推荐 | reviewed | 老顽童(WorkBuddy) | 1042 | 无 | `60_feedback/tasks/task_20260628_laowantong-link-repair-b3-island-cards.md` | 欧阳锋终审通过：2014 YAML引号修复 + 163 bare id包裹 + 119句子删除 + 33张孤岛补真实wikilink + pending_unknown.md移到system/；孤岛卡片清零；lint 140 ERROR全为历史遗留无新增；pre-submit 抽检5/5 PASS；55张仍全pending为已知限制 |
| 21 | `task_20260628_laowantong-wave6-decision-science-systematization` | Wave 6-A：决策科学域系统化 | reviewed | 老顽童(Hermes) | 5 | 依赖 Wave 6 诊断 reviewed | `60_feedback/tasks/task_20260628_laowantong-wave6-decision-science-systematization.md` | 欧阳锋终审通过：5/5 卡片结构完整，lint 148 ERROR 全为历史遗留无新增；删除 framework-decision-quality-checklist 中重复 related；决策科学域 reviewed 从 14→18 |
| 22 | `task_20260628_laowantong-wave6-demand-analysis-deepening` | Wave 6-B：需求分析域深化 | reviewed | 老顽童(Hermes) | 5 | 依赖 Wave 6 诊断 reviewed | `60_feedback/tasks/task_20260628_laowantong-wave6-demand-analysis-deepening.md` | 欧阳锋终审通过：5/5 卡片结构完整，case section 英文标题改为中文；lint 140 ERROR 全为历史遗留无新增，且修复 8 个历史 case section 错误；5 张卡全部加入 index.md；pre-submit 5/5 PASS |
| 23 | `task_20260629_huangyaoshi-lint-a1-empty-source-refs` | A1：空 source_refs 清理 | reviewed | 黄药师 | 8 | 无 | `60_feedback/tasks/task_20260629_huangyaoshi-lint-a1-empty-source-refs.md` | 欧阳锋终审通过：8/8 文件 source_refs 补为 pending_archive；`kdo lint` empty source_refs ERROR 清零；pre-submit 8/8 PASS |
:
| 24 | `task_20260629_laowantong-lint-a2-case-section-completion` | A2：case section 缺失补全 | done | 老顽童(Hermes) | 83 | 依赖 A1 无冲突 | `60_feedback/tasks/task_20260629_laowantong-lint-a2-case-section-completion.md` | frontmatter 修复目标已完成（日期字段/parse error/title/type）；欧阳锋终审通过；132 个 `Case card missing section` 历史遗留已拆分为独立债务任务 #24-debt |
| 24-debt | `task_20260629_historical-debt-case-section-132` | 历史债务：132 个 Case card missing section 修复 | reviewed | 老顽童(Hermes) | 43 | 无 | `60_feedback/tasks/task_20260629_historical-debt-case-section-132.md` | 欧阳锋终审通过：43 文件 132 section 已补全；8 个战略 case 补全 reviewed_by/review_date；`kdo lint` 无 Case card missing section；pre-submit 本次产出无 ERROR |
| 25 | `task_20260629_laowantong-expand-ai-learning-concept-cards` | 扩展 AI 工具学习方法论原子概念卡 | reviewed | 老顽童(Hermes) | 7 | 无 | `60_feedback/tasks/task_20260629_laowantong-expand-ai-learning-concept-cards.md` | 欧阳锋终审通过：7 张新卡结构完整；修复 3 张 tool 卡标准 section；补全 4 张核心卡 related 双向链接；index.md 已收录；lint 0 新增 ERROR；pre-submit 本次产出无 ERROR（全量 FAIL 为历史遗留） |
| 26 | `task_20260629_kimi-full-frontmatter-compliance-cleanup` | 全库 frontmatter 合规修复（循环处理直到归零） | reviewed | 老顽童(Hermes) | ~88 文件 + 22 目录 | 无 | `60_feedback/tasks/task_20260629_kimi-full-frontmatter-compliance-cleanup.md` | 欧阳锋终审通过：frontmatter 类、目录结构类 ERROR 全部清零；`kdo pre-submit` 448/0 PASS；`kdo lint` 0 ERROR / 7507 WARNING；剩余 WARNING 为内容质量类，需单独任务处理 |
| 27 | `task_20260629_kimi-lint-mechanical-noise-reduction` | lint 机械类 WARNING 直接降噪 | reviewed | 老顽童(Hermes) | ~2700 WARNING | 无 | `60_feedback/tasks/task_20260629_kimi-lint-mechanical-noise-reduction.md` | 欧阳锋终审通过：lint 阈值调整已确认；435 文件 source_refs 规范化；1637 页面补录 index；751 个 tool 卡补 section 骨架；`kdo lint` 从 7507 降到 3286 WARNING；`kdo lint` 0 ERROR；`kdo pre-submit` PASS |
| 29 | `task_20260629_wangyuyan-goat-milk-channel-partnership-bridge` | 羊奶「卖地图」跨域桥接卡生产 | reviewed | 老顽童(Hermes分身-Claude) | 3 张卡 | 无 | `60_feedback/tasks/task_20260629_wangyuyan-goat-milk-channel-partnership-bridge.md` | 欧阳锋终审通过：3 张卡已补录 index、修正 section 标题、补充 Critique 外部反对者与关键术语、补相邻域 related 回链；3 张目标卡 lint 无 ERROR/WARNING；pre-submit 目标卡无 ERROR（全量 FAIL 为 raw/ocr 与 _dogfood 历史遗留） |
| 30 | `task_20260629_vikki-info-emotion-skill-upgrade` | Vikki + 大馨：content-production-polish skill 2.0 升级 | reviewed | 老顽童(Kimi) | 1 个 skill | 无 | `60_feedback/tasks/task_20260629_vikki-info-emotion-skill-upgrade.md` | 欧阳锋终审通过：SKILL.md Core Standard 扩展为 6 条 + Step 5.5 6 项验证 + Platform Notes 5 平台模板 + Mini Scoring Rubric 6 维；human-speech-rules.md 新增 #13-#15 方法（5-part 结构 + 5 跨域示例）；`kdo pre-submit` 2/2 PASS；shared 与 `.claude/skills/` 桥接一致；审查中修正 2 处文本不一致（4→6 标准、Mini Scoring Rubric 6 维）；`agent复盘/Kimi/2026-06-30.md` 缺失记为后续微债务 |
| 31 | `task_20260629_vikki-five-tag-quality-labels` | Vikki 五标签 + 大馨品牌三度 → KDO 卡片质量标签体系 | reviewed | 老顽童(Kimi) | 1 个 schema + 50 张试点卡片 + 1 张 framework | 原 assignee 黄药师；schema/脚本层已由黄药师完成（label-quality-migrate.py）；老顽童(Kimi)完成内容层 | `60_feedback/tasks/task_20260629_vikki-five-tag-quality-labels.md` | 欧阳锋终审通过：framework-brand-three-degree 概念卡 + system-kdo-quality-labels 指南通过 pre-submit；50 张试点卡片标签迁移完成；审查中发现并修复 48 张卡片存在重复 `quality_labels` 字段的问题；迁移脚本已增加防御性跳过逻辑；`kdo pre-submit` 新卡 2/2 PASS + 抽查 4/4 PASS；`.agent/laowantong-context.md` 已更新 quality_labels 检查项 |
| 32 | `task_20260629_vikki-open-source-knowledge-boundary` | 沉淀「开源知识使用边界」概念卡 | reviewed | 老顽童(Kimi) | 1 张 concept 卡 | 无 | `60_feedback/tasks/task_20260629_vikki-open-source-knowledge-boundary.md` | 欧阳锋终审通过：concept-open-source-knowledge-usage-boundary 概念卡正文 300 行，四层级（学习/引用/改编/蒸馏）+ 三条边界线 + KDO 默认协议建议（CC BY-NC-SA/CC BY-NC-ND/CC BY）+ 游侠事件/Anthropic-DeepSeek 双案例 + Critique 内部局限 + 2 个外部攻击者；`kdo pre-submit` 1/1 PASS；5 个 related 链接全部有效；WebSearch 来源建议后续补入 source_refs |
| 33 | `task_20260630_daxin-methodology-cards-production` | 大馨战队核心方法论卡片化 | reviewed | 老顽童(Kimi) | 5 张卡（#30 skill 已覆盖脚本模板，省略 tool-shortvideo-script-templates） | 无 | `60_feedback/tasks/task_20260630_daxin-methodology-cards-production.md` | 欧阳锋终审通过：5 张目标卡全部 `kdo pre-submit` PASS；framework-brand-three-degree 从 concept 升级为 framework 并补全 6 步操作法；case-daxin-team-content-training-camp 证据链（615 条群聊）+ 6 个失败模式完整；审查中修正 1 处 `quality_labels: observed` 为受控标签 `cited`；队列抢跑异常已按补审流程处理 |
| 34 | `task_20260630_community-knowledge-failure-modes` | 社群知识生产失败模式库（Vikki + 大馨融合） | reviewed | 老顽童(Hermes) | 1 张 framework + 1 张可选 case | 无 | `60_feedback/tasks/task_20260630_community-knowledge-failure-modes.md` | 来源：Vikki群 + 大馨战队；融合10个失败模式，建立KDO多Agent协作/社群运营的失败模式库与早期预警指标 |
| 35 | `task_20260630_kdo-state-json-sqlite-migration-mvp` | KDO state.json → SQLite MVP 迁移（sources 集合） | reviewed | **黄药师** | 1 个集合 / 689 条记录 | 无；用户指定本周高优先级基础设施任务 | `60_feedback/tasks/task_20260630_kdo-state-json-sqlite-migration-mvp.md` | 欧阳锋终审通过（B+）：`.kdo/state.sqlite` 生成，`state.json` 已重命名为 `.migrated`，689 条 sources 一致；`kdo lint --summary` 0 新增 ERROR，`kdo status` 正常；新增 11 个 SQLite state 单元测试；审查中修复 append 不提交、reload 丢失 sources、跨线程 finalizer、多命令未关闭连接、lint 基线未复制 SQLite 等 5 处问题；`kdo enrich --all --dry-run` 当前无 TODO 页面待补测；全量 pytest 538 passed / 1 skipped / 1 failed（failed 为预存在 Windows GBK 编码问题） |
| 36 | `task_20260630_kdo-query-label-filter` | 实现 kdo query --label 质量标签过滤命令 | reviewed | 黄药师 | 1 个 CLI 参数 | 依赖 #31 reviewed；48 张重复标签问题已由欧阳锋现场修复 | `60_feedback/tasks/task_20260630_kdo-query-label-filter.md` | #31 遗留：验收标准要求 `kdo query --label actionable` 可过滤；当前用 rg 临时替代；黄药师实现后更新 system-kdo-quality-labels 指南 |
| 37 | `task_20260630_kdo-cli-syntaxerror-fix` | 修复 kdo CLI SyntaxError（kdo/commands/delivery.py:686） | reviewed | 黄药师 | 1 个 bugfix | 无；老顽童在 #34 生产中发现 | `60_feedback/tasks/task_20260630_kdo-cli-syntaxerror-fix.md` | `python -m kdo pre-submit` 等命令触发 SyntaxError，需黄药师修复 delivery.py 语法错误；修复后老顽童可恢复直接使用 CLI |
| 38 | `task_20260701_kdo-index-lint-wikilink-format-alignment` | KDO index/lint wikilink 格式对齐 | reviewed | 黄药师 | 1 个 KDO 代码修复 + 1 个测试 | 无；阻塞 #28 strategy 域真实清零 | `60_feedback/tasks/task_20260701_kdo-index-lint-wikilink-format-alignment.md` | 欧阳锋建议插队；根因：`kdo index --rebuild` 生成 bare wikilink，`kdo lint` 期望带路径 wikilink，导致 strategy 148 个 / 全库约 700+ WARNING 误报；修复后 strategy 域可真实清零；预计 0.5-1 天 |
| 39 | `task_20260701_design-domain-encoding-diagnosis` | design domain 编码损坏诊断 | reviewed | 老顽童(Kimi) | 1 份诊断报告 | 无；阻塞 #28 design 域清理 | `60_feedback/tasks/task_20260701_design-domain-encoding-diagnosis.md` | 欧阳锋建议插队；目标：只读诊断 design 域文件编码损坏根因，给出 healthy/display-only/recoverable/corrupted 分类及后续处理建议；诊断完成前禁止批量修改 design 文件；预计 0.5-1 天 |
| 40 | `task_20260701_wangyuyan-wobeirushen-pilot-orchestration` | 《吾辈如神》条件性纳入 + 3 张卡 | reviewed | 老顽童(Kimi) | 3 张卡（1 concept + 1 tool + 1 concept） | 无；验证报告已完成 | `60_feedback/tasks/task_20260701_wangyuyan-wobeirushen-pilot-orchestration.md` | 王语嫣价值判断：B 级素材，不做试点，直接产出 3 张卡——`concept-cognitive-offloading-in-ai-era`（已有初稿，需终审）、`tool-ai-use-barbell-strategy`（新建）、`concept-abundance-paradox`（新建）；纠正 BMW 85%/AGI 2029/AI 无法创造等误读；其余概念本次不纳入，封账 |
| 42 | `task_20260702_laowantong-vikki-daxin-dark-knowledge-pilot-production` | 暗知识补挖试点生产：Vikki + 大馨战队 | reviewed | 老顽童(Kimi) | 4 张新 dk + 7-9 张已有卡补充 | 依赖王语嫣诊断 `diag_20260702_vikki-daxin-dark-knowledge-extraction.md` | `60_feedback/tasks/task_20260702_laowantong-vikki-daxin-dark-knowledge-pilot-production.md` | 黄药师试点建议书：验证「一句话金矿扫描」流程；王语嫣已扫描 22 条暗知识，建议 4 张新 dk（肌肉记忆/创始人 IP 信任>流量/隐性价值传递/讲师 vs 群众社群），其余 18 条补充到已有卡；欧阳锋抽检 ≥3 张 |
| 43 | `task_20260702_laowantong-live81-ai-trademark-design-production` | Live81 AI 赋能商标设计：1 case + 2 tool + 1 dk | claimed-kimi | 老顽童(Kimi) | 4 张（1 case + 2 tool + 1 dk） | 无；王语嫣九层深挖诊断已完成 | `60_feedback/tasks/task_20260702_laowantong-live81-ai-trademark-design-production.md` | 王语嫣判断：Live81 是「一堂方法论+AI协作+调研+决策卫生」在 AI 交付物打磨场景的实例化；核心产出 `case-live81-ai-trademark-design` + `tool-ai-deliverable-polish-loop` + `tool-scene-design-language-translation` + `dk-ai-design-pitfalls`；60 分起盘、模型选择、一页纸上下文、黑盒/白盒/池子审美判断等概念已有 KDO 卡覆盖，本次通过 related 关联而非新建；反向更新 20 张已有卡 related |
| 44 | `task_20260702_laowantong-yitang-scientific-sales-methodology-production` | 一堂科学销售方法论：1 framework + 5 tool + 1 framework + 2 case + 1 dk | queued | - | 10 张 | 无；王语嫣九层深挖诊断已完成；#44 已按用户挑战从 6 张扩展为 10 张 | `60_feedback/tasks/task_20260702_laowantong-yitang-scientific-sales-methodology-production.md` | 王语嫣独立判断：6 张会牺牲「未来用户带着具体问题咨询可直接给可执行方案」的深度；扩展为 1 framework（五步法总览） + 5 tool（用户分层/卖点提炼/过程拆解/业绩管理/工具箱） + 1 framework（六维激励） + 2 case（剧本杀 SaaS / 美容院转型） + 1 dk（销售反模式）；用户分层与卖点提炼独立成卡，case 与反模式独立成卡，保证工具卡可独立调用、案例卡可对标；用户分层/价值主张/目标管理/工具化等概念已有 KDO 卡覆盖，本次只做销售域实例化；反向更新 ≥26 张已有卡 related；OPC 智能体军团由 `opc-ai-sales-agent-architecture.md` 承接 |
| 45 | `task_20260702_huangyaoshi-kdo-inbox-grade` | kdo inbox --grade 自动分级命令 | reviewed | 黄药师 | 1 个 CLI 命令 | 无；Sprint 6 lake transparency 基建 | `60_feedback/tasks/task_20260702_huangyaoshi-kdo-inbox-grade.md` | 欧阳锋审查通过：新增 `kdo inbox --grade`，按 S/A/B/C 自动给 00_inbox/ 素材打分；10104 文件分级 S 2832 / A 40 / B 6559 / C 673；pytest 548 passed；建议下一步加 `--grade --ready` 过滤和 C 级清理任务；缺 inbox grade 单元测试，记为微债务 |
| 41 | `task_20260701_wangyuyan-time-management-domain-orchestration` | 时间管理域升级：3 张高密度桥接卡 | reviewed | 老顽童(Kimi) | 3 张（1 framework 桥接 + 1 tool 审计循环 + 1 dk 反模式） | 无；洪七公 OCR+VLM 预处理已完成 | `70_product/tasks/task_20260701_wangyuyan-time-management-domain-orchestration.md` | 王语嫣经九层深挖返工：时间管理 = 一堂五步法/IPO/单元模型/决策卫生在自管理场景的实例化；3 张高密度卡 + 反向更新 ≥10 张已有框架卡 related；详见 `diag_20260701_time-management-nine-layer-isomorphism.md` |

> **当前总待生产卡数**：约 98-99 张（含历史批量工单 62 张 + 新任务 36-41 张）+ lint Batch 2 约 280 文件修复 + 补链 350-700 文件 + Wave 6 新域 10 张卡 + 7 张 AI 学习方法论扩展卡 + 3 张羊奶渠道桥接卡（已 reviewed）+ 5 个 Vikki/大馨 提炼任务（#30-34）+ **2 个已 reviewed 黄药师基础设施任务（#36 kdo query --label、#37 kdo CLI SyntaxError 修复）** + **2 个新入队 P1 基建任务（#38 index/lint wikilink 对齐、#39 design 编码诊断）** + **2 个王语嫣编排内容任务（#40《吾辈如神》试点卡、#41 时间管理域升级）** + **1 个长线周期性任务（#28 lint 内容债）**；#35 `state.json → SQLite MVP` 已由欧阳锋终审通过。
> **本周高优先级基础设施任务**：#38 `kdo index/lint wikilink 格式对齐` 与 #39 `design domain 编码损坏诊断` 由王语嫣独立判断后入队；#36/#37 已由欧阳锋终审通过。
> **#28 状态更新**：已由欧阳锋审查并暂停为**长线周期性任务**，任务单 status 改为 `paused`，队列移入「三、长线周期性任务」区域、不直接领取，待王语嫣拆批后以新 ID 入队。当前 strategy 域真实内容问题已清零，剩余 148 个 WARNING 为 #38 机制误报；yitang 已处理 20 个 tool 卡（WARNING ↓65）；design 域编码损坏待 #39 诊断。
> **#38 / #39 说明**：欧阳锋建议、王语嫣独立判断后入队。两个基建任务可与 #28 周期性批次及 #40 内容任务并行，互不等对方完成。#38 修复后 #28 strategy 域可真实清零；#39 诊断完成前禁止批量修改 design 文件。
> **#40 说明**：《吾辈如神》素材经 6 层交叉验证 + 9 层深挖 + 全网调研后评级为 **B（条件性纳入）**，不是 A 级，不能免检，不能批量生产 5-6 张卡。王语嫣做出明确价值判断：**值得产出 3 张卡**，分别为 `concept-cognitive-offloading-in-ai-era`（已有初稿，需终审）、`tool-ai-use-barbell-strategy`（新建）、`concept-abundance-paradox`（新建）。必须纠偏 BMW 85%、AGI 2029、AI 无法创造等误读；3 张卡之间需互相建立 wikilink；其余概念本次不纳入，封账。
> **#44 说明**：一堂科学销售方法论素材经九层深挖诊断，王语嫣判断为 A 级；经用户挑战「深度是否够未来直接咨询可用」后，王语嫣独立判断将核心产出从 6 张扩展为 10 张：1 framework（五步法总览） + 5 tool（用户分层 / 卖点提炼 / 过程拆解 / 业绩管理 / 工具箱） + 1 framework（六维激励） + 2 case（剧本杀 SaaS / 美容院转型） + 1 dk（销售反模式）；用户分层与卖点提炼独立成卡，case 与反模式独立成卡，保证工具卡可独立调用、案例卡可对标；剧本杀 SaaS / 美容院 / 快钱支付等案例不再仅作嵌入式证据；反向更新 ≥26 张已有卡 related；OPC 智能体军团由 `opc-ai-sales-agent-architecture.md` 承接。
> **当前 lint 基线**：`kdo lint` 全量 0 ERROR / 2656 WARNING；机械类 WARNING 经 #27 处理后降至 3286；#28 第一轮后降至 3255，第二轮累计处理 23 张 card 后降至 2666（copy-paste 从 76 清零），第三轮处理 5 个 strategy case 后降至 2656；剩余主要为 body 过短、L2 Critique、L2 Condense、L2 Synthesis 等内容债，由 #28 按 domain 分批处理；`kdo lint --domain <domain> --summary` 已可用。
> **人员状态**：A1/A2 reviewed；#24-debt reviewed；Wave 6 已完成；B1/B2/B3 已完成；#25 扩展卡已 reviewed；#26 全库 frontmatter 合规修复已 reviewed。
> **执行顺序建议**：frontmatter 与目录结构类历史债务已全部处理完毕，进入下一阶段。剩余 7507 WARNING 建议作为内容精修任务按需分批处理，不要继续机械修复。#38 成为下一个可直接领取的任务；#39/#40 与 #28 拆批后的子任务可并行推进；#41 时间管理域升级可与 #40 内容任务并行。
> 历史批量工单卡数估算来自 `laowantong-batch-2026-06-20.md` 的 waves 1-5。
>
> **🆘 临时分流（2026-06-27）**：Hermes 老顽童历史任务重，启动 Kimi 老顽童临时协助生产 2026-06-27 新标注任务。历史批量工单 waves 1-5 仍由 Hermes 负责；刻意练习域、渠道增长域、兰毅泛产品组织内容及跨域桥接卡由 Kimi 负责。欧阳锋/黄药师无感知——他们只按 pending_review 顺序审卡。
>
> **2026-06-29 更新**：A1 已完成 reviewed；A2 基线判断错误，132 case section 缺失需另开任务；#25 AI 学习方法论扩展卡已入队。

---

## 状态流转图

```
queued
  ↓ 老顽童领取
claimed
  ↓ 老顽童生产完成 + pre-submit 通过
pending_review
  ↓ 欧阳锋审核
reviewed
  ↓ 王语嫣最终验收（如需）
done
```

**中间状态**：
- `blocked`：任务被阻塞，需用户/其他角色先解决
- `paused`：任务暂停，等待用户决策或外部输入

---

## 各角色启动时必读

- **老顽童**：启动后先读 `.agent/startup.md` → `.agent/kb-evolution-direction.md` → `70_product/tasks/production-queue.md`，领取队列最前面的 `queued` 任务。
- **欧阳锋**：启动后先读 `.agent/startup.md` → `.agent/kb-evolution-direction.md` → `70_product/tasks/production-queue.md`，按顺序审核 `pending_review` 任务。
- **黄药师**：关注队列中任务的 KDO 基建依赖（如 lint/index），按需支持。
- **用户**：可随时查看本队列，回复「调整顺序」「插队」「暂停某任务」。

---

## 三、长线周期性任务（不直接领取，待拆批）

| ID | 任务单 ID | 任务名称 | 状态 | Assignee | 规模 | 依赖 | 任务单路径 | 备注 |
|---:|---|---|---|---:|---|---:|---|---|
| 28 | `task_20260629_kimi-lint-content-debt-by-domain` | lint 内容债按 domain 分批清理 | queued | 老顽童(Kimi) | ~2656 WARNING / 14 个子任务 | 依赖 #27 reviewed | `60_feedback/tasks/task_20260629_kimi-lint-content-debt-by-domain.md` | 已暂停，作为长线周期性任务待王语嫣统一拆批；strategy 域已真实清零（#38 修复后 WARNING 148→0），yitang 已处理 20 个 tool 卡（WARNING ↓65），design 域编码损坏已排除（#39 reviewed，196/196 healthy）；#38 index/lint 修复后全库 WARNING 4329→2570。本任务不直接领取，拆批后的子任务以新 ID 入队。 |

---

## 变更日志

| 日期 | 变更 | 变更人 |
|:---|:---|:---|
| 2026-06-27 | 创建统一生产队列，整合历史批量工单与新域任务 | 王语嫣 |
| 2026-06-29 | #23 A1 reviewed；#24 A2 done；#24-debt 132 case section 缺失已修复并 pending_review；#25 AI 学习方法论扩展卡入队 | 欧阳锋/王语嫣 |
| 2026-06-29 | 用户决策：#28 lint 内容债任务过长，改为 background batch 逐步清理，当前 Kimi 实例切换至 #30；#30 Vikki + 大馨 skill 2.0 升级任务已领取执行；#28 checkpoint 写入任务单 | 王语嫣 |
| 2026-06-29 | 欧阳锋独立评审完成：state.json → SQLite 迁移方案 A- 采纳，从 MVP 开始；#35 高优先级基础设施任务入队，黄药师负责本周执行 | 欧阳锋/王语嫣 |
| 2026-06-30 | #31 Vikki 五标签质量体系终审通过；欧阳锋发现并修复 48 张卡片重复 `quality_labels` 字段问题；#36 `kdo query --label` 实现任务入队，黄药师负责 | 欧阳锋/王语嫣 |
| 2026-06-30 | #35 `state.json → SQLite MVP` 由黄药师完成，欧阳锋终审通过；审查中修复 append 提交、reload 注册、跨线程 finalizer、连接关闭、lint 基线复制等 5 类问题；新增 11 个 SQLite state 单元测试 | 欧阳锋/黄药师 |

---

*维护人：王语嫣 | 最后更新：2026-06-30（#35 reviewed）*
