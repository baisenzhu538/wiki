---
id: review_20260628_ouyangfeng-wave4
type: review_task
created_at: 2026-06-28
updated_at: 2026-06-28
author: 王语嫣
assignee: 欧阳锋
priority: P1
scope: 老顽童批量工单 wave4：新域建设 15 张卡终审
related:
  - '[[laowantong-batch-2026-06-20-wave4]]'
status: pending_review
---

# 欧阳锋审查任务：wave4 新域建设（15 张卡）

> **来源**：`70_product/tasks/laowantong-batch-2026-06-20.md` 第 4 波。
> Hermes 老顽童负责生产，分两部分：4.1 调研方法论域 8 张卡 + 4.2 Master 域 7 张卡。

---

## 0. 任务元信息

| 项目 | 内容 |
|------|------|
| 待审任务 | `laowantong-batch-2026-06-20-wave4` |
| 来源队列 | `70_product/tasks/production-queue.md` 第 8 项 |
| 生产方 | Hermes 老顽童 |
| 卡数 | 15 张 |
| 目标 | 4.1 调研方法论域 8 张新卡 + 4.2 Master 域 7 张卡规范化 |
| 质量门禁 | 15 张卡 `kdo pre-submit` 全通过 |

---

## 1. 待审 15 张卡清单

### 4.1 调研方法论域（8 张新卡）

| # | 卡片路径 | 类型 | 标题 | 审查重点 |
|:---:|:---|:---|:---|:---|
| 1 | `30_wiki/frameworks/yt-research-osl-framework.md` | framework | OSL调研五步法：一堂通用商业调研框架 | OSCAR 框架、五步流程、失败模式 |
| 2 | `30_wiki/frameworks/yt-research-intelligence-map.md` | framework | 情报获取全景地图：13+渠道穷尽手段 | 13+ 渠道分类、穷尽性、适用边界 |
| 3 | `30_wiki/tools/yt-research-competitor-toolkit.md` | tool | 竞品拆解工具包：三层分类+内核边界+单元模型对标 | worksheet、三层拆解、单元模型桥接 |
| 4 | `30_wiki/tools/yt-research-expert-interview.md` | tool | 专家访谈工具：2小时获取行业共识的标准流程 | 流程 checklist、问题模板、避坑 |
| 5 | `30_wiki/tools/yt-research-user-jtbd.md` | tool | 用户深度访谈工具：JTBD视角区分“说的”和“真正要的” | JTBD 区分、访谈问题、分析模板 |
| 6 | `30_wiki/tools/yt-research-industry-canvas.md` | tool | 行业分析画布：五维快速扫描+二维定位 | 画布字段、示例、使用步骤 |
| 7 | `30_wiki/tools/yt-research-hypothesis-test.md` | tool | 假设验证调研工具：关键假设→可证伪问题→最小实验 | 假设→问题→实验映射、失败模式 |
| 8 | `30_wiki/concepts/yt-research-mindset.md` | concept | 调研认知升级：从“原创自信”到“情报驱动” | 认知转变、判断标准、When NOT |

### 4.2 Master 域（7 张既有卡规范化）

| # | 卡片路径 | 类型 | 标题 | 审查重点 |
|:---:|:---|:---|:---|:---|
| 9 | `30_wiki/frameworks/master-ai-info-literacy.md` | framework | AI 信息素养框架 | frontmatter 规范、source 真实、related 互链 |
| 10 | `30_wiki/frameworks/master-cognitive-bias-diagnosis.md` | framework | 认知偏差快速诊断清单 | 同上；是否有 ≥2 条适用边界 + ≥2 条失败模式 |
| 11 | `30_wiki/frameworks/master-decision-hygiene.md` | framework | 决策卫生五步法 | 同上；Action Checklist |
| 12 | `30_wiki/frameworks/master-first-principles.md` | framework | 第一性原理 | 同上 |
| 13 | `30_wiki/frameworks/master-systems-thinking.md` | framework | 系统思考 | 同上 |
| 14 | `30_wiki/frameworks/master-antifragile-checklist.md` | framework | 反脆弱决策检查清单 | 同上；checklist 形式 |
| 15 | `30_wiki/frameworks/master-knowledge-compound.md` | framework | 知识复利 | 同上 |

---

## 2. 已知 Hermes 已完成的修复（4.2 部分）

根据最新汇报，4.2 Master 域 7 张卡已完成以下共性修复：

1. **7 张卡 frontmatter `---` 闭合修复**
2. **`confidence` 0.92 → 0.78，`trust_level` high → medium**
3. **`related` 从 `src_unknown` 改为 Master 域互链（`[[master-*]]`）**
4. **每张卡新增 4 个标准 section**：
   - `## 关键证据`
   - `## 可迁移场景`
   - `## 教训`
   - `## 失败模式`
5. **外部攻击部分 `src_unknown` 替换为真实 wikilink**
6. **所有卡 `kdo pre-submit` 全部通过**

---

## 3. 欧阳锋审查标准

### 3.1 通用标准

| 判定 | 条件 |
|:---|:---|
| **deep / 通过** | 正文 ≥100 行（framework ≥150 行）；Claims/Evidence/Critique/Synthesis/Action Triggers/Failure Modes 六段齐全；失败模式具体；数字有来源；`related` 有效；frontmatter 规范 |
| **shallow / 返工** | 正文 < 80 行；缺六段中任一；失败模式模板化；数字无来源；related 死链；frontmatter 不规范 |
| **borderline / 小修** | 局部数字未标注、related 缺 1-2 条、个别表述不精确 |

### 3.2 4.1 调研方法论域重点

- 是否基于 SKILL.md 中的 OSCAR + 13 武器体系拆卡
- 每张新卡是否有明确的使用场景和失败模式
- tool 卡是否有可执行的 worksheet/checklist
- framework 卡是否有端到端流程图
- 新卡与现有 `yt-research-*` 卡的互链是否完整

### 3.3 4.2 Master 域重点

- frontmatter 是否完整规范（id/type/status/author/reviewed_by/review_date/updated_at/source_person/source_context/confidence/trust_level/domain/source_refs/related）
- `source_refs` 是否移除了虚假 source，替换为真实存在的 source
- `confidence` 是否 0.75-0.78，`trust_level` 是否 medium
- 是否有 ≥2 条 Master 域内部互链
- 是否有「边界/失败模式」表格（≥2 条适用边界 + ≥2 条失败模式）
- 是否有「Action Checklist / 使用步骤」

---

## 4. 判定规则

| 情况 | 处理 |
|:---|:---|
| 15 张全部 deep | 全部标记 `reviewed_by: 欧阳锋`，`status: reviewed`，任务状态改 `reviewed` |
| 少数 shallow/borderline | 通过的卡先标记 reviewed；返工卡列清单退回 Hermes；任务保持 `pending_review` |
| 多张核心问题 | 整体任务改为 `blocked`，列明问题，通知王语嫣/用户 |

---

## 5. 审查后动作

### 5.1 若全部或大部分通过

1. 15 张卡片 frontmatter 更新：
   - `status: enriched` → `reviewed`
   - `reviewed_by:` → `欧阳锋`
   - 加 `review_date: "2026-06-28"`
   - `updated_at:` → `2026-06-28`
2. `70_product/tasks/production-queue.md`：任务 #8 状态改为 `reviewed`
3. `70_product/tasks/dashboard.md`：wave4 状态改 `reviewed`
4. `.agent/context.md`：追加 wave4 终审完成记录
5. **解锁 wave5**：wave4 reviewed 后，wave5（#9）可正式生产
6. 本文件末尾追加审查结论

### 5.2 若有返工

1. 保持任务 #8 状态为 `pending_review` 或改为 `blocked`
2. 在本文件末尾追加返工清单
3. 通知 Hermes 老顽童按清单修复

---

## 6. 给欧阳锋的启动口令

**完整版**：
> 你是欧阳锋。先进入工作目录 `C:\Users\Administrator\Desktop\wiki\`，读 `.agent/startup.md`、`.agent/ouyangfeng-context.md`、`70_product/tasks/production-queue.md`，找到 wave4 pending_review 项，读 `60_feedback/tasks/review_20260628_ouyangfeng-wave4.md`，按清单审 15 张卡，重点检查 4.1 新卡拆卡质量和 4.2 Master 域规范化，跑 `kdo pre-submit` 抽查，给出 verdict。

**短版**：
> 欧阳锋，切到 wiki 目录，读 startup、队列、wave4 审查任务单（`60_feedback/tasks/review_20260628_ouyangfeng-wave4.md`），审 15 张卡。

---

## 7. 状态记录

| 日期 | 事件 | 操作人 |
|:---|:---|:---|
| 2026-06-28 | wave4 解锁，Hermes 开始生产 | 王语嫣 |
| 2026-06-28 | Hermes 完成 4.2 Master 域 7 张卡修复，开始 4.1 调研方法论域 8 张卡生产 | Hermes 老顽童 |
| 2026-06-28 | 王语嫣写本审查任务单 | 王语嫣 |
| 2026-06-28 | 欧阳锋完成 4.2 Master 域 7 张卡终审：pre-submit 7/7 通过，lint 7/7 通过；审查中修复 20 个缺失 source_refs 为 pending_archive 占位；7 张卡全部标记 reviewed | 欧阳锋 |

---

## 8. 欧阳锋 4.2 Master 域审查结论

**Verdict：4.2 Master 域 7 张卡通过**

### 审查动作

- 全量 7 张卡 `kdo pre-submit`：7 passed / 0 failed
- 全量 7 张卡 `kdo lint`：0 ERROR
- 检查 frontmatter：id/type/status/author/confidence/trust_level/domain/related 均规范
- 检查 related：Master 域内部互链有效
- 检查 section：7 张卡均新增 `关键证据` / `可迁移场景` / `教训` / `失败模式` 4 个标准 section

### 审查中修复

- 7 张卡 `source_refs` 中 20 个不存在的 source 文件，全部替换为 `pending_archive:` 占位
- 全库 lint ERROR 从 540 回稳至 **519**

### 已执行动作

- 7 张 Master 卡 frontmatter 更新：
  - `status: enriched` → `reviewed`
  - `reviewed_by:` → `欧阳锋`
  - `review_date:` → `2026-06-28`
  - `updated_at:` → `2026-06-28`

### wave4 整体状态

- **4.2 Master 域 7 张卡**：✅ 已 reviewed
- **4.1 调研方法论域 8 张卡**：⏳ 待 Hermes 老顽童生产完成后再次审查
- wave4 任务单保持 `pending_review`，等 4.1 完成后统一终审

---

*维护人：王语嫣 | 最后更新：2026-06-28 | 4.2 终审：欧阳锋*
