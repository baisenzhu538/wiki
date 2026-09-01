---
id: '594'
title: 调研能力层整合——17 skill 综合深挖为全 agent 基础能力（Skills助理生产首单）
type: skill-production
status: in_progress
priority: P1
assignee: skills-assistant
created_by: 王语嫣
created_at: 2026-09-02
source_refs:
- 40_outputs/capabilities/skills/shared/research/SKILL.md
- 40_outputs/capabilities/skills/shared/research-multi-agent/SKILL.md
- 40_outputs/capabilities/skills/shared/nine-layer-deep-dig/SKILL.md
- 60_feedback/tasks/task_20260901_huangyaoshi-skills-assistant-deploy.md
instance: skills-assistant
updated_at: '2026-09-01T14:32:10.533569+00:00'
---

# #594 调研能力层整合（Skills助理生产首单）

## 背景

老朱 09-02 拍板：「深度调研的 skills 是不是可以整合下，综合深挖，以后的任何 agent，调研能力其实是最基础的必备能力。」——调研能力定位从「王语嫣专用工具」升格为**全 agent 基础能力层**（任何 agent 生产的必备底座，类比：会读写的 agent 才能上岗）。

现状实测（09-02 编排层盘点）：
- 调研能力簇 17 个 skill：research 入口 + 13 个 research-* 子策略 + 3 个近亲（six-layer-cross-validation / knowledge-collision / nine-layer-deep-dig）
- 挂载面：仅王语嫣角色路由挂 2 个（knowledge-collision / research-cross-validation / research-expert-interview），**其余全部无主**（MOUNT-MATRIX 09-01 版：无主 skill 43 个，调研族为最大族）
- research 入口 skill 已有 OSCAR 意图分类路由骨架，但子策略靠人工记忆调用，无统一分层结构

## 任务（Skills助理 SPEC §四 P1-P4 全流程）

### 1. P1 行为化评审（17→分层结构，产出判定书）

对 17 个 skill 逐一评审，产出**三层结构**整合方案：

```
research-core（新产：统一入口层）
├── 第一层 意图路由：OSCAR 分类 → 判断调用哪类子能力（吸收现 research 入口）
├── 第二层 核心纪律（所有调研必经）：
│   ├── 交叉验证（research-cross-validation + six-layer 合并判定）
│   ├── 质量门禁（research-quality-gate）
│   └── 深挖引擎（nine-layer-deep-dig + research-sats 合并判定）
└── 第三层 专项武器库（按需载入，渐进式披露第三层）：
    行业报告/财报/专家访谈/替代数据/OSINT/爬虫/Dorking/媒体验证/多Agent/CI情报
```

- 合并判定原则：功能重叠（如 cross-validation 与 six-layer）→ 合并为单卡双源；独立场景 → 保留独立武器
- 明确反触发：非调研任务（纯写卡/纯施工）不得路由进本层

### 2. P2 SKILL.md 生产

- 新产 `research-core` 入口 skill（含三层路由+基础纪律，对齐 SPEC 渐进式披露三层）
- 改造 `research` 入口为 research-core 的薄壳或直接合并（P1 判定）
- 子策略 skill 只改 frontmatter（description 对齐路由面），正文不大动

### 3. P3 质量门禁

- 路由面盲测：3 个独立请求（「调研某行业」「验证某断言」「深挖某问题」）仅凭 description 正确路由到正确层
- `kdo pre-submit -f` 0 ERROR
- 自攻击一轮：没读过任何子卡的 agent 拿到 research-core 能否独立完成一次基础调研？

### 4. P4 注册挂载（本单核心交付——消灭无主状态）

- research-core 挂载到**全部 agent spec「已挂载skills」节**（基础能力层语义：全员必挂）
- 七角色（老顽童/欧阳锋/黄药师/风清扬/王语嫣/skills-assistant/洪七公段王爷按岗位判定）+ agents 实例逐个登记
- 挂载变更 manifest changelog 留痕，三写一致（spec 节/MOUNT-MATRIX/manifest）
- 重跑 scan_skills_registry.py 刷新矩阵

## 验收标准

1. 三层结构判定书在案（17 个 skill 每个有归属：core/纪律层/武器库/明确不并入）
2. research-core 通过路由面盲测 3/3
3. 全部 agent spec「已挂载skills」节含 research-core；MOUNT-MATRIX 无主调研 skill 清零或标注保留理由
4. 三写一致抽查 2 个 agent 通过

## 边界

- ❌ 不改子策略 skill 正文内容（只动入口+frontmatter）
- ❌ 不碰 wiki 卡（30_wiki 归老顽童）
- ❌ 不做新调研策略 skill（武器库已够，本单只整合不扩军）
- 飞书壳/IM 入口不在本单范围

## 执行报告

**交付物**：`40_outputs/capabilities/skills/shared/research-core/`（SKILL.md 195 行三层统一入口 + manifest.yaml + JUDGEMENT.md 三层判定书）+ `shared/research/SKILL.md` 薄壳化重定向（v1.1.0，原 90 行 OSCAR 路由并入 research-core，保 KDO 工具链指针）+ 16 个子 skill frontmatter description 加【research-core 纪律层/武器库/前置纪律】路由前缀 + 全部 10 个 agent-spec「已挂载skills」节与 11 个 agents 实例登记 research-core + INDEX/MOUNT-MATRIX 重扫刷新。

**完成内容**：#594 调研能力层整合四阶段全走完——P1：17 skill（14 research 系+3 近亲）逐一评审归属（纪律层双源合并 2 组：cross-validation×2、deep-dig+SATs；武器库 10 个独立保留；knowledge-collision 判通用前置纪律独立不并入）；P2：research-core 三层结构（OSCAR 意图路由→核心纪律三卡最小自包含版→武器库按需载）+ 硬约束段（防捏造铁律/信源时效 30天-12个月——自攻击发现丢失后补回）+ KDO 工具链段（research_adapter 三命令——自攻击发现丢失后补回）；P3：路由面盲测 5/5（含 2 反触发探针；首测抓到 T2「验证说法」直路由纪律层缺陷，修 description 补验证类触发词后复测全过）+ `kdo pre-submit -f` research-core 与 research 双 PASS（首查 FAIL 因缺 status/reviewed_by，按库内先例补 `status: enriched / reviewed_by: 待审` 诚实值）+ 自攻击一轮（白纸 agent 走查，2 个能力缺口已修）；P4：research-core 挂载全部 10 个 agent-spec + 11 个 agents 实例（21 挂载单元全员覆盖，基础能力层语义），重跑 scan_skills_registry 矩阵刷新 🟢 fresh（76 skills，无主 43→31——调研族 12 个全部脱无主），三写一致抽查 2/2（zhu-boss 纯新挂、ouyangfeng 含既有 skill 混挂均通过）。

**验证**：路由盲测机械匹配脚本 5/5 PASS（T1 行业调研/T2 断言验证/T3 深挖均首位命中 research-core，T4 写卡/T5 施工正确不路由）；`kdo pre-submit -f` research-core 与 research 均 ✅ PASS 0 ERROR；`scan_skills_registry.py --check` 🟢 fresh；MOUNT-MATRIX 实测 research-core 已挂载单元=21（10 spec+11 实例），无主计数 31（原 43-12 调研族）；三写一致抽查① agent-spec-zhu-boss（1 处引用+矩阵行一致）② agent-spec-ouyangfeng-reviewer（3 skill 混挂+矩阵行一致），manifest changelog 已留痕。

**边界**：16 个子 skill 仅动 description 一行（任务单边界合规），其老卡普遍缺 status/reviewed_by/updated_at 字段（pre-submit 报 3 ERROR 为 HEAD 既有状态非本单引入，stash 对照实证）——批量补字段超本单范围，留作全厂 skill 字段补齐任务建议；role-routes.md 路由2 表未动（owner=王语嫣编排，本单只登记 spec 层+实例层）；不扩军（未新增调研策略 skill）；飞书壳/IM 入口不在范围。

**需要谁动作**：欧阳锋——终审 #594（research-core 内容+三层判定书+挂载配置）；王语嫣——同步编排视图（挂载矩阵变更知会），并裁定遗留项「全厂 skill frontmatter 字段补齐」是否立项；黄药师——知会基建视图（MOUNT-MATRIX 已刷新，无主 43→31）。
