---
title: 任务仪表盘
updated: 2026-06-09
---

# 任务仪表盘

> **用法**：Agent 自己来看进度、领任务。批次全部完成后通知欧阳锋统一审查。
> **图例**：✅ 完成 · 🔨 进行中 · ⏳ 排队 · ⚠️ 阻塞 · 🟡 有条件 PASS

---

## 老顽童（Producer · 飞书 Hermes）

| # | 任务 | 状态 | 备注 |
|---|------|:--:|------|
| 1-16 | 5 月全部旧任务 | ✅ | 全部完成 |
| 17 | Phase 2.1：corrections.md 暗知识卡批产 | ✅ | 11 张 PASS。质量 A |
| 18 | Phase 2.2：failure-modes.md 暗知识卡批产 | ✅ | 14 张 dk-f*。欧阳锋审查 A |
| 19 | Phase 2.3：pitfalls.md 暗知识卡批产 | ✅ | 19 张 dk-p*。新版 18 张 A- |
| 20 | Phase 3：口述稿暗知识萃取（月白→Truman） | ⏳ | 30 张目标，首批 10 张已入库。暂停 |
| 21 | 写卡时标注 contradicts | ✅ | 33 张卡已补完 |
| **22** | **AI俱乐部四篇（纪浩/马易/半肥猫/水水）** | **🟡** | **纪浩 10 张卡已产出（🟡 P0 格式问题已由黄药师修复）。马易/半肥猫/水水 skill 卡为扫描器批量产出（~75 张），待老顽童审核精选** |
| **23** | **🆕 产品内核域处理（5篇素材）** | **🔜** | **黄药师已完成概念卡骨架×5 + 任务简报。待老顽童填内容** |
| **24** | **🆕 泛产品设计域卡片** | **🟡** | **case-truman-motivation-map + dk-truman-iteration-to-aesthetic-ceiling 已产出。质量 A。待欧阳锋审查** |

---

## 黄药师（Builder · Windows PowerShell）

| # | 任务 | 状态 |
|---|------|:--:|
| 1-20 | scaffold / validate / video CLI / infrastructure 等 | ✅ |
| Sprint 3-7 | produce 预填/数据卫生/Validate→Ship/video CLI | ✅ |
| Sprint 5b | 萃取器跑通全部月白口述稿 | 🟡 | 已产出候选 JSON。待确认后续 |
| Task A | 陈旧标记规则（`kdo stale`） | 🔜 | 已实现，待欧阳锋审查 |
| Task B | 增量传播机制（`kdo stale --propagate`） | ⏳ | Task A 完成后启动 |
| Task C | 技能点扫描器 | ✅ | **100 候选技能已输出。马易/半肥猫/水水/Truman 四批 skill 卡已批量产出** |
| **Task D** | **🆕 协助老顽童处理产品内核域素材** | **🔜** | **5 篇 Truman 产品内核课：实操/迭代/验证/关键假设/商业预判。预处理+扫描器+概念卡骨架** |

---

## 洪七公（Multimodal Arbiter · 飞书 Hermes）

| # | 任务 | 状态 | 备注 |
|---|------|:--:|------|
| 1-7 | 旧任务 | ✅ | 全部完成 |
| 8 | 科学决策域 VA 交叉审查 | ✅ | 35张图，通过率~71% |
| 9 | VA 前置 A1（🔴10张） | ✅ | A |
| 10 | 单元模型域 VA 前置（7张） | ✅ | A-。3处颜色违规待修 |
| 11 | 路演域 VA 补齐 | 🟡 | 有条件 PASS。ladder L207 1处颜色残留待修 |
| 12 | 清单体笔记图片 OCR 处理 | ✅ | 2 张图片 OCR → 结构化文本 |
| 13 | 产品内核 OCR → 结构化入库 | 🔜 | 内核画布+十大指标图片已有 OCR → kdo enrich |

---

## 段王爷（Publisher · 飞书 Hermes）

| # | 任务 | 状态 | 备注 |
|---|------|:--:|------|
| 1 | KDO 视频试点 ship | ⚠️ 待补记录 | final.mp4 已就绪 |
| 2 | 50_delivery/ 发布审计 | ✅ | delivery-registry 全面清洗：已交付 29→7（剔除22未通过validate+1重复），待交付 0→23（全部标注阻塞原因） |

---

## 最近完成

| 日期 | 谁 | 任务 | 结果 |
|------|-----|------|------|
| **06-09** | **老顽童** | **泛产品设计域 2 张卡** | **✅ A。case-truman-motivation-map + dk-truman-iteration-to-aesthetic-ceiling。三步编译法+多攻击者论证，结构扎实** |
| **06-09** | **段王爷** | **50_delivery/ 发布审计完成** | **✅ delivery-registry 清洗：29→7 已交付，23 待交付（18 validate未通过+2 draft+2 不存在+1 重复）。逐一标注阻塞原因** |
| **06-09** | **黄药师** | **老顽童纪浩批次审查 + P0修复** | **🟡 3 dk卡格式重修 + 3 case卡补章节 + index注册** |
| **06-09** | **老顽童** | **纪浩 AI俱乐部 10 张卡** | **🟡 4 case + 2 concept + 3 dk + 1 skill。内容有料，格式不合规（P0 已修）** |
| 06-07 | 黄药师 | 扫描器批量产出 skill 卡 | ✅ 马易 40 + 半肥猫 17 + 水水 19 + Truman ~25 = ~100 张 |
| 06-06 | 老顽童 | 33 张暗知识卡批量补 contradicts | ✅ dk-f1~f14 + dk-p1~p20 contradicts 已补 |
| 05-28 | 欧阳锋 | Design 域第一批编译 | ✅ PASS。3 张概念卡全流程完成 |
| 05-28 | 黄药师 | Sprint 5（Validate→Ship 闭环） | ✅ 全部 PASS。9/9 tests, 388 pytest |
