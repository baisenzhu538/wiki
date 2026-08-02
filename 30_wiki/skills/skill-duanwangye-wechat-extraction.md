---
id: skill-duanwangye-wechat-extraction
title: 段王爷·微信消息解密与结构化提取
type: skill
status: reviewed
confidence: 0.9
trust_level: high
domain:
- wechat
- data-extraction
- agent-capability
source_refs:
- capability/duanwangye/wechat-mcp
author: 段王爷（南帝）
reviewed_by: 欧阳锋
review_date: '2026-06-29'
related:
- '[[skill-duanwangye-feishu-publishing]]'
- '[[concept-streaming-extraction-pattern]]'
tags:
- audience:executor
- scene:execution
- skill-level:advanced
discoverable_by:
- 微信消息解密
- 微信提取
- 聊天记录解析
- 结构化提取
- 段王爷微信
---

# 段王爷·微信消息解密与结构化提取

> **一句话**：从加密微信SQLite数据库提取聊天记录，支持群聊搜索、私聊查询、时间范围过滤、上下文扩展。

## 其他 Agent 何时调用我

| 场景 | 触发条件 | 示例 |
|------|---------|------|
| 群聊分析 | 需分析特定群聊的讨论内容 | "把Vikki战队2群最近一周的消息提取出来" |
| 用户反馈收集 | 需从微信收集用户反馈/需求 | "查一下上周关于OPC定价的讨论" |
| 聊天记录归档 | 需将微信聊天转为结构化文档 | "把大航海群结业分享整理成文档" |

## 我的核心能力

| 能力 | 状态 | 说明 |
|------|------|------|
| 群聊搜索 | ✅ | contact.db按群名→wxid→MD5→Msg_表名→SQL查询 |
| 私聊查询 | ✅ | Msg_MD5(wxid)表直接读 |
| 时间范围 | ✅ | create_time BETWEEN毫秒时间戳过滤 |
| 上下文扩展 | ✅ | 关键词命中→local_id±N行自动扩展 |
| 多账号 | ✅ | 大号baconzhu_5d29(34MB)+小号(3MB) |
| 语音转录 | ✅ | 提取语音→faster-whisper转文字 |
| 结构化输出 | ✅ | 原始消息→主题归类→Markdown→飞书/本地 |

## 调用姿势

```
用户 → 段王爷：查XX群最近一周的消息
段王爷 → contact.db搜群名→计算Msg_表名→SQL查询→结构化整理→交付
```

## 已知限制

- 需微信登录状态才能解密最新消息（解密DB是静态快照）
- 语音/图片/文件为二进制blob，不可直接还原原文
- WSL下需先cp DB到/tmp/避免跨文件系统I/O错误
