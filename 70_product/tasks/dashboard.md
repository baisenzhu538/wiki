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
| **18** | **Phase 2.2：failure-modes.md 暗知识卡批产** | **✅** | **14 种失败模式全部完成（dk-f1 ~ dk-f14）。欧阳锋审查 A** |
| **19** | **Phase 2.3：pitfalls.md 暗知识卡批产** | **✅** | **19 张 dk-p* 卡产出。新版 18 张 A-，contradicts 已补** |
| **20** | **Phase 3：口述稿暗知识萃取（月白→Truman）** | **⏳** | **30 张目标，首批 10 张已入库。暂停，先处理 AI 俱乐部四篇** |
| **21** | **🆕 写卡时标注 contradicts** | **✅** | **33 张卡已补完。格式待统一（wikilink→纯文本 id）** |
| **22** | **🆕 AI俱乐部四篇文章（纪浩/马易/半肥猫/水水）** | **🔜** | **素材在 00_inbox/，按顺序处理。见 laowantong-next-tasks.md** |

---

## 黄药师（Builder · Windows PowerShell）

| # | 任务 | 状态 |
|---|------|:--:|
| 1-20 | scaffold / validate / video CLI / infrastructure 等全部旧任务 | ✅ |
| Sprint 3-7 | 全部交付（produce 预填/数据卫生/Validate→Ship/video CLI/Sprint 6-7） | ✅ | **全部欧阳锋审查通过。Sprint 7 评级 A** |
| Sprint 5b | 萃取器跑通全部月白口述稿 | 🟡 | 已产出候选 JSON。待欧阳锋确认后续 |
| **Task A** | **陈旧标记规则（`kdo stale`）** | **🔜** | **已实现，待欧阳锋审查后 commit** |
| **Task B** | **增量传播机制—反向引用索引（`kdo stale --propagate`）** | **⏳** | **Task A 完成后启动** |
| **🆕 Task C** | **技能点扫描器（扫描已有素材的遗漏技巧）** | **🔜** | **识别所有已 ingest 素材中被遗漏的可操作技巧，输出候选清单** |

---

## 洪七公（Multimodal Arbiter · 飞书 Hermes）

| # | 任务 | 状态 | 备注 |
|---|------|:--:|------|
| 1-7 | 旧任务（双三角VA/Excalidraw/文章审计/视频试点等） | ✅ | 全部完成 |
| 8 | 科学决策域 VA 交叉审查 | ✅ | 35张图逐图审查，通过率~71% |
| 9 | VA 前置 A1（🔴10张） | ✅ | A。10/10 四维法通过 |
| 10 | **单元模型域 VA 前置**（7张 yt-unit-model 卡） | ✅ | VA 补齐完成。欧阳锋审查 A-。3处颜色违规待修（计入下个任务前置） |
| **11** | **路演域 VA 补齐**（讲香十指模型 + 表达力火箭） | **🟡** | **有条件 PASS**。ladder L207 1 处颜色残留待修 |
| **12** | **🆕 清单体笔记图片 OCR 处理** | **✅** | **2 张图片 OCR → 结构化文本已输出** |
| **13** | **🆕 [临时] 产品内核 OCR → 结构化入库（熟悉 kdo enrich 管线）** | **🔜** | **内核画布+十大指标图片已有 OCR → 用 kdo enrich 转成结构化素材** |

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
| **2** | **🆕 [临时] 50_delivery/ 发布审计（熟悉 kdo ship → validate 闭环）** | **🔜** | **检查所有已交付项的 kdo validate 状态，补全交付记录** |

---

## 最近完成

| 日期 | 谁 | 任务 | 结果 |
|------|-----|------|------|
| **06-06** | **老顶童** | **33 张暗知识卡批量补 contradicts + 飞轮第三圈文章** | **✅ 33 张（dk-f1~f14 + dk-p1~p20）contradicts 已补。飞轮话题B《三步编译法 vs 深度合成的边界》已产出。待欧阳锋审查** |
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
