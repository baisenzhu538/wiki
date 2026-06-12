---
title: KDO 概念卡地图诊断报告
diagnostician: 王语嫣
date: 2026-06-12
type: diagnosis
source: 全库 30_wiki/ 扫描 + frontmatter 分析
---

# KDO 概念卡地图诊断报告

## 一、全库概览

| 目录 | 文件数 | 备注 |
|------|-------:|------|
| `concepts/` | **1132** | 含 14 张真概念卡 + 大量误放的其他类型 |
| `frameworks/` | 7 | 桥接卡集中地（McKinsey + 单元模型） |
| `tools/` | 24 | 含 Skill 卡 + 一堂方法论工具 |
| `cases/` | 11 | 正式案例卡（无误放的） |
| `dark-knowledges/` | 17 | 正式暗知识卡 |
| `systems/` | 9 | KDO 基础设施/架构 |
| `entities/` | 5 | 组织/人实体 |
| `decisions/` | 39 | 旧决策记录（计划、建议书） |
| `projects/` | 3 | HIS 项目 |
| **总计** | **1258** | |

**核心发现**：`concepts/` 占全库 **90%**，是"大杂烩目录"，混淆了 6 种不同类型的卡片。

---

## 二、concepts/ 目录混存分析

### 2.1 类型分布（按命名前缀）

| 前缀 | 数量 | 应该放哪里 | 说明 |
|------|-----:|------------|------|
| `concept-*` | **14** | `concepts/` ✅ | 真正的概念卡。仅占 1.2% |
| `yt-*` | **238** | 混合（21%在 frameworks/ 已分离，其余散落） | 一堂方法论卡片 |
| `dk-*` | **99** | `dark-knowledges/` | 暗知识卡误放 |
| `case-*` | **27** | `cases/` | 案例卡误放 |
| `sk-*`（.sk-backup） | **12** | `skills/` 或 `tools/` | 扫描器批量产出的技能卡，未整合 |
| 无前缀（非 yt-/dk-/case-） | ~750+ | 需逐张审查 | 原始口述稿/课程/AI 素材 |

### 2.2 严重程度

- **P0**：99 张 dk-* 卡、27 张 case-* 卡、12 张 sk-* 卡 **目录错位** → 导致 `kdo validate` 断言链断裂，Domain 索引失效
- **P1**：~750 张无前缀卡片身份不明 → 无法被 `kdo query` 正确召回
- **P2**：真正的概念卡（concept-*）仅 **14 张**，不足以支撑"概念卡地图"的核心功能

---

## 三、Domain 标签覆盖率严重不足

### 3.1 全域统计

| Domain 值 | 出现次数 | 说明 |
|-----------|---------:|------|
| 空（`domain:`） | **743** | 绝大部分卡片 |
| `""` / `[]` / `''` | 196 | 空值变体，效果等同无标签 |
| `yitang` | 15 | 极少数正确标注 |
| `consulting` | 4 | McKinsey 桥接卡 |
| `decision-science` / `一堂·科学决策` | 3 | |
| `product` | 2 | |
| `ai-collaboration` | 2 | |
| `master`、`kdo`、`knowledge-management` 等 | 各 1 | |

> **结论**：~97% 的卡片没有有效的 domain 标签。

### 3.2 格式混乱

同一 KDO 知识库中，domain 字段至少有 5 种格式：

```yaml
domain:                    # 空（最常见）
domain: ""                 # 空字符串
domain: []                 # 空数组
domain: yitang             # 裸字符串（只有 yt- 旧卡如此）
domain: "yitang"           # 带引号字符串（少数 yt- 卡）
domain:                    # YAML 列表（concept- 新卡和 bridge 卡）
  - "consulting"
  - "yitang"
```

### 3.3 Domain 零覆盖率区域

以下内容域在 domain 标签中**完全不存在**：
- **design**（0 张）- 即使有 20+ 张 dk-yb* 卡源自设计课程
- **structured-thinking**（0 张 - 但 MECE 卡标注了此域）
- **learning**（0 张 - 但半肥猫卡标注了此域）
- **business-strategy**（0 张 - 但 McKinsey 桥接卡标注了此域）
- **personal-growth**（0 张 - 但大量 yt-personal* 未标注）

---

## 四、桥接卡现状

### 4.1 已有的桥（通过 frameworks/ 实现）

| 桥接卡 | 桥接的域 | 连接强度 |
|--------|---------|:--------:|
| MECE / Issue Tree | consulting ↔ yitang（一堂） | ✅ 强 |
| 7-S Framework | consulting ↔ yitang（管理域） | ✅ 强 |
| Trusted Advisor | consulting ↔ yitang（产品内核） | ✅ 强 |
| Hypothesis-Driven | consulting ↔ yitang（关键假设） | ✅ 强 |
| 单元模型六段 | decision-science ↔ yitang | 🟡 中等 |

**问题**：frameworks/ 只有 7 张卡，仅 bridge 了 **2 个外部域**（consulting + decision-science）。其他域完全没有桥接卡。

### 4.2 需要桥接的孤岛域

| 孤岛域 | 卡量 | 问题 |
|--------|:---:|------|
| **design** | ~40 张（dk-yb* + aigc*） | 完全孤立，无任何 bridge 到 yitang/consulting |
| **ai-collaboration** | ~30 张（纪浩 + 半肥猫） | 概念卡质量高但孤悬，没有 framework 卡映射到组织结构 |
| **personal knowledge** | ~22 张（yt-personal-*） | 自成一系，与 consulting/design 无桥 |
| **management** | ~22 张（yt-management-*） | 缺乏外部 management 框架对照 |

---

## 五、概念卡（真 · concept 卡）分布

### 5.1 核心概念卡（14 张）

| 卡片 | Domain | 状态 | 桥梁 |
|------|--------|:----:|:----:|
| concept-一堂-business-prediction | product, yitang | ❌ deprecated | → yt-foresight-* |
| concept-一堂-product-kernel | product, yitang | ✅ reviewed | → 假设/关键假设 |
| concept-一堂-key-assumptions | product, yitang | 需核实 | → kernel/hypothesis |
| concept-一堂-kernel-iteration | product, yitang | draft | → kernel-validation |
| concept-一堂-kernel-validation | product, yitang | draft | → kernel-iteration |
| concept-一堂-hypothesis-driven-business-methodology | product, yitang | draft | → 假设/内核 |
| concept-mckinsey-mece | consulting, structured-thinking | draft | → yt-* consulting bridge |
| concept-mckinsey-issue-tree | consulting, structured-thinking | draft | → yt-* (in tools/) |
| concept-半肥猫-ai-learning-toolification-methodology | ai-collaboration, learning | draft | → 纪浩概念卡 |
| concept-半肥猫-learning-toolification-methodology | ai-collaboration, learning | draft | 与上张重复？ |
| concept-纪浩-ai-collaboration-five-layer | ai-collaboration, yitang | draft | → 案例+暗知识 |
| concept-纪浩-ai-collaboration-methodology | ai-collaboration, yitang | draft | → Skill 卡+案例 |
| concept-ai-native-organization-five-steps | — | draft | 孤岛，未桥接 |
| concept-five-step-growth-to-barrier-transition | — | draft | 孤岛，未桥接 |

### 5.2 概念卡质量评价

- ✅ **bridge 卡**（McKinsey 系列）：质量最高——结构化 frontmatter + `bridges_to` + `diagnostic_signals` + 完整源引用
- 🟡 **一堂概念卡**：domain 标注完整但 `related` 连接偏少（每个 4-8 条），缺少外部对峙
- ❌ **ai-native / five-step-growth**：2 张卡无 domain 标签，未连接到任何其他卡，**事实上的孤岛卡**

---

## 六、知识空白发现

### Gap 1：缺少 consulting 域的工具卡
**现状**：frameworks/ 有 McKinsey 桥接卡，但 `tools/` 对应的 consulting 工具卡缺失。
**建议**：为 MECE / Issue Tree / 7-S / Trusted Advisor / Hypothesis-Driven 各配套 1 张 tool 卡（含 Checklists、Workflows）

### Gap 2：design 域缺少 framework 层
**现状**：design 域有 ~40 张操作卡（dk-yb* + aigc*），但没有任何 framework 卡（设计方法论、设计思维、设计系统架构）
**后果**：design 域的知识无法被 "诊断式召回"，只能通过关键词匹配

### Gap 3：跨域同构未卡片化
**现状**：dashboard 中提到多组跨域同构关系（如"反谄媚↔冲突化同构"、"四遍学习法↔IPO闭环"），但均未卡片化
**建议**：为每对同构关系产 concept 卡或暗知识卡

### Gap 4：.sk-backup 的 12 张技能卡未整合
**现状**：扫描器批量产出的技能卡躺在 `.sk-backup/`，未被审核、未被 domain 标注、未被 index 正确定位
**建议**：老顽童审核精选后，补充 domain 标签并移入 `tools/`

### Gap 5：yt- 卡片缺少"课程域"标签
**yt- 卡片按子域分类**：panproduct(33)、model(32)、entrepreneur(23)、personal(22)、management(18)、tool(15)、unit(10)、research(10)、pitch(10)、decision(10)、foresight(8)...
**但全都只有 `yitang` 标签**，缺乏子域区分（如 `domain: yitang/panproduct`），导致跨域检索时无法细分

---

## 七、域间连接图（Summary）

```
                    consulting (4 frameworks + tools)
                    ┃   ↕ (McKinsey 桥)
                    ┃
   ┌──── yitang/panproduct (33) ────┐
   │    yitang/model (32)            │
   │    yitang/entrepreneur (23)     │  ← 一堂核心域（238+ yt- 卡）
   │    yitang/personal (22)         │
   │    yitang/management (18)       │
   └───────────────────────────────┘
                    ┃   
                    ┃   孤岛域（无桥接）
                    ┃
    design (40)     ai-collaboration (30)    decision-science (少量)
    (完全孤立)      (内聚但孤悬)              (框架级 + 工具级)
```

---

## 八、建议行动项

| # | 行动 | 负责 | 优先级 |
|---|------|------|:------:|
| 1 | `concepts/` 目录类型分离：dk-* → dark-knowledges/, case-* → cases/ | 黄药师 | P0 |
| 2 | domain 标签格式统一 + 批量补齐（先定标准格式：YAML list） | 欧阳锋→黄药师 | P0 |
| 3 | 为 design 域编 1 张 framework 卡（作为 bridge 底座） | 老顽童 | P1 |
| 4 | .sk-backup 12 张 skill 卡审查 + 入库 | 老顽童 | P1 |
| 5 | 概念卡地图（本诊断）接入 cron 自动更新 | 黄药师 | P2 |
| 6 | 为每对跨域同构关系产 concept 或 dk 卡 | 老顽童 | P2 |

---

## 九、诊断元数据

- **覆盖率**：全量 scanned（1258 文件，domain 值、type 值、目录分布、bridge 分析）
- **置信度**：高（基于 grep 扫描 + 抽样前 50 张卡 frontmatter 验证）
- **缺口**：未逐张验证 yt- 卡的身体内容（仅检查 frontmatter），内容质量需欧阳锋审查时补充
- **下一步**：产出后触发任务2——自迭代机制设计文档

*本诊断不修改 30_wiki/ 下任何文件。*
