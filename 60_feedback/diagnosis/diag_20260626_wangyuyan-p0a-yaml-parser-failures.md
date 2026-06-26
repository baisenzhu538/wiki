---
id: diag_20260626_wangyuyan-p0a-yaml-parser-failures
type: diagnosis_report
created_at: 2026-06-26
author: 王语嫣
scope: P0-A 单元模型域 15 张卡 frontmatter YAML 解析检查
---

# P0-A 单元模型域 YAML 解析失败诊断（2026-06-26）

> 老顽童完成 4 项返工后，王语嫣对 P0-A 15 张卡做 YAML 全量扫描时发现新增 10 张解析失败。
> 本诊断仅写入 `60_feedback/`，不污染 `30_wiki/`。

---

## 一、问题概述

| 项目 | 数值 |
|:---|:---|
| 扫描范围 | P0-A 单元模型域 15 张卡 |
| YAML 解析通过 | 5 张 |
| YAML 解析失败 | 10 张 |
| broken link | 0 个 |
| 问题模式 | `related:` 字段列表缩进断裂 |

**结论**：P0-A 单元模型域**尚未达到封版标准**。YAML 解析失败会直接导致 `kdo lint`、`kdo query`、索引重建等后续工具失效，必须在封版前全部修复。

---

## 二、失败模式详解

### 2.1 共性模式

10 张卡的 frontmatter 中，`related:` 字段的列表被拆成两段：

```yaml
related:
  - '[[A]]'
  - '[[B]]'
- "[[C]]"
- "[[D]]"
```

前半段（`  -`）正确缩进在 `related:` 下；后半段（`-`）回到根级缩进，YAML 解析器将其视为「映射根级出现裸列表」，导致解析失败。

### 2.2 正确格式

```yaml
related:
  - '[[A]]'
  - '[[B]]'
  - "[[C]]"
  - "[[D]]"
```

所有列表项必须统一缩进在 `related:` 之下。

---

## 三、受影响的 10 张卡

| # | 卡片 ID | 类型 | 状态 |
|---|:---|:---|:---|
| 1 | `ai单元模型口述蒋老师` | concept | YAML 失败 |
| 2 | `concept-单元模型-学练用` | concept | YAML 失败 |
| 3 | `dk-单元模型-找全成本实操难点` | dk | YAML 失败 |
| 4 | `dk-单元模型-找单元模型实操难点` | dk | YAML 失败 |
| 5 | `dk-单元模型-找基准值实操难点` | dk | YAML 失败 |
| 6 | `dk-单元模型-规模对抗实操难点` | dk | YAML 失败 |
| 7 | `framework-单元模型-外部对抗地图` | framework | YAML 失败 |
| 8 | `yt-unit-model-ladder` | framework | YAML 失败 |
| 9 | `tool-单元模型-单城市` | tool | YAML 失败 |
| 10 | `tool-单元模型-壁垒预判` | tool | YAML 失败 |

---

## 四、根因分析

1. **老顽童批量生成 frontmatter 时模板不一致**：部分 `related` 项被工具以不同缩进层级写入。
2. **验收脚本未把 YAML 解析作为前置门禁**：此前只检查了 broken link 和字段存在性，未强制要求 `yaml.safe_load` 通过。
3. **`yt-unit-model-overview` 的修复未触发同批次全量 YAML 扫描**：06-26 修复该卡时，未意识到同一批次其他卡可能存在同类问题。

---

## 五、处理建议

1. **老顽童对 10 张卡统一修复 `related` 缩进**（任务见 `task_20260626_hermes-laowantong-p0a-yaml-fix.md`）。
2. **修复后必须逐个用 `yaml.safe_load` 验证**，不通过不提交。
3. **王语嫣复核时把 YAML 解析设为第一门禁**，然后再检查 broken link 和内容结构。
4. **建议黄药师在 `kdo lint` 或自动门禁中把 frontmatter YAML 解析失败设为 FATAL**，避免此类问题流入仓库。

---

## 六、关联文件

- 原验收报告：`60_feedback/audit/audit_20260626_wangyuyan-p0a-unit-model-cards.md`
- 原返工任务：`60_feedback/tasks/task_20260626_hermes-laowantong-p0a-fix.md`
- 新增 YAML 修复任务：`60_feedback/tasks/task_20260626_hermes-laowantong-p0a-yaml-fix.md`
- 致欧阳锋备忘：`60_feedback/audit/audit_20260626_wangyuyan-p0a-rework-memo-for-ouyangfeng.md`

---

*诊断人：王语嫣 | 日期：2026-06-26*
