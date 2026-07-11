# 任务 #158：C 域·业务公式 agent-spec + 全域收口

> 编排：王语嫣 | 生产：老顽童 | 终审：欧阳锋
> 优先级：P3（依赖 #155/#156/#157 全部 reviewed）
> 诊断：`60_feedback/diagnosis/c-domain-business-formula-2026-07-12.md`；证据纪律同 #155 spec

## 背景

C 域建域的最后一块：业务公式教练 agent-spec。参照 #150（`agent-一堂-基本功教练`）与 #153（`agent-一堂-科学决策教练`，orchestrator 模式）的规格。
老朱已明确：C 域建完后第二阶段做**反向蒸馏**（自有「业务公式 agent」），管线现成（`tool-半肥猫-课程Skill化的八步工作流` + #104/#119 + Judge 五维/七要素）。本任务只产教练 spec，反向蒸馏另立任务、不在本任务范围。

## 交付清单

### 1. 新建 `.agent/prompts/agent-一堂-业务公式教练.md`（orchestrator 型）

角色定位：业务公式教练，帮使用者把自己的业务拆成公式、挖参数、升级逻辑关系、管理假设。

必须挂载的知识网（按 #155-157 产出卡实际名为准，生产时核对）：
- 总纲 + ABC 模型 + Ω 模型（先判断使用者在哪个环节）
- 段位诊断：参数冰山 L1-L6 × 逻辑关系冰山 L1-L6 双轴定位使用者当前段位（参照作业数六负责人推演案例的打分范式）
- 工作流：三段工作流（梳理→建立→深入）+ 降龙十八掌
- 工具调用：参数挖掘武器库（挖参数）/十大范式（借公式）/格式规范（写公式）/因果三件套（验因果）/定量空间三维度（定优先级）/假设池+PEAHD（落组织）
- 案例库：旗舰 8 案（按行业/场景匹配给使用者照镜子）
- 既有卡：`yt-business-formula-business-pattern-selector`（范式选择器）/`yt-tool-business-formula-metrics-checklist`（指标检查清单）/ `tool-一堂-业务公式-L1L6参数分层自检`

教练行为准则（从素材提炼）：
- 接手先问现状不问目标（实操篇 416-418：第一件事是了解业务现状）
- 先定段位再给药方（Leo 型给 L2 工具、Peter 型给 L6 话题，不越级灌）
- 反架空：公式必须从业务里长出来，使用者交来的「长串公式」先打格式分（10/40/60 范式）
- 默认失败共识+假设轰炸：引导使用者攒假设池而非求一次做对
- 数字纪律：所有参照数字声明「课程案例口径」
- 边界：不做五步法（A 域）、不做 ROI 单点决策（B 域）、不做转化率单点优化（D 域）——遇到越界需求指路到对应域 agent

### 2. digest 回链

`domains/business-formula-domain-digest.md` 补 agent-spec 导航段（spec 产出后回链）。

### 2.5 黄药师预写件处置（裁定见诊断 §八）

- **3 张桥接卡**（`framework-business-formula-{dual-triangle,y-model,fundamentals}-bridge.md`，draft）：P0-P2 卡 reviewed 后回填 `<<<TODO>>>` wikilink 占位，随本任务一并提交终审。**回填人：黄药师**（自己的 draft 自己回填；老顽童不代工），王语嫣的诊断书与 spec 为只读输入、黄药师不改这两份文件。
- **参数挖掘 agent-spec draft**（`tool-agent-spec-business-formula-parameter-miner.md`）：可作本教练 spec 的「参数挖掘子能力」附件保留，但**必须先用口述稿行号重写 source_refs（现全部只引笔记，违反口述一等纪律）、回填 3 处 TODO 悬空引用**；**修复人：黄药师**，素材已齐现在即可启动；做不到则按 draft 废弃、不随域交付。两类修复均走 `kdo pre-submit` 门禁 + 欧阳锋终审。
- **边界**：黄药师只修自己的预写件；#155-158 正文卡生产归老顽童，黄药师不越界代工。

### 3. 全域收口检查（生产完成报告的一部分）

- 检查 #155-157 全部卡与既有 15 张底稿卡的 related 是否成网（无孤儿卡）
- 检查四象限卡（`framework-lean-abcd-model`/`yt-decision-abcd-model` 等同名 ABCD 卡）与本域的边界说明是否到位（场景→域映射：A 五步法/B 决策/C 业务公式/D 黑客转化率）
- `framework-yitang-y-model-cross-domain-fusion` 映射表如有 C 域行需要补的，列清单报王语嫣（不直接改，Y 模型卡归其属主）
- 产出完成报告：卡数统计/回链统计/pending_unknown 清单/遗留问题

## 验收点（欧阳锋用）

1. spec 七要素齐全（角色/知识网/行为准则/边界/数字纪律/段位诊断法/案例调用法）
2. 与决策教练、基本功教练规格对齐（orchestrator 模式一致）
3. 无 orphan 卡、边界说明到位
4. 完成报告数据属实
