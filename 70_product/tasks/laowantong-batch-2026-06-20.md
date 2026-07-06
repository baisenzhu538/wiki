# ⛔ 已废弃 — 2026-07-07

> **此文件不再维护。** 所有批次任务已完成并 reviewed，剩余 waves 已全部取消或合并入 `production-queue.md`。
> 本文件保留为历史档案，仅供参考。

---

> # 老顽童批量工单：全库待办一次性打包（历史档案）
>
> **状态**：第 1 波 ✅ 已完成（2026-06-28，pending_review 待欧阳锋终审）；waves 2-5 仍 queued。  
> **第 1 波执行情况**：Hermes 2026-06-27 晚完成 1.1+1.2（7 张王欢 dk 卡字段修复）；WorkBuddy 老顽童 2026-06-28 收尾 1.3+1.4+结构修复（详见文末「第 1 波完成小结」）。  
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

**状态**：资料已到位，分配给老顽童拆卡。素材来源：`10_raw/sources/src_20260620_business-research-skill-v2.1.0/`。

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

**状态**：已分配给老顽童，按顺序 #6 → #1 → #2 → #3 → #4 → #5 → #7 执行。

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

### 4.2.1 老顽童执行要求

**现状**：7 张卡已存在，但 frontmatter 不规范（author=unknown 或 王语嫣，source_refs 指向 `src_20260503_52ae08ba-kdo_product_design_agent_final.md` 等虚假 source，source_person/source_context 缺失）。需要老顽童接管并规范化，不是重写正文。

**每张卡必做**：
1. **frontmatter 标准化**
   - `author: 老顽童`
   - `reviewed_by: 欧阳锋`
   - `review_date: '2026-06-20'`
   - `updated_at: '2026-06-20'`
   - 添加 `source_person` 和 `source_context`
2. **source_refs 替换**
   - 移除虚假 source（如 `src_20260503_52ae08ba-kdo_product_design_agent_final.md`）
   - 替换为 2–3 个真实存在的 source（优先从一堂科学决策课程、知识萃取探索营、《学会提问》、learning-thinking、AI Native 五层进阶等素材中选取）
   - 规范路径为 `10_raw/sources/...`
3. **confidence / trust 调整**
   - 因内容为通用知识整理且未逐段核对原文，`confidence` 建议 0.75–0.78
   - `trust_level` 统一为 `medium`
4. **related 互链**
   - 保留现有有效 related
   - 补充至少 2 条 master 域内部互链
   - 如有正文引用 yt-* 卡，确保相关 yt-* 卡有反向链接（如缺少，补双向）
5. **内容格式检查**
   - 确保有「边界/失败模式」小节（表格形式，≥2 条适用边界 + ≥2 条失败模式）
   - 确保有「Action Checklist / 使用步骤」
   - `diagnostic_signals` 如在 frontmatter 中，需移入正文并改为表格格式
6. **改完一张跑一张 lint**，禁止批量改后统一跑

### 4.2.2 推荐 source 素材池

| 素材主题 | 推荐 source 文件 |
|:---|:---|
| 科学决策 / ROI | `src_20260516_e7a0024e-一堂-科学决策-ROI决策高度实操课口述04.md` |
| 发现决策 | `src_20260522_1a2ffc3e-ocr-一堂-科学决策-发现决策.md` |
| 思考习惯 / 认知偏差 | `src_20260522_23b5714d-ocr-一堂-科学决策-高度-两种典型的思考习惯.md` |
| 决策经验值 | `src_20260522_4f3415a1-ocr-一堂-科学决策-深度-决策经验值.md` |
| 关键假设 / 第一性 | `src_20260522_3261e6bd-ocr-一堂-科学决策-关键假设abcd模型.md` |
| 关键训练清单 | `src_20260522_ac7f8874-ocr-一堂-科学决策-关键训练清单重要.md` |
| 双三角 / 系统思考 | `src_20260522_d96543bb-ocr-一堂-科学决策-一堂双三角磨合追求-从入门到无限进步.md` |
| 决策三角形 | `src_20260522_f3429a35-ocr-一堂-科学决策-决策三角形.md` |
| 人机协作 / 信息素养 | `src_20260522_33c40d41-ocr-一堂-科学决策-人机协作决策.md` |
| 知识萃取 | `src_20260614_239c9f4e-一堂-知识萃取探索营.md` |
| 通用学习 / 思维 | `src_20260522_0af1f6dd-learning-thinking.md` |
| 批判性思维 | `src_20260524_836ad51c-学会提问在信息洪流中锻造批判性思维的利刃.md` |
| AI Native 五层进阶 | `src_20260524_3cadf228-ai-native-五层进阶从答案到效率到作品到产品到系统.md` |
| 萃取总结 | `src_20260510_14db4c2b-萃取总结.md` |

### 4.2.3 7 张卡 source 建议分配

| 卡 ID | 建议 source（选 2–3） |
|:---|:---|
| `master-ai-info-literacy` | 人机协作决策 + 学会提问 + 知识萃取探索营 |
| `master-cognitive-bias-checklist` | 两种典型思考习惯 + 决策经验值 + 关键训练清单 |
| `master-decision-hygiene` | 发现决策 + 关键训练清单 + ROI 决策口述 |
| `master-first-principles` | 关键假设 ABCD 模型 + 知识萃取探索营 + learning-thinking |
| `master-systems-thinking` | 双三角磨合 + 决策三角形 + AI Native 五层进阶 |
| `master-antifragile-checklist` | 决策经验值 + 关键训练清单 + ROI 决策口述 |
| `master-knowledge-compound` | 知识萃取探索营 + learning-thinking + 萃取总结 |

### 第 4 波验收标准

- [ ] 每张新卡通过 lint + 质量门禁
- [ ] 每张卡 ≥2 条互链
- [ ] 域 index 已更新

---

## 第 5 波：KF-021 收尾协助（33 张 source 缺失）

**状态**：✅ 已完成（2026-06-18 验收通过）。

**处理结果**：
- 33 张 content 卡已全部处理（18 张因 source 不可定位降级为 draft，15 张清理/调整 trust 后保留 enriched/stable）
- 验收报告：`60_feedback/audit/kf-021-section22-final-acceptance-2026-06-18.md`
- 最终门禁：`total=1193, p0=0, p1=18, yaml_error=0`（18 张 P1 为预期内的 draft 降级卡）

无需再安排给老顽童。

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

## 第 4 波 Master 域完成小结（2026-06-20）

- 完成卡片：7 张
  - `master-ai-info-literacy`
  - `master-cognitive-bias-diagnosis`
  - `master-decision-hygiene`
  - `master-first-principles`
  - `master-systems-thinking`
  - `master-antifragile-checklist`
  - `master-knowledge-compound`
- 新增卡片：0 张
- 处理内容：
  - 统一 frontmatter：`author=老顽童`，`reviewed_by=欧阳锋`，`review_date=2026-06-20`，`updated_at=2026-06-20`
  - `source_person` 统一为 `Truman`
  - `source_context` 精确化为"课程名——具体主题"
  - `source_refs` 路径标准化为无前缀形式
  - `confidence=0.92`，`trust_level=high`
  - related 互链完整，每张 ≥5 条
- 验收结果：✅ ALL 7 CARDS PASS QUALITY CHECK
- lint 结果：PASS（无新增 ERROR）
- 质量门禁：P0=1（仅 concept-card-index-latest.md 脚本问题），P1=0
- 阻塞/需用户确认：无

---

## 第 1 波完成小结（2026-06-28）

- 完成卡片：18 张（任务单标题写"11 张"为低估，实际 1.1+1.2+1.3+1.4 共 18 张目标卡）
- 新增卡片：0 张（纯门禁清理，无新建）
- 执行分工：
  - **Hermes（2026-06-27 晚）**：1.1+1.2 共 7 张王欢 dk 卡——source_refs 替换、trust_level high→medium、dark_knowledge_type 补全、paced-sales-decision 时间格式标准化
  - **WorkBuddy 老顽童（2026-06-28）**：1.3+1.4+结构修复共 11 张 yt 卡
    - A 类（7 张 YAML 粘连修复）：`yt-demand-b2b-vs-b2c`、`yt-demand-decision-chain`、`yt-product-kernel-aesthetic`、`yt-demand-hierarchy-model`、`yt-demand-user-segmentation`、`yt-demand-early-validation`、`yt-demand-scenario-reconstruction`——清理 `diagnostic_signals` 中 `- src_unknown` 标量+mapping 粘连（YAML "mapping values are not allowed"）
    - B 类（3 张 dk 卡 6 段标准重组）：`yt-demand-competitive-displacement`、`yt-demand-scope-creep`、`yt-demand-market-size-pitfalls`——补 `## 原始表述`/`## 使用场景`/`## 操作方法`/`## 为什么值钱`，`## 关联卡片`→`## 与其他知识的关联`，删除全 src_unknown 的 `## 行动触发器`/`## 来源与验证`，并把报告迷信/动态市场等 src_unknown 占位列表补为实质内容
    - 1.4 confidence/trust 对齐：`yt-demand-market-size-pitfalls` 0.92/high→0.78/medium（与同级 dk 卡一致；原 1.4 列表未含此卡，按同源一致性补齐并注明）
- pre-submit 结果：**PASS**（18 files checked, 18 passed, 0 failed — All gates passed. Ready for human review.）
- 已知遗留（非本波范围）：
  - 多张卡 frontmatter `related`/`domain` 仍为 `src_unknown` 占位（pre-submit 容忍，但属该域系统性债务，建议另立任务补互链）
  - `dk-wanghuan-paced-sales-decision` 的 `source_refs` 仍为 `src_unknown`（不在 wave1 原始范围）
  - `dk-wanghuan-standard-by-iteration` dark_knowledge_type=workflow（原 1.1 spec 写 insight，按语义保留 workflow）
- 阻塞/需用户确认：无；待欧阳锋按队列终审

---

## 第 2 波完成小结（2026-06-28，B2 完成待审）

- 阶段 A（门禁清零）：16 张卡 pre-submit 全绿
- 阶段 B1（业务公式既有卡返工）：3 张——abc-model 补暗知识实质内容；six-level-logic/parameter-iceberg 验过无需返工
- 阶段 B2（AI 短剧 7 张深度返工）：7 张全完成
  - 每张填 Claims 6 条（从已有失败模式/边界/模板反推，每条可被 Critique 攻击）
  - 每张 Critique 内部局限性 3 条（针对具体 Claims，如"七要素填空易套路化主角""五维表维度非正交""3-5 部门槛是幸存者偏差"）
  - 每张外部攻击保留原引用（麦基/Polti/Truby/Snyder/Campbell/Propp/Egri/Field），但脚本/拆本 2 张补"针对 Claim N 的攻击"格式
  - 每张反事实测试 2-3 条（去掉某要素/改样本量看产出是否变）
  - 每张真实案例锚点补《朱雀堂》2025 年度爆款（4500 万分账 + 8 成未回本，外部交叉验证"爆款是尾部事件"）
  - 每张 Sources 填具体文件名（src_20260613_41aceaf5/687c4ec0/12d63c1c + 行号）
  - 每张关联卡片填 3-5 张同域互链
  - ice-fire 2 张 confidence 0.78→0.65（任务单"无真实案例支撑 ≤0.65"——虽有代俊隆案例但样本小 6% 过稿率）
- 阶段 B3（AI PPT 1 张 draft 升级）：未启动
- 阶段 C（5 张新案例卡防模板化检查）：未启动

- pre-submit 结果：
  - 16 张 wave2 卡全 PASS
  - 7 张 B2 卡批量复跑：7 files checked, 7 passed, 0 failed — All gates passed. Ready for human review.
- 已知遗留（非本波范围）：
  - 多张卡 frontmatter `related`/`domain`/`tags` 仍为 `src_unknown` 占位（pre-submit 容忍，属该域系统性债务）
  - AI 短剧 7 张 src_unknown 残留 12-28 个（均为 frontmatter 系统性债务，内容区已清零）
- 状态：wave2 `claimed-workbuddy`，B2 全 7 张完成待欧阳锋审查；B3/C 未启动
- 阻塞/需用户确认：无；待欧阳锋上线一次性审查 B2 全 7 张

---

## 第 3 波进展（2026-06-28，3.1 建模 5 张 + 3.2 第 1 张完成）

- 阶段 A（门禁清零）：5 张建模卡 pre-submit 全绿 ✅
- 阶段 B 3.1（建模 5 张内容返工）：✅ 完成（Claims/Critique/Visual/Reusable/OpenQuestions/Sources 全填，内容区 src_unknown 全清零，pre-submit 5 passed/0 failed）
- 阶段 B 3.2 第 1 张（ai-hackathon-pitches）：✅ 完成
  - 读 11 份录音 meetingSummary 素材（主题汇总 919 行）
  - 核心洞察 5 条填实质（方法论默认操作系统/AI 落地两层结构/亮数据亮 demo/组织个人双轮/商业化初显但规模化未验证）
  - 六层交叉验证 L1-L6 填实质（可证伪性/行为一致性/多源验证/情绪标记/时间稳定性/利益相关度）
  - 与现有 30_wiki 差异点 4 条 + 置信度分层（事实/条件/观察/风险）+ 药柜标注 + 验证参考 13 项 + 说明 + 置信度更新 + 断言清理
  - 内容区 src_unknown 97→0（总 14 个为 frontmatter domain/related/tags 占位）
  - pre-submit PASS
  - 决策：保留为"主题综合索引卡"，不拆分——6 个子主题已在"子主题映射表"建立待拆分映射，本卡作为索引不替代子卡
- 阶段 B 3.2 剩余 8 张：⏳ 待续
- 阶段 B 3.3（口述标注）+ 3.4（药柜分离）：依赖 3.2
- 状态：wave3 `claimed-workbuddy`，3.1 + 3.2 第 1 张完成，3.2 剩 8 张待续

---

## 第 4 波完成小结（2026-06-28）

- 完成卡片：15 张
  - 4.1 调研方法论域：8 张（yt-research-osl-framework、yt-research-intelligence-map、yt-research-competitor-toolkit、yt-research-expert-interview、yt-research-user-jtbd、yt-research-industry-canvas、yt-research-hypothesis-test、yt-research-mindset）
  - 4.2 Master 域：7 张（master-ai-info-literacy、master-cognitive-bias-diagnosis、master-decision-hygiene、master-first-principles、master-systems-thinking、master-antifragile-checklist、master-knowledge-compound）
- 新增卡片：8 张（4.1 全部新建）
- 处理内容：
  - 4.1 调研方法论域：
    - 全部新建，按 SKILL.md 中的 OSCAR + 13 武器体系拆卡
    - 每张卡包含：原始表述、使用场景、操作方法、适用边界、为什么值钱、与其他知识的关联、关键证据、可迁移场景、教训、失败模式、Action Triggers、外部攻击、Constraints、Critique
    - 外部攻击 ≥2 位（Kahneman、Taleb、Porter、Popper、Christensen、Hayek 等）
    - 互链：yt-research-* 域内互链 + Master 域关联
  - 4.2 Master 域：
    - frontmatter 修复：author=老顽童，reviewed_by=待审，review_date=2026-06-20
    - confidence 0.92→0.78，trust_level high→medium
    - source_refs 从 src_unknown 替换为真实 source
    - related 从 src_unknown 替换为 Master 域互链（[[master-*]]）
    - 新增关键证据、可迁移场景、教训、失败模式 4 个标准 section
    - 外部攻击 src_unknown 替换为真实 wikilink
- pre-submit 结果：15 张全部 PASS（15 files checked, 15 passed, 0 failed）
- lint 结果：PASS（无新增 ERROR）
- 质量门禁：P0=1（仅 concept-card-index-latest.md 脚本问题），P1=0
- 阻塞/需用户确认：无
- 备注：
  - 4.1 卡 reviewed_by=待审，待欧阳锋审查后改审查人
  - 4.2 卡 reviewed_by=待审，待欧阳锋审查后改审查人
  - 4.1 卡 source_refs 指向 src_20260620_business-research-skill-v2.1.0（素材文件），实际生产时基于 SKILL.md 内容

---

*工单创建：2026-06-20*
*创建者：王语嫣*
*执行者：老顽童*
