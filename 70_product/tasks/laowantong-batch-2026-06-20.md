> # 老顽童批量工单：全库待办一次性打包
>
> **状态**：已领取，按波次执行  
> **来源**：王语嫣 2026-06-20 全库待办梳理 + 2026-06-14 深度审计报告 + parking-lot PL-012  
> **总目标**：把老顽童能修的问题一次性修完，先清门禁、再做深度返工、最后新域建设。

---

## 执行原则

1. **按波次顺序执行，做完一波再开下一波。**
2. **每张卡改完立即跑 lint，每波结束跑 `kcard-quality-gate.py`。**
3. **遇到不确定的 source/数字/边界，先标注待验证，不要硬编。**
4. **所有产出卡必须包含：一句话讲清楚、核心洞察、边界/失败模式表、Action Checklist、≥2 条互链。**
5. **改完一张更新 `updated_at`，新卡写 `created_at`。**

---

## 第 1 波：门禁快速清理（11 张卡，预计 30–60 分钟）

**目标**：让 `kcard-quality-gate.py` 的 P0/P1 归零（除 `concept-card-index-latest.md` 需黄药师修脚本外）。

### 1.1 王欢域 dk 卡 source_refs + trust_level + dark_knowledge_type（4 张）

| 卡片 | 修复动作 |
|:---|:---|
| `dk-wanghuan-ai-lifts-personal-ceiling.md` | ① source_refs 改为 `10_raw/sources/src_20260619_536bca67_wanghuan_actor_director_oral.txt` + `10_raw/sources/src_20260619_a3a2a803_wanghuan_actor_director_notes.txt`<br>② trust_level: high → medium<br>③ 添加 `dark_knowledge_type: insight` |
| `dk-wanghuan-creativity-in-description-and-taste.md` | 同上 |
| `dk-wanghuan-output-equals-standard-times-iteration.md` | 同上 |
| `dk-wanghuan-standard-by-iteration.md` | 同上 |

### 1.2 王欢域 dk 卡缺 dark_knowledge_type + 时间格式（3 张）

| 卡片 | 修复动作 |
|:---|:---|
| `dk-wanghuan-magic-defeats-magic.md` | 添加 `dark_knowledge_type: workflow` |
| `dk-wanghuan-spec-trap.md` | 添加 `dark_knowledge_type: insight` |
| `dk-wanghuan-paced-sales-decision.md` | ① 添加 `dark_knowledge_type: insight`<br>② `created_at: '2026-06-19T10:02:33+00:00'` → `'2026-06-19'`<br>③ `review_date: '2026-06-19T10:02:33+00:00'` → `'2026-06-19'` |

### 1.3 yt-域 dangling 链接修复（3 张）

| 卡片 | 修复动作 |
|:---|:---|
| `concepts/yt-demand-b2b-vs-b2c.md` | 从 `related` 中移除 `xujian-tob-fivestep-oral`（source_refs 已引用） |
| `frameworks/yt-demand-decision-chain.md` | 从 `related` 中移除 `xujian-tob-fivestep-oral` |
| `concepts/yt-product-kernel-aesthetic.md` | `yt-model-pan-product-aesthetic-progression` → `yt-model-aesthetic-progression` |

### 1.4 yt-域 confidence/trust 不匹配（8 张）

| 卡片 | 修复动作 |
|:---|:---|
| `concepts/yt-demand-hierarchy-model.md` | trust_level: high → medium；confidence 0.92 → 0.78 |
| `concepts/yt-demand-user-segmentation.md` | 同上 |
| `dark-knowledges/yt-demand-competitive-displacement.md` | 同上 |
| `dark-knowledges/yt-demand-fake-demand-detection.md` | 同上 |
| `dark-knowledges/yt-demand-scope-creep.md` | 同上 |
| `frameworks/yt-demand-early-validation.md` | 同上 |
| `frameworks/yt-demand-scenario-reconstruction.md` | 同上 |

> 注：`dark-knowledges/yt-demand-market-size-pitfalls.md` 虽在 lint 中缺 `dark_knowledge_type`，但不触发 P1，本轮一起补 `dark_knowledge_type: insight`。

### 第 1 波验收标准

- [ ] `kcard-quality-gate.py` 运行后 P0=1（只剩 concept-card-index-latest.md 脚本问题）、P1=0
- [ ] `kdo_lint.py 30_wiki/dark-knowledges` 中，本轮目标卡无新增 ERROR
- [ ] 每卡改完单独跑 lint，无 ERROR

---

## 第 2 波：P0 返工（13 张卡，核心）

**来源**：`60_feedback/issues/fb_20260614_9e5a2c8b-老顽童业务公式域工作深度审计.md`、`60_feedback/issues/kcard-laowantong-cross-domain-depth-audit-2026-06-14.md`

### 2.1 业务公式域返工（6 张既有卡 + 5 张新案例卡）

#### 新案例卡（5 张）

| 新卡 ID | 来源素材 | 核心案例 |
|:---|:---|:---|
| `case-private-domain-ecommerce-formula.md` | 业务公式逐字稿 | 10W 人社群月 GMV 100 万，人均贡献低 |
| `case-saas-renewal-formula.md` | 业务公式逐字稿 | 续费率 50% vs 竞对 80%，客户没用起来 |
| `case-dental-clinic-formula.md` | 业务公式逐字稿 | 月接诊 2000 人成交率 30%，危机感知不足 |
| `case-offline-catering-formula.md` | 业务公式逐字稿 | 同店增长 30% 的会员复购盲区 |
| `case-gym-membership-formula.md` | 业务公式逐字稿 | 续卡率 35%→50%，关键是到店习惯而非满意度 |

每张案例卡标准：
- 原始表述/背景
- 问题
- 方案（用 ABC/六层逻辑/十大范式中的哪个框架拆解）
- 结果/数据（标注口述待验证）
- 可迁移点
- 关联已有业务公式卡

#### 既有卡补充暗知识/自检清单（3 张）

| 卡片 | 补充内容 |
|:---|:---|
| `yt-business-formula-abc-model.md` | 增加“暗知识”小节：① 加法 vs 乘法业务含义 ② 先切分再拆转化顺序 ③ 相关 vs 因果判断方法 |
| `yt-business-formula-six-level-logic.md` | 增加“自检清单”：当前业务应拆到哪一层、每个定性参数是否找到 3-5 个行为指标、公式是否可验证可执行 |
| `yt-business-formula-parameter-iceberg.md` | 同上，或增加 L5-L6 停止条件：能否提出可验证假设 |

### 2.2 AI 短剧域返工（7 张卡）

| 卡片 | 返工重点 |
|:---|:---|
| `ai-short-drama-ice-fire-scripting-compass.md` | 补充 1-2 个真实爆款短剧案例；source 精确到逐字稿段落；Critique 针对具体 Claims 而非套模板 |
| `ai-short-drama-ice-fire-dissection-compass.md` | 同上；明确“冰火”拆解的实际操作示例 |
| `ai-short-drama-plot-three-axes.md` | 补充真实短剧的三轴分析示例；source 精确 |
| `ai-short-drama-script-planning-three-axes.md` | 同上 |
| `ai-short-drama-framework-three-axes.md` | 同上 |
| `ai-short-drama-conflict-three-axes.md` | 同上 |
| `ai-short-drama-platform-policy-comparison.md` | 补充平台真实政策条款来源；标注政策版本日期 |

返工标准：
- 每张卡至少 1 个真实短剧案例或 1 个真实数据锚点
- source 精确到具体文件/段落
- 降低 confidence：无真实案例支撑的工具卡 confidence ≤ 0.65
- Critique 必须针对本卡具体 Claims，禁止泛泛引用麦基/坎贝尔

### 2.3 AI PPT 工具卡重写（1 张）

| 卡片 | 返工重点 |
|:---|:---|
| `tools/yt-tool-ai-ppt-maker.md` | ① 从 draft 升级为标准 tool 卡<br>② 补充精确 source 引用<br>③ 验证 Critique 中名人引用真实性<br>④ 补充真实使用案例和失败教训 |

### 第 2 波验收标准

- [ ] 5 张新案例卡通过 lint + 质量门禁
- [ ] 9 张既有卡更新后 lint + 质量门禁无 P0/P1
- [ ] 每张卡新增/修改内容有明确 source 支撑
- [ ] 王语嫣/欧阳锋可抽样审查 3 张，无明显模板化痕迹

---

## 第 3 波：P1 返工（14 张卡 + 2 项清理）

### 3.1 建模能力域补充案例（5 张）

| 卡片 | 补充重点 |
|:---|:---|
| `modeling-capability-system.md` | 补充 1-2 个 Truman 课程中的具体建模案例；增加 Critique |
| `modeling-three-stages.md` | 为流程建模→抽象建模→本质提炼每阶段配 1 个案例 |
| `modeling-level-map.md` | 补充 C5 推断的 source；明确自评标准使用步骤 |
| `modeling-weapon-library.md` | 为代表性模型（清单、雷达图、冰山图）补充使用步骤、典型场景、常见错误 |
| `process-modeling.md` | 补充失败教训案例 |

### 3.2 王语嫣综合卡格式转换（9 张）

| 卡片 | 处理方式 |
|:---|:---|
| `ai-hackathon-pitches.md` | 拆分为 concept 卡或建立子卡映射 |
| `business-validation-models-collaboration.md` | 同上 |
| `finance-legal-business-operations.md` | 同上；先剥离药柜/医疗内容 |
| `industry-ai-cases.md` | 同上 |
| `personal-growth-complex-systems.md` | 同上 |
| `product-business-strategy.md` | 同上；先剥离药柜/医疗内容 |
| `supply-chain-beverage.md` | 同上 |
| `yitang-methodology-system.md` | 同上 |
| `ai-methodology-tools.md` | 同上 |

处理原则：
- 优先把主题综合草稿转换为标准 30_wiki 概念/框架/工具卡
- 若一张卡跨度过大，拆分为多张子卡，并在原卡中建立映射
- 所有口述数据标注“未验证口述数据”
- 药柜/医疗片段剥离后移入 `60_feedback/pending-wiki-cards/` 或新建药柜域卡

### 3.3 口述数据独立验证标注

对所有零散域综合卡中的数字型断言：
- 来源为口述/项目方自述的，加注 `> 来源：...，数字待独立核实`
- 优先寻找第三方公开数据交叉验证（不强求，找不到就标注待核实）

### 3.4 药柜/医疗内容分离

确保以下卡中的药柜/医疗片段已剥离：
- `finance-legal-business-operations.md`
- `product-business-strategy.md`
- `ai-methodology-tools.md`
- `yitang-methodology-system.md`

剥离后的内容写入 `60_feedback/pending-wiki-cards/` 对应药柜队列，或新建 `smart-medicine-cabinet-*` 卡。

### 第 3 波验收标准

- [ ] 5 张建模卡均有新增案例或失败教训
- [ ] 9 张综合卡转换为标准格式或建立清晰子卡映射
- [ ] 所有口述数字已标注验证状态
- [ ] 药柜/医疗污染内容已剥离并登记
- [ ] 全库 lint + 质量门禁无新增 P0/P1

---

## 第 4 波：新域建设（15 张卡，需审批后启动）

### 4.1 调研方法论域（8 张卡）

**前置条件**：`proposal-next-domain-research.md` 获 @欧阳锋 审批。

| 卡 ID | 类型 | 标题 |
|:---|:---:|:---|
| `yt-research-osl-framework` | framework | OSL调研五步法：一堂通用商业调研框架 |
| `yt-research-intelligence-map` | framework | 情报获取全景地图：13+渠道穷尽手段 |
| `yt-research-competitor-toolkit` | tool | 竞品拆解工具包：三层分类+内核边界+单元模型对标 |
| `yt-research-expert-interview` | tool | 专家访谈工具：2小时获取行业共识的标准流程 |
| `yt-research-user-jtbd` | tool | 用户深度访谈工具：JTBD视角区分“说的”和“真正要的” |
| `yt-research-industry-canvas` | tool | 行业分析画布：五维快速扫描+二维定位 |
| `yt-research-hypothesis-test` | tool | 假设验证调研工具：关键假设→可证伪问题→最小实验 |
| `yt-research-mindset` | concept | 调研认知升级：从“原创自信”到“情报驱动” |

素材来源：
- `00_inbox/ideas/一堂-创业必修-调研武器库.md`
- `00_inbox/ideas/一堂-创业必修-调研行动营.md`
- `00_inbox/ideas/一堂-创业-调研行动营口述01.md`
- `00_inbox/ideas/一堂-创业必修-需求分析.md`
- 已有 `yt-research-action-camp-launch.md`、`yt-research-weaponry-course.md`

### 4.2 Master 域 7 张卡

**前置条件**：确认分配给老顽童（当前 `master-7-cards-layer-and-boundary.md` 未明确分配）。

| 序号 | 卡 ID | 标题 |
|:---:|:---|:---|
| #6 | `master-ai-info-literacy` | AI 信息素养框架 |
| #1 | `master-cognitive-bias-diagnosis` | 认知偏差快速诊断清单 |
| #2 | `master-decision-hygiene` | 决策卫生五步法 |
| #3 | `master-first-principles` | 第一性原理 |
| #4 | `master-systems-thinking` | 系统思考 |
| #5 | `master-antifragile-checklist` | 反脆弱决策检查清单 |
| #7 | `master-knowledge-compound` | 知识复利 |

写卡顺序：#6 → #1 → #2 → #3 → #4 → #5 → #7。

### 第 4 波验收标准

- [ ] 每张新卡通过 lint + 质量门禁
- [ ] 每张卡 ≥2 条互链
- [ ] 域 index 已更新

---

## 第 5 波：KF-021 收尾协助（33 张 source 缺失）

**来源**：parking-lot PL-012。

**角色**：王语嫣牵头，老顽童协助补充证据链，黄药师协助 source 注册表基础设施。

**老顽童任务**：
- 从王语嫣提供的 33 张卡清单中，认领自己熟悉/产出的卡片
- 为每张卡补充 `source_refs`，规范为 `10_raw/sources/` 下相对路径
- 无法追溯的 source 留空，并将 confidence 控制在 ≤0.89
- 协助验证 source 注册表中是否存在对应条目

**前置条件**：等待王语嫣提供 33 张卡的具体清单和分工。

---

## 全局验收标准

1. `kcard-quality-gate.py`：P0=1（仅 concept-card-index-latest.md 脚本问题）、P1=0
2. `kdo_lint.py 30_wiki`：本轮目标卡无 ERROR
3. 王欢域所有 dk 卡有 `dark_knowledge_type`
4. 审计报告 P0/P1 项全部处理完毕
5. 新域建设卡片已入域 index

---

## 严禁事项

- ❌ 不要批量改卡后统一跑 lint——改一张跑一张
- ❌ 不要编造 source 或数字——找不到就标“待验证”
- ❌ 不要把策略和话术/表达混存在同一个文件
- ❌ 不要写“步骤跳过→严格按步骤执行”这种模板化失败模式
- ❌ 不要在新卡里用王语嫣/欧阳锋作为 author（老顽童是 author，reviewed_by 才写欧阳锋）
- ❌ 不要动 `concept-card-index-latest.md` 的 P0 问题——那是黄药师的脚本问题

---

## 本工单完成小结模板

每波完成后在此文件末尾追加：

```markdown
## 第 X 波完成小结（2026-06-XX）

- 完成卡片：N 张
- 新增卡片：M 张
- lint 结果：PASS / FAIL（如有 FAIL 列卡 ID）
- 质量门禁：P0=?, P1=?
- 阻塞/需用户确认：...
```

---

## 第 3 波完成小结（2026-06-20）

- 完成卡片：16 张
  - 建模能力域：5 张（modeling-capability-system、modeling-three-stages、modeling-level-map、modeling-weapon-library、process-modeling）
  - 王语嫣综合卡：9 张（concepts/ 下 8 张 + frameworks/ai-methodology-tools）
  - 药柜/医疗剥离登记：2 个 pending 文件
- 新增卡片：2 个 pending 文件
  - `60_feedback/pending-wiki-cards/pending-medicinal-food-ecommerce-2026-06-20.md`
  - `60_feedback/pending-wiki-cards/pending-smart-city-medical-2026-06-20.md`
- lint 结果：PASS（本轮目标卡无新增 ERROR；全库剩余 2 个 ERROR 为文件名乱码卡的 updated_at 格式问题，不在本轮范围）
- 质量门禁：P0=1（仅 concept-card-index-latest.md 脚本问题），P1=0
- 阻塞/需用户确认：无
- 备注：
  - 9 张综合卡已统一 frontmatter（author=老顽童，reviewed_by=欧阳锋，review_date=2026-06-20）。
  - 所有综合卡已补充子主题映射表、口述数据标注。
  - 药柜/医疗内容已剥离并登记至 pending-wiki-cards。

---

*工单创建：2026-06-20*  
*创建者：王语嫣*  
*执行者：老顽童*
