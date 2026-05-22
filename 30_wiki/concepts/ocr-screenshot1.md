---
title: "OCR: screenshot1"
type: "concept"
status: "enriched"
source_refs: ["src_20260522_64727b82"]
created_at: "2026-05-21T20:13:51+00:00"
updated_at: "2026-05-22T06:49:36+00:00"
---




# OCR: screenshot1

## Summary

原图: `00_inbox/screenshot1.

png` KimiCodeAPI同时兼容OpenAl和Anthropic两种协议。

不同工具对地址配置的要求不同： •BaseURL：部分工具(如ClaudeCode)只需填写BaseURL，工具会自动拼接后续路径。

## Source Refs

- `src_20260522_64727b82` -> `10_raw/sources/src_20260522_64727b82-ocr-screenshot1.md`

## Reusable Knowledge

- KimiCodeAPI supports both OpenAI and Anthropic protocol formats with different URL configuration requirements depending on the tool used.
- For OpenAI-compatible protocol, use BaseURL `https://api.kimi.com/coding/v1` or full endpoint `https://api.kimi.com/coding/v1/chat/completions`.
- For Anthropic-compatible protocol, use BaseURL `https://api.kimi.com/coding/` or full endpoint `https://api.kimi.com/coding/v1/messages`.
- Some tools like ClaudeCode only need BaseURL and auto-append paths; others like Trae require the complete endpoint URL.
- API keys can be created and managed in the KimiCode console by Kimi members, limited to 5 keys, displayed only once at creation.
- The universal model ID for all third-party tool integrations is `kimi-for-coding`, used in the model field regardless of protocol choice.
- The `kimi-for-coding` model ID is fixed and automatically maps to the latest released model version on the backend.

## Open Questions

- What is the exact path auto-appended by ClaudeCode when given the Anthropic BaseURL `https://api.kimi.com/coding/` — does it expect `/v1/messages` or a different path?
- Does the "5 API keys maximum" limit apply per account, per organization, or per project/workspace within KimiCode console?
- What happens when the backend auto-updates the model behind `kimi-for-coding` — is there any version pinning mechanism, notification, or breaking change policy for users?
- Are there rate limits, pricing tiers, or regional restrictions for KimiCodeAPI that differ between OpenAI-compatible and Anthropic-compatible endpoints?
- What authentication method is used for the API key — is it a Bearer token in the Authorization header, and does this differ between the two protocol implementations?
- Does "Kimi会员" (Kimi member) refer to a free-tier account, a paid subscription tier, or a specific developer program — and what are the eligibility requirements?
- What is the fallback or error behavior if a tool configured with BaseURL sends a request to an unsupported or non-standard endpoint path?
- Are there any supported parameters or features (e.g., streaming, function calling, system prompts) that differ in availability or behavior between the OpenAI-compatible and Anthropic-compatible protocol implementations?

## Output Opportunities

Content: <article: "KimiCodeAPI Multi-Protocol Integration Guide" — a configuration reference bridging OpenAI-compatible and Anthropic-compatible endpoints for ClaudeCode, Trae, and similar tools, covering BaseURL vs full endpoint selection, universal model ID usage, and API key lifecycle management>
Code: <script: `kimi-code-api-config-validator.js` — Node.js tool that validates endpoint configurations against protocol-specific rules, auto-detects whether a tool requires BaseURL or full endpoint, and generates ready-to-paste config snippets for ClaudeCode, Trae, and other supported tools>
Capability: <workflow: "Screenshot-to-Structured-KDO-Ingestion Pipeline" — a playbook integrating PaddleOCR ONNX extraction, automated OCR quality validation (ligature correction, visual structure reconstruction), and KDO source YAML generation with cross-referenced metadata validation for screenshot-based knowledge capture>
