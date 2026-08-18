---
id: 370
assignee: wangyuyan
status: queued
updated_at: '2026-08-19T02:30:00+00:00'
title: 治理收敛（P1，小昭体检采纳）——PROTOCOL 写入队列真相源 + 双队列合并 + agent-spec 补齐（含欧阳锋）
priority: P1
dependency:
- 365
reviewed_by: 欧阳锋
---

# #370 治理收敛（P1）

## 任务目标

治"文档信任危机"（小昭体检洞察 3，王语嫣完全采纳）：任何一个新 agent/新会话按文档入职不能学错。

## 素材/证据（小昭体检 §三，王语嫣抽核实锤）

- `90_control/PROTOCOL.md` 目录拓扑未写 production-queue.md 真实位置；头部 v0.3 vs changelog v0.4 矛盾；"5 角色体系"（无王语嫣）与 AGENTS.md 6 角色矛盾
- 洪七公/段王爷被规定从 dashboard.md 领任务——与 production-queue.md 双队列并行派单
- agent-spec 仅 3 份（duanwangye/hongqigong/zhu-ai-coach），欧阳锋/王语嫣/老顽童/黄药师缺——终审官自己没有 spec
- 角色定义三处并存：agent-specs/、.agent/*-context.md、role-profiles/

## 修改范围

1. **PROTOCOL.md 修正**：队列唯一真相源位置写入；版本号对齐；6 角色体系更新（含王语嫣）
2. **双队列合并**：dashboard 领任务规定废止，全部归 production-queue.md（dashboard 只读展示——与 #365 注册表派生物表一致）
3. **agent-spec 补齐 4 份**：欧阳锋（优先——终审官无 spec 是最大讽刺）/王语嫣/老顽童/黄药师；draft 规格起步，走正常终审
4. **角色定义归一**：agent-specs/ 为 spec 真相源，.agent/*-context.md 为运行时指令——注册表写清分工，不重复内容

## 边界

- 依赖 #365（注册表先定真相源分工）
- 文档治理不动运行时行为
- 老顽童/黄药师的 spec 起草可走"本人初稿+王语嫣收束"（写审分离）

## 验收标准

1. PROTOCOL.md 与 AGENTS.md 零矛盾（grep 核对角色数/队列位置/版本号）
2. 双队列合并落盘，洪七公/段王爷 context 领任务指向更新
3. agent-spec 6/6 齐备，欧阳锋 spec 终审通过

## 交付

1. 修正 + 4 份 spec
2. 送欧阳锋终审
