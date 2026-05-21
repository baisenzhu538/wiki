---
source_id: "src_ocr_screenshot1"
kind: "image_ocr"
captured_at: "2026-05-22T04:13:07.137770"
original_image: "00_inbox/screenshot1.png"
ocr_engine: "paddleocr_onnx"
char_count: 554
trust_level: "medium"
freshness: "2026-05"
rights: "yitang_course_material"
---

# OCR: screenshot1

原图: `00_inbox/screenshot1.png`

## OCR 原文

KimiCodeAPI同时兼容OpenAl和Anthropic两种协议。不同工具对地址配置的要求不同：
•BaseURL：部分工具(如ClaudeCode)只需填写BaseURL，工具会自动拼接后续路径。
•完整Endpoint：部分工具(如Trae)需要填写完整的API请求地址。
按需选择对应的地址：
协议 BaseURL 常用Endpoint示例
OpenAl
兼容 https://api.kimi.com/coding/v1 https://api.kimi.com/coding/v1/chat/completions
Anthropic
兼容 https://api.kimi.com/coding/ https://api.kimi.com/coding/v1/messages
上
获取APIKey
Kimi会员可在KimiCode控制台创建和管理(最多5个，仅创建时显示一次，请妥善保存）。
模型ID
在第三方工具中调用KimiCodeAPI时，请统一使用模型IDkimi-for-coding。无论是OpenAl
兼容协议还是Anthropic兼容协议，请求体里的model字段都填这个值。
说明：kimi-for-coding是固定的模型ID，后端会根据最新发布的模型自动更新其对应的

## 备注

- 本文件由 PaddleOCR ONNX pipeline 自动提取
- 可能存在连字/误识，需要人工校对
- 视觉结构信息（标题/正文/表格分块）未在 OCR 中体现，需要结合原图理解
