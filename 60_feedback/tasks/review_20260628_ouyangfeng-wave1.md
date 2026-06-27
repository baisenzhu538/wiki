---
id: review_20260628_ouyangfeng-wave1
type: review_task
created_at: 2026-06-28
updated_at: 2026-06-28
author: 王语嫣
assignee: 欧阳锋
priority: P0
scope: 老顽童批量工单 wave1：门禁快速清理 18 张卡终审
related:
  - '[[laowantong-batch-2026-06-20-wave1]]'
status: pending_review
---

# 欧阳锋审查任务：wave1 门禁快速清理（18 张卡）

> **用户/王语嫣转交欧阳锋时，请用这个文件。**
> 不要直接让欧阳锋去读 `laowantong-batch-2026-06-20.md` 全文，那个文件有 400+ 行，包含 waves 1-5 的全部规格。欧阳锋只需要审 wave1 的 18 张卡。

---

## 0. 任务元信息

| 项目 | 内容 |
|------|------|
| 待审任务 | `laowantong-batch-2026-06-20-wave1` |
| 来源队列 | `70_product/tasks/production-queue.md` 第 1 项 |
| 生产方 | Hermes 老顽童（1.1+1.2）+ WorkBuddy 老顽童（1.3+1.4+结构修复） |
| 卡数 | 18 张 |
| 目标 | 门禁快速清理：修复 frontmatter 字段、source_refs、trust_level、confidence、dark_knowledge_type、related 死链等机械问题 |
| 质量门禁 | 18 张卡 `kdo pre-submit` 全通过（18 passed / 0 failed） |

---

## 1. 待审 18 张卡清单

### 1.1 王欢域 dk 卡：source_refs + trust_level + dark_knowledge_type（4 张）

| # | 卡片路径 | 修复动作 | 审查重点 |
|:---:|:---|:---|:---|
| 1 | `30_wiki/dark-knowledges/dk-wanghuan-ai-lifts-personal-ceiling.md` | source_refs 改王欢素材；trust_level: high→medium；加 `dark_knowledge_type: insight` | source_refs 是否指向正确王欢素材；trust_level 是否 medium；dark_knowledge_type 是否存在 |
| 2 | `30_wiki/dark-knowledges/dk-wanghuan-creativity-in-description-and-taste.md` | 同上 | 同上 |
| 3 | `30_wiki/dark-knowledges/dk-wanghuan-output-equals-standard-times-iteration.md` | 同上 | 同上 |
| 4 | `30_wiki/dark-knowledges/dk-wanghuan-standard-by-iteration.md` | 同上 | 同上 |

### 1.2 王欢域 dk 卡：补 dark_knowledge_type + 时间格式（3 张）

| # | 卡片路径 | 修复动作 | 审查重点 |
|:---:|:---|:---|:---|
| 5 | `30_wiki/dark-knowledges/dk-wanghuan-magic-defeats-magic.md` | 加 `dark_knowledge_type: workflow` | dark_knowledge_type 是否正确 |
| 6 | `30_wiki/dark-knowledges/dk-wanghuan-spec-trap.md` | 加 `dark_knowledge_type: insight` | 同上 |
| 7 | `30_wiki/dark-knowledges/dk-wanghuan-paced-sales-decision.md` | 加 `dark_knowledge_type: insight`；时间格式从 ISO 精简为日期 | 时间格式是否正确；类型是否正确 |

### 1.3 yt-域 dangling 链接修复（3 张）

| # | 卡片路径 | 修复动作 | 审查重点 |
|:---:|:---|:---|:---|
| 8 | `30_wiki/concepts/yt-demand-b2b-vs-b2c.md` | 从 related 移除 `xujian-tob-fivestep-oral` | related 中是否还有 source 型链接 |
| 9 | `30_wiki/frameworks/yt-demand-decision-chain.md` | 从 related 移除 `xujian-tob-fivestep-oral` | 同上 |
| 10 | `30_wiki/concepts/yt-product-kernel-aesthetic.md` | `yt-model-pan-product-aesthetic-progression` → `yt-model-aesthetic-progression` | 链接是否已修正为指向存在的卡片 |

### 1.4 yt-域 confidence/trust 不匹配 + dark_knowledge_type（8 张）

| # | 卡片路径 | 修复动作 | 审查重点 |
|:---:|:---|:---|:---|
| 11 | `30_wiki/concepts/yt-demand-hierarchy-model.md` | trust_level: high→medium；confidence 0.92→0.78 | trust/confidence 是否对齐 |
| 12 | `30_wiki/concepts/yt-demand-user-segmentation.md` | 同上 | 同上 |
| 13 | `30_wiki/dark-knowledges/yt-demand-competitive-displacement.md` | 同上；加 `dark_knowledge_type: insight` | 同上；类型是否正确 |
| 14 | `30_wiki/dark-knowledges/yt-demand-fake-demand-detection.md` | 同上；加 `dark_knowledge_type: insight` | 同上 |
| 15 | `30_wiki/dark-knowledges/yt-demand-scope-creep.md` | 同上；加 `dark_knowledge_type: insight` | 同上 |
| 16 | `30_wiki/frameworks/yt-demand-early-validation.md` | 同上 | trust/confidence 是否对齐 |
| 17 | `30_wiki/frameworks/yt-demand-scenario-reconstruction.md` | 同上 | 同上 |
| 18 | `30_wiki/dark-knowledges/yt-demand-market-size-pitfalls.md` | 加 `dark_knowledge_type: insight`；confidence 对齐 0.78/medium | 类型是否正确；confidence/trust 是否对齐 |

---

## 2. 欧阳锋审查标准

本次 wave1 是**门禁快速清理**，不是深度返工。审查重点不是内容深度，而是：

1. **机械修复是否正确执行**
   - source_refs 是否指向真实存在的源文件
   - trust_level / confidence 是否按规则调整
   - `dark_knowledge_type` 是否对 dk 卡存在且值合理
   - related 中的 dangling link 是否已移除/修正
   - 时间格式是否统一为 `YYYY-MM-DD`

2. **是否引入新错误**
   - 跑 `kdo pre-submit -f <文件>` 抽查（建议至少抽 6 张，覆盖四类修复）
   - 跑 `kdo lint` 检查本轮目标卡是否无新增 ERROR

3. **内容完整性是否受损**
   - 修复 frontmatter 时是否误删正文
   - 调整 related 时是否误删有效连接

### 判定规则

| 情况 | 处理 |
|:---|:---|
| 机械修复正确、无新错误、内容完整 | **直接通过** |
| 个别卡 frontmatter 仍有小问题 | **退回老顽童返工**，在任务文件列明 |
| 多张卡内容被误删/改坏 | **整体退回 wave1**，状态改回 `claimed-workbuddy` 并说明 |
| 发现系统性问题（如 source_refs 指向错误素材） | **blocked**，通知王语嫣/用户 |

---

## 3. 审查后动作

### 3.1 若全部通过

1. 18 张卡片 frontmatter：
   - `status: enriched` → `reviewed`
   - `reviewed_by: pending` / 原值 → `欧阳锋`
   - 加 `review_date: "2026-06-28"`
2. `70_product/tasks/production-queue.md`：任务 #1 状态改为 `reviewed`
3. `70_product/tasks/dashboard.md`：该任务状态改 `reviewed`；Summary 中 `Queued` 减 1，`Review Done` 加 1
4. `.agent/context.md`：追加 wave1 终审完成记录
5. 本文件末尾追加审查结论

### 3.2 若有返工

1. 保持任务 #1 状态为 `pending_review` 或改为 `blocked`（视问题严重性）
2. 在本文件末尾追加返工清单
3. 通知老顽童（WorkBuddy）按清单修复

---

## 4. 给欧阳锋的启动口令

**完整版**：
> 你是欧阳锋。先进入工作目录 `C:\Users\Administrator\Desktop\wiki\`，读 `.agent/startup.md`、`.agent/ouyangfeng-context.md`、`70_product/tasks/production-queue.md`，找到 wave1（`laowantong-batch-2026-06-20-wave1`）pending_review 项，读 `60_feedback/tasks/review_20260628_ouyangfeng-wave1.md`，按清单审 18 张卡，跑 `kdo pre-submit` 抽查，给出 verdict。

**短版**：
> 欧阳锋，切到 wiki 目录，读 startup、队列、wave1 审查任务单（`60_feedback/tasks/review_20260628_ouyangfeng-wave1.md`），审 18 张卡。

---

## 5. 状态记录

| 日期 | 事件 | 操作人 |
|:---|:---|:---|
| 2026-06-27 | Hermes 完成 wave1 1.1+1.2 | Hermes 老顽童 |
| 2026-06-28 | WorkBuddy 完成 wave1 1.3+1.4+结构修复 | WorkBuddy 老顽童 |
| 2026-06-28 | 18 张卡 `kdo pre-submit` 全通过 | 老顽童 |
| 2026-06-28 | 王语嫣写本审查任务单 | 王语嫣 |
| 待填写 | 欧阳锋终审 | 欧阳锋 |

---

*维护人：王语嫣 | 最后更新：2026-06-28*
