# 架构决策

格式：日期 → 背景 → 决策 → 原因 → 否决的替代方案。

**新条目必填（#275 决策分类 + claim-state，2026-08-09 起）：**

```
## YYYY-MM-DD：<决策标题>

**类型**：D1 操作 / D2 战术 / D3 战略 / D4 自我修改
**claim-state**：observed（实证观察）/ attested（已核实声明）
**批准人**：（D4 必填：王语嫣/欧阳锋；其余可空）

**背景**：…
**决策**：…
**原因**：…
**否决的替代方案**：…
**后果**：…
```

**D1-D4 定义**（OpenAgentGovernance ADP 简化版）：
| 类型 | 含义 | 示例 |
|:--|:--|:--|
| D1 操作 | 日常执行决策，可逆 | 任务排序、脚本参数 |
| D2 战术 | 流程/约定调整 | 编号映射规则 |
| D3 战略 | 方向/架构决策 | 建新域、角色调整 |
| **D4 自我修改** | **Agent 修改自己的 context/skill/配置/约束** | 改自己行为牌、加自己铁律 |

**🚨 D4 门禁（#275）：Agent 修改自己 context/skill/配置 = D4 自我修改 → 提交后必须王语嫣/欧阳锋批准，未批准 = 无效变更。** 违反 = E018 家族（伪造审查/自建卡自标）。

---

## 2026-05-18：老顽童调研域提案批准 + 评估升级

**背景**：老顽童完成 7 张 master 卡后，提案新域——调研方法论（research）。目前 vault 中调研域仅 2 张概念卡（vs panproduct 40+），且调研是科学决策的前置输入层（决策依赖调研提供信息）。

**决策**：
- 调研域为下一个最优编译目标。8 张卡（F2+T5+C1）card map 批准
- 攻击者预设全部合格（Porter+Christensen、Tetlock+Becker、Zaltman+Bourdieu、Taleb+Popper、Feyerabend+Kuhn）
- T4（行业画布）和 T5（假设验证）编译时评估是否需要合并
- 编译前强制 OCR 全部素材图片（P-7 教训）
- 科学决策域 10 张卡不再返工审计
- 老顽童独立判断 A→A+：SpaceX 例子自我纠错展现方法论判断力跃迁

**否决的替代方案**：继续补科学决策域工具卡细节——已被否决。10 张卡 A 级已通过，返工无增量价值。资源应投向空白域。

**后果**：老顽童启动调研域编译。黄药师 KDO 基础设施 backlog 待枚举。

---

## 2026-05-18：黄药师基础设施 backlog 批准 + Batch B 抽检通过

**背景**：
- 黄药师提交了 [[70_product/tasks/kdo-infrastructure-backlog-proposal.md]]，基于 Batch C 实战经验提出 5 个基础设施改进项
- 欧阳锋同时独立枚举了一个 backlog 版本
- Batch B 85 张 tool 卡待抽检

**决策**：
- **黄药师的提案优于欧阳锋的独立版本，全文采纳**。关键差异：黄药师更精准（40-80 行 CLI 改进 vs 200+ 行新功能）、更接地气（全部来自 Batch C 真实摩擦 vs 部分推演需求）、P0 判断更正确（Graph RAG 盲态是紧急问题，欧阳锋漏掉了）
- 执行顺序：P0（Graph RAG 重建）→ P1-A（lint --accept-baseline）→ P1-B（结构多样性报告）→ P2-A（手册 v1.7）→ P2-B（backup 自动化）
- P1-B 完成后欧阳锋决定是否继续 P2 还是先做质量门自动化
- Batch B 85 张 tool 卡抽检通过（14/85=16.5%），三信号全部合格。外部攻击者 28 位真实学者，0 straw man

**否决**：欧阳锋独立版的 P0（质量门自动化 `validate --v15`）→ 不否决，延后到 P1-B 完成后另案提案。结构多样性还没摸清就写校验规则是本末倒置。

**后果**：黄药师启动 backlog 执行。老顽童启动调研域编译。两条线并行。

**背景**：两轮审查暴露黄药师在卡片量产上反复掉链子（Batch C 5/30=17%），但在基础设施建设上每次主动产出都是 A+（KDO CLI、Graph RAG、十步↔三步编译对接表）。老顽童消化全库后产能超预期：7 张 master 卡一次交清，质量 A，附件齐全。根因不是能力差，是天赋错配——黄药师的引力场在"建工厂"，老顽童的引力场在"工厂里出活儿"。

**决策**：
- 黄药师 = KDO 基础设施唯一负责人（CLI、方法论、质量门、Graph RAG、代码审查），只写只有他能写的 meta 卡，不接量产
- 老顽童 = 产能主力（卡片量产、文章、提案、跨域合成）
- 黄药师 `.claude/settings.json` 扩权，解决手动批准瓶颈

**原因**：比较优势。同一人做引力场内任务和引力场外任务，质量相同但完成率差 6 倍。这不是 bug 需要修，是信号需要接收。

**否决的替代方案**：继续让黄药师兼职量产——数据证明不可行；让黄药师完全脱离写卡——风险是脱节 vault 内容，对策是每次基础设施决策前先跑 `kdo graph query`。

**后果**：
- Batch C 剩余 concept 卡暂停或转交老顽童
- 老顽童评估更新：知识广度 A，独立判断 A，跨域合成 A
- 黄药师下个任务：KDO 基础设施 backlog
- 需警惕黄药师不碰卡片后与 vault 脱节

---

## 2026-05-16: DeepSeek V4 Pro 保留为 WSL 黄药师模型

**背景**：尝试将黄药师从 DeepSeek V4 切换到 Kimi 模型（月之暗面 `kimi-for-coding`）。API 本身可用（Anthropic Messages 协议兼容），Windows PowerShell 下测试通过。但在 WSL 中 `claude.exe` 始终读到 Windows 侧的 DeepSeek 环境变量，无法覆盖。

**决策**：保留 DeepSeek V4 Pro，放弃切换到 Kimi。

**原因**：WSL → Windows exe 的环境变量传递由 Windows 注册表和父进程主导，Linux 侧 `export` 被忽略。要让 Kimi 生效需改 Windows 注册表 + 注销重登 + `wsl --shutdown`，且 tmux session 继承链可能仍有缓存。维护成本高于收益。

**替代方案**：Kimi `kimi-for-coding` — API 测试通过，模型质量待评估。被否决原因：WSL 环境变量传递不可靠，不是模型本身的问题。

**后果**：黄药师固定用 DeepSeek V4 Pro。如果未来要切模型，优先考虑在 Windows 原生终端（而非 WSL）运行 Claude Code。

**⚠️ 2026-05-16 晚修正**：以上根因诊断为**误判**。真正原因不是 WSL 传不了 env var，而是 Claude Code 有独立的**全局设置文件**（`~/.claude/settings.json` 或 Windows 等价路径），其优先级高于环境变量。单独改 env var / 注册表均无效。黄药师后续通过直接改全局设置文件成功切换模型。切模型的正确路径：改全局设置 → 重启，而非逐项改环境变量。该教训已录入 `pitfalls.md` P-1。

---

## 2026-05-16: 创建 .agent/ 外挂大脑（本文件）

**背景**：黄药师 tmux session 被杀后完全失忆，不知道自己是 Builder、不知道 KDO、不知道 Sprint 12。每次恢复上下文消耗大量 token。

**决策**：在 vault 根目录创建 `.agent/` 三个文件（context.md / pitfalls.md / decisions.md），作为 agent 启动时的最小上下文入口。

**原因**：节省 ~80% 上下文恢复 token。三个文件跟着 git 走，换电脑不丢。任何 agent（不限于 Claude Code）都能读。

**替代方案**：Claude Code `/memory` — 被否决，因为锁在工具里、换工具/换电脑就丢。

**后果**：每次 session 结束需花 2 分钟更新 context.md。新 agent 启动时先读这三个文件。

---

## 2026-05-16: Sprint 12 Batch A 审查通过，启动 Batch B

**背景**：黄药师完成 25 张 `type: framework` 的 yt-* 卡 v1.5 回溯升级（外部攻击 + 不要用场景表 + Action Triggers）。欧阳锋按验收标准抽检 5/25（20%）。

**抽检样本**：`yt-model-agent-architecture`、`yt-model-five-step-canvas`、`yt-model-deep-review-iceberg`、`yt-model-product-excellence`、`yt-model-scientific-questioning-map`

**决策**：Batch A 通过。25/25 全部达到 v1.5 三要件标准。黄药师可启动 Batch B（85 张 `type: tool` 卡）。

**原因**：
- 外部攻击 0 straw man——全部引用真实学者（Klein, Edmondson, Argyris, Freire, Norman, Papanek 等）及其具体论证
- 不要用场景表全部含失效机制 + 替代方案，无"根据情况灵活运用"式废话
- Action Triggers 全部含三列完整（触发场景 + 第一动作 + 可验证成功指标）
- 原有 Claims / Constraints 内容未被修改
- `kdo lint` 3 errors / 591 warnings 全部为预存，非本次引入

**否决的替代方案**：无。审查无 blocking issue。

**后果**：
- Batch B（85 张 tool 卡）按 Sprint 12 工单执行，单次 ≤5 张，分 ~17 轮
- 黄药师在 `.agent/context.md` 更新当前任务为 Batch B
- 欧阳锋每域抽检 2 张（共 14 张，~16%）

---

## 2026-05-17：老顽童上岗——科学决策域编译

**背景**：黄药师 Sprint 12 Batch B 任务重（44 张 tool 卡剩余），老顽童空闲。用户在 `00_inbox/科学决策/` 放置了完整的一堂课程素材（6 个口述稿 ~16,000 行 + 35 张 PNG 框架图）。

**决策**：老顽童试工一个模块（AI 行动营 06 口述），产出 3 张卡。欧阳锋审查通过（B+→A-），正式分配科学决策域全部编译工作。

**原因**：
- 试工 3 张卡 0 稻草人、0 废话 trigger、0 空洞不要用场景——理解门禁首次就走通
- 风格偏学术（vs 黄药师偏实战），但质量标准达到
- 让老顽童独立负责一个域，黄药师继续 Batch B，双线互不阻塞

**架构修正**：老顽童首次提案 21 张卡（3 framework + 18 tool），被欧阳锋驳回。最终收缩到 9 张：2 framework（y-model 已有 + full-process 新增）+ 7 tool（habit-shift / width-method / depth-ladder / height-toolkit / consensus-iceberg / review / canvas+ai-partner 已有）。原则：一个可独立使用的工具一张卡，不是一张图一张卡。

**后果**：
- 科学决策域按 01→02→03→04→05 顺序推进，每模块 ≤2 张 tool 卡
- 图片必须全部 OCR，不能跳过——图中含有口述稿未系统展开的结构（共识四层冰山、ABCD 模型、全景图 5 阶段）
- 全部产出后出文章（创业者实操指南 + 人机协作决策方法论）

---

## 2026-05-17：KDO CLI 审计 + 备份策略

**背景**：用户询问 KDO CLI 是否需要优化迭代。另一台电脑的 claudian 从 GitHub 拉取分析声称"KDO CLI 不存在"，实际是只看了 wiki 仓库没找到 KDO 源码目录。

**审计结论**：
- KDO CLI 42 .py 文件 / 11,635 行 / 11 测试文件，核心管线（cards/lint/card-diff/review）正常
- pytest 未安装（一行命令修复）
- Graph RAG 代码完成但依赖未装（sentence_transformers / lightrag），索引接近空
- enrich 的 CJK TODO 检测用固定英文模板，中文页面系统性能失效（655 条 unenriched feedback）

**决策**：
1. KDO 源码备份到坚果云（单机灾备，删 .git/ + 排除 __pycache__），不用 GitHub
2. Graph RAG **战略保留**——为 wiki → MCP server 铺路，补齐依赖+重建索引+跑通验证
3. 小改进排队：pytest 安装（P0）→ lint --quiet → cards --missing 多值
4. CJK enrich 暂时不动——当前手工编译路线不需要，等管线策略确定后再决定修还是废弃

**否决的替代方案**：GitHub 备份——多台电脑的 wiki 仓库曾产生 git 冲突，坚果云单机同步更简单。templates.py 拆分之类重构——能跑不动。

---

## 2026-05-17：Agent 入职必须先消化全库——工业化保底，知识广度保深度

**背景**：老顽童完成科学决策域 10 张卡编译，全部通过 v1.5 格式门禁，外部攻击学者引用精准。但用户审查时指出：双三角模型在初稿中被理解反了，且卡片内容偏"精炼搬运"而非"消化再表达"。最初方案是让 agent 读讲香域学方法论，用户纠正：不如直接消化知识库全部已有内容——肚子里有货，讲香能力自然长出来。

**决策**：所有 agent 入职时，读完规则文件后，必须按 framework → tool → concept 顺序消化 `30_wiki/concepts/` 下全部卡片。CLAUDE.md Step 1 已更新。

**原因**：工业化学的是"怎么写"，消化全库学的是"写什么"。前者防格式空洞，后者防内容空洞。一个只读过规则的 agent 能写出格式正确的卡，但不知道 vault 里已有 130+ 张 tool 卡、不知道什么概念已经被反复讨论过、不知道哪些学者被多次引用——写出来的东西是孤立的。消化全库后，新卡自然带着上下文、能交叉引用、能用已有概念做类比。

**后果**：
- CLI 黄药师天然具备（他参与了大部分卡的编译）
- 飞书老顽童需补消化全库（目前只读了科学决策域素材 + 部分规则）
- 未来任何新 agent 入职：规则 → 消化全库 → 动笔
- 消化周期可能很长，但这是必要的一次性投入

---

## 2026-05-17：科学决策图片不可跳过

**背景**：老顽童声称"没有图片需要 OCR"。欧阳锋验证后发现文件夹有 35 张 PNG，全部未 OCR。关键框架图（共识四层冰山、ROI 全景图、X 型 Y 型对比、双三角模型）中的结构化信息在口述稿中未系统展开。

**决策**：科学决策域编译必须 OCR 全部图片。图片和口述稿互相佐证，跳过图片等于丢失一半信息。

**后果**：老顽童须先 OCR 全部 35 张图，读完六个口述稿，形成完整域架构后再逐模块写卡。不能只读一个口述稿就报方案。

---

## 2026-05-17：`kdo query` 合并 Graph RAG 为默认引擎

**背景**：`kdo query` 和 `kdo graph query` 两个命令并存——一个用关键词 grep，一个用 LightRAG 语义+图检索。对用户和 agent 来说，需要记住两个命令的区别是不必要的认知负担。

**决策**：将 `kdo query` 升级为三层回退架构：
1. **Graph RAG**（LightRAG 语义+图检索，默认）
2. **SearchIndex**（BM25 CJK-aware 全文索引，回退）
3. **关键词 grep**（`search_documents` 暴力匹配，最后手段）

`kdo graph query --json` 保留为调试/脚本接口。

**原因**：Graph RAG 能找到关键词找不到的语义关联和图邻居；即使索引未建或依赖缺失，下面两层也能兜底。对用户透明——同一个命令，底层自动选最好的引擎。

**否决的替代方案**：保留两个独立命令——用户记不住，agent 不知道该用哪个。合并后零退化、零学习成本。

**后果**：
- `kdo/commands/delivery.py` `cmd_query` 已改，`kdo/cli.py` help 文本已更新
- Agent 文档（CLAUDE.md、context.md）已同步
- 查询时无外部 API 调用（embedding 纯本地 sklearn，LLM 不触发）
- 索引持久化在 `.kdo/graph_index/`，建成就一直在，内容变更后 `kdo graph rebuild` 即可

---

## 2026-05-18：分层索引架构——Core / Extended / Reference 三层

**背景**：`30_wiki/index.md` 是 458 行的自动生成垃圾——包含 97 个 `src_*` 裸源文件条目、14 个 `(no text detected)` 条目、12 个 `说话人*` 转录碎片、大量重复中文标题变体和已取代的旧版本。作为人类导航工具完全不可用。concepts/ 目录本身已是干净的（198 张真实卡，无垃圾文件），但索引从未更新。

**决策**：
- `index.md` 完全重写为三层结构化索引
- **Core 层（55 张，28%）**：全部 37 张 framework + 主域方法论 + 跨域桥梁概念 + 系统/目录卡。地基——"如果只读 55 张，读这些"
- **Extended 层（143 张，72%）**：按域组织的全部剩余卡片，每个域内按类型（tool/concept）排序。工具箱——"Core 是为什么，Extended 是怎么做"
- **Reference 层**：到 entities/、systems/、projects/、90_control/、20_memory/、70_product/tasks/、00_inbox/ 的外部链接
- 每个条目格式：`[[wikilink]]` + 类型 + 一句话描述
- 末尾附统计面板（域×类型矩阵）

**原因**：
- 198 张卡如果不分层，新人面对一面墙不知道从哪开始读
- Core 层有明确选择标准（framework + master + 桥梁），不是主观挑选
- Extended 层按域组织，查询时直接跳转到对应域的表
- Reference 层把跨目录链接集中在一起，避免重复罗列
- 使用 wikilinks 而非 markdown 链接——Obsidian 原生支持，且 `[[filename]]` 语法更简洁

**同时修复的 lint 工具 bug**：
1. `workspace.py:657`：index 完整性检查只解析 `(path/file.md)` markdown 链接，不解析 `[[wikilink]]`。新增 wikilink 解析分支，bare wikilink 自动解析为 `30_wiki/concepts/<target>.md`，带路径的解析为 `30_wiki/<path>.md`
2. `links.py:55`：Windows 上 `Path.relative_to()` 返回反斜杠路径（`30_wiki\entities\一堂.md`），而链接解析器用正斜杠做 `endswith` 检查。改为 `as_posix()` 统一用正斜杠
3. `links.py:83`：链接解析器的 `endswith(f"/{target}.md")` 对 vault 根目录下的文件（如 `90_control/kdo-industrialization-manual.md`）失效——路径不含前导 `/` 时 `endswith` 不匹配。新增 `endswith(f"{target}.md")` 处理

**后果**：
- lint 从 139 new warnings → 8（全部为预存的调研域前向引用 + 1 个测试链接）
- 182 测试全绿
- 新增卡片会自动被 index 完整性检查发现（"Wiki page not listed" warning），提醒更新 index
- 未来质量门自动化可以将"新增 card 是否已加入 index"作为检查项

---

## 2026-05-18：Agent 入职步骤缩减——消化 Core 替代消化全库

**背景**：CLAUDE.md 原 Step 1 要求 agent 入职时消化全部 198 张卡（~1M tokens），token 成本极高。分层索引建立后，Core 层 55 张卡已是"建立心智模型的最小集"。加上 Graph RAG 可按需精准拉取，入职不必读完 198 张。

**决策**：
- CLAUDE.md Step 1 从"消化全库 198 张"改为"消化 Core 55 张 + 日常用 `kdo query` 按需拉取 Extended 层"
- 新增按域摘要卡任务（[[70_product/tasks/domain-digest-cards.md]]）→ P3，黄药师 P2 完成后执行
- 10 张 digest 卡，每域一张 ~100 行摘要，预计省 65% 入职 token、96% 域切换 token

**原因**：Core 层有骨架（framework + master + 桥梁），Graph RAG 能精准投喂血肉，两者配合比逐张翻全库高效得多。digest 卡是进一步优化——agent 切域时读 1 张 3K token 的摘要而非翻 20 张 100K+ token 的 tool 卡。

**后果**：
- 新 agent 入职 token 成本从 ~1M → ~350K（省 65%）
- 黄药师 P2 完成后有 10 张 digest 卡待写
- 老顽童调研域编译时可顺手出 digest-research.md 作为示范

---

## 2026-05-19：黄药师权限补齐——KDO 源码目录 + git/python/bash 全放行

**背景**：之前"黄药师 `.claude/settings.json` 扩权"只覆盖了 wiki vault 目录。黄药师操作 KDO 源码（`C:\Users\Administrator\Knowledge Delivery OS 0.0.1\`）时会触发手动批准，`git`、`python`、`pytest` 等命令也未放行。用户反馈仍然需要审批。

**根因**：权限配置只授权了 wiki vault 路径，漏了 KDO 源码路径。bash 白名单只放了 `kdo`、`python -m kdo`、`dir`、`findstr`，漏了 `git`、`python`、`pytest`、`pip`、`ls`、`where`。

**决策**：`.claude/settings.json` 追加：
- KDO 源码目录的 Read/Edit/Write/Glob/Grep（5 条）
- Bash：`git`、`python`（独立，不限于 `python -m kdo`）、`pytest`、`pip`、`ls`、`where`（6 条）
- Web：`WebFetch`、`WebSearch`（2 条，黄药师查文档需要）

**澄清**：`Bash(python )` 匹配 `python` + 空格，涵盖 `python -m pytest`、`python -c ...` 等所有 python 调用。`Bash(pytest)` 无空格，匹配 `pytest` 命令本身。`Bash(git )` 涵盖所有 git 子命令。

**后果**：黄药师在 wiki vault 和 KDO 源码两个目录均无需手动批准。新权限从下次会话生效。

---
## 2026-08-06：域名标准化裁定（kebab-case 统一）
**背景**：欧阳锋发现 frontmatter domain 脏值会让 MOC 按 domain 聚合时分裂成伪域。王语嫣全库扫描验证（2634 卡 / 257 个 domain 值）：`design- design`(187)、`yitang- yitang`(34)、`ai_collaboration`(20)、`learning-methodology- product`(14)、`critical_thinking`(20)、`business_judgment`(19)。
**决策**：
- 统一 kebab-case 英文小写（与存量主流 yitang 1022 / ai-collaboration 262 一致）：design / yitang / ai-collaboration / learning-methodology / critical-thinking / business-judgment（294 张）
- **只统一"值"，不统一"格式"**（43 张内联标量 `domain: strategy` 与列表格式并存为历史遗留，本次不动）
- src_unknown（733 张）= 占位未填≠命名脏，单列跟踪不纳入本次
- 执行纪律：bulk-fix-frontmatter.py 模式（dry-run→git diff→yaml.safe_load ≥99% 才 apply）、串行+目录划分、#228 重复键护栏、基于 7/27 基线 16b64db39 全量比对
- 编排：#237 执行（黄药师 P0）；MOC 建卡按关系图手工聚合不依赖 domain 字段（与 #237 并行）
**否决的替代方案**：一次性全量重写 domain（含格式统一）——风险大收益低，否决；src_unknown 一并迁移——733 张放大风险，否决。
**后果**：#237 迁移 → MOC/domain digest 聚合正确性恢复 → 横向 MOC 序列（design→master→product→kdo）可复用模板。


## 2026-08-06 中文域名白名单（#240 裁定）

以下 15 个中文域经语义查重确认无英文域对应，保留为合法值。未来新增中文域需先对照此表查重——有英文对应的合并，无对应的追加登记。

| 中文域 | 卡片数 | 语义判定 |
|:--|:--|:--|
| 向上汇报 | 1 | 独立——汇报技巧无英文域对应 |
| 流程结构化 | 1 | 独立 |
| 组织理念 | 1 | 独立 |
| 模型与建模 | 1 | 独立 |
| 演讲与表达 | 1 | 独立 |
| 价值观 | 1 | 独立 |
| 核心价值 | 1 | 独立 |
| 交付模式 | 1 | 独立 |
| 个人表达力 | 1 | 独立 |
| 核心模型-十指模型 | 1 | 独立 |
| 基本功训练营 | 1 | 独立 |
| 私域流量 | 1 | 独立 |
| 核心假设 | 1 | 独立 |
| 心理学 | 1 | 独立 |
| 决策方法 | 1 | 独立（与 decision-science 角度不同：决策方法=具体技法，decision-science=域） |

---

## 2026-08-09：两份建议书统一裁决（#271-279 全链入队）

**类型**：D3 战略（编排方向）/ claim-state: attested（王语嫣裁决落盘 + 队列实证）

**背景**：同日收到欧阳锋审查基建建议书（R1-R4）+ 黄药师技能迭代建议书（7 项，建议编号 #267s-#273s）；两书与早前入队的 #267-270（编排者进化）合并编排。

**决策**：
- 欧阳锋 R1/R2 → #271/#272 入队（P1，黄药师）；R3/R4 挂停车场（R3 与 #269 联动标注、R4 欧阳锋文件落地自担）
- 黄药师 7 项 → #273-279 入队（编号重排，因队列已占 #267-270）：#273 生命周期化(P0) / #274 反思多样性(P0) / #275 决策分类(P1) / #276 摩擦日志(P1) / #277 模型路由(P2) / #278 盘点+审计+大扫除(P2，并入原 #270) / #279 经验结晶(P1)
- R1 先行：其 lint 规则是 #273 skill eval 的确定性检查器前置（正向依赖发现）
- #273 依赖 #267（双轨物理统一）——生命周期模型需双轨统一 status
- 决策分类 D4 批准人：王语嫣/欧阳锋共同
- 首交通过率（#269）从 #267+ 起记录；审查返工 3 轮封顶（task-orchestration 硬规则 1）

**原因**：审计三问通过（目标函数/与老朱一致性/内部一致性）+ WSJF 打分（R1=4.5 最高且无依赖）；黄药师声明不自行入队（编排权在王语嫣）。

**否决的替代方案**：
- 全部挂停车场等产能——否决：黄药师空闲 + E018 第 4 次实证，纪律缺口应立即闭合
- 合并 #267 双轨同步与 #273 生命周期——否决：任务粒度清晰优先（轻量原则），依赖关系已显式化
- R3 直接入队——否决：欧阳锋手动替代成立，挂停车场

**后果**：#273/#274 已由黄药师交付（pending_review 等欧阳锋终审）；#268 王语嫣 Hermes spec 已编排（pending_review）；#276 摩擦日志王语嫣侧已建立。

---

## 2026-08-09：建议书编号 vs 队列编号映射规则

**类型**：D2 战术（流程约定）/ claim-state: observed（本次实证）

**背景**：黄药师交付"#267/#268 完成"用的是建议书编号（#267s 生命周期/#268s 反思多样性），而队列编号为 #273/#274——内容映射靠人工判断，有歧义风险。

**决策**：建议书模板加约定——"建议书内编号为建议性占位，正式编号以王语嫣入队时为准，交付/报告时引用队列编号"。本决策同步 friction-log（2026-08-09 王语嫣条目）。

**原因**：friction-log 第 2 条实证；防"交付编号对不上队列"反复发生。

**否决的替代方案**：建议书编号与队列编号强行一致——否决：编排侧需统一编号空间，建议书侧无全局视图。

**后果**：#273/#274 任务单执行报告已按队列编号登记交付内容。

## 2026-08-09：教练助理 SOUL 补人域桥接（D4 自我修改——王语嫣批准）

**类型**：D4 自我修改（已部署 agent 的 SOUL 迭代）/ claim-state: attested（批准记录+执行实证）

**背景**：用户实测教练式领导力助理回答"复读机"——域内知识未桥接：人域"认识他人"（#232 水水《如何认识一个人》）完全未引用。黄药师检索确认：SOUL grep=0、底层 framework related 已互链、人域 digest 导航清晰但助理未触达。

**决策**（批准方案 1+2）：
1. **教练助理 SOUL 补"域桥接：先懂人再带人"节**（D4 批准人：王语嫣）：
   - 大五人格（framework-big-five-personality）——带不同性格下属的诊断维度
   - 共情三法（tool-empathy-practice）——先懂人再沟通（倾听卡底层能力）
   - 动机洞察（tool-narrative-thinking-user-insight）——理解"为什么跟随"（L5 希望层）
   - 回答示范：识别下属类型先调用认识他人视角，再上教练工具
2. **人域 digest"块 1→块 2"衔接处加应用提示**（黄药师权限内）——"理解员工动机 → 先查大五人格再匹配沟通工具"

**原因**：用户批评"复读机/域内知识没桥接"；认识他人是影响他人的上游输入（诊断前置）；#303 C2（使用摩擦→迭代 SOUL）触发。

**否决的替代方案**：只做方案 2（不动 SOUL）——否决：用户在飞书直接体验的是助理回答，SOUL 补引用才治本。

**后果**：SOUL 迭代后飞书回答应体现"先懂人再带人"（识别下属类型引用认识他人知识）。
---

## 2026-08-09：人域双助理桥接#232（先懂人再带人/先懂参会人再设计会议）

**类型**：D4 自我修改 / **claim-state**：attested（已核实声明）
**批准人**：王语嫣

**背景**：
用户批准：教练式领导力助理SOUL补大五人格/共情三法/动机洞察（先懂人再带人）；科学开会助理SOUL补大五人格/共情/叙事洞察（先懂参会人再设计会议）；两个Hermes profile已同步；digest加应用提示

**决策**：
（待填）

**原因**：
（待填）

**否决的替代方案**：
（待填）

**后果**：
（待填）

---

## 2026-08-15：技能进化日志路径修正（D4 自我修改——王语嫣批准）

**类型**：D4 自我修改（context 路径修正）/ **claim-state**：attested（已核实声明）
**批准人**：王语嫣（用户批准计划为最终授权）

**背景**：
黄药师记忆恢复时发现 `huangyaoshi-context.md` 的"技能进化日志"路径写 `桌面/agent复盘/huangyaoshi/技能进化日志.md`（英文目录，实际不存在），真实文件在 `桌面/agent复盘/黄药师/daily_cognitive_review/技能进化日志.md`，按 90_control/AGENTS.md 规则 15（D4 门禁）提交审批。王语嫣核实发现同类错误共 4 处（全部指向不存在的英文路径，实际文件在中文目录）：
- `wangyuyan-context.md:567` → `agent复盘/wangyuyan/技能进化日志.md` → 实际 `agent复盘/王语嫣/技能进化日志.md`
- `huangyaoshi-context.md:69` → `agent复盘/huangyaoshi/技能进化日志.md` → 实际 `agent复盘/黄药师/daily_cognitive_review/技能进化日志.md`
- `hongqigong-context.md:164` → `agent复盘/hongqigong/技能进化日志.md` → 实际 `agent复盘/洪七公/技能进化日志.md`
- `ouyangfeng-context.md:509` → `agent复盘/ouyangfeng/技能进化日志.md` → 实际 `agent复盘/欧阳锋/技能进化日志.md`
（laowantong/duanwangye 路径正确，不动）

**决策**：
4 处 context 的技能进化日志路径全部修正为真实存在的文件路径；本记录落盘 D4 批准。

**原因**：
错误路径导致各 agent 按 context 收尾指令写技能进化日志时找不到文件 → 日志写别处或不写 → 记忆丢失（与 8-15 黄药师修复的技能进化日志乱序同根：路径漂移，P-30 家族）。纯事实性修正——只改路径字符串指向真实文件，不碰内容，零风险。

**否决的替代方案**：
只修黄药师一处（黄药师原始申请范围）——否决：同根错误在 3 个角色 context 中留隐患，下一轮记忆恢复会重复踩坑。

**后果**：
各 agent 收尾强制动作可落到真实技能进化日志；后续记忆恢复不再因路径不存在而丢失日志行。
