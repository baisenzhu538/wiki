---
id: task_20260629_vikki-open-source-knowledge-boundary
type: task
status: queued
assignee: 老顽童(Hermes)
priority: P2
created_at: 2026-06-29
updated_at: 2026-06-30
reviewed_by: 欧阳锋
reviewer: 欧阳锋
source_refs:
- 00_inbox/AI-study/0071Vikki战队-2群 · 认知精华提炼.md
- 00_inbox/AI-study/0017大馨战队 · 短视频内容拆解方法论精华提炼.md
related:
- 30_wiki/concepts/concept-kdo-knowledge-boundary
- 30_wiki/frameworks/framework-kdo-content-license
- framework-community-knowledge-production-failure-modes
---

# 沉淀「开源知识使用边界」概念卡

## 目标

基于 Vikki 战队群聊中的「游侠蒸馏事件」，沉淀一张 `concept-open-source-knowledge-usage-boundary` 概念卡，明确 KDO 知识库中开源/分享知识的使用边界，保护自身资产，也规范我们引用外部素材的行为。

## 核心素材

1. **Vikki 开源 3 万字知识库** → 建立了「开源不怕抄袭」的信用
2. **游侠「蒸馏」事件** → 外部人士用渡鸦模型拆 Vikki 业务，引发信任危机
3. **群友冲突** → 「Vikki 做开源就不怕抄袭，你在蒸馏的是别人的价值」
4. **Vikki 边界线** → 从「学习」到「蒸馏」的分界线是「是否用于商业竞争产品」
5. **大馨「抄作业」边界试探** → 群内故意用「抄作业」而非「借鉴」，引发讨论和互动，是一种精心设计的边界策略
6. **大馨 AI 拆解 vs 人工拆解** → 用 AI 代替手动实践是否越界？边界线：AI 是工具，「拆完后的内化」才是目的

## 卡片待产出内容

### 1. concept-open-source-knowledge-usage-boundary

- **type**: concept
- **title**: 开源知识使用边界：学习与蒸馏的分界线
- **核心主张**：开源分享不等于放弃所有权利，学习与商业蒸馏之间存在明确边界。
- **必须包含**：
  - 定义「学习」「引用」「改编」「蒸馏」四个层级
  - 游侠事件作为核心案例
  - 三条边界线：
    - 个人学习 / 内部参考：✅ 允许
    - 商业引用 / 署名转载：⚠️ 需授权或遵循许可协议
    - 直接用于竞争产品 / 竞品 fork：❌ 越界
  - KDO 知识库默认使用协议建议
  - 失败模式：开源无协议 → 信任危机 → 贡献者流失

### 2. 可选配套：license 建议卡或系统配置

- 在 `30_wiki/systems/` 或 `90_control/` 中增加 KDO 默认内容使用协议模板
- 例如：CC BY-NC-SA 4.0（署名-非商业-相同方式共享）或自定义协议

## 执行要求

1. 老顽童先搜索国际上通行的开源知识/content license 最佳实践（WebSearch 强制步骤）。
2. 案例卡必须包含关键证据、可迁移场景、失败模式、相关方法论。
3. 与现有 `framework-kdo-content-standards` 或 `concept-kdo-knowledge-boundary` 建立 related 链接。
4. 跑 `kdo pre-submit` 通过。

## 验收标准

- 概念卡正文 ≥100 行，含 L1-L5 深挖
- `kdo pre-submit` 通过
- related ≥5，包含至少 1 张 KDO 系统/框架卡和 1 张 case 卡
- 欧阳锋终审：边界线清晰、案例具体、协议可操作
