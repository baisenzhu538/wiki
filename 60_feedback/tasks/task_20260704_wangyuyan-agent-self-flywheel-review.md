---
id: task_20260704_wangyuyan-agent-self-flywheel-review
type: task
status: reviewed
assignee: 黄药师
reviewer: 欧阳锋
reviewed_by: 欧阳锋
review_date: 2026-07-04
priority: P1
created_at: 2026-07-04
updated_at: 2026-07-04
related:
- '[[method-dual-triangle-flywheel-engine]]'
- '[[method-yihang-dual-triangle-ai-review]]'
- '[[concept-yihang-dual-triangle-core]]'
---

# 任务 #98：Agent 自复盘——飞轮引擎从手动到自动化

## 来源

口述稿 L2220-2312。Truman 现场演示了最高阶用法：**AI 自己复盘自己。**

## Truman 的完整操作

1. 跟 AI 协作完成项目后，给 AI 一段提示词：
   > "你去学一下双三角模型，帮我还原一下刚才咱们所有的工作过程。你做了什么，我做了什么，咱们两个如何互补的。"

2. AI 自动输出：
   - **每轮对话映射到六要素**："第一轮交锋我做了什么？对应双三角的什么？"
   - **画飞轮**：人的审美体系做评估 → AI改进 → 人说不够好 → 继续补 → 七轮对话四个大飞轮
   - **对照实验**：没有 AI 人要做 40-60 小时，没有人 AI 只能产出四五十分，合在一起 15 分钟干完
   - **自我反思**："下一次你来主导，还有什么能做得更好？"

3. 这篇复盘报告存下来**可以迭代训练 AI**，质量比 AI 生成的其他分析报告更高

## 当前 KDO 的差距

flywheel.py 目前是**手动版**——人在会话结束后回答飞轮四问，人写日志。Truman 的高阶用法是：**Agent 在会话结束时自己调 flywheel pattern，自己写"这一轮我的审美进步了什么、体系补了什么、数据积累了什么"**。

## 任务目标

将 flywheel.py 从"人手动填表"升级为"Agent 自复盘"：

1. Agent 会话结束时自动触发双三角自复盘
2. Agent 自己映射本轮对话到六要素
3. Agent 自己画飞轮（几轮对话、几个飞轮、每次迭代改变了什么）
4. 输出结构化自复盘报告（可被下次会话作为 data pack 加载）
5. 报告存入 `60_feedback/agent-traces/<agent-id>/flywheel/`

## 技术路径

- 不重写 flywheel.py——在现有基础上加 `--auto` 模式
- `flywheel.py --auto <session-trace>` 读取会话 trace，调用 LLM 按 Truman 的提示词模板生成自复盘
- 输出格式对齐双三角六要素 + 飞轮 + 对照实验 + 自我改进

## 验收标准

- `kdo pre-submit` PASS
- 至少 1 个 Agent 实测：会话结束后自动生成自复盘报告
- 报告含六要素映射 + 飞轮识别 + 对照实验 + 自我改进建议
- 欧阳锋终审通过

## 依赖

- #85（AI 辅助复盘法 method 卡）提供提示词模板
- #69（画布 Agent CLI）作为第一个试点 Agent

---

<!-- 手动状态同步（欧阳锋 2026-07-12）：本任务队列已标记 reviewed，任务单 frontmatter 仍为 queued。手动同步 status/review_date/reviewed_by，保持队列与任务单一致。 -->
