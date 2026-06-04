---
title: "黄药师：电子工程域 KDO 化建议（对齐讨论稿）"
type: improvement-plan
status: draft
domain:
  - electronics
  - master
created_at: 2026-06-05
author: 黄药师
target_reviewer: 欧阳锋 + 用户
source_refs:
  - 欧阳锋对电子资料归档整理及学习迭代的建议书
  - electronics-practice/ (5 文件)
  - embedded-debugging-retrospective-20260604
  - kdo-lessons-from-codex-debug-20260604
wiki_refs:
  - P-21 诊断优先原则
  - embedded-ir-debugging playbook
---

# 黄药师：电子工程域 KDO 化建议

> ⚠️ 对齐阶段讨论稿，非定稿。供欧阳锋和用户一起看。

---

## 一、现状：欧阳锋已有的东西

| 文件 | 位置 | 性质 | 评价 |
|:-----|:-----|:-----|:-----|
| project-standards.md | `90_control/electronics-practice/` | 三条规则（文件三分类、版本锁、收网） | ✅ 执行规则，放这里对 |
| failure-modes-electronics.md | `90_control/electronics-practice/` | 4 条 E-FM | ⚠️ 应该是知识卡片，不是规则文档 |
| diagnostic-firmware-skills.md | `90_control/electronics-practice/` | 三阶段诊断法 | ⚠️ 应该是 playbook，不是规则 |
| archive-plan-top-level-design.md | `90_control/electronics-practice/` | 8 阶段处理架构 | ✅ 给 AI Agent 的执行规范，放这里对 |
| archive-prompt-system-design.md | `90_control/electronics-practice/` | 三套提示词模板 | ✅ 给提示词使用者的指南，放这里对 |

**核心问题**：5 个文件全部放在 `90_control/`（控制层），没有一个在 `30_wiki/`（知识层）或 `40_outputs/`（能力层）。这意味着 `kdo query "红外对射 电平转换"` 搜不到 E-FM-001 和诊断套路。

---

## 二、核心原则：KDO 的边界

我坚持一个判断：

```
KDO 管「关于硬件项目的知识」，不管硬件项目本身。

   ✅ KDO 管这些                     ❌ KDO 不管这些
   ─────────────────────────         ──────────────────
   失败模式卡（dk-ef-*）              原理图 .sch/.SchDoc
   调试 playbook                     PCB .pcb/.PcbDoc
   器件对比 checklist                 BOM .xlsx/.csv
   项目元数据卡（存指针）              固件 .hex/.bin
   retrospective → 方法论提炼         示波器截图
   版本锁表的结构化存储                 Gerber 文件
```

理由：原理图和 PCB 是二进制/闭源格式，KDO 的 capture→ingest→enrich 管线对它们完全无效。硬塞进去只会产出一堆"标题是文件名的空壳卡"——C-8 的硬件版。

**欧阳锋的 archive-plan 就是"不管硬件文件本身"的方案——我完全同意这个方向。**

---

## 三、具体建议：分层迁移

### 建议 1：失败模式 → dk 卡（立即做）

**现状**：E-FM-001 ~ 004 在 `90_control/electronics-practice/failure-modes-electronics.md`，是一个 markdown 文件里的 4 个表格。

**改法**：每条拆成独立 dk 卡，放入 `30_wiki/concepts/`：

```
30_wiki/concepts/
  dk-ef-001-sn74lvc2g07-open-drain.md     ← 从 E-FM-001 迁移
  dk-ef-002-bom-version-async.md          ← 从 E-FM-002 迁移
  dk-ef-003-hand-soldering-bom-divergence.md ← 从 E-FM-003 迁移
  dk-ef-004-missing-diagnostic-firmware.md   ← 从 E-FM-004 迁移
```

- 前缀 `dk-ef-*`（dk = dark knowledge, ef = electronics failure）——纳入 dk 暗知识体系，老顽童的暗知识卡 SOP 可以直接复用
- frontmatter 新增 `dark_knowledge_type: hardware-failure`
- 每条保留 E-FM 编号作为溯源
- 原文的 `90_control/` 文件保留，但改为"索引页"——只列条目和链接，正文在 dk 卡里

**收益**：`kdo query "电平转换 开漏输出"` 能命中。stale --propagate 可以传播依赖。老顽童可以用暗知识卡 SOP 持续生产。

---

### 建议 2：诊断套路 → playbook（立即做）

**现状**：`diagnostic-firmware-skills.md` 已经是 playbook 的内容形态（三阶段 + 速查表）。

**改法**：直接 link 到已有的 `40_outputs/capabilities/playbooks/embedded-ir-debugging.md`。诊断版固件套路的内容本质上就是那个 playbook 的补充。

不需要新建文件——在现有 playbook 里加一节"欧阳锋的三阶段诊断法"，引用 `diagnostic-firmware-skills.md` 作为 source。

**收益**：避免两份内容分叉维护。

---

### 建议 3：项目元数据卡模板（短期）

**问题**：广冷项目归档在 `00_inbox/广冷电子/_archive/`，但没有一张 KDO 卡告诉 kdo query "广冷项目踩过什么坑、用了什么器件、版本锁表在哪"。

**建议**：新建一张项目元数据卡：

```yaml
---
id: proj-hx-smj-infrared-gate
title: "广冷电子 HX-SMJ 红外光栅板"
type: project
domain: electronics
status: completed
project_status: 批量投产
version_lock:
  baseline: B2.1
  schematic: V2.0
  pcb: V2.0
  bom: V2.0
  firmware: V2.1
file_pointers:
  archive: "00_inbox/广冷电子/_archive/"
  readme: "00_inbox/广冷电子/_archive/README.md"
  retrospective: "00_inbox/广冷电子/_archive/07_logs/"
related_dk_cards:
  - dk-ef-001
  - dk-ef-002
  - dk-ef-004
related_playbooks:
  - embedded-ir-debugging
created_at: 2026-06-05
---
```

**收益**：`kdo query "广冷 红外"` 直接命中，返回版本锁表 + 关联的失败模式 + playbook。下一个红外项目启动时，搜一下就能拿到全套上下文。

---

### 建议 4：retrospective → dk 自动管线（中期）

**触发**：每个硬件项目收网时，retrospective.md 已经写好了。

**自动化步骤**：
1. `kdo capture retrospective.md --kind hardware-retrospective`
2. LLM 提取新的失败模式 → 生成 dk-ef 卡骨架
3. LLM 提取新的调试技巧 → 追加到对应 playbook
4. 更新项目元数据卡的 `related_dk_cards`

这不是全自动——每次产出的骨架需要人审核——但可以把"从复盘到卡片"的 80% 体力活自动化。

---

### 建议 5：失败模式库的定期合并提醒（中期）

**问题**：随着项目积累，`dk-ef-005`, `dk-ef-006`...会越来越多。同类型的失败模式（比如三条都和"电平转换"有关）需要合并。

**机制**：利用已有的 `kdo stale` 扩展——给 dk-ef 卡加 `review_interval_review` 字段（不是 stale 检查，是合并检查）。每季度自动跑：

```
kdo electronics --merge-check

  以下失败模式可能重复（相似度 > 80%）：
    dk-ef-001 (SN74LVC2G07 开漏) ↔ dk-ef-00X (TXS0108 边沿)
    → 建议人工审查是否合并
```

不自动合并——合并需要工程判断——但提醒可以自动化。

---

## 四、和欧阳锋现有设计的对齐

| 欧阳锋的文件 | 黄药师的建议 | 共识/分歧 |
|:------------|:------------|:---------|
| project-standards.md | 留在 90_control，不动 | ✅ 共识 |
| failure-modes-electronics.md | 拆成 dk-ef-* 卡，原文降级为索引 | ⚠️ 需讨论 |
| diagnostic-firmware-skills.md | link 到已有 playbook，不建新文件 | ⚠️ 需讨论 |
| archive-plan-top-level-design.md | 留在 90_control，不碰 | ✅ 共识 |
| archive-prompt-system-design.md | 留在 90_control，不碰 | ✅ 共识 |
| （新）项目元数据卡 | 新建 proj-* 类型 | 🆕 黄药师提案 |
| （新）retrospective→dk 管线 | capture --kind hardware-retrospective | 🆕 黄药师提案 |
| （新）合并提醒 | stale 扩展 | 🆕 黄药师提案 |

---

## 五、不建议做的事

1. **不给原理图/PCB/BOM 建 KDO 卡片**——KDO 的文本管线对二进制文件无效，建了也是空壳
2. **不自动解析工程文件提取版本号**——格式碎片化（Altium / KiCad / Eagle / 立创EDA），投入产出不成比例。版本锁表是人写的，KDO 只存储和校验
3. **不把 archive-plan 的 8 阶段做成 kdo 命令**——那是 AI Agent 的执行规范，做成 kdo CLI 命令过度工程了

---

## 六、如果只能做一件事

**先把 E-FM-001~004 拆成 dk-ef 卡。** 这是 ROI 最高的一步——改动最小、立即让 `kdo query` 能检索电子工程失败模式、后续所有自动化都基于这个基础。

---

*黄药师 · 2026-06-05 · 对齐讨论稿*
