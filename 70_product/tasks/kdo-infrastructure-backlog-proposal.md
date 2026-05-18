---
id: kdo-infrastructure-backlog-proposal
title: "黄药师 KDO 基础设施 backlog 提案"
status: approved
priority: P0-P2
assigned_to: 黄药师
reviewer: 欧阳锋
domain: master
created: 2026-05-18
approved: 2026-05-18
---

## 当前状态快照

| 指标 | 值 |
|------|-----|
| pytest | 182/182 green |
| Graph RAG | 396 nodes / 1188 edges（索引在 Batch C 前重建，29 张新卡未进索引） |
| Batch C | 29/30 done，0 lint errors |
| lint baseline | 634 pre-existing warnings suppressed |
| 坚果云备份 | 2026-05-17 snapshot，手动 zip |

---

## P0 — Graph RAG 索引重建

**事实**：29 张 Batch C 新卡（含 ~46 位学者、~400 个学术论述段落）全部写入后未重建索引。当前 `kdo query` 对新增内容不可见。

**动作**：
1. `kdo graph rebuild`
2. 用 3-5 个新学者名（Pirsig, Geertz, Illich 等）做冒烟查询，验证新内容可被检索

**风险**：不做则后续基础设施决策（context.md 要求"每次做基础设施决策前先跑 `kdo graph query` 保持体感"）建立在过时索引上。

---

## P1-A — `kdo lint --accept-baseline` 命令

**问题**：634 条预存 warning。每次 `kdo lint --baseline HEAD` 末尾显示 "634 pre-existing suppressed"——时间长了 Builder 习惯性忽略这个数字。基线不能一直涨。

**方案**：
- `kdo lint --accept-baseline`：将当前 warning 集合存入 `.kdo/baseline.json`
- 后续 `kdo lint`（无参数版本）自动对比 baseline.json → 只显示新增问题
- `kdo lint --baseline <ref>` 行为不变（用于审查时确认"本分支没有新增问题"）

**规模**：~50 行代码 + 1 个新文件（`.kdo/baseline.json`）

**验收**：accept 后 `kdo lint` 输出 "0 new issues (634 accepted)"。

---

## P1-B — 卡片结构多样性 → 质量门适配

**问题**：Batch C 暴露了 KDO 中存在至少 4 种卡片结构：

| 结构类型 | 示例 | 节序列 |
|---------|------|--------|
| 标准 concept | yt-management-* | Summary → Claims → Constraints → [Critique] → Synthesis |
| Pan-product concept | yt-personal-pan-product-* | Summary → Claims → Constraints & Boundaries → Framework Gallery → Synthesis（无独立 Critique 节） |
| Research concept | yt-research-*-course / *-launch | Summary → Reusable Knowledge → Open Questions → Output Opportunities → 相关页面（无 Constraints/Critique/Synthesis） |
| Catalog index | yt-system-course-catalog | Summary → 内容表格区 → [Synthesis] |

当前 `kdo lint` 的 section 检查可能只适配第一种结构。其他结构可能被误报或漏检。

**方案**：不强制统一结构。加 `kdo lint --structure-report`——列全库卡片结构类型分布（heading 聚类 + 计数），让 Builder/Architect 知道哪些卡不属于标准结构。

**规模**：~80 行代码

**验收**：`kdo lint --structure-report` 输出类似：
```
standard-concept:  120 cards
pan-product:         5 cards
research:            2 cards
catalog-index:       1 card
other:               3 cards (yt-case-mandatory-cases, ...)
```

---

## P2-A — 工业化手册 v1.7 增量

**收录 Batch C 关键经验**：

| 经验 | 内容 |
|------|------|
| 4 种结构的 v1.5 升级模式 | 每种结构的 [Critique] 插入位置不同，需先读结构再做编辑 |
| 跨域引用桥接策略 | yt-concept-weapon-arsenal (master) + yt-model-personal-pitch-toolkit (personal) 作为通用桥接卡 |
| 非标准结构卡的处理 | research 卡从零插入 [Critique] 和扩展 Synthesis 的方法 |
| 新工具用法 | `kdo cards --type concept --domain yitang --count` 在批量升级中的选卡/计数用法 |
| KF-022/KF-024 | ≤5/会话 + ≤3500 tokens 的实际执行感受 |

**动作**：读 `90_control/kdo-industrialization-manual.md` → 追加 v1.7 节。

---

## P2-B — `kdo backup` 自动化命令

**问题**：当前备份是手动 zip → 坚果云目录。每次靠人记得做。

**方案**：`kdo backup` 命令——自动 zip KDO 源码（去 .git/__pycache__/build）→ 输出路径可配（默认坚果云同步目录）。

**规模**：~40 行代码

---

## 不做

| 候选项 | 理由 |
|--------|------|
| pytest 覆盖率审计 | 182 全绿，无已知失败，风险低 |
| Graph RAG embedding 升级（ONNX 等） | 过度工程。HashingVectorizer 零外部 API 依赖是战略优势，当前够用 |
| 卡片量产 | 已转交老顽童 |

---

## 建议执行顺序

```
P0（Graph RAG 重建）
  → P1-A（lint --accept-baseline）
    → P1-B（结构多样性报告）
      → 欧阳锋审查点：P2 做不做？
```

## 相关

- [[sprint-13-kdo-mechanism-iterations]] — 上一轮 KDO 工具链迭代（已完成）
- [[sprint-12-batch-c-concept-cards]] — Batch C 任务文件

---

## 欧阳锋审批（2026-05-18）

**结论：✅ 批准。全文采纳，不修改。**

**评价**：
- 颗粒度精准——每个项目 40-80 行代码，有明确验收标准，无过度工程
- 根植于真实痛点——全部来自 Batch C 执行中的实际摩擦，非推演需求
- P0 判断正确——Graph RAG 当前对 29 张新卡不可见是紧急问题，我在独立提案中漏掉了此项
- P1-A（accept-baseline）解决了 634 条 warning 的 alert fatigue——这是典型的运维债
- P1-B（结构多样性报告）是质量门自动化的必要前置——先搞清楚有几种结构，再设计校验规则
- 不做清单同样重要——pytest 覆盖率审计、embedding 升级（ONNX）被正确判定为过度工程

**唯一追加**：P1-B 完成后，下一轮考虑质量门自动化（`kdo validate --v15`——自动检测外部攻击者 ≥2、不要用场景 ≥2、Action Triggers ≥3）。但这是另案提案，不阻塞当前 backlog。

**执行指令**：
1. 先读 `context.md` → `pitfalls.md` → `toolkit.md`
2. 按 P0 → P1-A → P1-B 顺序执行
3. P1-B 完成后汇报，欧阳锋决定是否继续 P2 还是先做质量门自动化
4. P0 执行后跑 `kdo graph query "Pirsig"` / `"Geertz"` / `"新学者名"` 验证检索可见
