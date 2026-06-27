---
id: dk-p8-toolkit-forget
title: P-8：欧阳锋忘记本地已有武器——重新调研已部署工具
type: dk
dark_knowledge_type: failure
status: enriched
domain:
- src_unknown
source_person: system
source_context: pitfalls.md P-8
source_refs:
- src_unknown
created_at: 2026-06-03
updated_at: '2026-06-19'
related:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
pipeline:
- src_unknown
- src_unknown
- src_unknown
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
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

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **启动时先查武器库**：
   - src_unknown
   - src_unknown
   - src_unknown

2. **维护 toolkit.md**：
   - src_unknown
   - src_unknown
   - src_unknown

3. **启动 checklist 更新**：
   - src_unknown
   - src_unknown

4. **团队共享**：
   - src_unknown
   - src_unknown
   - src_unknown

5. **不要做的事**：
   - src_unknown
   - src_unknown
   - src_unknown

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 常见失败模式

| 失败模式 | 典型信号 | 根因 | 修复动作 |
|---|---|---|---|
| 启动时不查武器库直接调研 | 新 session 启动后 10 分钟内开始调研已部署工具 | 启动 checklist 缺少 `.agent/toolkit.md` | 启动流程第一步：先读 `toolkit.md` 再决定是否需要新工具 |
| 工具信息藏在巨型文档里 | 工具清单混在 CLAUDE.md 第 200+ 行，启动时不会被读到 | 未抽出独立的武器库文件 | 新建 `.agent/toolkit.md`，并从启动文档中移除冗余工具信息 |
| 部署后不更新武器库 | toolkit.md 中没有最新部署工具的条目 | 缺少"部署即记录"的纪律 | 把"更新 toolkit.md"写进每次部署的完成定义（DoD） |
| 武器库过期未验证 | toolkit.md 记录的工具路径已失效或工具已被卸载 | 缺少定期审计与验证机制 | 每月/每季度 audit 一次 toolkit.md，对失效条目标记"已退役" |
| 多角色重复部署同一工具 | 不同角色目录下出现同一工具的多个副本 | 武器库未作为团队共享契约 | 所有角色启动时读取同一个 toolkit.md，统一工具位置 |

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
