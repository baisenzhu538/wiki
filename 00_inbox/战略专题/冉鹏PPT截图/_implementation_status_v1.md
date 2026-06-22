# 冉鹏战略课 PPT 卡片化实现进度（v1）

> 王语嫣（CLI）分期分批实现进度追踪
> 时间：2026-06-22

---

## 已完成卡片清单

### 第 1 批：业务设计六要素 tool 卡（5 张）

| 文件 | 标题 | 来源 PPT |
|--|--|--|
| `30_wiki/tools/tool-strategy-value-proposition.md` | 价值主张设计工具：三问 + 六维排序法 | _107, _110, _112 |
| `30_wiki/tools/tool-strategy-value-capture.md` | 价值获取设计工具：8 问盈利模型 | _115, _117 |
| `30_wiki/tools/tool-strategy-activity-scope.md` | 活动范围设计工具：What × How × Where 三问 | _119, _121 |
| `30_wiki/tools/tool-strategy-control-points.md` | 战略控制点设计工具：价值定位模型 | _124 |
| `30_wiki/tools/tool-strategy-risk-management.md` | 业务设计风险管理工具：ISO31000 × Grace LaConte | _127, _129, _131 |

### 第 2 批：核心分析框架卡（5 张）

| 文件 | 标题 | 来源 PPT |
|--|--|--|
| `30_wiki/frameworks/framework-strategy-pyramid.md` | 企业战略金字塔 | _20, _21 |
| `30_wiki/frameworks/framework-strategy-blm.md` | IBM BLM + 华为五看三定 | _34, _35, _97 |
| `30_wiki/frameworks/framework-strategy-five-forces.md` | 波特五力分析框架 | _74 |
| `30_wiki/frameworks/framework-strategy-ansoff.md` | 安索夫矩阵 | _91 |
| `30_wiki/frameworks/framework-strategy-three-horizons.md` | 三个地平线 | _246 |

### 第 3 批：分析工具卡（5 张）

| 文件 | 标题 | 来源 PPT |
|--|--|--|
| `30_wiki/tools/tool-strategy-fishbone.md` | 鱼骨图根因分析工具 | _42, _44, _48 |
| `30_wiki/tools/tool-strategy-ksf.md` | 关键成功因素（KSF）分析工具 | _82, _84, _85 |
| `30_wiki/tools/tool-strategy-core-competence-matrix.md` | 核心能力评估矩阵 | _145 |
| `30_wiki/tools/tool-strategy-swot.md` | SWOT 分析工具 | _87 |
| `30_wiki/tools/tool-strategy-lifecycle.md` | 企业生命周期战略 | _26 |

### 第 4 批：补充框架 + 待确认（1 张完成）

| 文件 | 标题 | 来源 PPT | 状态 |
|--|--|--|--|
| `30_wiki/frameworks/framework-strategy-mckinsey-7s.md` | 麦肯锡 7S 模型 | _128, _203 | ✅ 已完成 |
| `framework-strategy-blue-ocean` | 蓝海战略四步动作框架 | 未定位 | ❌ 待确认 |
| `framework-strategy-kainar` | 凯纳创新框架 | 未找到 | ❌ 待确认 |

---

## 待确认事项

### 1. 凯纳创新框架

- **检索结果**：在 299 张 PPT 的 OCR 文本中未找到“凯纳”“横切”“纵切”“侧切”等关键词。
- **可能情况**：
  1. 存在于其他文件（视频、另外的 PDF）。
  2. 名称记忆有误（如“跨界创新”“水平/垂直/侧向扩展”）。
  3. 课程中未实际涉及。
- **建议**：欧阳锋/用户确认是否继续寻找，或从本次任务中移除。

### 2. 蓝海战略四步动作框架

- **检索结果**：仅 _59 提到“红海”，未找到“蓝海”“剔除”“减少”“增加”“创造”“价值曲线”等关键词。
- **可能情况**：
  1. 冉鹏课程中仅提及红海/蓝海概念，未深入四步动作框架。
  2. 关键词出现在 VLM parse error 文件中（未修复前无法检索）。
- **建议**：待 parser 修复后重新检索；若仍未找到，则按“概念提及”处理，不单独建 framework 卡。

### 3. Parser 修复

- **状态**：已交由黄药师（Claude Code）主导。
- **王语嫣贡献**：
  - 写了 `repair-vlm-parse-errors.py`（不调用 API，修复已有 113 张 parse error 文件）。
  - 在脚本中实现了状态机式内部引号修复函数，可作为黄药师修复 `describe-images-minimax.py` 的参考。
- **下一步**：等黄药师修复完成后，重新运行检索和审计。

---

## 建议下一批工作（第 5 批）

### 案例卡（高价值）

| 候选卡 | 来源 PPT | 价值 |
|--|--|--|
| `case-strategy-wc-pyramid` | _21 | W&C 战略金字塔对比 |
| `case-strategy-retailer-activity-scope` | _121 | 零售商 A/B/C 活动范围对比 |
| `case-strategy-m-brand-profit-model` | _117 | M 品牌代理加盟盈利模式 |
| `case-strategy-snack-business-design` | _131 | 零食企业业务设计六要素示例 |
| `case-strategy-model-selection-quiz` | _203 | 10 个商业情境模型选择练习 |

### 框架卡（视检索结果）

- 蓝海战略四步动作框架（若重新检索找到出处）
- 凯纳创新框架（若用户确认存在）

---

## 统计

- 已完成 framework 卡：6 张
- 已完成 tool 卡：10 张
- 已完成 concept/case 卡：0 张
- 待确认框架：2 个
- 待黄药师修复：parser

---

*王语嫣 v1 · 2026-06-22*
