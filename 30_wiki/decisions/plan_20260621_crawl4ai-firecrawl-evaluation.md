---
id: plan_20260621_crawl4ai-firecrawl-evaluation
title: Crawl4AI vs Firecrawl 选型评估——KDO 检索架构 Phase 2 爬虫引擎决策
type: decision
status: proposed
domain:
  - master
  - kdo
source_refs:
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
created_at: "2026-06-21"
author: 黄药师
reviewed_by: 欧阳锋
confidence: 0.85
trust_level: high
related:
  - "[[system-yitang-research-workflow]]"
  - "[[framework-yitang-research-quality-gate]]"
  - "[[tool-yitang-web-scraping-research]]"
---

# Crawl4AI vs Firecrawl 选型评估

> 狗粮测试：用调研域武器库跑完整调研工作流。黄药师 · 2026-06-21。

## 调研结论

**KDO 检索架构 Phase 2 应选 Crawl4AI 作为底层爬虫引擎。**

## 六维对比

| 维度 | Crawl4AI | Firecrawl | 胜出 |
|:--|:--|:--|:--|
| **许可** | MIT 完全开源 | AGPL-3.0（自托管缺Fire-engine） | Crawl4AI |
| **自部署** | `pip install` 分钟级 | Docker + PG + Redis，小时级 | Crawl4AI |
| **LLM集成** | 支持 Ollama 本地模型 | 云API付费 + AI Extract $89起 | Crawl4AI |
| **维护活跃度** | 80贡献者，v0.8.9（Jun 4） | 95k stars，v1.15 | 持平 |
| **成本（100K页）** | ~$70（EC2+代理） | ~$83/月（SaaS） | 持平 |
| **反爬能力** | 自建 Playwright+代理 | 云版Fire-engine强，自托管弱 | 云版Firecrawl |

## 决定性因素

1. **KDO 需要自托管**：检索架构在本地/WSL 跑，Firecrawl 自托管缺 Fire-engine（反爬）+ `/agent` 端点——等于买了半成品
2. **Crawl4AI 支持本地 LLM**：KDO 已有 Ollama，不需要为每次提取付 API 费用
3. **MIT vs AGPL**：AGPL 在内部使用没问题，但 MIT 更干净

## 风险

- Crawl4AI 仅 Python SDK（Firecrawl 多语言）——但 KDO 技术栈就是 Python
- 反爬需自建代理池——Phase 2 初期不需要，后续可加
- 保护站点成功率普遍低（Firecrawl 也才 33%），不构成选择差异

## 建议

Phase 2 选 Crawl4AI。如后续需要多语言 SDK 或零运维，可切换到 Firecrawl Cloud——两者 API 语义相似，迁移成本低。

---

*狗粮测试完成 · 调研工作流 7 步全跑通 · 六维门禁自检通过*
