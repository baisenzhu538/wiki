# VLM 描述：screenshot1

**原图**: `C:\Users\Administrator\Desktop\wiki\00_inbox\_vlm_reprocess\_batch_其他\screenshot1.png`

**模型**: `MiniMax-M3`

## 结构化描述

- **类型**: 信息图
- **标题**: Kimi Code API 地址配置说明
- **置信度**: 0.95
- **视觉风格**: 极简、科技、文档风格，采用白底黑字配灰色表格的清爽排版，使用项目符号和无序列表组织信息，URL 以蓝色等宽字体显示，关键名词以代码样式高亮

### 描述

这是一张技术文档截图，介绍了 Kimi Code API 的地址配置方法。文档说明 Kimi Code API 同时兼容 OpenAI 和 Anthropic 两种协议，并详细列出两种协议对应的 Base URL 和常用 Endpoint 示例。文档分为三个主要部分：地址配置说明（包含表格展示两种协议的 URL 对比）、获取 API Key 的方法说明、以及模型 ID 的使用规范，强调统一使用 kimi-for-coding 作为 model 字段值。整体为白色背景的网页文档排版，文字与表格结合呈现。

### 关键元素

- Kimi Code API 协议兼容性说明文字
- Base URL 与完整 Endpoint 的区别说明（提到 Claude Code 和 Trae 等工具）
- 三列对比表格：协议、Base URL、常用 Endpoint 示例
- OpenAI 兼容行：Base URL 为 https://api.kimi.com/coding/v1，Endpoint 示例为 https://api.kimi.com/coding/v1/chat/completions
- Anthropic 兼容行：Base URL 为 https://api.kimi.com/coding/，Endpoint 示例为 https://api.kimi.com/coding/v1/messages
- 「获取 API Key」标题及说明（最多 5 个，提及 Kimi Code 控制台）
- 「模型 ID」标题及说明（统一使用 kimi-for-coding）
- 代码样式标记：kimi-for-coding、model
- 超链接：Kimi Code 控制台

### 标签

- Kimi Code
- API 文档
- OpenAI 兼容
- Anthropic 兼容
- Base URL
- Endpoint
- API Key
- 模型 ID
- 技术文档
- 开发者指南

### 适用场景

适用于 AI 开发工具集成教程、第三方编程工具配置指南、API 对接文档参考、开发者技术博客配图、AI 编程助手接入说明等场景

## 原始 JSON

```json
{
  "category": "信息图",
  "title": "Kimi Code API 地址配置说明",
  "description": "这是一张技术文档截图，介绍了 Kimi Code API 的地址配置方法。文档说明 Kimi Code API 同时兼容 OpenAI 和 Anthropic 两种协议，并详细列出两种协议对应的 Base URL 和常用 Endpoint 示例。文档分为三个主要部分：地址配置说明（包含表格展示两种协议的 URL 对比）、获取 API Key 的方法说明、以及模型 ID 的使用规范，强调统一使用 kimi-for-coding 作为 model 字段值。整体为白色背景的网页文档排版，文字与表格结合呈现。",
  "key_elements": [
    "Kimi Code API 协议兼容性说明文字",
    "Base URL 与完整 Endpoint 的区别说明（提到 Claude Code 和 Trae 等工具）",
    "三列对比表格：协议、Base URL、常用 Endpoint 示例",
    "OpenAI 兼容行：Base URL 为 https://api.kimi.com/coding/v1，Endpoint 示例为 https://api.kimi.com/coding/v1/chat/completions",
    "Anthropic 兼容行：Base URL 为 https://api.kimi.com/coding/，Endpoint 示例为 https://api.kimi.com/coding/v1/messages",
    "「获取 API Key」标题及说明（最多 5 个，提及 Kimi Code 控制台）",
    "「模型 ID」标题及说明（统一使用 kimi-for-coding）",
    "代码样式标记：kimi-for-coding、model",
    "超链接：Kimi Code 控制台"
  ],
  "visual_style": "极简、科技、文档风格，采用白底黑字配灰色表格的清爽排版，使用项目符号和无序列表组织信息，URL 以蓝色等宽字体显示，关键名词以代码样式高亮",
  "tags": [
    "Kimi Code",
    "API 文档",
    "OpenAI 兼容",
    "Anthropic 兼容",
    "Base URL",
    "Endpoint",
    "API Key",
    "模型 ID",
    "技术文档",
    "开发者指南"
  ],
  "usable_for": "适用于 AI 开发工具集成教程、第三方编程工具配置指南、API 对接文档参考、开发者技术博客配图、AI 编程助手接入说明等场景",
  "confidence": 0.95
}
```
