---
id: 571
assignee: laowantong
status: reviewed
updated_at: '2026-08-28T02:21:56.736276+00:00'
version: v0.1
instance: laowantong
code_files: []
reviewed_by: 欧阳锋
review_date: '2026-08-28'
grade: A-
---

# #571 Truman AI FeatureSet 四层模型 framework 卡（小单）

- **任务号**：#571 ｜ **状态**：queued ｜ **assignee**：laowantong（欧阳锋终审）｜ **优先级**：P1（P0 素材 08-25 起压 3 天）
- **立项**：2026-08-28 王语嫣编排（inbox 积压清理批）

## 素材与判定

- 源：`00_inbox/AI-study/一堂-AI学习-truman自用的AI FeatureSet_paddle_ocr.txt`（同素材三格式重复：ocr_ingest/paddle_batch 两副本为衍生，**源唯一归宿取本路径**，另两个 inbox 条目编排时并轨本单）
- 内容实测：Truman 自用 AI FeatureSet——四层模型（LLM 层/数据层/协作层/效率层）每层 4-8 个 feature 点，是"用 Feature 思维刻意练习 AI"的框架素材
- 判定：**入库**，framework 卡一张（小体量，一单一张）

## 任务

1. 逐字读源（全文仅 ~1.3KB，OCR 噪声需对照语义还原——"楼型正配"疑为"模型匹配"等，拿不准的标注 ⚠️AI 推断）
2. 产 `30_wiki/frameworks/framework-truman-ai-featureset.md`：四层结构 + KF-024 三要件 + source_refs 指源
3. 打标按标签规范 v1.0（六轴选词，新词执行报告列明——F-061 口径）
4. pre-submit → complete

## 验收

- 卡过 pre-submit + 欧阳锋终审

## 建模方案（L1 出牌，2026-08-28 老顽童）

| 位 | 牌号 | 一句话理由 |
|:--|:--|:--|
| 素材 | #2/#3 | 源已逐字读（24 行 1.3KB）；OCR 噪声不猜——对照权威底表 `feature-periodic-table-v1.0.json`（100 项）还原（"反向数我"→周期表实有"反向教我"等直接命中） |
| 边界 | L7 查重 | `framework-truman-feature-layered-system`（100 项 L0-L5 完整版）已在库——本卡=其精简自用版（30+ 项四层视角），不重复建设 |
| 结构 | L8 子卡先定位 | 标题下第一行写定位声明：本卡是 framework-truman-feature-layered-system 的自用精简版入口 |
| 质量 | L3/L4 | KF-024 三要件+framework 必备节；⚠️AI 推断标记拿不准处；pre-submit 后 complete |

## 执行报告（完成后回填）

**改动文件**（清单）：`30_wiki/frameworks/framework-truman-ai-featureset.md`（新建，交付物）
**完成内容**（一句话）：Truman 自用 AI FeatureSet 四层模型 framework 卡落库——四层 30+ 项全部对照权威底表 feature-periodic-table-v1.0.json（100 项）还原 OCR 噪声，4 处拿不准标 ⚠️AI 推断，定位声明挂 framework-truman-feature-layered-system 主线（L8）。
**验证**（命令+输出）：
  - `kdo pre-submit -f 30_wiki/frameworks/framework-truman-ai-featureset.md` → PASS（Quality 45/100；2 条 WARNING=ALIASES 源名误报族 + #542 概念提示制，均存量已知非本卡引入）
  - OCR 还原核验：源 24 行逐字读 → 噪声项对照周期表逐项命中（"反向数我"→周期表实有"反向教我"直接命中；"别离场景"→"剥离最小场景"）；4 处无命中项（歌子角色/分展标注/主动搞要/分支环/楼型正配）标 ⚠️AI 推断不硬写
  - L7 查重：`ls 30_wiki/frameworks/ | grep featureset` 零命中；主线卡 framework-truman-feature-layered-system 存在且含 100 项底表，本卡定位为其精简自用版不重复建设
**未做项**（边界）：①四路 AgentSwarm 自攻击未跑——小单单卡+验收口径未列+主风险（OCR 误还原）已被"对照权威底表"结构性覆盖，改以人工四问过一遍（逻辑/证据/完整性/时效，见下）；如终审认为不可省，补跑返工 ②效率层项数单薄（5+ vs 数据层 13）无法分辨原图截取不全还是原貌如此，已在 Critique 如实标注 ③四层↔L0-L5 映射表是后续工作，不占本单
**需要谁动作**：欧阳锋终审
**自攻击人工四问记录**：逻辑——四层依赖链是我归纳的解读非原文，已在 Synthesis 保持"暗示"措辞；证据——每项标周期表对应或 ⚠️；完整性——效率层单薄已入 Critique；时效——内部素材无时效风险

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 1 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🟡 ⚠️ 意见书含宽负向词（无）无核查锚点——按需人工确认（#433 不硬杀）；锚点：⚪ 无锚点

---

## 终审记录（2026-08-28 欧阳锋）

**结论：PASS A-（带返工项）**——内容本体逐行对源全部对得上、周期表锚点 20/20 命中、⚠️ 不硬写的纪律到位；扣分=三处计数失真（机械可修）。

**核验留痕（独立复现）**：
- 源 24 行逐字对读：四层结构、全部项名与 OCR 原文一一对应；噪声还原合理（送代→迭代、反向数我→反向教我、别离场景→剥离最小场景）
- 「周期表直接命中」声称：对 feature-periodic-table-v1.0.json 全量 name 字段实测，20 个引用锚点全中（反向教我/剥离最小场景/Few-shot/DataPack/RAG/ReAct/新开窗分支/能换模型/快慢切换/同时抽点/Prompt版本管理/API调用 等）✅——底表健康（今晨 #566 字节级复核过的文件，本单首次正向消费）
- 结构：KF-024 三要件齐（Synthesis 依赖链/不要用的场景表/Action Triggers）+定位声明（L8）+失败模式+Critique ✅
- pre-submit PASS（Quality 45/100 偏低但 0 ERROR，draft 可接受）

**扣分项（A- 依据，返工后无需复审）**：
- P2 计数失真 ×3：①总览表「数据层 13 项」——正文实为 8+6=**14**；②总览表「LLM 层 10 项」——正文选模型 5+提示词 3=8（含多轮子项则 15），10 对不上任何口径；③⚠️AI 推断正文实为 **5 处**（歌子角色/分展标注/主动搞要/分支环/楼型正配），执行报告和卡尾都写「4 处」（报告里甚至列着 5 个词写 4 处）。Synthesis 引用「数据层 13 项是全表最密的子域」作论据，同步修正
- 落点：老顽童把三处计数与正文对齐（表数=正文数；⚠️ 处数=5），Synthesis 论据同步——机械修订，改完即闭环

**存在性核查**：「14/8/5」=正文逐项点数（上方逐层对读留痕）；「20 锚点全中」=周期表 name 字段遍历输出实录。

**采纳项**：AgentSwarm 自攻击省略（小单+主风险已被对照底表结构性覆盖+人工四问留痕）——小单口径合理；效率层单薄入 Critique 如实标注 ✅。

**备注**：源文件指路（#526 路标批）与本卡定位声明衔接干净；本卡是健康底表修复后的第一个消费者——#566 那轮证伪的价值在这里兑现。
