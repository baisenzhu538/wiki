---
id: diag_20260823_zijing-ag-architecture-deep-dive
title: 紫鲸 AG·产品架构与技术架构深入调研
type: diagnosis/research
author: 王语嫣
created_at: 2026-08-23
status: draft
audience: 老朱
related: diag_20260823_zijing-ag-product-outline-study
---
# 紫鲸 AG·产品架构与技术架构深入调研

> 研究方法：① install 页（安装/PAT/账号）② 主站 z.pifu.ink 首页+SOP+定价+about（产品全貌）③ `/.well-known/mcp.json`（discover）④ `tools/list` 13 工具完整 inputSchema+metadata（Python 探针干净输出）
> ⚠️ 不含凭据（PAT/账号未入文件/git）

## 一、产品架构

### 1. 定位与哲学
- **产品名**：紫鲸 AI / "AI 获客操作系统"（"让实体老板拥有一支 AI 获客团队"）
- **口号**：把"想法→内容→成交"跑成闭环；让增长从偶然变成复利
- **哲学**（与 KDO 高度相通）：把方法论写进系统，让普通人"做选择题"跑通闭环；老板最贵的资源=决策力；不承诺播放量/涨粉/转化率，只承诺闭环+产能+复利
- **底层方法**：洞察→诊断→工程→分发→承接→迭代（六环）

### 2. 组织架构：18 数字员工 × 5 部门
主站揭示**实际 18 位**（推广文案/MCP 的"8 个"只是开放子集）：

| 部门 | 员工（AG 编号） |
|:--|:--|
| 战略部 | 丁定位(AG1) / 陆变现(AG102) / 顾画像(AG103) / 甄能力(AG104) |
| 内容部 | 赵选题(AG2) / 温脚本(AG3) |
| 制作部 | 柯声音(AG8-1) / 裴配音(AG8-2) / 沈分身(AG8-3) / 景导演(AG8-4) / 简剪辑(AG8-5) |
| 运营部 | 周发布(AG4-1) / 盖小稿(AG4-1R) / 搜排名(AG4-2) / 曹运营 |
| 销售部 | 彭友圈(AG5) / 佘群发(AG6) / 程成交(AG7) |

> **关键**：MCP 仅开放 13 工具（8 业务角色 + 3 内容形态 + 2 门禁）；**制作部 5 个数字人需工作台**（数字人合成要本地/专有运行时，不开放远程 MCP）。这解释了"8 个数字员工"营销口径与 13 工具的差。

### 3. 五大阶段方法论（产品骨架）
战略定位→内容工程→制作系统→运营分发→私域成交。每阶段明确输入输出，"先对，再快"。

### 4. 诊断体系（双诊断）
- **六维诊断**：定位/产品/内容/流量/私域/成交（找短板）
- **四环诊断**：获客→成交→交付→复购（找漏水环）

### 5. 三层架构
- **工具层**（效率，立刻能用）：选题/脚本/出片/发布/承接流水线
- **方法论层**（稳定）：四环诊断/脚本公式/赛马机制/发布排雷，"会做"→"持续做"
- **资产层**（复利）：24 条铁律 + 行业知识库 + 案例库，产出沉淀为库存

### 6. 商业模式
| 维度 | 设计 |
|:--|:--|
| 定价三档 | 入门（1 账号/月产 30 条/基础定位/标准模板/邮件）/ 专业（3 账号/月产 100 条/深度定位+竞品/自定义模板+数字人/专属顾问）/ 企业（定制/不限账号/全功能/**API 接入**+**私有化部署可选**+SLA）|
| 计费轴 | 账号数 × 月产条数 × 功能深度 × 交付支持 |
| 产能限制 | 月产 30/100/不限——产能即计费维度 |
| 数字人 | 专业版+（制作部能力付费墙）|
| 课程变现 | 老板 AI 提效实战营 / 公开课 / 线下实操营 |
| 行业方案 | 医药（品牌方/服务商）/ 美业门店 / 知识 IP |
| 解决方案入口 | 减负 / 一人公司 / 第二曲线 / 内容产能翻倍 |
| 分销 | affiliate |
| 转化路径 | 预约演示→诊断→试用→套餐 |

### 7. 团队与数据背书
- **创始人**：许院（18 年创业/3026 家联盟店/3000+ 创业者教练）
- **联创**：**半肥猫**（24 年商业实战/AI 商业应用先行者）——**关键**：半肥猫既是紫鲸联创，又是 KDO 素材来源（一堂/AI 俱乐部/00_inbox/半肥猫/）。这条推广很可能经半肥猫而来。
- 内容策略组（行业模型/脚本结构卡/赛马机制 SOP）+ 数字拍摄组（数字人训练/出片/发布）
- 数据：53 账号试错 / 500+ 直播（75000 分钟/479500 观众）/ 2000+ 数字人 / 5000+ 短视频 / 4315+ 客户

## 二、技术架构

### 1. MCP 协议层
- **端点**：`https://aixt.pifu.ink/mcp`（aliases: `/api/v1/mcp` + `https://api.zjai.ink/mcp`）
- **协议**：MCP-Protocol-Version `2025-06-18`
- **鉴权**：Bearer PAT（`Authorization: Bearer {PAT}`），PAT 在 `/settings/api-keys` 管理
- **discover**：`/.well-known/mcp.json` 自描述（mcpServers.zijing-ag + bearer auth + aliases）
- **健康检查**：`/mcp/health`（公开，返回 status/authenticated/endpoint/protocolVersion/tools 数）
- **多底座适配**：WorkBuddy/Claude Desktop 用 JSON，Codex 用 TOML（`~/.codex/config.toml`）

### 2. 13 工具完整 DAG 邻接表（upstream 硬依赖为权威）

```
ag1定位 ──► ag103画像 ──► ag2选题 ──► ag3脚本 ──► compliance ──► publish
   │            │            │            │
   │            ├──► ag5朋友圈          └──► ag6社群
   │            ├──► ag7销售
   │            │
   ├──► ag9小红书 ◄──(ag1+ag103+ag2)
   ├──► ag10公众号 ◄──(ag1+ag103+ag2)
   ├──► ag11图文 ◄──(ag1+ag103+ag2)  ◄──(ag3脚本可选)
   │
   └──► ag-cao运营规划 ◄──(ag2选题)
              │
              ├──► ag5/ag6/ag7（销售三件）
              └──► ag9/ag10/ag11（内容三形态）
```

| 工具 | output_kind | 硬依赖(upstream) | credits | ip_persona |
|:--|:--|:--|:--:|:--:|
| ag1 丁定位 | positioning_object | —（root）| 10 | False |
| ag103 顾画像 | profile_object | ag1 | 8 | True |
| ag2 赵选题 | topic_object | ag103 | 8 | False |
| ag3 温脚本 | script_object | ag2 | 10 | True |
| ag5 彭友圈 | private_traffic_object | ag103 | 6 | True |
| ag6 佘群发 | community_ops_object | ag103+ag3 | 8 | True |
| ag7 程成交 | sales_dialogue_object | ag103 | 8 | True |
| ag-cao 曹运营 | growth_ops_object | ag2 | 12 | False |
| ag9 小红书 | xiaohongshu_note_object | ag1+ag103+ag2 | 12 | True |
| ag10 公众号 | wechat_article_object | ag1+ag103+ag2 | 12 | True |
| ag11 图文 | graphic_note_object | ag1+ag103+ag2 | 12 | True |
| compliance | compliance_check_object | ag3 | 15 | True |
| publish | publish_pack_object | ag3+compliance | 6 | True |

### 3. 两条主干
- **内容产出链**：ag1→ag103→ag2→ag3→（ag9/ag10/ag11 内容形态）→compliance→publish
- **运营成交链**：ag2→ag-cao→（ag5/ag6/ag7 销售）+（ag9/ag10/ag11 内容形态）

### 4. 超级枢纽
- **ag103 顾画像**：8 个下游（几乎全部内容+销售 agent 消费画像）——画像定 IP 人设后全链复用
- **ag-cao 曹运营**：6 个下游（驱动销售+内容形态）——运营规划是第二指挥中心
- **ag3 温脚本**：门禁汇聚点（compliance+publish 都以脚本为上游）

### 5. 产物机制（核心）
- **result_id 串联**：每步产 `result_id`（如 `positioning_xxx`/`script_xxx`），下游 `upstream_*_result_id` 显式取上游产物；同一 script 可被多下游复用（一鱼多吃）
- **强类型 output_kind**：13 类产物即合约（positioning_object/script_object/...）
- **pack_only 双形态返回**：默认 false（返小包=result_id+runtime_object）；true 时只返结构化封装（配合 writer_prompt 临时输入时用）
- **runtime_object**：结构化产物对象，含可被下游消费的字段

### 6. 上下文与匹配
- **space_id**：同业务/项目固定，跨项目不同（产物隔离）
- **override**：运行时覆盖 runtime_object 的 industry_slug/industry_group/business_model/buyer_role/content_goals/platform_focus/content_formats——同 agent 适配多场景
- **ip_persona**：IP 人设文本（多数工具 requires_ip_persona=True，从 ag103 画像继承）
- **硬依赖 vs 软依赖**：metadata `upstream_dependencies`=硬依赖（必须先有）；公共参数 `upstream_*_result_id`=软依赖（可选增强，如 ag-cao 硬依赖只 ag2 但可软取画像）

### 7. 公共参数契约（13 工具共享）
每工具共享一套 13 公共参数：`input`/`user_input`/`space_id`/`override`/`source_output_id`/`topic`/`goal`/`writer_mode`/`ip_persona`/`adopt_profile`/`pack_only` + 7 类 `upstream_*_result_id`（positioning/profile/topic/growth_ops/script/article/note）。
**工具专属参数**：ag3（batch_mode/topics/confirm_mode）/ag6（mode）/ag7（mode+customer_profile+product_info+customer_message+key_objection+conversation_stage+session_id）/compliance（script_result_id+script_body+platform+industry+persona_type+output_mode）/publish（script_result_id+platform+account_type A/B+topic_summary+upstream_qc_result_id）/ag1（industry_anchor）。

### 8. AG4-OPS gateway 自动路由
`source_output_id`：直接传 AG4-OPS 的 output_id，gateway 自动转 `upstream_growth_ops_result_id`，并可顺带取 topic/profile/positioning 等软依赖——说明有个**运营规划系统（AG4-OPS）+ gateway 自动路由层**，不是纯工具直连。

### 9. 分层调用
- **MCP 网关层**（13 工具，pro tier，远程 HTTP）——对开发者/集成方开放
- **crew 层**（L3+ 高级模型，不走 MCP，仅 crew 直接调用）——compliance/publish 标注"L3+ 不走 MCP 网关，仅 crew 直接调用"
- **工作台层**（制作部 5 数字人，需工作台本地运行时）——数字人合成不开放 MCP

### 10. 门禁 MANIFEST
- `compliance_check → publish_pack` **强制顺序**（合规过了才发布）
- compliance：verdict(safe/low_risk/blocked)+violations+qc_id，基于 COMPLIANCE-101/102/103/201/202/301 知识体系，平台/行业/人设型专项
- publish：7 字段（标题SEO/封面/话题标签/置顶评论/神评论/SEO关键词/发布时间窗），基于 PUBLISH-101/102/201/202
- **知识体系编号**（COMPLIANCE-xxx/PUBLISH-xxx）= 沉淀的方法论卡体系（类似 KDO 的卡）

### 11. 积分计费梯度
credits_per_call 6-15：门禁/枢纽贵（compliance 15/ag-cao 12/ag9-11 各 12），普通业务 6-10。定价反映工具价值/枢纽性。business_models 7 类（ag1+两门禁限定选择性开放，其余 * 全商业模式）。

## 三、对 KDO 的技术借鉴判断（深化）

| 紫鲸机制 | KDO 现状 | 借鉴价值 |
|:--|:--|:--|
| 产物级 DAG（result_id+output_kind+邻接表）| 任务级 depends_on（F-047 刚立）| **最高**——升级 KDO 任务依赖到产物依赖，产物可被多下游复用 |
| 公共参数契约（13 工具共享）| 任务单 frontmatter 四件套 | 中——KDO 任务单可加产物 schema 契约 |
| pack_only 双形态返回 | 产物=文件 | 中——KDO 可加"结构化产物对象 vs 文件"双形态 |
| override 运行时上下文覆盖 | 商业模式匹配轴缺失 | 中——KDO 加 business_model/industry 匹配轴 |
| crew 分层（网关 vs 高级模型）| 双实例/多实例（agent-os §13）| 低——KDO 已有更成熟的多实例分层 |
| 积分计费 | 内部工厂无计费 | 高（仅对外产品化时）|
| MANIFEST 门禁（compliance→publish）| quality gate + 段王爷发布 | 中——KDO 门禁可产品化为 MCP 工具 |
| 知识体系编号（COMPLIANCE-xxx）| KF-001~022 铁律 + dk 卡 | 低——KDO 已有更完整的卡体系 |

**核心借鉴结论**：最值钱的是**产物级 DAG**——紫鲸用 result_id+强类型 output_kind+邻接表把"任务依赖"升级到"产物依赖"，产物可复用、可组合、可计费。KDO 的 F-047 depends_on 是任务级，可在此之上加一层"产物 result_id"机制，对内（编排可组合）对外（产品化）都有用。其余机制 KDO 多已有更成熟版本（治理/状态机/记忆/门禁深度），不必照搬。

## 四、关键背景发现

1. **半肥猫是紫鲸联创**——这解释了 KDO 为何有大量半肥猫素材（00_inbox/半肥猫/、AI 知识库、口述逐字稿）。这条推广很可能经半肥猫而来。老朱与紫鲸存在人脉交集。
2. **哲学相通**：紫鲸"把方法论写进系统"≈ KDO"把知识沉淀进 vault"；紫鲸"做选择题跑闭环"≈ KDO"用户做 ≤3 选项"。两者都是"把经验变成可复用系统"的路子，但场景不同（紫鲸=内容营销即弃产出，KDO=知识资产可溯源复用）。
3. **企业版有 API 接入+私有化部署**——说明紫鲸已支持企业级交付（私有化），技术架构有可私有化的设计。
4. **18 人 vs 8 vs 13**：营销口径（8）、主站全貌（18）、MCP 实际（13）三层口径不一致——开放度分层（工作台数字人/MCP 网关/crew 内部）。

---
*王语嫣 · 2026-08-23 · 深入调研产出 · 不含凭据（PAT/账号未入文件/git）· 与 `diag_20260823_zijing-ag-product-outline-study` 互补（前者产品大纲，本件架构深挖）*
