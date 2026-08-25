---
id: 526
assignee: laowantong
status: reviewed
updated_at: '2026-08-25T14:36:59.344754+00:00'
version: v0.1
instance: kimi-cli
code_files:
- 10_raw/ocr-cards/ocr-一堂-ai学习-truman自用的ai-featureset.md
- 30_wiki/frameworks/framework-truman-feature-layered-system.md
- 30_wiki/frameworks/framework-truman-feature-thinking-core.md
- 30_wiki/bridges/bridge-two-feature-systems.md
- 30_wiki/domains/ai-basic-domain-digest.md
- 30_wiki/dark-knowledges/dk-analogy-blinds-search.md
reviewed_by: 欧阳锋
review_date: '2026-08-25'
grade: A
---

# #526 Feature 域入口路标收尾批（盲测报告建议 1/2/3/7 + 类比遮蔽 dk 卡）

- **任务号**：#526
- **状态**：queued
- **assignee**：laowantong（内容批；欧阳锋批次验收）
- **优先级**：P2（入口层收尾——低成本高收益，盲测同口径复测预期全绿）
- **立项**：2026-08-25 王语嫣（小昭《KDO知识库检索检测报告与建设建议》裁定；老朱对齐确认+每日一问节奏拍板）

## 背景

老朱自然语言盲测 4 问（小昭仅 grep/glob/read）：第 1 问「feature 有哪些怎么分类」未命中周期表框架卡（无声的错误=拿到 30% 答案自以为完整）。根因=入口层缺路标：OCR 转录卡 related 空、自然问法未注册、两套 Feature 体系无澄清、digest 无资产地图。原件在 inbox 三处落点（AI-study/paddle_batch/ocr_ingest），检索者从哪层进来哪层就要有路标。

## 任务

1. **转录卡挂链**：`10_raw/ocr-cards/ocr-一堂-ai学习-truman自用的ai-featureset.md` 补 related→framework-truman-feature-layered-system；正文加指路行（自用精简版 30+ vs 完整周期表 100/L0-L5，数据源 v1.0.json）
2. **inbox 三处副本指路注释**：`00_inbox/AI-study/一堂-AI学习-truman自用的AI FeatureSet_paddle_ocr.txt`、`00_inbox/paddle_batch/同名.md`、`00_inbox/ocr_ingest/src_ocr_一堂_AI学习_truman自用的AI_FeatureSet.md` 各加一行指路（轻量注释，不改原内容）
3. **问法回填 discoverable_by**（复用 #315 模式）：layered-system 卡增 `truman的feature分类`/`feature有哪些`/`feature怎么分`/`周期率表`（笔误也收）；feature-thinking-core 卡增 `feature思维`/`T型F型`/`feature和工具的区别`
4. **澄清卡** `bridge-two-feature-systems`：cap_hub/features.json（KDO 工程 Feature）vs feature-periodic-table（AI 能力 Feature）一句话区分+互指，防 grep 互相污染
5. **digest 路标**：`30_wiki/domains/ai-basic-domain-digest.md` 头部加「本域核心资产路标」（Feature 思维根卡/周期表/v1.0.json/feature_menu.py）
6. **dk 卡** `dk-analogy-blinds-search`：类比遮蔽检索——比喻带来「已理解」错觉跳过实体验证；发现者署名小昭（消费端贡献首例），实证=本次盲测第 1 轮

## 边界

- 只加路标/挂链/回填，不改资产本体内容；OCR 卡维持 10_raw 层不升 30_wiki（流转规范：OCR 默认 10_raw，trust=low）
- 问法回填只收本次实证问法，不臆造同义词

## 验收

- 复测第 1 轮问法（grep「truman feature 分类」类自然问法）能经任一层路标到达 layered-system 框架卡（附检索路径输出）
- 澄清卡/dk 卡过欧阳锋批次验收（dk 卡走三方法口径按 P2 卡从简）
- 欧阳锋终审

---

## 执行报告（F-034 五字段 · 2026-08-25 老顽童 kimi-cli）

**文件清单**：10_raw/ocr-cards/ocr-一堂-ai学习-truman自用的ai-featureset.md（挂链+指路）/ 00_inbox 三处副本（AI-study .txt + paddle_batch .md + ocr_ingest .md 各追加指路注释）/ framework-truman-feature-layered-system.md + framework-truman-feature-thinking-core.md（discoverable_by 回填）/ 30_wiki/bridges/bridge-two-feature-systems.md（新建澄清卡）/ 30_wiki/domains/ai-basic-domain-digest.md（头部资产路标）/ 30_wiki/dark-knowledges/dk-analogy-blinds-search.md（新建 dk 卡）。

**完成内容**（六项全做）：
1. OCR 卡 related→framework-truman-feature-layered-system + 正文指路行（精简版 30+ vs 完整周期表 100/L0-L5/v1.0.json/feature_menu.py）；顺手修 pre-submit 拦截的存量 domain 污染（yitang→yihang，#493 漏网）
2. inbox 三处副本各尾部追加指路注释（🪧 标记+#526 批次+日期，原内容零改动）
3. discoverable_by 回填（只收实证问法）：layered-system +4（truman的feature分类/feature有哪些/feature怎么分/周期率表-笔误收）；thinking-core +2（feature思维/feature和工具的区别——T型F型已有不重复）
4. bridge-two-feature-systems 新建：一句话区分表（cap_hub/features.json=KDO 工程 Feature vs feature-periodic-table-v1.0.json=AI 能力 Feature）+互指；头部注明完整论述见 bridge-dual-track-feature-system（L7 查重发现已有双轨桥接卡，本卡只做轻量路标不复制内容）
5. ai-basic-domain-digest 头部加「本域核心资产路标」5 条（根卡/周期表/v1.0.json/feature_menu.py/澄清卡）
6. dk-analogy-blinds-search 新建：类比遮蔽检索——比喻带来「已理解」错觉跳过实体验证；发现者署名小昭（消费端贡献首例），实证=盲测第 1 轮；六段 dk 结构齐全（原始表述/使用场景/操作方法/适用边界/为什么值钱/关联）；小昭报告原件经飞书入未在库，source_refs 锚任务单并卡内注明待补（不编造）

**验证**：`kdo index` 重建（4146 docs）→ pre-submit 6 文件 **Passed 6 / Failed 0**（WARNING 均为存量 tags/src_unknown，不阻断）；**验收复测**：`kdo query "truman的feature分类"` 与 `kdo query "feature有哪些"` 均 Top-1 命中 framework-truman-feature-layered-system（附检索路径输出于会话记录）——盲测第 1 轮问法修复实证 ✅。feat commit 先行（path-scoped，9 文件）。

**未做项**：无。

**需要谁动作**：欧阳锋终审（澄清卡/dk 卡批次验收；dk 走 P2 从简口径）。

## 终审记录

- **终审**：欧阳锋 08-25 **PASS A**（批次验收，P2 从简口径）
- **版本对齐**：feat commit 13b501d29（22:19，提审 22:20 前先行，path-scoped 9 文件）✓
- **O0 溯源（六项逐条）**：①OCR 卡 related 挂链+指路行 ✓（`:19-24`，30+ vs 100/L0-L5/v1.0.json/feature_menu.py 全要素）；②inbox 三处副本指路注释 ✓（🪧+批次+日期+原内容零改动，三处实测）；③discoverable_by 回填 ✓——layered-system +4 全在（**笔误"周期率表"已收**，`:29-32`）、thinking-core +2 在（feature思维/feature和工具的区别），T型F型已有不重复声明属实；④bridge 澄清卡 ✓（一句话区分表+互指+L7 查重声明=只做轻量路标不复制 bridge-dual-track 内容，frontmatter 三轴 tags 齐全）；⑤digest 路标 5 条全 ✓（`:66`——在"域定义"节前=逻辑头部，任务书"头部加"措辞与落点轻微出入不降级）；⑥dk 卡 ✓（六段齐全、小昭署名、source_refs 锚任务单+报告原件待补注明=不编造纪律、同族 dk 关联）
- **验收复测亲跑**：`kdo query`（asyncio 直调 search）两问法 Top-1 均命中 framework-truman-feature-layered-system ✓——盲测第 1 问修复实证；**且命中卡带 ⚠️（draft）前缀**——#524 消费端契约在本批复测中活体生效，双单交叉验证
- **pre-submit 复跑**：本批 6 文件 PASS（9 条 WARNING 均存量 tags/src_unknown 不阻断）与声明一致 ✓；#517 门禁活体（OCR 卡存量占位 WARNING 标出）+「有警在身」安慰语修正生效 ✓
- **边界**：资产本体未改、OCR 卡守 10_raw 层、问法只收实证 ✓；顺手修 domain 污染（yitang→yihang）属声明内附带修复，diff 小可接受
- **批次收尾**：bridge/dk 两新卡补 review_mark（见下）
