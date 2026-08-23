---
id: diag_20260823_zijing-ag-product-outline-study
title: 紫鲸 AG 数字员工·智能体编排与产品思路研究 + 产品大纲
type: diagnosis/research
author: 王语嫣
created_at: 2026-08-23
status: draft
audience: 老朱
---
# 紫鲸 AG 数字员工·编排与产品思路研究 + 产品大纲

> 研究方法：① webfetch install 页（8 员工分工/安装/PAT/账号积分/安全）② webfetch 主页 aixt.pifu.ink（产品定位/课程/分销）③ curl MCP `/mcp/health`（在线/13 工具）④ curl MCP `tools/list`（13 工具完整 inputSchema + metadata）。
> ⚠️ 安全：原推广消息含 PAT 与账号密码，**未写入本文件/git**（安全铁律）。本研究只引用产品架构，不含任何凭据。

## 一、产品定位

- **名称**：紫鲸 AI / "AI 超级个体增长操作系统"
- **口号**：把"想法→内容→成交"跑成闭环
- **目标用户**：超级个体 / 小老板 / 知识 IP（`one_person_company` / `knowledge_ip` / `b2c_local_*` / `b2b_*` 七类商业模式）
- **解决什么**：内容营销全链路（方向 → 内容 → SOP → 成交）从想法到闭环
- **一句话**：面向"一个人公司"的、agent 编排式内容营销工厂

## 二、智能体编排架构（核心，最值得学）

### 1. 13 工具 = 8 业务角色 + 3 内容形态 + 2 编排门禁

| # | 工具(推测 name) | output_kind | 角色 | 上游依赖 |
|:--:|:--|:--|:--|:--|
| 1 | ag1-beta 丁定位 | positioning_object | 品牌定位 | —（链头）|
| 2 | ag103-beta 顾画像 | profile_object | 客户画像 | positioning |
| 3 | ag2-beta 赵选题 | topic_object | 内容选题 | positioning/profile |
| 4 | ag3-beta 温脚本 | script_object | 脚本/文案 | topic（链主干）|
| 5 | ag5-beta 彭友圈 | private_traffic_object | 朋友圈/私域触达 | script |
| 6 | ag6-beta 佘群发 | community_ops_object | 社群运营 | script |
| 7 | ag7-beta 程成交 | sales_dialogue_object | 销售话术/成交 | script |
| 8 | ag-cao-beta 曹运营 | growth_ops_object | 增长运营规划 | positioning/profile（链头分支）|
| 9 | ag9-beta | xiaohongshu_note_object | 小红书笔记 | script（消费 ag3）|
| 10 | ag10-beta | wechat_article_object | 公众号文章 | script（消费 ag3）|
| 11 | ag11-beta | graphic_note_object | 图文笔记 | positioning/profile/topic |
| 12 | compliance_check | compliance_check_object | **L2 合规审查** | script |
| 13 | publish_pack | publish_pack_object | **L3 发布包** | script + compliance_check |

> 注：面向用户宣传"8 个数字员工"是营销口径；MCP 实际暴露 13 工具（8 业务 + 3 内容形态 + 2 门禁）。文案与 install 页角色名也有出入（文案"唐成文"vs install"程成交"），口径不一致。

### 2. DAG 有向无环图流水线（关键设计）

```
定位 ──► 画像 ──► 选题 ──► 脚本 ──┬─► 小红书笔记 ──┐
                                  ├─► 公众号文章 ──┤
                                  ├─► 朋友圈/私域 ─┤
                                  ├─► 社群运营 ────┤
                                  ├─► 销售成交 ────┤
                                  └─► 合规审查 ──► 发布包
运营规划（从定位/画像分支）───────────────────────┘
```

**result_id 串联机制**：每步产出强类型 `result_id`（如 `positioning_xxx` / `topic_xxx` / `script_xxx`），下游通过 `upstream_*_result_id` 参数**显式取上游产物**。同一 `script_result_id` 可被小红书/公众号/图文 3 个内容形态复用——一次脚本、多平台分发（"一鱼多吃"）。

### 3. 强类型产物 + 邻接表（每个工具 metadata 声明）

每个工具 metadata 含：
- `output_kind`：强类型产物名（13 类，产物即合约）
- `upstream_dependencies`：上游依赖列表
- `downstream_consumers`：下游消费者列表
- `credits_per_call`：积分消耗（6-15/工具，按价值定价）
- `required_tier`：分级（pro）
- `supported_business_models`：适配的商业模式（7 类）
- `supported_industries`：行业（* 通用）
- `requires_ip_persona`：是否需 IP 人设

**这本质是一张可组合的 DAG 邻接表**——产物强类型 + 依赖/消费者声明 = 可编排、可复用、可计费。

## 三、商业化机制

| 维度 | 设计 |
|:--|:--|
| 计费 | 积分制（credits_per_call 6-15/工具，按工具价值差异化定价）|
| 分级 | required_tier（pro 等）|
| 匹配轴 | 商业模式（7 类）× 行业 slug × buyer_role × 内容目标 × 平台 |
| 试用转化 | 1 月体验 + 1000 积分 + 套餐购买（z.pifu.ink 主站）|
| 产物隔离 | `space_id`（同业务/项目下固定，跨项目意味不同）|

## 四、门禁与知识体系

- **L2 合规审查**（compliance_check）：`verdict(safe/low_risk/blocked) + violations + qc_id`，基于 `COMPLIANCE-101/102/103/201/202/301` 知识体系；平台/行业/人设型专项（医疗专词/小红书敏感等）
- **L3 发布包**（publish_pack）：7 字段分发（标题SEO/封面/话题标签/置顶评论/神评论/SEO关键词/发布时间窗），基于 `PUBLISH-101/102/201/202` 知识体系
- **知识体系编号**（COMPLIANCE-xxx / PUBLISH-xxx）= 沉淀的方法论卡体系（类似 KDO 的卡）
- **MANIFEST 链路**：`compliance_check → publish_pack` 强制顺序（合规过了才发布）
- **L3+ 高级模型不走 MCP 网关，仅 crew 直接调用**（分层：MCP 网关 vs 内部 crew）

## 五、交付与生态

- **交付**：远程 MCP（`aixt.pifu.ink/mcp`），PAT Bearer 鉴权，多底座（WorkBuddy/Claude Desktop/Codex 的 JSON 或 TOML 配置）
- **账号体系**：aixt.pifu.ink 登录/PAT 管理（/settings/api-keys）/积分
- **课程变现**：AI 超级个体实战营 / 公开课 / 线下实操营（z.pifu.ink/course）
- **内容生态**：产品介绍/SOP/视频案例/客户案例/研发历史/博客
- **分销体系**：affiliate 分销

## 六、对 KDO 的借鉴判断（王语嫣独立判断）

### A. 紫鲸比 KDO 更成熟的地方（值得学）

1. **产物级 DAG（result_id 串联 + 强类型 output_kind + 邻接表）**——KDO 的 `depends_on`（F-047）是任务级依赖，紫鲸是**产物级**编排：每步产物是强类型合约，可被多下游复用。这比 KDO 任务依赖更细、更可组合。KDO 可在 `depends_on` 之上加一层"产物 result_id"机制。
2. **积分制商业化**——KDO 是内部工厂无计费；紫鲸按工具价值差异化定价（6-15 积分）。若 KDO 对外产品化，积分制是现成范式。
3. **门禁产品化（合规/发布层）**——紫鲸把审查做成 MCP 工具（compliance_check + publish_pack + MANIFEST 强制顺序）。KDO 的 quality gate + 段王爷发布可借鉴此"门禁即工具"形态对外暴露。
4. **商业模式/行业匹配轴**——紫鲸用 `supported_business_models`（7 类）+ `industry_slug` 让 agent 自适应场景。KDO 卡片有 domain/tags 但无"商业模式匹配"这一对外维度。

### B. KDO 比紫鲸更成熟的地方（不必学）

1. **组织治理**：KDO 有 charter v1.0（六角色岗位说明书 + 通用准则 + 自迭代双回路）+ 双实例印证 + provenance 溯源——紫鲸是远程黑盒，无治理层。
2. **状态机**：KDO queue_transition.py 状态机（queued/claimed/pending_review/reviewed/cancelled）+ #390 原子 commit + 探针自动通知——紫鲸的 DAG 是无状态 result_id 链（无任务状态流转概念）。
3. **记忆架构**：KDO 记忆胶囊 L1-L4 + 全量保存 + WAL——紫鲸"共享记忆文档"是内部实现，对外不可见。
4. **门禁深度**：KDO 三层门禁（L1 结构/L2 内容/L3 管线）+ KF-001~022 铁律 + pre-submit——紫鲸只有 L2 合规 + L3 发布两层。

### C. 关键差异：场景不同

- 紫鲸 = **内容营销工厂**（一次性内容产出，产物=文案/脚本）
- KDO = **知识沉淀工厂**（可复用知识卡/文章/课程，产物=可溯源知识资产）

紫鲸的 DAG 是"产出即弃"（一条短视频脚本用完即弃），KDO 是"产出即资产"（卡片进 vault 复用）。两者编排哲学不同，**不能直接照搬**，但产物级 DAG 思路可借鉴。

## 七、KDO 产品化方向建议（大纲）

若借鉴紫鲸思路把 KDO 对外产品化，产品大纲如下：

### 产品名（建议）
"KDO——知识交付操作系统（Knowledge Delivery OS）"

### 定位
面向知识工作者/内容团队/培训师的**知识沉淀与交付工厂**：把口述稿/素材/经验 → 可复用知识资产（卡片/文章/课程）→ 多渠道交付。

### 智能体编排（借鉴紫鲸 DAG + result_id）

```
素材诊断 ──► 主题域 MOC ──► 任务编排 ──► 卡片生产 ──┬─► 文章（多平台）
   （王语嫣）     （黄药师基建）   （王语嫣）    （老顽童）├─► 课程
                                                      ├─► 报告
                                                      └─► 终审（欧阳锋）──► 发布（段王爷）
```

- 每步产出强类型 `output_kind`（diagnosis_object / moc_object / card_object / article_object / course_object / review_object）
- `result_id` 串联：同一批卡片可被多下游（文章/课程/报告）复用
- `upstream_dependencies` / `downstream_consumers` 邻接表

### 商业化（借鉴积分制）
- 积分制：诊断/编排/产卡/终审/发布各工具按价值计积分
- 分级：个人版/团队版/企业版
- 匹配轴：知识领域（domain）× 角色（TCPR）× 交付形态

### 门禁产品化（借鉴 compliance/publish）
- 终审即 MCP 工具（review_object，verdict pass/fail + 扣分点 + 修复项）
- 发布即 MCP 工具（publish_object，多渠道分发 + 版本记录）
- MANIFEST 链路：`review → publish` 强制顺序

### 差异化（vs 紫鲸）
- 紫鲸产出即弃；KDO 产出即资产（可溯源、可复用、可演进）
- 紫鲸无治理；KDO 有 charter 六角色 + 双实例印证
- 紫鲸无状态机；KDO 有 queue_transition 全流转 + 探针通知

## 八、给老朱的决策点

1. **是否产品化**：KDO 目前是内部工厂，是否要做对外产品（借鉴紫鲸形态）？
2. **借鉴优先级**：若借鉴，最值钱的是**产物级 DAG（result_id + 强类型 output_kind）**——这能升级 KDO 的任务依赖到产物依赖，对内对外都有用（不止为产品化）。
3. **试点**：可先在 KDO 内部试"产物 result_id"机制（F-047 depends_on 升级），跑通后再考虑对外产品化。
4. **不照搬**：紫鲸的远程黑盒 MCP + 限时积分 + 内容营销场景，不建议直接搬进 KDO 生产链（场景/架构/信任都不匹配，前轮已判断）。

---
*王语嫣 · 2026-08-23 · 诊断式研究产出 · 不含凭据（PAT/账号未入文件）*
