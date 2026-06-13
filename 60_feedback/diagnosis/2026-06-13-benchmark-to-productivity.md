# 诊断记录：外部知识库对标 → 人员产能建议

**诊断者**：王语嫣
**日期**：2026-06-13
**诊断编号**：D-20260613-001
**关联诊断**：D-20260612-001（外部知识库对标研究报告）
**输出文件**：`70_product/people-productivity/2026-06-13-external-benchmark-insights.md`

---

## 诊断摘要

基于 D-20260612-001 的发现，提取了对"人员产能"最有价值的 5 条启示，写入产品目录。

## 本次做了什么

1. **确认 Nikita Voloboev's Wiki 可访问性**：新 wiki（wiki.nikiv.dev）Cloudflare 已通过，但内容较瘦（21 页，刚起步）。旧 wiki（wiki-old.nikiv.dev）可访问，VitePress 静态站，1,000+ 主题/150K+ 行 markdown，但 sidebar 客户端渲染无法自动提取。
2. **提取对标对产能的关键发现**：
   - 断言式标题 → 知识复用率提升（检索效率）
   - 出链门禁 → 消除知识孤岛
   - Queries 沉淀 → 消除重复劳动
   - 原子性卡片 + 持续演化 → 降低维护成本
   - 目录扁平化 → 降低决策疲劳
3. **输出到产品目录**：`70_product/people-productivity/`（新创建目录）

## 未解决的问题

- KDO 物理上没有 `70_product/` 目录，这是第一次写入。需要确认目录子结构是否与 README 定义一致（projects/、tasks/、connectors/、roadmaps/）。
- 当前写的 `people-productivity/` 应该放在 `70_product/roadmaps/` 下还是直接作为 `70_product/` 的子目录？目前暂时放在新建目录下。
- 建议未被真正"排入迭代"——需要有产品负责人（老顽童？）评估后决定是否以及何时实施。

## 知识库缺口反馈

- 研究过程中发现 KDO 知识库中缺少对"人员产能"的明确定义——这是否应该作为 30_wiki 下的一张新卡片？
- Andy Matuschak 的 Evergreen Notes 理论体系在 KDO 中没有对应的中文翻译/解读卡片
