---
title: 任务仪表盘
updated: 2026-06-03
---

# 任务仪表盘

> **用法**：Agent 自己来看进度、领任务。批次全部完成后通知欧阳锋统一审查。
> **图例**：✅ 完成 · 🔨 进行中 · ⏳ 排队 · ⚠️ 阻塞

---

## 老顽童（Producer · 飞书 Hermes）

| # | 任务 | 状态 | 备注 |
|---|------|:--:|------|
| 1-16 | 5 月全部旧任务（工具箱B1-B3/设计域Skill/Anthropic手册/科学决策PNG/单元模型域/OCR Batch/综合管线/Phase C文章等） | ✅ | 全部完成，已从任务文件清除 |
| 17 | Phase 2.1：corrections.md 暗知识卡批产 | ✅ | 11 张全部 PASS。质量 A |
| **18** | **Phase 2.2：failure-modes.md 暗知识卡批产** | **🔨** | **22 种失败模式，分 7-8 批。执行中 + 写 contradicts 字段** |
| **19** | **Phase 2.3：pitfalls.md 暗知识卡批产** | **⏳** | **15 条踩坑，Phase 2.2 完成后启动** |
| **20** | **Phase 3：口述稿暗知识萃取（月白→Truman）** | **⏳ 阻塞** | **~100 张。等黄药师萃取器 A 版就绪** |
| **21** | **🆕 写卡时标注 contradicts** | **🔨** | **从 Phase 2.2 开始执行。每张新卡检查与已有卡片的矛盾** |

---

## 黄药师（Builder · Windows PowerShell）

| # | 任务 | 状态 |
|---|------|:--:|
| 1-20 | scaffold / validate / video CLI / infrastructure 等全部旧任务 | ✅ |
| Sprint 3 | produce 自动预填 | ✅ commit 6270360。欧阳锋审查通过 |
| Sprint 4 | 数据卫生（断链/frontmatter/双格式） | ✅ | **S4-1/S4-2/S4-3 全部 PASS** ✅ 欧阳锋审查通过。A类断链83→0，frontmatter245→0，双格式134→0 |
| **Sprint 5** | **Validate→Ship 闭环** | ✅ | **S5-1/S5-2/S5-3 全部 PASS** ✅ 欧阳锋审查通过。9/9 tests, 388 pytest |
| **Sprint 5a** | **Article validator source_refs 修复** | ✅ | 欧阳锋审查通过 ✅。详见 [[task-20260528-huangyaoshi-sprint5a-article-validator-fix]] |
| **Sprint 5b** | **🔨 萃取器跑通全部月白口述稿** | **🔨** | **3 篇口述稿过萃取器，产出候选 JSON。见 [[task-20260531-huangyaoshi-extractor-run-all]]** |
| Sprint 6 | query --stats/--aggregate + inbox --count/--search + kdo prompt + label pipeline | ✅ | commit 150c58b。413 tests。飞轮第一圈 Feedback 驱动 |
| Sprint 7 | produce --stats + flywheel status + 数据质量门三层 | ✅ | commit d6a38dd。16 new tests, 430 pass。飞轮可视化闭环 |

---

## 洪七公（Multimodal Arbiter · 飞书 Hermes）

| # | 任务 | 状态 | 备注 |
|---|------|:--:|------|
| 1-7 | 旧任务（双三角VA/Excalidraw/文章审计/视频试点等） | ✅ | 全部完成 |
| 8 | 科学决策域 VA 交叉审查 | ✅ | 35张图逐图审查，通过率~71% |
| 9 | VA 前置 A1（🔴10张） | ✅ | A。10/10 四维法通过 |
| 10 | **单元模型域 VA 前置**（7张 yt-unit-model 卡） | ✅ | VA 补齐完成。欧阳锋审查 A-。3处颜色违规待修（计入下个任务前置） |
| **11** | **路演域 VA 补齐**（讲香十指模型 + 表达力火箭） | **🟡** | **有条件 PASS**。ladder L207 1 处颜色残留待修（修完即结） |

### 单元模型域 VA 原图速查

| 卡 | 源图（`00_inbox/单元模型/`） |
|:---|:---|
| overview | TCPR皇冠模型.png、最简单元模型.png、十大单元模型.png、段位专家.png、修炼地图.png |
| ladder | 修炼地图.png、学练用.png、斧子尺子梯子.png、象限分析法.png |
| dynamic | 动态预测.png |
| selection ✅ | ABCD策略模型.png 等 |
| construction ✅ | 找单元模型实操难点.png 等 |
| benchmark ✅ | 基准值.png |
| ai-assisted | TCPR底层网络协议.png、人机协作-双三角模型.png |

---

## 段王爷（Publisher · 飞书 Hermes）

| # | 任务 | 状态 | 备注 |
|---|------|:--:|------|
| 1 | 🎬 KDO 视频试点 ship | ⚠️ 待补记录 | final.mp4 已就绪。需补交付记录 JSON |
| 2 | 花总AMA全流程（培训任务） | ✅ | 卡片修补3项 + 综合文章1篇全部完成。produce→validate→ship 管线跑通。见 [[task-20260529-duanwangye-huazong-ama-fixes]] |

---

## 最近完成

| 日期 | 谁 | 任务 | 结果 |
|------|-----|------|------|
| 05-28 | 欧阳锋 | Design 域第一批编译（月白AIGC设计课程） | ✅ **PASS**。3 张概念卡全流程完成。源素材 ingest → enrich → index → graph rebuild |
| 05-28 | 黄药师 | Sprint 5（Validate→Ship 闭环） | ✅ **全部 PASS**。9/9 tests, 388 pytest, S5-1/S5-2/S5-3 |
| 05-28 | 老顽童 | Phase C 文章 3 篇 | 🟡 有条件 PASS。内容 A-/A，缺 Audience/Core Thesis 节，修复后无需再审 |
| 05-28 | 老顽童 | 路演工具箱 Batch 1（故事化/数字化/比喻化） | ✅ **PASS**。Phase A+B，3卡全通过，攻击者论证充实，v1.5 0 Failed |
| 05-28 | 洪七公 | 单元模型域 VA 补齐（overview/dynamic/ladder） | ✅ A-。3处颜色违规需修 |
| 05-28 | 老顽童 | 管理工具箱 Batch 3（T6+T7+T8 精修） | ✅ A-。格式+攻击者合格。补 Synthesis+旧卡重定向后升A |
| 05-28 | 老顽童 | y-model validator 修复 + 单元模型域2处小修 | ✅ |
| 05-26 | 欧阳锋 | Batch 5 评估——不需老顽童投入 | ✅ 科学决策31张已精修，其余77张ROI低 |
| 05-25 | 老顽童 | OCR Batch 4 批量模板8张修补 | ✅ A-。5位新攻击者全部启用 |
| 05-25 | 欧阳锋 | Sprint 3 审查通过 | ✅ commit 6270360，379 tests |
| 05-25 | 欧阳锋 | Sprint 4 确认虚假报告 | ❌ 零改动零commit。P-15记录 |
| 05-24 | 洪七公 | Task 9 VA 前置 A1（🔴10张） | ✅ A |
| 05-24 | 老顽童 | OCR Batch 2+3 格式调整 | ✅ 31张统一 `## Critique` |
| 05-23 | 老顽童 | OCR Batch 1（5张视觉卡） | ✅ A+ |
