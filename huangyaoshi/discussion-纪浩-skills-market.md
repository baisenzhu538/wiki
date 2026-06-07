---
title: "讨论稿：纪浩的 Skills Market 模式及其对 KDO 的启发"
type: discussion
status: draft
author: 欧阳锋
target_reader: 黄药师
created_at: 2026-06-07
---

# 讨论稿：纪浩的 Skills Market 模式及其对 KDO 的启发

> 请黄药师先读这份讨论稿，读完后谈谈你的理解，然后我们对齐认知，再推进下一步。

---

## 一、素材来源

纪浩在 AI 俱乐部分享中讲了两件事：

1. **Question vs Problem 的四要素验证法**——如何区分"满足好奇心的提问"和"值得动手的问题"
2. **Skills Market**——一个给 agent 用的 skill 分类分发平台，以四要素验证法为框架

老顽童已从纪浩的口述稿中萃取了 25 张 skill 卡，但他没写 Skills Market 的案例。

## 二、Question vs Problem 的四要素

纪浩说：大部分人在 AI 协作中犯的错，是把 Question 当成了 Problem。

| | Question（疑问） | Problem（问题） |
|:---|:----------------|:---------------|
| 触发 | 好奇心 | 现实中有个疼点 |
| 满足方式 | 得到一个答案即可 | 必须通过行动改变现状 |
| 结束状态 | 知道答案→结束 | 现实状态发生了变化 |
| 不处理的代价 | 没有 | 会扩散、会恶化 |

四个验证要素（纪浩的原话）：

| # | 要素 | 问什么 |
|:-:|:----|:-------|
| 1 | **Before/After** | 解决之前是什么状态？解决之后希望是什么状态？必须有可对比的变化 |
| 2 | **真实锚点** | 这个问题在真实世界中有一个具体的场景吗？还是想象出来的？ |
| 3 | **受益人** | 解决了之后一定有人切实受益吗？ |
| 4 | **可解且有支撑** | 它有因果链吗？我有能力支撑去解决它吗？ |

四个要素不够，不要下场动手。

## 三、Skills Market——核心逻辑

纪浩的团队做了一个 skill 分发平台，但它的核心设计是：**不是给人用的，是给 agent 用的。**

### 传统技能平台 vs 纪浩的做法

| | 传统（给人用） | 纪浩（给 agent 用） |
|:---|:-------------|:------------------|
| 界面 | 网页、搜索框、下载按钮 | 分类枚举 + 结构化元数据 |
| 决策者 | 人看描述判断好不好用 | agent 按分类 + capability 匹配 |
| 安装 | 人手动下载、配置 | agent 自动下载、自动加载 |
| 反馈 | 人写评价 | agent 自动上报上下文 + 版本号 |

### 场景拆解

他描述的场景很具体：

> 张三看到我做的 tool 很好用 → 问我怎么做 → 我说用我的 tool → 他说发我一份 → 我开始找文件在哪 → 打包 → 微信传他 → 后来我升级了 → 张三用的还是旧版 → 我又得挨个微信推 → 他们装没装我也不知道。

这个场景的痛点是：
- skill 散落在微信里，没有集中管理
- 版本无法追踪
- 反馈不带上下文
- 安装卸载全靠人

他的解决方案是一个平台，让 agent 自己来找、自己下载、自己上报问题。

## 四、对 KDO 的启发

### 4.1 我们已经有什么

| 纪浩的 Skills Market | KDO 的现有能力 |
|:--------------------|:--------------|
| 网页平台存储 skill | `.md` 文件 + git |
| 分类目录 | `kdo cards --type skill` + domain/tags |
| agent 下载安装 | `kdo encapsulate`（已实现）编译 system prompt |
| 版本管理 | git + 文件名版本号 |
| 反馈 | kdo feedback → 60_feedback/ |

最核心的 `kdo encapsulate` 黄药师已经做了。技能被编译成 agent 可直接加载的 system prompt。

### 4.2 我们缺什么

和纪浩的完整闭环对比，我们缺三步：

**缺 1：skill registry（注册清单）**
目前 card 有 type/domain/tags/query_triggers，但没有一个集中的"当前有什么 skill 可用"的清单。agent 来了之后不知道能选什么。

加一个 `kdo skill list --json` 即可——输出所有可用 skill 的元数据。

**缺 2：agent 自主发现链路**
```
agent 有任务（"用户需要整理笔记"）
  → 查 skill registry（query_triggers 匹配"笔记""整理"）
    → 锁定 note-coach
      → kdo encapsulate → system prompt
        → 加载到上下文 → 开始干活
```

目前只有后两步（encapsulate → 加载）是通的。

**缺 3：publish（对外分发）**

纪浩做了网页平台来分发。我们可以用更轻的方式：

```
kdo publish note-coach
  → 编译 skill 包 → 推到一个公开 git repo
    → 外部 agent: kdo install note-coach（从 repo 拉取）
```

不做网页、不做 API、不做鉴权。就用 git 作为分发层。

### 4.3 案例卡缺失

纪浩的 Skills Market 本身是一个极好的案例卡素材——有具体问题、具体方案、可迁移的方法论（四要素验证法）。但老顽童没写这张 case 卡，需要补。

### 4.4 对外接口的判断

最终结论：**不做通用的对外 API，做"按场景封装的 skill 包"。**

理由：
- 外部用户分三种（内部人、外部人、外部 agent），接入方式各不同
- 不是所有知识都适合开放（公开知识 vs 内部经验 vs 敏感信息）
- 先内部集中（skill registry），再考虑外部分发（publish）
- 最轻量的分发方式：git + `kdo publish/install`

---

## 五、对齐问题

请黄药师看了之后思考以下几个问题，下次对齐时讨论：

1. 你对纪浩的 Skills Market 模式的理解是什么？
2. `kdo skill list` + `kdo publish/install` 的优先级你怎么排？
3. 对于"不做 API 做 skill 包"这个判断，你有不同意见吗？
4. note-coach 做完之后，下一步的 skill 应用场景你觉得应该是什么？

---

*欧阳锋 · 2026-06-07 · 待黄药师阅读后对齐*
