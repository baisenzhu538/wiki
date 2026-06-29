---
id: task_20260629_vikki-info-emotion-skill-upgrade
type: task
status: queued
assignee: 老顽童(Hermes)
priority: P2
created_at: 2026-06-29
updated_at: 2026-06-29
reviewed_by: 欧阳锋
reviewer: 欧阳锋
source_refs:
- 00_inbox/AI-study/0071Vikki战队-2群 · 认知精华提炼.md
related:
- 30_wiki/skills/content-production-polish
- framework-kdo-content-standards
---

# Vikki「信息 × 情绪」模型融入 content-production-polish skill

## 目标

将 Vikki 战队群聊中提炼出的「信息是弹头，情绪是制导系统」二元模型，系统性地写入 `40_outputs/capabilities/skills/shared/content-production-polish/SKILL.md` 与 `human-speech-rules.md`，提升现有讲人话 skill 的理论深度和可操作性。

## 待融入核心洞察

1. **信息 × 情绪 二元模型**
   - 信息是弹头：承载认知增量、判断、框架
   - 情绪是制导系统：决定用户是否愿意听、是否记得住、是否行动
   - 核弹（纯信息）和导弹（纯情绪）搭配起来效果才最大

2. **信息密度类比**
   - 信息密度太高 → 认知负荷 → 不自觉紧张
   - 像酒精浓度，单位能耗过高
   - 唠嗑聊天 > 书面语，信息密度适中才有效

3. **表达方式差异**
   - 读书和讲课是不同的表达方式
   - 像新闻播音员一样说话 → 有距离感
   - 好的内容出现在和朋友聊天中，互相激发

4. **情绪流动性**
   - 除了信息传递，还要有情绪流动性
   - Gemini 案例：能像闺蜜一样提供情绪价值

## 执行要求

1. 在 `SKILL.md` 的 Core Standard 中增加「情绪制导」维度，与「听得懂/听得下去/信得过/用得上」并列或融合。
2. 在 `human-speech-rules.md` 中新增方法 #13「信息 × 情绪配比法」，结构遵循：Problem → Fix → Pattern → Hard vs Human → Why it works。
3. 提供至少 3 个跨域示例（AI/商业、亲子教育、销售）。
4. 更新 skill 后，跑 `kdo pre-submit -f <skill文件>` 验证。

## 验收标准

- `SKILL.md` 和 `human-speech-rules.md` 通过 `kdo pre-submit`
- 新增内容不破坏原有 12 条方法编号
- 欧阳锋抽查：新增方法必须有具体场景 + 可执行 Pattern + 跨域示例
