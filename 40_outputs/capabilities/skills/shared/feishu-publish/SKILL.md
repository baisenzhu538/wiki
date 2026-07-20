---
name: feishu-publish
description: "Publish any Markdown/text content as a Feishu Docx document with rich formatting, permission settings, batch writing, and GEO optimization. Use when other agents need to ship content to Feishu — '发飞书', 'publish to Feishu', 'create Feishu doc'. Routes through 段王爷."
version: 1.0.0
author: 段王爷
status: enriched
reviewed_by: 欧阳锋
review_date: 2026-07-07
updated_at: 2026-07-21
metadata:
  hermes:
    tags: [publishing, feishu, docx, distribution, ship]
    related_skills:
      - content-production
      - content-production-polish
      - kdo-self-attack
    caller: [huangyaoshi, hongqigong, laowantong, wangyuyan, ouyangfeng]
---

# 飞书文档发布引擎

> 把任何 Markdown/文本内容发布为飞书 Docx 文档，含富文本排版、权限设置、分批写入、GEO优化。

## 触发条件

| 场景 | 触发词 | 示例 |
|------|--------|------|
| 内容发布 | "发飞书""publish to Feishu" | "把这个分析发飞书" |
| 文档转换 | ODT/DOCX/文本 → 飞书 | "把这个Word转飞书" |
| Wiki提取 | 从飞书Wiki批量提取 | "把一堂Wiki那篇文章抓下来" |
| 批量发布 | 多篇统一发布 | "把这批文章全发飞书" |

## 核心能力

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
| ODT→飞书 | ✅ | XML解析保留表格+标题层级 |
| 图片嵌入 | ❌ | API限制，用消息配图替代 |
| 原生表格 | ⚠️ | ≤7列×≤12行可用，超限用文本表格 |

## 调用流程

```
其他 Agent → 段王爷：把这篇发飞书
段王爷 → 读源文件 → Markdown→Blocks → 创建doc → 分批写入 → 设权限 → 返回链接
```

## 已知限制

- 图片无法嵌入Docx（API限制），通过消息配图发送
- Convert API返回blocks顺序是乱的，必须手动构建
- 跨企业文档提取需OAuth（部分域TAT不可达）
- write_file截断需用subprocess绕行

## When NOT to Use

| 场景 | 原因 | 替代 |
|------|------|------|
| 内容还未通过审查 | 发布前必须先通过欧阳锋终审 | 等审查通过 |
| 目标渠道不是飞书 | 本skill只覆盖飞书Docx | 用 produce-and-ship-flow 选其他渠道 |
| 需要图片嵌入的文档 | API限制不支持 | 用消息配图或手动上传 |

## 参考卡片

- `skill-duanwangye-feishu-publishing` — 本skill的wiki卡版本
- `skill-duanwangye-kdo-pipeline` — produce→validate→ship完整闭环
- `concept-feishu-api-pagination-trap` — 飞书API分页陷阱
- `concept-streaming-extraction-pattern` — 流式提取模式
