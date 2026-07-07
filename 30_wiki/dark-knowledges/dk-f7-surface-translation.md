---

id: dk-f7-surface-translation
title: F-KDO-007：表层翻译式提炼→Condense 段变成课程目录改写
type: dk
dark_knowledge_type: failure
status: reviewed
domain:
- master
source_person: system
source_context: failure-modes.md F-KDO-007
source_refs:
- src_unknown
created_at: 2026-05-31
updated_at: '2026-06-19'
related:
  - "[[kdo-input-channel-strategy-2026-06-16]]"
  - "[[kdo-protocol]]"
  - "[[modeling-to-kdo-toolchain]]"
  - "[[kdo-batch-produce-req014]]"
  - "[[kdo-15-dimension-label-spec]]"
  - "[[obsidian-kdo-内容产出工作流-产品设计大纲]]"
  - "[[tool-ban-fei-mao-qing-xi-zi-liao-wei-markdown-ge-shi-wei-gei-ai]]"
  - "[[kdo-watch-health-check-layer]]"
  - "[[framework-kdo-self-attack]]"
  - "[[kdo-yaml-frontmatter-safety]]"
  - "[[kdo-priority-checklist]]"
  - "[[kdo_product_design_agent_final]]"
  - "[[proposal-kdo-flywheel-infrastructure]]"
  - "[[yc-放出一套ai-native-公司组织方法论直接把公司当操作系统来设计中层管理变成了-markdown]]"
pipeline:
- src_unknown
- src_unknown
author: unknown
reviewed_by: 欧阳锋
review_date: '2026-06-19'
confidence: 0.88
trust_level: medium
diagnostic_signals:
- src_unknown
- src_unknown
- src_unknown# F-KDO-007：表层翻译式提炼→Condense 段变成课程目录改写

---

## 原始表述/核心洞察

> **触发场景**：Builder 执行三步编译法的 Condense 阶段
>
> **表现**：Condense 段是课程目录的翻译改写（"本课程属于 XX 模块，与 YY 课程并列"），而非课程核心结论的提取。读者看完 Condense 不知道这门课教了什么独特方法
>
> **根因**：Builder 未阅读源材料（或只有目录级信息），用目录结构+公共知识填充 Condense 段
>
> **触发信号**：Condense 段出现大量"本课程属于""在一堂知识地图中的位置""与同模块其他课程"等目录定位语言，缺少具体方法论描述
>
> **防御措施**：① L2 Lint：检测 Condense 段是否含 ≥3 条课程特有的核心结论（非目录描述）② Concept Card Step 0 前置检查：Builder 必须回答「源材料的 3 条核心洞见是什么」
>
> **关联案例**：yt-entrepreneur-five-step-method.md、yt-entrepreneur-scientific-method.md、yt-entrepreneur-fundraising.md — 三张模式 A 卡（2026-05-08 审查）
>
> **关联**：与 F-KDO-011（百科词条化）有重叠——表层翻译式提炼是百科词条化的 Condense 段表现形态

核心洞察：

- src_unknown
- src_unknown
- src_unknown

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **阅读源材料**：Condense 前必须先完整阅读源材料，不能只读目录或摘要
2. **提取核心洞见**：回答「源材料的 3 条核心洞见是什么」——这些洞见必须是该课程独有的，不能是通用知识
3. **剔除目录语言**：删除所有"本课程属于""在知识地图中的位置""与同模块其他课程并列"等目录定位语言
4. **验证区分度**：将提取的 3 条结论与课程目录对比——如果目录已经包含了这些信息，说明提炼还不够深
5. **Reader Test**：让一个没读过源材料的人只看 Condense 段，问他"这门课的核心方法是什么？"——如果他答不上来，说明 Condense 不合格

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

| 失败模式 | 典型表现 | 为什么难以发现 | 快速自检 |
|
|---|---|---|
| 目录改写型 Condense | 出现"本课程属于 XX 模块""与 YY 课程并列"等定位语言 | 卡片格式完整，看起来像知识卡片 | 遮住标题，问自己"这门课教了什么独特方法" |
| 公共知识填充 | 结论是该领域的通用说法，非本课程特有 | 内容"正确"，容易被误认为有价值 | 把结论与课程目录对比，看是否目录已包含 |
| 源材料阅读不足 | Builder 只读目录/摘要，未读完整材料 | 产出有结构、有标题，像那么回事 | 追问"源材料中支持这条结论的具体证据是什么" |
| 与百科词条化并发 | 同时出现定义→分类→特征结构 | 两种失败模式互相掩盖 | 检查是否同时满足 F-KDO-011 的诊断信号 |

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
