---
id: dk-tool-chain-naming-is-infrastructure
title: 命名不规范会让整条工具链"失明"
type: dk
dark_knowledge_type: cross-domain-pattern
status: enriched
domain:
- master
- kdo
- yitang
source_person: KDO 团队复盘
source_context: 第26-27节精修中反复出现：source ID、文件名、正则边界、YAML 命名导致解析失败
source_refs:
- src_unknown
related:
- '[[yitang-domain-digest]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
- '[[pending_unknown]]'
bridges_to:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
author: 老顽童
reviewed_by: 欧阳锋
review_date: '2026-06-19'
confidence: 0.88
trust_level: medium
diagnostic_signals:
- signal: src_unknown
  framework_lens: 命名超出正则
  follow_up_question: 这个命名能否被当前工具链的正则/解析器唯一识别？如果不能，是否需要改名或改规则？
- signal: src_unknown
  framework_lens: 命名边界不一致
  follow_up_question: 失效卡片的命名是否与有效卡片存在字符长度、分隔符、编码差异？
- signal: src_unknown
  framework_lens: 人眼与机器解析不一致
  follow_up_question: 是否有别名、特殊字符、过长 ID 导致解析器只能识别前半段？# 命名不规范会让整条工具链"失明"
updated_at: 2026-06-28
---

## 原始表述 / 核心洞察

在第 26、27 节精修中，同一类问题反复出现：

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

**核心洞察**：命名不是"怎么好读怎么写"的装饰，而是工具链能够识别、索引、校验、链接的基础设施。一旦命名超出正则、解析器、链接器的能力边界，整条工具链就会"失明"——它看不到完整信息，只能看到前半段、错误段，或者根本看不到。人眼觉得对，机器已经错了。

## 原始表述

- src_unknown（待补充来源原话）

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **先定义解析规则，再命名**：在创建新的 id/文件名/字段前，先写出能匹配它的正则。如果正则写不出来，说明命名不规范。
2. **强制通过 gate/正则验证**：新增命名必须先跑一次工具链检查，确认能被唯一识别。
3. **避免使用解析器的保留字符**：
   - src_unknown
   - src_unknown
   - src_unknown
4. **保持命名空间一致性**：卡片 id、文件名、source id、wikilink 目标使用同一套字符集和分隔规则。
5. **为人眼可读性使用元数据，而不是命名**：
   - src_unknown
   - src_unknown
6. **为旧数据设置兼容层**：如果历史命名不规范，集中一次迁移/重命名，而不是让解析器不断打补丁。

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 常见失败模式

| 失败模式 | 典型症状 | 根因 | 修复方法 |
|:
|:---|:---|:---|
| **ID 过长且含描述** | source_id_map 只能识别前半段 | 命名超出正则长度/字符预期 | id 与标题分离，id 简短规范 |
| **使用保留字符** | YAML 解析失败或正则匹配错误 | 命名中包含解析器保留字符 | 转义、加引号、或避免使用 |
| **人眼可读但机器读错** | 链接看起来对但 dangling | 别名、特殊符号、编码差异 | 用 gate 验证机器视角 |
| **新旧命名混用** | 批量脚本对部分数据失效 | 没有统一迁移，兼容补丁太多 | 集中迁移，统一命名空间 |
| **假设所有字段都是简单字符串** | 手写解析器在嵌套结构上失败 | 命名/结构假设过于简单 | 用成熟库，不要手写解析器 |

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
