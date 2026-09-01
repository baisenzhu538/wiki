---
id: '588'
title: Skill目录与挂载矩阵机制——扫描生成+登记制（Skills助理基建配套）
type: infrastructure
status: in_progress
priority: P1
assignee: 黄药师
created_by: 王语嫣
created_at: 2026-09-01
updated_at: '2026-09-01T02:37:25.367632+00:00'
source_refs:
- 40_outputs/capabilities/skills/shared/
instance: huangyaoshi
---

# #588 Skill 目录与挂载矩阵机制（老朱 09-01 直令，#587 配套基建）

## 现状缺口（王语嫣盘点实证）

- 73 个 shared skill 无统一目录：其他 agent「不知道有什么可挂载」
- agent-spec 无「已挂载skills」标准节：谁挂了什么全黑箱，重复挂载/漏挂无对账

## 交付物

1. **扫描脚本**：遍历 `40_outputs/capabilities/skills/shared/*/`，从 SKILL.md frontmatter 提取 name/description/trigger.natural_language/adapted_from → 生成 `40_outputs/capabilities/skills/INDEX.md`（目录菜单：名称/一句话/触发词/来源卡）
2. **挂载矩阵**：扫描 `agents/*/CLAUDE.md` + `30_wiki/agent-specs/*.md` 的 skills 引用 → 生成 `40_outputs/capabilities/skills/MOUNT-MATRIX.md`（agent×skill 对照表，标出：已挂载/可挂载未挂/无主skill）
3. **spec 模板增补**：agent 出生模板（#326 机制）加「已挂载skills」节标准
4. **增量更新钩子**：新 skill 注册/新 agent 部署时目录与矩阵自动刷新（或纳入健康巡检 #326 巡检项）

## 验收标准

- INDEX.md 覆盖 73/73，字段齐全可检索
- MOUNT-MATRIX.md 出全厂 agent 挂载现状（含「可挂未挂」清单≥1 份 actionable）
- 增量机制可演示（新增一个测试 skill → 目录自动出现）

## 执行报告

**交付物**：4 项——
1. `40_outputs/code/scripts/scan_skills_registry.py`（扫描脚本，INDEX+MOUNT 一体生成，`--check` 新鲜度门禁）
2. `40_outputs/capabilities/skills/INDEX.md`（73/73 全覆盖：名称/一句话/触发词/来源卡/位置/已挂载单元 六列 + 待补登记缺口清单）
3. `40_outputs/capabilities/skills/MOUNT-MATRIX.md`（26 挂载单元×73 skill：单元清单表 + 状态三档对照表 + 可挂未挂 actionable 清单 + 挂载纪律节）
4. spec 模板增补 + 增量钩子（见下）

**完成内容**：①扫描 shared/+根目录全部 skill 目录，frontmatter（yaml.safe_load，BOM 兼容 utf-8-sig）+manifest.yaml 双源提取 name/description/trigger.natural_language/adapted_from/author；②挂载判定=登记制「文件引用即挂载」，扫三类登记处——role-routes.md 路由2（六角色）+30_wiki/agent-specs/*.md（9 份）+agents/*/CLAUDE.md/AGENTS.md/SPEC.md/SOUL.md（14 实例），状态三档：已挂载 31/单点 1/无主 41（无主+单点=可挂未挂清单，含关键词启发式归属建议）；③agent 出生模板增补：workflow-kdo-agent-production-pipeline Step 1 加「已挂载skills」标准节（格式+INDEX 注册前置+三写一致），Step 2 加「Skills 挂载=固定动作」部署三步；④增量钩子：脚本幂等重跑即刷新 + `--check` 新鲜度门禁（mtime 对比+计数漂移双检）+ 挂 health-check.py 第 20 项检查（自动巡检）+ infra-status.py 资产行 + infrastructure-inventory.md 巡检族登记。终审记档两小项施工对齐：①SPEC L99 mount-matrix.md→MOUNT-MATRIX.md 统一大写命名（已改+注明）②数量口径实测裁定：73 个 skill 目录（验收「73/73」成立；「74」=ls 含 README.md 的口径差，INDEX 生成行数=73 亲验）。

**验证**：①`python 40_outputs/code/scripts/scan_skills_registry.py` → INDEX 73 skills + MOUNT 26 挂载单元，输出亲跑；②`--check` → `🟢 fresh：73 skills，INDEX/MOUNT 与源一致`；③增量钩子演示：造 `_test-588-hook` 测试 skill → `--check` 报 `🔴 stale` exit=1 → 重跑自动收录 74（INDEX 行+矩阵无主清单+归属建议齐）→ 删除后重跑恢复 73 fresh；④health-check 集成 → `[PASS] Skill 目录+挂载矩阵新鲜度（#588）🟢 fresh：73 skills`（20 项检查含本项）；⑤INDEX 描述列空值=0（BOM 修复后全 73 有 description）；⑥frontmatter name≠目录名仅 2 个（content-production-polish→Vikki-human-speech、knowledge-collision→knowledge-collision-workflow），INDEX 已标注进缺口清单。

**边界**：①挂载=「登记面引用」非「运行时可用性」实证——矩阵头部已声明，运行时实证属 #326 MCP 巡检同族后续；②无主 41 个的归属裁定+单点 1 个（deep-debug）推广挂载=内容维护，归 Skills 助理（#587 分工表），本单只出 actionable 清单与建议；③trigger.natural_language 71 个缺失的补登记=Skills 助理维护面（INDEX 缺口清单已列，补后重跑脚本即刷新）；④部署落地（新 agent 出生跑 Skills 挂载固定动作）待下一个部署单按 workflow 增补段执行。

**需要谁动作**：欧阳锋——按基建单终审本交付（重点：MOUNT-MATRIX 状态三档口径、可挂未挂清单 actionable 性、health-check 挂接）。Skills 助理（部署后）——按 INDEX 缺口清单补 trigger/来源卡登记、无主 41 个归属裁定。
