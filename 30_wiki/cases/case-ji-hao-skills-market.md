---

id: case-ji-hao-skills-market
title: 案例：一堂内部 Skills 分发平台——从微信传 zip 到 Agent 自助
type: case
status: reviewed
domain:
- src_unknown
- src_unknown
source_person: 纪浩
source_context: AI俱乐部-AI协作方法论 分享
source_refs:
- 10_raw/sources/src_20260606_0ecc1afc-AI俱乐部-AI协作方法论-纪浩-口述.md
tags:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
created_at: 2026-06-07
updated_at: '2026-06-28'
related:
  - "[[yt-tool-peas-agent-analysis]]"
  - "[[tool-agent-research-pipeline]]"
  - "[[case-ai-agent-milestone-design]]"
  - "[[tool-agent-crawl4ai]]"
  - "[[agent-external-brain-design]]"
  - "[[dk-demand-pitfall-travel-agent]]"
  - "[[tool-从案例中学习]]"
  - "[[tool-纪浩-Agent开工检查单制作法]]"
  - "[[tool-纪浩-案例池构建法]]"
  - "[[case-科学决策-ROI案例03]]"
  - "[[tool-马易-业务问题AI化拆解-餐饮设计案例法]]"
  - "[[case-科学决策-深度案例06]]"
  - "[[case-纪浩-from-zip-to-five-layers]]"
  - "[[tool-demand-agent-signal-substitute]]"
author: 纪浩
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- framework_lens: 伪需求 vs 真实问题：没有真实锚点的需求会无限放大
  follow_up_question: 能否列出最近一周 3 个因 zip 分发而产生实际损失的现场？如果列不出，先用四问法验证再动手。
- framework_lens: Agent-facing 设计：元数据应让人"说清楚"后由 AI 补全，安装由 Agent 自动完成
  follow_up_question: 哪些字段可以让维护者口述/截图后由 AI 自动转成结构化元数据？安装步骤能否由 Agent 自己完成？

---

# 案例：一堂内部 Skills 分发平台

## 一句话摘要

一堂内部因长期靠"微信传 zip"分发 Skill，导致版本混乱、反馈无上下文、安装依赖人工；纪浩团队通过建设**面向 Agent 的集中式 Skills 分发平台**，实现了版本管理、结构化反馈与 Agent 自动安装更新。

## 背景

一堂内部多个团队（前端、后端、运营）各自开发了 AI 协作的 skill。分享 skill 的方式是：找到 skill 文件夹 → 打包成 zip → 微信传给对方 → 对方手动解压安装。每次升级后要挨个微信推新版本，对方装没装也不知道。反馈靠口头描述（"你的 skill 不好使"），没有上下文无法定位问题。

这一场景不是"如果有一个 skill 市场就好了"的想象需求，而是真实锚点：张三每天都在微信里问李四"你的 skill 在哪、最新版是哪个"。

## 关键事件/决策点

### 1. 四要素验证：确认这是真实问题再做平台

| 维度 | Before | After |
|:---|:---|:---|
| 分发方式 | 微信传 zip，路径散落各台电脑 | 集中平台，一个入口 |
| 版本管理 | 文件名标记（"最终版""真的最终版"） | 平台版本号 + changelog |
| 反馈 | 口头描述，无上下文 | Agent 自动上报上下文 + 版本号 |
| 安装 | 人手下载解压配置 | Agent 自己下载安装 |

- src_unknown
- src_unknown
- src_unknown

### 2. 核心设计决策：给 Agent 用的，不是给人用的

这个平台最关键的决策不是技术选型，而是**用户定位**：

| | 传统平台（给人用） | 这个平台（给 Agent 用） |
|:---|:---|:---|
| 界面 | 网页、搜索框、下载按钮 | 分类枚举 + 结构化元数据 |
| 决策者 | 人看描述判断好不好用 | Agent 按分类 + capability 匹配 |
| 安装 | 人手动下载、配置 | Agent 自动下载、自动加载 |
| 反馈 | 人写评价 | Agent 自动上报上下文 + 版本号 |
| 写描述 | 人填表单 | 人跟 AI 说清楚 → AI 补全元数据 |

> **"写描述不要让人去填，最好是让人跟 AI 说清楚之后，AI 去把信息补全，安装也是 AI 去安装。"**

## 结果

| 维度 | Before | After |
|:---|:---|:---|
| 分发方式 | 微信传 zip，路径散落 | 集中平台，统一入口 |
| 版本管理 | 文件名标记，版本混乱 | 平台版本号 + changelog |
| 反馈 | 口头描述，无上下文 | Agent 自动上报上下文 + 版本号 |
| 安装 | 人手下载解压 | Agent 自动下载安装 |

- src_unknown
- src_unknown
- src_unknown

## 复盘与洞察

1. **平台的核心价值是"减少人的重复劳动"，而不是"做个更漂亮的界面"**。如果界面只服务于人，Agent 仍然无法自助使用，平台就只是换了个下载站。
2. **元数据和安装流程必须 Agent-facing**。描述由 AI 补全、安装由 Agent 完成，才能把维护者从"填写表单 + 客服式答疑"中解放出来。
3. **真实锚点是第一约束**。没有"每周多次 zip 混乱"的真实场景，平台需求会无限放大成"应用商店 + 广告 + 生态"。
4. **对 KDO 的启发**：KDO 已有 `kdo encapsulate`（编译）和 `40_outputs/capabilities/skills/`（存储），缺的是中间的**task→skill 路由表**——不是给人看的，是给 Agent 的 function call 用的。

   ```
   现在：人手选 skill → kdo encapsulate → 人手加载 prompt
   纪浩模式：Agent 识别任务 → 查分类层 → 命中 skill → 自动加载
   ```

## 可迁移场景

1. **KDO 的 Skill 分发**：`kdo encapsulate` 编译后的 skill 包，加一个 agent-facing 的分类层和 registry，Agent 按任务类型自动匹配和加载。
2. **组织内部工具平台**：当一个团队内部有超过 5 个 AI tool/skill 时，天然需要这样的分发机制。
3. **任何"把人的能力封装为可复用单元"的场景**：不只是 AI skill——SOP 文档、检查清单、最佳实践模板都可以走这个模式。

## 教训

- src_unknown（待补充：从本案例学到的核心教训）

## 失败模式

**什么时候不应该学这个案例**（或会导致失败）：

- src_unknown
- src_unknown
- src_unknown

**具体失败模式**：

| 模式 | 症状 | 修复 |
|:---|:---|:---|
| **给人做的平台** | 界面精美、搜索方便，但 Agent 无法解析元数据和自动安装 | 把元数据设计成结构化 manifest，安装接口暴露给 Agent |
| **需求无限放大** | 从"解决 zip 混乱"滑向"做应用商店、加广告、做生态" | 用真实锚点清单锁住最近一周的 3 个混乱现场，无关功能砍掉 |
| **元数据靠人填** | 维护者嫌麻烦，更新一次要填一堆表单，最终放弃维护 | 让人口述/截图，AI 自动补全元数据 |

## 相关卡/互链

- src_unknown
- src_unknown
- src_unknown

## 关键证据

| 证据点 | 来源 | 可检验性 |
|:---|:---|:---|
| src_unknown | src_unknown | src_unknown |
| src_unknown | src_unknown | src_unknown |
