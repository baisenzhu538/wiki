---
id: diag-role-routes
title: KDO 角色路由层建议书（任务路由 + 技能路由 + 知识路由）
type: proposal
doc_id: D-20260823-018
version: v1.0
author: huangyaoshi
created_at: '2026-08-23T20:30:00+08:00'
updated_at: '2026-08-23T20:30:00+08:00'
audience: 王语嫣
status: resolved
---

# KDO 角色路由层（三路由合一建议书）

## 现象一句话

路由层只到"文件"，缺"任务/技能/知识"三路由——每个角色进入后该领哪单、该用什么招、该先掌握什么，靠人肉拼图。

## 实证（在哪发现）

2026-08-23 黄药师会话：进入后依次人肉判断——①任务路由缺失：我名下 queued 有 #450（依赖 #449 生效）/ #456（无依赖）/ #459（**被 #460 取代应冻结**），哪单可领靠逐个读任务书+记忆 #460 关系才分辨；②技能路由缺失：52 个 skill 靠触发词被动命中，角色不知道"我是 Builder 该掌握哪 5-10 个"；③知识路由缺失：CLAUDE.md 一句"消化 Core 层 55 张卡"，无角色视角的掌握路径。

## 现状盘点（已有雏形，未成路由）

| 层 | 已有 | 缺口 |
|:--|:--|:--|
| 文件路由 | CAPSULE_STARTUP §2 角色→必读文件 | 只答"读什么" |
| 行为路由 | 行为牌组 B1-B6/L1-L8/W1-W8（遇信号出牌） | 只防"跳步"，不管"该领什么" |
| 知识检索路由 | B6 牌（MOC 优先）+ domain-mapping（域清单双轨）+ domain-routes.yaml | 回答"怎么查"，不回答"角色先掌握什么" |
| 任务路由 | production-queue assignee 列（人肉 grep） | **无主动路由** |
| 技能路由 | 52 skill + 触发词（被动命中） | **无角色→技能映射** |

## 方案：三路由合一（进入即答三问）

### 路由 1 · 任务路由——"我该领哪单"

`queue_transition myqueue --role <role>` 脚本视图（数据源=production-queue，不新增状态）：

```
# role=huangyaoshi
✅ 可领：<task_id>（依赖已满足）
⏸ 等依赖：#xxx（等 #yyy 终审）
🧊 冻结：#459（被 #460 取代，待王语嫣 cancel）
🚧 进行中：claimed-<instance>
```

规则：assignee=我 + queued + 依赖满足 + 非冻结 → 可领；冻结/等依赖/被取代标注原因。已审/历史不显示。

### 路由 2 · 技能路由——"我该用什么招"

角色→技能映射表（从 52 skill 按角色职责归类，每角色 5-10 个核心 + 触发场景；技能触发词不删，路由表只做"角色主动知道"）：

| 角色 | 核心技能（示例） |
|:--|:--|
| 黄药师 Builder | agent-self-iteration（工具卡顿五步闭环）/ domain-iteration / kdo-self-attack / distill-own-skill / self-evolution / nine-layer-deep-dig |
| 王语嫣 Consultant | task-orchestration / stage-1-diagnose / stage-2-skeleton / stage-3-tooling / stage-4-validate / stage-5-assetize / research 系（专家访谈/交叉验证/OSINT）/ knowledge-collision |
| 老顽童 Producer | content-production（draft/polish/positioning）/ domain-iteration / kdo-self-attack / multi-page-article-capture / author-targeted-collect / distill-own-skill |
| 欧阳锋 Architect | kdo-self-attack / six-layer-cross-validation / research-cross-validation / anti-ai-bs-three-moves / pre-ship-check / self-evolution |
| 洪七公 Multimodal | beikai-multimodal-pipeline / comfyui-local / vlm-image-describe-pipeline / visual-asset-analysis / visual-polish / wan-video-generation / cosyvoice-tts / drawio-mcp-diagrams |
| 段王爷 Publisher | feishu-publish / pre-ship-check / presenton-ppt-generator |

### 路由 3 · 知识路由——"我该先掌握什么"

角色→知识路径（先 Core 卡骨架 → 域 digest → MOC → 按需检索；domain-mapping 已有域清单，补"角色视角掌握路径"）：

| 角色 | 知识路径（示例） |
|:--|:--|
| 黄药师 | kdo-moc（52 卡自省）→ 基建相关卡 → 检索按需 |
| 王语嫣 | task-orchestration 方法论 → 全域 digest 全景（domain-mapping 19 域） |
| 老顽童 | 生产域 digest（五步法/战略/销售/调研/内容生产）→ MOC |
| 欧阳锋 | 全域 digest + 审查方法论（framework-ouyangfeng-review-methodology） |
| 洪七公 | 多模态域 digest |
| 段王爷 | 发布域 digest |

## 承载位置

`90_control/role-routes.md`（三路由表，静态）+ `queue_transition myqueue` 子命令（任务路由，动态）+ CAPSULE_STARTUP v3 入口（角色路由表升级，指向 role-routes.md）。基建造表（infrastructure-inventory.md）降级为路由层附录（本建议书附录 A 待补）。

## 边界

- 不动队列状态机（myqueue 只读视图）；不动技能触发词（路由表是增强不是替换）
- 与行为牌/CAPSULE_STARTUP/domain-mapping 并存不冲突（路由层是"导航"，行为牌是"纪律"，文件路由是"入口"）
- 存量角色 spec（#446/#447/#448 已定稿/在产）不因本建议书改动——路由表是新增导航层

## 待讨论点（给王语嫣/老朱）

1. 任务路由的"依赖"数据从哪来——任务书依赖字段（现状无结构化依赖，需任务书 frontmatter 加 `depends_on` 或队列行解析）？
2. 技能路由表放哪维护——六角色谁更新？（建议:各角色 spec 定稿后由编排统一维护）
3. 知识路由的"角色 Core 卡骨架"按什么粒度——每角色 10-20 张？（建议基于 domain-mapping 卡数+角色职责划定）
4. 三路由是否都要脚本化——任务路由 yes；技能/知识路由静态表是否够？
