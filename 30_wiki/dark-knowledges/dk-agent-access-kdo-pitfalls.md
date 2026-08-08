---
id: dk-agent-access-kdo-pitfalls
title: "外部Agent接入KDO：审批门禁/路径格式/检索规则三连坑"
type: dk
status: reviewed
domain:
  - kdo
  - ai-collaboration
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.9
trust_level: observed
aliases:
  - Agent接入KDO
  - 审批门禁坑
  - Hermes接入KDO
  - 外部Agent踩坑
  - smart审批
discoverable_by:
  - Agent接入KDO
  - 审批门禁
  - Hermes接入KDO
  - 外部Agent踩坑
  - smart审批
source_refs:
  - 30_wiki/agent-specs/agent-spec-basic-skills-coach.md
  - cap_hub/features.json
diagnostic_signals:
  - signal: "外部Agent(如Hermes教练)在网关里跑python3 -c / execute_code 被 BLOCKED：'timed out without user response'"
    severity: high
    implication: "approvals.mode=manual 时，代码执行类命令在无人工确认的网关环境必然超时被杀——不是命令坏了，是没人点'同意'"
  - signal: "terminal.cwd 写成 Windows 路径 C:\\Users\\... 在 WSL 里报 'No such file or directory'"
    severity: medium
    implication: "WSL 环境下 cwd 必须用 /mnt/c/... 格式，否则所有 cd 失败"
  - signal: "SOUL.md 检索规则写 'kdo feature 点菜'，但 kdo CLI 无 feature 子命令"
    severity: medium
    implication: "检索规则文档会过时——真实入口 kdo-tools/feature_menu.py 才是准的"
related:
  - '[[agent-spec-basic-skills-coach]]'
  - '[[tool-kdo-help]]'
  - '[[tool-mcp-reachability-check]]'
  - '[[dk-c8-format-complete-mind-empty]]'
created_at: 2026-08-09
updated_at: 2026-08-09
review_date: 2026-08-09
tags:
  - audience:builder
  - scene:reference
  - skill-level:advanced
  - agent:hermes
---

# 外部Agent接入KDO：审批门禁/路径格式/检索规则三连坑

> 一句话：外部 Agent（Hermes AI基本功教练）接入 KDO 时踩了三个配置层坑——审批模式挡住代码执行、cwd 用了 Windows 路径、检索规则文档过时。全修好后端到端检索链路跑通。

## 原始表述/核心洞察

2026-08-09，AI基本功教练（Hermes Agent，飞书网关）按 SOUL.md 的 KDO 知识库接入配置做实测，连续踩坑：

### 坑1：审批门禁挡住代码执行（最痛）

- 现象：`python3 -c "..."`、`iconv | python3`、`execute_code` 全部 BLOCKED
- 报错：`Command timed out without user response. The user has NOT consented to this action.`
- 根因：`config.yaml → approvals.mode: manual` + `timeout: 60`——代码执行类命令触发审批，但飞书网关端没有确认按钮/用户没看到，60 秒超时被杀
- 特征：只读命令（ls/grep/cat/kdo status）不触发审批，全放行——看起来像"命令坏了"，其实是"要人点头的命令点不了头"
- 修复：`hermes config set approvals.mode smart` → 低风险命令自动批准，高危命令仍标记

### 坑2：cwd 用了 Windows 路径格式

- 现象：`hermes config` 报 `cd: C:\Users\Administrator\Desktop\wiki: No such file or directory`
- 根因：`terminal.cwd: C:\Users\Administrator\Desktop\wiki`——WSL 里不认 Windows 反斜杠路径
- 修复：改为 `/mnt/c/Users/Administrator/Desktop/wiki`

### 坑3：检索规则文档过时

- 现象：SOUL.md 写"Feature 点菜用 `kdo feature`"，实际 `kdo feature` 报 `invalid choice`
- 根因：kdo CLI 无 feature 子命令，真实入口是 `kdo-tools/feature_menu.py`（features.json 的 FEATURE_MENU 指向它）
- 修复：更新 SOUL.md 检索规则第3条为 `python kdo-tools/feature_menu.py pick --n 5`，补第4条：kdo 命令必须在 workspace 内运行

### 核心洞察

1. **配置层问题伪装成"命令坏了"**——诊断时先查 approvals.mode / cwd / 文档规则，别急着怀疑命令本身
2. **smart 模式是网关场景的甜点位**——manual 在无人工确认场景必死，off 太危险，smart 是折中
3. **smart 模式仍放行 rm -rf**（标记"delete in root path"后自动批准）——系统层放行后，行为层必须自律：危险命令先问用户
4. **编码误判教训**：features.json 曾被误判为 GBK，实测是 UTF-8——遇到乱码先试多编码再下结论，别把"显示乱码"当"文件编码"

## 使用场景

- 任何外部 Agent（Claude Code/Codex/Kimi/CodeBuddy/Hermes）要接入 KDO 知识库时
- 任何 Agent 在网关/无人值守环境跑代码被 BLOCKED 时
- 排查"命令在终端能跑但 Agent 跑不了"类问题

## 操作方法

1. **诊断三步**：查 `config.yaml → approvals.mode` → 查 `terminal.cwd` 路径格式 → 查 SOUL.md 检索规则是否过时
2. **审批模式选择**：有确认界面选 manual；网关/无人值守选 smart；绝不选 off（除非完全隔离环境）
3. **路径格式**：WSL 一律 `/mnt/c/...`；Windows 原生才用 `C:\...`
4. **验证**：改完跑一遍 `python3 -c "print('ok')"` + `kdo status` + `feature_menu.py pick --n 3`，看 approval 字段是否 auto-approved
5. **行为自律**：即使 smart 放行，rm -rf / git push --force / DROP TABLE 类命令默认先问用户

## 适用边界

- 适用：Hermes Agent 接入 KDO、飞书网关场景、审批配置诊断
- 不适用：纯本地交互式终端（manual 模式反而合适）；纯只读检索场景（无需改审批）
