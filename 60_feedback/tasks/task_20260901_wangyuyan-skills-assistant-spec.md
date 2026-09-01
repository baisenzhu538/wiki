---
id: '587'
title: Skills助理Agent spec——Skill生产+配置中枢（工厂第7角色）
type: spec
status: in_progress
priority: P1
assignee: 王语嫣
created_by: 王语嫣
created_at: 2026-09-01
updated_at: '2026-09-01T01:22:51.013843+00:00'
source_refs:
- 30_wiki/workflows/workflow-kdo-agent-production-pipeline.md
- agents/research-explosion-partner/SPEC.md
instance: wangyuyan
---

# #587 Skills 助理 Agent spec（老朱 09-01 直令）

## 定位（老朱原话锚定）

「我要的 skills 助理是专门生产和配置 skills 的」——不是点菜员，是工厂 Skill 生产+配置中枢。爆炸式建模助理=流水线产 agent 的先例；本角色=流水线产 skill 的同构位。

## 理论根基（王语嫣已深挖，锚点卡）

- framework-AI知识库-五阶段演进：阶段4数字员工=Skill封装+岗位制；阶段5「全面打开让AIGC协作」
- framework-dual-center-feishu-obsidian：飞书给人、Obsidian给AI——飞书Agent是阶段4入口层（远期，本单不做）
- case-truman-ai-skill-self-packaging：楚门 skill 自封装全流程实证

## spec 必答六问（按 Agent 生产流水线标准）

1. **触发条件**：什么卡值得行为化成 skill？（候选标准：欧阳锋终审出口判断「工具类/被≥2任务引用/老朱直令」三选一触发入队）
2. **生产行为化流程**：30_wiki 卡 → SKILL.md + manifest.yaml（trigger.natural_language 必填，参照 anti-ai-bs-three-moves 先例）→ 注册 shared/
3. **目录服务**：skill 目录菜单自动维护（配合 #588 黄药师扫描机制）
4. **挂载配置**：agent-spec「已挂载skills」节标准 + 全局 agent×skill 矩阵维护
5. **边界**：不产知识卡（那是老顽童）、不终审（欧阳锋）、不做飞书壳（远期另立项）
6. **基线用例**：≥3 个（含一个存量工具卡行为化实例）

## 验收标准

- SPEC.md 落 `agents/skills-assistant/SPEC.md`，走 #335 同款终审
- 基线用例 3 个可复跑
- 与 #588 黄药师机制的接口定义清楚（谁扫描、谁登记、谁维护）

## 执行报告

**交付物**：`agents/skills-assistant/SPEC.md`（新建，134 行，十节全齐+基线用例 3 个）。

**完成内容**：Skills 助理（工厂第 7 角色）SPEC 定稿——角色定位/三源理论根基（Truman 四步封装法口述稿 L335-L475+Anthropic 官方范式+KDO #335 先例三源交叉）/触发条件三选一/卡→skill 四阶段流程/与 #588 的目录服务接口分工（谁扫描/谁登记/谁维护均落定）/挂载配置三写一致/When NOT 边界五条/基线用例 U1-U3。

**验证**：`grep -c "^## " agents/skills-assistant/SPEC.md` → 10（十节全齐）；与 #588 接口分工表逐项对应 #588 交付面（扫描脚本+目录生成+spec 模板增补「已挂载skills」节）；基线用例 3 个均有库内实卡背书（九字诀卡族/#586 method-anthropic-skill-design-patterns/deep-debug skill）；source_refs 三源路径实存。

**边界**：U1-U3 为部署验收用例（本单只定义不实跑，部署另立项走流水线）；agent-spec 模板增补「已挂载skills」节落点在 #588（黄药师）；73 存量 skill 目录生成属 #588 扫描脚本职责，本 SPEC 只定格式。

**需要谁动作**：欧阳锋——按 #335 同款标准终审本 SPEC（终审 PASS 后 #588 依赖解除，黄药师可开工）。
