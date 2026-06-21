---
id: "task_20260621_digest卡更新"
type: "task"
created_at: 2026-06-21
author: "王语嫣 · 综合欧阳锋审查结论"
executor: "老顽童"
---

# 域索引入口卡更新：yitang-research-domain-digest

## 当前状态

`30_wiki/domains/yitang-research-domain-digest.md` 由黄药师建骨架，但：
- 标题写"60张卡"——实际已 90+
- 待产区全标 ⏳——30 张已完成卡未更新
- 工具索引缺 30 张新卡入口
- 缺域间桥接

## 任务：更新 digest 卡（1 项，预计 30 分钟）

### 1. 更新"待产"区状态

**位置**：L164-172  
**操作**：所有 Wave 1-5 的 ⏳ 改为 ✅，补充实际产出路径

```markdown
### 🆕 武器库盲区补充（全部完成 ✅）

| Wave | 数量 | 内容 | 状态 |
|:--|:--|:--|:--|
| Wave 1 | 6 张 | OSINT 工具链（overview/Maltego/SpiderFoot/Shodan/Sherlock/Wayback） | ✅ 已入库 `30_wiki/tools/tool-osint-*.md` |
| Wave 2 | 5 张 | Agent 原生工具（overview/Firecrawl/Crawl4AI）+ MCP协议 | ✅ 已入库 `30_wiki/tools/tool-agent-*.md` + `concepts/concept-mcp-protocol.md` |
| Wave 3a | 2 张 | 替代数据（overview/免费替代数据） | ✅ 已入库 `30_wiki/tools/tool-alt-data-*.md` |
| Wave 3b | 2 张 | 高级搜索（Google Dorking/DNS情报） | ✅ 已入库 `30_wiki/tools/tool-google-dorking.md` + `tool-dns-intelligence.md` |
| Wave 3c | 3 张 | 媒体验证（overview/反向图片/元数据提取） | ✅ 已入库 `30_wiki/tools/tool-media-verification-*.md` + `tool-reverse-image-search.md` + `tool-metadata-extraction.md` |
| Wave 4 | 交叉链接 | 武器库 + 18策略 + 四类调研补链 | ✅ 已完成 |
| **Wave 5** 🆕 | **12 张** | **CI框架(3) + SATs工具包(5) + 多智能体架构(4)** | ✅ 已入库 |
```

### 2. 工具索引新增 30 张卡

在已有的"情报获取""分析与验证""实战执行"后，新增以下分组：

```markdown
### 🆕 OSINT 开源情报工具

| 场景 | 用这张卡 |
|:--|:--|
| OSINT 工具总览与选择 | `tool-osint-overview` |
| 画竞对/供应链关联网络 | `tool-osint-maltego` |
| 一键自动扫描 200+ 数据源 | `tool-osint-spiderfoot` |
| 搜索全球联网设备 | `tool-osint-shodan` |
| 跨 300+ 平台追踪用户名 | `tool-osint-sherlock` |
| 看竞对 5 年前的官网 | `tool-osint-wayback` |

### 🆕 Agent 原生调研

| 场景 | 用这张卡 |
|:--|:--|
| Agent 原生工具选型 | `tool-agent-native-overview` |
| URL → 结构化 Markdown | `tool-agent-firecrawl` |
| 开源 LLM 友好爬虫 | `tool-agent-crawl4ai` |
| Agent 调用外部工具标准 | `concept-mcp-protocol` |

### 🆕 替代数据

| 场景 | 用这张卡 |
|:--|:--|
| 替代数据分级与 ROI 评估 | `tool-alt-data-overview` |
| 零成本：Google Trends/Reddit/Glassdoor | `tool-alt-data-free` |

### 🆕 高级搜索

| 场景 | 用这张卡 |
|:--|:--|
| Google Dorking 九个操作符 | `tool-google-dorking` |
| WHOIS/DNS/SSL 域名情报 | `tool-dns-intelligence` |

### 🆕 媒体验证

| 场景 | 用这张卡 |
|:--|:--|
| 媒体验证总览 | `tool-media-verification-overview` |
| 反向图片搜索四引擎 | `tool-reverse-image-search` |
| 照片 GPS/时间/天气验证 | `tool-metadata-extraction` |

### 🆕 CI 竞争情报系统框架

| 场景 | 用这张卡 |
|:--|:--|
| CI 系统设计（Define→Gather→Analyze→Implement） | `framework-ci-operating-model` |
| 决策驱动的提问定义（KITs/KIQs） | `tool-ci-define-phase` |
| 洞察嵌入运营节奏（battlecard/forecast/QBR） | `tool-ci-implement-phase` |

### 🆕 结构化分析技术（SATs）

| 场景 | 用这张卡 |
|:--|:--|
| SATs 八类工具箱总览 | `framework-structured-analytic-techniques` |
| 审计隐藏假设 | `tool-key-assumptions-check` |
| 主动攻击自己的结论 | `tool-devils-advocacy` |
| 模拟竞对最优策略 | `tool-red-team-analysis` |
| 设置假设重新评估的触发信号 | `tool-indicators-signposts` |

### 🆕 多智能体调研架构

| 场景 | 用这张卡 |
|:--|:--|
| 四种模式对比与选择 | `framework-multi-agent-research-architecture` |
| Supervisor：一主多 Worker | `tool-agent-research-supervisor` |
| Swarm：多 Agent 自发协同 ⚠️2026中快速演化 | `tool-agent-research-swarm` |
| Pipeline：OSCAR 五步法的 Agent 实现 | `tool-agent-research-pipeline` |
```

### 3. 更新标题卡数

**位置**：L3  
**操作**：`60张卡` → 搜索全量调研域卡，更新为准确数字（预计 90+）

### 4. 新增域间桥接

在文末补充：

```markdown
## 域间桥接

- **→ 五步法域**：调研是五步法第二步"产品内核"的前置——先用调研验证需求假设，再进入产品设计
- **→ 单元模型域**：替代数据 + 逆向数据分析可反推竞对单元模型
- **→ 精益测试域**：SATs 的 Key Assumptions Check 是精益假设验证的分析层升级
- **→ ToB 域**：ToB 调研手段卡是通用武器库的行业深化
```

---

## 参考模板

`30_wiki/domains/five-step-domain-digest.md` — 黄药师已审过的 digest 格式，参考其结构。

---

*王语嫣综合欧阳锋审查结论 | 2026-06-21 | 此项完成后调研域建制完整收工*
