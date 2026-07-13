# Skill 卡模板（统一标准 v1.0）

> 技能卡记录**程序性知识**——"怎么做、什么时候做、用什么工具做"。
> 与概念卡（陈述性知识）和暗知识卡（负向经验）互补。

## Frontmatter 必填字段

```yaml
---
id: skill-{domain}-{short-name}
title: 技能：{动词开头的一句话}
type: skill
status: draft
domain: []
source_person: {谁说的}
source_context: {场合，日期}
source_refs: []
wiki_refs: []
definition_of_done:
  - 操作步骤清晰可执行
  - 适用场景有正反例
  - 工具要求明确
tags:
  - "#domain/{领域}"          # 必填：领域标签
  - "#skill-type/{类型}"      # 必填：技能类型
  - "#tool/{工具名}"          # 可选：依赖的工具
  - "#method/{方法名}"        # 可选：方法论标签
tools_required: []
prerequisite_skills: []
related: []
created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD
---
```

### 标签三层体系

| 层级 | 前缀 | 示例 | 说明 |
|:------|:-----|:-----|:-----|
| 领域 | `#domain/` | `#domain/AI`, `#domain/embedded` | 知识所属领域 |
| 技能类型 | `#skill-type/` | `#skill-type/input-method`, `#skill-type/validation` | 技能的操作类型 |
| 工具/方法 | `#tool/`, `#method/` | `#tool/doubao-input`, `#method/checklist` | 依赖或方法论 |

### 技能类型枚举

| 类型 | 说明 | 例子 |
|:------|:-----|:-----|
| `input-method` | 输入类 | 语音输入、快捷指令 |
| `setup` | 搭建/配置类 | 工作空间搭建、环境配置 |
| `validation` | 验证/检查类 | 证据核查、平行验证 |
| `execution` | 执行/落地类 | 五步落地法 |
| `evaluation` | 评估/判断类 | 需求验证、偏差识别 |
| `documentation` | 文档/记录类 | PRD写作、笔记方法 |
| `checklist` | 清单类 | 区分清单、评估清单 |

## 正文必填章节

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
- ❌ {什么时候不用}

## 为什么有效
{背后的原理。不要只说"经验"，解释机制。}

## 工具/环境
- {需要什么工具}
- 备用方案：{如果主方案不可用}

## 常见失败模式
- {失败现象} → {原因} → **{解决方案}**

## 关联技能
- [[skill-xxx]] — {关系说明}
- `[[concept-xxx]]` — {关系说明}

## 来源
- {谁}，{场合}，{日期}

## Feedback Path
- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
```

## 提交前自检

- [ ] `type: skill`，`id` 前缀 `skill-`
- [ ] 操作步骤编号清晰，至少 2 步
- [ ] 适用场景有 ✅ 和 ❌ 两种
- [ ] 至少一条常见失败模式
- [ ] 标签三层体系完整（领域+类型+工具/方法）
- [ ] `kdo validate --all` 通过
- [ ] `kdo cards --type skill` 可检索到
