# Project Continuity

## 2026-05-15：工业化手册 v1.4 + Sprint 11 启动

- **KDO 方法论升级 v1.4**：对标 AI 思维卡「认知升级系统 v3.2」，引入行为转化层（ACTION→CTA→FOLLOWUP）、EVIDENCE 审计标准（偏差标注+外部攻击+反事实）、Burn line。新增 KF-023 和 F-KDO-016
- **审而不改**：控制文件和规则由欧阳锋直接改。知识卡和素材处理走 KDO 管线，黄药师执行
- **[[sprint-11-cognitive-upgrade-framework]]** 已创建——AI思维卡 HTML ingest + 十步框架萃取 + PEAS 工具卡
- **活跃任务**：[[sprint-11-cognitive-upgrade-framework]]（P0，黄药师待领取）

- **[[sprint-9-cleanup-source-refs-query-triggers]]** → completed ✅。52 张 source_refs 归零，31 张 triggers 重写，20 张 Constraints 去模板化
- **[[sprint-10-fill-remaining-related-edges]]** 已创建——76 张非 panproduct 卡图边填充 + 管理域收尾
- **活跃任务**：[[sprint-10-fill-remaining-related-edges]]（P0，黄药师待领取）

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

### Next Session Priorities (由 Human 决定启动)

- [ ] 调研方法论 artifact 填充（角度已定：面向创业者的实操指南，等 Builder 执行）
- [ ] 继续 enrich 下一批一堂课程
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
