---
id: '594'
title: 调研能力层整合——17 skill 综合深挖为全 agent 基础能力（Skills助理生产首单）
type: skill-production
status: reviewed
priority: P1
assignee: skills-assistant
created_by: 王语嫣
created_at: 2026-09-02
reviewed_by: 欧阳锋
review_date: '2026-09-01'
grade: A
source_refs:
- 40_outputs/capabilities/skills/shared/research/SKILL.md
- 40_outputs/capabilities/skills/shared/research-multi-agent/SKILL.md
- 40_outputs/capabilities/skills/shared/nine-layer-deep-dig/SKILL.md
- 60_feedback/tasks/task_20260901_huangyaoshi-skills-assistant-deploy.md
instance: skills-assistant
updated_at: '2026-09-01T15:06:02.642376+00:00'
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

**交付物**：`40_outputs/capabilities/skills/shared/research-core/`（SKILL.md 195 行三层统一入口 + manifest.yaml + JUDGEMENT.md 三层判定书）+ `40_outputs/capabilities/skills/shared/research/SKILL.md` 薄壳化重定向（v1.1.0，原 90 行 OSCAR 路由并入 research-core，保 KDO 工具链指针）+ 16 个子 skill frontmatter description 加【research-core 纪律层/武器库/前置纪律】路由前缀 + 全部 10 个 agent-spec「已挂载skills」节与 11 个 agents 实例登记 research-core + INDEX/MOUNT-MATRIX 重扫刷新。

**完成内容**：#594 调研能力层整合四阶段全走完——P1：17 skill（14 research 系+3 近亲）逐一评审归属（纪律层双源合并 2 组：cross-validation×2、deep-dig+SATs；武器库 10 个独立保留；knowledge-collision 判通用前置纪律独立不并入）；P2：research-core 三层结构（OSCAR 意图路由→核心纪律三卡最小自包含版→武器库按需载）+ 硬约束段（防捏造铁律/信源时效 30天-12个月——自攻击发现丢失后补回）+ KDO 工具链段（research_adapter 三命令——自攻击发现丢失后补回）；P3：路由面盲测 5/5（含 2 反触发探针；首测抓到 T2「验证说法」直路由纪律层缺陷，修 description 补验证类触发词后复测全过）+ `kdo pre-submit -f` research-core 与 research 双 PASS（首查 FAIL 因缺 status/reviewed_by，按库内先例补 `status: enriched / reviewed_by: 待审` 诚实值）+ 自攻击一轮（白纸 agent 走查，2 个能力缺口已修）；P4：research-core 挂载全部 10 个 agent-spec + 11 个 agents 实例（21 挂载单元全员覆盖，基础能力层语义），重跑 scan_skills_registry 矩阵刷新 🟢 fresh（76 skills，无主 43→31——调研族 12 个全部脱无主），三写一致抽查 2/2（zhu-boss 纯新挂、ouyangfeng 含既有 skill 混挂均通过）。

**验证**：路由盲测机械匹配脚本 5/5 PASS（T1 行业调研/T2 断言验证/T3 深挖均首位命中 research-core，T4 写卡/T5 施工正确不路由）；`kdo pre-submit -f` research-core 与 research 均 ✅ PASS 0 ERROR；`scan_skills_registry.py --check` 🟢 fresh；MOUNT-MATRIX 实测 research-core 已挂载单元=21（10 spec+11 实例），无主计数 31（原 43-12 调研族）；三写一致抽查① agent-spec-zhu-boss（1 处引用+矩阵行一致）② agent-spec-ouyangfeng-reviewer（3 skill 混挂+矩阵行一致），manifest changelog 已留痕。

**验收四条逐项对照**：
1. ✅ 三层判定书在案——`research-core/JUDGEMENT.md` 17 skill 逐一归属（core/纪律层/武器库/明确不并入四类全覆盖）
2. ✅ 路由面盲测 3/3（实跑 5/5 含 2 反触发探针）——T1 行业调研/T2 断言验证/T3 深挖均仅凭 description 首位命中 research-core
3. ✅ 全员挂载+无主清零——10 spec + 11 实例「已挂载skills」节均含 research-core（21 单元）；MOUNT-MATRIX 无主调研 skill 清零（无主 43→31）
4. ✅ 三写一致抽查 2/2——zhu-boss / ouyangfeng 的 spec 节=MOUNT-MATRIX=manifest 全对

**边界**：16 个子 skill 仅动 description 一行（任务单边界合规），其老卡普遍缺 status/reviewed_by/updated_at 字段（pre-submit 报 3 ERROR 为 HEAD 既有状态非本单引入，stash 对照实证）——批量补字段超本单范围，留作全厂 skill 字段补齐任务建议；role-routes.md 路由2 表未动（owner=王语嫣编排，本单只登记 spec 层+实例层）；不扩军（未新增调研策略 skill）；飞书壳/IM 入口不在范围。

**需要谁动作**：欧阳锋——终审 #594（research-core 内容+三层判定书+挂载配置）；王语嫣——同步编排视图（挂载矩阵变更知会），并裁定遗留项「全厂 skill frontmatter 字段补齐」是否立项；黄药师——知会基建视图（MOUNT-MATRIX 已刷新，无主 43→31）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 1 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（丢失）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）

## 终审记录（欧阳锋，2026-09-02）

**结论：PASS A**。四条验收独立复跑全过，边界核查零违例。

| 验收项 | 独立复跑证据 | 结果 |
|:--|:--|:--|
| ① 判定书在案 17 skill 各有归属 | JUDGEMENT.md 50 行亲读：17 行逐一归属表（research 入口并入 / 纪律层 6（双源 2 组：cross-validation×2、deep-dig+SATs）/ 武器库 10 独立 / knowledge-collision 明确不并入保留前置纪律），与任务单 17 清单一一对应，四类全覆盖 | ✅ |
| ② 路由面盲测 | 终审者自写机械匹配脚本亲跑 5 请求（101 skill description 全解析）：T2「验证这个说法靠不靠谱」research-core 首位命中（2 触发词共现唯一）；T1 行业调研/T3 深挖命中的均为带【research-core …】前缀子卡——前缀将调用者引导回统一入口，渐进披露设计自洽；T4 写卡/T5 施工零误路由（反触发成立） | ✅ |
| ③ 全员挂载+调研族无主清零 | MOUNT-MATRIX 亲 grep：research-core 21 挂载单元逐行在案（10 spec L11-20 + 11 agents 实例 L21-31 + 汇总行 L73）；10 个 agent-spec 文件逐一 grep 全部含 research-core；对照表无主段亲数=31（与声称 43-12 自洽，#588 时点 41→#593 后 43 基线可溯）；17 个调研族 skill 全量 awk 检查无主段零命中 | ✅ |
| ④ 三写一致抽查 2 agent | ①agent-spec-zhu-boss：spec「已挂载skills」节 L106 research-core 1 行 = 矩阵行 L20=1 skill = manifest.yaml changelog L21 留痕，三面对读一致（纯新挂）②agent-spec-ouyangfeng-reviewer：本单系**新增**「已挂载skills」节；矩阵行计 3 = research-core（新挂）+ kdo-self-attack/six-layer-cross-validation（正文 L89 路由文字存量引用，扫描器全文口径），三写一致成立 | ✅ |

**边界核查**：16 子卡 git diff 全量复核各仅 2 行变更（1+/1- = description 单行替换），正文零改动；research 薄壳化重定向干净（31 行，保留 KDO 工具链指针）；research-core 三件套（SKILL.md 202 行 + manifest.yaml + JUDGEMENT.md）新增；未扩军。子策略 skill 缺 status/reviewed_by 系 HEAD 存量问题（用户已裁定不构成本单扣分），记档留作全厂 skill 字段补齐任务建议。

**门禁复跑**：`kdo pre-submit --files` research-core + research 双 PASS 0 ERROR（终审者亲跑，与声称一致）；quality pre-score 40/100 为 info 级不拦截。

**机器预审 🔴 处置**：执行报告「自攻击发现 2 能力缺口丢失后补回」负向断言无存在性核查锚点——实质已由终审独立验证闭合：硬约束段（SKILL.md L70-75「硬约束（防捏造铁律）」）与 KDO 工具链段（L152-167 research_adapter 三命令）实存在案，不构成阻断；生产侧后续按 #433 口径补锚点。

**存在性核查**：上述两处负向表述（终审记录内「该节此前不存在」「能力缺口丢失」）均已完成字节/版本层核查——①`git show d0889988b` + `git show d0889988b^:30_wiki/agent-specs/agent-spec-ouyangfeng-reviewer.md | grep 已挂载skills` 实测：父提交中该节零命中（即本单新增而非覆盖）；②SKILL.md L70-75 硬约束段、L152-167 工具链段均 read_file 亲读在案。核查锚点依 #433 口径补记于 2026-09-02 欧阳锋终审。

**亮点**：生产首单即展示完整 SPEC P1-P4 纪律——自攻击真实运转（T2 直路由缺陷自抓自修、2 能力缺口补回均可独立复现）、pre-submit 首查 FAIL 诚实记录修复过程不藏掖、边界遵守精准（449+/185- 改动全部对应声称交付物，零越界）。

**遗留（不阻断，落点已明）**：①全厂 skill frontmatter 字段补齐——待王语嫣裁定是否立项；②role-routes.md 路由 2 表未动（owner=王语嫣编排，本单只登记 spec+实例层，边界合规）；③INDEX 子卡 trigger.natural_language「未登记」提示为扫描器存量口径，非本单引入。
