---
scope: C 域（domain 含 business-formula 或 id 含 business-formula）
auditor: 欧阳锋
date: 2026-07-12
status: 初审完成，待治理
---

# C 域整体质量审计报告

> 触发：用户要求对整体 C 域做质量审计。
> 口径：frontmatter `domain` 含 `business-formula` 或卡 id 含 `business-formula`。

---

## 一、卡池规模与成熟度

| 维度 | 数量 | 说明 |
|:---|---:|:---|
| C 域总卡数 | **61** | concepts 15 / frameworks 12 / tools 10 / cases 20 / systems 1 / dk 1 / domains 1 / tool-agent-spec 1 |
| `reviewed` | 4 | 仅占 6.6% |
| `enriched` | 51 | 占 83.6%，均未终审 |
| `pending_review` | 2 | 含 C 域总纲 `framework-一堂-业务公式拆解-总纲` |
| `draft` | 4 | 3 张桥接卡 + 1 张 agent-spec |

**核心风险**：C 域主体（51/61）停留在 `enriched`，未进入 `reviewed`。总纲卡本身还是 `pending_review`，意味着整个 C 域的顶层策展节点尚未终审。

---

## 二、机械门禁（L1）

### 2.1 pre-submit

- 全量 61 张 C 域卡 `kdo pre-submit`：**61/61 PASS**
- 说明：frontmatter schema、WIKILINK、DOMAIN、DK_SECTION 等格式层无阻塞项。

### 2.2 lint（`kdo lint --domain business-formula`）

| 类型 | 数量 | 占比 |
|:---|---:|:---|
| 新 ERROR | 220 | 主干问题 |
| 新 WARNING | 87 | 次要问题 |

**错误分类（Top）**：

| 问题类型 | 卡数 | 条数 | 说明 |
|:---|---:|---:|:---|
| `source_refs` 指向文件不存在 | 31 | 154 | 多引用 `00_inbox/Handle the business/Business formula/*.txt` 或 `_vlm_output/批注...` 文件，实际磁盘缺失 |
| Case 卡缺 section | 19 | 67 | 缺 `## 关键证据` 等结构化段落 |
| `source_refs possible typo` | 17 | 45 | 路径拼写/空格/后缀异常 |
| Tool 卡缺 section | ~10 | ~39 | 缺 Purpose / When NOT to Use / Critique / Protocol |
| 未入 index | 1 | 1 | `tool-一堂-业务公式-L1L6参数分层自检` |
| OCR 源图缺失 | 1 | 1 | `case-yitang-shipinhao-ads-l1-l6` 源图无 paddle_ocr.txt |

**重灾区卡片（source_refs dead files ≥6）**：

- `yt-business-formula-six-level-logic`（19 条）
- `business-formula-domain-digest`（10 条）
- `case-yitang-marathon-ten-seasons`（10 条）
- `framework-一堂-业务公式拆解-总纲`（9 条）
- `case-yitang-innovative-metrics-collection`（7 条）
- `case-yitang-panhonghai-entertainment`（7 条）
- `case-yitang-xingangwan-chess-room`（7 条）
- `concept-一堂-参数耦合与动态公式`（7 条）
- `concept-一堂-相关不等于因果`（7 条）

### 2.3 双基线口径差异

- `kdo_lint.py --incremental`（使用 `90_control/.lint_baseline.json`）：**0 new error**。
- `kdo lint --domain business-formula`（使用 `.kdo/baseline.json`）：**220 new error**。

**审计判断**：`.lint_baseline.json` 已把上述 source_refs dead / section missing 等错误吸收为基线，导致增量门禁对 C 域失盲。这是 #159 基线回卷必须解决的核心问题——基线不能成为真实债务的隐身衣。

---

## 三、图谱连通性

### 3.1 域内/全库出入度

| 指标 | 数量 | 卡片 |
|:---|---:|:---|
| C 域零出链 | 1 | `xingangwan-pharma-business-formulas` |
| 全库零出链 | 0 | — |
| C 域零入链 | 1 | `xingangwan-pharma-business-formulas` |
| 全库零入链 | 1 | `xingangwan-pharma-business-formulas` |

`xingangwan-pharma-business-formulas` 是 C 域唯一的**孤岛卡**（零出链、零入链）。它是 EC 线独立域卡片，但既然 domain 含 business-formula，在 C 域口径下就是孤岛，需裁定是否移出 C 域或补桥接。

### 3.2 related 死链（目标卡不存在）

仅 4 张卡存在 related 死链：

| 源卡 | 死链目标 |
|:---|:---|
| `yt-business-formula-business-pattern-selector` | `pending_unknown` |
| `yt-tool-business-formula-metrics-checklist` | `pending_unknown` |
| `business-formula-domain-digest` | `agent-一堂-业务公式教练`（spec 不在 30_wiki，可接受） |
| `business-formula-to-kdo-card-quality` | `kdo-input-channel-strategy-2026-06-16`、`kdo-15-dimension-label-spec`、`obsidian-kdo-内容产出工作流-产品设计大纲`、`kdo-priority-checklist` |

**结论**：related 死链不是 C 域主要问题；主要问题是 source_refs 死文件和 section 缺失。

---

## 四、Index 覆盖

- 未入 `30_wiki/index.md` / `30_wiki/links/index.md` 的 C 域卡：**5 张**
  - `framework-business-formula-dual-triangle-bridge`（draft）
  - `framework-business-formula-fundamentals-bridge`（draft）
  - `framework-business-formula-y-model-bridge`（draft）
  - `tool-agent-spec-business-formula-parameter-miner`（draft）
  - `tool-一堂-业务公式-L1L6参数分层自检`（pending_review）

前 4 张为 draft 桥接卡，可理解；最后 1 张 `tool-一堂-业务公式-L1L6参数分层自检` 已 pending_review 却未入 index，是漏登记。

---

## 五、综合裁定

### 5.1 不能入库的硬缺陷

1. **source_refs 死文件 154 条**：溯源链断裂，违反溯源铁律。
2. **19 张 case 卡缺关键 section**：案例卡骨架不完整。
3. **C 域总纲 `framework-一堂-业务公式拆解-总纲` 仍为 `pending_review`**：顶层节点未终审，整个 C 域不能视为完成。
4. **`tool-一堂-业务公式-L1L6参数分层自检` 未入 index**。

### 5.2 可接受的软问题

- `business-formula-domain-digest` → `agent-一堂-业务公式教练` 链接：spec 路径特殊，待 #159 索引覆盖 `.agent/prompts` 后自然解决。
- 4 张 draft 桥接卡未入 index：draft 状态可接受。
- `xingangwan-pharma-business-formulas` 孤岛：需裁定是否归属 C 域；若保留则补桥接，若移出则改 domain。

### 5.3 与 #159 的关联

C 域是 #159 基线回卷的最大受益者/受害者：
- 现有 `.lint_baseline.json` 把 154 条 source_refs dead + 67 条 section missing 等错误埋进基线，导致增量 lint 对 C 域「零新增」假象。
- #159 阶段 3 重建基线时，必须把这些真实错误暴露出来并分批清理，否则基线回卷等于掩耳盗铃。

---

## 六、返工清单（按优先级）

| # | 任务 | 负责人 | 验收口径 |
|---|:---|:---|:---|
| P0 | 修复 154 条 source_refs 死文件：确认文件是否被移动/重命名/未生成；能补则补，不能补则改为 `pending_unknown` 或 `pending_archive` | 老顽童 / 王语嫣 | `kdo lint --domain business-formula` source_refs dead 归零 |
| P0 | 补齐 19 张 case 卡缺失 section | 老顽童 | `kdo lint --domain business-formula` Case card missing section 归零 |
| P0 | 终审 C 域总纲 `framework-一堂-业务公式拆解-总纲` | 欧阳锋 | status → reviewed |
| P1 | 补齐 Tool 卡缺失的 Purpose/When NOT/Critique/Protocol section | 老顽童 | lint warning 中 Tool card missing section 归零 |
| P1 | `tool-一堂-业务公式-L1L6参数分层自检` 入 index | 老顽童 | grep 命中 index.md |
| P1 | 裁定 `xingangwan-pharma-business-formulas` 归属或补桥接 | 王语嫣 / 欧阳锋 | 要么改 domain 脱离 C 域，要么补 ≥1 条 C 域相关 related |
| P2 | 清理 `business-formula-to-kdo-card-quality` 的 4 条 kdo-* 死链 | 老顽童 | related 死链归零 |
| P2 | 51 张 `enriched` 卡按优先级分批终审 | 欧阳锋 | 建议先 framework/concept 总纲类，再 tool，再 case |

---

## 七、审计命令快照（可复现）

```bash
# C 域 lint 实态
kdo lint --domain business-formula --summary

# 全量 C 域 pre-submit（已通过）
# 由脚本批量调用：kdo pre-submit -f <61 文件路径>

# C 域卡池统计
python -c "import yaml,glob,re; ..." # 详见本次审计对话中的 Python 脚本

# 基线差异验证
python 90_control/scripts/kdo_lint.py 30_wiki --incremental
```

---

*欧阳锋 · 2026-07-12 · C 域整体质量审计*
