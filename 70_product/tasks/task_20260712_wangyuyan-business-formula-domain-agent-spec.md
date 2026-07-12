---
assignee: kimi
status: pending_review
updated_at: '2026-07-12T02:23:19.473118+00:00'
---
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

## 完成报告（老顽童 kimi · 2026-07-12 · 提交 pending_review）

### 交付清单

1. **`.agent/prompts/agent-一堂-业务公式教练.md`**（新建，orchestrator 型，21.5KB）——七要素落位：角色（§一+§八 Role）/知识网（§六调度速查 58 条 related，含任务单 L29 点名 3 张既有卡全在）/行为准则 6 条（§八，逐条带口述行号）/边界（§二越界指路表 A→五步法教练、B→科学决策教练、D→关键假设教练 + §十）/数字纪律（准则第 5 条+§十）/段位诊断法（§四 双轴打分 4 步流程，打分范式锚 `case-yitang-homework-six-owners`）/案例调用法（§七，旗舰 8 案全在、学员 7+合集 4 按需调）。规格与基本功教练/科学决策教练对齐（frontmatter 字段、orchestrator 结构、System Prompt 模板同款）。Ω 模型未造卡，统一指总纲第四节（实存，总纲 L174 起）。
2. **digest 回链**：related 追加 spec 链；L92 导言行「#158 在产」→已交付；L147 导航占位转正为正式条目（basename 裸链，照 decision-science-domain-digest L58 先例）；L148 参数挖掘 draft 挂账行未动（黄药师的事）。
3. **全域收口检查**（本报告下述）+ 交付 2.5 黄药师预写件：未触碰（裁定明确回填人/修复人=黄药师，老顽童不代工）。

### 验收点对照

- **1 spec 七要素齐全**：✅ 见上落位对照，可逐章 grep。
- **2 与决策/基本功教练规格对齐**：✅ orchestrator 模式、frontmatter（status: enriched / reviewed_by: pending / author: 老顽童 / updated_at '2026-07-12' 带引号 / tcp_* 四件套 / quality_labels）、System Prompt 模板结构同款。
- **3 无 orphan 卡、边界说明到位**：✅ 见下「收口检查」。
- **4 完成报告数据属实**：✅ 全部数据为脚本实测输出（python 扫描 30_wiki 全库 + spec，非估算）。
- pre-submit：spec PASS（1/1）、digest PASS（1/1）；spec 内 59 个去重 wikilink 目标逐一 find 核验零悬空。

### 收口检查数据（脚本实测）

- **卡数统计**：#155 交付 8（总纲/参数冰山/六层逻辑/十范式/ABC/playbook/武器库/digest）+ #156 交付 20 + #157 交付 19 + #158 spec 1 = **48 项新交付**；既有底稿接入 9（yt-management-business-formula / l6-essence-formulas / business-pattern-selector / qualitative-metrics-library / business-formula-to-kdo-card-quality / L1L6参数分层自检 / metrics-checklist / dk-plus-times-trap / yewenbin 射箭馆；EC 线 xingangwan 按既定裁定不动）。域内卡 **56 张 + 1 spec**。
- **回链统计**：域内 wikilink 边总数 **803**（56 卡+spec 互相及与域内卡的全部出向边实测）。孤儿扫描：**0 张零入链卡、0 张单入链卡**——56 卡+spec 每张 ≥2 条入链，全域成网。族内双向对称性（39 张 #156/#157 新卡）复扫 asymmetric: 0（F1 清零后保持）。
- **边界说明**：四象限同名卡边界均到位——`framework-lean-abcd-model` L44 有「C 业务提升·策略：业务公式」场景映射；`yt-decision-abcd-model` L148/L194 有「业务公式→增长场景（C）」映射；spec §二越界指路表与之一致（A 五步法/B 决策/C 业务公式/D 转化率）。
- **Y 模型映射表**：`framework-yitang-y-model-cross-domain-fusion` L74 已有五步法/业务公式行（链 yt-five-step-method-complete / yt-unit-model-overview，未链 C 域总纲）——按任务单裁定不直接改，**建议项报王语嫣**：该行可补 `framework-一堂-业务公式拆解-总纲` 链。
- **pending_unknown 清单**（11 卡 20 处，脚本实测）：18-moves 3（F2/F3 两源冲突+第 10 招无案例类标注）、three-industry-formula-demos 4（3 隐含假设+1 口述未点名注明）、business-pattern-selector 4（历史遗留，非本域轮次引入）、yt-management-business-formula 2（历史遗留）、marathon/woqingke/gacha-points/三类目标策略/format-spec/six-level-logic/metrics-checklist 各 1（含已裁定项的历史标注，如 gacha 卡内裁定过程记述）。

### 遗留问题（不阻塞本任务）

1. `tool-agent-spec-business-formula-parameter-miner` draft：source_refs 全引笔记+related 悬空，修复人=黄药师（诊断 §八+任务单 L46），修不好按 draft 废弃；spec 已将其挂为「修复前不得调用」。
2. 黄药师基线纠正（移除 10 条签名+三连复验）未回卷——欧阳锋提醒#158 终审前须落地，否则 lint 增量门禁形同虚设（转述，非老顽童范围）。
3. expert-interview 双卡并存去重：留 #158 收口后的清理任务（#156 终审 F5 裁定原文）；本轮已按裁定完成互链注定位。
4. 18-moves 第 13 招编号口径（内部评估 vs 专家访谈）与 expert-interview-10 卡不一致：已在 #156 修复记录提出，待另开任务裁定。
5. 3 张桥接卡 TODO 回填：回填人=黄药师（任务单 L45），随本任务一并提交终审。

### 协议 2 扫窗自查

#158 实动文件 = spec 新建 1 + digest 改动 1 + 本任务单 = 3 个（黄药师预写件不在老顽童实动集）。申报集=实动集，差集为空。

*老顽童（kimi）2026-07-12 · C 域建域收官，静候欧阳锋终审*
