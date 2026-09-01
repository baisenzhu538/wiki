---
id: '593'
title: Skills助理Agent部署——U1-U3实跑验收（两阶段第二阶段）
type: deploy
status: reviewed
priority: P1
assignee: 黄药师
created_by: 王语嫣
created_at: 2026-09-01
source_refs:
- agents/skills-assistant/SPEC.md
- 60_feedback/tasks/task_20260901_wangyuyan-skills-assistant-spec.md
- 60_feedback/tasks/task_20260901_huangyaoshi-skill-registry-mount-matrix.md
instance: huangyaoshi
updated_at: '2026-09-01T07:09:11.792621+00:00'
evidence: 60_feedback/tasks/task_20260901_huangyaoshi-skills-assistant-deploy.md
reviewed_by: 欧阳锋
review_date: '2026-09-01'
grade: A
---

# #593 Skills 助理 Agent 部署（#587 终审指令：编排层立项，带两阶段口径）

## 背景

#587 SPEC 已欧阳锋终审 PASS A（2026-09-01），终审指令「**部署另立项，编排层处理部署单排期**；部署验收单须把 U1-U3 实跑作为验收门」。#588 挂载矩阵已 PASS A-（扫描脚本/INDEX/MOUNT-MATRIX/spec 模板增补全交付），前置依赖全清。源头=老朱 09-01 直令：「我要的 skills 助理是专门生产和配置 skills 的」（工厂第 7 角色=Skill 生产+配置中枢）。

## 任务（SPEC 两阶段流程·第二阶段：部署验收）

1. 按 `agents/skills-assistant/SPEC.md` 建 agent 实体部署面（比照 #303/#304 三件套部署先例：SOUL/config/profile 注册+cap_hub 登记）；挂载配置遵 SPEC 第六节：默认 shared 全员可见+专属标 `scope: <角色>`+挂载变更 manifest changelog 留痕
2. 施工对齐 #587 终审记档小项：mount-matrix 大小写统一（随 INDEX.md/MOUNT-MATRIX.md 大写惯例，一行对齐）
3. **U1-U3 实跑验收（=验收门，逐条必过）**：
   - U1 存量工具卡行为化：`30_wiki/tools/` 九字诀卡族候选→P1-P4 全流程→另一 agent 仅凭 description 正确决定用/不用
   - U2 新卡行为化：`method-anthropic-skill-design-patterns`（#586 产）→行为化 skill→与 `tool-ai-skill-engineering-guide` 互链不撞车
   - U3 配置流：deep-debug skill 挂载到指定 agent spec「已挂载skills」节→矩阵更新→changelog 留痕（三写一致）
4. 执行报告五字段提审

## 验证

- U1-U3 三用例逐条实跑留痕（SPEC 第八节验证点全命中）
- `python 40_outputs/code/scripts/scan_skills_registry.py` 重跑矩阵刷新正常（shared 计数以扫描实测为准，#587 终审实测 74）
- 路由面自检：skill 注册后可被其他 agent 按 description 正确路由

## 边界

- ❌ 不含飞书壳/IM 入口（SPEC 边界第三条：远期另立项，老朱拍板后才启动）
- ❌ U1/U2 产出的 skill 内容本身仍走欧阳锋终审，部署单验收口径=流程走通+用例通过
- agent-spec 模板「已挂载skills」节 #588 已落，本单不重复改模板

## 关联

- #587 SPEC（PASS A，两阶段第一阶段已闭环）
- #588 挂载矩阵（PASS A-，依赖已解除）
- #335 研究伙伴部署先例同构

## 需要谁动作

黄药师——按 SPEC 第九节两阶段口径执行部署+U1-U3 实跑，完成后执行报告五字段提审，欧阳锋终审。


## 执行报告（2026-09-01 黄药师）

**交付物**：部署面 8 项——
1. `agents/skills-assistant/SOUL.md` + `CLAUDE.md`（三件套部署件，认知件含 KDO 知识地图+P1-P4 工作流内嵌；SPEC.md #587 已在）
2. Hermes profile `skills-assistant`：现行数据根 `~/AppData/Local/hermes/profiles/skills-assistant/`（config.yaml 含 kdo MCP+cwd=wiki、SOUL.md 同源复制，`hermes profile create` 注册）+ `C:/Users/Administrator/.hermes/profiles/skills-assistant/` 旧树同款（两处对齐）
3. MCP 挂载：`kdo-tools/sync-hermes-mcp.py` WINDOWS_PROFILES +`skills-assistant` → `--apply` 渲染分发（备份自动）；`90_control/scripts/check-mcp-roaming.py` 名单同步扩展
4. `30_wiki/agent-specs/agent-spec-skills-assistant.md`（cap_hub 可发现副本，#303 先例同构；单一真相源指针回 SPEC.md）→ `python -m cap_hub list` 已可见
5. `cap_hub/agent-registration-norm.md` 已注册 Agent 表 +skills-assistant（active，2026-09-01）
6. U1 skill：`40_outputs/capabilities/skills/shared/nine-character-ai-collaboration/`（SKILL.md+manifest.yaml）
7. U2 skill：`40_outputs/capabilities/skills/shared/skill-architecture-design/`（SKILL.md+manifest.yaml）
8. U3 配置流三写：`30_wiki/agent-specs/agent-spec-huangyaoshi-builder.md` 增「已挂载skills」标准节（deep-debug 等 4 项）+ `40_outputs/capabilities/skills/shared/deep-debug/manifest.yaml` 补建（trigger.natural_language+changelog 留痕）+ `INDEX.md`/`MOUNT-MATRIX.md` 重跑刷新（生成物，75 skills/27 单元，🟢 fresh）

**完成内容**：#593 部署+验收全闭环——①部署面按 #303/#304/#335 先例：三件套+profile+kdo MCP+cap_hub 登记四件齐；②#587 终审记档小项（mount-matrix 大小写）验证已清（SPEC 现文=MOUNT-MATRIX.md 大写+注明，全库小写引用零残余，无需再改）；③U1 九字诀卡 P1-P4 全流程（判定 Go→四步封装→pre-submit PASS→注册收录）；④U2 method-anthropic-skill-design-patterns 行为化（设计向）与 tool-ai-skill-engineering-guide（流程向）互链不撞车；⑤U3 deep-debug 挂载三写一致（单点挂载→已挂载，builder-spec 3→4）；⑥真机冒烟：`hermes --profile skills-assistant -z` 实例准确自报第 7 角色身份。

**验证**：分层留痕——
- A 部署面实测：`sync-hermes-mcp.py --apply` 渲染成功（config 含 mcp_servers.kdo）；`check-mcp-roaming.py` → `[OK] windows/skills-assistant: mcp_servers.kdo 已挂`（exit=2 系既有未部署 profile 的 WARN 语义，非本次回归）；`cap_hub list` → `📦 agent-spec-skills-assistant` 可见；真机冒烟自报身份全对（第 7 角色/P1-P4/三写一致/欧阳锋终审）
- B 结构校验：`kdo pre-submit -f` 两个新 SKILL.md 均 ✅ PASS（U1 首轮 4 错误→补 title/status/reviewed_by/updated_at/tags 后过）；3 份 manifest.yaml `yaml.safe_load` 全 dict+name/trigger/changelog 齐；spec 副本 source_refs 存在性核过（`00_inbox/AI知识库/…逐字稿.md` 在位）
- C U1 路由面：独立 hermes 实例仅凭 description 判 5 请求 → 5/5（3 use 2 skip，理由命中触发场景，非关键词自测）
- D U2 互链路由：独立实例凭两条 description 分诊 4 请求 → 4/4（架构→本 skill/封装流程→工程指南/description→本 skill/转格式→都不用）
- E U3 三写一致：spec 节 4 行=manifest 适用agent+changelog=MOUNT-MATRIX `deep-debug 已挂载（3 单元）`+builder 行 3→4；`scan_skills_registry.py --check` → 🟢 fresh：75 skills（=#587 实测 74−README 口径差 73+本单新增 2）；顺带修复 spec 副本 domain 值 `ai-collaboration` 与同名 skill 目录的 token 碰撞（曾伪升「单点挂载」，改 agent-capability 后单点归零=真实语义）
- F 外部锚点 L1：U1 用 promptingguide.ai 技术目录+Microsoft Learn 提示工程（curl 实测命中）；U2 用 Anthropic 官方 skills 工程博客（实测命中，渐进式披露原文）；Anthropic docs 域地区屏蔽已留痕绕行

**未做项**：①飞书壳/IM 入口不做（SPEC 边界③，远期老朱拍板另立项）——profile 未配 feishu 平台块，即边界执行；②U1/U2 产出的 skill **内容本身**归欧阳锋终审（reviewed_by: pending），本单验收口径=流程走通+用例通过（任务单边界第二条）；③发现的基建漂移不在本单修：sync/check 脚本 profile 常量指向 `.hermes` 旧树而现行数据根=AppData（实证：巡检报 `[MISS] windows/wangyuyan` 而该 profile 实际在跑）——本单已双树对齐保可用，根治（脚本常量迁移）需编排另立项；④`kdo lint` 全量跑 300s 超时（#588 终审记档②同族已知）→ 改用交付标准 B 同款 yaml.safe_load 校验等价覆盖；⑤`--apply` 时 wangyuyan 滞后 kdo 子节被顺带刷新（模板驱动全量更新语义，有 .bak 备份，如实留痕）；⑥`.hermes`/AppData 侧 profile 文件在 vault 仓外，无法随本单 commit。

**需要谁动作**：欧阳锋——终审本单（重点：U1/U2 两个新 skill 的内容质量、U3 三写一致性、路由实测 A-D 复跑）；王语嫣——知会挂载变更（编排视图）+③脚本常量漂移是否立项裁量。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 7 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）

## 终审记录（2026-09-01 欧阳锋）

**结论：PASS A**（独立复跑 14 项全过，声称-交付零差集）

### 验收对照（欧阳锋独立复跑，非采信执行报告）

| # | 验收标准 | 独立复跑动作 | 实测 | 判定 |
|:--|:--|:--|:--|:--|
| 1 | 部署三件套实存 | ls agents/skills-assistant/ + 两处 profile 树 | SOUL(5933B)/CLAUDE(1980B)/SPEC 在位；AppData config.yaml 含 mcp_servers.kdo+cwd=wiki；旧树同款+.bak 备份 | ✅ |
| 2 | MCP 挂载实测 | python 90_control/scripts/check-mcp-roaming.py | `[OK] windows/skills-assistant: mcp_servers.kdo 已挂`（exit=2 系既有未部署 profile WARN 语义，与报告口径一致） | ✅ |
| 3 | cap_hub 登记 | grep agent-registration-norm.md | L55 行 skills-assistant active 2026-09-01 在案 | ✅ |
| 4 | 真机冒烟 | `hermes -z --profile skills-assistant` 亲跑 | 自报「第 7 号角色 / P1-P4 四阶段 / spec 节+MOUNT-MATRIX+manifest 三写一致」逐字命中 | ✅ |
| 5 | U1 存量卡行为化 | 读 SKILL.md 全文（88 行） | 六节齐（触发条件含**不触发**反例/操作步骤/失败模式表/适用边界/Action Triggers/来源）+src_unknown=0+adapted_from 指实存来源卡 | ✅ |
| 6 | U2 互链不撞车 | 读 SKILL.md 全文（101 行）+来源卡存在性 | 与 tool-ai-skill-engineering-guide 分工声明在文内（设计向 vs 流程向）；method-anthropic-skill-design-patterns 实存 | ✅ |
| 7 | 路由面盲测 | 独立实例 4 请求仅凭两 description 判断 | 4/4（2 use 2 skip），理由命中触发场景非关键词匹配 | ✅ |
| 8 | U3 三写一致 | 三面并读 | builder spec「已挂载skills」L126-131（deep-debug 4 项，注明 #593）= manifest 适用agent 2 项+changelog 留痕 = MOUNT-MATRIX L12(builder=4)/L51(已挂载，3 单元) 互洽 | ✅ |
| 9 | 矩阵刷新 | scan_skills_registry.py --check 亲跑 | 🟢 fresh 75 skills，INDEX/MOUNT 与源一致；两个新 skill INDEX L49/L60 已收录 | ✅ |
| 10 | mount-matrix 大小写统一 | grep 施工面（SPEC/INDEX/MATRIX/agent-specs） | 全大写；小写命中仅在 todos 流水历史（不回改纪律，非施工面） | ✅ |
| 11 | E040 交付物入仓 | git ls-files + git status --porcelain | 5 文件全 tracked、三目录零脏改动、commit 699346811 在案 | ✅ |
| 12 | 版本对齐 | git log 对读 | 提审 14:46 交付=699346811；HEAD 仅多王语嫣时钟划销 3b23d341c，交付物无后续触碰 | ✅ |
| 13 | pre-submit | python -m kdo pre-submit --files 两 SKILL.md 亲跑 | PASS | ✅ |
| 14 | manifest 结构 | yaml.safe_load 三份亲跑 | 全 dict，name/trigger/changelog 齐全 | ✅ |

### 内容面抽验（任务单边界第二条：U1/U2 内容终审归欧阳锋，本轮同场覆盖）

两 SKILL.md 按 P0-P2 抽验达标（触发真实/操作可执行/失败模式带信号/边界清晰/零占位符/来源锚点真实）；`reviewed_by: pending` 按部署口径在本终审同步转正（review_mark），`status: enriched` 维持 skill 包语义。

### 🟡 记档项（均有落点）

| # | 事项 | 落点 |
|:--|:--|:--|
| 🟡1 | 基建漂移：sync-hermes-mcp/check-mcp-roaming 脚本 profile 常量指 `.hermes` 旧树，现行数据根=AppData（实测复现 `[MISS] windows/wangyuyan` 而该 profile 在跑）——本单双树对齐保可用，根治需另立项 | 执行报告未做项③已在案，**待王语嫣裁量立项**（脚本常量迁移） |
| 🟡2 | `--apply` 时 wangyuyan kdo 子节被顺带刷新（模板全量语义，.bak 备份在，如实留痕） | 并入 🟡1 同一立项（`--only` 白名单候选），记档观察 |
| 🟡3 | `kdo lint` 全量 300s 超时 → yaml.safe_load 等价覆盖 | #588 终审记档②同族既有观察项，不新开 |

**存在性核查**（#433 锚点，本记录负向表述核查表）：

| 负向表述 | 核查方法 | 结果 |
|:--|:--|:--|
| 施工面小写「仅在 todos 流水」 | grep -rn "mount-matrix" agents/ 30_wiki/agent-specs/ 90_control/ skills/INDEX/MOUNT-MATRIX | 施工面 0 命中；todos 流水 6 处（历史记录不回改纪律） |
| 工作区「零脏改动」 | git status --porcelain 三交付目录 | 输出为空 |
| U1/U2「src_unknown=0」 | grep -c src_unknown 两 SKILL.md | 0 / 0 |

### 遗留路由

- 🟡1 脚本常量漂移根治 → 王语嫣裁量是否立项（执行报告③在案）
- Skills 助理正式上岗（第 7 角色），候选池入口=欧阳锋终审「建议行为化」标注 + 复用 ≥2 + 老朱直令（SPEC 第三节三选一）；U1-U3 用例通过，两阶段流程全闭环
