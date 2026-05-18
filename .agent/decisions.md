# 架构决策

格式：日期 → 背景 → 决策 → 原因 → 否决的替代方案。

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
