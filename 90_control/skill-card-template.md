# Skill 卡模板

> 技能卡记录**程序性知识**——"怎么做、什么时候做、用什么工具做"。和概念卡（"是什么"）、暗知识卡（"不要做什么"）互补。

## Frontmatter

```yaml
---
id: skill-{domain}-{short-name}
title: "技能：{动词开头的一句话描述}"
type: skill
status: draft
domain:
  - {领域1}
  - {领域2}
source_person: {谁说的}
source_context: {什么场合，日期}
source_refs:
  - {口述稿/课程路径}
wiki_refs:
  - {关联的概念卡}
definition_of_done:
  - 操作步骤清晰可执行
  - 适用场景有正反例
  - 工具要求明确
tags:
  - "#skill/{子类}"
  - "#tool/{需要什么工具}"
created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD
tools_required:
  - {工具1}
  - {工具2}
prerequisite_skills:
  - {前置技能卡 id}
related:
  - {关联卡 id}
---
```

## 正文结构

```markdown
# 技能：{标题}

## 原始表述
> {谁说的，原文引用。保留口语感，方便追溯}

## 操作步骤
1. {第一步}
2. {第二步}
3. {第三步}

## 适用场景
- ✅ {什么时候用}
- ✅ {什么时候用}
- ❌ {什么时候不用}
- ❌ {什么时候不用}

## 为什么有效
{背后的原理。不要只说"经验"，解释机制。}

## 工具/环境
- {需要什么工具，版本，获取方式}
- {环境要求}
- 备用方案：{如果主方案不可用}

## 常见失败模式
- {失败现象} → {原因} → **{解决方案}**
- {失败现象} → **{解决方案}**

## 关联技能
- [[skill-xxx]] — {关系说明}
- [[concept-xxx]] — {关系说明}

## 来源
- {谁}，{场合}，{日期}

## Feedback Path
- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
```

## 检查清单（提交前自检）

- [ ] 操作步骤至少 2 步，编号清晰
- [ ] 适用场景有"要用的"和"不要用的"两种
- [ ] 有至少一条常见失败模式
- [ ] wiki_refs 链接到已有的概念卡
- [ ] `kdo validate --all` 通过
