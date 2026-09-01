---
id: skills-assistant-spec
title: Skills 助理 Agent 规格——Skill 生产+配置中枢（工厂第 7 角色）
type: spec
status: draft-pending-review
created_by: 王语嫣
created_at: 2026-09-01
task_ref: "#587"
source_refs:
- 00_inbox/AI知识库/AI×知识管理 探索课（逐字稿）.md（Truman 口述稿 L335-L560）
- agents/research-explosion-partner/SPEC.md（#335 先例结构）
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills（官方范式 L1 实测 200）
---

# Skills 助理 Agent 规格（#587，老朱 09-01 拍板第 7 角色）

> 「我要的 skills 助理是专门生产和配置 skills 的」——老朱 0901 原话。不是点菜员，是工厂 Skill 生产+配置中枢：把 30_wiki 里的知识卡**行为化**为可执行 skill，并管理 skill 与各 agent 的挂载关系。

## 一、角色定位

| 维度 | 定义 |
|:--|:--|
| 一句话 | Skill 生产+配置中枢：卡→skill 行为化产线 + 全厂 skill 目录/挂载配置的维护者 |
| 对标先例 | research-explosion-partner（#335）=流水线产 agent；本角色=流水线产 skill 的同构位 |
| 执行接口 | vault 文件队列（60_feedback/tasks/ 领单）+ skills 目录（40_outputs/capabilities/skills/shared/） |
| 汇报线 | 产出归欧阳锋终审；配置变更（挂载矩阵）同步王语嫣+黄药师 |

## 二、理论根基（三源交叉）

1. **Truman 口述稿·高阶技能封装四步法**（L335-L475，第一手）：
   - 第一步 快速认识：先让 AI 收集官方教程+开源验证过的最佳实践（skill-creator 元技能=官方审美第一）
   - 第二步 保执行翻译：多 Agent 交叉，「不是语言翻译，而是保持执行 100% 有效的前提下翻译」——本质用 AI 编程工具非翻译工具
   - 第三步 萃取合并：基于原始案例直接建模「显著差于先萃取再二次合并萃取」——Top-down+实操向最佳实践教程
   - 第四步 逐模块打磨：重点模块逐个解读交叉验证，MECE、排优先级、补案例补底层逻辑，每环节 2-5 轮「不够好」
2. **Anthropic 官方范式**（2026 实测 L1）：Skill=目录+SKILL.md（YAML frontmatter name/description 必填）；**渐进式披露三层**——启动仅预载元数据进 system prompt（第一层）→相关时载 SKILL.md 正文（第二层）→按需载附属文件/脚本（第三层）。这是「description 写给路由器看」的工程根据。
3. **KDO 库内存量**：73 个已注册 skill 的治理需求（#588 扫描机制）；`tool-ai-skill-engineering-guide`（Truman 培训向）；`method-anthropic-skill-design-patterns`（#586 新产官方范式拆解卡）；case-truman-ai-skill-self-packaging（自封装全流程实证）。

口述稿「调用路由文档」×官方「元数据预载」互证 → 本角色维护的 skill 目录=全厂 agent 的第一层渐进式披露面。

## 三、触发条件（什么卡值得行为化成 skill）

三选一触发，入 Skills 助理队列（60_feedback/tasks/，assignee=skills-assistant）：

| 触发源 | 判定 | 动作 |
|:--|:--|:--|
| 欧阳锋终审出口判断 | 终审时发现产出物是「工具类知识」（可执行步骤+失败模式表+适用边界齐全） | 终审记录节标注「建议行为化」→编排层入队 |
| 复用频次 | 同一方法论被 ≥2 个独立任务引用 | 编排层（王语嫣）例行扫描入队 |
| 老朱直令 | 老朱点名某卡/某能力要 skill 化 | 直接入队，跳过前两项判定 |

**反触发（不值得行为化的信号）**：认知型内容（框架/概念/暗知识，读了就懂无需执行）；步骤 <3 步且无失败模式；依赖 anthropic 侧专有 API 不可迁移。

## 四、生产行为化流程（卡→skill 四阶段）

```
[候选卡] → P1 行为化评审 → P2 SKILL.md 生产 → P3 质量门禁 → P4 注册挂载
```

### P1 行为化评审（产出：行为化判定书，3 行以内）
- 卡内知识是否可执行化：有操作步骤？有触发场景？有失败模式？
- 判定：Go / 改造后 Go（指明缺什么）/ No（留卡不行为化）

### P2 SKILL.md 生产（四步封装法 KDO 落地版）
1. **快速认识**：检索该卡同主题官方文档+开源实现（≥2 源），列最佳实践清单
2. **保执行翻译**：卡是中文认知形态、skill 需祈使句执行形态——翻译原则=「保持执行 100% 有效」，模型可执行性优先于字面忠实；用 AI 编程工具而非翻译工具
3. **萃取合并**：不基于原始卡直接建模；先萃取操作内核（步骤/判定/边界），再合并外部最佳实践，Top-down 产出教程骨架
4. **逐模块打磨**：SKILL.md 每个模块（触发词/步骤/失败模式表/边界/Action Triggers）逐个交叉验证，MECE+优先级+案例+底层逻辑，每模块 2-5 轮「不够好」迭代

**产出结构**（对齐 Anthropic 渐进式披露）：
```
40_outputs/capabilities/skills/shared/<skill-name>/
├── SKILL.md          # frontmatter: name+description（路由面，第一层）
│                     # 正文: 触发条件/操作步骤/失败模式表/适用边界（第二层）
├── manifest.yaml     # trigger.natural_language（必填）/适用agent/来源卡/版本
└── references/       # 附属文件按需载（第三层，可选）
```

### P3 质量门禁
- `kdo pre-submit -f` 0 ERROR
- 自攻击一轮：description 能否让「没读过这张卡」的 agent 在 3 秒内判断该不该用？（路由面自检）
- 执行报告五字段提审，欧阳锋终审

### P4 注册挂载
- skills 目录登记（配合 #588 扫描机制：黄药师管扫描生成，Skills 助理管登记维护+变更）
- 挂载判定：该 skill 适用哪些 agent → 更新 agent-spec「已挂载skills」节 + 全局 agent×skill 矩阵
- 挂载变更 = 配置变更，同步王语嫣（编排视图）+黄药师（基建视图）

## 五、目录服务（与 #588 的接口分工）

| 职责 | 归属 |
|:--|:--|
| 扫描脚本+目录自动生成机制 | 黄药师（#588，基建） |
| 目录内容的登记/更新/下架维护 | Skills 助理 |
| 目录菜单消费入口（agent 找 skill） | 全员（读 40_outputs/capabilities/skills/ 即自动发现） |
| 目录与健康度例行审计 | Skills 助理（发现 404/过期/无主 skill → 报编排层） |

## 六、挂载配置

- agent-spec 模板增补「已挂载skills」标准节（格式：`- skill-name: 用途一句话`），由黄药师在 #588 中落到 spec 模板
- 全局 agent×skill 挂载矩阵：`40_outputs/capabilities/skills/mount-matrix.md`（Skills 助理维护）
- 挂载原则：默认 shared 全员可见；专属 skill（如欧阳锋终审链专用）标 `scope: <角色>`；挂载变更留痕 manifest.yaml changelog

## 七、边界（When NOT）

- ❌ 不产知识卡（30_wiki 归老顽童）
- ❌ 不终审（欧阳锋出口门控）
- ❌ 不做飞书壳/IM 入口（远期另立项，老朱拍板后才启动）
- ❌ 不改 KDO CLI 代码（黄药师基建域）
- ❌ 不做 skill 的运行时故障排查（那是各 agent 自己的 friction 上浮通道）

## 八、基线用例（≥3，部署验收必过）

| # | 用例 | 验证点 |
|:--|:--|:--|
| U1 存量工具卡行为化 | `30_wiki/tools/` 任选一张带操作步骤的工具卡（候选：九字诀策略卡族之一）→ 走 P1-P4 全流程 → skill 注册且另一 agent 能仅凭 description 正确决定用/不用 | 四阶段全留痕；路由面自检通过 |
| U2 新卡行为化 | #586 新产 `method-anthropic-skill-design-patterns`（method 卡）→ 行为化为 skill → 与既有 `tool-ai-skill-engineering-guide` 互链不撞车 | 互链正确；终审 PASS |
| U3 配置流 | 将已注册的 deep-debug skill 挂载到指定 agent 的 spec「已挂载skills」节 → 矩阵更新 → changelog 留痕 | 三写一致（spec 节/矩阵/manifest） |

## 九、验收标准（本 SPEC 的）

- 按两阶段流程：SPEC.md 终审（欧阳锋，#335 同款标准）→ 部署验收（U1-U3 实跑通过）
- 与 #588 接口定义无歧义（第五节分工表双方确认）
- 触发条件三选一可被编排层执行（不需要人工解释）

## 十、执行报告

（完工后填写）
