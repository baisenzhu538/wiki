---
id: skill-duanwangye-feishu-publishing
title: 段王爷·飞书文档发布引擎 — 从内容到飞书docx的全链路发布
type: skill
status: reviewed
confidence: 0.95
trust_level: high
domain:
- publishing
- feishu
- agent-capability
source_refs:
- capability/duanwangye/feishu-publishing
author: 段王爷（南帝）
reviewed_by: 欧阳锋
review_date: '2026-07-07'
related:
- '[[skill-duanwangye-wechat-extraction]]'
- '[[skill-duanwangye-kdo-pipeline]]'
- '[[feishu-docx-pagination-extraction]]'
- '[[concept-feishu-api-pagination-trap]]'
- '[[concept-streaming-extraction-pattern]]'
tags:
- audience:executor
- scene:execution
- skill-level:advanced
discoverable_by:
- 段王爷发布
- 飞书文档
- 全链路发布
- docx发布
- KDO发布管线
---

# 段王爷·飞书文档发布引擎

> **一句话**：把任何 Markdown/文本内容发布为飞书 Docx 文档，含富文本排版、权限设置、分批写入、GEO优化。

## 其他 Agent 何时调用我

| 场景 | 触发条件 | 示例 |
|------|---------|------|
| 内容发布 | 黄药师/洪七公产出需发布到飞书 | "把这个分析发飞书" |
| 文档转换 | ODT/DOCX/文本需转飞书docx | "把这个Word转飞书" |
| Wiki提取 | 需从飞书Wiki批量提取内容 | "把一堂Wiki那篇文章抓下来" |
| 批量发布 | 多篇内容需统一发布+追踪 | "把这批文章全发飞书" |

## 我的核心能力

| 能力 | 状态 | 说明 |
|------|------|------|
| 创建飞书文档 | ✅ | Docx API v1，Markdown→Blocks自动解析 |
| 富文本排版 | ✅ | H1-H4标题、粗体、列表、引用、分割线、代码块 |
| 文本表格 | ✅ | 粗体表头+分隔线+数据行，零API失败 |
| 权限设置 | ✅ | anyone_readable + external_access |
| 分批写入 | ✅ | 50块/批，失败逐块重试 |
| GEO优化 | ✅ | 标题关键词、结构化摘要、可引用片段 |
| Wiki SSR提取 | ✅ | 双路径（clientVars + 直挂），零API零权限 |
| Wiki API提取 | ✅ | Docx API全量提取，含分页安全版 |
| 远程MCP | ✅ | fetch-doc/create-doc，零安装HTTP调用 |
| 跨企业文档 | ✅ | MCP TAT提取（部分域需OAuth UAT） |
| ODT→飞书 | ✅ | XML解析保留表格+标题层级 |
| 图片嵌入 | ❌ | API限制，用消息配图替代 |
| 原生表格 | ⚠️ | ≤7列×≤12行可用，超限用文本表格 |

## 调用姿势

```
用户 → 段王爷：把这篇发飞书
段王爷 → 读文件 → Markdown→Blocks → 创建doc → 分批写入 → 设权限 → 返回链接
```

## 已知限制

- 图片无法嵌入Docx（API限制），通过消息配图发送
- Convert API返回blocks顺序是乱的，必须手动构建
- 跨企业文档提取需OAuth（部分域TAT不可达）
- write_file截断需用subprocess绕行
