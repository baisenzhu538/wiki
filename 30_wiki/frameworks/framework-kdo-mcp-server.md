---
id: framework-kdo-mcp-server
title: KDO MCP Server — 知识库能力的外部协议暴露层
type: framework
status: draft
confidence: 0.88
trust_level: high
domain:
- kdo
- ai-collaboration
author: 黄药师
created_at: '2026-07-26'
updated_at: '2026-07-26'
quality_labels:
- actionable
- principle
source_refs:
- 30_wiki/concepts/concept-mcp-protocol.md
- 90_control/domain-routes.yaml
- kdo-tools/mcp/server.py
- kdo-tools/mcp/tools.py
related:
- framework-kdo-modeling-methodology
- framework-kdo-retrieval-architecture-v2
- concept-mcp-protocol
- agent-spec-duanwangye-publisher
- agent-spec-hongqigong-multimodal
tags:
- audience:ceo
- scene:diagnosis
- skill-level:advanced
---

# KDO MCP Server — 知识库能力的外部协议暴露层

> **一句话**：KDO MCP Server 是 KDO 知识工厂编译链的最终产物——把 framework → tool → skill → workflow → agent-spec 的完整能力栈，通过 MCP 标准协议暴露给任何外部 Agent。

---

## 一、核心主张

KDO 工厂的能力栈已经建成（242 frameworks + 105 skills + 10 workflows + 6 agent-specs），但只有进入 wiki 目录、知道 `kdo query` 和 `cap_hub list` 的 Agent 才能调用。MCP Server 是**协议层**——把内部能力翻译为标准 MCP Tool，让飞书 Agent、Codex、Claude Desktop、Web 应用等任何 MCP 客户端都能直接使用。

**这不是又建一个工具——是把已有能力的最后一个编译步骤补上。**

---

## 二、在 KDO 编译链中的位置

```
framework-kdo-modeling-methodology (方法论总纲)
  → framework-kdo-retrieval-architecture-v2 (检索架构)
    → tool: domain-routes.yaml
    → tool: RRF fusion in delivery.py
  → framework-kdo-mcp-server (本卡 — 协议暴露)
    → tool: kdo-tools/mcp/server.py    ← MCP Server
    → tool: kdo-tools/mcp/tools.py     ← 4 个 Tool Handler
    → config: kdo-tools/mcp/config.yaml ← 客户端注册
```

Truman 的解压展开：1 个 framework → ≥3 个解压资产（tool + config + case）。MCP Server 是 `framework-kdo-modeling-methodology` 的最外层解压产物——从方法论到可调用协议的完整编译链闭合。

---

## 三、架构：4 个 Tool = 4 个 Feature

遵循 Truman 的 Feature 思维——每个 Tool 是一个最小可操作能力单元，可独立调用、跨工具迁移：

| MCP Tool | Feature | 已有能力复用 | 跨工具可迁移？ |
|:--|:--|:--|:--:|
| **kdo_search** | RRF 融合检索 | delivery.py cmd_query | ✅ 任何 RAG 系统 |
| **kdo_onboard** | MOC 绝对优先 + 域路由 | domain-routes.yaml | ✅ 任何知识库 |
| **kdo_read** | 卡片 ID → 完整内容 | safe_read() | ⚠️ KDO 卡片格式 |
| **kdo_capabilities** | 能力注册表发现 | cap_hub/registry.py | ✅ 任何插件系统 |

### 调用流程

```
外部 Agent
  → kdo_capabilities()          # "这里有什么？"
  → kdo_onboard("销售管理")      # "给我销售管理的全貌"
    ← framework + tools + cases + reading_order
  → kdo_search("客户分层 方法")  # "有没有具体方法？"
    ← [{id, title, type, snippet}]
  → kdo_read("tool-yitang-customer-segmentation-4step")  # "完整内容是什么？"
    ← {frontmatter, body}
```

---

## 四、与各 Agent 的关系

| Agent | 调用场景 | 常用 Tool |
|:--|:--|:--|
| **飞书老顽童** | 接到新域任务，先了解全貌 | `kdo_onboard` → `kdo_read` |
| **飞书王语嫣** | 用户问"XX域有什么" | `kdo_search` → `kdo_read` |
| **飞书段王爷** | 发布前需要某张卡的完整内容 | `kdo_read` |
| **飞书洪七公** | 需要了解素材域的卡片结构 | `kdo_onboard` |
| **Codex 新 Agent** | 刚接入 KDO，不知道有什么 | `kdo_capabilities` |
| **外部 MCP 客户端** | 任何需要 KDO 知识的场景 | 全部 4 个 Tool |

---

## 五、技术实现

- **Transport**: stdio（本地 Agent）+ SSE（远程 Agent）
- **SDK**: FastMCP（`mcp.server.fastmcp`）
- **依赖**: `mcp>=1.0.0`（和 OpenMontage-zh-MCP 同栈）
- **零额外依赖**: 检索、读卡、能力发现全部复用 KDO 现有代码

### 客户端注册（claude_desktop_config.json）

```json
{
  "mcpServers": {
    "kdo": {
      "command": "python",
      "args": ["kdo-tools/mcp/server.py"],
      "cwd": "C:\\Users\\Administrator\\Desktop\\wiki",
      "env": {
        "WIKI_ROOT": "C:\\Users\\Administrator\\Desktop\\wiki",
        "KDO_SRC": "C:\\Users\\Administrator\\Knowledge Delivery OS 0.0.1"
      }
    }
  }
}
```

---

## 六、Critique

### 内部局限

1. **依赖 kdo query 管线**: `kdo_search` 的 RRF 融合依赖 Graph RAG 索引和 BM25 索引都存在且新鲜。索引过期时，检索质量下降。
2. **kdo_onboard 的域发现基于关键词匹配**: 如果 `domain-routes.yaml` 没有覆盖某个域，`onboard` 无法引导。新域上线时必须同步更新 routes 配置。
3. **stdio transport 只支持本地 Agent**: 远程 Agent 需要 SSE transport，增加了部署复杂度。
4. **无鉴权**: 当前版本假设调用者在可信环境中。多租户场景需要加 API Key 验证。

### 外部攻击

**[Closed-System Advocate]**
> "MCP 把知识库暴露给外部 Agent，等于让没有 KDO 训练背景的 Agent 直接调核心能力。这些 Agent 不懂 KDO 的卡片设计标准、不知道 trust_level 的含义——它们会误用检索结果。"

**回应**: 这正是 `kdo_onboard` 存在的理由——它不只是返回卡片列表，还返回 reading_order。外部 Agent 不需要知道 KDO 内部标准——onboard 已经帮它编排好了。误导风险由检索质量决定（RRF + MOC 优先），而非协议本身。

---

## 七、Action Triggers

| 触发条件 | 动作 |
|:--|:--|
| 新 Agent 接入 KDO | 先调 `kdo_capabilities` → `kdo_onboard("<域>")` |
| Agent 需要回答域知识问题 | 先调 `kdo_search` → 找到 framework 卡 ID → `kdo_read` 完整内容 |
| 新域上线 | 更新 `domain-routes.yaml` → `kdo_onboard` 自动能发现 |
| MCP Server 无响应 | 检查 `WIKI_ROOT` 和 `KDO_SRC` 环境变量是否正确 |

---

## 八、解压路径

| # | 类型 | 路径 | 状态 |
|:--|:--|:--|:--:|
| 1 | **tool** | `kdo-tools/mcp/server.py` | ✅ 本次同步构建 |
| 2 | **tool** | `kdo-tools/mcp/tools.py` | ✅ 本次同步构建 |
| 3 | **config** | `kdo-tools/mcp/config.yaml` | ✅ 本次同步构建 |
| 4 | **case** | (收集 MCP 调用案例) | 🔴 待收集 |
