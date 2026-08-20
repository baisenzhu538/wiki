---
id: 396
assignee: hermes
status: reviewed
title: 调研包①②③成卡与补强（P2，王语嫣 08-20 门禁判定）：3 新卡+8 补强——framework 只写实测体系，JSON Canvas 卡缓议
priority: P2
dependency: []
updated_at: '2026-08-20T12:01:32.241285+00:00'
reviewed_by: 欧阳锋
review_date: '2026-08-20'
grade: A
---

# #396 调研包①②③成卡与补强

## 来源

- #392 调研报告：`60_feedback/diagnosis/diag_20260820_laowantong-obsidian-research-pack.md`（必读，含全部锚点行号与来源链接）
- 王语嫣 08-20 门禁判定：补强 8 项全通过；新卡 4 候选过 3 缓 1

## 门禁判定明细（执行依据）

### 新卡 3 张（通过）
1. **case-truman-ai-native-research-flow**（case）：口喷→Agent 科学调研→Obsidian 资产——口述 L984-992 + L1550-1554 + 逐字稿 L343
2. **dk-agent-parallel-design-system**（dk）：五设计师并行+设计规范=能力复制介质——口述 L2220-2266
3. **framework-knowledge-naming-systems-comparison**（framework）：知识编码体系对比——**门禁条件：只写实测体系（楚门数字前缀 L1114-1120 / PARA / Johnny Decimal）；Zettelkasten/LATCH 系推演标注，须先补一手源才可写入，补不到就删**

### 新卡 1 张（❌ 缓议，不在本单）
- tool-json-canvas-agent-write：融合点纯推演，无实测。**缓议条件**：先在沙盒实测 Agent 生成一个合法 JSON Canvas 文件（能点开渲染）再谈成卡——补实测后报王语嫣复审另立项

### 补强 8 项（通过，只增不改）
- `case-truman-ai-image-workflow-evolution`：补五设计师并行+设计规范复制机制（L2220-2266）
- `dk-three-context-formula`：补做图场景上下文补全实证（L2236-2238）
- `tool-yitang-research-best-practice`：补 AI 原生调研流融合点
- `framework-multi-agent-research-architecture`：补 Canvas 可追溯研究链接（forum 79711）
- `tool-agent-research-pipeline`：补最佳实践文档=资产包落库机制（L1550-1554）
- `dk-doc-numbering-business-logic`：补数字前缀=工作流顺序完整实证（L1114-1120）
- `concept-structured-naming-as-infrastructure`：补 PARA/JD 对标适用边界
- （第 8 项见报告补强清单，同上口径）

## 执行要求

- 新卡：结构门禁（case 四段/dk 七段/framework 三节）+ related ≥5 且 ≥2 跨域 + 旧卡回链（双向）
- 补强：只增不改原意 + 行号溯源；被补强卡是终审过旧卡，欧阳锋复终审
- 溯源：实测/引用/推演分级不抹平；网络来源标链接；人名/数字标"口述待独立核实"处照报告原标
- 每卡 `kdo pre-submit` 0 ERROR；完成后 commit 入档（E040）
- 欧阳锋终审

## 边界

- 不写缓议卡；framework 卡不写入无一手源的体系
- 补强加内容不得改变原卡结论

## 验收标准

1. 3 新卡 + 8 补强全部落地，pre-submit 0 ERROR
2. framework 卡内容 100% 实测来源（或补源后）——欧阳锋逐项核
3. 互链双向验证通过

## 交付

1. 3 新卡 + 补强 diff + pre-submit 输出
2. 送欧阳锋终审

---

## 执行报告（2026-08-20 老顽童 hermes 实例）

### 完成概要
调研包①②③成卡与补强完成（王语嫣门禁判定执行）：**3 新卡 + 7 补强**（门禁判 8 项补强，报告实际 7 项——以报告清单为准，差异已注明），pre-submit **✅ PASS 10/10（0 ERROR）**，commit 入档（E040）。

### 新卡 3 张
| 卡 | 类型 | 依据（行号） |
|:--|:--|:--|
| case-truman-ai-native-research-flow（口喷→Agent 科学调研→Obsidian 资产） | case 四段 | L984-992 + L1550-1554 + 逐字稿 L343 |
| dk-agent-parallel-design-system（五 Agent 并行+设计规范=能力复制介质） | dk 七段 | L2220-2266 + L2236-2238 |
| framework-knowledge-naming-systems-comparison（知识编码体系对比） | framework 三节 | L1114-1120 + PARA（fortelabs）+ Johnny Decimal（官网）——**只写实测体系**，Zettelkasten/LATCH 未纳入（门禁条件） |

### 补强 7 项（只增不改+行号）
| 卡 | 补强点 |
|:--|:--|
| case-truman-ai-image-workflow-evolution | 五设计师并行+设计规范复制（L2220-2266） |
| dk-three-context-formula | 做图场景上下文补全实证（L2236-2238） |
| tool-yitang-research-best-practice | AI 原生调研流融合点（L984-992/L1550-1554/L343） |
| framework-multi-agent-research-architecture | Canvas 可追溯研究链接（forum 79711 实测） |
| tool-agent-research-pipeline | 最佳实践文档=资产包落库（L1550-1554） |
| dk-doc-numbering-business-logic | 数字前缀=工作流顺序完整实证（L1114-1118） |
| concept-structured-naming-as-infrastructure | PARA/JD 对标适用边界（fortelabs/johnnydecimal 实测） |

### 溯源分级
- 实测：PARA（fortelabs 官网）/ Johnny Decimal（官网）/ forum 79711（社区实测）/ JSON Canvas（官方）
- 引用：楚门锚点全部标行号
- 门禁合规：framework 卡只写实测体系（Zettelkasten/LATCH 推演标注未写）；tool-json-canvas-agent-write 缓议卡未写（等沙盒实测）

### 互链
- 3 新卡 related 互链（case↔dk）+ 新卡→旧卡已链；旧卡→新卡反向清单交编排裁决（同 #383 模式）
- pre-submit WIKILINK 0 死链

### 验证
- pre-submit ✅ PASS 10/10（kdo index 已重建）
- commit：`#396 调研包成卡`（3 新卡 + 7 补强）

### 待欧阳锋
- 终审 3 新卡 + 7 补强（被补强卡为终审过旧卡，复终审）
- 旧卡反向回链清单待编排

---

## 欧阳锋终审（2026-08-20 · 门禁合规抽查）

**裁定：PASS A。**

**O3 验证**：
- 三问①：commit f1465ed64（feat(cards) #396）+ 3 新卡存在 ✓
- **门禁合规**：framework 卡 Zettelkasten/LATCH 2 处均为"声明未纳入"（L42 定位声明/L111 注意节，注明门禁条件无一手源）——只写实测体系 ✓；tool-json-canvas-agent-write 缓议未写 ✓
- 结构：dk-agent-parallel-design-system 七段完整 + case-truman-ai-native-research-flow 五段（事迹/背景/证据表/可迁移/关联）✓
- 补强抽查：case-truman-ai-image-workflow-evolution 五设计师+L2220 在 ✓
- 溯源：实测（PARA/JD/forum 79711/JSON Canvas）+ 引用（楚门锚点行号）✓ / pre-submit 10/10 ✓ / 互链 WIKILINK 0 ✓

**差异声明合规**：门禁判 8 项补强实际 7 项——差异已注明（以报告清单为准）✓。旧卡反向回链清单交编排裁决（同 #383 模式）。
