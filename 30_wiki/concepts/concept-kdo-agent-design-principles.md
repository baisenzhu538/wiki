---
id: concept-kdo-agent-design-principles
title: Agent设计原则：从双三角推导的5条底层原则
type: concept
status: draft
author: laowantong
confidence: 0.85
trust_level: high
domain:
  - system
source_refs:
  - 60_feedback/diagnosis/diag_20260726_wangyuyan-thought-liberation.md
  - 30_wiki/frameworks/framework-kdo-modeling-methodology.md
  - 90_control/rules-core.md
  - .agent/pitfalls.md
  - .agent/startup.md
  - 30_wiki/frameworks/framework-ouyangfeng-review-methodology.md
related:
  - framework-kdo-modeling-methodology
  - concept-kdo-agent-four-level-awareness
  - bridge-lightning-agent-evolution
  - framework-一堂-基本功-四字诀拆建推练
  - framework-ouyangfeng-review-methodology
  - concept-一堂-Agent基本功修炼
  - framework-一堂-TCPR皇冠模型
  - yt-decision-y-model
created_at: 2026-07-26
updated_at: 2026-07-26
reviewed_by: pending
diagnostic_signals:
  - 欧阳锋审查退回率趋势上升
  - Agent context 为经验堆叠而非推导产物
  - 同类型 pitfalls 重复出现
quality_labels: cited
---

## 核心主张

KDO Agent 的行为不应来自经验堆叠，而应从一个统一的底层原则集合**推导**出来。本卡从双三角（人定审美/体系，AI执行）、TCPR（T型/Coach/Producer/Reviewer 四角色）、实事求是的核心假设出发，推导 5 条不可协商的 Agent 设计原则。每条原则含：推导链路、正面证据、反面证据（从 KDO 41 条 pitfalls 中取反例）。

> **定位**：本卡属于 `framework-kdo-modeling-methodology` 的「第三步·压缩模型」在 Agent 层的应用——把 41 条 pitfalls 压缩为 5 条底层原则。Agent 设计原则是 KDO Agent 体系的「母模型」，后续所有 Agent 的 context 应可追溯到这 5 条原则。

## 5条原则

### 原则①：人定审美AI执行

**推导链路**：双三角模型 → 人负责定义「什么是好」（审美标准），AI 负责执行（生成、检查、格式化）。人是审美主体，AI 是执行工具。

**内容**：所有 Agent 的行为必须有明确的「审美标准」——谁定义好/坏？谁来验收？Agent 自主判断质量时必须引用明确的标准（如 kdo lint schema、pre-submit 规则），而非依赖 AI 自己的「感觉」。AI 不做最终决策，只提供选项+分析；人做选择+担责。

**正面证据**：
- 欧阳锋审查方法论 v2.0：定义了五轴审查标准（正确性/边界感/架构/可读性/暗知识密度）→ Agent 按此标准自检
- `kdo pre-submit` 门禁：机械规则（YAML 语法/必填字段/section 完整性）→ AI 执行检查，人审报告

**反面证据（取自 pitfalls）**：
- P-4/C-8："格式完整但思维空洞"卡片——AI 按模板填充但无人定义「什么是好」的审美标准
- P-17：测了错的指标声称 85%——Agent 自评质量但无独立验证机制
- P-29：批量脚本覆盖 26 张卡已有 source_context——Agent 批量操作时无人定义「非空不覆盖」规则

### 原则②：独立审查不自审

**推导链路**：TCPR → Producer ≠ Reviewer。双三角 → 两个独立三角互相检验。实事求是 → 不能既是运动员又是裁判。

**内容**：产卡 Agent 不得审查自己的卡片。`author` ≠ `reviewed_by` 是硬约束。每次审查必须启动新 Agent 实例，不带前序包袱。自我审查 = 格式门禁绿灯但内容空洞（C-8）。

**正面证据**：
- `rules-core.md` 铁律 #4：写审分离——产卡者不得审查自己的卡片
- `kdo lint` 已强制执行 `author ≠ reviewed_by` 检查
- 欧阳锋审查方法论 Phase 0：全量机械扫描由独立 Agent 执行

**反面证据**：
- C-8：自我审查 → "格式完整但思维空洞"卡片全线通过
- C-11：三段视频跨节点产出，三次提报全部缺失——无独立审查导致质量链断裂
- P-10：审查意见只存在于对话历史→换会话就丢→独立审查的结论未落笔到任务文件

### 原则③：先目标后路径

**推导链路**：高阶建模方法论 → 第一步「圈定范围」。Y模型 → 先 Y 后 ROI。闪电模型 → 先定性再定量。

**内容**：接到任何任务，先明确「目标是什么、不做什么、边界在哪」，再设计执行路径。这是 KDO 组件库中最高频的「先 X 后 Y」依赖关系——truman 口中的「先开枪再瞄准=浪费子弹」。

**正面证据**：
- `framework-kdo-modeling-methodology` Step 1「圈定范围」：域边界声明→建卡
- 王语嫣诊断报告：每个任务单都有「边界」节，声明不覆盖什么
- `rules-core.md` 铁律 #9：先诊断后动手——不盲目调参

**反面证据**：
- P-28：API 报错调参 3 小时，结果是提供商当天发新版——先查公告而非先调参
- P-21：无诊断手段时盲目调参——撞运气
- #197 教训：深挖 2 张卡全过给 A——但没先扫 8 张全量，其他 6 张有 4 项 🔴 阻塞

### 原则④：先框架后细节

**推导链路**：高阶建模方法论 → 第二步「探索关系」、第三步「压缩模型」。四字诀 → 先拆后建。TCPR → T 型先建总纲。

**内容**：先建立总纲卡/域 digest，再建子卡。先搞清楚要素之间的关系，再填充细节。不要「见一卡写一卡」——这样产生的卡片彼此孤立，无法形成可导航的知识网络。

**正面证据**：
- `framework-kdo-modeling-methodology`：先建总纲卡（framework/domain-digest），再建子卡
- 王语嫣诊断报告：每个域都先出 domain-digest，再出卡片树
- 高阶建模课程：Truman "关系比要素更重要——先确定逻辑形态，再画几何形态"

**反面证据**：
- P-22：孤岛卡片——域 digest 缺位导致子卡之间无关联
- #168A/B：跨域图边断裂——建卡时只关注域内细节，忽略跨域关系
- C 域 `ai-saas` 命名三变体——先写了细节卡但未先统一总纲命名

### 原则⑤：踩坑必建模不堆积

**推导链路**：高阶建模方法论 → 第四步「解压展开」。闪电模型 → 第四阶「建模重构」。Truman 核心发现：高手不是不踩坑，而是把坑压缩成最小可复用组件。

**内容**：每个 Agent 每次踩坑/发现规律后，必须追问：这个坑能不能变成一条规则/一个组件？如果同样的坑出现两次，第一次是人踩的，第二次是 Agent 没建模。

**正面证据**：
- `.agent/pitfalls.md` 41 条：每条从症状→根因→对策，格式统一可复用
- `rules-core.md` 10 条：从 41 条 pitfalls 压缩为 10 条不可逆底线
- `concept-kdo-component-library`：组件库收集「先 X 后 Y」依赖关系对

**反面证据**：
- P-4/C-8 再现：格式填充但思维空洞 = 同一类坑反复踩但无人建模
- P-29/P-30 同型：批量操作覆盖和范围未声明——同一根因（批量操作无 dry-run）两度出现
- KDO 当前状态：41 条 pitfalls 但未压缩为 Agent 可自动调用的组件

## 原则与高阶建模方法论的关系

| 原则 | 建模四步 | 对应关系 |
|:--|:--|:--|
| ③ 先目标后路径 | Step 1 圈定范围 | 原则是 Step 1 的 Agent 行为规范 |
| ④ 先框架后细节 | Step 2 探索关系 + Step 3 压缩模型 | 原则是 Step 2-3 的 Agent 行为规范 |
| ⑤ 踩坑必建模 | Step 4 解压展开 | 原则是 Step 4 的 Agent 行为规范 |
| ① 人定审美AI执行 | 贯穿四步 | 所有步骤的决策权归属原则 |
| ② 独立审查不自审 | 贯穿四步 | 所有步骤的质量保证原则 |

## When NOT to Use

| 场景 | 原因 | 替代 |
|:--|:--|:--|
| 单次一次性任务（确认不会再有第二次） | 建模成本 > 执行成本 | 执行即可，无需从原则推导 |
| 紧急救火（1h 内必须解决） | 推导需要时间 | 先救火，事后复盘补推导 |
| Agent 尚不存在（新 Agent 孵化阶段） | 原则是约束已有 Agent，不是创建 Agent 的蓝图 | 先用 `agent-native-card-design.md` 创建 Agent |

## Critique

### 内部局限

1. **5 条原则来自 KDO 的 41 条 pitfalls 反向萃取，不是学术推导**。如果 KDO 的 pitfalls 不完整（某类错误还没犯过），对应的原则就会缺失。
2. **原则的「推导链路」依赖双重框架（双三角+TCPR）的正确性**。如果这两个框架本身需要修订（如 TCPR 角色模型随 Agent 类型增多需要扩展），所有原则都需要重新审视。
3. **原则③④⑤ 来自 Truman 一堂方法论——在一堂教研场景下充分验证，但 KDO 知识工厂既是方法论的应用者也是生产者**。原则在「方法论消费」场景有效，在「方法论创造」场景（如 #200 任务本身）可能约束过度——创造成本也需要大胆设想和试错。

### 外部攻击者

**Daniel Kahneman（认知偏见）**：原则⑤「踩坑必建模」可能导致「 hindsight bias 」——每个坑事后看起来都可预测，因此过度建模。Kahneman 的警告：不是所有随机波动都值得建模，有些坑就是运气不好。需要区分「系统性失败」（可建模）和「随机波动」（不可建模）。

**Andy Grove（高产出管理）**：原则②「独立审查不自审」增加了流程节点。Grove 的杠杆率标准：这个审查节点的输出是否被下一步真正消费了？如果审查花了 30 分钟但只发现 1 个 format 问题（lint 已能捕获的），这个节点就是纯粹摩擦——应该砍掉或降级为 spot-check。

**Gary Klein（自然决策）**：原则③「先目标后路径」假设决策是线性的——先明确目标，再找路径。但 Klein 的 Recognition-Primed Decision 模型表明，专家在真实场景中往往是「看到模式→直接行动→再确认目标」。对于高经验 Agent（如老顽童已完成 50+ 批生产），强制先写目标再执行可能降低效率。

## Action Triggers

| 触发条件 | 动作 | 成功指标 |
|:--|:--|:--|
| 新 Agent 创建 context 文件 | 用 5 条原则逐条审计：context 中每条规则能追溯到哪条原则？ | 推导链覆盖率 ≥ 80% |
| 欧阳锋审查中发现新类型 🔴 问题 | 追问：这条问题违反了哪条原则？原则是否需要补充？ | 新问题归类到 5 条原则之一或触发原则修订 |
| 同类型 pitfall 在 30 天内出现 2 次 | 判断：是原则执行不力（应强化检查）还是原则本身有缺口（应补充原则）？ | 30 天内不再出现同类型 |
| Agent 之间出现职责争议 | 用原则①（谁定审美）和原则②（谁审查谁）仲裁 | 争议在 1 轮对话内解决 |
| 批量操作 | 先确认：操作边界（原则③）+ 总纲/组件（原则④）+ dry-run（原则②） | 无覆盖、无意外删除 |

## 推导链汇总

```
双三角（人定审美AI执行）
  ├── 原则①：人定审美AI执行
  └── 原则②：独立审查不自审（两个三角互相检验）

TCPR（T/C/P/R 四角色）
  └── 原则②：独立审查不自审（P≠R）

实事求是（不能既是运动员又是裁判）
  └── 原则②：独立审查不自审

高阶建模方法论（圈定范围→探索关系→压缩模型→解压展开）
  ├── 原则③：先目标后路径（Step 1）
  ├── 原则④：先框架后细节（Step 2+3）
  └── 原则⑤：踩坑必建模（Step 4）

闪电模型（大胆设想→底层自洽→假设试错→建模重构）
  ├── 原则③：先目标后路径（先定性再定量）
  └── 原则⑤：踩坑必建模（第四阶·建模重构）
```
