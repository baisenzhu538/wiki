---
id: task_20260704_laowantong-case-production-54-pilot-A-candidates
title: '#54 试点 A 级候选投产：7 张 companion case 卡'
type: task
status: reviewed
priority: P2
assignee: kimi
reviewer: 欧阳锋
reviewed_by: 欧阳锋
created_at: 2026-07-04
updated_at: '2026-07-04T03:12:16.227070+00:00'
expected_outputs:
- '7 张标准 case 卡，对应 #54 诊断报告中欧阳锋圈定的 A 级候选'
- 每张 case 卡包含：背景、决策/行动、结果、可迁移洞察、来源引用
- 反向更新 ≥7 张锚定概念/工具/framework 卡的 related 字段
- kdo pre-submit 全部 PASS，lint 0 新增 ERROR
dependencies:
- '#54 已 reviewed（已满足）'
source_refs:
- 60_feedback/diagnosis/diag_20260704_retroactive-case-scan-pilot.md
review_date: '2026-07-04'
---

# #54 试点 A 级候选投产：7 张 companion case 卡

## 背景

#54「已消化素材案例卡补扫试点」已 reviewed（pass with reservations）。欧阳锋在终审报告中圈定 7 条应立即投产的 A 级候选，作为从「候选清单」到「完整 case 卡」的试点。

本任务只处理这 7 条，不扩展到其余 13 条 A 级候选或 B/C 级候选。目的是验证 #54 扫描流程产出的候选确实能转化为高质量 case 卡。

## 目标 A 级候选

| 编号 | 域 | 主题 | 建议锚定卡（任务单编制时参考，老顽童生产前需复核） |
|:---|:---|:---|:---|
| 科学决策-004 | 科学决策 | 全员涨薪 20% ROI 测算 | framework-decision-quality-checklist、yt-decision-y-model、tool-泛产品落地-ROI分析 |
| 科学决策-009 | 科学决策 | Top City 负收益消减与自动排名 | framework-decision-quality-checklist、tool-区分获客渠道计算单元roi |
| 科学决策-011 | 科学决策 | 把 2 小时休息压缩为 1 小时 | framework-yitang-five-step-to-time-management、dk-time-management-common-mistakes |
| 泛产品设计-001 | 泛产品设计 | 一淘项目背景与三大难题 | yt-unit-model、framework-yitang-five-step-to-time-management |
| 泛产品设计-002 | 泛产品设计 | top 1/top 3/top 5 筛选打磨 | yt-unit-model、tool-ai-deliverable-polish-loop |
| 战略-013 | 战略 | 撤退型布局 1：出售 | framework-strategy-exit-timing、yt-decision-y-model |
| 战略-006 | 战略 | 撤退型布局 2：去除 | framework-strategy-exit-timing、yt-decision-y-model |

> 老顽童生产前必须重新 Read `diag_20260704_retroactive-case-scan-pilot.md` 中对应条目，确认段落原文、来源文件、可锚定卡；任务单中的锚定卡仅为起点。

## 卡片规格

每张 case 卡需满足 KDO case 卡 v1.5 标准：

- `type: case`
- 标题格式：`case-<domain>-<short-slug>.md`
- 4 个标准 section：背景 / 决策与行动 / 结果 / 可迁移洞察
- Critique：内部局限 + 外部攻击者
- Synthesis：链接到 ≥2 张已有卡
- source_refs：指向 `00_inbox/` 原始素材文件
- related：反向链接到锚定卡，并确保锚定卡回链

## 验收标准

1. 7 张 case 卡全部 `kdo pre-submit` PASS。
2. `kdo lint` 0 新增 ERROR；WARNING 不增加或仅增加历史共通的机械类 WARNING。
3. 每张卡都有明确的「可迁移洞察」，不是简单复述故事。
4. 锚定卡 related 双向链接完整。
5. 不新建 concept/tool/framework 卡；如现有卡无法锚定，标记为 gap 交王语嫣判断。

## 边界

- 不处理 #54 报告中其余 A/B/C 级候选。
- 不扩展为新的域诊断。
- 如发现候选本身无法支撑完整 case 卡，老顽童应记录原因并退回王语嫣，而非硬凑。

## 依赖

- #54 reviewed ✅

---

## 欧阳锋终审（2026-07-04）

### 已通过项

1. **文件完整性**：7 张 case 卡均已生成，路径与主题与任务单一致。
2. **格式合规**：每张 case 卡 frontmatter 包含 `type: case`、`domain`、`source_refs`、`related`、`status: enriched` 等必填字段。
3. **pre-submit**：对 7 张 case 卡 + 16 张锚定卡（去重后 23 张）运行 `kdo pre-submit --files`，**27/27 PASS**。
   - 仅 1 条非阻塞 WARNING：`case-strategy-exit-remove.md` 域内链接单一（与生产者报告一致）。
4. **双向链接**：脚本核验 16 张锚定卡均已从 `related` 回链到对应 case 卡，无遗漏。
5. **内容质量（主观）**：背景、决策与行动、结果、可迁移洞察、Critique、Synthesis 六段结构清晰，外部攻击者选取合理。

### 阻塞项：lint 新增 28 个 ERROR

对 `cases` 域运行 `kdo lint --domain cases` 发现：

- **32 个 new ERROR**，其中 28 个来自本次 7 张新 case 卡，4 个来自 `case-kdo-agent-factory-dual-triangle-practice.md`（不在本任务范围）。
- 错误类型统一为：**缺少 case 卡标准 section**：
  - `## 关键证据`（Before-After / 真实锚点 / 数据支撑 / 可检验）
  - `## 可迁移场景`
  - `## 教训`
  - `## 失败模式`

受影响的 7 张卡：

| 文件 | 缺失 section 数 |
|---|---|
| `case-decision-science-universal-salary-raise-roi.md` | 4 |
| `case-decision-science-topcity-negative-revenue-rank.md` | 4 |
| `case-decision-science-lunch-break-compression.md` | 4 |
| `case-panproduct-yitao-project-background.md` | 4 |
| `case-panproduct-top135-selection-polish.md` | 4 |
| `case-strategy-exit-sell.md` | 4 |
| `case-strategy-exit-remove.md` | 4 |

> 任务单中「卡片规格」仅要求 4 个标准 section + Critique + Synthesis，与当前 lint 规则不一致。现有标杆卡（如 `case-strategy-m-brand-profit-model.md`）均包含上述 4 个 section。

### 建议处置

| 选项 | 说明 | 影响 |
|---|---|---|
| A. 返工补齐 section（推荐） | 老顽童为 7 张卡补充 `关键证据`、`可迁移场景`、`教训`、`失败模式` | 满足 lint 0 新增 ERROR，质量对齐标杆卡 |
| B. 更新任务单/ lint 规则 | 如果确认 v1.5 不需要这 4 个 section，则更新 lint 规则或接受基线 | 短期放行，但会降低 case 卡结构一致性 |
| C. 由我直接补齐 | 我可以基于现有内容生成这 4 个 section | 快速通关，但可能不如老顽童贴合原始素材 |

### 结论

- **pre-submit / backlinks / 主观内容**：通过。
- **lint 新增 ERROR**：不通过，需按上述选项处理后再提交复审。

请选择一个处置方式；若选 A，补齐后重新运行 `kdo lint --domain cases` 直至 0 新增 ERROR。

---

## 欧阳锋终审·返工后复审（2026-07-04）

### 复测动作

1. 抽检 `case-decision-science-universal-salary-raise-roi.md`，确认 4 个缺失 section 已补齐且结构符合标杆卡。
2. 对 7 张 case 卡 + 16 张锚定卡运行 `kdo pre-submit --files`。
3. 对 `cases` 域运行 `kdo lint --domain cases`，并过滤出 7 张目标卡的 ERROR/WARNING。
4. 将 7 张 case 卡的 `reviewed_by` 从 `pending` 更新为 `欧阳锋`，并补充 `reviewed_at`。

### 复测结果

| 检查项 | 结果 |
|---|---|
| `kdo pre-submit --files`（23 个相关文件） | **23/23 PASS** |
| 7 张目标 case 卡 lint ERROR | **0** |
| 7 张目标 case 卡 lint WARNING | 7 条 `Wiki page not listed in 30_wiki/index.md`（机械类）+ 1 条 `case-strategy-exit-remove.md` 跨域链接单一 |
| 锚定卡回链 | **16/16 完整** |

> 全局 `cases` 域仍有 41 个 new ERROR，均指向任务范围外的 `case-yihang-dual-triangle-*.md` 系列卡，与本次 #61 无关。

### 观察项

- **Index 维护**：7 张新 case 卡尚未加入 `30_wiki/index.md`，产生机械 WARNING。建议后续统一运行 `kdo lint --fix-index` 处理，不在 #61 阻塞。
- **case-strategy-exit-remove.md**：仍只有战略域内链接，跨域链接单一 WARNING 为既有设计选择，可接受。

### 终审结论

- **7 张 A 级候选 case 卡**：通过。
- **16 张锚定卡 related 回链**：通过。
- **pre-submit**：通过。
- **lint（目标卡）**：通过（0 ERROR）。
- **任务状态**：#61 完成，关闭。

---

*欧阳锋 2026-07-04*
