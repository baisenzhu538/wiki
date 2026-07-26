---
id: framework-yitang-research-weapon-supplement-2026
title: 调研武器库补充：2025-2026年新武器——OSINT工具+Agent原生+替代数据+验证技术
type: framework
status: draft
author: 老顽童
reviewed_by: 待审
review_date: 2026-06-21
created_at: 2026-06-21
confidence: 0.88
trust_level: high
language: zh-CN
domain:
- yitang
- research
source_refs:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
related:
- '[[tool-alt-data-free]]'
- '[[tool-agent-native-overview]]'
- '[[tool-osint-overview]]'
- '[[tool-yitang-web-scraping-research]]'
- '[[web-scraping-三剑客-scrapling-crawl4ai-firecrawl]]'
- '[[framework-yitang-research-weapon-system]]'
- '[[tool-yitang-ai-research-workflow]]'
- '[[tool-yitang-database-index]]'
- '[[framework-yitang-nine-layer-deep-dig]]'
- yt-model-agent-architecture
- proposal-ai-domain-mastery-pipeline
updated_at: '2026-06-29'
tags:
- audience:ceo
- scene:diagnosis
- skill-level:advanced
---
# 调研武器库补充：2025-2026年新武器

> 一堂武器库以人工执行为主。2025-2026年涌现了大量Agent原生工具、OSINT自动化框架、替代数据源——这些都是我们原本不知道的武器。本卡做系统性补充。

---

## 一、OSINT工具矩阵（一堂武器库未覆盖）

OSINT（Open Source Intelligence）是情报界的"调研方法论"——专业机构几十年的积累，远超商业调研的视野。

### 核心OSINT工具清单

| 工具 | 用途 | 为什么强大 | 免费/付费 |
|:---|:---|:---|:---:|
| **Maltego** | 实体关系图谱分析 | 输入一个域名/人名/公司名，自动绘制关联网络——谁认识谁、谁控股谁、谁和谁打过官司 | 付费 |
| **SpiderFoot** | 自动化OSINT扫描 | 输入目标，自动跑200+数据源的扫描——IP/域名/邮箱/社交账号全关联 | 开源免费 |
| **theHarvester** | 邮箱/域名/子域名收集 | 被动收集目标公司的邮箱地址、子域名、员工姓名——不需要和目标交互 | 开源免费 |
| **Shodan** | 互联网设备搜索引擎 | 搜索全球联网设备——服务器、摄像头、工业控制系统。竞对用什么技术栈？暴露了什么设备？ | 免费+付费 |
| **Sherlock** | 用户名跨平台搜索 | 输入一个用户名，自动搜索300+社交平台——找到一个人的所有社交账号 | 开源免费 |
| **Wayback Machine** | 网页历史快照 | 看竞对官网的历史版本——什么时候改了定位？什么时候删了产品？什么时候换了团队介绍？ | 免费 |
| **ExifTool** | 文件元数据提取 | 从图片/PDF/Office文件中提取隐藏的元数据——拍摄时间、GPS坐标、作者信息 | 开源免费 |
| **Have I Been Pwned** | 数据泄露查询 | 查询某公司的邮箱域名是否出现在数据泄露事件中——暴露了哪些信息？ | 免费 |

### OSINT框架

[OSINT Framework](https://osintframework.com) 是一个元工具——按类别整理了几百个OSINT工具和技巧的导航。不需要记住所有工具，需要的时候上去按类别找。

---

## 二、Agent原生调研武器（2025-2026新范式）

这是最大的缺口。一堂武器库完全以"人手动执行"为前提设计。2025-2026年出现了大量为AI Agent设计的工具。

### 2.1 AI驱动的Web抓取

| 工具 | 关键能力 | 对Agent的意义 |
|:---|:---|:---|
| **Firecrawl** | 输入URL，输出干净Markdown。支持递归爬取整站、schema化JSON提取、MCP协议 | Agent可以像人一样"打开网页→阅读→提取信息" |
| **Crawl4AI** | 开源AI爬虫，支持自然语言描述提取需求 | "提取这个页面所有的产品名称和价格"——不需要写选择器 |
| **ScrapeGraphAI** | 用LLM理解网页结构，自动适应页面变化 | 网页改版不影集爬取——AI自己理解新结构 |
| **Apify** | 预建爬虫市场+MCP兼容 | 不需要写爬虫代码，直接用现成的 |

### 2.2 Agent搜索API

| 工具 | 关键能力 |
|:---|:---|
| **Parallel.ai** | 专为AI Agent设计的深度搜索API，支持多轮迭代搜索 |
| **Exa.ai** | 语义搜索而非关键词搜索——搜"快速增长的小众消费品类"能理解意图 |
| **Tavily** | 专为AI Agent优化的搜索API，返回结构化结果+来源标注 |

### 2.3 MCP协议（Model Context Protocol）

2025年出现的新标准。MCP让AI Agent可以直接调用外部工具而无需人工配置。Firecrawl、Apify、Bright Data等已支持MCP——Agent说"帮我搜一下竞对的招聘信息"，底层自动调用Scraper→提取→返回结构化数据。

**一堂武器库的调研手段，未来都可以封装为MCP工具**——Agent不再需要"人手动执行"，而是"Agent自主执行调研武器库中的策略"。

### 2.4 免费API替代爬虫

80%的公开数据其实有API，不需要爬虫：

| 平台 | API | 能获取什么 |
|:---|:---|:---|
| **Reddit** | `.json` 后缀 | 任何帖子/评论的结构化数据 |
| **YouTube** | Innertube API | 视频元数据、字幕（无需API Key） |
| **GitHub** | REST API | 仓库信息、提交历史、Star趋势（60req/hr免费） |
| **Wikipedia** | REST API | 任何词条的全文和元数据（200req/sec） |
| **300+更多** | [awesome-free-apis-2026](https://github.com/spinov001-art/awesome-free-apis-2026) | 覆盖几乎所有主流平台 |

---

## 三、替代数据源（Hedge Fund级别武器）

对冲基金每年花28亿美元购买替代数据——这些数据源远超传统调研的视野。

| 数据类型 | 具体来源 | 能发现什么 | 一堂武器库是否有 |
|:---|:---|:---|:---:|
| **卫星图像** | Planet Labs, Maxar | 追踪零售停车场车流量→预测同店销售；追踪工厂卡车进出→预测出货量；追踪建筑工地进度→预测房地产供应 | ❌ 无 |
| **信用卡交易数据** | Second Measure, Earnest | 竞对的真实销售额（非财报数字）、客单价变化、复购率 | ❌ 无 |
| **App使用数据** | data.ai, Sensor Tower | 竞对App的DAU/MAU、使用时长、用户留存 | ❌ 无 |
| **招聘数据** | Revelio Labs, LinkUp | 按部门/地区的招聘趋势、薪资变化、离职率→预判竞对战略方向 | ⚠️ 有基础版 |
| **供应链/物流数据** | Panjiva, ImportGenius | 竞对的进口量/出货量→从海关提单反推真实业务规模 | ⚠️ 部分 |
| **社交媒体情感** | Talkwalker, Brandwatch | 品牌情感趋势、危机预警、竞品对比 | ⚠️ 有基础版 |
| **地缘位置数据** | SafeGraph, Advan | 消费者线下行为——去了哪里、停留多久、频率 | ❌ 无 |
| **NLP财报脚注挖掘** | 自建或付费 | 大多数人只看财报正文，脚注里往往藏着最重要但被刻意隐藏的信息 | ❌ 无 |

### Hedge Fund替代数据的核心原则

1. **数据不是越贵越好——越"不可替代"越好。** 如果一份数据只有你买了，信息差就存在。如果大家都买了，就没有信息优势。
2. **替代数据的价值在"交叉验证"，不是"替代传统数据"。** 信用卡交易数据+卫星图像+Sensor Tower+财报=四面验证同一家公司的真实表现。
3. **小团队也能用**：Google Trends（免费）、Reddit讨论分析（免费）、Glassdoor员工评价（免费）——这些是"穷人版的替代数据"。

---

## 四、高级搜索与验证技术

### 4.1 Google Dorking（高级搜索语法）

| 语法 | 作用 | 示例 |
|:---|:---|:---|
| `site:` | 限定网站 | `site:competitor.com confidential` |
| `filetype:` | 限定文件类型 | `filetype:pdf "internal" site:competitor.com` |
| `intitle:` | 限定标题 | `intitle:"salary" site:competitor.com` |
| `inurl:` | 限定URL | `inurl:admin site:competitor.com` |
| `-` | 排除 | `company name -official -press` |
| `before:` / `after:` | 限定时间 | `after:2025-01-01 company news` |

### 4.2 域名/DNS/SSL情报

- src_unknown
- src_unknown
- src_unknown

### 4.3 媒体验证技术（来自OSINT的最佳实践）

| 技术 | 用途 |
|:---|:---|
| **反向图片搜索** | 竞对用的图是真的还是偷的/买的？这张图最早出现在哪里？ |
| **元数据分析** | 竞对发的照片是什么时候拍的？在哪里拍的？用什么设备拍的？ |
| **天气/阴影/太阳位置验证** | 竞对声称"在某日某地拍摄"的视频，天气和阴影与当时实际情况吻合吗？ |
| **Chronolocation** | 通过视频/照片中出现的时间线索（钟表、手机时间、电视节目）定位拍摄时间 |

---

## 五、对Agent的关键建议

### Agent使用调研武器库的最佳范式

```
传统模式（人）：想问题 → 选工具 → 手动执行 → 分析
Agent模式：   想问题 → 自主选择武器库策略 → 自主调用API/MCP工具 → 自主交叉验证 → 输出
```

**核心转变**：Agent不应该只是"帮人执行调研"，而应该"自主运行整套调研方法论"。

### 建议武器库升级方向

1. **每个工具卡增加Agent执行指令**：不只写"人怎么做"，同时写"Agent怎么调用对应的API/MCP工具"
2. **建立Agent调研决策树**：Agent接到调研任务→自动匹配武器库策略→自动选择工具→自动执行→自动交叉验证
3. **封装为MCP Server**：将整套武器库封装为MCP Server，让任何MCP兼容的Agent都能直接调用

---

## Constraints & Boundaries

- src_unknown
- src_unknown
- src_unknown
- src_unknown

---

*卡片类型：framework | 置信度：0.88 | 审核状态：待审*
