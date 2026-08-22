---
title: Agent 修复记录目录
type: index
status: active
domain: infrastructure
created_at: '2026-08-22'
updated_at: '2026-08-22'
author: 欧阳锋
---

# Agent 修复记录目录

> 所有 agent 故障修复记录的统一存放处——不只 codex：relay/网关/hermes 服务/飞书/各角色 Agent 的故障排查与修复，全部按规范记在这里。

## 什么时候写

- 任何 agent/服务/进程故障被修复后，**当天写入** + commit
- 故障排查时**先查本目录**——同类故障可能已记录，直接定位

## 命名规范

```
<agent>-<故障简述>-<YYYY-MM-DD>.md
```

示例：`codex-relay-fix-2026-08-22.md` / `hermes-gateway-timeout-2026-08-25.md`

## 文件模板

每份记录包含（按序）：

| 节 | 内容 |
|:--|:--|
| frontmatter | title / type: memo / status / domain: infrastructure / author / related |
| 一句话摘要 | 故障 → 根因 → 修复，三要素一行说清 |
| 故障现象 | 报错原文、现象、复现条件 |
| 根因 | 诊断过程 + 证据（日志/端口/任务查询输出） |
| 修复动作 | 逐步命令 + 说明；含踩坑（如 Git Bash MSYS 路径转换） |
| 验证结果 | 修复后实测证据（监听/接口返回/日志） |
| 架构真相 | 正确架构与劣化陷阱（防止下次修偏） |
| 历史与教训 | 同类故障的时间线、复发模式、待验证项 |
| 跟进项 | 遗留验证、观察项、下次故障排查速查 |

## 索引

| 文件 | Agent | 故障 | 日期 |
|:--|:--|:--|:--|
| [codex-relay-fix-2026-08-22.md](codex-relay-fix-2026-08-22.md) | codex-relay | 502 Bad Gateway（4444 无监听 + 自启任务丢失） | 2026-08-22 |

> 新记录写入后，在索引表追加一行（保持 README 可 grep）。
