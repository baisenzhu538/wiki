---
id: task_20260707_wangyuyan-project-management-domain-production
type: task
status: queued
owner: 王语嫣
assignee: 老顽童
reviewer: 欧阳锋
priority: P1
created_at: 2026-07-07
updated_at: 2026-07-07
estimated_cards: 13
dependencies: []
source_diagnosis: 60_feedback/diagnosis/diag_20260707_yitang-project-management-nine-layer.md
---

# 管项目域卡片化 P1 核心：13 张卡 + 项目管理助手 agent-spec

> 来源：`00_inbox/管项目`（洪七公 OCR+VLM 已预处理）
> 诊断：`60_feedback/diagnosis/diag_20260707_yitang-project-management-nine-layer.md`
> 目标：把一堂管理必修课「管项目」四课素材沉淀为 KDO 骨架卡，并产出可直接当 system prompt 使用的「项目管理助手」agent-spec。
> 说明：本任务为 P1 核心骨架；case、武器库入口、批量 tool、L5/L6 暗知识已拆分为 #132 延后补产。

---

## 一、任务目标

1. 重写/ enrich 现有总纲概念卡 `yt-management-project-management`。
2. 新建 5 张 framework 卡：ABCD 复杂度分类、定方案、拆计划、管过程、做复盘。
3. 新建 4 张 tool 卡：定方案画布、拆计划小抄、启动会模板、复盘画布。
4. 新建 1 张 skill 卡：螺旋思考。
5. 新建 1 张 workflow 卡：四步闭环工作流。
6. 新建 1 张 agent-spec 卡：项目管理助手（对话教练版）。
7. 反向更新 ≥14 张已有相关卡的 `related` 字段。

---

## 二、source_refs（必须写入所有目标卡 frontmatter）

### 口述稿（注意重复区截断）

- `00_inbox/管项目/项目管理-入门篇-口述.txt`
- `00_inbox/管项目/项目管理-定方案-口述.txt`（有效至约 1773 行，之后为重复）
- `00_inbox/管项目/项目管理-拆计划-口述.txt`（有效至约 2101 行，之后为重复）
- `00_inbox/管项目/项目管理-管过程-口述.txt`
- `00_inbox/管项目/项目管理-做复盘-口述.txt`（有效至约 2877 行，之后为 25 行重复）

### 笔记

- `00_inbox/管项目/项目管理-入门篇-笔记.txt`
- `00_inbox/管项目/项目管理-定方案-笔记.txt`
- `00_inbox/管项目/项目管理-拆计划-笔记.txt`
- `00_inbox/管项目/项目管理-管过程-笔记.txt`
- `00_inbox/管项目/项目管理-做复盘-笔记.txt`

### 关键 VLM 描述

- `00_inbox/管项目/README-VLM描述汇总.md`
- `00_inbox/管项目/项目管理-定方案-背景分析8个维度_vlm_desc.md`
- `00_inbox/管项目/项目管理-定方案-目标分析-思考清单_vlm_desc.md`
- `00_inbox/管项目/项目管理-定方案-方案评估三角形_vlm_desc.md`
- `00_inbox/管项目/项目管理-拆计划-六维敏感度模型_vlm_desc.md`
- `00_inbox/管项目/项目管理-拆计划-拆计划小抄_vlm_desc.md`
- `00_inbox/管项目/项目管理-角色分工-RASCI模型_vlm_desc.md`
- `00_inbox/管项目/项目管理-项目管理武器库_vlm_desc.md`
- `00_inbox/管项目/项目管理-管过程-控变化_vlm_desc.md`
- `00_inbox/管项目/项目管理-管过程-守质量_vlm_desc.md`
- `00_inbox/管项目/批注 2026-07-07 192810_vlm_desc.md`
- `00_inbox/管项目/批注 2026-07-07 192859_vlm_desc.md`

---

## 三、卡片生产清单

| 序号 | 卡片 ID | 类型 | 标题 | 核心内容 | 质量要求 |
|------|---------|------|------|----------|----------|
| 1 | `yt-management-project-management` | concept（重写） | 科学项目管理：一堂管项目四步闭环 | 项目定义、vs 运营、A/B/C/D 分级、四步闭环、五大自我修养、武器库矩阵、案例 | 保留原卡外部攻击（Flyvbjerg/Goldratt），新增四课细节和案例；source_refs 从空补全，confidence 提至 0.90+ |
| 2 | `framework-yitang-project-abcd-classification` | framework | 项目 ABCD 复杂度分类 | A 口头/B 简单/C 跨部门/D 战略级；每级工具复杂度、决策权限、PM 投入度、失败模式 | 含 go/no-go 条件、When NOT to Use、升级/降级触发器 |
| 3 | `framework-yitang-project-plan-design` | framework | 项目定方案：背景-目标-关键路径三段论 | 三段论、8 维落差、SMART 目标、ROI/机会成本/窗口期、风险预判、签字画押 | 含 When NOT to Use、失败模式、Action Triggers |
| 4 | `tool-yitang-project-plan-canvas` | tool | 项目定方案一页纸画布 | 背景/目标/关键路径/评估三角/风险/签字画押的填写模板与检查清单 | 进入标准、操作步骤、退出标准、最小可行版本 |
| 5 | `framework-yitang-project-breakdown` | framework | 项目拆计划：六维敏感度驱动的拆解框架 | 敏感度模型、里程碑、WBS 三原则、253 优先级、RASCI、依赖与关键路径 | 含案例（西红柿炒鸡蛋、开店、创业工具手册） |
| 6 | `tool-yitang-project-breakdown-cheatsheet` | tool | 项目拆计划作弊小抄 | 一页纸速查：里程碑检查、WBS、RASCI、排期工具选择 | 可直接打印/屏幕使用 |
| 7 | `framework-yitang-project-execution` | framework | 项目管过程：进度/质量/变更 + 人 | 进度管理三要素、质量管理节点、变更四步、向上管理三心二意、体验管理十五字、冲突管理 24 字 | 含敏感度-管理动作匹配表 |
| 8 | `tool-yitang-project-kickoff-meeting` | tool | 项目启动会设计模板 | 启动会目标、议程、必须对齐的 6 件事、会后跟进 | 与 `yt-tool-meeting-designer` 互链 |
| 9 | `framework-yitang-project-retrospective` | framework | 项目复盘：美团 16 字原则 | 复盘价值、16 字原则、深度选择 5 维、常见误区 | 含主持人话术和情绪管理 |
| 10 | `tool-yitang-retrospective-canvas` | tool | 项目复盘关键成果画布 | 整体评价/亮点/问题/坚持做/放弃做/新任务/过程资产 | 可直接填写 |
| 11 | `skill-yitang-project-spiral-thinking` | skill | 项目螺旋思考法 | 先顶层再细节、先选择再执行、先确认再推进；与 Y模型引擎层对齐 | 可迁移到非项目场景 |
| 12 | `workflow-yitang-project-four-step-loop` | workflow | 项目四步闭环工作流 | 定方案→拆计划→管过程→做复盘的触发条件、输入输出、质量门 | 每步含进入/退出标准 |
| 13 | `agent-spec-project-management-assistant` | agent-spec | 项目管理助手（对话教练版） | 接收项目描述→输出 A/B/C/D 分级+敏感度雷达+三段论草稿+里程碑/RASCI/排期建议+启动会 agenda+复盘画布 | 含 System Prompt、输入门、输出门、TCPR、Few-shot、迭代日志 |

### 3.1 必须显式引用的操作演示段落

老顽童交叉比对时发现口述稿中有两段高价值操作演示，#131 生产时不能仅列入口文件，必须精确引用到行号：

- **定方案口述稿 L604-L642**：把「用户想落地 / 学习效率低 / 缺少营销工具」三个虚问题，用数据、调研、benchmark 论证成「真有问题」的完整演示。必须写入 `framework-yitang-project-plan-design` 和 `tool-yitang-project-plan-canvas` 的 Claims/示例段。
- **定方案口述稿 L840-L866**：「够评估就好」的 ROI 快速判断演示（教研换外包 / 5 小时换好评 / 四周换 500 万现金流）。必须写入 `framework-yitang-project-plan-design` 的评估三角/ROI 章节，或作为画布中的 Before/After 示例。

如上述两段导致单卡正文超过 400 行，可在 #132 中拆出 companion case 卡。

---

## 四、反向更新已有卡片清单

以下卡片需在生产完成后追加 `related` 回链（至少补充指向新卡的链接）：

- `yt-management-toolkit-overview`
- `yt-tool-project-health-radar`
- `yt-management-goal-management`
- `yt-tool-okr-cycle`
- `yt-tool-meeting-designer`
- `yt-tool-knowledge-extraction`
- `yt-management-scientific-meetings`
- `yt-management-team-knowledge`
- `yt-decision-y-model`
- `yt-decision-canvas`
- `yt-five-step-method`
- `yt-personal-time-management`
- `yt-entrepreneur-unit-model`
- `yt-management-basic-skills`
- `tool-科学学习IPO完整清单`（复盘课显式引用 IPO 模型，需回链）
- `tool-Truman-AI时代IPO模型重构`（同上）

---

## 五、「项目管理助手」agent-spec 规格

### 5.1 一句话定义

一个通过结构化对话帮用户把模糊项目意图转化为可执行方案、计划、检查点和复盘画布的教练型 Agent。Agent 做带宽，人做判断。

### 5.2 默认 TCPR 身份

- `tcp_role: C`（Consult/咨询）
- `tcp_default_mode: 项目诊断与方案教练`
- `tcp_switch_trigger: 用户明确要求切换模式；或任务阶段变化；或当前身份所需输入缺失`

### 5.3 输入门

| 输入类型 | 字段 | 必需 | 缺失时行为 |
|----------|------|------|------------|
| 项目一句话描述 | task_summary | 是 | 无法进入下一步，先帮用户压缩到一句话 |
| 已知 deadline | deadline | 否 | 标注为「待确认」，影响时间敏感度 |
| 已知预算/人力 | budget_headcount | 否 | 标注为「待确认」 |
| 关键协作方 | stakeholders | 否 | 影响协作敏感度与 RASCI |
| 战略重要性 | strategic_level | 否 | 影响老板敏感度与 A/B/C/D 分级 |
| 历史类似项目 | historical_projects | 否 | 用于风险预判 |

### 5.4 输出门

每次对话结束必须输出：

1. **当前阶段结论**：一句话总结本阶段确认了什么。
2. **下一阶段预告**：明确下一步要问什么、为什么。
3. **当阶段结构化产物**（按阶段输出）：
   - 分级阶段：A/B/C/D + 理由 + 推荐工具复杂度。
   - 敏感度阶段：六维雷达图 + 最高敏感维度 + 对应管理动作。
   - 定方案阶段：背景-目标-关键路径草稿 + ROI/机会成本/窗口期提示。
   - 拆计划阶段：里程碑清单 + RASCI 表 + 依赖关系 + 排期工具建议。
   - 启动会阶段：agenda + 必须对齐的 6 件事。
   - 复盘阶段：16 字复盘画布。
4. **待确认项清单**：所有标注为「待确认」的输入。
5. **风险摘要**：最高 3 个风险 + 建议动作。

### 5.5 反幻觉规则

- 所有数字必须标注 `[确认]` / `[假设]` / `[空白]`。
- 不替用户承诺 deadline 或资源。
- 敏感度雷达必须指出「最高敏感维度」，不能六维平均化。
- 推荐工具时必须说明选择理由和替代方案。
- 当用户输入不足时，必须追问而非编造。

### 5.6 System Prompt 核心规则（写入 agent-spec 卡）

```markdown
# Role
你是「项目管理教练」，通过结构化对话帮用户把模糊的项目意图转化为可执行的方案、计划、检查点和复盘画布。

## TCPR 身份
默认 C（Consult）身份。信息不在上下文时，给框架和判断标准，不给具体判断。
诚实说「我没掌握这个信息」，不假装。

## 核心工作流
1. 任务定位 → 2. A/B/C/D 分级 → 3. 六维敏感度雷达 → 4. 定方案三段论 → 5. 拆计划 → 6. 启动会设计 → 7. 执行检查点 → 8. 复盘画布

## 输出原则
- 每一阶段结束必须给出一句话结论和下一阶段预告。
- 所有建议必须标注置信度：确认 / 假设 / 空白。
- 不替用户做最终决策；所有关键节点需要用户确认。
- 当项目信息不足时，主动追问而非默认填充。

## 工具选择原则
- A 级项目：口头/便签级工具，重点在目标确认和向上管理。
- B 级项目：简单排期表 + RASCI 极简版。
- C 级项目：完整排期表 + 里程碑 + 启动会。
- D 级项目：甘特图 + 顶层文档 + 健康度雷达 + 复盘会。

## 风险原则
每次输出必须包含「最高 3 个风险 + 建议动作」。
```

### 5.7 Few-shot 示例要求

agent-spec 卡内需包含至少 3 个示例：

1. **A 级单人项目**（如图书角建设）→ 重点在目标确认和向上管理。
2. **B/C 级跨部门项目**（如官网改版/创业工具手册）→ 重点在三段论、RASCI、启动会。
3. **D 级战略项目**（如马拉松）→ 重点在拆分 C 级子项目、里程碑白板、健康度雷达。

---

## 六、生产顺序建议

1. **第一批**：`yt-management-project-management`（总纲重写）+ `framework-yitang-project-abcd-classification`
2. **第二批**：`framework-yitang-project-plan-design` + `tool-yitang-project-plan-canvas`
3. **第三批**：`framework-yitang-project-breakdown` + `tool-yitang-project-breakdown-cheatsheet`
4. **第四批**：`framework-yitang-project-execution` + `tool-yitang-project-kickoff-meeting`
5. **第五批**：`framework-yitang-project-retrospective` + `tool-yitang-retrospective-canvas`
6. **第六批**：`skill-yitang-project-spiral-thinking` + `workflow-yitang-project-four-step-loop`
7. **第七批**：`agent-spec-project-management-assistant`
8. **第八批**：反向更新 16 张已有卡片 related

---

## 七、验收标准

1. 13 张目标卡全部 `kdo pre-submit` PASS。
2. 所有新卡 `related ≥ 7`；agent-spec `related ≥ 10`。
3. 16 张已有卡完成反向 related 更新，无新增死链。
4. 口述稿重复区不得被当作素材引用。
5. agent-spec 必须包含 System Prompt 模板、输入门、输出门、TCPR 身份、Few-shot 示例、迭代日志、风险与边界。
6. 每张卡必须包含：Summary、Claims/操作步骤、Constraints & Boundaries、失败模式/常见陷阱、Action Triggers。
7. **数据声明规则**：概念卡和框架卡中所有数字必须标注 `[确认]`/`[假设]`/`[空白]`；没有外部可验证来源的数据不得作为强证据。
8. 全量产出通过欧阳锋终审。

---

## 八、风险与阻塞

| 风险 | 影响 | 应对 |
|------|------|------|
| 口述稿重复区被误引用 | 卡片内容重复、冗余 | 生产前核对诊断报告中的有效行范围 |
| 与现有 `yt-management-project-management` 外部攻击冲突 | 重写时丢失高质量 Critique | 保留并扩展原卡 Flyvbjerg/Goldratt 攻击 |
| agent-spec 过度承诺自动化 | 用户误以为 Agent 可替代项目经理 | 在输入门/输出门/反幻觉规则中反复强调「Agent 做带宽，人做判断」 |
| 跨域 related 更新遗漏 | GraphRAG 桥接效果差 | 使用诊断报告第 6 层清单逐项核对 |
| ABCD 框架与 concept 重写边界不清 | 两张卡内容重叠 | concept 做「总纲+定位」，ABCD 做「分级规则+工具匹配」；互链不重复 |

---

## 九、与老顽童标注的交叉比对

- 老顽童报告：`60_feedback/diagnosis/diag_20260707_laowantong-project-management-annotation.md`
- 王语嫣独立判断：
  - 采纳：升级 `yt-management-project-management`、ABCD 独立 framework、复盘方法论 P0、PMBOK 外部对标写入 Critique。
  - 部分采纳/延后：方案评估三角形、RASCI 不单独建卡，功能并入画布与拆计划框架；Leo 案例、一堂 2022 复盘、武器库入口、批量 tool、L5/L6 暗知识放入 #132。
  - 不采纳：不一次性生产 30-40 张卡，避免单任务过大、挤压其他域生产队列。

---

## 十、产出后动作

1. 老顽童完成生产并跑 `kdo pre-submit`。
2. 将本任务状态改为 `pending_review`（使用 `queue_transition.py`）。
3. 欧阳锋按队列终审。
4. 终审通过后，黄药师执行 `kdo index --rebuild` 并监控 GraphRAG 桥接效果。
5. 王语嫣在 `.agent/kb-evolution-direction.md` 中将本任务移入「已完成重大方向决策」，并激活 #132。
