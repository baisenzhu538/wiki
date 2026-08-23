---
id: role-routes
title: KDO 角色路由层（三路由合一）
type: navigation
version: v1.0
created_at: '2026-08-23T22:00:00+08:00'
updated_at: '2026-08-23T22:00:00+08:00'
owner: 王语嫣（编排统一维护）
audience: 六角色
---

# KDO 角色路由层（进入即答三问）

> #472 交付（建议书 `diag_20260823_huangyaoshi-role-routes.md` 采纳）。导航层：只答「领哪单 / 用什么招 / 先掌握什么」，不替代行为牌（纪律层）、文件路由（CAPSULE_STARTUP 入口层）、domain-mapping（知识清单层）。
> 维护权：**编排统一维护**（王语嫣）——各角色 spec 定稿后随 spec 演进，与标签建议同模式；改动走任务制。

## 路由 1 · 任务路由 —— 我该领哪单

```bash
python 90_control/scripts/queue_transition.py myqueue <拼音角色名>
```

只读视图，五态：✅ 可领（queued+依赖满足+非冻结）/ ⏸ 等依赖（任务书 `depends_on` 未满足）/ 🧊 冻结（队列行标注勿领/冻结留档，含被取代挂账）/ 🚧 进行中（claimed-&lt;role&gt;）/ ⏳ 待终审（pending_review）。

**依赖字段约定（F-047 登记字段演进）**：任务书 frontmatter `depends_on: "<任务号>"`（可逗号分隔）——新任务单起强制登记；存量任务无字段=可领（向前生效，不回改）。

## 路由 2 · 技能路由 —— 我该用什么招

52 skill 按角色职责归类（触发词体系保留——路由表是"角色主动知道"，不是替换）：

| 角色 | 核心技能（5-10 个） | 触发场景 |
|:--|:--|:--|
| 黄药师 Builder | agent-self-iteration · domain-iteration · kdo-self-attack · distill-own-skill · self-evolution · nine-layer-deep-dig | 工具卡顿/规则失效 · 新域任务 · 产卡自攻击 · 沉淀自己的技能 · 深挖需求 |
| 王语嫣 Consultant | task-orchestration · stage-1-diagnose · stage-2-skeleton · stage-3-tooling · stage-4-validate · stage-5-assetize · research-expert-interview · research-cross-validation · knowledge-collision | 编排任务 · 素材诊断 · 域五阶段 · 专家访谈调研 · 交叉验证 · 桥接设计 |
| 老顽童 Producer | content-production · content-production-draft · content-production-polish · content-production-positioning · domain-iteration · kdo-self-attack · multi-page-article-capture · author-targeted-collect | 产卡 · 草稿打磨 · 去 AI 味 · 定位声明 · 长文捕捉 · 博主定向采集 |
| 欧阳锋 Architect | kdo-self-attack · six-layer-cross-validation · research-cross-validation · anti-ai-bs-three-moves · pre-ship-check · self-evolution | 终审自攻击 · 六层验证 · 交叉验证 · AI 输出甄别 · 出库前检查 |
| 洪七公 Multimodal | beikai-multimodal-pipeline · comfyui-local · vlm-image-describe-pipeline · visual-asset-analysis · visual-polish · wan-video-generation · cosyvoice-tts · drawio-mcp-diagrams | 多模态渲染路由 · 生图 · 图片识别 · 视频 · TTS · 图表 |
| 段王爷 Publisher | feishu-publish · pre-ship-check · presenton-ppt-generator | 飞书分发 · 出库检查 · PPT 生成 |

## 路由 3 · 知识路由 —— 我该先掌握什么

角色 → 路径：先 Core 卡骨架 → 域 digest → MOC → 按需检索（检索架构 v2：MOC 绝对优先 + BM25 融合 + RRF 排序，`kdo query` 执行）。

| 角色 | 知识路径（粒度=每角色 10-20 张 Core，基于 domain-mapping 卡数+职责） |
|:--|:--|
| 黄药师 Builder | `kdo-moc`（52 卡，KDO 系统自省）→ 基建相关卡（质量门/检索/胶囊）→ `kdo query` 按需 |
| 王语嫣 Consultant | task-orchestration 方法论 → 全域 digest 全景（domain-mapping 19 域：调研/战略/销售/需求/决策/人域…）→ 按需 |
| 老顽童 Producer | 生产域 digest 优先（五步法/战略/销售/调研/内容生产/AI协作）→ 对应 MOC → 按需 |
| 欧阳锋 Architect | 全域 digest + `framework-ouyangfeng-review-methodology` → 跨域桥接（`30_wiki/cross-domain-patterns/`） |
| 洪七公 Multimodal | 多模态域 digest（design-moc）→ 视觉资产桥接 → 按需 |
| 段王爷 Publisher | 发布域 digest（feishu-publish 卡）→ 反馈闭环卡 → 按需 |

**检索纪律**：回答域知识问题前必须 `kdo query`（域知识检索铁律）——路由表给"掌握路径"，检索给"即时答案"，两者不互相替代。

## 入口衔接

- CAPSULE_STARTUP（唯一启动指针）§2 角色路由表 → 本文件（三路由）
- 冷启动完整链路：#445 一键启动（WT 5 标签）→ CAPSULE_STARTUP → 本文件 → `myqueue` → 领任务
- **六角色 spec 冷启动链已接路由层**（#475 收口）：各 `30_wiki/agent-specs/agent-spec-<角色>.md` 工作流「0. 冷启动」步引用本文件 → 恢复完即答三问

## 附录 A · 基建资产地图（#488，D-018 附录 A 结清）

- **总表**：`90_control/infrastructure-inventory.md`（全厂基建：门禁/工具/服务/计划任务/数据资产/台账/一次性批——位置+职责+维护人+最近验证+关联）
- **健康快照**：`python kdo-tools/infra-status.py`（27 项资产一键 🟢/🔴）
- 本附录即 D-018「基建造表附录 A 待补」的结清项——路由层管"该做什么"，总表管"有什么"

## 维护纪律（解 #472 终审残余风险：spec↔路由同步）

- **owner**：王语嫣（编排统一维护）
- **双向同步**：本文件改（技能/知识路由表、角色段）→ 同步更新对应角色 spec 冷启动步；角色 spec 演进（职责/技能集变更）→ 同步回本文件。任一侧改，另一侧不滞后（防欧阳锋终审点名「不同步」）
- **演进触发**：各角色 spec 定稿/大改、标签体系建轴（#474 体检后）、新技能卡入库 → 触发本文件审视
- **不动本文件本体**：路由层只读导航；myqueue 脚本归 #472 黄药师线，本文件只描述不实现

---

*黄药师初稿 · 王语嫣编排维护 · 2026-08-23 · #475 收口补维护纪律*
