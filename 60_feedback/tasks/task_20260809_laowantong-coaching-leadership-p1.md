---
id: task_20260809_laowantong-coaching-leadership-p1
assignee: hermes
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-09
updated_at: '2026-08-09T09:15:09.953341+00:00'
priority: P1
wsjf: 3.3
---

# 教练式领导力 P1 增量（#281 · 4 张）

## 任务目标

教练式领导力卡片化 P1 批次——跨课桥接 + 暗知识增量。诊断：`60_feedback/diagnosis/diag_20260809_coaching-leadership.md`。

## 卡片规格（4 张）

| # | 卡 id | type | 核心内容 | source_refs 主锚 |
|:--|:--|:--|:--|:--|
| 11 | bridge-coaching-leadership-feature-layered | bridge | 教练式领导力 × Feature 分层 L5：五阶梯 = 组织层 Feature 组合（L1 以身作则=组织文化、L2 扛事=目标管理、L3 讲道理=决策沟通、L4 反馈=人才发展、L5 希望=愿景组织）；教练对话 = 倾听/提问/反馈 Feature 点菜 | 01-口述 + framework-truman-feature-layered-system + 周期表 JSON |
| 12 | tool-leadership-exit-consulting | tool | 出口式咨询（超级小抄：找出口→换视角→探究解法 + "增长 3-5 倍卡在哪"出口模板 + 共识前提：需求是事实/商业可预判） | 01-L2650/L2656 |
| 13 | dk-leadership-trust-coin-sensitivity | dk | 信任硬币敏感性（领导力 = 成百上千次互动的加减币觉察）+ 2×5 耐心标准（安全空间有期限）+ 希望表达库三维度方法 | 01-L776/L786/L2250/L3090 |
| 14 | dk-leadership-feedback-iceberg | dk | 反馈冰山理论（显性/隐性）+ 反馈三明治结构（正面/改进/负面三段式）——若与 tool 6 内容高度重叠可合并入 tool 6（二选一，生产时判断） | 02-口述 + VLM 反馈区 |

## 生产纪律

- 桥接卡（#11）必写：双域同构映射表（五阶梯每层 ↔ Feature 域卡）+ 使用导航（什么时候用哪边）+ **ICF/GROW 元技能认识（"模型不会倾听，教练才会"——模型选择是元技能，三方法补全 §五·补）**
- dk 卡含失败模式/反例/边界；source_refs 行号可核实
- 定位声明必写；related 回链 Feature 域（framework-truman-feature-layered-system / 周期表 JSON）+ ICF 体系（外部对照）

## 验收标准

- 每卡 `kdo pre-submit` 通过 + lint 0 ERROR
- 桥接卡同构映射表完整（5 层 ↔ Feature 映射）
- dk 卡含 ≥2 个失败模式或反例
- 与 #280 的卡组无重复（dk-14 合并判断记录在案）

## 依赖

- #280 卡组 reviewed（桥接卡依赖 framework 卡定位）

## 边界

- 不新建 Feature 域卡（只做桥接）
- 不深挖 21 章工具卡全量（P2 候选，VLM 校对后另排）

## 终审记录（2026-08-09 欧阳锋）

**verdict: PASS A · blocking: 无 · methodology v2.2**

O0 溯源验证：
1. 3 新卡存在（bridge/tool/dk）+ 合并判断记录真实：tool6 L160"冰山延伸"——口述 02 与 VLM 反馈区均无冰山直接表述，内核已由三种反馈结构+3F 倾听覆盖，按任务单二选一条款合并（**避免无源推断，#250 教训遵守**）
2. 出口式咨询锚点 L2650-2658 原文命中（"定一个出口…有了高价值出口再往前推"+"需求是事实，你认吗"共识前提）
3. 2×5 耐心标准 L2250 原文命中（改五轮→四次→三次递减）+ L776 黑盒模型/L3090 希望表达库已在 #280 验证
4. bridge 映射完整：定位声明 + 五阶梯×Feature L5 同构映射表（L5 组织层 13 Feature 组合）+ 教练对话=Feature 点菜命题 + ICF/GROW 元技能认识
5. dk 失败模式 ≥2；pre-submit 3 卡批量 PASS
6. 边界遵守：不新建 Feature 域卡（只桥接）、不深挖 21 章工具卡（P2）

五维：溯源 90/逻辑 90/暗知识 90/可操作 90/表达 90 → 总分 90（A）
