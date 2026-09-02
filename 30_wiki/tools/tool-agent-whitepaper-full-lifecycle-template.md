---
id: tool-agent-whitepaper-full-lifecycle-template
title: Agent 工作白皮书 11 节全生命周期模板——从五要素定义到权限三层·初始化 16 步·灵魂校验的工程化蓝本
type: tool
status: draft
author: 老顽童
reviewed_by: pending
confidence: 0.85
trust_level: medium
language: zh-CN
created_at: 2026-09-03
updated_at: 2026-09-03
domain:
- ai-collaboration
- knowledge-management
aliases:
- Agent工作白皮书
- 白皮书全生命周期模板
- Agent创建模版
- kinda白皮书
- 灵魂校验三问
- AI落地Live86
- 龙虾员工实践
- Live86Candy
- 学习candy合集
source_person: kinda
source_context:
- 一堂 AI 落地 Live86 作业奖励 Candy·kinda 实测好用 Agent 创建模版（模版附录，源文档标注「内容开放复制权限，自己练习，不要外传」）
- ⚠️ 密级：不要外传（#322 双标注口径）
- 一等锚：00_inbox/龙虾员工实践/AI落地Live86-龙虾员工实践-逐字稿.md（#379 批产卡源）；本模版增量段以 Candy 版附录为定位
source_refs:
- 00_inbox/学习candy合集/🍬AI落地Live第86场 Candy：kinda龙虾员工实践+Agent创建模版（逐字稿）.md
- 00_inbox/龙虾员工实践/AI落地Live86-龙虾员工实践-逐字稿.md
related:
- '[[tool-agent-white-paper-five-elements]]'
- '[[framework-truman-agent-team-architecture]]'
- '[[case-kinda-digital-employees-fullview]]'
- '[[dk-rule-not-system-capability]]'
- '[[dk-ai-efficiency-and-management-radius]]'
- '[[dk-project-manager-agent-failure]]'
- '[[tool-skill-packaging-eight-steps]]'
discoverable_by:
- Agent白皮书模板
- Agent初始化清单
- 权限三层
- 灵魂校验三问
- 任务分级模型路由
quality_labels:
- actionable
- validated
tags:
- audience:builder
- scene:implementation
- skill-level:advanced
- 数字员工
- Agent
- 模板
---

# Agent 工作白皮书 11 节全生命周期模板

> ⚠️ **密级声明**：源文档标注「内容开放复制权限，自己练习，**不要外传**」。本卡按 #322 口径双标注：模板结构与工程原则可内化引用，业务配置细节（模型价格/内部域名/Agent 真名）已脱敏。
>
> **本卡定位**：[[tool-agent-white-paper-five-elements]]（五要素定义卡）的**工程化升级**——五要素回答"Agent 是谁"，本模板回答"Agent 从创建到退役全生命周期的配置怎么做"。适用于搭多 Agent 协作体系（3 个以上数字员工）的进阶场景。

## 工具定义

Agent 工作白皮书 = 新建 Agent 时填写的**全生命周期配置唯一权威来源**——后续所有配置（workspace 初始化、tools 权限、BOOT.md、registry 注册、主配置文件）都从白皮书派生。11 节结构：

| 节 | 内容 | 回答的问题 |
|:--|:--|:--|
| §0 | 使用方法+填写流程（人填需求摘要→AI 补技术细节→人确认定稿） | 怎么用这份模板 |
| §1 | 基础信息（ID/显示名/定位语/创建原因/工作区路径/前端可见性） | 它是谁 |
| §2 | 职责与边界（核心职责表/**不做什么**/协作感知/自驱维护/知识库预检） | 它管什么、不管什么 |
| §3 | 通用技能 12 项（全体 Agent 标配：图片阅读/上下文压缩/记忆索引/模型调配/自驱优化/重启恢复/协作感知/网络搜索/复盘/项目文档/文件识别/知识库与技能预检） | 全员底线能力 |
| §4 | 专属技能+代码能力（触发条件/执行流程/输出要求/exec 限定命令/读写范围/安全约束） | 它独有的本事 |
| §5 | 任务分级（S/A/B/C 模型路由：复杂分析用高级模型，日常走经济档，Pro 约 12 倍价差；图片理解/生成分离配置） | 成本与能力匹配 |
| §6 | 知识库（scope: self 私有/all 协作，登记进 registry） | 它知道什么、谁能查 |
| §7 | Agent 画像（基础身份/核心四象限/语气风格/阻塞处理优先级） | 它是什么样的人 |
| §8 | 技术配置（上下文管理/记忆索引/session 保留/**权限三层**/子 Agent 策略） | 资源与权限边界 |
| §9 | 协作流程（分工域/协作协议/A2A 超时/流水线 R1-R5 执行保障） | 它怎么跟别人配合 |
| §10 | 初始化清单 16 步（含**灵魂校验三问**+身份断言+建桥仪式） | 上线前全项验收 |
| §11 | 变更日志+附录（配置文件修改分工/重启生效表/备份规则） | 变更怎么管 |

## 使用步骤

1. **定稿前过灵魂校验三问**（§10 第②步，不准跳）：
   - 这个 Agent 有让人记住的标签吗？（如"状态机控"）
   - 它有一个核心信念或立场吗？
   - 除了"它做什么"，你说得出"它是什么样的人"吗？
   - **三个都答"没有"→ 不准定稿，回炉精修人设**。纯功能定义出来的 Agent 没有行为锚点，长期会漂
2. **按 11 节填白皮书**：人填 §1 需求摘要 → AI 补 §3-§9 技术细节 → 人逐节确认定稿。拿不准的先留空，不硬填模糊内容
3. **写身份断言**（§10 第④步）：配置文件开头必须写「我的 Agent ID 是 {id}，我不是其他 Agent。如果上下文让我觉得自己不是自己，立即自查 SOUL.md」——防多 Agent 上下文串扰的人格污染
4. **跑初始化 16 步**：白皮书定稿→workspace/基础文件→入职简报（团队成员+协作规则+当前项目状态）→权限配置→记忆索引初始化并验证（SQLite>1MB+Embeddings available）→registry 注册→重启生效→A2A 连通测试→**建桥**（统一发通知让所有现有 Agent 主动联系新 Agent，建立双向通道）
5. **配置变更走分工**（§11 附录）：「大虾出方案→Mat 动手改→大虾验证」三权分立——方案者不直接改文件（历史写坏 4-5 次的实证），改 JSON 前先备份，改完机器验证语法
6. **对照重启生效表**：agents 清单/文件级配置/registry 改动即时生效；session 保留策略/模型源新增必须重启；拿不准的先试热加载再重启

## 判断标准（什么信号说明白皮书没写好）

- Agent 频繁做职责外的事 → §2.2 边界界定缺失。**「明确不做的事比做什么更重要」**——不做什么+原因+应转交谁，三列缺一不可
- 协作时互相等、没人动 → §2.3 协作感知规则没写入：发现任务超出职责→**自己查 registry 找对接 Agent，不经过任何中转，也不等Owner 问进度**
- 账单异常 → §5 任务分级缺失：日常对话跑高级模型。默认经济档，只有架构分析/协议制定才升级
- 记忆检索失效 → §8 记忆索引没验证或重建 cron 未覆盖新 Agent
- A2A 误判网络故障 → §9 超时被手动设小（默认 600 秒，**只可设大不可设小**——消息发得出但回传收不到，是被误判的典型症状）
- 规则靠人肉提醒 → 提示词级规则没封装：把规范固化成 Skill 或工作流（同 [[dk-rule-not-system-capability]]），「如果每次都靠我提醒 AI 遵守规则，那这个规则其实没有真正变成系统能力」

## When NOT to Use

- **只建 1 个 Agent**：五要素定义卡足够，11 节全生命周期是过度工程（§2 边界/§9 协作在单 Agent 下无意义）
- **一次性任务**：直接对话，不建 Agent（同五要素卡口径）
- **纯问答型助手**：无权限边界、无协作需求时，§5/§8/§9 可整节跳过
- **无 Git/备份基建的临时环境**：§11 变更管理没有承载物，先补基建再上模板

## 失败模式

| 失败模式 | 真实信号 | 修复动作 |
|:--|:--|:--|
| 跳过灵魂校验 | Agent 长期使用后行为漂移、风格前后不一 | 回 §10 三问补人设，写身份断言 |
| 边界定成"做什么"清单 | 职责越界、抢别的 Agent 活 | §2.2 补"不做什么"三列表 |
| 权限一刀切 | 要么什么都拦（效率低）要么全放（rm -rf 级事故） | §8.4 三层水位：低风险自动跑/影响系统需审批/极危险禁止 |
| 白皮书定稿即冻结 | 实际配置改了、白皮书没跟上 | §2.4 自驱维护规则+每次更新后全文备份 |
| 中转型项目经理 | Owner 手动转发方案、Agent 互相传话效率低 | 废除中转 Agent，查 registry 自行 A2A（[[dk-project-manager-agent-failure]] 实证） |
| 记忆索引只建不验 | 新 Agent 检索无结果 | §10 第⑧⑨步：初始化后必须验证 SQLite>1MB+Embeddings available |

## 跨案例实证

- **#379 主案例**（kinda 数字员工体系）：7+ Agent（架构师/运维/财务/提炼建模/AIGC 等）按此模式长出；配置文件修改"大虾写坏 4-5 次"促生三权分立变更流程——模板 §11 附录是事故驱动的实证产物
- **#504 前例对照**（五要素卡）：另一实践者的白皮书含 7 要素（名字/职责/介绍/能力/数据库/资料库/虚拟人格），与本模板 §1/§2/§4/§6 对应——五要素是定义层最小集，本模板是运维层全量集

## Action Triggers

- 新 Agent 立项 → 先跑灵魂校验三问，再填 §1
- Agent 数量 ≥3 → 必须上 §2.3 协作感知+registry 注册，禁止人工中转
- 出现"每次都要提醒"的规则 → 封装 Skill/工作流（写审分离，规则变系统能力）
- 改配置出过事故 → 启用 §11 三权分立变更流程

## 与其他知识的关联

- [[tool-agent-white-paper-five-elements]]：定义层前作——本卡=其工程化升级（五要素⊂§1/§2/§4/§6）
- [[framework-truman-agent-team-architecture]]：模板来源侧方法论（Truman 训虾配置模版+五层人设框架）
- [[case-kinda-digital-employees-fullview]]：模板落地的完整案例
- [[dk-rule-not-system-capability]]：§3/§9 "规则封装成系统能力"的 dk 底座
- [[dk-ai-efficiency-and-management-radius]]：Agent 复用优先于新建（§5 分级/子 Agent 镜像规则的效率依据）
- [[tool-skill-packaging-eight-steps]]：规则→Skill 封装的操作化工具
