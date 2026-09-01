---
name: research-core
title: 调研能力层统一入口——OSCAR 意图路由+核心纪律+专项武器库三层结构
description: 统一调研入口（全 agent 基础能力层，老朱 09-02 拍板）——任何调研/查证/深挖/情报任务先走本入口：第一层 OSCAR 意图路由→第二层核心纪律（交叉验证+质量门禁+深挖引擎）→第三层专项武器库按需载。触发：调研、帮我查、查证、验证断言、验证这个说法、这个说法靠不靠谱、fact check、数据核验、深挖、尽调、行业分析、竞品分析、市场研究、情报收集。非调研任务（纯写卡/纯施工）不路由进本层。
version: 1.0.0
author: Skills 助理（#594 整合生产）
adapted_from: business-research-skill-oscar-13-weapon-system
status: enriched
reviewed_by: 待审（欧阳锋，#594 提审后终审）
updated_at: 2026-09-02
license: MIT
platforms: [linux, macos, windows]
tags:
  - audience:executor
  - scene:research
  - skill-level:foundation
  - research
  - 调研
  - 统一入口
  - OSCAR
  - 基础能力层
metadata:
  hermes:
    tags: [research, 调研, 统一入口, OSCAR, 基础能力层, 交叉验证, 深挖]
    related_skills: [research-cross-validation, six-layer-cross-validation, research-quality-gate, nine-layer-deep-dig, research-sats, research-industry-report, research-financial-report, research-expert-interview, research-alt-data, research-osint, research-web-scraping, research-google-dorking, research-media-verification, research-multi-agent, research-ci-framework]
---

# research-core 统一调研入口

> 全 agent 基础能力层：调研是最基础的必备能力（老朱 09-02 拍板——会读写的 agent 才能上岗，会调研的 agent 才能干活）。任何调研类任务先走本入口，禁止凭记忆直接输出结论。

## 触发条件（何时必须走本层）

| 场景 | 示例请求 |
|:--|:--|
| 事实查证 | 「验证一下这个说法」「这个数据靠谱吗」 |
| 行业/市场研究 | 「调研一下XX行业」「市场规模和趋势」 |
| 竞品/公司分析 | 「分析一下XX公司」「这个赛道怎么样」 |
| 深挖分析 | 「帮我深挖这个项目」「风险画像」 |
| 情报收集 | 「查竞对XX」「尽调XX」 |
| 决策前调研 | 「要不要做XX，先调研下」 |

**反触发（不路由进本层）**：纯写卡、纯施工、纯格式整理、已有明确答案不需要外部信息——这些走各自产线，不消费本层。

## 三层结构总览

```
第一层 意图路由：OSCAR 定目标（30 秒，必做）
  ↓
第二层 核心纪律（所有调研必经，逐项过）：
  ├── 交叉验证（双源判定：research-cross-validation + six-layer-cross-validation）
  ├── 质量门禁（research-quality-gate 六维自检）
  └── 深挖引擎（双源判定：nine-layer-deep-dig + research-sats，按需启用）
  ↓
第三层 专项武器库（按需载入，渐进式披露——先跑核心，遇到缺口再调用）
```

## 第一层：OSCAR 意图路由（30 秒，必做）

进入调研先回答五个问题，答案写进调研文档头部：

- **O**bjective（目标）：要验证什么假设？调研结果支撑哪个决策？
- **S**cope（范围）：时间/地域/竞品范围？明确「不包括什么」？
- **C**hecklist（清单）：需要哪些具体信息？拆成 3-5 个可搜索的 query。
- **A**cquire（获取）：用哪些渠道获取？默认 ≥5 个独立渠道（搜索引擎/官方统计/行业报告/新闻/社区/专家）。
- **R**eport（归因）：结论如何输出？每条结论带来源+置信度+行动建议。

> 目标不清直接开工 = 调研事故。发现「了解一下这个行业」这类模糊目标，先追问用户，或按行业报告武器库的 Step 1 从搜索中收敛。

## 硬约束（防捏造铁律，所有调研必守）

- 严禁捏造数据：每条事实必须附可验证的来源 URL，或标注「口述待独立核实」
- 数字/金额/市占率必须回查原始链接核验，不转引二手转述
- 信源时效：AI/监管/融资类 ≤30 天；行业报告 ≤12 个月（超期信源须标注「时效存疑」）
- 核心结论必须 ≥2 个独立来源交叉验证（进纪律 1 执行）

## 第二层：核心纪律（所有调研必经）

### 纪律 1：交叉验证（双源判定）

**合并判定**：`research-cross-validation`（信源层级 L1-L6 + 多重身份）与 `six-layer-cross-validation`（六维验证：来源/时间/逻辑/数据/反例/行动）功能重叠 → 合并为单节点双源。执行时二选一为主、另一为交叉检验：

**最小可执行定义（入口卡内自包含，不必先读子卡）**——信源层级：

| 层级 | 含义 | 处理 |
|:--|:--|:--|
| L1 | 官方文件（财报/监管/政府公告） | 直接采用 |
| L2 | 权威第三方（审计/咨询/学术） | 采用，标注机构 |
| L3 | 多源交叉（≥3 独立来源一致） | 采用，列来源 |
| L4 | 推理验证（逻辑自洽） | 标注「推理」 |
| L5 | 单源参考 | ⚠️ 追加搜索或降级 |
| L6 | 传闻/推测 | 不可用作结论依据 |

- 执行步骤：①列出所有核心结论 ②逐条标 L1-L6 ③L5/L6 追加搜索，找不到则降级标注 ④矛盾处理：标注分歧，不做推测 ⑤输出验证矩阵（结论+来源1+来源2+层级+可信度）
- 铁律：**每条核心结论 ≥2 个独立来源**；关键断言交叉用六维检验（谁说的/什么时候/说得通吗/有数字吗/有反例吗/能指导行动吗）
- 方法细节（多重身份验证、六维操作细节）→ 加载 `research-cross-validation` / `six-layer-cross-validation`

### 纪律 2：质量门禁（research-quality-gate 六维自检）

提交前逐项自检（任一不通过 → 回补后再提交）：

| 维度 | 检查项 | 不合格信号 | 回补动作 |
|:--|:--|:--|:--|
| Objective | 目标一句话说清？对应哪个决策？ | 「了解一下这个行业」 | 回 OSCAR 重定目标（30 分） |
| Scope | 时间/地域/竞品范围明确？声明了不包括？ | 「最近的」无日期 | 补「本次不包括」声明（10 分） |
| Sources | 关键数字 ≥2 独立来源？层级标注？时效遵守？ | 单源结论未标注 | 追加 2 个独立来源（1-2 时） |
| Weapons | 用了几个渠道？标准 ≥5 | 全程只用 WebSearch | 追加 1-2 个渠道（1-4 时） |
| Counter | 找过否定证据？结论最可能错在哪？ | 只有正面论证 | 做一次 Pre-Mortem：假设结论错了，列出最可能的 3 个原因（30 分） |
| Action | 报告能直接支持决策？有立即行动建议？ | 「需要更多研究」结尾 | 加「立即行动」建议（15 分） |

> 门禁细节（每维完整检查项表）→ 加载 `research-quality-gate`。本表为最小自包含版本，BLOCKING：六维全过才交付。

### 纪律 3：深挖引擎（双源判定，按需启用）

**合并判定**：`nine-layer-deep-dig`（九层深挖主框架：业务公式→决策框架）与 `research-sats`（CIA 结构化分析技术：KAC/魔鬼代言人/Red Team/Indicators）功能互补 → 合并为单节点双源。深挖任务默认走 nine-layer；在分析阶段用 SATs 技术增强：

**最小可执行定义（入口卡内自包含）**——九层主流程：

| 层 | 问什么 | 关键动作 |
|:--|:--|:--|
| L1 业务公式 | 收入-成本-毛利-回本模型是什么？ | 建单元模型 |
| L2 假设审计 | 每个数字依据？最敏感数字？ | 标保守/中性/乐观边界 |
| L3 政策边界 | 准入/许可/监管态度？ | 一条可推翻 L1 |
| L4 失败模式（最关键） | 同类项目怎么死的？ | **强制 ≥5 个失败案例**提取共因 |
| L5 隐性成本 | 机会/管理/合规成本？替代方案？ | 列用户所有替代项 |
| L6 执行能力 | 所需能力 vs 可调动资源？ | 人岗对照 |
| L7 市场情绪 | 加盟骗局/躺赚/半年回本信号？ | 主动搜负面信息 |
| L8 边界案例 | 看似能做但不能 / 看似不能但可以？ | 找边界反例 |
| L9 决策框架 | go/no-go 条件？最大风险？最小验证路径？ | 整合输出 |

- SATs 增强点：得出结论后跑 KAC（关键假设检查：列支撑结论的 5-10 条假设→逐条问「不成立会怎样」→🔴 无证据的必须补或修正）；结论「太对了」跑魔鬼代言人（假设结论是错的，构建最强反驳）；预测竞对跑 Red Team（扮演竞对决策者设计最优策略）；持续监控设 Indicators（可观测信号+阈值+检查频率）
- 停止条件：各层无矛盾 / 新信息增量 <10% / L9 完成 / 用户喊停 / 知识库缺口已标注
- 方法细节（SATs 四技术完整模板、九层案例）→ 加载 `nine-layer-deep-dig` / `research-sats`

## 第三层：专项武器库（按需载入）

遇到下列缺口时加载对应武器（渐进式披露第三层；不预先全载，省上下文）：

| 需求信号 | 加载 | 一句话 |
|:--|:--|:--|
| 行业报告/市场规模/赛道 | `research-industry-report` | Doris 四步法+搜索七技，7 天建立行业认知 |
| 上市公司财报/招股书 | `research-financial-report` | 财报深度解读，数字必须来自原始报告 |
| 专家访谈 | `research-expert-interview` | 黄金十步法，2 小时获取行业共识 |
| 替代数据（Trends/卫星/信用卡） | `research-alt-data` | 免费层到百万级按预算分级 |
| OSINT 工具链 | `research-osint` | SpiderFoot/Shodan/Sherlock/Wayback |
| 全网爬虫采集 | `research-web-scraping` | 10 大工具+合规红线 |
| 高级搜索/域名情报 | `research-google-dorking` | Google Dorking+DNS/SSL 零成本挖信息 |
| 图片/视频真伪 | `research-media-verification` | 反向搜索→元数据→天气阴影验证 |
| 复杂任务分工 | `research-multi-agent` | 四种多 Agent 架构，Pipeline+OSCAR 首选 |
| 持续监控竞对 | `research-ci-framework` | CI 循环 Define→Gather→Analyze→Implement |

## KDO 工具链（KDO 环境内可选加速）

KDO 环境内用已适配工具执行搜索与校验（输出 JSON 可直接写入调研文档）；非 KDO 环境用各 agent 自带 web_search：

1. **OSCAR 第一轮搜索**（按 Checklist 自动拆 query）：
   ```bash
   python kdo-tools/research_adapter.py oscar --objective "验证某假设" --scope "2024-2026, 中国" --checklist "市场规模,竞品定价,渠道结构" --json
   ```
2. **单点/多 query 搜索**：
   ```bash
   python kdo-tools/research_adapter.py search "query1" "query2" --json
   ```
3. **报告 P0 质量门自检**（纪律 2 的机械检查层）：
   ```bash
   python kdo-tools/research_adapter.py validate report.md --json
   ```

## 快速执行路径（基础调研，30-45 分钟）

1. **OSCAR 定目标**（第一层）：写 O/S/C 三行到文档头
2. **首轮搜索**：按 Checklist 拆 3-5 个 query 搜索，收集 ≥5 个独立渠道素材（渠道不足 → 加载爬虫/Dorking/OSINT 补）
3. **交叉验证**（纪律 1）：核心结论逐条标信源层级，L5/L6 追加搜索；≥2 独立来源
4. **深挖**（纪律 3，按需）：关键假设跑 KAC；找 ≥1 个反例；矛盾处标注
5. **质量门禁**（纪律 2）：六维自检，不合格回补
6. **输出**：结论 + 来源列表 + 置信度标注 + 立即行动建议

## 失败模式表

| 症状 | 根因 | 修复 |
|:--|:--|:--|
| 调研报告全是单源观点 | 跳过交叉验证 | 逐条回标 L1-L6，单源标 ⚠️ |
| 数据前后矛盾不自知 | 未做对立面检验 | 跑一次 Pre-Mortem，找反例 |
| 目标模糊产出一堆信息 | 跳过 OSCAR | 回 Step 1，先定 O/S/C |
| 深挖变成凑层数 | 无真实失败案例支撑 | 强制 ≥5 个失败案例（L4） |
| 武器库滥用（杀鸡用牛刀） | 未走意图路由直接跳武器 | 先走第一层，按需求信号载入 |

## 适用边界

- ✅ 本层是**入口+纪律层**：具体执行细节在对应武器库 skill 里，按需加载
- ✅ 所有角色通用（基础能力层语义：任何 agent 生产前可调用）
- ❌ 不做业务决策（调研产出决策素材，决策归用户/业务方）
- ❌ 不替代内容生产（调研完的写作走 content-production 产线）
- ❌ 非调研任务不得路由进本层（见触发条件反触发）

## 相关 wiki 卡片

- `framework-yitang-oscar-research` — OSCAR 五步法（第一层依据）
- `business-research-skill-oscar-13-weapon-system` — OSCAR + 13 武器体系总览
- `framework-yitang-six-layer-cross-validation` — 六层交叉验证（纪律 1 依据）
- `framework-yitang-nine-layer-deep-dig` — 九层深挖法（纪律 3 依据）
- `framework-yitang-research-quality-gate` — 质量门禁（纪律 2 依据）
