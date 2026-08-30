---
id: 575
assignee: laowantong
status: in_progress
updated_at: '2026-08-30T05:31:05.774877+00:00'
version: v0.1
instance: laowantong
---

# #575 OpenClaw vs Harness 选型决策树卡

- **任务号**：#575 ｜ **状态**：queued ｜ **assignee**：老顽童（欧阳锋终审）｜ **优先级**：P1
- **立项**：2026-08-30 王语嫣编排（诊断 `diag_20260830_战略笃定篇`，老朱拍板）

## 背景

老朱核心问题："到底什么情况下用 OpenClaw、什么情况下用 Harness？" Truman 在口述稿里反复讲但散落多处，知识库已有 `tool-ai-agent-feature-comparison` 只覆盖 Claude/Hermes/Codex/CodeBuddy，缺 OpenClaw + Harness + "项目制/Agent 级/工作台"三分法。

## 任务

产出 `framework-openclaw-vs-harness-selection` 选型决策树卡，必须含：

1. **70% 论**（Truman 原话："CodeX/WorkBody/龙虾/Hermes/Harness 这套 70% Feature 一样，每个有额外 10-30 个差异化 Feature"）
2. **三分法决策树**：OpenClaw=养员工（长期记忆/角色身份/主动/陪伴进化）｜Harness=造工具（组件化/插件可改/跨平台/多机部署，"Everything is a Plugin"）｜Codex/Claude Code=打短工（一次性 Session）
3. **触发场景表**（每类 2-3 个具体场景 + 1 个反例）
4. **KDO 映射**：六角色=Hermes（≈OpenClaw 层），pipeline/门禁/脚本可 Harness 化

## 素材锚点

- 口述稿 66000-77616（Harness 详述："把个人定制 Harness 工作台门槛打掉""组件化连官方都组件化"）+ 第七轮（OpenClaw：灵魂赋能/10 角色硅基团队）
- 外部调研：GitHub `deepseek-ai/deepseek-harness`（"Everything is a Plugin"）、`garrytan/gbrain`（"OpenClaw/Hermes Agent Brain"——OpenClaw 与 Hermes 同类）
- 已有卡：`tool-ai-agent-feature-comparison`（四工具 Feature 表，复用其表格结构）

## 验证

- 选型树能一句回答"什么情况用 OpenClaw / 什么情况用 Harness"，含触发场景 + 反例
- 与 `tool-ai-agent-feature-comparison` 不重复（本卡=三分法决策视角，该卡=逐工具 Feature 明细）

## 边界

- 不重写 `tool-ai-agent-feature-comparison`（那是 #576 黄药师的活），本卡只出"选型决策树"框架卡
- 不涉及 Harness 实跑验证（老朱自己在手操验证中）

## 建模方案（老顽童出牌，2026-08-30）

出牌链：`[素材牌#3 先口述稿再笔记] → [边界牌#6 先查已有卡再新建] → [边界牌#7 先对标准则再命名] → [结构牌#8 先定总纲再子卡] → [结构牌#10 先骨架再填肉] → [质量牌#16 先lint再pre-submit] → [质量牌#15 先自攻击再提交]`

- 素材牌#3：口述稿 1870 行全文已逐字读完（含末尾闲聊 L1536-1870），素材消费率目标 ≥80%
- 边界牌#6：已有 `tool-ai-agent-feature-comparison`（#576 黄药师已完成补全 OpenClaw/Harness 两列+三分法总纲）——本卡只做**选型决策树视角**增量，逐工具 Feature 明细归该卡，不重写
- 边界牌#7：DeepSeek Harness 无公开网源（已 WebSearch 验证），以 Truman 口述 + 老朱一手体感 + 王语嫣编排为准；外部参考 GitHub `deepseek-ai/deepseek-harness`（Everything is a Plugin）已在 #576 卡记录
- 结构牌#8：本卡属于 [[framework-truman-feature-thinking-core]] 的应用层选型卡（定位声明 O8）
- 结构牌#10：framework 四节完整性——When NOT to Use / 失败模式 / Action Triggers / Critique
- 质量牌#16/#15：kdo pre-submit 门禁 + 四路自攻击

## 需要谁动作

- **老顽童**：生产 `framework-openclaw-vs-harness-selection`
- **欧阳锋**：终审

## 执行报告

**交付物**：
- `30_wiki/frameworks/framework-openclaw-vs-harness-selection.md`（新建 framework 卡，正文 258 行）
- `60_feedback/adversarial/atk_framework-openclaw-vs-harness-selection_20260830.md`（自攻击报告）

**完成内容**：OpenClaw vs Harness 选型决策树框架卡——70% 论（Truman 原话 L1716-1718）+ 三分法决策树（打短工/养员工/造工具，含 Q1-Q4 判断节点）+ 触发场景表（每类 4 场景 + 1 反例）+ KDO 映射（六角色=Hermes 养员工层，pipeline/门禁可 Harness 化）+ When NOT to Use×5 + 失败模式×6（症状+修复）+ Action Triggers×4 + Critique（内部局限×3 + 外部攻击者×3 不同范式）+ Synthesis 关联×7。复用 tool-ai-agent-feature-comparison 表格结构但本卡专注决策树视角，未重写该卡（related 双向互链）。

**验证**：`kdo pre-submit -f 30_wiki/frameworks/framework-openclaw-vs-harness-selection.md` → ✅ PASS 1/1（WARNING×1：CONCEPT_CROSSCHECK 提示制不拦截，人工核对决策树/硅基组织行为学/Truman/一号位与权威定义一致）；`kdo index --incremental` → +0 ~1（4281 总数）；自攻击四路 0🔴 1🟡（混合场景已知边界，卡内已覆盖）3🟢。

**边界**：70% / 10-30 个差异化 Feature 为 Truman 口述估计（数字待独立核实，卡内已标注）；DeepSeek Harness 为 2026-08 新工具、老朱手操验证中，实跑定论待补充（卡内已标注，trust_level medium）；WebSearch 确认 DeepSeek Harness 无公开网源，术语以口述+编排为准。
