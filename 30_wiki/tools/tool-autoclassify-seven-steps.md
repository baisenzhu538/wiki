---
id: tool-autoclassify-seven-steps
title: 自动分类脚本 7 步：inbox 到目录的自动化流水线
type: tool
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
- 自动分类脚本
- 分类脚本7步
- LongCat模型分类
- T1强制quality
- MUSE目录
- OCR_一堂DOC-20260816015732
- OCR_一堂DOC-20260816015732.md
- OCR_一堂DOC-20260816015737
- OCR_一堂DOC-20260816015737.md
- AI知识库
tags:
- audience:executor
- scene:execution
- skill-level:intermediate
source_person: 楚门
source_context: AI×知识管理探索营（2026-08-15 晚直播）——自动分类（L3290-3310 + 015732/015737）
source_refs:
- 00_inbox/AI知识库/OCR_一堂DOC-20260816015732.md
- 00_inbox/AI知识库/OCR_一堂DOC-20260816015737.md
related:
- '[[framework-serendipity-five-channels]]'
- '[[framework-patrolkit-radar]]'
- '[[framework-knowledge-five-leaps]]'
- '[[tool-knowledge-cheatsheet-sab]]'
- '[[framework-truman-agent-team-architecture]]'
- '[[concept-session-vs-memory-vs-document]]'
- '[[dk-ai-builder-illusion]]'
- '[[case-cross-xingangwan-pharma]]'
- bridge-how-to-know-person-to-business
---

# 自动分类脚本 7 步：inbox 到目录的自动化流水线

> 本卡属于「AI×知识管理」体系（楚门探索营第五次飞跃·体系自动化，L3290-3310 + 015732/015737 图）：自动分类脚本——把 inbox 里的文章按规则自动分类到目录（MUSE 目录结构），7 步流水线：提取字段→关键词预匹配（仅参考）→LongCat 模型分类→结果校验（T1 强制 quality:S）→写 frontmatter→移动文件→审计日志。本质：采集自动化之后连分类都自动化（L3298）。

## 1. 工具定义

自动分类脚本 7 步（015732/015737 图，已 OCR）：

| 步骤 | 动作 | 细节 |
|:--|:--|:--|
| Step 1 | 提取文章字段 | 标题/摘要/正文前 500 字/来源类型/收藏时间 |
| Step 2 | 关键词预匹配 | 记录但不直接使用（作为模型参考输入） |
| Step 3 | LongCat 模型分类 | 输入：标题+摘要+正文+关键词建议；输出：目录 ID/标签/质量等级/SS 课题/置信度；内部先执行 T1（CEO 核心课题）扫描 |
| Step 4 | 结果校验与修正 | 校验目录 ID 有效/标签在标签库内；T1 命中强制 quality:S |
| Step 5 | 写入 frontmatter | 文件头部插入 YAML 元数据 |
| Step 6 | 移动文件 | 创建目录（如不存在）+移动文件到目标目录 |
| Step 7 | 生成分类日志 | 记录每篇文章（审计） |

## 2. 关键设计

- **关键词预匹配仅参考**（Step 2）："记录但不直接使用"——避免规则误分类（L3302-3304"能做但是不准，需要很多规则"）
- **T1 强制 quality:S**（Step 4）：CEO 核心课题命中即升级质量等级——高层课题优先
- **frontmatter 审计**（Step 5/7）：YAML 元数据+分类日志——可追溯
- **MUSE 目录**（015732）：阅读库目录结构（分类的落点）

## 3. 使用步骤

1. 文章进 inbox（00-Cubox_Inbox 原始入口）
2. 脚本提取字段 → 关键词预匹配（仅参考）
3. LongCat 模型分类（带关键词建议）
4. 校验（目录 ID/标签/T1 强制 S）
5. 写 frontmatter → 移动文件 → 审计日志

## 4. When NOT to Use

1. **文章量少**——手动分类更快（脚本成本高）。
2. **目录体系未定**——没有稳定目录结构前自动化分类无意义。
3. **无模型可用**——LongCat 这类分类模型是核心依赖。

## 5. 失败模式

| 失败模式 | 真实信号 | 修复动作 |
|:--|:--|:--|
| 规则不准 | 分类错误率高 | 关键词只作参考+模型分类（Step 2-3） |
| T1 漏标 | 核心课题被埋 | T1 扫描+强制 quality:S（Step 4） |
| 无审计 | 分类错了找不到 | Step 7 分类日志（审计追溯） |
| 目录不存在 | 移动失败 | Step 6 自动创建目录 |

## 6. Action Triggers

- inbox 文章堆积 → 上自动分类脚本
- 分类靠人工且量大 → 7 步流水线自动化
- 需要质量分级 → T1 强制 quality:S（核心课题优先）

## 7. 与其他知识的关联

- `framework-serendipity-five-channels`：五通道采集后的分类环节（采集+分类=完整自动化）
- `framework-patrolkit-radar`：分类后巡检（资产雷达配套）
- `framework-knowledge-five-leaps`：自动分类=第五次飞跃的组成
- `tool-knowledge-cheatsheet-sab`：质量分级（S/A/B）与 quality:S 同构
- `framework-truman-agent-team-architecture`：分类结果供 Agent 团队调用
- `concept-session-vs-memory-vs-document`：frontmatter=文档元数据（AI 可读）
- `dk-ai-builder-illusion`：模型分类不可全信（校验步骤防幻觉）（跨域）
- `case-cross-xingangwan-pharma`：决策域实证（跨域）
- `bridge-how-to-know-person-to-business`：跨域补充（决策域/组织域实证）
