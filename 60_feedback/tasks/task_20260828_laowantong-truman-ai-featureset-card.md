---
id: 571
assignee: laowantong
status: in_progress
updated_at: '2026-08-28T01:45:37.619837+00:00'
version: v0.1
instance: laowantong
code_files: []
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
