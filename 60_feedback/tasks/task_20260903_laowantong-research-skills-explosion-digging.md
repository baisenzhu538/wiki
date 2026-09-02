---
id: task_20260903_laowantong-research-skills-explosion-digging
title: 调研域 skill 补位：爆炸式五步法 skill + 挖掘式穷尽手段流程 skill + research-core 第一层嵌四类型判定
seq: 629
status: pending_review
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-03
decision_source: skills-assistant 建议书《调研域skill化缺口与四类型整合》（老朱直令勘察的产出）09-03 王语嫣裁定：动作1/2 立项本单；动作3 裁定=嵌入 research-core 第一层（不另起前置 skill，防路由分裂）；动作4 并入；动作5 验收挂载归 skills-assistant 本职
reviewer: 欧阳锋
instance: laowantong
updated_at: '2026-09-02T22:15:34.267763+00:00'
evidence: 60_feedback/diagnosis/盲测_20260903_research-routing-four-types.md
---

# #629 调研域 skill 补位（老顽童）

## 背景

skills-assistant 全库勘察实证：调研域 90+ 卡方法体系完整，但 skill 化不均——爆炸式完全无 skill（五步法卡在库、research-explosion-partner agent 已部署，唯独缺通用 skill）、挖掘式只有工具无流程、四类型判定逻辑未行为化。建议书：`60_feedback/diagnosis/建议书_20260902_调研域skill化缺口与四类型整合.md`（内含四类型表/缺口证据/验收口径）。

## 任务

1. **research-explosion-five-step skill**（P0）：爆炸式五步法行为化——参照 research-explosion-partner SPEC（#335 终审 A-）+ framework-baozhashidiaochan-five-step 卡；含 manifest/触发词/失败模式/When NOT（单一信息点→挖掘式/推理决策→OSCAR/时间极短不用）/反例黑名单
2. **research-digging-approach skill**（P1）：挖掘式流程——穷尽手段 5 层升级逻辑+单点狙击+合规边界（When NOT：简单查询/紧急决策/成本过高/法律风险）
3. **research-core 第一层嵌四类型判定**（P1）：诊断信号表+When NOT 写进第一层（最小自包含），按深/高/宽/动态分型路由到四方法线；不改 OSCAR 现有武器库路由，两者互补
4. 验收配合：产出后交 skills-assistant 过 darwin-skill 9 维门禁+挂载（他不产只验）

## 边界

- 不重写 30_wiki 卡（产 skill 不产卡）；与 #594/#595/#597 已收口无撞车面
- 参照样板：skill-architecture-design（#593 U2 行为化样板）
- 自动式不动 CI 框架，只把「何时启用+监控搭建」写进判定层

## 交付

- 2 个 skill + research-core 第一层 diff + manifest 三写一致 + 路由盲测记录 + 执行报告
- claim/complete 走 queue_transition（complete 629）

## 执行报告（#629）

**交付物**
- `40_outputs/capabilities/skills/shared/research-explosion-five-step/`（SKILL.md + manifest.yaml）
- `40_outputs/capabilities/skills/shared/research-digging-approach/`（SKILL.md + manifest.yaml）
- research-core 第一层嵌四类型判定（SKILL.md v1.0→v1.1 diff，author 行注明 #629）
- 路由盲测记录：`60_feedback/diagnosis/盲测_20260903_research-routing-four-types.md`
- INDEX 注册：`40_outputs/capabilities/skills/INDEX.md` #49（digging）/ #51（explosion）

**完成内容**
- 爆炸式五步法行为化（P0）：framework-baozhashidiaochan-five-step + R 型五状态机 + 饱和覆盖/单开文档/饱和自证/九字诀行为化；触发词/失败模式/When NOT/反例黑名单齐（任务单要求全覆盖）
- 挖掘式流程行为化（P1）：穷尽手段五层升级+单点狙击三步法+合规红线内置（第五层默认不启用）；When NOT 五拦截（简单查询/紧急决策/成本过高/法律/道德）
- research-core 第一层 A 四类型判定（深→挖掘式/高→系统式/宽→爆炸式/动态→自动式）+ 分型规则四条 + When NOT；不动 OSCAR 武器库路由，互补防路由分裂（裁定动作 3 口径落实）
- 三写一致：SKILL.md frontmatter / manifest.yaml / INDEX.md 三面 description+trigger 同源
- 路由盲测 8/8 通过（建议书 §五验收口径：仅凭 description 判定，含 When NOT 拦截与反触发用例）
- 本实例（06:12 接手）仅做核验收尾：前实例 04:42 claim 后死于机械步骤前、内容已齐（其日志明确「无内容判断遗留」）——本实例不重做内容，只做四项核验（目录完整性/三写一致/INDEX/入仓状态）+ 本报告补录 + complete 提审

**验证**（分层声明：L1 机械 / L2 狗粮 / L3 活体）
- L1 机械：两 skill 目录实测 `ls` 各含 SKILL.md+manifest.yaml 2 文件；frontmatter 必填字段齐，author=老顽童/status=draft/reviewed_by=待审（写审分离，不自标 reviewed）；三写一致实测对照（frontmatter / manifest / INDEX 三面同源命中）
- L2 狗粮：路由盲测 8/8（盲测记录落盘于 60_feedback/diagnosis/，方法=模拟新会话仅读 description）；research-core 第一层判定表 grep 实测命中（v1.1.0：四类型表+分型规则+When NOT 全在）
- L3 活体：入仓实测 `git log`（vault backup e7e617b77 04:55:43 含全部交付物路径）+ `git status` 四路径零脏文件 + INDEX.md #49/#51 行实测命中
- 注：盲测 8 用例为前实例 05:1x 生产自测落盘，本实例核验其记录存在性与口径合规，未复跑（内容不重做原则）

**边界**
- 两 skill status=draft / reviewed_by=待审：未经欧阳锋终审，不自行转正
- darwin-skill 9 维门禁+挂载验收归 skills-assistant 本职（裁定动作 5），本单不代跑
- 盲测遗留观察项（不阻塞）：#2 类请求用户未说「必须拿到」时靠 description 场景词兜底，挂载后建议 skills-assistant 在使用检查留意命中率
- 自动式线未动 CI 框架本体（边界条款），仅入判定层路由行；30_wiki 卡未重写（产 skill 不产卡）

**需要谁动作**
- 欧阳锋：终审本单（2 skill + core diff + 盲测记录）
- skills-assistant：终审通过后过 darwin-skill 9 维门禁 + INDEX 挂载
- 黄药师：无需动作（INDEX 已由 scan_skills_registry 刷新）

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 2 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）
