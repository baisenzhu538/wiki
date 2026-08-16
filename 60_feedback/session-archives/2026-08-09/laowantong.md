---
session_id: laowantong-2026-08-09
agent_id: laowantong
date: 2026-08-09
created_at: 2026-08-09T09:20:41.714172+00:00
updated_at: 2026-08-09T09:20:41.714172+00:00
---

# laowantong · 2026-08-09

# 老顽童复盘 2026-08-09（kimi 实例 · 科学开会 #285/#286）

## 概要（一句话：今天做了什么）

领取并完成科学开会 #285（9 卡）+#286（7 卡+补链 25 条）：三篇口述稿 6990 行证据库提取 → 16 卡生产 → pre-submit 全 PASS → 四路自攻击修 🔴×1🟡×13 → 双任务 pending_review 双验证流转，为 #287 会议助理 agent 备好完整数据源。

## 差异栏（本次 vs 上次复盘哪里不同）

- **新视角：主代理不逐字读全文也能满足"口述稿第一"铁律**——3 个子代理分篇逐字通读+结构化证据库（含行号/ASR 还原表/噪声段标注），主代理 sed 抽查 6 处全命中后才采信。上次（教练域 hermes 实例同日）是单实例硬读 7267 行。对比结论：证据库模式把"逐字读"从内存约束变成可验证工件，且自攻击代理可复用同一证据库做数据攻击。
- **被打破的假设**：以为队列铁律"前方 pending_review 不可领"会堵死 #285——实际脚本的 `--force` 就是为多实例并行设计的合法通道，不是绕过。 blocked 感来自没读脚本 docstring。
- **复发的模式**：队列文件注释行夹进表格导致 parse 提前 break（E021 家族"状态不一致"的解析层同构）——王语嫣修过一次没修干净（注释仍夹在 #284/#285 之间），我二次修复并把它移出表格。教训：修复后要跑解析验证，不是看 diff 觉得对。

## 关键决策

| 决策 | 理由 | 结果 |
|:--|:--|:--|
| 修 production-queue.md 注释位置而非改脚本 | 最小侵入，不动状态字段不违规 | parse 267 行全通，#285 可领 |
| claim --force 跨 pending_review | 不同 assignee 并行（脚本设计用途）+ 用户直接派单 | 合规领取 |
| 证据库子代理×3 + 写卡 swarm×8+7 | 6990 行超单上下文；证据落盘可抽查可复用 | 数据攻击 105+ 处引用零编造 |
| 卡 1 升级保留旧版无源内容但加批注隔离 | 任务单"不重写不降级"vs 铁律"不许无源数字"的折中 | 🔴 消解，结构保留 |
| dk 6 张全产不启用 6→4 裁剪 | 用户强调暗知识重要 | #287 数据源完整 |

## 思维盲点

1. **差点把"待补充链接"当旧版装饰留着**：自攻击才发现概念卡旧版有编造数字（承诺级 L1/L2/L3、30→8 人案例）——为什么漏掉：升级任务时注意力全在"补新内容"，默认旧版 reviewed 内容可信。教训：升级卡 = 对旧内容重新承担溯源责任，"已 reviewed"不等于"已溯源"。
2. **跨域链接的判定口径**：补链时以为复盘域算跨域，实际 pre-submit 按 frontmatter domain 差集判定，复盘域卡 domain 也是 [yitang, management] 不算——为什么漏掉：凭"域"的语义直觉没看检查器实现。教训：门禁口径先读代码再设计。

## 顿悟

**"脚本说它流转了 ≠ 队列真流转了"的逆命题也成立：脚本报错 ≠ 真的被堵。** 今天两个"阻塞"（parse break、pending_review 前置）都在读脚本源码后 10 分钟解决。E019 教我们验证流转，今天的补充是：验证失败时先怀疑解析层，再怀疑流程层。

## 过程资产

- 新卡 15 张：30_wiki/frameworks/framework-meeting-{iceberg-canvas,ten-principles}.md；30_wiki/tools/tool-meeting-{basic,execution,result}-principles.md；30_wiki/cases/case-meeting-{roi-awakening,scene-mastery}.md、case-truman-meeting-leadership.md；30_wiki/bridges/bridge-meeting-leadership-coaching.md；30_wiki/dk/dk-meeting-{roi-first,principle-over-process,rederive,borrow-false-repair-true,asset-harvest,pressure-ignition}.md
- 升级卡 1 张：30_wiki/concepts/yt-management-scientific-meetings.md（source_refs 补齐+新四节+无源批注）
- 补链 10 张已有卡 related +25 条
- 证据库+规格+自攻击报告：`_tmp/scientific-meeting-evidence/`（evidence-×3/CARD-WRITING-SPEC/self-attack-285/self-attack-286）——#287 王语嫣可直接复用
- 任务单执行报告×2；production-queue.md 注释区修复

## 元反思（下次怎么做才能不一样）

下次接到多文件大体量口述稿任务：第一步直接立"证据库+抽查"管线（不再犹豫单读还是委派）；升级卡任务先 grep 旧版"待补充/无源数字"再动笔；队列报错先读脚本源码/docstring 再上报阻塞。

## Truman复盘

### 逐轮映射

| 轮次 | 人做什么 | 双三角要素 | AI做什么 | 双三角要素 |
|:--|:--|:--|:--|:--|
| 1 | 用户一句口令派单（角色+记忆位置+任务号） | 目标 | 找记忆→读 AGENTS/context/队列→定位任务单 | 对齐 |
| 2 | — | — | 修队列解析断点、claim #285 | 执行 |
| 3 | — | 素材 | 子代理×3 逐字读 6990 行→证据库 | 萃取 |
| 4 | — | 框架 | 出牌建模方案→swarm 产 15 卡+升级 1 卡 | 建模 |
| 5 | — | 验证 | pre-submit×16 + 四路自攻击×2 + 修复 | 质疑 |
| 6 | — | 闭环 | 执行报告→complete×2→双验证 | 交付 |

### 飞轮效应

证据库模式加速了"使用→反思"回路：证据库不仅服务写卡，还服务自攻击（数据攻击直接对照证据库+原稿），下一轮（#287）还能直接当 spec 数据源复用——一次提取，三次消费。

### 对照实验

- 无人（纯 AI）：无用户口令定位任务，agent 不知道 #285→#287 的链路意图
- 无 AI（纯人）：6990 行逐字读+16 卡+门禁，人需要数天；且行号级溯源人难以稳定执行
- 合在一起：人给方向和验收标准，AI 给产能和机械纪律，自攻击兜底诚实性

### 下次改进

- Agent 自身：证据库提取 prompt 沉淀为可复用模板（含 ASR 还原表/噪声段标注要求），入 skills 候选
- 方法论卡更新：`framework-kdo-modeling-methodology` 的 Step2 可补"子代理证据库+主代理抽查"作为大体量素材的标准消化姿势
