---
title: "TinyFish — Agentic Web 基础设施建设层 Skill"
type: concept
status: enriched
domain: ['master']
source_refs: []
created_at: "2026-05-06"
updated_at: "2026-05-06"
related:
  - "[[web-scraping-三剑客-scrapling-crawl4ai-firecrawl]]"
  - "[[business-research-skill-oscar-13-weapon-system]]"
  - "[[truman-perspective-skill]]"
  - "[[KDO Protocol]]"
tags:
  - "#skill"
  - "#web-infrastructure"
  - "#agentic-web"
  - "#tool"
  - "#tinyfish"
trust_level: high
reviewed_by: "黄药师"
review_date: "2026-05-06"
---

# TinyFish — Agentic Web 基础设施建设层 Skill

> $47M Series A (led by ICONIQ)，为 AI Agent 提供 Search/Fetch/Browser/Agent 一体化 Web 操作基础设施。

## Summary

TinyFish 是 Palo Alto 公司（2024年成立，11-50人）推出的四合一 Web 基础设施平台。将 **Search、Fetch、Browser、Agent** 四项能力统一在一个 API Key 下，以 SKILL.md + CLI 架构直接嵌入 AI Coding Agent（Claude Code / Cursor / Codex 等）。定位不是爬虫，是 **Agentic Web 的操作系统层**。

---

## [Condense] 核心架构

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

## [Critique] 批判性评估

### 前提假设

- 假设 Agent 端点（Mind2Web 89.9%）在生产环境中的可靠性接近基准分数。【可靠性：中】基准是标准化任务，真实 Web 的碎片化程度远超基准数据集
- 假设 CLI + Skills 架构（87% token reduction vs MCP）在所有 Agent 框架中普遍适用。【可靠性：中高】测试数据来自 TinyFish 自己，但 token 节省的逻辑是合理的——写文件比塞上下文窗口更省
- 假设 500 步免费额度足够开发者的评估和原型阶段。【可靠性：高】但对重度使用者，免费额度可能在几轮对话内耗尽

### 边界与反例

- **最适合**：AI Agent 需要搜索/抓取/操作真实网站的场景——商业调研、竞品监控、数据采集
- **不适合**：本地文件操作、纯 API 数据源、不需要浏览器渲染的简单 HTTP 请求
- **关键限制**：依赖 TinyFish 的托管基础设施，不是本地工具；API 服务稳定性取决于 TinyFish 的运维水平

### 与 business-research Skill 的关系

- **互补关系**：business-research 的 Step 3（在线信息采集）可以用 TinyFish Search + Fetch 替代通用 WebSearch，获得更结构化、更可控的信息源
- **增强关系**：business-research 的 Step 5（线下武器）中"产品体验"部分，TinyFish Agent 可以替代部分人工操作（表单填写、交互式页面浏览）
- **非替代关系**：TinyFish 不提供 OSCAR 调研框架、质量门、15项机械检查——这些是 business-research Skill 独有的

### 可靠性

**整体：中高。** TinyFish 的客户名单（Google、DoorDash、Volkswagen）和 $47M 融资表明其基础设施质量经得起验证。但作为年轻的创业公司，API 稳定性和长期可用性存在不确定性。

---

## [Synthesis] 与 wiki 知识库的关联

- [[web-scraping-三剑客-scrapling-crawl4ai-firecrawl]] — TinyFish 是第四个维度：从"爬虫工具"升级到"Agentic Web 基础设施"。四者形成层次：库(Scrapling) → 框架(Crawl4AI) → API平台(Firecrawl) → Agent基础设施(TinyFish)
- [[business-research-skill-oscar-13-weapon-system]] — TinyFish 可以成为 business-research 的"在线采信引擎"——Step 3 Search 替代通用搜索引擎，Step 5 Agent 替代部分线下产品体验
- [[truman-perspective-skill]] — 两个 Skill 是不同品类：truman-perspective 是人格模拟型，use-tinyfish 是工具型（第三个品类，与 methodology 和 persona 并列）
- [[KDO Protocol]] — TinyFish 的 SKILL.md + CLI 架构验证了 KDO Protocol 的 External Intake Routing 规则中"已结构化 Skill 包 → 直接安装"路径

### Skill 类型体系（至此形成三个品类）

| 类型 | Skill | 特征 | 安装方式 |
|------|-------|------|---------|
| **methodology** | business-research | 方法论执行引擎，流程驱动 | 完整 SKILL.md + references/ + templates/ |
| **persona** | truman-perspective | 人格模拟器，角色扮演 | SKILL.md + references/research/（6 Agent 调研） |
| **tool** | use-tinyfish | 基础设施工具，CLI 驱动 | SKILL.md（pre-flight check + 命令速查） |

### 可迁移到 KDO 的改进

- Skill 类型枚举（methodology / persona / tool）应纳入 KDO Protocol 的 Schema 定义
- TinyFish 的 tinyskills recipe（自动生成 SKILL.md）可能是"研究并内化新技术"的加速器
- Pre-flight check 模式（`which tinyfish` + `tinyfish auth status`）可推广到其他 tool 型 Skill 的安装验证

## Open Questions

- TinyFish Agent 在中国网站（防火墙、反爬、验证码）上的表现如何？
- 500 免费步对 business-research 的一次完整调研（通常 250+ 次搜索）是否足够？
- TinyFish 的 SKILL.md 格式与 Anthropic 官方 Skill 规范的兼容性？
- tinyskills 自动生成的 SKILL.md 质量能否达到概念卡的深度标准？

## Output Opportunities

- **business-research + TinyFish 集成**：在 business-research 的 Step 3 中优先使用 TinyFish Search/Fetch
- **KDO Skill 类型系统**：在 `90_control/schemas/` 中新增 skill-type 枚举 Schema
- **TinyFish tinyskills 试用**：用 TinyFish 的 SKILL.md 生成器反向验证我们的概念卡质量
