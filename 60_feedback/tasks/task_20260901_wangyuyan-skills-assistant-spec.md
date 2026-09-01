---
id: '587'
title: Skills助理Agent spec——Skill生产+配置中枢（工厂第7角色）
type: spec
status: reviewed
priority: P1
assignee: 王语嫣
created_by: 王语嫣
created_at: 2026-09-01
updated_at: '2026-09-01T02:17:06.910079+00:00'
source_refs:
- 30_wiki/workflows/workflow-kdo-agent-production-pipeline.md
- agents/research-explosion-partner/SPEC.md
instance: wangyuyan
reviewed_by: 欧阳锋
review_date: '2026-09-01'
grade: A
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

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 1 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）

## 终审记录（欧阳锋 · 2026-09-01）

**结论：PASS / A（设计稿类，#525 同款口径）**

### 核查矩阵（六项全过，均亲跑）

| # | 终审要点 | 核验方法 | 结果 |
|:--|:--|:--|:--|
| 1 | 触发条件可执行性 | 三选一逐条对照编排层动作：①终审记录节标注「建议行为化」=结构化可 grep 信号→编排层入队 ②≥2 独立任务引用=数值阈值可扫描 ③老朱直令=直接入队；反触发三条均有机械判据 | ✅ 可机械执行，无需人工解释 |
| 2 | 四阶段流程完备性 | P1→判定书 3 行（Go/改造后Go/No）；P2→目录结构+四步封装法逐步有动作；P3→pre-submit 0 ERROR+路由面自攻击+五字段提审；P4→登记+矩阵更新+changelog 留痕 | ✅ 每阶段有产出物与门禁 |
| 3 | 与 #588 接口 | SPEC 第五节分工表 4 行 vs #588 交付物 4 项逐项对照：扫描脚本+目录生成=黄药师（#588 交付1/2）、登记维护=Skills助理、spec 模板增补落 #588 交付3、「生成机制归黄药师/内容维护归Skills助理」与分工表自洽 | ✅ 无歧义 |
| 4 | 三源抽查 | 源1 Truman 口述稿 L335-L475 逐字核：四步法（L365 快速认识/L375 保执行100%有效翻译/L387 先萃取再合并/L393 每环节2-5轮不够好）与 SPEC 第二节表述吻合；源2 Anthropic URL 亲 curl HTTP 200（渐进式披露三层与官方 Agent Skills 范式一致）；源3 #335 SPEC.md 实存，8 节对照本 SPEC 10 节为同构超集 | ✅ 抽 2 处全过 |
| 5 | 边界五条+U1-U3 | 边界 L102-108 五条齐；U1 背书 tool-nine-character-mantra-14-strategies.md 实存、U2 背书 method-anthropic-skill-design-patterns.md（#586 产）实存、U3 背书 shared/deep-debug/SKILL.md 实存（name/description frontmatter 亲读）；「只定义不实跑、部署另立项」与 SPEC 第九节两阶段口径一致 | ✅ 验收口径成立 |
| 6 | 执行报告五字段 | 交付物/完成内容/验证/边界/需要谁动作齐；声称「134行十节」亲测 wc -l=134、grep -c "^## "=10 全吻合；「三源路径实存」亲测全实存 | ✅ 诚实度复核通过 |

### 存在性核查（本意见书涉及的全部实存断言）

| 断言 | 验证 |
|:--|:--|
| SPEC.md 134 行 | wc -l 亲测 =134 |
| 十节 | grep -c "^## " 亲测 =10 |
| anti-ai-bs-three-moves manifest 含 trigger.natural_language | 亲读 manifest.yaml L10-11 在位（任务单六问 2 的先例引用成立） |
| deep-debug skill 实存 shared/ | ls 亲测在位 |
| shared skill 数量 | ls 亲测 74（#588 验收标准写 73——量差 1 为 #586/#587 期新增属正常漂移，#588 施工时以扫描实测为准，记档不阻塞） |

### 缺陷与小项（均不阻塞）

- 🟡 大小写记档：SPEC L99 `mount-matrix.md` vs #588 交付物 2 `MOUNT-MATRIX.md`——语义同一文件，Windows 文件系统大小写不敏感，不构成接口歧义；**#588 施工时统一为一个命名**（建议随 INDEX.md/MOUNT-MATRIX.md 大写惯例），此为施工期一行对齐项。
- 🔵 shared 数量口径：#588 验收「73/73」与本审实测 74——非本单范围，#588 开工时以扫描实测计数为准。

### 残余风险

- U1-U3 未实跑（设计如此，部署另立项）——部署验收单须把 U1-U3 实跑作为验收门，编排层立项时带上本 SPEC 第九节两阶段口径。

**#588 依赖解除。黄药师可开工；编排层处理部署单排期。**
