---
id: tool-kdo-wechat-serendipity-collect
title: KDO 偶遇采集管线：手机转发链接 → 全自动入库（视频号/今日头条/公众号）
type: tool
status: reviewed
confidence: 0.9
trust_level: high
language: zh-CN
created_at: 2026-08-18
updated_at: 2026-08-19
domain:
- knowledge-management
- ai-collaboration
- infrastructure
aliases:
- 偶遇采集
- 偶遇自动采集
- 视频号转知识库
- 视频号逐字稿
- 手机转发视频
- 自动入库
- 今日头条视频
- 头条视频
- toutiao
- wechat-serendipity
- 文件传输助手采集
- 超级入口
- KDO偶遇采集
discoverable_by:
- 偶遇采集
- 视频号 逐字稿
- 今日头条 视频
- 自动入库
- 手机转发
- 文件传输助手
- 逐字稿自动化
- wechat_link_monitor
- parse_sph
- 元宝
author: 黄药师
reviewed_by: 待审
source_refs:
- 70_product/projects/proj_20260816_wechat-collect-顶层文档.md
- 40_outputs/code/scripts/wechat-serendipity-collect-guide.md
- 40_outputs/code/scripts/wechat_link_monitor.py
- 40_outputs/code/scripts/wechat_knowledge.py
- 40_outputs/code/scripts/yuanbao_cookie_extract.py
related:
- framework-serendipity-five-channels
- tool-wechat-transcript-automation-workflow
- framework-knowledge-five-leaps
- tool-autoclassify-seven-steps
- framework-patrolkit-radar
tags:
- audience:all-agents
- scene:execution
- skill-level:intermediate
- method:automation
- content-format:tool
quality_labels:
- actionable
- validated
- cited
diagnostic_signals:
- signal: 用户问"偶遇采集怎么做/视频号怎么自动进知识库/头条视频怎么转逐字稿"
  lens: 其他 agent 被问到偶遇采集能力时——检索本卡回答，不凭记忆
  follow_up: 读本卡链路+脚本路径，指导用户复制链接转发即可
---

# KDO 偶遇采集管线（手机转发链接 → 全自动入库）

> 楚门「偶遇自动采集五通道」通道② 的 KDO 落地（`framework-serendipity-five-channels`）。
> **用户操作 = 手机复制链接转发一次，其余全自动**（每 10 分钟计划任务无人值守）。
> 实测闭环：视频号 WorkBuddy ×2、今日头条 Clean Code 视频——零人工。

## 使用方式（用户视角）

```
手机：视频号/头条/公众号 → 分享 → 复制链接 → 发送到 文件传输助手/任意群
  → 10 分钟内自动：提取 → 解析直链 → 下载 → GPU 转写 → LLM 三层次知识化
  → 00_inbox/wechat-collect/（待转正入仓）
```

## 支持通道

| 通道 | 链接格式 | 解析方式 |
|:--|:--|:--|
| 视频号 | `weixin.qq.com/sph/xxx`（复制链接） | parse_sph（元宝 Cookie）→ finder.video.qq.com 直链 |
| 今日头条视频 | `m.toutiao.com/video/xxx` | info API → token → vod.bytedanceapi.com 直链 |
| 今日头条文章 | `m.toutiao.com/group/xxx`、`/article/xxx`、`/isXXX/` 短链 | info API → content HTML → 纯文本入库 |
| 公众号文章 | `mp.weixin.qq.com/s/...` | 抓 HTML 正文入库 |

> ⚠️ 视频号"直接转发卡片"无解析入口（微信设计），需电脑播放拦截（兜底）。
> 🆕 2026-08-19：文章（公众号/头条）同样自动走 LLM 三层次知识化；链接按规范化键去重（公众号 `__biz+mid+idx`、头条 gid），同一内容多次转发只采一次。

## 组件与路径

| 组件 | 路径 | 作用 |
|:--|:--|:--|
| 监控脚本 | `kdo-tools/wechat_link_monitor.py`（40_outputs 副本） | 全链路主控：数据库解密→提取→解析→下载→转写→知识化→自动转正 |
| 知识化 | `kdo-tools/wechat_knowledge.py` | LLM 三层次（事实/规律/洞察），DeepSeek v4-flash |
| Cookie 重建 | `kdo-tools/yuanbao_cookie_extract.py` | CDP 提取元宝全量 Cookie（1 个月过期重建） |
| 解析服务 | `C:\Users\Administrator\tools\wx_channels_download_bin\` | parse_sph API 127.0.0.1:2022（ltaoo v260817，元宝 Cookie） |
| 微信解密 | `C:\Users\Administrator\wechat-decrypt\` | SQLCipher 4 数据库解密（passphrase 复用） |
| 转写引擎 | WSL `/home/dministrator/wechat-collect/transcribe.py` | faster-whisper GPU |
| 计划任务 | `wechat-link-monitor`（每 10 分钟）+ `wx-channels-download`（登录自启） | 无人值守 |

## 运维要点

- **元宝 Cookie 约 1 个月过期**：过期后 `yuanbao_cookie_extract.py` 重建（Edge 调试端口 9222 + 用户扫码）
- **产物铁律**：第一站 `00_inbox/wechat-collect/`，未经 ingest/validate 不入 `10_raw/30_wiki`；`wechat_promote.py` 自动转正
- **故障速查**：`40_outputs/code/scripts/wechat-serendipity-collect-guide.md` §六（no cookie/无法播放/加密视频/403/WAL 未合并）
- **MCP 检索**：段王爷等 agent 用 kdo_search 即可检索本卡（#351 后 8.6s 响应）

## When NOT to Use

| 误用场景 | 正确做法 |
|:--|:--|
| 直接转发视频号卡片（非复制链接） | 引导用户"复制链接"转发；卡片仅电脑播放拦截兜底 |
| 大规模商业采集 | 合规评估；仅个人学习用途 |
| 元宝 Cookie 过期未重建 | 先重建 Cookie 再使用（否则"此内容暂时无法播放"） |

## Skill 挂载

- Claude Code Skill：`.claude/skills/wechat-serendipity-collect/`（触发词：偶遇采集/视频号转知识库/手机转发视频/视频号逐字稿/自动入库/今日头条/toutiao）
- 其他 agent 检索本卡即可获得完整能力链路
