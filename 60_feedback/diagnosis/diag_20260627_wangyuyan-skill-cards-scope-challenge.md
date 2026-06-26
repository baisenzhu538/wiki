---
id: diag_20260627_wangyuyan-skill-cards-scope-challenge
type: diagnosis_report
created_at: 2026-06-27
author: 王语嫣
scope: 老顽童提出的 483 张 skill 卡精修计划独立复核
confidence: 0.85
trust_level: high
related:
  - '[[framework-yitang-iterative-recursive-digging]]'
  - '[[framework-yitang-nine-layer-deep-dig]]'
---

# 王语嫣独立诊断：关于老顽童「483 张 skill 卡精修计划」的质疑与修正建议

> 老顽童汇报：483 张 skill 卡中 P1 级 380 张，建议按优先级精修。
> 王语嫣独立扫描后，发现数据口径、taxonomy 前提、前置条件均存在重大问题。
> **结论：当前不应批准 380 张批量精修，需先解决 taxonomy 归属 + 93 张 YAML 解析失败 + 精修范围重新定义。**

---

## 一、老顽童诊断 vs 王语嫣独立扫描结果对比

| 指标 | 老顽童汇报 | 王语嫣扫描（`90_control/scripts/check_skill_cards.py`） | 偏差 |
|:---|:---|:---|:---|
| skill-* 卡片总数 | 483 张 | **457 张** | -26 张（5.4%） |
| P1 需精修 | 380 张（78.7%） | draft 257 + needs-review 60 = **317 张** | -63 张 |
| 无 Constraints & Boundaries | 363 张 | **0 张**（所有卡都含 When NOT to Use / 边界 / 失败模式 / 不要用 等） | **完全相反** |
| 无 diagnostic_signals | 337 张 | **411 张无 DS**（有 DS 仅 46 张） | 方向一致但口径不同 |
| trust_level=low | 329 张 | **257 张 low** + 60 张 medium-low | -12 张 |
| status=draft | 328 张 | **257 张 draft** | -71 张 |
| reviewer=pending | 321 张 | **317 张 pending** | 基本一致 |
| A 级达标 | 34 张（7%） | **46 张接近 A 级**（6 项标准满足 ≥5） | 口径不同 |
| YAML 解析失败 | 未提及 | **93 张** | 重大遗漏 |
| enriched 但缺结构 | ~50 张 | **0 张**（因所有卡都有 C&B） | **完全相反** |
| 纯 draft 骨架 | ~330 张 | **0 张**（严格定义下） | **完全相反** |

**核心发现**：老顽童的统计口径与实际情况存在系统性偏差，尤其是「无 Constraints & Boundaries = 363 张」与王语嫣扫描结果（0 张）完全相反。

---

## 二、关键质疑：这些还是「skill 卡」吗？

### 2.1 历史决策

`wiki/.agent/context.md` 2026-06-18 里程碑明确记录：

> **470 skill 重分类为 tool/concept（欧阳锋 taxonomy 裁决执行）**

### 2.2 当前实际状态

王语嫣扫描结果：

| 文件前缀 | frontmatter type | 数量 |
|:---|:---|---:|
| `skill-*` | `tool` | **361 张** |
| `skill-*` | `concept` | 2 张 |
| `skill-*` | `missing` / 其他 | 1 张 |

**结论**：457 张 `skill-*.md` 文件中，**361 张（79%）已经在 frontmatter 中被欧阳锋 taxonomy 裁决为 `type: tool`**，只是文件名仍保留 `skill-` 前缀。

### 2.3 这意味着什么？

老顽童建议「精修 380 张 skill 卡」，但实质上：
- **79% 的卡片不是 skill，而是 tool**；
- 正确的操作不是「精修 skill 卡」，而是 **「将 type=tool 的 skill-* 文件重命名为 tool-*，并按 tool 卡标准补齐」**；
- 若按老顽童的方案批量精修，会强化「skill」这一错误分类，与欧阳锋 taxonomy 裁决冲突。

---

## 三、前置条件未满足

### 3.1 93 张 YAML 解析失败

在王语嫣扫描的 457 张 skill-* 文件中，**93 张（20.4%）YAML 解析失败**。例如：

- `skill-ai-four-elements-validation.md`：第 9 行 `domain:` 列表断裂，`yitangsource_person: 纪浩` 未换行。
- 大量 `skill-ban-fei-mao-*`、`skill-ai-*` 卡片 frontmatter 结构错误。

**风险**：若老顽童直接开始批量精修，这些 YAML 错误会导致 `kdo lint`、`kdo query`、索引重建全部失效。必须先修 YAML，再谈精修。

### 3.2 缺少精修标准

老顽童的「A 级」标准未明确：
- A 级需要满足哪些字段？（DS / C&B / related≥5 / status / reviewer / trust / source_refs？）
- 不同 type（tool vs concept）的 A 级标准是否不同？
- 精修后的卡片是否需要从 `skill-*` 重命名为 `tool-*`/`concept-*`？
- 精修优先级由谁确定？是否与王欢域、科学决策域、单元模型域等当前重点冲突？

---

## 四、王语嫣的修正建议

### 4.1 立即暂停 380 张批量精修计划

在以下问题未解决前，不应启动大规模精修：
1. taxonomy 归属未明确（skill vs tool vs concept）；
2. 93 张 YAML 错误未修复；
3. 精修标准、范围、优先级未与欧阳锋/用户确认；
4. 与当前 active_task（P0-A 封版、王欢 AI 2041、science 域等）的资源冲突未评估。

### 4.2 第一步：taxonomy 澄清（最高优先级）

请欧阳锋确认：
- 457 张 `skill-*.md` 中，type=tool 的 361 张是否应**重命名为 `tool-*`**？
- type=concept 的 2 张是否应重命名为 `concept-*`？
- 是否还有 genuinely 属于 `skill` type 的卡片？（当前看几乎没有）
- 重命名时如何处理 wikilink 引用？

### 4.3 第二步：修复 93 张 YAML 错误

由黄药师写脚本批量修复，或老顽童按批次处理。必须满足：
- 所有 `skill-*` / 重命名后的 `tool-*` 文件 `yaml.safe_load` 通过。

### 4.4 第三步：重新定义精修范围

 taxonomy 澄清 + YAML 修复后，再按以下优先级精修：

| 优先级 | 范围 | 理由 |
|:---|:---|:---|
| P0 | 46 张「接近 A 级」卡（多为 enriched + DS + C&B + reviewer=欧阳锋 + trust=medium） | 只差 related≥5 或 trust 微调，快速达标 |
| P1 | 已明确归属为 tool 且属于当前重点域（AI 协作、一堂、纪浩、B2B 等） | 与当前知识库建设重点一致 |
| P2 | 其他 tool/concept 卡 | 按域分批处理 |
| P3 | 需要合并/归档的重复/低价值卡 | 避免为无价值卡片浪费精修资源 |

### 4.5 第四步：建立精修标准与验收门禁

每张卡精修前必须明确：
- type（tool/concept/framework/dk）
- 该 type 的标准结构（framework 卡 vs tool 卡 vs concept 卡不同）
- 必须字段：id / type / status / author / reviewed_by / confidence / trust_level / source_refs / related≥5
- tool/framework/dk 必须含：操作步骤 / When NOT to Use / 失败模式
- case 卡必须含：关键数字 + 证据表
- 精修后必须跑 `yaml.safe_load` + broken link 检查

---

## 五、对老顽童诊断能力的评估

| 维度 | 评估 |
|:---|:---|
| 主动性 | 主动扫描并汇报问题，值得肯定 |
| 数据准确性 | **严重不足**，关键指标（C&B、enriched 缺结构、纯 draft 骨架）与事实相反 |
| taxonomy 意识 | 不足，未意识到 79% 的 skill 卡已被欧阳锋裁决为 tool |
| 风险识别 | 遗漏 93 张 YAML 错误这一重大前置风险 |
| 结论 | 不是「做不好」，是「没验准 + 没对齐 taxonomy + 没看全局」；与 P0-A 事件模式一致 |

---

## 六、建议用户 / 欧阳锋的决策

1. **否掉老顽童当前提出的 380 张 skill 卡精修方案**。
2. **先召开 taxonomy 澄清会**：确认 361 张 type=tool 的 skill-* 卡是否全部重命名为 tool-*。
3. **由黄药师先批量修复 93 张 YAML 错误**（或确认是否已修复）。
4. **重新定义精修范围后，再批准老顽童执行**。

---

## 七、关联文件

- 扫描脚本：`90_control/scripts/check_skill_cards.py`
- 历史决策：`wiki/.agent/context.md`（2026-06-18 里程碑：470 skill 重分类为 tool/concept）
- 错误模式库：`agent复盘/王语嫣/错误模式库.md`（E004：Producer 汇报完成但未通过客观验证）

---

*诊断人：王语嫣 | 日期：2026-06-27*
*状态：建议暂停当前方案，待 taxonomy + YAML 问题解决后再议*
