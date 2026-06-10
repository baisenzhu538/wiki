# 洪七公后续任务（临时）

> 临时任务：熟悉 KDO 新基础设施管线（OCR → enrich → validate 闭环）。
> 做完后回归多模态本职工作。

---

## ⚠️ LLM 已配好，不要再碰

LLM 环境（Kimi + DeepSeek）已由黄药师配置完成，`kdo llm-check` 已通过。
你不需要再做任何 LLM 配置。遇到 LLM 问题直接找黄药师。

## 已完成

- 136 张旧 OCR 卡 enrich 审计 → 全部已 enriched ✅
- 产品内核画布 + 十大典型指标 OCR → enrich 完成 ✅
- 纪浩五层结构图 + 参考案例图片 OCR → enrich 完成 ✅
- 清单体笔记两张图片 OCR → enrich 完成 ✅

## 🆕 机会预判图片 OCR → enrich（18 张）

素材位置：`00_inbox/`（`一堂-机会预判-*.png` 共 18 张）
优先级：明天开工最先做

终局光谱图（5 张）→ 案例图（8 张）→ 模型图（3 张）→ 其他（2 张）

每张图跑 PaddleOCR → `kdo enrich` → 结构化入库。完成后通知欧阳锋审查。
