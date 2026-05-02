---
title: "KDO Protocol Priority Checklist"
type: improvement-plan
status: draft
source_refs:
  - "src_20260503_protocol_design_session"
created_at: "2026-05-03"
updated_at: "2026-05-03"
related:
  - "[[KDO Protocol]]"
  - "[[KDO Protocol Implementation Roadmap]]"
tags:
  - #kdo
  - #priority
  - #checklist
trust_level: high
---

# KDO Protocol Priority Checklist

## P0 — 本周必须做（Blocking）

不做这些，系统不完整，AI 操作有失控风险。

| # | 任务 | 为什么 blocking | 预计时间 |
|---|------|----------------|----------|
| 1 | **补全 6 个 Schema**<br>`entity.yaml` `decision.yaml` `improvement.yaml`<br>`artifact-content.yaml` `artifact-code.yaml` `source.yaml` | AI 现在写非 concept 页面时没有校验标准，frontmatter 格式会混乱 | 2h |
| 2 | **给 `诊所O2O` 补 `source_refs`** | 当前唯一一个 orphan + 无源的页面，拉低整个知识层可信度 | 15min |
| 3 | **把 `routing-rules.md` 从散文改成决策矩阵** | AI 现在读的是"建议"，不是"路由表"，任务分发仍靠猜 | 1.5h |

---

## P1 — 下周做（高杠杆）

做了这些，AI 操作体验从"勉强可用"跃升到"流畅"。

| # | 任务 | 为什么高杠杆 | 预计时间 |
|---|------|------------|----------|
| 4 | **创建 `CONTEXT.md`**<br>每次会话开始时自动生成：当前活跃议题、最近新增、未解决矛盾、待 review 页面 | AI 不用每次都重读整本说明书，直接加载上下文快照 | 1h |
| 5 | **创建 `30_wiki/concepts/graph-rag.md`** | 一堂课程的核心洞察，KDO 知识层目前缺这张图 | 1.5h |
| 6 | **Backfill 遗留卡片的 `trust_level` + `reviewed_by`**<br>（互联网医院、街顺、鑫港湾、YC） | 让统计仪表盘从"有洞"变成"可信" | 30min |

---

## P2 — 月内做（战略级）

做了这些，KDO 从"个人笔记系统"变成"真正的 AI-Native 知识操作系统"。

| # | 任务 | 为什么战略级 | 预计时间 |
|---|------|------------|----------|
| 7 | **Graph RAG 索引层**<br>把 `[[双向链接]]` 解析成显式图结构（JSON/GraphML），让 AI 能做关系推理 | 一堂正在做的事；没有它，AI 对知识网络的理解永远停留在文本层面 | 4-6h |
| 8 | **自动化校验钩子**<br>`kdo lint` 命令或 Obsidian 保存时钩子，自动检查 frontmatter 是否符合 Schema | Schema 从"纸面标准"变成"强制执行"，这是 Protocol 从宣言到制度的关键一跃 | 3-4h |
| 9 | **跨工具桥接协议**<br>定义从飞书/网页/Notion 流入 KDO 的标准格式（`kdo ingest` 的输入契约） | 解决"捕获层到知识层"的 friction，让外部输入自动归位 | 2h |

---

## P3 — 季度完善（基础设施）

| # | 任务 | 说明 |
|---|------|------|
| 10 | **多端同步协议固化**<br>把 `.gitignore` + Obsidian Git 配置写成 `30_wiki/systems/obsidian-git-sync-protocol.md` | 防止新设备加入时再次踩坑 |
| 11 | **Agent 沙箱测试**<br>给每个 Agent 角色（研究员/图书管理员/仲裁者）写评测用例 | 类似单元测试，验证 Agent 在边界条件下是否遵守 Protocol |
| 12 | **质量门自动化**<br>把 `PROTOCOL.md` Section 6 的检查清单变成可执行的 `kdo validate` 子命令 | Produce/Ship 前自动跑检查，不通过就阻断 |

---

## 执行顺序（建议）

```
本周：1 → 2 → 3
下周：4 → 5 → 6
月内：7 → 8 → 9
季度：10 → 11 → 12
```

**核心原则**：先让系统"不出错"（P0），再让系统"跑得快"（P1），最后让系统"有壁垒"（P2+P3）。

---

## 验收标准（全部完成后）

- [ ] 任意 AI Agent 进入仓库，读 `CONTEXT.md` + `PROTOCOL.md` 两页即可开始操作
- [ ] 所有 `30_wiki/` 页面通过对应 Schema 校验，0 orphan，0 missing source
- [ ] `kdo lint` 能自动发现 frontmatter 错误和孤立页面
- [ ] AI 能回答"和 X 概念相关的所有知识"而不用逐页搜索（Graph RAG）
- [ ] 新设备加入时，按同步协议文档操作即可零冲突接入
