# 老顽童整改任务：王欢《AI 2041》全 22 张卡 frontmatter 标准化（王语嫣）

> 王语嫣铁律：本指令仅写入 `60_feedback/`，不污染 `30_wiki/`。老顽童负责按此指令在 `30_wiki/` 修改卡片。
> 触发来源：P2 批次验收为「有条件通过」，发现 2 个系统性 schema 问题在 P1 已提出但未修复、P2 重复出现。
> 前置验收报告：`60_feedback/audit/ai2041-p2-production-audit-20260625.md`

---

## 0. 元信息

| 项目 | 内容 |
|------|------|
| 任务类型 | 整改 / correction |
| 反馈日期 | 2026-06-25 |
| 质量负责人 | 王语嫣（CLI） |
| 生产方 | 老顽童 |
| 优先级 | P0（阻塞 AI 2041 域正式收工与后续 synthesis dk 卡生产） |
| 预计工作量 | 22 张卡 frontmatter 批量修改，约 10–15 分钟 |

---

## 1. 必须整改的 2 类问题

### 1.1 `confidence` 字段必须是单一数值，不能是范围字符串

**问题描述**：多张卡片 frontmatter 中写成：

```yaml
confidence: 0.75-0.85
```

这会破坏 YAML schema / lint 校验，导致后续自动化处理失败。

**整改方式**：改为单一数值。

| 卡片类型 | 建议取值 |
|:---|:---:|
| concept / dk | `0.78` |
| tool | `0.80` |
| case | `0.80` |

如果某张卡确实需要表达区间，在正文新增一段「可信度说明」解释即可，frontmatter 只保留单一数值。

### 1.2 `source_person` / `source_context` 必须从 frontmatter 移除

**问题描述**：case 卡和 dk 卡 frontmatter 中使用了自定义字段：

```yaml
source_person: 王欢
source_context: ...
```

这两个字段未纳入通用 schema，会导致 schema 漂移。

**整改方式**：

- 从 frontmatter 中**删除**这两个字段。
- 正文已有「来源人与来源语境」节的，保留正文内容。
- 正文没有的，将 frontmatter 中的内容迁移到正文「来源人与来源语境」节。

---

## 2. 涉及卡片清单（22 张）

### 2.1 P0 5 张

| 卡片 | confidence 是否范围 | source_person/source_context 是否自定义 |
|:---|:---:|:---:|
| `framework-ai2041-critical-reading-os` | 否 | 否 |
| `framework-ai-deconstruction-methodology` | 否 | 否 |
| `tool-ai-critical-reading-three-layers` | 否 | 否 |
| `concept-ai-amara-law-business-judgment` | 否 | 否 |
| `tool-tech-probability-80-filter` | 否 | 否 |

### 2.2 P1 9 张

| 卡片 | confidence 是否范围 | source_person/source_context 是否自定义 |
|:---|:---:|:---:|
| `concept-ai-chair-determines-view` | **是** | 否 |
| `concept-ai-neutrality-bias` | **是** | 否 |
| `tool-ai-cross-reading-method` | **是** | 否 |
| `tool-ai2041-source-verification-checklist` | **是** | 否 |
| `case-compas-racial-bias` | **是** | **是** |
| `case-apple-card-gender-bias` | **是** | **是** |
| `case-dutch-childcare-scandal` | 待自查 | 待自查 |
| `case-cambridge-novelists-survey` | 待自查 | 待自查 |
| `case-chen-qiufan-ai-writing` | 待自查 | 待自查 |

### 2.3 P2 8 张

| 卡片 | confidence 是否范围 | source_person/source_context 是否自定义 |
|:---|:---:|:---:|
| `dk-ai-prediction-expiry-date` | 否 | **是** |
| `dk-ai-social-progress-not-automatic` | **是** | **是** |
| `dk-ai-scarcest-resource-is-self` | 否 | **是** |
| `concept-ai-information-quality-ladder` | **是** | 否 |
| `case-deepfake-market-misuse` | **是** | **是** |
| `case-ai-companion-emotional` | **是** | **是** |
| `case-roblox-ai-npc-education` | **是** | **是** |
| `case-ai-job-displacement-wef` | **是** | **是** |

> 老顽童应全量扫描 22 张卡，不仅限于上表标记为“是”的卡片。

---

## 3. 整改自查清单

每修改一张卡后勾选：

- [ ] `confidence` 为单一数值（如 `0.78` / `0.80`）
- [ ] 不存在 `source_person` 字段，或已迁移到正文「来源人与来源语境」节
- [ ] 不存在 `source_context` 字段，或已迁移到正文「来源人与来源语境」节
- [ ] frontmatter 仍能被标准 YAML 解析
- [ ] `id` / `title` / `type` / `status` / `author` / `reviewed_by` / `source_refs` / `related` 未被误删
- [ ] 正文内容未因迁移而重复或丢失

---

## 4. 验收方式

老顽童完成全部 22 张卡整改后：

1. 在 `60_feedback/corrections/` 下新建一条简短确认（或回复本任务文件路径）。
2. 王语嫣随机抽查 2 张卡，确认无范围字符串、无自定义 frontmatter 字段。
3. 抽查通过后，将 P2 验收报告 verdict 从「有条件通过」更新为「通过 ✅」。

---

## 5. 整改完成后的下一任务

整改通过即视为王欢《AI 2041》域 22 张卡正式收工。下一任务：

> `60_feedback/tasks/task_20260625_laowantong-synthesis-dk-cards.md`

生产 strategy / research / yitang 三域跨案例 synthesis dk 卡 9 张。

---

*任务下达：王语嫣 | 日期：2026-06-25*
