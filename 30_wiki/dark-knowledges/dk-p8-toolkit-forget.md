---
id: dk-p8-toolkit-forget
title: P-8：欧阳锋忘记本地已有武器——重新调研已部署工具
type: dark-knowledge
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: system
source_context: pitfalls.md P-8
source_refs:
- 10_raw/sources/src_20260619_1545a6ee_.agent_pitfalls.md#P-8
created_at: 2026-06-03
updated_at: '2026-06-19'
related:
- '[[master-knowledge-compound]]'
- '[[kdo-flywheel]]'
- '[[master-first-principles]]'
pipeline:
- confidence-draft
- confidence-source-cited
- confidence-reviewed
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- 新 session 启动后 10 分钟内就开始调研或部署一个已存在的本地工具
- 工具信息分散在 CLAUDE.md 或长文档中，没有独立的 toolkit.md
- 同一工具在仓库不同位置出现多个副本或安装记录
- toolkit.md 最后更新时间早于最近一次工具部署时间
---# P-8：欧阳锋忘记本地已有武器——重新调研已部署工具

## 原始表述/核心洞察

> **症状**：新欧阳锋 session 启动后，遇到 OCR/图片处理需求，花大量时间调研方案、测试依赖、试图部署新工具。最后才想起来 vault 旁边 `C:\Users\Administrator\ocr-pipeline\` 已经部署了 PaddleOCR v5，且有 PowerShell 封装脚本。
>
> **根因**：
> 1. 启动时只读了 `context.md` + `pitfalls.md`，本地工具清单藏在 277 行的 CLAUDE.md 里，读完前两个文件根本看不到
> 2. `.agent/` 记忆系统缺少"武器库"文件——记录"我们有什么、在哪、怎么用"
> 3. 工具部署完成后没有在 startup checklist 中加入验证步骤
>
> **对策**：
> - 新建 `.agent/toolkit.md`（OCR/KDO CLI/Git/WSL 桥接/内置 Skills/常见操作模式）
> - CLAUDE.md 启动指令已改：`Read .agent/context.md → .agent/pitfalls.md → .agent/toolkit.md`
> - context.md "下次启动"第 1 条加了 `toolkit.md` 提醒
> - 新增工具/能力时必须同步更新 `toolkit.md`
> - 原则：**先查武器库再行动——不要重复造轮子**

核心洞察：**在多角色、多 session 的协作环境中，"本地已有什么能力"必须是一份独立、最新、且被强制读取的武器库；否则每个新 session 都会重复支付调研与部署的启动税。** 工具信息不能藏在巨型启动文档里，也不能只依赖人的记忆。

## 使用场景

- 你面对一个新问题，想要寻找解决方案或部署新工具
- 你是新 session 或新角色启动，不确定本地已有什么能力
- 你花了大量时间调研某个问题，发现解决方案已经存在
- 你设计 Agent 启动流程，需要确保武器库文件被读取

## 操作方法

1. **启动时先查武器库**：
   - 启动第一步：读 `.agent/toolkit.md`
   - 看看是否有现成工具能解决当前问题
   - 如果没有，再开始调研/部署

2. **维护 toolkit.md**：
   - 每次部署新工具后，立即记录：工具名、版本、位置、使用场景、封装脚本路径
   - 定期检查 toolkit.md 是否过期（工具是否仍在、版本是否更新）
   - 将已弃用的工具标记为"已退役"，而不是直接删除

3. **启动 checklist 更新**：
   - 在 context.md 的"下次启动"提醒中加入 toolkit.md
   - 确保每个新 session 都先看武器库再开工

4. **团队共享**：
   - toolkit.md 是团队级的，不是个人的
   - 其他角色启动时也应该读取同一个武器库
   - 避免不同角色重复部署同一个工具

5. **不要做的事**：
   - 不要遇到问题就直接开始调研——先问"我们是否已经有现成工具"
   - 不要把工具信息藏在一个巨大的文件里（如 CLAUDE.md）——放不进启动 checklist
   - 不要部署完工具后不记录——下次还会重复造轮子

## 适用边界

- 适用于所有多角色、多 session 协作的环境
- 不适用于单人单机的短期项目（那些场景下大脑就是武器库）
- **与 P-7 的区别**：P-7 是"执行者跳过了图片"，P-8 是"架构者忘了有 OCR 工具可以处理图片"。两者是同一事件的两个维度
- 如果武器库文件存在但过期了（工具已被卸载），P-8 仍然会触发——需要定期验证
- 如果工具是云端服务（如 SaaS API），武器库需要记录 API 文档链接和账户信息

## 常见失败模式

| 失败模式 | 典型信号 | 根因 | 修复动作 |
|---|---|---|---|
| 启动时不查武器库直接调研 | 新 session 启动后 10 分钟内开始调研已部署工具 | 启动 checklist 缺少 `.agent/toolkit.md` | 启动流程第一步：先读 `toolkit.md` 再决定是否需要新工具 |
| 工具信息藏在巨型文档里 | 工具清单混在 CLAUDE.md 第 200+ 行，启动时不会被读到 | 未抽出独立的武器库文件 | 新建 `.agent/toolkit.md`，并从启动文档中移除冗余工具信息 |
| 部署后不更新武器库 | toolkit.md 中没有最新部署工具的条目 | 缺少"部署即记录"的纪律 | 把"更新 toolkit.md"写进每次部署的完成定义（DoD） |
| 武器库过期未验证 | toolkit.md 记录的工具路径已失效或工具已被卸载 | 缺少定期审计与验证机制 | 每月/每季度 audit 一次 toolkit.md，对失效条目标记"已退役" |
| 多角色重复部署同一工具 | 不同角色目录下出现同一工具的多个副本 | 武器库未作为团队共享契约 | 所有角色启动时读取同一个 toolkit.md，统一工具位置 |

## 为什么值钱

- 这是**组织知识**的实战教训：单人可以靠记忆，但团队必须靠文档。每次新 session 重建记忆 = 重复造轮子
- 极具时间浪费：花 30 分钟调研 PaddleOCR 部署，最后发现本地已经有 v5 带封装脚本
- 揭示了"启动成本"问题：Agent 启动时的信息缺口会导致每个新 session 都重复做同样的无效工作
- **AI 训练语料中不会有这条**：没有任何文档会写"在多角色协作环境中，新 session 启动时先查武器库再行动"

## 与其他知识的关联

- [[dk-p7-ocr-skip]] — P-7 和 P-8 是同一事件的两个维度。如果当时查了 toolkit.md 发现 OCR 工具已部署，P-7 可能不会发生
- [[dk-p1-model-switch-env]] — 同样是"启动时信息缺口"导致的问题：不知道配置层级优先级 → 改了配置不生效
- [[master-first-principles]] — 先查武器库再行动，本质上是在执行前先做"事实核查"，避免默认从零开始
- `.agent/toolkit.md` — 武器库文件（如果存在）
- `.agent/pitfalls.md` → P-8（原始记录）
