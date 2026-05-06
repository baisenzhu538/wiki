---
title: TinyFish 深度评估报告
type: assessment
status: reviewed
source_refs:
  - https://tinyfish.ai
  - https://github.com/tinyfish-io/tinyfish-cookbook
  - https://github.com/tinyfish-io/agentql
created_at: 2026-05-06
updated_at: 2026-05-06
---

# TinyFish 深度评估报告

## 1. 公司定位与核心认知

**TinyFish** 是 YC 背景的 AI Web Agent 基础设施公司，双品牌策略：
- **TinyFish**（tinyfish.ai）→ 企业级 Web Agent 平台，面向 B 端客户（Google、DoorDash、Amazon 等）
- **AgentQL**（agentql.com）→ 开源开发者品牌，GitHub 1.3k+ stars，社区驱动

> **核心一句话**：把任意网站变成结构化 API 的基础设施。给 URL + 自然语言目标，拿回干净 JSON。

### [Critique]
- **前提假设**：目标网站可被浏览器渲染（对纯 API 型服务无用）
- **边界**：反 bot 能力不是 100%，官网自称 85% pass rate
- **可靠性**：⚠️ 中 — 公司成立时间较短，长期存活不确定，但 YC 背书 + 客户名单降低风险

---

## 2. 技术能力矩阵（四大 API）

| API | 功能 | 计费 | 速度 | 最佳场景 |
|-----|------|------|------|----------|
| **Search** | 实时网页搜索，返回结构化 JSON，不缓存 | **免费**（所有计划） | <1s | 快速情报发现、素材收集 |
| **Fetch** | 渲染页面后返回干净 Markdown/JSON/HTML | **免费**（所有计划） | 几秒 | 网页内容清洗、喂给 LLM/RAG |
| **Agent** | 自动导航、填表、登录、多步操作，返回 JSON | 1 credit/step | 10s~分钟 | 竞品监控、价格抓取、复杂表单 |
| **Browser** | 托管云浏览器（Playwright/Selenium） | 1 credit/4分钟 | 实时 | 自定义脚本、深度反爬 |

### 关键技术指标
- Mind2Web 准确率：**89.9%**（公开 benchmark 最高）
- 浏览器冷启动：**<250ms**
- 反 bot 通过率：**85%**
- 检测覆盖率：**99.3%**
- 平均 Agent 工作流：**19 steps**

### [Critique]
- Search/Fetch 免费是大优势，可低成本做大量实验
- Agent 按 step 计费，复杂任务（如翻页+提取+对比）可能消耗 50+ credits
- 失败 run 不扣费，降低了试错成本

---

## 3. 定价分析

| 计划 | 月费 | Credits | Search限速 | Fetch限速 | Agent并发 |
|------|------|---------|-----------|-----------|----------|
| **Free** | $0 | 500（一次性） | 5 req/min | 25 url/min | 2 |
| **PAYG** | $0 | $0.015/credit | 5/25 | 5/25 | 2 |
| **Starter** | $15 | 1,650/月 | 20/100 | 20/100 | 10 |
| **Pro** | $150 | 16,500/月 | 50/250 | 50/250 | 50 |

### 成本测算（KDO 场景）

| 场景 | 预估消耗 | Free 计划 | Starter 月费 |
|------|---------|----------|-------------|
| 素材收集（Fetch 50 篇网页）| 0 credits | ✅ 够用 | 不需要 |
| 竞品价格监控（Agent，10 个站点）| ~200 credits | ⚠️ 2-3 次 | ✅ 充足 |
| 深度调研（Agent 翻页+提取，20 个源）| ~500 credits | ❌ 不够 | ✅ 够用 |

> **结论**：Fetch/Search 阶段完全免费，Agent 阶段需要付费。Free 的 500 credits 足够做一轮完整评估测试。

---

## 4. 与 KDO 流水线的对接评估

### 4.1 可直接对接的环节

```
KDO 流水线                    TinyFish 补位
─────────────────────────────────────────────────
capture (URL/链接)     →     Search API 增强发现能力
ingest (raw→wiki骨架)  →     Fetch API 替代现有网页抓取
                              （更干净、反爬更强）
enrich (充实wiki)      →     Agent API 自动提取结构化数据
produce (生成artifact) →     Cookbook recipe 参考
```

### 4.2 具体场景映射

| KDO 需求 | TinyFish 方案 | 优先级 |
|----------|--------------|--------|
| 批量抓取文章素材 | Fetch API（免费，25/min） | ⭐ 高 |
| 竞品价格/功能监控 | Agent API + 定时 cron | ⭐ 高 |
| 实时情报发现 | Search API（免费） | ⭐ 中 |
| 登录态数据抓取 | Browser API + Session 复用 | ⭐ 中 |
| 自动化内容生成 | Agent API 提取 → KDO produce | ⭐ 低 |

### 4.3 接入方案设计

**方案 A：轻量接入（推荐先试点）**
- 仅使用 **Fetch API** 替换 KDO 现有的 `fetch-url` 能力
- 优势：零成本、反爬更强、输出更干净（Markdown 结构化）
- 触发方式：`kdo fetch-url <url> --engine tinyfish`

**方案 B：深度接入**
- Agent API 作为 KDO connector 插件
- 新增 `kdo connector tinyfish --kind agent`
- 在 enrich 阶段自动调用 Agent 提取结构化数据

### [Critique]
- KDO 设计哲学是"零运行时依赖"，接入外部 SaaS 是架构偏离
- 但 Fetch/Search 免费 + API 简单，可作为可选增强而非核心依赖
- 建议以 connector 形式接入，保持核心 KDO 的独立性

---

## 5. Cookbook 架构分析与可迁移模板

### 5.1 Cookbook 组织方式

TinyFish cookbook 采用 **"Recipe + Live Demo + Source Code"** 三层结构：

```
tinyfish-cookbook/
├── viet-bike-scout/          ← Recipe 目录（独立项目）
│   ├── README.md             ← 项目说明 + Live Demo 链接
│   ├── app/                  ← 前端应用代码
│   ├── api/                  ← 后端 API（调用 TinyFish）
│   └── package.json
├── tutor-finder/
├── openbox-deals/
├── tinyskills/               ← 特色：自动生成 SKILL.md
├── N8N_WorkFlows/            ← n8n 集成模板
└── README.md                 ← 总目录 + 快速开始
```

### 5.2 Recipe 标准化结构（可迁移）

每个 Recipe 包含：
1. **问题定义**（一句话描述解决什么问题）
2. **解决方案**（用 TinyFish 哪个 API，什么策略）
3. **Live Demo**（Vercel 部署的可交互演示）
4. **源代码**（完整可运行的项目）
5. **架构图**（数据流：输入 → TinyFish → 输出）

### 5.3 对 KDO `40_outputs/capabilities/` 的启发

当前 KDO 的 capability 结构：
```
40_outputs/capabilities/
├── skills/
│   └── knowledge-curator/SKILL.md
├── workflows/
│   └── daily-capture-flow.md
└── agents/
```

**建议迁移模板**：
```
40_outputs/capabilities/
├── skills/
│   ├── knowledge-curator/
│   └── web-research-agent/      ← 新增（参考 tinyskills）
├── workflows/
│   ├── daily-capture-flow/
│   └── competitor-monitor-flow/  ← 新增（参考 competitor-analysis recipe）
└── playbooks/
    └── pricing-intelligence/     ← 新增（参考 openbox-deals）
```

每个 playbook 包含：
- `README.md`：问题 + 方案 + 输入输出示例
- `script.py`：可运行的脚本
- `demo.md`：效果展示（截图或录屏）
- `integration.md`：如何接入 KDO 流水线

---

## 6. 关键 Recipe 对咱们的价值

| Recipe | 核心价值 | 迁移可能性 |
|--------|---------|-----------|
| **tinyskills** | 自动抓文档/GitHub/博客生成 SKILL.md | ⭐⭐⭐ 高 — 直接对应 KDO skill 生产 |
| **competitor-analysis** | 实时竞品价格/功能情报 | ⭐⭐⭐ 高 — 文章生产线素材来源 |
| **competitor-scout-cli** | NL CLI 研究竞品决策 | ⭐⭐ 中 — 可改成 KDO query 扩展 |
| **research-sentry** | 语音优先研究助手（ArXiv/PubMed） | ⭐⭐ 中 — 可改成中文源版本 |
| **openbox-deals** | 多站点并行价格聚合 | ⭐⭐ 中 — 参考架构设计 |
| **code-reference-finder** | GitHub/SO 代码片段分析 | ⭐⭐ 中 — 技术文章素材 |

---

## 7. 行动建议（老板决策点）

### 立即可以做（零成本）
1. ✅ 注册 Free 计划，拿 500 credits 做一轮测试
2. ✅ 用 Fetch API 抓 10 个咱们关注的网页，对比 KDO `fetch-url` 效果
3. ✅ 用 Search API 做一轮实时情报搜索，评估质量

### 需要评估后决定
4. ❓ 是否将 Fetch API 作为 KDO `fetch-url` 的可选引擎？
   - 成本：零（免费）
   - 收益：反爬更强、输出更结构化
   - 风险：增加外部依赖

5. ❓ 是否开发 TinyFish connector 插件？
   - 成本：约 1-2 天开发
   - 收益：enrich 阶段自动提取结构化数据
   - 风险：架构耦合

6. ❓ 是否复刻 tinyskills recipe 到 KDO？
   - 成本：约 2-3 天
   - 收益：自动化生成 skill，减少黄药师手工工作量
   - 风险：需要维护 prompt 模板

### 不建议做
- ❌ 深度依赖 Agent API 作为核心能力（按 step 计费，成本高且不可控）
- ❌ 用 Browser API 做大规模采集（4分钟/credit，贵）

---

## 8. 相关链接

- 官网：https://tinyfish.ai
- Cookbook：https://github.com/tinyfish-io/tinyfish-cookbook
- AgentQL：https://github.com/tinyfish-io/agentql
- MCP Server：https://github.com/tinyfish-io/agentql-mcp
- 定价页：https://www.tinyfish.ai/pricing

---

*报告完成。下一步：等老板拍板是否注册测试，或是否有其他方向要深入。*
