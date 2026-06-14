---
id: "case-纪浩-skills-market"
title: "案例：一堂内部 Skills 分发平台——从微信传 zip 到 Agent 自助"
type: "case"
status: draft
domain:
  - "agent-infrastructure"
  - "yitang"
source_person: "纪浩"
source_context: "AI俱乐部-AI协作方法论 分享"
source_refs:
  - "00_inbox/AI俱乐部-AI协作方法论-纪浩-口述.txt"
tags:
  - "#boundary/requires-human-judgment"
  - "#confidence/draft"
  - "#confidence/source-cited"
  - "#confidence/verified-by-case"
  - "#domain/agent-infrastructure"
  - "#domain/yitang"
  - "#scene/agent-infrastructure/discovery-chain"
  - "#scene/agent-infrastructure/skill-registry"
  - "#scene/ai-collaboration/problem-validation"
  - "#scene/ai-collaboration/skill-market"
  - "#scene/learning-methodology/feedback-loop"
  - "#scene/note-taking"
  - "#scene/skill-engineering/manifest-design"
  - "#scene/skill-engineering/publish-deploy"
  - "#type/case"
created_at: 2026-06-07
updated_at: 2026-06-07
related:
  - "case-truman-ai-partner"
author: legacy
reviewed_by: pending
---

# 案例：一堂内部 Skills 分发平台

> 纪浩在 AI 俱乐部分享中描述的真实案例——一堂团队从"微信传 zip"到"Agent 自助下载安装"的 Skills 分发平台建设历程。

## 场景

一堂内部多个团队（前端、后端、运营）各自开发了 AI 协作的 skill。分享 skill 的方式是：找到 skill 文件夹 → 打包成 zip → 微信传给对方 → 对方手动解压安装。每次升级后要挨个微信推新版本，对方装没装也不知道。反馈靠口头描述（"你的 skill 不好使"），没有上下文无法定位问题。

## 四要素验证

### Before-After

| | Before | After |
|:---|:---|:---|
| 分发方式 | 微信传 zip，路径散落各台电脑 | 集中平台，一个入口 |
| 版本管理 | 文件名标记（"最终版""真的最终版"） | 平台版本号 + changelog |
| 反馈 | 口头描述，无上下文 | Agent 自动上报上下文 + 版本号 |
| 安装 | 人手下载解压配置 | Agent 自己下载安装 |

### 真实锚点

一堂内部真实使用。不是"如果有一个 skill 市场就好了"的想象需求——是张三每天都在微信里问李四"你的 skill 在哪、最新版是哪个"。

### 受益人

- **维护者**：反馈有上下文，可以复盘改进。版本管理不再靠文件名里的感叹号
- **用户**：有稳定入口找 skill，不用担心用的是旧版
- **Agent**：自行匹配+下载+安装，不依赖人操作

### 可解性

因果链清晰：
1. 存储分散 → 集中存储（数据库不是瓶颈）
2. 版本混乱 → 平台版本号
3. 反馈无上下文 → Agent 上报结构化数据
4. 安装靠人 → Agent 自操作

## 核心设计洞察：给 Agent 用的，不是给人用的

这个平台最关键的决策不是技术选型，是**用户定位**：

| | 传统平台（给人用） | 这个平台（给 Agent 用） |
|:---|:---|:---|
| 界面 | 网页、搜索框、下载按钮 | 分类枚举 + 结构化元数据 |
| 决策者 | 人看描述判断好不好用 | Agent 按分类 + capability 匹配 |
| 安装 | 人手动下载、配置 | Agent 自动下载、自动加载 |
| 反馈 | 人写评价 | Agent 自动上报上下文 + 版本号 |
| 写描述 | 人填表单 | 人跟 AI 说清楚 → AI 补全元数据 |

**"写描述不要让人去填，最好是让人跟 AI 说清楚之后，AI 去把信息补全，安装也是 AI 去安装。"**

## 可迁移场景

1. **KDO 的 Skill 分发**：`kdo encapsulate` 编译后的 skill 包，加一个 agent-facing 的分类层和 registry，Agent 按任务类型自动匹配和加载
2. **组织内部工具平台**：当一个团队内部有超过 5 个 AI tool/skill 时，天然需要这样的分发机制
3. **任何"把人的能力封装为可复用单元"的场景**：不只是 AI skill——SOP 文档、检查清单、最佳实践模板都可以走这个模式

## 反例

**什么时候不应该学这个案例**：
- 只有 1-2 个 skill，且只有一个人在用——微信传 file 就够了，平台是过度工程
- skill 的形态还不稳定，每周都在大改——先稳定 skill 定义，再做分发平台
- 没有真实的分发痛点（"我们设想未来可能需要"）——这是 Question（"想想很激动"），不是 Problem（"不解决现在难受"）。四要素验证不通过时不做

## 对 KDO 的启发

KDO 已经有了 `kdo encapsulate`（编译）和 `40_outputs/capabilities/skills/`（存储），缺的是中间的分类层和 Agent 发现链路：

```
现在：人手选skill → kdo encapsulate → 人手加载prompt
纪浩模式：Agent识别任务 → 查分类层 → 命中skill → 自动加载
```

中间缺的那一层就是一个 **task→skill 路由表**——不是给人看的，是给 Agent 的 function call 用的。

## Synthesis

- **纪浩体系**：[[concept-纪浩-ai-collaboration-methodology]] — 纪浩 AI 协作方法论总纲
