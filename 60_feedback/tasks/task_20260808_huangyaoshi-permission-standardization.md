---
id: task_20260808_huangyaoshi-permission-standardization
task_id: 262
assignee: huangyaoshi
status: queued
updated_at: 2026-08-08
domain: system
priority: P0
---

# #262 命令权限标准化（agent 被拦问题治理）

## 背景（用户实测触发）

多角色 agent 反馈"命令行方式被拦截/权限问题"。核查根因：
1. **allowlist 缺口**：wiki/.claude/settings.json 允许 python/kdo/git/ls 等，但 **cd 不在列表**（agent 最常用的"cd 进 wiki 再跑命令"被拦——复合命令匹配规则只认开头）；node/curl/grep 等常用工具缺失
2. **模板与实际不一致**：`.agent/permissions-template.json`（新 agent 部署模板）允许项远少于实际 settings.json——**新 agent 按模板部署天然权限不足**（"经常被拦"的根源）
3. **飞书端（Hermes）**：命令执行层是另一套（WSL/Hermes gateway）——需单独确认其白名单/沙箱配置（coach 能跑 kdo feature 是特例不是标配）

## ⚠️ 环境区分修正（2026-08-09 用户纠正——王语嫣概念错误修正）

**飞书端 agent 跑的是 Hermes（WSL gateway），不是 Claude Code**——权限拦截机制是 Hermes 自己的工具执行配置（WSL 侧 hermes-gateway-* 服务），**不是** wiki/.claude/settings.json 的 allowlist。

两个环境分开处理：
- **Hermes 端（飞书全体 agent——重点）**：查 WSL 侧 hermes-gateway-* 的配置（工具权限/命令白名单/sandbox 机制）——这是"经常被拦截"的主战场
- **Claude Code 端（CLI/终端侧 agent）**：settings.json allowlist（cd 缺失等问题）——次要，但顺手修

## 任务目标

命令权限三处标准化：

### 1. wiki settings.json allowlist 补齐（实际生效层）
补常见被拦命令：`Bash(cd )`（含复合命令 cd && ... 模式）、`Bash(node )`、`Bash(grep )`、`Bash(curl )`、`Bash(cat )`、`Bash(wc )`、`Bash(mkdir )` 等（黄药师按实际使用审计补充，dry-run 后落盘）

### 2. permissions-template.json 对齐（新 agent 部署层）
模板更新为与 settings.json 一致（或引用同一份清单）——**新 agent 部署不再天然缺权限**

### 3. 飞书端 Hermes 命令执行配置确认
- 确认 Hermes gateway 的命令执行白名单/沙箱机制
- coach 已可用的 kdo feature/python 调用——确认是特例还是通用配置；通用化（#260/#261 的 agent 体系配套）

### 4. 被拦命令清单收集
- 从近期会话/agent 反馈收集常见被拦命令（grep 权限日志或 agent 复盘）
- 输出：常见被拦命令 → 处置（加入 allowlist / 改用法 / 明确拒绝）

## 验收标准

1. settings.json + template 更新落盘，新部署 agent 默认可跑核心命令（cd/python/kdo/git 复合）
2. 飞书端任一 agent 实测：终端操作 + kdo feature 调用不再被拦
3. 被拦命令清单产出（≥5 条常见项 + 处置）
4. 无权限事故回归（#260/#261 的 agent 实测不受影响）

## 依赖 / 边界

- 与 #261（agent 全局认知）配套——权限是认知的落地条件
- 只加必要命令（最小权限原则，不加无谓的宽放）
- 用户级 settings.json（C:\Users\Administrator\.claude\）如需同步由黄药师裁定

## 🆕 教练实测偏差处置（2026-08-09 飞书 coach 实测发现，王语嫣字节级验证确认）

**偏差 1：SOUL.md 检索规则过时**——写"Feature 点菜用 `kdo feature`"，但 kdo 命令无 feature 子命令（实际入口 `kdo-tools/feature_menu.py`）。处置：更新 SOUL.md/检索规则文档为实际入口；或把 feature_menu.py 注册为 kdo 子命令（统一入口，黄药师裁定——最小动作是改文档）

**偏差 2：cap_hub/features.json GBK 编码**——UTF-8 解码失败（字节级确认），其他工具读取会乱码。处置：转码 UTF-8（对齐全库标准），转码后验证 json 可解析 + FEATURE_MENU 读取正常

## 🆕 飞书欧阳锋请求并入（2026-08-09，corr_20260808_ouyangfeng-self-iteration.md）

① `cmd.exe`/`iconv`/`dir` 等只读命令加进 approvals whitelist（飞书欧阳锋实测：复杂内联命令被 BLOCKED——"user has NOT consented"）
② 飞书网关 approvals.mode 评估（至少只读命令放行；长期 smart——教练侧已实测验证 smart 生效）
④ production-queue 编码统一修复（UTF-8-SIG 混合 mojibake，历史遗留挂账——本次落实）

**请求③（ouyangfeng-context.md runtime）不归本任务**——双实例问题（Claude 端 Kimi Code CLI 描述正确），由用户拍板：共享文件双注 vs 飞书端独立配置。
