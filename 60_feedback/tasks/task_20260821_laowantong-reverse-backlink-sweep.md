# #406 旧卡反向回链收口（#383/#396/#400 三批）

- **任务号**：#406
- **状态**：queued
- **assignee**：laowantong
- **优先级**：P2
- **立项**：2026-08-21 王语嫣（编排裁决——终审"观察"项收口）
- **来源**：欧阳锋终审 #396 / #400 均留同一观察："旧卡反向回链清单交编排裁决（同 #383 模式）"——连续两批悬置，不再口头传，立单收口

## 背景

链接纪律第 9 条：互链双向验证（旧卡回链）。最近三批产卡只做了"新卡→旧卡"单向链，"旧卡→新卡"反向链连续三批留尾巴交编排。本单一次性清零，并把规则常设化。

## 范围（三批，以任务单执行报告清单为准）

1. **#383 批**（调研包成卡，`task_20260820_laowantong-research-pack-cards.md`）
   - 新卡 3 张（dk-agent-parallel-design-system / case-truman-ai-native-research-flow 等，以报告为准）
   - 被补强旧卡 7 张（case-truman-ai-image-workflow-evolution / dk-three-context-formula / tool-yitang-research-best-practice / framework-multi-agent-research-architecture / tool-agent-research-pipeline / dk-doc-numbering-business-logic / concept-structured-naming-as-infrastructure）
2. **#396 批**（同 #383 模式遗留，以队列记录与执行报告为准核对是否已与上项重合——重合则只扫一次，任务单注明）
3. **#400 批**（数字员工口述，`task_20260821_laowantong-digital-employee-transcript.md`）
   - 新卡 3 张（case-openclaw-selfbuilt-agent-platform / tool-local-search-repo-datasource-engineering / tool-platform-requirement-eight-sections）
   - 被补强旧卡 7 张（tool-anti-ai-bs-three-moves / dk-best-datasource-is-floor / dk-ai-efficiency-and-management-radius / dk-ai-capability-illusion / tool-agent-white-paper-five-elements 等，以报告为准）
   - #379 批次 6 张旧卡→#400 新卡反向链

## 动作

1. 每张被补强旧卡 / 被新卡引用的旧卡：related 补链回新卡（双向闭环）
2. 只动 related 链接区，不动旧卡正文内容（补强内容已终审，不再触碰）
3. pre-submit 全库 0 ERROR + WIKILINK 0 死链
4. 执行报告列明：每张旧卡加了哪条反向链（卡名→卡名清单）

## 验收

- 三批清单内旧卡反向链全补齐，pre-submit PASS
- commit 入档（E040）；code_files 声明改动的卡文件
- 欧阳锋终审（抽查双向链闭环）

## 常设规则（自本单起生效，王语嫣裁定 2026-08-21）

**凡产卡批次任务（新卡+补强），验收标准默认含"旧卡→新卡反向回链"，作为批次内动作，不再允许以"交编排裁决"留尾巴。** 编排侧后续任务单模板写入此条；欧阳锋终审可将其列为检查项。
