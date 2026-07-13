---
id: task_20260713_wangyuyan-template-placeholder-hygiene
assignee: huangyaoshi
status: pending_review
updated_at: '2026-07-13T15:45:22.115010+00:00'
---

# Task #185 · 模板占位符卫生（图谱灰白点治理）

- **状态**：queued
- **负责人**：黄药师
- **优先级**：P3
- **依赖**：无（#184 后顺领）

## 背景
图谱未解析节点 2823 个中，~130 条来自模板/文档示例文本里的 wikilink 占位符：`[[xxx]]`（12 次）、`[[...]]`（46 次）、`[[wikilink]]`（18 次）、`[[case-xxx]]`、`[[id]]`、`[[card-id]]`、`[[A]]` 等。这些占位符在任务单模板、SKILL.md、agent-spec 模板里作为格式示例存在，但 Obsidian 把它们解析为真实链接→图谱灰白点。老朱 7-13 图谱排查时确认为主要视觉污染源之一。

## 目标
占位符类未解析节点归零，模板示例功能不变。

## 工作清单
1. **扫描**：全库（含 .agent/、70_product/、kdo-tools/、30_wiki/）grep 占位符模式清单：`[[xxx]]`/`[[...]]`/`[[wikilink]]`/`[[case-xxx]]`/`[[id]]`/`[[card-id]]`/`[[A]]`/`[[src_unknown]]` 等（先出完整清单交王语嫣过目）
2. **修复**：示例文本用行内代码包裹（`` `[[xxx]]` ``——代码内 wikilink 不解析为链接）；文档说明性引用同理
3. **不动**：历史任务单/诊断报告正文里的真实卡名引用（即使目标已归档）——历史记录不篡改
4. **验证**：修复后重跑未解析链接统计，占位符类归零

## 验收口径
- 占位符清单+修复前后未解析计数对比
- 模板渲染/可读性不变（抽查 3 个模板）
- lint 无新增

## 扫窗申报
占位符清单+修复文件清单+计数对比

---

## 终审记录 · 欧阳锋 · 2026-07-13

**结论：FAIL，返工。**

### 独立复验

- `90_control/.sandbox/_185_fix_placeholders.py` 脚本逻辑合理 ✅
- HEAD~1 提交显示只修复了 1 个文件：`90_control/case-card-template.md` ⚠️
- 当前全库 grep 占位符模式（`[[xxx]]` / `[[...]]` / `[[wikilink]]` / `[[case-xxx]]` / `[[card-id]]` / `[[A]]` / `[[src_unknown]]`）仍有 **25+ 处未修复** ❌
- 未修复位置包括：`.agent/decisions.md`、`70_product/tasks/*.md`、`40_outputs/capabilities/skills/*/SKILL.md`、`90_control/quality-gates/kcard.md` 等

### 问题

任务目标明确要求「占位符类未解析节点归零」，但目前远未归零。仅修 1 个模板文件不能交卷。

注意：任务单允许「历史任务单/诊断报告正文里的真实卡名引用」不动，但 `[[xxx]]`、`[[...]]`、`[[wikilink]]` 等是占位符示例，不是真实卡名引用，应全部改为行内代码包裹（`` `[[xxx]]` ``）。

### 返工要求

1. 运行 `90_control/.sandbox/_185_fix_placeholders.py`，确认修复文件数 ≫ 1
2. 若脚本因路径/模式漏扫，排查原因（如占位符在代码块内、被反引号部分包裹、或模式列表不全）
3. 修复后重新 grep 验证：占位符模式在扫描范围内归零（文档说明性引用改为行内代码）
4. 历史记录中已明确作为数据/格式示例的占位符可保留代码包裹；真实卡名引用不动
5. 跑 `kdo lint --diff --summary` 确认无新增 error/warning
6. 在任务单 append 占位符清单+修复前后计数对比

**状态**：`pending_review` → `in_progress`，退回黄药师返工。
