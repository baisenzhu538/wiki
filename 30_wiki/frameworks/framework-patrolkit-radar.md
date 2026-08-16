---
id: framework-patrolkit-radar
title: PatrolKit 知识资产雷达：自动巡查与资产回收系统
type: framework
status: pending_review
author: 老顽童
reviewed_by: 待审
confidence: 0.85
trust_level: medium
language: zh-CN
created_at: 2026-08-16
updated_at: 2026-08-16
domain:
- knowledge-management
- ai-collaboration
aliases:
- PatrolKit
- 知识资产雷达
- 自动巡查系统
- 资产回收
- 健康检查记忆补全技能迁移
- OCR_一堂DOC-20260816015759
- OCR_一堂DOC-20260816015759.md
- 楚门-AI知识管理探索营-口述
- 楚门-AI知识管理探索营-口述.txt
- AI知识库
tags:
- audience:manager
- scene:planning
- skill-level:advanced
source_person: 楚门
source_context: AI×知识管理探索营（2026-08-15 晚直播）——在测系统（015759 已人工核验 1 处纠偏 + L3290-3346）
source_refs:
- 00_inbox/AI知识库/OCR_一堂DOC-20260816015759.md
- 00_inbox/AI知识库/楚门-AI知识管理探索营-口述.txt
related:
- '[[tool-autoclassify-seven-steps]]'
- '[[framework-serendipity-five-channels]]'
- '[[framework-knowledge-five-leaps]]'
- '[[framework-knowledge-compound-rocket-six]]'
- '[[framework-truman-agent-team-architecture]]'
- '[[concept-session-vs-memory-vs-document]]'
- '[[dk-ai-builder-illusion]]'
- '[[case-cross-xingangwan-pharma]]'
- bridge-how-to-know-person-to-business
---

# PatrolKit 知识资产雷达：自动巡查与资产回收系统

> 本卡属于「AI×知识管理」体系（楚门探索营在测系统，015759 图已人工核验 1 处纠偏 + L3290-3346）：从手动知识整理升级为半自动巡查与资产回收系统——Before（知识资产散落：做完就丢/靠人想起/经验锁在本地）→ Process（自动巡查+模型分析：健康检查/记忆补全/资产回收/技能迁移）→ After（知识复利飞轮）。本质：别靠人驱动萃取，靠知识资产雷达自动巡查（L3326-3328）。0.18 原型。

## 1. 核心洞察

知识管理最巅峰的设想（L3332-3340）：**一套足够熟悉你审美和工作体系的 AI 系统，自动把散落在各处的知识资产抽离出来**——session 精华、会议片段、技能草案、经验教训——沉淀到知识库里，用日报周报方式带着你讲。当前靠人肉驱动萃取（L3324："其实都是人不断的在从业务实践场景去萃取经验和知识放到知识库里"），PatrolKit 想把这个驱动自动化。

## 2. 系统架构（015759 已核验）

```
Before：知识资产散落
  Codex 会话 / Claude Code 会话 / Obsidian 文档 / 飞书材料
  （做完就丢 / 靠人想起 / Prompt 模版 / 设计图片 / Skill 草案 / 服务日志 / 手动搜索 / 经验锁在本地）
  → 高价值经验难回流

Process：自动巡查 + 模型分析
  输入源：MacBook / Obsidian Vault / Codex memories / Skills 目录 / 飞书 / Flomo
  → PatrolKit 知识资产雷达引擎
  | 模块 | 功能 |
  | A 健康检查 | 健康码（知识库健康度） |
  | B 记忆补全 | 断点在哪（记忆缺口） |
  | C 资产回收 | 什么是沉淀（经验萃取） |
  | D 技能迁移 | 谁该抢滩（技能复用） |
  → 聚合 / 分类评分 / 资产识别

After：知识复利飞轮（0.18 原型）
```

## 3. 四模块

| 模块 | 检查什么 | 输出 |
|:--|:--|:--|
| A 健康检查 | 知识库健康度（健康码） | 健康报告 |
| B 记忆补全 | 记忆断点在哪 | 缺口清单 |
| C 资产回收 | 什么是沉淀（session/会议精华） | 资产建议 |
| D 技能迁移 | 谁该抢滩（技能复用给其他 Agent） | 迁移建议 |

## 4. 使用步骤（当前人肉版先行）

1. **日常萃取**：做完一段工作 → "这段还不错帮我抽个 skill""这段错误值得分享写个 case study"（L3318-3324）
2. **巡查输入源**：Codex 会话/Claude Code 会话/Obsidian/飞书/Flomo——定期扫
3. **四模块检查**：健康检查/记忆补全/资产回收/技能迁移
4. **沉淀回知识库**：精华 → 技能进化日志/错误模式库/case 库
5. **目标**：自动化替代人肉驱动（PatrolKit 0.18 原型）

## 5. When NOT to Use

1. **知识量小**——还没到"资产散落"规模时不需要雷达。
2. **人肉萃取已覆盖**——每日复盘+技能日志习惯健全时可延后自动化。
3. **工具未打通**——输入源（Codex/Obsidian/飞书）未接入时雷达无数据。

## 6. 失败模式

| 失败模式 | 真实信号 | 修复动作 |
|:--|:--|:--|
| 只采不巡 | 知识库堆积不回流 | 四模块定期巡查（健康检查优先） |
| 只巡不沉 | 巡查报告没人看 | 用日报周报方式带着讲（L3330） |
| 人肉依赖 | 萃取靠人想起 | 自动巡查替代（雷达目标） |
| 过度自动化 | 误抽/误沉 | 分类评分+资产识别（人确认） |

## 7. Action Triggers

- 知识资产散落（做完就丢/经验锁本地） → 上 PatrolKit 四模块巡查
- 高价值经验难回流 → 资产回收模块（C）+技能迁移（D）
- 复盘靠人肉驱动 → 自动巡查（K1：KDO Session 资产自动回收机制同源）

## 8. 与其他知识的关联

- `tool-autoclassify-seven-steps`：自动分类=PatrolKit 的输入预处理（配套）
- `framework-serendipity-five-channels`：采集五通道=PatrolKit 的素材来源
- `framework-knowledge-five-leaps`：PatrolKit=第五次飞跃（体系自动化）的巅峰设想
- `framework-knowledge-compound-rocket-six`：自动化引擎=PatrolKit 的定位
- `framework-truman-agent-team-architecture`：巡查对象=各 Agent 的产出（session/技能）
- `concept-session-vs-memory-vs-document`：session 精华=资产回收的对象
- `dk-ai-builder-illusion`：自动巡查不可全信（人工确认环节）（跨域）
- `case-cross-xingangwan-pharma`：决策域实证（跨域）
- `bridge-how-to-know-person-to-business`：跨域补充（决策域/组织域实证）
