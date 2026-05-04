---
title: "KDO 产品 Backlog"
type: "product"
status: "draft"
created_at: "2026-05-03"
source: "EC工业化规范手册 附录D — EC卡清单方法论"
---

# KDO 产品 Backlog

> 每一个待处理项对应一条需求。状态流转：`排队` → `进行中` → `已完成` → `已交付`。
> 更新规则：每完成一项，更新状态和完成日期。每新增一项，追加到对应优先级区块。

---

## 已完成

| 编号 | 源文件 | 目标产出 | 目标用户 | 领域 | 完成日期 |
|:-----|--------|----------|----------|------|:--------:|
| REQ-001 | 街顺APP全面调研报告 | 调研文章 | 物流/SaaS从业者 | healthcare | 2026-04-30 |
| REQ-002 | 紫鲸AI智能体工作流平台 | 产品设计分析 | SaaS创业者 | ai-saas | 2026-05-01 |
| REQ-003 | 鑫港湾HIS系统分阶段整改报告 | 整改方案综述 | 医疗IT管理者 | healthcare | 2026-05-01 |
| REQ-004 | 诊所O2O外卖平台业务调研 | 业务模式分析 | 医疗/零售从业者 | healthcare | 2026-05-01 |
| REQ-005 | 互联网医院模式深度调研 | 行业调研报告 | 医疗从业者 | healthcare | 2026-05-01 |
| REQ-006 | YC AI-Native公司组织方法论 | 方法论文章 | 创业者 | ai-saas | 2026-04-30 |
| REQ-007 | Kimi深度调研集群方法论 | 方法论综述 | 调研者 | ai-saas | 2026-05-02 |
| REQ-008 | EC工业化规范手册 v2.8.0 | 方法论摘要 | 技术管理者 | healthcare | 2026-05-03 |
| REQ-009 | KDO+CKJ enrich 机制建设 | 失败模式库 + 禁止清单 | KDO Agent | master | 2026-05-03 |
| REQ-010 | — | 70_product 机制建设 | KDO 用户 | master | 2026-05-03 |
| REQ-012 | — | 50_delivery 交付注册表 | KDO 用户 | master | 2026-05-03 |
| REQ-013 | — | quality-gates 内容填充 | KDO Agent | master | 2026-05-03 |
| REQ-021 | KDO产品设计大纲 v1.0 | 产品设计方法论文章 | KDO贡献者 | ai-saas | 2026-05-03 |
| REQ-022 | Kimi调研方法论 | AI集群调研方法论文章 | 调研者 | ai-saas | 2026-05-03 |
| REQ-023 | Graph RAG分析 | Graph RAG知识管理文章 | KDO开发者 | ai-saas | 2026-05-03 |

## 进行中

| 编号 | 源文件 | 目标产出 | 目标用户 | 领域 | 阻塞项 |
|:-----|--------|----------|----------|------|--------|
| — | — | — | — | — | — |

## 排队 — P0（本周）

| 编号 | 源文件 | 目标产出 | 目标用户 | 领域 | 备注 |
|:-----|--------|----------|----------|------|------|
| REQ-011 | 00_inbox/一堂-调研行动营启动_原文润色.md | 调研方法论文章 | 调研者 | master | 等待用户定角度 |

## 排队 — P1（本月）

| 编号 | 源文件 | 目标产出 | 目标用户 | 领域 | 备注 |
|:-----|--------|----------|----------|------|------|
| REQ-014 | wiki 现有 enrich 页面 | 每篇一个产出物 | 各领域从业者 | mixed | 12篇已 enrich 页面的 produce |
| REQ-015 | — | kdo watch 生产就绪 | KDO 用户 | master | 文件监听+自动 pipeline |
| REQ-016 | — | CJK enrich 自动化 | KDO Agent | master | LLM endpoint 配置或 extractor 升级 |
| REQ-017 | 20_memory/ | 记忆生命周期管理 | KDO Agent | master | staleness 检测 + 自动更新 |
| REQ-024 | — | kdo watch 自动识别 skill 路由 | KDO Agent | master | watch 检测 frontmatter type:skill → 走 capability 管线而非 knowledge 管线 |

## 排队 — P2（远期）

| 编号 | 源文件 | 目标产出 | 目标用户 | 领域 | 备注 |
|:-----|--------|----------|----------|------|------|
| REQ-018 | — | 60_feedback 闭环回路 | KDO 用户 | master | feedback → improve → verify |
| REQ-019 | — | 70_product 路线图 | KDO 用户 | master | backlog → roadmap 可视化 |
| REQ-020 | — | 跨项目 EC 卡模板迁移 | 技术管理者 | healthcare→ai-saas | 鑫港湾EC模板复用 |

---

## 统计

| 状态 | 数量 |
|------|:----:|
| 已完成 | 13 |
| 进行中 | 0 |
| P0 排队 | 1 |
| P1 排队 | 5 |
| P2 排队 | 3 |
| **合计** | **22** |

---

> 维护规则：Architect 审查产出后可以新增 backlog 条目。Builder 完成条目后更新状态和日期。用户随时可以调整优先级。
