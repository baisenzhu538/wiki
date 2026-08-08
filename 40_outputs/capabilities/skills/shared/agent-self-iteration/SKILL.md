---
name: agent-self-iteration
description: 工具卡顿/超时/规则失效时走五步闭环——发现问题→诊断配置层→修复→沉淀→注册，不绕过。
version: 1.0.0
author: 王语嫣（教练Agent案例启发，2026-08-09）
metadata:
  hermes:
    tags: [自我迭代, 自我进化, 配置诊断, 工具故障, 沉淀, 闭环]
    related_skills: [entry-quality-gate, six-layer-cross-validation, self-evolution, kdo-self-attack]
---

# Agent 自我迭代闭环

> 教练Agent（AI基本功教练，Hermes飞书网关）在#252试点中的意外收获证明：**Agent + KDO知识库 + 终端权限 = Agent能自己修自己**。它不是"被调用"，它在自我迭代——发现权限问题→切smart模式→发现路径问题→改WSL路径→发现检索规则过时→建dk卡沉淀→注册进MOC。

## 触发词

工具卡顿、超时、BLOCKED、报错、命令坏了、搜不到、规则过时、配置问题、"又踩坑了"、"忍一忍绕过"

## 核心洞察

### 配置层问题伪装成"命令坏了"

诊断工具故障时，**先查配置层，再怀疑命令本身**：

| 配置层 | 检查项 | 典型症状 |
|:---|:---|:---|
| 审批模式 | `config.yaml → approvals.mode` | manual在网关无确认界面→代码命令60s超时被杀；只读命令不触发审批全放行 |
| 工作目录 | `terminal.cwd` | cwd在/home下→search_files递归跨/mnt/c全树→超时；WSL路径必须是/mnt/c/格式 |
| 命令白名单 | `command_allowlist` | kdo等命令未列入→manual拦截无豁免路径 |
| 文档规则 | SOUL.md/检索规则 | 文档写的命令已过时（如"kdo feature"实际不存在） |

### 三个真实坑（2026-08-09 教练Agent）

1. **审批门禁**：`python3 -c`/`execute_code` BLOCKED——"timed out without user response"。根因：approvals.mode=manual + 网关无确认按钮。修复：`hermes config set approvals.mode smart`（低风险自动批准，高危仍标记）
2. **路径格式**：cwd写成Windows路径`C:\Users\...`在WSL报"No such file"。修复：`/mnt/c/Users/...`
3. **检索规则过时**：SOUL.md写"kdo feature"实际`invalid choice`。修复：查真实入口（kdo-tools/feature_menu.py）更新文档

> 沉淀卡：`dk-agent-access-kdo-pitfalls`（30_wiki/dark-knowledges/）——含三坑诊断+操作方法+适用边界

## 五步闭环

### Step 1：发现问题（不绕过）

工具卡顿/超时/规则失效时——**显式记录，不"忍一忍用别的方法"**。绕过=下次重踩；记录=开始闭环。

### Step 2：诊断根因（先查配置层）

按上面的配置层检查表逐项排查：approvals.mode → cwd → allowlist → 文档规则。**别急着怀疑命令本身**。

### Step 3：修复或降级

- 能自己改的（自己的config/SOUL.md/skill）：立即改
- 权限外的（全局config/基建脚本）：写corrections请求有权限角色修复

### Step 4：沉淀为知识

| 沉淀载体 | 适用 | 内容 |
|:---|:---|:---|
| skill故障表 | 每次任务必加载的skill | 故障→表现→回退方案（一坑一行） |
| dk卡 | 知识库（30_wiki/dark-knowledges/） | 完整案例：现象/根因/修复/教训 |
| corrections文件 | 60_feedback/corrections/ | 请求修复+证据+建议方案 |
| MOC注册 | 30_wiki/domains/ | 让下次会话/其他Agent可发现 |

### Step 5：验证闭环

下次遇到同类问题→查沉淀的记录→不重复踩。**验证成功的标志：同样的坑，第二次不再踩。**

## 王语嫣落地案例（2026-08-09）

| 环节 | 动作 |
|:---|:---|
| 发现问题 | search_files搜30_wiki多次超时（60s被杀）——一直默默降级terminal find |
| 诊断根因 | 查config发现cwd=/home/dministrator→递归跨/mnt/c全树→超时 |
| 修复/降级 | 显式传绝对路径`/mnt/c/Users/Administrator/Desktop/wiki/30_wiki` |
| 沉淀 | ①patch entry-quality-gate skill故障表（+3条）②发现老顽童已写corr_20260808（含4项修复请求）③本skill |
| 请求修复 | 老顽童corrections：cwd固定wiki + kdo加allowlist + queue_transition编码修复 |

## 为什么这个闭环对Agent重要

1. **打破"重复踩坑"**——Agent每次会话是新的，不沉淀=永远从零踩
2. **诊断者也能自我迭代**——不只执行者能修自己，诊断者能沉淀自己的工具链知识
3. **知识库是Agent的延伸记忆**——坑沉淀进KDO，等于Agent把经验写进自己的"大脑"
4. **多角色互相学习**——一个Agent踩的坑沉淀后，所有Agent受益（dk卡+MOC+skill三载体）

## 适用边界

- 适用：Agent遇到工具/配置/规则问题；想建立自我迭代习惯的Agent
- 不适用：业务知识类问题（那是诊断管线的事，不是配置闭环）；危险命令的执行（smart模式仍需行为自律）

## 关联

- `dk-agent-access-kdo-pitfalls`——外部Agent接入KDO三连坑（审批/cwd/检索规则）
- `entry-quality-gate` §已知工具故障与回退方案——王语嫣沉淀的故障表
- `corr_20260808_laowantong-hermes-config-layer-diagnosis.md`——老顽童配置层诊断+修复请求
- `kdo-moc`——KDO基建知识导航（Agent接入条目）
- `self-evolution`——周期自我进化（本skill是即时闭环，self-evolution是定期复盘）
