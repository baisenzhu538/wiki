---
title: "KDO 失败模式库"
type: "control"
status: "draft"
created_at: "2026-05-03"
source: "EC工业化规范手册 第十三章 — 失败模式库方法论"
---

# KDO 失败模式库

> 每踩一次坑，入库一种模式。目标是下一个 Agent session 启动时读一遍，执行前就知道哪里会摔。

---

## 模式索引

| 编号 | 名称 | 严重度 | 状态 |
|------|------|:------:|:----:|
| F-KDO-001 | CJK regex 静默零返回 | 🔴 | 已知，无自动化防御 |
| F-KDO-002 | 非 .md 文件 ingest 静默跳过 | 🟠 | 已知，无自动化防御 |
| F-KDO-003 | state.json 覆盖写竞态 | 🔴 | 已修复代码，未入库 |
| F-KDO-004 | 错误工作目录执行 pipeline 命令 | 🟠 | 已知，无自动化防御 |
| F-KDO-005 | 过期 feedback 引用残留 | 🟡 | 已知，手动清理 |
| F-KDO-006 | 骨架页面 CJK 内容损毁 | 🟠 | 设计约束，手动绕过 |
| F-KDO-007 | 表层翻译式提炼 | 🟠 | 已知，L2 Lint 待实现 |
| F-KDO-008 | 虚假关联 | 🟡 | 已知，L2 Lint 待实现 |
| F-KDO-009 | 无质疑接受 | 🟠 | 已知，L2 Lint 待实现 |
| F-KDO-010 | 溯源断裂 | 🔴 | 已知，L1 Lint 待实现（Sprint 1） |
| F-KDO-011 | 百科词条化 | 🟡 | 已知，L2 Lint 待实现 |
| F-KDO-012 | Builder 上下文过载死锁 | 🔴 | 已知，操作规范已更新 |

---

## F-KDO-001: CJK regex 静默零返回

| 属性 | 内容 |
|------|------|
| **触发命令** | `kdo enrich --all` |
| **表现** | 输出 "0 pages enriched"，无报错，无任何页面被更新 |
| **根因** | `extractors.py` 中的 `extract_open_questions()` 使用 `\b` 词边界匹配——`\b` 不识别中文字符边界，对全中文页面永远返回空列表 |
| **触发信号** | `kdo enrich --all` 输出 "0 pages enriched" 但 wiki 目录下有未 enrich 的中文页面 |
| **防御措施** | ① `kdo self-check` 的 unenriched-wiki-page 检查会在事后发现（已生效）② 事前防御：ingest 时检测内容语言，CJK 内容跳过 regex enrich 并提示走 Agent 三步编译 |
| **临时绕过** | Agent 直接编辑 wiki 页面文件，执行三步 CJK 编译（浓缩→质疑→对标），手动更新 frontmatter status=enriched |
| **永久修复** | 配置 `KDO_LLM_ENDPOINT` 环境变量启用 LLM-based CJK enrich 路径（`curation.py:enrich_wiki_page_llm`），或等待 `extractors.py` 增加 CJK-aware 分词器 |
| **关联文件** | `kdo/extractors.py`, `kdo/commands/curation.py` lines 142-336 |

---

## F-KDO-002: 非 .md 文件 ingest 静默跳过

| 属性 | 内容 |
|------|------|
| **触发命令** | `kdo ingest` |
| **表现** | 对 `.txt` 文件：无输出、无报错、state.json 无变化、无源文件创建。用户以为 ingest 成功了。 |
| **根因** | `kdo ingest` 只扫描 `00_inbox/*.md`，其他扩展名被静默忽略 |
| **触发信号** | `ls 10_raw/sources/` 没有新文件产生；state.json 的 `ingested_inbox_files` 列表无新增 |
| **防御措施** | ingest 完成后：① 打印实际处理的文件数量 ② 对 `00_inbox/` 中剩余的非 .md 文件给出 warning ③ 建议在 ingest 前跑 `find 00_inbox -type f` 确认所有文件都是 .md |
| **临时绕过** | `cp file.txt file.md && rm file.txt` 后重新 ingest |
| **关联文件** | `kdo/commands/ingestion.py` |

---

## F-KDO-003: state.json 覆盖写竞态

| 属性 | 内容 |
|------|------|
| **触发命令** | `kdo improve --apply` |
| **表现** | improve 执行后 wiki_snapshots 为空，revision 记录丢失。无报错。 |
| **根因** | `snapshot_wiki_page()` 内部独立调用 `load_state()` + `save_state()`，但调用方 `cmd_improve()` 之后也用自己持有的旧 state dict 写回磁盘，覆盖了 snapshot 的写入 |
| **触发信号** | `kdo improve --apply` 成功但 `.kdo/state.json` 中 `wiki_snapshots` 为空 |
| **防御措施** | ① 代码修复：`snapshot_wiki_page()` 接受调用方的 state dict 参数，不独立读写 ② 所有写 state.json 的函数统一走一个 save 入口 |
| **状态** | 代码已修复（2026-05-01），但问题模式未记录入库 |
| **关联文件** | `kdo/commands/feedback.py`, `kdo/workspace.py` |

---

## F-KDO-004: 错误工作目录执行 pipeline 命令

| 属性 | 内容 |
|------|------|
| **触发命令** | `kdo revise --scan`, `kdo improve --apply` 等 |
| **表现** | 命令静默失败——不报错、不更新文件、不改变 state.json |
| **根因** | 命令依赖 `find_workspace()` 定位 wiki 根目录。从非 wiki 目录（如 `~/.claude/plugins/`）执行时，`find_workspace()` 要么找不到要么找到错误的目录 |
| **触发信号** | 命令返回 0 但无任何文件变化 |
| **防御措施** | ① 命令启动时打印当前识别的 workspace root ② `find_workspace()` 失败时 exit(1) 并给出明确信息而非静默降级 ③ 在 AGENTS.md 禁止清单中列出 |
| **禁止行为** | **不准在 `~/.claude/plugins/` 或任何非 wiki 根目录下执行 KDO pipeline 命令** |
| **正确做法** | 始终 `cd /mnt/c/Users/Administrator/Desktop/wiki` 后执行 |

---

## F-KDO-005: 过期 feedback 引用残留

| 属性 | 内容 |
|------|------|
| **触发命令** | `kdo lint` |
| **表现** | `ERROR: Feedback 'fb_xxx' path does not exist` —— lint 报告一个磁盘上已不存在的文件 |
| **根因** | feedback 的 .md 文件被删除（如 Obsidian 清理），但 state.json 的 `feedback` 列表中仍保留该文件路径 |
| **触发信号** | `kdo lint` 输出 "Feedback path does not exist" |
| **防御措施** | ① `kdo lint` 自动检测并清理 stale feedback 引用（当前只报错不修复）② 定期运行 `kdo self-check` ③ 删除 feedback 文件时同时从 state.json 移除 |
| **清理方法** | `python3 -c "import json; state=json.load(open('.kdo/state.json')); state['feedback']=[f for f in state['feedback'] if 'DEAD_ID' not in str(f)]; json.dump(state, open('.kdo/state.json','w'), indent=2)"` |
| **关联文件** | `.kdo/state.json` → `feedback` 列表 |

---

## F-KDO-006: 骨架页面 CJK 内容损毁

| 属性 | 内容 |
|------|------|
| **触发命令** | `kdo ingest` |
| **表现** | 自动生成的 `30_wiki/concepts/<page>.md` 骨架中，Summary 和 Reusable Knowledge 段落是随机断裂的中文碎片，不可读 |
| **根因** | `kdo ingest` 的 extractor 用 regex 提取段落摘要——`\b` 不识别中文词边界，在随机位置断句。与 F-KDO-001 同一根因。 |
| **触发信号** | 读自动生成的 wiki 页面骨架，中文内容为无意义的碎片拼接 |
| **防御措施** | 这是设计约束而非 bug——CJK extractor 未实现。当前所有 CJK 内容的骨架都是垃圾，需由 Agent 重写 |
| **临时绕过** | ingest 后立即读 wiki 页面，用三步 CJK 编译（浓缩→质疑→对标）完整重写 |
| **关联** | 与 F-KDO-001 共享根因，但触发阶段不同（ingest vs enrich） |

---

## F-KDO-007: 表层翻译式提炼

| 属性 | 内容 |
|------|------|
| **触发场景** | Builder 执行三步编译法的 Condense 阶段 |
| **表现** | Condense 段是课程目录的翻译改写（"本课程属于 XX 模块，与 YY 课程并列"），而非课程核心结论的提取。读者看完 Condense 不知道这门课教了什么独特方法 |
| **根因** | Builder 未阅读源材料（或只有目录级信息），用目录结构+公共知识填充 Condense 段 |
| **触发信号** | Condense 段出现大量"本课程属于""在一堂知识地图中的位置""与同模块其他课程"等目录定位语言，缺少具体方法论描述 |
| **防御措施** | ① L2 Lint：检测 Condense 段是否含 ≥3 条课程特有的核心结论（非目录描述）② Concept Card Step 0 前置检查：Builder 必须回答「源材料的 3 条核心洞见是什么」 |
| **关联案例** | [[yt-entrepreneur-five-step-method.md]]、[[yt-entrepreneur-scientific-method.md]]、[[yt-entrepreneur-fundraising.md]] — 三张模式 A 卡（2026-05-08 审查） |
| **关联** | 与 F-KDO-011（百科词条化）有重叠——表层翻译式提炼是百科词条化的 Condense 段表现形态 |

---

## F-KDO-008: 虚假关联

| 属性 | 内容 |
|------|------|
| **触发场景** | Builder 执行三步编译法的 Synthesis 阶段 |
| **表现** | Synthesis 段的 wikilink 出现以下情况之一：① wikilink 指向自身（A 卡 link 了 A）② 灌水关联（"A 和 B 都是一堂的课"这种无信息量的链接）③ 为满足 ≥2 个 wikilinks 的机械要求而堆砌无关链接 |
| **根因** | Builder 为通过 L2 Lint 的"Synthesis ≥ 2 个 wikilinks"规则而凑数，而非真正寻找知识关联 |
| **触发信号** | Synthesis wikilink 目标与当前卡片的 domain/module 无实质交叉；或 link 了自己 |
| **防御措施** | ① L2 Lint：检测 self-link（直接报 P0）② 审查时检查每个 wikilink 目标页面的内容是否与本卡有实质关联 |
| **关联案例** | [[yt-entrepreneur-scientific-method.md]] Synthesis 段 wikilink 了自己（2026-05-08 审查） |

---

## F-KDO-009: 无质疑接受

| 属性 | 内容 |
|------|------|
| **触发场景** | Builder 执行三步编译法的 Critique 阶段 |
| **表现** | Critique 段出现万能废话——「本卡片基于目录提取，默会知识未完全转化」「课程无法覆盖所有场景」「从知道到做到有鸿沟」——这些话可以粘贴到任何一张知识卡片上。多条 Critique 没有一条指向该课程具体主张的假设或边界 |
| **根因** | Builder 未对课程的具体方法论主张进行批判性思考，用通用质疑模板替代针对性质疑 |
| **触发信号** | 多张不同主题的卡片 Critique 段高度雷同（dist < 20%） |
| **防御措施** | ① L2 Lint：检测 Critique 段是否含「具体假设」「边界」「反例」等指向性关键词② EC 决策第 2 条底线：至少一条 Critique 必须指名具体假设或边界 |
| **关联案例** | 三张模式 A 卡的 Critique 段几乎完全相同（2026-05-08 审查） |

---

## F-KDO-010: 溯源断裂

| 属性 | 内容 |
|------|------|
| **触发场景** | Builder 完成知识卡片后标记 `status: enriched` |
| **表现** | frontmatter 中 `source_refs: []` 为空数组，知识卡片无法追溯到原始材料 |
| **根因** | Builder 在 enrich 阶段未记录源文件引用，或 ingest 阶段未正确设置 source_refs |
| **触发信号** | `kdo lint` 检查 frontmatter 的 source_refs 字段为空或指向不存在的文件 |
| **防御措施** | ① L1 Lint：`source_refs` 为空数组 = P0 阻断，卡片不得标记为 enriched（Sprint 1 实现）② 对标 KF-005（溯源强制） |
| **关联案例** | 2026-05-08 审查的 5 张卡片 source_refs 全部为空；EC 迁移提案痛点 #1（14 broken wikilinks） |
| **关联** | 与 F-KDO-007（表层翻译式提炼）互为因果——无源文件可追溯 → 只能用目录填充 |

---

## F-KDO-011: 百科词条化

| 属性 | 内容 |
|------|------|
| **触发场景** | Builder 创建知识卡片时 |
| **表现** | 概念卡写成百科词条结构——「定义 → 分类 → 特征 → 应用场景」——而非三步编译（浓缩→质疑→对标）。这种卡"看起来完整"但没有经过批判性加工 |
| **根因** | Builder 用百科词条的 mental model 理解"知识卡片"，混淆了"信息整理"和"知识萃取" |
| **触发信号** | 卡片正文缺少 `[Condense]`/`[Critique]`/`[Synthesis]` 区块标记；或标题为「XX 的定义」「XX 的分类」「XX 的应用」 |
| **防御措施** | ① L2 Lint：检测是否包含三步编译法的三个强制区块标记② Concept Card Step 0：Builder 在写卡前必须确认理解三步编译法与百科词条的区别 |
| **关联** | 与 F-KDO-007（表层翻译式提炼）有交叉——百科词条化的卡往往同时有表层翻译式提炼的 Condense |

---

## F-KDO-012: Builder 上下文过载死锁

| 属性 | 内容 |
|------|------|
| **触发场景** | 用户一次性给黄药师派发 ≥3 个独立任务，或任务涉及读取 ≥5 个规范/源文件 |
| **表现** | Token 数长时间零跳动（"Caramelizing…"持续数十分钟），无产出，无文件变更。用户观察到的直接表现：Agent 卡死，需要 `/new` 重开 |
| **根因** | 入职流程（CLAUDE.md）要求读取 5+ 个规范文件，加上任务上下文 + 被操作文件，总上下文消耗 >50%。剩余窗口不足以完成推理+输出。Agent 进入过度分析循环无法退出 |
| **触发信号** | ① 给黄药师的单条指令含 ≥3 个文件操作目标 ② 指令引用了 ≥2 个规范文件 ③ Agent 执行时间 >20 分钟无产出 |
| **防御措施** | ① **单轮单任务**：给黄药师每次只发 1 个任务（≤5 分钟可完成）② **不引规范**：纯执行指令不引用 PROTOCOL.md / 工业化手册 / failure-modes.md ③ **`/new` 接力**：大任务拆成多个 `/new` 会话，每个会话做一步 ④ AGENTS.md 禁止清单 #7 |
| **事故记录** | 2026-05-09：Sprint 1 Lint 修复卡死（56 分钟零产出）→ `/new` 后单任务执行成功 2026-05-09：Sprint 2 设计审查响应后卡死 → 待 `/new` 恢复 |

---

## 执行前自检清单

每个 Agent session 启动时，对照此清单：

```
□ F-KDO-001: 处理的页面是中文内容？→ 跳过 kdo enrich，走 Agent 三步编译
□ F-KDO-002: 00_inbox/ 有非 .md 文件？→ 先转换再 ingest
□ F-KDO-003: 即将执行 improve --apply？→ 确认 state.json 可写且无其他进程持有
□ F-KDO-004: 当前工作目录是 wiki 根目录？→ pwd 确认
□ F-KDO-005: 删除过 feedback 文件？→ 同步清理 state.json
□ F-KDO-006: ingest 中文源文件后？→ 立即读骨架页面，准备重写
□ F-KDO-007: Condense 是课程目录改写还是核心结论提取？→ 检查是否含 ≥3 条课程独有方法论
□ F-KDO-008: Synthesis wikilink 是实质关联还是凑数？→ 检查每个 link 目标页内容是否相关
□ F-KDO-009: Critique 是万能废话还是指名假设边界？→ 至少一条指向具体前提假设
□ F-KDO-010: source_refs 是否为空？→ 不得标记 enriched 如果为空
□ F-KDO-011: 卡片是三步编译还是百科词条？→ 检查 [Condense]/[Critique]/[Synthesis] 区块
□ F-KDO-012: 给黄药师的任务是否 ≤1 个、≤5 分钟、未引用规范文件？→ 单轮单任务
□ F-KDO-012: 黄药师的会话是否 >20 分钟无产出？→ token 零跳动 = 卡死，立即 `/new`
```

---

> 更新规则：每次发现新模式 → 追加到此文件 → 更新索引表 → 更新执行前自检清单。
> 退役规则：当防御措施已自动化（如代码修复 + CI 门禁），将状态改为"已退役"而非删除。
