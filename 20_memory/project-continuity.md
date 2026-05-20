# Project Continuity

## 2026-05-20：视频试点 Gate 0+1+2 通过 + C-11 流程违规 + 黄药师 Task 16

- **🛑 Gate 0 v1 驳回**：老顽童初版脚本格式门禁全过但内容停在"清单式讲香"，十指模型缺失，用户驳回
- **🛑 Gate 0 v2 通过 · A+**：老顽童按十指讲香重写，十指 10/10 全命中。2219 字，烹饪比喻贯穿（生肉→粥→菜），墓碑意象，4 层情绪弧线
- **Gate 1 v1 废止**：洪七公旧分镜基于旧脚本，新版脚本新增内容无对应。要求 7a v2 修订分镜
- **🛑 Gate 1 v2 通过 · A+**：洪七公分镜 v2（40 帧，6/6 门禁全过，烹饪比喻 3 帧+墓碑独立设计+Emotional Arc Guide），7b 可立即开工
- **🛑 Gate 2 通过**：用户初步看过 7b+7c+7d 三段 31 帧画面，先跑通再迭代
- **🔥 C-11 流程违规（05-20）**：洪七公在 17:54→18:07→18:39 窗口内连续产出 Seg1（10帧）+Seg2（7帧）+Seg3（14帧），三次提报全部跳过。根因：将"快速提报"理解为"可以不报"。已写入 [[20_memory/corrections#C-11]] + F-KDO-017 禁止清单 + [[20_memory/beikai-role-positioning.md]] 审批纪律章节。后续 7e→7f 遵守停等信号，纪律生效
- **7e ✅ 7f ✅**：洪七公 Seg 4（3帧）+ Seg 5（6帧）完成。7d→7e 间隔 49min，7e→7f 间隔 8min，遵守停等
- **kdo video render 缺陷发现**：散文体格式不匹配（工具期待 `- bullet`）+ TTS 未集成。写入 Task 16 给黄药师
- **黄药师 Task 16 已下发**：修 render 两个缺口，~1h P0。4 门禁 + 6 验收标准。阻塞洪七公 7h
- **洪七公任务书重写**：Dashboard 洪七公 section 全量更新，每个子任务（7a-7g）均有独立 🛑门禁/🛑审批/🛑节点
- **老顽童回归主线**：脚本任务关闭，回归 v1.5 全库修复（20 FAILED）
- **🛑 Gate 3 ✅ 通过**：用户终检 40 帧，效果一般，先跑通流程
- **黄药师 Task 16 ✅**：`fa66855`，render 修复完成。阻塞解除
- **洪七公 7h ✅**：draft.mp4 生成（11810 KB, 500.1s, H.264/AAC, 1920×1080）
- **🛑 Gate 4 ⚠️ 条件通过 · B+**：7g 音画对位基本合格。3 项待修（拆出 timing.md + 补逐段时长表 + Seg 5 bug 记录），15min
- **段王爷激活**：首个任务下发——视频试点 ship。待洪七公 timing.md 修正 + Gate 4 正式放行后执行 `kdo video ship`
- **活跃任务**：洪七公补 timing.md → 欧阳锋复审 → 段王爷 kdo video ship

## 2026-05-15：工业化手册 v1.5 + Sprint 11/12 任务下发

- **KDO 方法论升级 v1.5**：黄药师提交 AI 思维卡分析建议书（[[ai-thinking-card-vs-kdo-analysis]]），欧阳锋独立裁决——采纳三个卡片层行为转化要件（Critique 外部攻击 + Synthesis 不要用场景 + Action Triggers），否决 ICAP 和 FOLLOWUP（原因：ICAP 是读者属性非卡片属性，FOLLOWUP 已被 v1.4 project-continuity 机制覆盖）
- **v1.5 变更**：工业化手册新增 §1.7（卡片层三要件）、KF-024 铁律、L2 门禁规则更新。适用方法/工具/框架卡，概念卡和索引卡豁免
- **Sprint 11 更新**：[[sprint-11-cognitive-upgrade-framework]] 质量门禁追加 v1.5 三要件——2 张新卡将成为第一批 v1.5 实例
- **Sprint 12 创建**：[[sprint-12-backfill-card-behavioral-requirements]]——~140 张 yt-* 卡分三批回溯升级（25 framework → 85 tool → ~30 concept）
- **活跃任务**：[[sprint-11-cognitive-upgrade-framework]]（P0）→ [[sprint-12-backfill-card-behavioral-requirements]]（P0，待 Sprint 11 完成后启动）

## 2026-05-15：工业化手册 v1.4 + Sprint 11 启动（已被 v1.5 取代）

- **KDO 方法论升级 v1.4**：对标 AI 思维卡「认知升级系统 v3.2」，引入行为转化层（ACTION→CTA→FOLLOWUP）、EVIDENCE 审计标准（偏差标注+外部攻击+反事实）、Burn line。新增 KF-023 和 F-KDO-016
- **审而不改**：控制文件和规则由欧阳锋直接改。知识卡和素材处理走 KDO 管线，黄药师执行
- **[[sprint-11-cognitive-upgrade-framework]]** 已创建——AI思维卡 HTML ingest + 十步框架萃取 + PEAS 工具卡
- **活跃任务**：[[sprint-11-cognitive-upgrade-framework]]（P0，黄药师待领取）
- **注**：v1.4 的产出层行为转化标准和 EVIDENCE 审计标准在 v1.5 中保留，卡片层三要件为增量
- **[[sprint-9-cleanup-source-refs-query-triggers]]** → completed ✅。52 张 source_refs 归零，31 张 triggers 重写，20 张 Constraints 去模板化
- **[[sprint-10-fill-remaining-related-edges]]** → completed ✅。76 张非 panproduct 卡图边全填充，16 张管理域 query_triggers 新增，管理域 Constraints 保留原 Critique（已为工具特有）

## 2026-05-13：Sprint 6 终审 + Sprint 8 通过 + Sprint 9 启动

- **Sprint 6 终审**：格式升级通过 ✅，质量有条件通过 ⚠️。发现 57 张卡 `source_refs: []`（KF-020 违规，Phase 1 完成声明不实）、Batches 3-4 的 query_triggers 被自动提取污染、~20 张 entrepreneur 卡 Constraints 模板化
- **Sprint 8 通过** ✅：39 张 panproduct 卡图边全填充（105 edges），2 张 management 卡 00_inbox 已清。6 张卡 14 条 related 抽查全部有效
- **[[sprint-9-cleanup-source-refs-query-triggers]]** 已创建：修复 source_refs 空值 + query_triggers 重写 + Constraints 去模板化
- **全局状态**：`source_refs: []` 仍有 57 张；`00_inbox` 残留仅剩 1 张（paddleocr-skill，非 yt- 域）
- **活跃任务**：[[sprint-9-cleanup-source-refs-query-triggers]]（P0，黄药师待领取）

## 2026-05-13：讲香域架构裁决 + 理解门禁建立

- **讲香域三方讨论完成**：黄药师建议书（[[new-course-讲香十指模型-消化建议书]]）→ 欧阳锋独立裁决 → 用户终批
- **架构方案**：1 framework + 10 tool + 1 武器库概念卡，分两批交付（基础+进阶先，增强+奇效后）
- **关键创新**：新增理解门禁——格式门禁检测不到"搬运 vs 理解"。三个信号：反例具体性、案例筛选、跨域连接
- **发现失败模式 C-8**：批处理格式升级产生"格式完整但思维空洞"的卡片（抽检 `motivation-resistance` + `peak-end-rule` 双杀）
- **校准任务**：`[[calibration-understanding-gate-motivation-peakend]]`——黄药师先深度重写两张旧卡，建立质量标尺后再进入讲香域
- **活跃任务**：`[[calibration-understanding-gate-motivation-peakend]]`（P1）→ `[[domain-xiang-jiang-deep-digestion]]`（P0）
- **待执行**：黄药师完成当前工作后领取校准任务
- **欧阳锋审查标准**：不再做程序性 checkbox 检查，每条 constraint 必须有具体场景 + 可验证的失败模式

## 2026-05-13：提示词工程域完成

- **[[domain-prompt-engineering-andre-ng]]** → completed。7 张新卡（1 framework + 4 tool + 2 concept），格式+理解双门禁通过
- **产出**：`ai-deep-work` SKILL.md + `human-ai-collaboration-playbook`，两资产通过技能门禁
- **跨域边**：提示词工程与讲香/IPO/动力阻力/武器库/科学表达五域已连接
- **讲香策略实战**：黄药师输出文章覆盖 9/10 十指策略，建议反收入讲香案例库
- **关键沉淀**：反谄媚↔冲突化同构、四遍学习法↔IPO闭环、上下文工程↔泛产品约束方法论——三组跨域同构关系已验证
- **Sprint 6**：仍进行中，下一批卡片升级待分配

## 2026-05-13：讲香域完成 + 校准通过 + 提示词工程启动

- **讲香域全部完成**：[[domain-xiang-jiang-deep-digestion]] → completed。12 张新卡（1 framework + 10 tool + 1 concept），格式门禁+理解门禁双通过
- **校准任务通过**：[[calibration-understanding-gate-motivation-peakend]] → completed。黄药师第二轮交付质量高于第一轮，理解门禁标准已被内化
- **C-8 已录入**：批处理格式升级产生"格式完整但思维空洞"卡片的失败模式
- **理解门禁制度化**：写入 `operating-principles.md` 第 6 条，成为欧阳锋审查硬标准
- **新任务**：[[domain-prompt-engineering-andre-ng]] — 吴恩达提示词课程消化 + 人机协作技能内化
- **新材料**：一堂拆书会吴恩达提示词课程口述稿（~2700行）+ PDF课件（1.4MB）
- **关键判断**：提示词工程是人机协作的操作系统层知识——需产出 wiki 卡 + executable skills/playbooks
- **活跃角色**：黄药师（执行），欧阳锋（审查+架构）

## 2026-05-12：Sprint 5 关闭 / Sprint 6 启动

- **Sprint 5 完成**：7 张 composite+framework 卡 agent-native 升级通过质量门禁
- **Sprint 6 进行中**：~66 张卡片分批升级。任务文件：`70_product/tasks/sprint-6-agent-native-upgrade-all-cards.md`
- **活跃角色**：黄药师（执行），欧阳锋（审查）
- **关键决策**：agent-native 格式已定案，不可回退到旧格式

## Session 2026-05-03 Evening

**Human**: Linhai Zhu
**Context**: KDO vault 结构评审 + 多库架构咨询

### Key Decisions Made (历史记录 — 部分已被用户终决覆盖)

> **注意：** 以下第 1、2 项的文件夹前缀方案已被用户否决。最终决策见下方 `## 最终定案` 章节。

1. ~~**Vault Architecture: 1 + N (Deferred)**~~
   ~~- 当前阶段**不拆多库**，采用单库 + 文件夹前缀隔离 + Workspaces Plus 工作区方案~~
   ~~- 三个领域文件夹：`_master/`（通用方法论）、`_healthcare/`（医疗信息化）、`_ai-saas/`（AI产品与组织方法论）~~
   ~~- 未来当单一领域超过 500 篇笔记或客户数据有强合规隔离需求时，再物理拆库~~
   → **被用户否决，改用 domain 字段方案。详见下方最终定案。**

2. ~~**单库内隔离方案**~~
   ~~- 使用下划线前缀 `_` 让领域文件夹排在文件树顶部~~
   ~~- 安装 Workspaces Plus 插件，预设三个工作区快速切换~~
   ~~- 跨领域搜索可用 `path:(_healthcare)` 等语法过滤~~
   → **被用户否决。不装 Workspaces Plus，不用前缀目录。**

3. **Obsidian 切换 Vault 的真实成本**
   - 原生切换需重新加载（2-5秒），打断心流
   - 如未来必须拆库，使用 Obsidian URI + AutoHotkey 快捷键降低摩擦
   - 软链接方案（Symlink）风险高，不推荐
   → **仍有效，但与当前 domain 方案无关。**

4. **Wiki 健康度评审结论（历史记录）**
   - 20_memory/ 之前全是占位符，本次开始填充
   - 12 sources ingested / 0 fully enriched — 已由 Builder 后续 session 解决，enrich 链路已突破 0
   - 8/10 artifacts 为空壳 — 部分已由 Builder 填充，部分仍待完成
   - 14 broken wikilinks 待修复 — 状态未知，需重新审查
   - 8 个旧 improvement plan 未标记 superseded — 已由 Builder 处理
   - 紫鲸AI重复页面已处理
   → **多数项已过时。当前状态应以最新评估文件为准。**

---

## 用户最终定案（2026-05-03）

**背景：** 另一 agent session 提议了文件夹前缀方案 + Workspaces Plus。用户评估后选择了更轻量的方案。

| 维度 | 原提议（被否决） | 最终决策 |
|------|----------------|---------|
| 领域隔离方式 | 下划线前缀目录 `_master/` `_healthcare/` `_ai-saas/` | frontmatter `domain:` 字段 |
| 例 | `30_wiki/_master/一堂调研方法论.md` | `domain: master` |
| 跨域标签 | 不支持 | `domain: ['master', 'ai-saas']` |
| 工作区切换 | Workspaces Plus 插件 | **不安装插件**，用 Dataview 按 domain 过滤 |
| 现有文件 | 需搬迁到新目录 | **不动目录**，只加一行 frontmatter |
| 执行人 | 未定 | 黄药师（已完成 ✅ 2026-05-03） |

---

### 2026-05-19：Inbox 全面盘点发现重大积压

**盘点人**：老顽童（飞书 Hermes）
**发现**：`00_inbox/` 共 438 个文件，存在任务文件未覆盖的重大素材积压。

**🔴 最大积压 — `00_inbox/科学决策/`**：
- 76 个文件（35 张 PNG + 5 份口述稿 + 36 份 OCR 转录稿）
- 图片包括：决策三角形、双三角模型、X型Y型对比、关键假设ABCD、共识曲线、ROI评估画布（1主图+4案例）、宽度/深度/高度/稀缺各层模型图
- **问题**：之前 10 张科学决策卡仅从口述稿提取，35 张 PNG 几乎未被利用。用户明确要求"图片不能跳过——35张PNG和口述稿互相佐证，跳过等于丢一半信息"
- **状态**：未分配任务，未启动消化

**🟡 第二大积压 — `00_inbox/ideas/`**：
- 112 个文件，一堂课程口述稿
- 按域分布：个人修炼(17) / 个人修身(5) / 创业必修(4) / 地图(3) / 案例拆解(2) / 其他(5)
- 大量素材尚未分类到对应 domain，未进入 KDO 管线

**🟡 待处理 — `00_inbox/design/`**：
- 两期 AI 设计分享已清理（`cleaned/`），待编译为 3 个 Skill（S1生图选型/S2 Prompt工程/S3资产管理）
- 任务文件 `laowantong-next-tasks.md` ⑤ 已规划，未启动

**🟢 轻量项**：
- `business-research-skill/` — 待入库
- `prompts/` — 6 个 prompt 文件，轻量
- `Anthropic 创始人手册.md` — 已入库

**当前活跃任务队列（老顽童）**：
1. 补 related 边（①，30min）— pending
2. 修 T1+T3 typo — pending（多次被点名）
3. 设计域 3 个 Skill（⑤）— 素材就位，待启动
4. v1.5 全库修复 89 卡（⑥）— scaffold 已可用
5. 管理工具箱 Batch 3 T6+T7+T8（⑦）— 待穿插
6. **新增**：科学决策 35 张 PNG 完整消化 — 待分配优先级

### Next Session Priorities (由 Human 决定启动)

- [ ] 科学决策 35 张 PNG + 口述稿完整消化（高价值但工作量大）
- [ ] 老顽童按队列执行：①补related边 → 修typo → ⑤设计域Skill → ⑥v1.5修复
- [ ] 修复 broken wikilink（上次排查 14 个，需重新审查当前数量）
- [ ] 给 contradictions.md 写第一条真矛盾

---

## Session 2026-05-06 Afternoon

**Human**: 朱振滔
**Context**: TinyFish 深度评估 — 调研完成，测试暂缓

### 完成的工作
1. 深度评估报告已完成：`wiki/laowantong/tinyfish-assessment-report.md`
2. Cookbook 模板已提炼：`wiki/laowantong/tinyfish-cookbook-template.md`
3. Skill 已存入系统：`tinyfish-web-agent-platform`
4. Wiki index 已更新

### 待续进度
- 需注册 TinyFish Free 账号获取 API Key
- 需跑 Fetch API / Search API 实测
- 需与 KDO `fetch-url` 做对比评估
- WSL 网络问题导致无法直接访问注册页面

### 重要结论
- Fetch/Search API **全部免费**，对 KDO 素材收集价值高
- Agent API 按 step 计费，Free 500 credits 足够评估测试
- 五绝可共用一个 key，受并发限制（Free: 2 并发 Agent）

### 复用时间节点
老板想重启时，只需说"继续搞 TinyFish"或"把 TinyFish 测试跑了"，我会自动记得当前进度并推进。

---

## ✅ 2026-05-11 黄药师方向共识（辩论完成）

**辩论路径**：v1.0 复合编译 → v2.0 细粒度+导航层 → v1.3 Agent 原生标准

**最终共识**：
- 采纳 [[agent-native-card-design]] 为强制标准
- 卡片类型：composite-concept → framework → tool 三层
- 三步编译映射为：Claims + Constraints + Synthesis 关系表 + frontmatter 图边
- 导航靠图边（component_of/related），不建 Hub Page
- 黄药师执行 Sprint 5：1 张 composite-concept + 6 张 framework 升级到 agent-native

### 黄药师当前任务
1. 压缩 `yt-composite-pan-product-methodology.md` → 12-15 claims
2. 6 张 yt-model-pan-product-* framework 卡升级到 agent-native 格式
3. 33 张 panproduct 卡 type → tool，渐进式升级

### 当前标准文件
- 内容工厂的工业化手册 v1.3：[[kdo-industrialization-manual]]
- Agent 原生设计规范：[[agent-native-card-design]]
- 高密度素材策略 v2.0：[[high-density-composite-compilation-strategy]]
