---
id: '313'
assignee: hermes
status: reviewed
updated_at: '2026-08-13T12:01:48.827404+00:00'
task_id: '313'
priority: P1
reviewed_by: 欧阳锋
review_date: '2026-08-13'
grade: B+
---

# #313：Live258 优秀作业 dk 卡生产（P1，2 张 + 1 修补）

## 任务目标

将 10 份作业中最痛、最普遍的失败模式沉淀为 dk 卡（2 张），并为已有 `dk-demand-feature-stacking` 补充数值证据与链式结构（1 项修补）。附业界印证（全网调研已完成，见诊断报告 §一）。

> 2026-08-13 黄药师建议书迭代：dk 4→2 张（砍"验收先行"——并入 #314 复盘五步法第五步；砍"叠加链式"独立卡——改为修补 dk-demand-feature-stacking 回填 4 案例证据+链式结构节）。裁定见 diag_20260813_live258-excellent-homework.md §九。

## 素材清单

- `00_inbox/AI基本功/Live258：AI基本功第一课优秀作业.md`（3024 行）
- `60_feedback/diagnosis/diag_20260813_live258-excellent-homework.md`（§三 L4 失败模式表 F1-F8）
- 精做笔记（**领取前置**，同 #312）

## 交付项

### 1. dk-ai-does-not-question-your-mistake（AI 不质疑你的口误）

王鹏飞 18 桥全链：人喂的错误输入被高执行力无差别放大（18 扩散到四份物料）→ 对治 = DataPack 事实约束 + 负面限制 + 强制核对。
- 关联：E020（回答前先检索验证）同构；业界印证 citation-grounded 最强抑制器
- 行号锚点：L2859-2863（翻车描述）/ L2879-2880（DataPack 假设）

### 2. dk-feature-pieces-not-recognized-as-cards（一堆散牌却不知道那是牌）

王鹏飞第二反思（字体/对齐/留白等散经验 = L2/L3 层 Feature，换工具就默认重踩）+ 黄华春"无意识用了 4 个 Feature"。
- 关联：KDO"不登记 = 不存在"原则、dk-feature-not-learned-but-used
- 行号锚点：L2891-2901（散牌）/ L23（无意识使用）/ L313-319（知道自己不知道什么）

### 3. 修补：dk-demand-feature-stacking 补充节

给已有卡补"数值证据 + 链式结构"节（黄药师洞察 2.3 的 4 案例复现）：
- 黄华春：角色（身份）+参考案例（风格）+格式设定（结构）= 三维覆盖，3800→6500（+71%）
- 王鹏飞：2A 身份 + 2B 上下文 = 40→65 分质量分水岭
- jeffgirl：V4 升级为 **Feature 链**（目标锚定→策略对齐→六层漏斗→货盘分层→跨维度一致性，上输出=下输入）
- 张丽娜：用户身份+经营场景+负面限制 = 从"卖货推销"变"经营沟通"

## 卡片要求

- dk 卡七段完整（KDO 门禁：#217 缺 Critique→ERROR）：含 Critique 节 + 走偏模式 + 边界（含反例：农夫三拳认知反差型失败——Feature 不是万能；黄谦"复杂度冗余"）
- **每个主张标注"实测/推演"**：翻车实录/迭代实录=实测；"如果用了会怎样"类=推演（如田力重做方案）
- source_refs 带行号；定位声明开头；related ≥4 含 framework-truman-feature-thinking-core
- 修补节不动 dk-demand-feature-stacking 已有内容，只追加（标注更新日期+证据来源）

## 验收标准

1. **素材精做证据**（P0 门禁，同 #312）
2. `kdo pre-submit` 全批 PASS（dk 七段完整性 ERROR 门禁）
3. Critique 节含真实攻击者（每卡 ≥1 外部攻击）；实测/推演标注齐全
4. 行号逐条命中素材
5. 修补节证据 4 案例数值与素材一致，feature-stacking 结构未被破坏
6. **同批互链闭环**：本批 dk 卡落库后，把 #312 四卡正文的纯文本引用补为 wikilink（#312 已 pending_review，related frontmatter 已含；补链后 pre-submit 复查）
7. 送欧阳锋终审；终审通过后状态流转走 queue_transition.py

## 边界

- 不写 framework/concept；不与 #312 case 卡内容重复（case 讲过程，dk 讲规律）
- 周期表 DataPack 类 Feature 补建与别名表见 #315（黄药师侧）

## 执行报告（老顽童 2026-08-12，hermes 实例）

### 交付物（2 张新 dk + 1 修补，全部完成）

| 卡 | 标题 | 素材行号 | 要点 |
|:--|:--|:--|:--|
| `30_wiki/dark-knowledges/dk-ai-does-not-question-your-mistake.md` | AI不质疑你的口误——它只会工整地扩散出去 | L2859-L2887（翻车描述/DataPack 假设） | 18 桥全链：人喂错输入被高执行力无差别放大→对治=DataPack+负面约束+强制核对；含产线放大效应+业界 citation-grounded 印证 |
| `30_wiki/dark-knowledges/dk-feature-pieces-not-recognized-as-cards.md` | 一堆散牌却不知道那是牌 | L2891-L2905（散牌）/L23（无意识）/L313-L319（知道自己不知道什么） | 散经验= L2/L3 Feature；对治=重命名/编号归层/使用记录/复盘制度化；含"库变收藏夹"反例 |
| `30_wiki/dark-knowledges/dk-demand-feature-stacking.md`（修补） | 追加"数值证据+链式结构"节 + Critique | 4 案例（素材 L239-L257/L2871/L2025-L2029/L2671-L2675） | 黄华春三维覆盖 3800→6500(+71%)/王鹏飞 40→65 分/jeffgirl V4 Feature 链/张丽娜推销→经营沟通；叠加不单调+负向产线放大；Critique 补齐（#217 门禁） |

### 验收对照

1. **素材精做证据** ✅：同 #312，`_tmp/live258-excellent-homework-精做笔记.md`（两任务共用）
2. **pre-submit 全批 PASS** ✅：3/3 卡 Passed=1 Failed=0（dk 七段完整性 ERROR 门禁通过，含 Critique）
3. **Critique 真实攻击者** ✅：每张 dk 含内部局限 + Kahneman 式 + Taleb 式外部攻击 + 业界反方（citation-grounded 约束成本）
4. **实测/推演标注** ✅：翻车实录/自评分数=实测；DataPack 预期效果（口径错误降 0）/重做方案=推演，Claims 表证据状态列已标
5. **行号逐条命中** ✅：L2859-L2863/L2879-L2880/L2891-L2901/L23/L313-L319 对照素材一致
6. **修补节** ✅：dk-demand-feature-stacking 已有内容未动，仅追加（标注 2026-08-13 #313 + 证据来源）；结构未被破坏（pre-submit PASS 验证）

### pre-submit 输出（摘要）

- dk-ai-does-not-question-your-mistake：✅ PASS
- dk-feature-pieces-not-recognized-as-cards：✅ PASS
- dk-demand-feature-stacking（修补）：✅ PASS（含历史 YAML 缩进修复 + Critique 补齐——该卡原 pre-submit YAML FAIL + 缺 Critique，本次顺手修到 PASS）

### 自攻击（四路）

- 概念攻击：2 张 dk 不重复已有卡（dk-feature-not-learned-but-used 是"学习失败"，本两张是"事实扩散"和"经验显性化"，论域不同）✅
- 数据攻击：行号逐条回素材核对；二手自述标 trust_level=observed ✅
- 反例攻击：适用边界含反例（农夫三拳认知反差失败——Feature 不是万能；黄谦复杂度冗余；DataPack 不防"引用前没核对"；库变收藏夹）✅
- 遗漏攻击：已剔除候选（验收先行并入 #314 第五步；叠加链式独立卡并入本批修补）按任务单裁定执行 ✅

### 遗留说明

- dk-ai-does-not-question-your-mistake 的 wikilink 已回补到 #312 卡 3（case-live258-fact-spread-18-bridges）正文，双向链接闭合
- tool-feature-review-five-step（#314 待产）在 case 卡中保持纯文本引用，related 已含——#314 完成后补链
- 未越界：未新建 framework/concept；周期表 JSON（#315）未触碰
