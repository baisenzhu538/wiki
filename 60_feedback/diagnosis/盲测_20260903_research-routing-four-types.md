---
id: blindtest-20260903-research-routing-four-types
title: "#629 路由盲测记录——四类型判定路由 8 用例（仅凭 description）"
type: report
status: draft
author: 老顽童
reviewed_by: 待审
created_at: 2026-09-03
updated_at: 2026-09-03
domain: research
tags:
  - audience:executor
  - scene:research
source_refs:
  - 60_feedback/diagnosis/建议书_20260902_调研域skill化缺口与四类型整合.md
  - 40_outputs/capabilities/skills/shared/research-core/SKILL.md
  - 40_outputs/capabilities/skills/shared/research-explosion-five-step/SKILL.md
  - 40_outputs/capabilities/skills/shared/research-digging-approach/SKILL.md
---

# #629 路由盲测记录（建议书 §五验收口径：agent 未读正文仅凭 description 判定）

> 测试时间：2026-09-03 05:1x · 测试人：老顽童（#629 生产自测）· 方法：模拟新会话 agent 只读三个 skill 的 frontmatter description（research-core v1.1 / research-explosion-five-step / research-digging-approach，正文不读），对 8 条改述请求做四类型判定，答案对照建议书 §五标准答案。

## 测试用例与结果

| # | 改述请求（不含原触发词原句） | 标准答案（建议书 §五） | 盲测判定 | 结果 |
|--:|:--|:--|:--|:--:|
| 1 | 「我们要进宠物智能用品这行了，一周内给我搭出这个领域的认知框架」 | 新领域建认知 → 爆炸式 | research-core 第一层 A 判「宽·全」→ 加载 research-explosion-five-step（description 命中词：新领域进入/建认知） | ✅ |
| 2 | 「帮我查一下竞品到底卖多少钱一台，这个数拿不到我们决策没法做」 | 单点关键情报 → 挖掘式 | 判「深·挖」→ 加载 research-digging-approach（命中：竞品核心数据/这个数必须拿到） | ✅ |
| 3 | 「公司要不要做海外市场，把几个维度都分析一下再给我建议」 | 复杂决策 → 系统式 OSCAR | 判「高·准」→ 走 research-core 第一层 B OSCAR（挖掘/爆炸两 skill 的 When NOT 均显式让位 OSCAR） | ✅ |
| 4 | 「盯着某某竞品，他们一有新动作就告诉我」 | 长期盯梢 → 自动式 | 判「动态·稳」→ 加载 research-ci-framework（research-core description 命中：竞对盯梢；第一层 A 表路由行明示"只搭监控不跑单次调研"） | ✅ |
| 5 | 「网上关于'预制菜进校园'的信息又多又乱，根本没法判断谁对」 | 信息乱无法判断 → 爆炸式（先宽后深） | 判「宽·全」→ research-explosion-five-step（description 命中：信息五花八门/盲人摸象同构） | ✅ |
| 6 | 「验证一下'某品牌市占率 30%'这个说法靠不靠谱」 | 事实查证 → research-core 纪律层（非四类型方法线） | 不进挖掘/爆炸——走第一层 B 前先过第二层交叉验证纪律（core description 命中：验证这个说法/数据核验） | ✅ |
| 7 | 「今晚就要，明天早会我要用这个行业的分析结论」 | 时间极短 → 爆炸式/挖掘式均 When NOT | 两 skill 反例黑名单均显式拦截（时间极短不用/紧急决策不用）→ 降级快速扫描+标注风险 | ✅ |
| 8 | 「纯格式整理：把这 20 份调研纪要排版归档」 | 非调研 → 不路由 | research-core 反触发明示（纯格式整理不路由进本层） | ✅ |

## 结论

- 8/8 判定正确：四类型路由（#1/2/3/4）+ 组合场景（#5）+ 纪律层任务（#6）+ When NOT 拦截（#7）+ 反触发（#8）
- 路由不分裂验证：三个 description 均带「research-core 第一层·X 路由线」前缀 + When NOT 互指，agent 从任一入口进入都会收敛到同一判定（#3/#7 双向验证通过）
- 遗留观察项（不阻塞）：#2 类请求用户未说"必须拿到"时靠 description 的「竞品真实成本/水下情报」场景词兜底，挂载后建议 skills-assistant 在使用检查中留意该类请求的实际命中率

## 三写一致核对

| 写面 | research-explosion-five-step | research-digging-approach | research-core |
|:--|:--|:--|:--|
| SKILL.md frontmatter description | ✅ 爆炸式路由线+触发词+When NOT | ✅ 挖掘式路由线+触发词+When NOT | ✅ v1.1 判定路由描述 |
| manifest.yaml description/trigger | ✅ 与 frontmatter 同源（触发词按 INDEX 口径分 4 组） | ✅ 同源（3 组） | ✅ v1.1+补 3 线触发组 |
| INDEX.md 生成物 | ✅ #51（scan_skills_registry 刷新，8/8 🟢 130 行） | ✅ #49（8/8 🟢 146 行） | ✅ 刷新后 description 同步 |
