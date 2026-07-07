---


id: tinyfish-agentic-web-infrastructure
created_at: 2026-05-06
domain: master
review_date: 2026-05-06
reviewed_by: 黄药师
review_notes: 历史遗留，写审分离规则确立前的早期卡片。有效性由月度抽检覆盖。
status: draft
title: TinyFish — Agentic Web 基础设施建设层 Skill
trust_level: medium
type: concept
updated_at: '2026-06-16'
author: unknown
confidence: 0.7
source_refs:
- src_unknown
source_context: （原始 source 无法追溯，已标记为 src_unknown，待后续补充）
related:
  - "[[paddleocr-skill]]"
  - "[[plan_20260621_skill-iteration-standard]]"
  - "[[dk-skill-market-agent-self-install]]"
  - "[[tool-yitang-web-scraping-research]]"
  - "[[web-scraping-三剑客-scrapling-crawl4ai-firecrawl]]"
---
# TinyFish — Agentic Web 基础设施建设层 Skill

> $47M Series A (led by ICONIQ)，为 AI Agent 提供 Search/Fetch/Browser/Agent 一体化 Web 操作基础设施。

## Summary

TinyFish 是 Palo Alto 公司（2024年成立，11-50人）推出的四合一 Web 基础设施平台。将 **Search、Fetch、Browser、Agent** 四项能力统一在一个 API Key 下，以 SKILL.md + CLI 架构直接嵌入 AI Coding Agent（Claude Code / Cursor / Codex 等）。定位不是爬虫，是 **Agentic Web 的操作系统层**。

---

## Claims

### 四产品体系（一套 API Key）

| 产品 | 做什么 | 性能指标 | 使用场景 |
|------|--------|---------|---------|
| **Web Search** | 结构化搜索，Chromium 实时抓取 | P50 ~488ms | 找 URL、快速信息发现 |
| **Web Fetch** | URL → 干净 Markdown/JSON/HTML | 批量并行，失败不扣费 | 读文章、文档、静态页面 |
| **Web Browser** | 托管 Stealth Chrome，CDP 协议 | <250ms 冷启动 | 复杂交互、需自定义脚本 |
| **Web Agent** | 自然语言目标 → 多步自主操作 | Mind2Web 89.9% | 动态页面、表单交互、数据提取 |

### 使用策略（轻到重）

```
search  →  fetch  →  agent  →  browser
最轻                             最重
```

**核心原则**：用最轻的工具完成任务，不行才升级。

### 安装与认证

```bash
npm install -g @tiny-fish/cli
tinyfish auth login   # 需要 TINYFISH_API_KEY
```

### 四工具命令速览

```bash
# 1. Search — 找链接
tinyfish search query "best React state management 2026"

# 2. Fetch — 读内容（支持多 URL 并行）
tinyfish fetch content get --format markdown "https://example.com/page"

# 3. Agent — 自然语言驱动 Web 操作
tinyfish agent run --url "https://example.com/products" \
  "Extract all products as JSON: [{\"name\": str, \"price\": str}]"

# 4. Browser — 裸浏览器会话
tinyfish browser session create --url "https://example.com"
```

### 常见组合模式

| 模式 | 流程 | 适用 |
|------|------|------|
| **Research** | search → fetch | 调研场景：搜主题 → 读全文 |
| **Deep Extraction** | search → agent | 找目标站 → 交互提取结构化数据 |
| **Escalation** | fetch → agent | fetch 空结果 → 升级到 agent |
| **Full Control** | agent → browser | agent 不够 → 裸 CDP 控制 |

### 与我们现有工具栈的定位

| 工具 | 定位 | 层面 | 状态 |
|------|------|------|------|
| **Scrapling** | Python 本地反反爬库 | 库 | 可用 |
| **Crawl4AI** | 开源 LLM 友好爬虫 | 框架 | 依赖修复中 |
| **Firecrawl** | API-first 托管爬虫（$19-749/月） | 平台 | 需付费 Key |
| **TinyFish** | 4合1 Agent 基础设施（500步免费/$15起） | 基础设施层 | **已安装 Skill** |

---

## Critique

### 前提假设

- src_unknown
- src_unknown
- src_unknown

### 边界与反例

- src_unknown
- src_unknown
- src_unknown

### 与 business-research Skill 的关系

- src_unknown
- src_unknown
- src_unknown

### 可靠性

**整体：中高。** TinyFish 的客户名单（Google、DoorDash、Volkswagen）和 $47M 融资表明其基础设施质量经得起验证。但作为年轻的创业公司，API 稳定性和长期可用性存在不确定性。

---

## Synthesis

- 待补充链接
- 待补充链接
- 待补充链接
- 待补充链接
### Skill 类型体系（至此形成三个品类）

| 类型 | Skill | 特征 | 安装方式 |
|------|-------|------|---------|
| **methodology** | business-research | 方法论执行引擎，流程驱动 | 完整 SKILL.md + references/ + templates/ |
| **persona** | truman-perspective | 人格模拟器，角色扮演 | SKILL.md + references/research/（6 Agent 调研） |
| **tool** | use-tinyfish | 基础设施工具，CLI 驱动 | SKILL.md（pre-flight check + 命令速查） |

### 可迁移到 KDO 的改进

- 待补充链接
- 待补充链接
- 待补充链接
### 不要用的场景

| 场景 | 为什么失效 | 替代方案 |
|------|-----------|---------|
| 把这个框架/方法当成绝对真理执行 | 任何方法论都是时间截面，它们假设未来会像过去一样发展 | 每次使用前先问"这个结论现在还成立吗？有没有新的反例出现？" |
## Open Questions

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## Output Opportunities

- src_unknown
- src_unknown
- src_unknown

## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|---------|-----------|---------|
| 需要基于这份调研/框架做出关键决策前 | 先问自己"这个结论现在还成立吗？有没有新的反例出现？" | 每次使用前都能说出至少一个可能影响结论有效性的新变化因素 |
