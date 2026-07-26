---
id: task_20260726_wangyuyan-agent-evolution
task_id: 200
assignee: laowantong
status: queued
created_at: 2026-07-26
updated_at: 2026-07-26
domain: system
priority: P0
source: 00_inbox/解放思想探索营/ + 30_wiki/frameworks/framework-kdo-modeling-methodology.md
diagnosis: 60_feedback/diagnosis/diag_20260726_wangyuyan-thought-liberation.md
---

# Agent 闪电进化：从后知后觉到先知先觉

## 先目标再方案

**目标**：KDO Agent 体系从"后知后觉"（踩坑→打补丁，41条pitfalls）升级到"先知先觉"（预判80%流程，Agent自主识别改进机会并建模沉淀）。

**现状诊断**：KDO Agent 是优秀的执行者——按spec生产、按标准审查。但没有一套方法论让Agent**自己变强**。当前改进全靠人推动（王语嫣诊断、黄药师建工具、欧阳锋审查）。

**目标状态**：Agent 能在执行中发现模式、自主提出改进、低成本验证、建模沉淀为可复用组件。人从"推动者"升级为"把关者"。

## 先框架后细节

### 核心框架：闪电模型 → Agent进化四阶

| 闪电模型 | Agent进化映射 | Agent当前状态 | 目标状态 |
|:--|:--|:--|:--|
| **大胆设想** | Agent 自主识别改进机会并 push back | ❌ 缺失——Agent 只执行不质疑 | 老顽童发现 spec 逻辑不自洽时主动 reject；欧阳锋审查中识别跨卡模式问题时发起系统改进 |
| **底层自洽** | Agent 行为从KDO底层原则**推导**出来 | ⚠️ 部分——context是经验堆叠，不是推导产物 | 每个Agent的context可追溯到双三角/TCPR/实事求是的具体原则 |
| **假设试错** | Agent新能力用3-5个任务低成本验证 | ❌ 缺失——新能力上线=大工程 | Feature级原子能力拆解（#198已试点），新能力先跑3个任务验证再推广 |
| **建模重构** | 产出模式和踩坑经验沉淀为可复用组件 | ⚠️ 部分——有个别case但未体系化 | 错误模式库+能力雷达图+暗知识捕捞 = 每个Agent标配 |

### 三层自洽诊断

| 层 | 应有 | 当前实际 | 动作 |
|:--|:--|:--|:--|
| **底层原则** | 双三角（人定审美/体系，AI执行）+ TCPR + 实事求是 | ✅ 已有 | 整理为Agent设计原则卡 |
| **中层方法** | 从底层推导出Agent设计规范（身份边界/协作协议/进化机制） | ⚠️ TCPR身份轴（D域）是对的但未推广 | 从TCPR+双三角推导出全体Agent的设计原则 |
| **上层执行** | 每个Agent的context/复盘/进化可追溯到中层原则 | ❌ context是经验堆叠 | 重构context为推导链：底层原则→设计规范→具体规则 |

### 四层觉察路线图

| 层次 | 定义 | KDO当前 | #200目标 |
|:--|:--|:--|:--|
| 不知不觉 | 混乱，重复踩坑 | — | — |
| **后知后觉** | 踩坑→复盘→打补丁 | ✅ 当前 | → |
| **当知当觉** | 边做边建模，实时捕获 | — | #200目标：Agent自主捕获规律 |
| **先知先觉** | 预判80%流程 | — | 下一阶段 |

## 先定性再定量

### 定性方向

Agent从"生产者"升级为"生产+进化者"。三个定性信号：
1. 欧阳锋审查中 🔴🟡 数量趋势下降（Agent自检前置）
2. Agent 自主提出改进并入库的案例从0→1→N
3. 新Agent上线不再需要"边踩坑边补context"——启动时80%规则已可推导

### 定量指标（后续建立）

- Agent 自我发起的改进提案数/月
- 欧阳锋退回率趋势（应下降）
- 重复踩坑次数（同类型pitfall复现频率）
- 组件库新增组件数（来自Agent自驱沉淀）

## 卡片产出

### P0（3张）

| # | id | type | title | 核心内容 |
|:--|:--|:--|:--|:--|
| 1 | concept-kdo-agent-design-principles | concept | Agent设计原则：从双三角推导的Agent行为规范 | 从双三角/TCPR/实事求是推导出Agent设计的5条底层原则。人类定义审美和体系→Agent执行→独立审查→建模沉淀→持续进化。每条原则含推导链路（从哪个底层概念来，推导到哪条具体规则） |
| 2 | concept-kdo-agent-four-level-awareness | concept | Agent四层觉察：从后知后觉到先知先觉 | 四层定义+判据+KDO当前定位+跃迁路径。每层对应的Agent行为特征和典型失败模式。与闪电模型四阶的映射 |
| 3 | bridge-lightning-agent-evolution | bridge | 闪电模型×Agent进化：同一个四阶在两个域的映射 | 大胆设想=Agent自主改进/底层自洽=从原则推导行为/假设试错=低成本验证/建模重构=沉淀为组件 |

### P1（4张）

| # | id | type | title | 核心内容 |
|:--|:--|:--|:--|:--|
| 4 | tool-agent-self-evolution-protocol | tool | Agent自我进化协议 | 每次复盘四问：①这次踩的坑能不能变成一条规则？②这条规则该写进context还是方法论卡？③能不能从已有底层原则推导出来？（能=推导链确认，不能=发现原则缺口）④改进后怎么验证有效？含每日复盘模板和组件沉淀格式 |
| 5 | dk-agent-evolution-pitfalls | dk | Agent进化常见失败模式 | 补丁堆叠不追溯原则/改进靠人推动Agent被动/验证不足过早推广/沉淀格式不一致无法复用 |
| 6 | tool-agent-context-derivation-audit | tool | Agent context推导链审计 | 逐条检查context中每条规则能否追溯到底层原则（双三角/TCPR/实事求是）。能追溯→标注推导链；不能→要么删除要么补充原则。含审计清单模板 |
| 7 | case-agent-self-evolution-pilot | case | Agent自我进化试点案例 | 记录本次#200任务中Agent体系自身进化的过程和经验——从王语嫣诊断→#200编排→老顽童生产→欧阳锋审查→Agent能力变化。作为Agent自我进化的第一个完整案例 |

**合计：7张（3 P0 + 4 P1）**

## 已有卡关联

| 已有卡 | 关系 | 类型 |
|:--|:--|:--|
| framework-kdo-modeling-methodology | Agent进化=建模方法论在Agent层的应用。四层觉察明确写入 | 关系型双向 |
| framework-yitang-thought-liberation-lightning (#200配套) | 闪电模型=Agent进化四阶的认知框架 | 关系型双向 |
| framework-一堂-基本功-四字诀拆建推练 | Agent进化也是"拆建推练"——拆出Agent组件→建Agent规范→推成Agent共识→练出进化能力 | 关系型双向 |
| framework-ouyangfeng-review-methodology | 双护栏=Agent自检前置的目标状态 | 引用型单向 |
| .agent/pitfalls.md (41条) | Agent进化组件库的原始材料——每条pitfall=一个待压缩的组件 | 引用型单向 |

## 边界

- 不覆盖：具体Agent的context重写（那是后续任务，本任务只建原则和工具）
- 不覆盖：KDO CLI/基础设施改进
- 不单独建域：这是system域，桥接innovation域和modeling域

## 执行顺序

```
P0先产：Agent设计原则 → 四层觉察 → 桥梁卡
  ↓
P1后产：自我进化协议 → 推导链审计 → 失败模式 → 案例
  ↓
后续任务（不在此任务单）：
  - 用推导链审计工具逐一审查现有Agent context
  - 老顽童/欧阳锋/王语嫣的context从经验堆叠重构为推导链
```
