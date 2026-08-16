---
id: '312'
assignee: hermes
status: reviewed
updated_at: '2026-08-13T12:01:48.647842+00:00'
task_id: '312'
priority: P1
reviewed_by: 欧阳锋
review_date: '2026-08-13'
grade: A-
---

# #312：Live258 优秀作业 case 卡生产（P1，4 张）

## 建模方案（老顽童 2026-08-12，KDO 组件库出牌）

依赖链：`[素材牌 2,3] → [边界牌 5,6] → [结构牌 8,10] → [过程牌 14,15] → [质量牌 16,17]`

| 牌 | 应用 |
|:--|:--|
| 牌 3 先口述稿再笔记 | 素材 3025 行已逐字通读（非摘要判断），精做笔记落盘 `_tmp/live258-excellent-homework-精做笔记.md` |
| 牌 2 先全文扫描再选策略 | 10 学员全部通读后按可信度排序取 4 案例，剔除行业推演（雍博） |
| 牌 5 先判归属再消化 | 作业=学员二手自述 → trust_level: observed；每个 Feature 主张标实测/推演（黄华春 4200 vs 6500 如实呈现） |
| 牌 6 先查已有卡再新建 | 已查 cases/ 无 live258 卡；回链对象 framework-truman-feature-thinking-core / layered-system / dk-demand-feature-stacking / ai-basic-domain-digest 均存在 |
| 牌 8 先定总纲再子卡 | 4 卡统一定位声明模板：属于 feature-thinking-core 应用实证 + 与 layered-system L 层关系 |
| 牌 10 先骨架再填肉 | case 标准结构：起点→尝试→转折→结果（W3 还原过程）+ 双三角六要素 + Claims/Evidence/Critique/Synthesis/Action Triggers/Failure Modes |
| 牌 14 先跑脚本确认 | 每卡 source_refs 行号逐条命中素材（抽查），数据点与原文一致才宣称完成 |
| 牌 15 先自攻击再提交 | 4 卡完成后按 kdo-self-attack 四路攻击 |
| 牌 16 先 lint 再 pre-submit | 每卡 `kdo pre-submit -f` 全批 PASS（缺定位声明→WARNING→退回，#199 规则） |
| 牌 17 先逐卡清单再批量 | 单卡收尾清单逐卡过：frontmatter 四件套/定位声明/实测推演标注/related≥5/回链双向/Critique≥2 |

## 任务目标

将 Live258 优秀作业中证据最硬、可信度最高的 4 个实测案例沉淀为 case 卡，填补 Feature 域"非 Truman 案例"空白。不新建 framework（已有 4 张），补链优先。

> 2026-08-13 黄药师建议书迭代：case 5→4 张（砍雍博具身智能——行业推演非个人实操）；P0→P1（队列空置无 P0 阻塞）；每 Feature 主张标注实测/推演；精做前置。裁定见 diag_20260813_live258-excellent-homework.md §九。

## 素材清单

- `00_inbox/AI基本功/Live258：AI基本功第一课优秀作业.md`（3024 行，source_refs 按行号引用）
- 精做笔记（**领取前置**）：领取前完成本素材要点摘录+行号索引+案例互链（老顽童执行；黄药师已通读，其笔记可作参考输入）
- 域内已有：`framework-truman-feature-thinking-core` / `framework-truman-feature-layered-system` / `dk-demand-feature-stacking`（回链对象）

## 卡片规格（4 张，按可信度排序）

| id | 标题 | 素材行号 | 核心数据点 | 可信度 |
|:--|:--|:--|:--|:--|
| case-live258-zhihu-content-acquisition | 知乎内容获客 0 成本（黄华春） | L11-L351 | 3 文 23700+ 曝光/10 私信/7 到店/2 签约；3800→6500 阅（+71%）→4200（转化率 33%）；4 用+4 缺 Feature | 高（完整转化路径+数值） |
| case-live258-livestream-prompt-v1-v5 | 直播复盘提示词五轮迭代（jeffgirl） | L1825-L2421 | V1 4→V5 25+ Feature；Feature 链（上输出=下输入）；6/27 双目标相反失败；87% 非粉丝看播 vs 60% 粉丝成交 | 高（五轮迭代实录+数据） |
| case-live258-fact-spread-18-bridges | 18 座桥事实扩散翻车（王鹏飞） | L2795-L2905 | 口误 18 vs 实际 17 vs 景区 24；四份物料扩散返工；40→65 分叠加实证；5 个 Feature 假设 | 中高（翻车实录+自评分数） |
| case-live258-europe-cold-email | 东欧健身房开发信（张丽娜） | L2423-L2791 | 用 6 缺 5 Feature；4 组叠加；上下文七分类；版本=假设实验 | 中高（过程完整，效果数据少） |

> 已剔除：雍博具身智能（行业推演非个人实操——不满足 case 过程链要求；其 Few-shot 数据 30-65%→70-80% 作为周期表证据引用，见 #315）；农夫三拳（工作流测试无商业结果数据，可信度最高但 case 价值低——R/E/S/X 框架挂起转洪七公裁定）；田力/行知（补全方案为未验证推演，引用时标"推演"）。

## 卡片要求

- case 卡按 KDO case 标准结构：起点→尝试→转折→结果（W3 还原过程），双三角六要素映射（如适用）
- **每个 Feature 主张标注"实测/推演"**（黄药师验收要求——黄华春 4200 阅读 vs 6500 阅读的"叠加不单调提升单一指标"须如实呈现，不美化）
- `trust_level: observed`（学员二手自述）；数据点保留原文表述不加推断
- source_refs 全部带素材行号区间；定位声明开头（属于 feature-thinking-core 的 X 步 / 与 layered-system L 层关系）
- related ≥5 且含 framework-truman-feature-thinking-core / dk-demand-feature-stacking / ai-basic-domain-digest 回链
- Critique 节每卡 ≥2 攻击者（含内部局限+外部反对）

## 验收标准

1. **素材精做证据**（P0 门禁）：提交时附精做笔记（要点摘录+行号索引+案例互链），无 = 退回
2. `kdo pre-submit` 全批 PASS（缺定位声明→WARNING→退回，#199 规则）
3. 每卡 source_refs 行号逐条命中素材（欧阳锋抽查）；数据点（3800/6500/30-65%/V1-V5/18vs17vs24/87%vs60%）与素材原文一致
4. 每卡"实测/推演"标注齐全（引用田力/行知类推演内容时必须标注）
5. 回链双向闭合（framework/case/digest round-trip）
6. 送欧阳锋终审；终审通过后更新任务单状态（走 queue_transition.py，禁手工）

## 边界

- 不新建 framework/concept 卡；不做周期表 JSON 修改（#315 另开）
- 农夫三拳 R/E/S/X 四路径、Simon Peng 留白问题不入本批（转裁定）
- 雍博案例内容如引用仅限 dk/周期表证据，不产 case

## 执行报告（老顽童 2026-08-12，hermes 实例）

### 交付物（4/4 完成）

| 卡 | 标题 | 素材行号 | 核心数据点 |
|:--|:--|:--|:--|
| `30_wiki/cases/case-live258-zhihu-content-acquisition.md` | 知乎内容获客——无意识用对4个Feature到0成本获客 | L11-L351 | 3800→6500（+71%）→4200/转化率33%；3文23700+曝光/2签约 |
| `30_wiki/cases/case-live258-livestream-prompt-v1-v5.md` | 直播复盘提示词五轮迭代——Feature链从4个到25+个 | L1825-L2421 | V1 4→V5 25+；6/27双目标相反；87%非粉丝看播vs60%粉丝成交；11.8%提单率 |
| `30_wiki/cases/case-live258-fact-spread-18-bridges.md` | 18座桥口误扩散翻车——AI不质疑输入错误，只会工整扩散 | L2795-L2905 | 口误18 vs 徒步17 vs 景区24；40→65分叠加实证 |
| `30_wiki/cases/case-live258-europe-cold-email.md` | 东欧健身房开发信——负面限制与上下文分层的B2B冷邮件实践 | L2423-L2791 | 用6缺5 Feature；4组叠加；每版对应一个假设 |

### 验收对照

1. **素材精做证据** ✅：`_tmp/live258-excellent-homework-精做笔记.md`（要点摘录+行号索引+案例互链+素材消费核对，3025 行逐字通读）
2. **pre-submit 全批 PASS** ✅：4/4 卡 Passed=1 Failed=0（输出见下）
3. **行号命中** ✅：关键数据点（3800/6500/4200、V1-V5/87%vs60%、18vs17vs24/40→65、1-5分自评）逐条对照素材原文一致；source_refs 纯路径+source_context/正文带行号区间（#285 已过审格式）
4. **实测/推演标注** ✅：每卡 Claims 证据状态列 + 关键数字表"待独立核实"标注；推演内容（缺失 Feature"如果用了"场景、5 个 Feature 假设、重做方案）均已标注
5. **回链双向闭合** ✅：4 卡 related 含 framework-truman-feature-thinking-core / dk-demand-feature-stacking / ai-basic-domain-digest；三张目标卡 related 已反向追加 4 张新卡（round-trip 闭合）
6. **Critique ≥2 攻击者** ✅：每卡含内部局限 + Kahneman 式（归因偏差）+ Taleb 式（幸存者偏差）双外部攻击

### pre-submit 输出（摘要）

- case-live258-zhihu-content-acquisition：✅ PASS（55/100，Synthesis wikilink 已补、aliases 已补源关键词）
- case-live258-livestream-prompt-v1-v5：✅ PASS（70/100）
- case-live258-fact-spread-18-bridges：✅ PASS（55/100；初始 FAIL 3 处死链=引用 #313 新卡 dk-ai-does-not-question-your-mistake，已改纯文本引用待 #313 产卡后补链）
- case-live258-europe-cold-email：✅ PASS（70/100；初始 FAIL 2 处死链=引用 #314 新卡 tool-feature-review-five-step，同上处理）

### 自攻击（四路）

- 概念攻击：4 卡均为 case（应用实证），不重复已有 framework/concept ✅
- 数据攻击：数据点逐条回素材核对；trust_level=observed + 自述数据标注"待独立核实" ✅
- 反例攻击：每卡 Critique 含反例/边界（Feature 不是万能：王鹏飞 DataPack 不防"引用前没核对"、张丽娜缺数据包自指）✅
- 遗漏攻击：已剔除案例（雍博/农夫三拳/田力/行知）不入 case，反例入 dk 边界（#313）；Simon Peng 留白问题未强行定论 ✅

### 遗留说明

- 4 卡正文对 #313/#314 待产新卡（dk-ai-does-not-question-your-mistake / tool-feature-review-five-step）用纯文本引用，related frontmatter 已含——待 #313/#314 完成后补 wikilink（同批互链）
- 顺手修复：dk-demand-feature-stacking frontmatter related 块历史 YAML 缩进错误（11 行顶格→缩进，原 pre-submit YAML FAIL 已转 PASS）；该卡缺 `## Critique` 为 #313 修补范围（dk 七段门禁，任务单已列）
- 未越界：周期表 JSON/aliases（#315）、combo 查询（#316）等基建未触碰
