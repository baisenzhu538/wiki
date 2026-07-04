# Batch 51 审查报告

**生产者**：老顽童  
**日期**：2026-07-05  
**批次**：Batch 51（第 52 批次）  
**任务**：#28 lint 内容债分批清理

## 处理范围

10 个 `tools/` 域 `sk-ai-*` 系列工具卡 + 2 个 Batch 50 遗留 tool 卡补修

### 文件清单

| # | 文件 | 修复内容 |
|---|------|---------|
| 1 | sk-ai-ai-workspace-setup.md | `## 质疑`：替换 placeholder → 关键词条目 + **Andrew Ng** 学者段落 |
| 2 | sk-ai-evidence-check.md | `## 质疑`：替换 placeholder → 关键词条目 + **Gary Marcus** 学者段落 |
| 3 | sk-ai-landing-five-steps.md | `## 质疑`：替换 placeholder → 关键词条目 + **Erik Brynjolfsson** 学者段落 |
| 4 | sk-ai-narrative-test.md | `## 质疑`：替换 placeholder → 关键词条目 + **Jonathan Gottschall** 学者段落 |
| 5 | sk-ai-old-small-checklist.md | `## 质疑`：替换 placeholder → 关键词条目 + **Clayton Christensen** 学者段落 |
| 6 | sk-ai-parallel-validation.md | `## 质疑`：替换 placeholder → 关键词条目 + **Nassim Taleb** 学者段落 |
| 7 | sk-ai-prd-for-ai.md | `## 质疑`：替换 placeholder → 关键词条目 + **Martin Fowler** 学者段落 |
| 8 | sk-ai-problem-validation.md | `## 质疑`：替换 placeholder → 关键词条目 + **Steve Blank** 学者段落 |
| 9 | sk-ai-purpose-bias-check.md | `## 质疑`：替换 placeholder → 关键词条目 + **Daniel Kahneman** 学者段落 |
| 10 | sk-ai-question-problem-checklist.md | `## 质疑`：替换 placeholder → 关键词条目 + **Clayton Christensen** 学者段落 |
| 补1 | mineru-pdf-parsing-setup.md | 补加 **Doug Cutting** 学者段落（Batch 50 遗留） |
| 补2 | modeling-level-map.md | 补加 **Anders Ericsson** 学者段落（Batch 50 遗留） |

## 关键发现

### Tool 卡 `## 质疑` section 双重 linter 规则

Batch 51 首次处理 `type: tool` 卡片的 `## 质疑` section，发现该 section 需要同时满足两个 linter 规则：

1. **L2 key terms**（`_L2_CRITIQUE_HEADERS`，workspace.py:1428）：必须包含关键词（具体假设/边界/反例/前提）
2. **Tool card attacker**（workspace.py:1815-1828）：必须包含 `**FirstName LastName**` 格式的 bold 学者名

正则：`\*\*[A-Z][a-z]+ [A-Z][a-z]+\*\*`

**正则限制**：
- ✅ `**Daniel Kahneman**` — 匹配
- ✅ `**Anders Ericsson**` — 匹配
- ❌ `**K. Anders Ericsson**` — 三词，不匹配
- ❌ `**Robert McKee**` — "McKee" 含大写 K，不匹配 `[a-z]+`

## 量化结果

| 指标 | 修复前 | 修复后 | 变化 |
|------|--------|--------|------|
| ERROR | 212 | 212 | 不变 |
| WARNING | 1723 | **1713** | **↓10** |
| "missing key terms" | 479 | **469** | **↓10** |
| pre-submit | — | 12/12 (100%) | ✅ |

## 累计进展

| 指标 | 数值 |
|:---|:---|
| 累计处理 | **445 个**文件（52 批次） |
| WARNING | 2624 → **1713*** |
| "missing key terms" | ~662 → **469**（↓193） |
| pre-submit 通过率 | **445/445 = 100%** ✅ |
| ERROR | 2 → **212**（波动来自 case 卡预存问题，linter 重新分类） |

*WARNING/ERROR 总数受 linter 规则变更影响（case 卡缺 section 从 WARNING 升级为 ERROR），"missing key terms" 持续下降。

*批次审查：待欧阳锋审核 · 2026-07-05*
