---
id: 551
assignee: laowantong
status: pending_review
updated_at: '2026-08-26T17:41:58.180369+00:00'
version: v0.1
instance: laowantong
code_files: []
---

# #551 审计判词库卡：13 条判词落 30_wiki/frameworks/（认知闭环补接）

- **任务号**：#551
- **状态**：queued
- **assignee**：laowantong（欧阳锋终审）
- **优先级**：P1（老朱 08-27 拍板「可以迭代任务」；老朱 08-26 点破的缺口：审计认知资产未沉淀）
- **立项**：2026-08-27 王语嫣（风清扬建议书 diag_20260826_fengqingyang-audit-maxims-library 裁定落地——形态裁决执行）

## 素材

- 唯一底本：`60_feedback/diagnosis/diag_20260826_fengqingyang-audit-maxims-library.md`（13 条判词全文+实证出处+适用边界，内容 95% 现成——本单=框架卡结构化，不是再创作）

## 卡片规格

- **id**：`framework-audit-maxims-library`
- **type**：framework ｜ **位置**：`30_wiki/frameworks/`
- **confidence**：0.85（内部制度提炼，全部判词有实证出处）｜ **trust_level**：medium（v0.1 首版，随审计实践迭代）
- **定位声明**（正文开头，#199 门禁硬要求）：属审查/治理方法论域——与 #433 族门禁词表的关系：**本卡=认知层单一真相源，门禁词表=实现层从判词提取**，词表变更须引用判词编号；与 charter §3.16/§3.17 的关系：A1/C2 已入宪，本卡是入宪判词的完整版+边界说明
- **source_refs**：建议书文件 + 抽查可回链的实证出处（#432/#433/#514/#444 任务单路径）
- **结构**：A 组（审计判词 6）/B 组（跨角色方法论 5）/C 组（自动化治理判词 2）——每条=判词+实证出处+适用边界三字段，不加戏不缩水
- **KF-024 三要件**（F-038 门禁）：Synthesis + 「不要用的场景」（如：判词不替代具体核查，A3 不适用于有机器验证的场景）+ Action Triggers（审计/终审/复盘时对照）

## 验收

- pre-submit 全过（含定位声明、KF-024 三要件）
- **实证出处抽验**：随机 3 条判词的出处任务单/文件真实存在且内容对得上（防誊抄漂移）
- 三方法适配声明：判词=内部制度提炼非外部事实断言，外部调研不适用；验证走出处回链
- 欧阳锋终审

## 边界

- 只结构化建议书已有 13 条，不新增判词（新增走风清扬后续审计件的「可固化资产候选」节常态通道）
- 不改 agent-os、不改各角色 spec（引用分发缓议——随各角色自迭代引入，不批量改）
- 不解压资产捆绑：本卡的解压=agent-os 引用+门禁词表引用（治理资产），随卡终审后由王语嫣落引用，不占本单

## 解压路径（W4 自检）

framework 卡 1 张 → 解压资产：①agent-os 引用节（终审后王语嫣落）②#433 族门禁词表引用判词编号（下次词表变更时执行）③风清扬审计件「可固化资产候选」常态节（已确认，自执行）

## 建模方案（L1 出牌，2026-08-27 老顽童）

依赖链：`[素材] → [边界] → [结构] → [质量]`

| 位 | 牌号 | 一句话理由 |
|:--|:--|:--|
| 素材 | #3 先口述稿再笔记（变体：先全文底本再二手转述） | 唯一底本=风清扬建议书全文（13 条判词+出处+边界），已逐字消费，卡内容 95% 现成——誊抄不走样是核心风险 |
| 素材 | #2 先全文扫描再选策略 | 底本含「边界声明」「裁决请求」节，全部读完再定取舍：只结构化 13 条判词，不把裁决请求誊进卡 |
| 边界 | #5 先判归属再消化 | 归属=审查/治理方法论域，`30_wiki/frameworks/`；与 #433 词表（`queue_transition.py` 强词/宽词）划界：本卡=认知层真相源，词表=实现层 |
| 边界 | #6 先查已有卡再新建 | 已查：frameworks/ 目录无 maxim/audit 同名卡，kdo query 无同主题卡，id 未被占用 |
| 结构 | #9 先 framework 再 concept | 本卡即 framework 层（判词体系的关系呈现：A/B/C 三组分工），不建子卡 |
| 结构 | #10 先骨架再填肉 | 骨架=定位声明+A/B/C 三表+KF-024 三要件（Synthesis/不要用的场景/Action Triggers）+framework 必备节（操作步骤/When NOT to Use/失败模式） |
| 质量 | #15 先自攻击再提交 | 四路攻击重点：誊抄漂移（对底本逐条对账）、边界重叠（与 charter §3.16/§3.17/§3.18 的关系是否说清） |
| 质量 | #16 先 lint 再 pre-submit | 逐张跑门禁贴输出；验收含实证出处抽验 3 条（已预验：#432/#433/#444/#514 任务单真实存在） |

## 执行报告（完成后回填）

**改动文件**（清单）：`30_wiki/frameworks/framework-audit-maxims-library.md`（新建，交付物）；`60_feedback/adversarial/atk_framework-audit-maxims-library_20260827.md`（新建，自攻击报告）；`60_feedback/tasks/task_20260827_laowantong-audit-maxims-card.md`（本任务单：建模方案+执行报告）；`.kdo/CAPSULE_STARTUP.md`（git_head/queue_tail 字段过期更新，启动校验动作）
**完成内容**（一句话）：风清扬 13 条审计判词（A6/B5/C2）已结构化为 `30_wiki/frameworks/framework-audit-maxims-library.md` v0.1，经四路自攻击修复 1🔴+9🟡 类问题，pre-submit PASS，已 commit。
**验证**（命令+输出）：
  - `kdo pre-submit -f 30_wiki/frameworks/framework-audit-maxims-library.md` → `Files checked: 1 / Passed: 1 / Failed: 0 / ✅ Result: PASS（2 条 WARNING 在列）`（全文见下）
  - 出处抽验 `ls 60_feedback/tasks/task_20260823_huangyaoshi-{memory-capsule-l0-minimal,negative-claim-gate,queue-force-ledger-assignee-role}.md` → 三文件均存在，内容与判词对得上
  - `git log --oneline -1` → 交付 commit 已入仓
**未做项**（边界）：①agent-os 引用节 + ②#433 词表引用判词编号——按任务单边界不占本单，终审后王语嫣落；B3/B4 出处为会话实录，文件级回链待补（已在卡内标注「待回链」）
**需要谁动作**：欧阳锋终审本卡；终审通过后王语嫣落解压资产①②
- **自攻击**：四路 AgentSwarm 并行攻击，报告落 `60_feedback/adversarial/atk_framework-audit-maxims-library_20260827.md`。🔴×1（Synthesis 伞命题被 5/13 反例证伪）+🟡×9 类+🟢×6 类全部修复/标注：词表-判词因果方向修正、A5 入宪状态纠偏、B2 算术改写、B1/B5/C1 出处补文件级回链、失败模式补 charter 漂移、When NOT to Use 补效力层级、行号锚点改常量名
- **出处抽验 3 条**（验收要求）：A2→#432 ✓（任务单存在+语录真实出处在 parking-lot F-027）/ A3→#433 ✓（任务单与判词完全互证）/ B1→#444 ✓（元凶单，事件实录在 session-archives/2026-08-24/wangyuyan-claude.md）。补链 5 个路径全部 `ls` 复验存在
- **三方法适配声明**：判词=内部制度提炼非外部事实断言，WebSearch 外部调研不适用；验证走出处回链（任务单规格 L37 裁定）
- **pre-submit 输出**（2026-08-27，修复后复跑）：

```
  Files checked: 1  |  Passed: 1  |  Failed: 0
  [YAML]: 0 issues  [WIKILINK]: 0  [DOMAIN]: 0  [DK_SECTION]: 0  [OUTLINK]: 0
  [ALIASES]: 1 warnings — Source names not in title/aliases（5 个 source 文件名）：
    如实说明——5 个名称已实际写入 aliases 和 discoverable_by 两字段，警告仍触发；
    已核实在库卡 bridge-lightning-agent-evolution 带同款警告且 PASS，判定为检查项实现缺陷（不阻断），留待黄药师排查
  [POSITION_DECLARATION]: 0  [SOURCE_REACHABILITY]: 0
  [QUALITY_SCORE]: 55/100 | pos:25 | tacit:5 | src:25 (6) | decomp:0
  [BODY_SRC_UNKNOWN]: 0  [VLM_TWO_SECTION]: 0
  ✅ Result: PASS（2 条 WARNING 在列——有警在身，非全清，终审前自行掂量）
```

- **过程发现（建议书素材）**：pre-submit 的 ALIASES 检查对新卡必须先跑 `kdo index --incremental` 才认 aliases——新卡未入索引时必 FAIL，且索引后警告仍残留（误报）。已记 friction-log，建议落最小建议书待评估

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 3 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🟡 ⚠️ 意见书含宽负向词（缺）无核查锚点——按需人工确认（#433 不硬杀）；锚点：⚪ 无锚点
