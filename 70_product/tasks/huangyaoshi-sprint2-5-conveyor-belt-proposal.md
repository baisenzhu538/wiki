---
title: "黄药师下阶段工单提案：补传送带（Sprint 2-5）"
author: "黄药师"
priority: "P1"
created_at: "2026-05-24"
status: "proposal"
reviewer: "欧阳锋"
depends_on: ["task-20260524-huangyaoshi-ai-study-dogfood.md"]
---

# 黄药师下阶段工单提案：补传送带（Sprint 2-5）

## 背景

2026-05-24 完成了AI学习域dogfood任务，完整跑通 capture→ingest→enrich→produce→validate 管线。核心发现：

> **工位齐全但工位之间没有传送带。每个半成品都要人手搬运。**

过去一年建设重心是"建工位"（9个管线阶段全有CLI命令，379 tests pass）。下一阶段重心应转向"连工位"——让数据在工位之间自动流动。

核心原则：**先闭环再自动化。** 不建全自动流水线，先让手动路径丝滑，再逐步放权。

## 当前管线成熟度

| 阶段 | 自动化 | 最大痛点 |
|------|--------|---------|
| capture | 手动 | 无批量，无连接器 |
| ingest | 半自动(watch) | ASR标题失效，无预标注 |
| enrich | 半自动(watch) | 正则模式几乎无用 |
| route | 手动 | 与produce无衔接 |
| **produce** | **手动** | **只生成TODO模板，不读wiki** |
| **validate** | **半自动** | **三源分裂（已修regex bug）** |
| ship | 手动 | 只记元数据，不发布 |
| feedback | 手动 | 无聚合 |
| improve | 手动 | 无闭环 |

**关键洞察**：前半段(capture→enrich)有watch串联。后半段(produce→ship)完全断开——恰恰是内容产出最后一公里。

## 已完成（Sprint 1-2）

| 任务 | 影响 |
|------|------|
| `section_content` regex修复 (`^##`→`^##\s`) | 解锁所有文章word count验证 |
| `kdo ingest --title --kind` 参数 | ASR稿可预标注标题和类型 |
| OCR失败fallback建议 | MinerU失败时提示用PaddleOCR |
| ingest确认打印 | 每条输出wiki路径+标题，立即可验 |
| `import sys` 遗漏修复 | 潜在运行时crash |

## 待审批（Sprint 3-5）

### Sprint 3: 传送带2 — Produce预填（~6h，最高ROI）

| # | 任务 | 复杂度 | 为什么重要 |
|---|------|--------|-----------|
| 7 | produce读wiki卡片→预填Body Structure | 中 | 当前produce=touch模板，100%手写 |
| 8 | produce自动填Source Lineage表 | 低 | 纯搬运，不该让人做 |
| 9 | produce后自动跑validate --advisory | 低 | 提前暴露问题，不等写完才发现 |
| 10 | validate以文件frontmatter为source of truth | 中 | 消除三源分裂根因 |
| 11 | artifact-registry.yaml降级为可选导出 | 中 | 减少冗余维护 |

**ROI论证**：如果老顽童要日产5篇文章，Sprint 3能把每篇的"搬运元数据"时间从30min降到0。

### Sprint 4: 数据卫生批修（~2h）

| # | 任务 | 来源 | 复杂度 |
|---|------|------|--------|
| 12 | ~113个broken wikilinks修复 | next-tasks Task 21 | 低(脚本) |
| 13 | ~271张卡缺失frontmatter补全 | Task 22 | 低(脚本) |
| 14 | ~166张卡老旧/新格式统一 | Task 23 | 低(脚本) |

**依赖**：Sprint 3的frontmatter变更逻辑(#10)应在Sprint 4批修前完成，否则批修后又要重做。

### Sprint 5: 传送带3 — Validate→Ship闭环（~4h）

| # | 任务 | 复杂度 | 为什么重要 |
|---|------|--------|-----------|
| 15 | 统一gate.py和validate为一套检查 | 高 | 当前两套系统重叠但不统一 |
| 16 | validate通过后自动更新artifact status→"ready" | 低 | 当前需手动改 |
| 17 | `kdo ship --dry-run` 预演模式 | 低 | 发布前看到会执行什么 |

### 未排期（需讨论）

| 主题 | 复杂度 | 决策点 |
|------|--------|--------|
| clean-transcript会话式规则 | 高 | 纯正则够吗？需要LLM分段？ |
| 多模态视觉理解管线 | 高 | 洪七公职责？还是黄药师建基础设施？ |
| 端到端pipeline编排 | 高 | Sprint 2-5完成后再议 |
| state.json数据保留策略 | 中 | 规模增长后再议 |

## 成功标准

Sprint 3完成后重做dogfood同等任务：
- ingest：0个垃圾标题
- produce：Body Structure + Source Lineage自动填好
- validate：直接通过，无需手动sync state.json
- 人工干预从"每步搬运"降到"只写Draft正文+审核"

## 风险

1. **Sprint 3 #10（validate读frontmatter）可能有连锁影响**——当前所有validation逻辑都假设数据来自state.json。改变数据源需要仔细审计所有调用路径。
2. **Sprint 4批修要遵守C-10铁律**——单卡dry-run→单卡write→validator验证→人审核→THEN批量。不能因为"只是脚本"就跳过。
3. **Sprint 5统一gate系统是架构重构**——两套系统合并需要先理清各自的检查项，确认无遗漏再合并。

## 我的建议

**Sprint 3先做，Sprint 4次之，Sprint 5再议。** Sprint 3是老顽童产能瓶颈的直接解锁；Sprint 4是技术债清理（不紧急但越早越好）；Sprint 5涉及架构决策，等Sprint 3体验沉淀后再定方案更稳妥。
