---
id: tool-darwin-skill
title: darwin-skill：Skill 自我进化器（评估→改进→实测→棘轮保留/回滚，人在回路）
type: tool
status: draft
confidence: 0.9
trust_level: high
language: zh-CN
created_at: 2026-08-19
updated_at: 2026-08-19
domain:
- knowledge-management
- ai-collaboration
- infrastructure
aliases:
- darwin
- darwin-skill
- 达尔文
- skill 自我进化
- skill 优化器
- skill 评分
discoverable_by:
- 优化 skill
- skill 评分
- skill 自我进化
- 达尔文
- darwin
- skill 质量检查
author: 黄药师（登记）；原作者 花叔 alchaincyf
reviewed_by: 待审
source_refs:
- 40_outputs/capabilities/skills/darwin-skill/SKILL.md
- 30_wiki/cases/case-wechat-e7536bf1d8f1a7b1.md
related:
- tool-cangjie-skill
- tool-yizhan-shendeng
tags:
- audience:all-agents
- scene:execution
- method:automation
- content-format:tool
quality_labels:
- actionable
- validated
- cited
diagnostic_signals:
- signal: 用户说"优化 skill/skill 评分/skill 自我进化/帮我改改 skill"
  lens: darwin 是生态里的进化件——nuwa 蒸人、仓颉蒸书、darwin 让 skill 持续进化
  follow_up: 调用 40_outputs/capabilities/skills/darwin-skill/SKILL.md 的评估→改进→实测→棘轮循环
---

# darwin-skill（Skill 自我进化器）

> 作者：花叔 alchaincyf（GitHub，MIT，v2.1）。
> 仓库：https://github.com/alchaincyf/darwin-skill
> 本地副本：`40_outputs/capabilities/skills/darwin-skill/`（2026-08-19 经 gh-proxy 克隆，含 docs/references/scripts/templates 全套）

## 能力

对任意 SKILL.md 做**自主优化循环**：评估 → 改进 → 实测验证 → 人类确认 → 保留或回滚（棘轮，只留改进）→ 生成成果卡片。

- **9 维评分 rubric**（满分 100）：结构 59（frontmatter/工作流/失败模式编码/检查点/可执行具体性/资源整合）+ 效果 35（架构/实测表现）+ meta 6（反例黑名单）——基于微软研究院 SkillLens（arXiv 2605.23899）+ SkillOpt（arXiv 2605.23904）
- **paired 同 judge 比较 + 奇数 N 多数决**：keep/revert 不看绝对分（judge 噪音 ±8），看同一评委前后对比——治"换尺污染"
- **独立 judge 盲评**：避免"自己改自己评"
- **git 棘轮**：每个候选改进一个 commit，退步自动回滚
- **人在回路**：每个 skill 优化完暂停等人确认

## 安装位置

| 环境 | 路径 |
|:--|:--|
| KDO | `40_outputs/capabilities/skills/darwin-skill/` |
| WorkBuddy | `~/.workbuddy/skills/darwin-skill/`（2026-08-19 已装） |

## 与生态的咬合

- **仓颉蒸书 → darwin 压力测试/进化**：仓颉阶段 4 的压力测试即 darwin 兼容格式（test-prompts.json）
- **一盏神灯/distill-own-skill 蒸出来的技能包**：跑 darwin 循环持续调优
- 轻量替代：`distill-own-skill` 内置的"成长功能"（每次使用后收集反馈迭代）适合日常小步进化；darwin 适合集中式大优化

## 边界

- 绝对总分只用于粗排（哪支最弱先改谁），keep/revert 必须走 paired 比较
- dry_run 比例 >30% 评估失效——实测维度需要能真跑测试 prompt
- 重要决策必须人审（rubric 对 fine-grained 差异不可信，作者自己标注）
