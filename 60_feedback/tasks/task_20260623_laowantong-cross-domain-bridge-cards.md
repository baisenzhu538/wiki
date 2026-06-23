# 老顽童任务指令：跨域桥接卡与枢纽 related 补全（王语嫣）

> 王语嫣铁律：本指令仅写入 `60_feedback/`，不污染 `30_wiki/`。老顽童负责按此指令在 `30_wiki/` 生产/修补卡片。
> 来源：已批准的跨域融合计划（策略 A）——`plans/jade-batgirl-kate-bishop.md`

---

## 0. 元信息

| 项目 | 内容 |
|------|------|
| 任务来源 | 跨域融合计划（战略 · 精益 · 决策 · AI 协作桥接体系） |
| 计划文件 | `plans/jade-batgirl-kate-bishop.md` |
| 设计稿 | `60_feedback/audit/cross-domain-bridge-design-specs.md` |
| 反馈日期 | 2026-06-23 |
| 质量负责人 | 王语嫣（CLI） |
| 生产方 | 老顽童 |

---

## 1. 任务目标

在不合并、不稀释现有域-specific 卡片的前提下，建立战略、精益、五步法、决策、AI 协作、需求分析之间的**桥接体系**：

- 生产 **5 张跨域 framework 桥接卡**；
- 补全 **10 张枢纽卡**的跨域 `related` 链接；
- 产出 **2 张跨域综合案例卡**；
- 所有新卡和修改后的卡通过王语嫣 9 层深挖 + 六层交叉验证标准。

---

## 2. 必须生产的 5 张桥接卡

| 优先级 | id | 标题 | 来源设计稿章节 |
|:------:|:---|:---|:---|
| P0 | `framework-strategy-lean-validation` | 战略假设的精益验证流程 | §2 |
| P0 | `framework-five-step-lean-interface` | 五步法与精益验证的接口 | §3 |
| P1 | `framework-lean-pivot-decision` | 精益验证结果如何触发战略/产品 pivot | §4 |
| P1 | `framework-ai-accelerated-strategy-cycle` | AI 加速的战略-验证闭环 | §5 |
| P2 | `framework-demand-lean-bridge` | 需求判断与精益验证的衔接 | §6 |

### 2.1 桥接卡通用要求

1. **一句话定义**：卡最开头用 1 句话说明解决什么问题。
2. **触发问题**：列出 2-3 个用户会在什么情况下查这张卡。
3. **端到端流程图**：用表格或 Mermaid 展示 A 域 → 桥接点 → B 域。
4. **调用清单**：明确引用哪些具体卡（通过 `related` 实现）。
5. **失败模式**：至少 3 个桥接常见错误。
6. **可信度标注**：引用原卡外的断言必须 `[conf=X, source=...]`。
7. **不重复原卡内容**：只讲接口，不讲原卡内部细节。
8. **related ≥ 5**：且必须覆盖 ≥2 个不同域的卡或 digest。

### 2.2 单卡特殊要求

#### `framework-strategy-lean-validation`
- 必须包含：战略假设类型 → 待验证问题 → 精益工具 → 通过/不通过标准 的对照表；
- 必须引用：`framework-strategy-brm`、`framework-lean-false-model`、`framework-lean-abcd-model`、`yt-entrepreneur-key-hypotheses`。

#### `framework-five-step-lean-interface`
- 必须包含：五步法每一步 → 待验证假设 → 精益工具 → 通过标准 的对照表；
- 必须引用：`yt-five-step-method`、`framework-lean-false-model`、`concept-一堂-kernel-validation`。

#### `framework-lean-pivot-decision`
- 必须包含：实验结果 → 对战略假设的影响 → 建议动作（pivot/persevere/kill）→ 决策检查清单 的矩阵；
- 必须引用：`framework-lean-false-model`、`yt-decision-y-model`、`framework-strategy-brm`。

#### `framework-ai-accelerated-strategy-cycle`
- 必须包含：AI 在战略分析阶段、精益验证阶段、战略迭代阶段的人机分工表；
- 必须引用：`framework-multi-agent-research-architecture`、`framework-wanghuan-harness-seven-stages`、`framework-lean-false-model`、`framework-strategy-brm`。

#### `framework-demand-lean-bridge`
- 必须包含：冰山 L1-L6 每一层 → 典型假设 → 验证工具 → 通过标准 的对照表；
- 必须引用：`framework-demand-iceberg`、`tool-demand-iceberg-l1-user` ~ `tool-demand-iceberg-l6-hypothesis`、`framework-lean-false-model`。

---

## 3. 必须补全 related 的 10 张枢纽卡

| 卡 id | 必须新增的 related | 当前上限控制 |
|:---|:---|:---|
| `framework-strategy-brm` | `framework-strategy-lean-validation`、`yt-decision-y-model` | 总 related 5-7 |
| `framework-strategy-six-stages` | `framework-lean-pivot-decision` | 总 related 5-7 |
| `framework-strategy-business-design` | `framework-five-step-lean-interface` | 总 related 5-7 |
| `framework-lean-false-model` | `framework-strategy-lean-validation`、`framework-five-step-lean-interface` | 总 related 5-7 |
| `framework-lean-abcd-model` | `yt-entrepreneur-key-hypotheses`、`framework-strategy-lean-validation` | 总 related 5-7 |
| `framework-lean-systematic-test-curve` | `framework-ai-accelerated-strategy-cycle` | 总 related 5-7 |
| `yt-five-step-method` | `framework-five-step-lean-interface`、`framework-strategy-lean-validation` | 总 related 5-7 |
| `yt-entrepreneur-five-step-method` | `framework-lean-false-model` | 总 related 5-7 |
| `framework-multi-agent-research-architecture` | `framework-ai-accelerated-strategy-cycle` | 总 related 5-7 |
| `framework-wanghuan-harness-seven-stages` | `framework-five-step-lean-interface` | 总 related 5-7 |

### 3.1 related 编辑原则
- 新增链接必须双向：如果 A 卡 related 到 B 卡，B 卡也应 related 回 A 卡；
- 若当前 related 数量超过 7 个，删除同域低价值链接，保留跨域链接；
- 修改后必须跑 `kdo lint` 检查孤立链接。

---

## 4. 必须生产的 2 张跨域综合案例卡

| 优先级 | id | 素材 | 必须覆盖的域 |
|:------:|:---|:---|:---|
| P1 | `case-cross-yuanqi-forest` | 元气森林（战略定位 + 精益试错 + 增长放大） | 战略、精益、增长 |
| P1 | `case-cross-xingangwan-pharma` | 鑫港湾智慧药柜（战略选择 + 商业模式验证 + 合规假设验证） | 战略、五步法、精益、决策 |

### 4.1 跨域案例通用要求

1. **一句话洞察**：必须同时引用 ≥2 个域的方法论。
2. **按时间线叙述**：战略选择 → 关键假设 → 验证动作 → 结果 → 决策/迭代。
3. **方法论标签**：在文中明确标注每一步用了哪个域的哪张卡（如 `[[framework-lean-false-model]]`）。
4. **失败/转折分析**：至少 1 个差点走错的方向，以及如何用另一域的方法纠正。

---

## 5. Frontmatter 规范

### 5.1 桥接卡

```yaml
---
id: framework-strategy-lean-validation
title: 战略假设的精益验证流程
type: framework
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.85
trust_level: high
language: zh-CN
domain:
- strategy
- lean-startup
- yitang
source_refs:
- 00_inbox/战略专题/冉鹏战略课逐字稿_ocr.md
- 00_inbox/精益创业/transcript_低成本验证认知篇.md
- 60_feedback/audit/cross-domain-bridge-design-specs.md
related:
- "[[framework-strategy-brm]]"
- "[[framework-lean-false-model]]"
- "[[framework-lean-abcd-model]]"
- "[[yt-entrepreneur-key-hypotheses]]"
- "[[yt-decision-y-model]]"
- "[[five-step-domain-digest]]"
- "[[lean-startup-domain-digest]]"
---
```

### 5.2 跨域案例卡

```yaml
---
id: case-cross-yuanqi-forest
title: 元气森林：战略定位与精益试错的跨域闭环
type: case
status: enriched
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.80
trust_level: medium
language: zh-CN
domain:
- strategy
- lean-startup
source_refs:
- 00_inbox/精益创业/元气森林-试错工具箱.png
- 00_inbox/战略专题/冉鹏战略课逐字稿_ocr.md
related:
- "[[framework-strategy-lean-validation]]"
- "[[framework-lean-false-model]]"
- "[[framework-lean-tenx-formula]]"
- "[[strategy-domain-digest]]"
- "[[lean-startup-domain-digest]]"
---
```

---

## 6. 执行批次

### 第一批：P0（优先完成）
1. 生产 `framework-strategy-lean-validation`
2. 生产 `framework-five-step-lean-interface`
3. 补全 10 张枢纽卡的 related
4. 通知王语嫣验收

### 第二批：P1
5. 生产 `framework-lean-pivot-decision`
6. 生产 `framework-ai-accelerated-strategy-cycle`
7. 生产 `case-cross-yuanqi-forest`
8. 生产 `case-cross-xingangwan-pharma`
9. 通知王语嫣验收

### 第三批：P2
10. 生产 `framework-demand-lean-bridge`
11. 通知王语嫣验收

---

## 7. 验收标准

王语嫣/欧阳锋验收时检查：
1. 5 张桥接卡是否全部存在，id/title/type 正确；
2. 桥接卡是否满足「一句话定义 + 触发问题 + 端到端流程 + 失败模式 + related ≥5 跨 ≥2 域」；
3. 桥接卡是否不重复原卡内容，只讲接口；
4. 10 张枢纽卡是否按要求补充了跨域 related，且双向链接成立；
5. 2 张跨域案例卡是否同时展示 ≥2 个域的方法论应用；
6. 所有新卡和修改卡的 YAML 是否通过 `kdo lint`；
7. 是否出现新的孤立 `related` 链接；
8. 是否严格遵守“王语嫣写 feedback，老顽童写 `30_wiki/`”的边界。

---

## 8. 特别注意

1. **不要合并现有卡片**：本任务只新增桥接卡和补 related，不修改现有卡片的 id、标题、核心模型。
2. **不要越界到黄药师任务**：跨域审计脚本由 `task_20260623_huangyaoshi-cross-domain-audit-script.md` 负责，老顽童不需要写脚本。
3. **每批完成后通知验收**：不要等全部 5 张桥接卡 + 2 案例 + 10 related 全部完成后再提交。
4. **遇到卡 ID 冲突先停**：如果某张桥接卡 id 已被占用，立即通知王语嫣，不要自行改名。

---

*质量负责人：王语嫣 | 生成时间：2026-06-23*
