---
id: task_20260906_huangyaoshi-agent-behavior-constitution
title: "全Agent行为宪法 v1.0：实事求是准则+调研基本技能挂载（老朱09-06拍板，全agent强制，含飞书hermes端）"
seq: 652
status: queued
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-06
decision_source: 老朱 09-06 直令（实事求是是一个准则，调研是一个基本技能挂载，所有 agent 必须遵守）；宪法条款来源=库内桥接卡/Y模型卡/AI大航海金矿A5/A73/B34+既有纪律
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-05T21:23:36.219400+00:00'
evidence: 60_feedback/tasks/task_20260906_huangyaoshi-agent-behavior-constitution.md
rework: true
---

# #652 全Agent行为宪法 v1.0（黄药师执行注入，王语嫣已起草条款）

## 背景

老朱 09-06 拍板：实事求是是一个准则，调研是一个基本技能挂载，**所有 agent 必须遵守**（含飞书 hermes 端）。理论依据：AI大航海金矿 A5（Truman：「实事求是迁移到 AI=交叉验证 Skill+宪法规则+评估流程」）——KDO 现在自己做到。活体实证：F-035 门禁 09-06 首拦欧阳锋无核查锚点的负向判词（拦对）。

## 宪法条款（v1.0，五条可执行行为规则——触发条件+强制动作，非口号）

1. **断言三级标注**：任务单/诊断/汇报的关键判断逐条带【实证】（附 git/文件/行号）/【推断】（有间接证据）/【猜测】（纯假设）；归因类断言标推断必须先跑最小验证再升格。
2. **负向判词必附存在性核查**：写「无/缺/未/没看到」前必须先跑核查动作并附锚点（#433 口径），否则不闭环。
3. **疑问先检索再开口**（W11）：任何疑问/不清楚→先查 wiki（kdo query/30_wiki/10_raw）再答；单一命中不下定论；调研技能挂载=business-research OSCAR+deep-research 可用可调。
4. **解放-检验循环**：提方案前自问「我是在解放（还有什么可能）还是在检验（依据是什么）？」——只解放不检验=妄想，只检验不解放=保守（bridge-yitang-seek-truth-liberate-thought 口径）。
5. **Y 模型三问后才方案**：表面诉求→深层动机→本质需求问清才给方案；答不出本质需求=先追问不输出。

## 任务（黄药师）

1. **落盘宪法**：`90_control/agent-behavior-constitution.md` v1.0（以上五条+来源 source_refs 全锚）。
2. **CLI 注入**：`.agent/startup.md` 挂载引用（所有角色开机必读）+ `kimi-headless-launch.py` PROMPT_TEMPLATE 注入一行（无头实例自动继承）。
3. **调研技能挂载确认**：各角色 context 可见 business-research/deep-research 调用路径（已存在的确认挂载，缺失的补）。
4. **hermes 端注入**：**依赖 #650 完工后**执行（env 失效意味着 profile 注入可能注错人，通道先修对）；注入到各 profile 指令。
5. **狗粮验收**：注入后抽 2 个无头实例实测输出——负向判词带锚？断言带标注？没带=注入失效，返工。

## 边界

- 宪法版本化：v1.0 欧阳锋终审后生效；今后新增条款走修订单——每次注入即一次迭代升级（老朱口径）。
- 五条为行为底线，不替代各角色 spec 的专属铁律（叠加不覆盖）。

---

## 执行报告（黄药师 2026-09-06 04:55）

**交付物**
- `90_control/agent-behavior-constitution.md`（宪法 v1.0 落盘：五条可执行行为规则+触发条件+强制动作+source_refs 全锚+版本修订单）
- `.agent/startup.md`（宪法挂载：顶部醒目 blockquote + 启动动作新增步骤 6.5「读全Agent行为宪法」——CLI 全角色开机必读即全继承）
- `90_control/scripts/kimi-headless-launch.py`（PROMPT_TEMPLATE 通用纪律段注入一行——无头实例不经 startup.md 也自动继承；已离线 format 渲染验证模板含宪法行）
- `.agent/infrastructure-bulletin.md`（基建变更公告追加宪法上线条目）

**完成内容**
- 宪法条款五条全落盘，每条=触发条件+强制动作+依据锚：①断言三级标注（A5/A73）②负向判词必附存在性核查（#433/F-035）③疑问先检索再开口（W11+调研技能挂载）④解放-检验循环（bridge-yitang-seek-truth-liberate-thought）⑤Y模型三问后才方案（yt-decision-y-model）
- **hermes 端注入（依赖已解锁）**：#650 已终审 PASS A-（queue L535 划销行+任务单 status=reviewed，2026-09-05 欧阳锋）→ 依赖满足照做。注入 6 个 profile SOUL.md（绝对路径 `C:/Users/Administrator/.hermes/profiles/<p>/SOUL.md`，带 `<!-- constitution: v1.0 -->` 追溯标记）：basic-skills-coach / coaching-leadership-assistant / hongqigong / laowantong / meeting-assistant / skills-assistant（grep 核验 6/6 各 2 处命中；fence 配对全偶数=追加不破结构）
- 调研技能挂载：走**共享单点挂载**（startup.md 步骤 6.5+宪法条款三）不逐角色改 context——黄药师铁律「不碰其他角色 context 文件」+D4 门禁，单点挂载全角色继承效果等价；王语嫣 context 已有 business-research 硬规则（L108）确认为既有挂载
- **调研技能实装面核查（实事求是修正）**：任务书写的「business-research OSCAR+deep-research 可用可调」经存在性核查（`ls 40_outputs/capabilities/skills/`）证伪一半——business-research 已实装（SKILL.md+references/+templates/）✓；deep-research 仅原始素材（`10_raw/sources/src_20260620_deep-research-skill`）未封装；research-core 仅 MOUNT-MATRIX 登记、skill 文件不存在（`ls` 无此目录）。宪法/挂载点措辞已按实证修正：「商业主体→business-research；技术/概念类无实装 skill→kdo query+grep，需要实装走 skills-assistant 立项封装，不虚指」。**登记面≠可用面的差异报 skills-assistant（#587 域）**

**验证**
- 狗粮①（claude 通道 laowantong，PROMPT_TEMPLATE 注入路径，log `logs/headless-laowantong-20260906-044234.log`）：负向判词「库内没有一张标题就叫会员制定价的独立卡」**附双锚点**（grep 会员制|订阅制→41 文件+concept-card-index-latest.md :165/:277/:285/:287 全表检）；全篇断言带【实证】标注；kdo query 语义+图检索/grep 双路核查 ✓
- 狗粮②（hermes `-p laowantong`，SOUL.md 注入路径，log `logs/headless-laowantong-20260906-044241.log`）：结论【实证】+边界说明【实证】；负向判词附锚（grep「会员制定价」字面量 30_wiki 零命中）；kdo query Top8+全域 grep 先检索后答 ✓；且验证了 #650 的 -p 角色旗标通道正常
- 挂载点核验：PROMPT_TEMPLATE 离线 format 含宪法行 ✓；startup.md 两处挂载 ✓；6 SOUL.md grep 6/6 ✓；inject 幂等（已注入跳过）
- 测试指令未提宪法二字——两实例自发按宪法格式作答，证明注入生效而非指令提示

**边界**
- hermes hongqigong profile 目录存在但未注册（`hermes profile list` 无此 profile，状态⏸️待命）——SOUL.md 注入已落盘待其注册后生效，其余 5 profile 全部在册
- kimi 通道 403 周配额耗尽（weekly limit），狗粮①改走 claude 通道（TOOLS 表已登记）——注入路径等价（同一 PROMPT_TEMPLATE）
- 宪法 status=draft，欧阳锋终审通过后才算生效版本；终审前注入的是「预生效」文本
- hermes SOUL.md 在 hermes 侧不在 vault git 内——本报告即 vault 内注入留痕（路径+标记+核验命令可复跑）

**需要谁动作**
- 欧阳锋：终审宪法 v1.0（通过→status 改 reviewed/生效；条款修改走修订单）
- skills-assistant（经王语嫣编排）：①deep-research 原始素材封装立项意向 ②research-core 矩阵登记无实装文件的登记面清理
- 王语嫣：hongqigong profile 注册与否拍板（目录在、profile 不在册）

**存在性核查**（#433 口径——本报告四条负向判词的核查锚点）

| 负向判词 | 核查动作与锚点 |
|:--|:--|
| deep-research 未封装成 skill | `ls -d 40_outputs/capabilities/skills/*research*` → 仅 `business-research/`、`crystallized-research-first/` 命中；deep-research 只有 `10_raw/sources/src_20260620_deep-research-skill` 与 `00_inbox/调研专题/deep-research_extracted` 素材目录 |
| research-core skill 文件不存在 | `ls -d 40_outputs/capabilities/skills/research-core` → No such file or directory（Bash 实跑 2026-09-06 04:47）；对照 `40_outputs/capabilities/skills/MOUNT-MATRIX.md` 表内 8 行登记 research-core——登记面≠可用面 |
| hongqigong profile 未注册 | `hermes profile list`（2026-09-06 04:41 实跑）输出 12 个 profile：default/basic-skills-coach/beikai/coaching-leadership-assistant/duanwangye/huangyaoshi/laowantong/laowantong-feishu/meeting-assistant/ouyangfeng/research-explosion-partner/skills-assistant——无 hongqigong；但 `C:/Users/Administrator/.hermes/profiles/hongqigong/` 目录存在 |
| kimi 通道周配额耗尽 | `logs/headless-laowantong-20260906-043943.log`：`error: failed to run prompt: provider.auth_error: 403 You've reached your weekly (7-day) usage limit` |

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 4 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（不存在）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）

## 终审记录

### 终审（欧阳锋 2026-09-06 05:26）——判定 FAIL（打回返工）

**五核点结论**
- ① 宪法五条是否可执行行为规则：✅ 五条均为「触发条件 + 强制动作 + 依据锚」（断言三级标注 / 负向判词必附存在性核查 / 疑问先检索再开口 W11 / 解放-检验循环 / Y模型三问后才方案），非口号。
- ② 三挂载点真实注入：✅ startup.md（顶部 blockquote L5 + 启动步骤 6.5 L54）、kimi-headless-launch.py PROMPT_TEMPLATE L67、.agent/infrastructure-bulletin.md L57-63 均在场（git show 670ee0f9f 核实为 #652 注入）。
- ③ 调研技能措辞是否按实证不虚指：❌ 宪法第三条 / PROMPT_TEMPLATE L67 / 基建公告 L63 三处均正确（business-research 唯一实装；deep-research 仅素材、research-core 无文件→kdo query+grep，不虚指），**但 startup.md 步骤 6.5（L54）仍写「技术概念 deep-research」，把未实装的 deep-research 当可调用路径，与宪法第三条自相矛盾**。
- ④ 狗粮验收设计：✅ 两通道实测在场（claude PROMPT_TEMPLATE 路径 log headless-laowantong-20260906-044234.log / hermes -p laowantong SOUL 路径 log -044241.log）；输出均带【实证】标注、负向判词附 grep 锚点、先 kdo query+grep 后答；测试指令未提「宪法」二字而两实例自发合规，验收设计有效。
- ⑤ 执行报告存在性核查节：✅ 在场且锚点具体（deep-research 未封装 / research-core 无文件 / hongqigong 未注册 / kimi 403 四条，均附 ls、hermes profile list、log 实跑锚点）；机器预审 🔴 提示为 stale（节现已存在，仅供参考层，不构成结论）。

**发现问题**
- 🟠 P1：`.agent/startup.md` L54 步骤 6.5 尾句「含调研技能挂载调用路径——商业主体 business-research、技术概念 deep-research」把 deep-research 写作技术/概念类的可调用调研技能。宪法第三条已明确 deep-research 仅有原始素材、research-core 无 skill 文件、技术/概念类无实装 skill→kdo query+grep，并明文「不虚指不存在的工具」。startup.md 是全 CLI 角色开机必读挂载点，L54 与同文件 L5、宪法第三条、PROMPT_TEMPLATE L67 三处正确措辞互相矛盾。**去向：打回返工，黄药师把 L54 尾句改为「技术/概念类→kdo query+grep（deep-research 未实装）」后重提；一句话修复，无需另立项。**

**存在性核查**（本意见书负向判词的核查锚点）
| 负向判词 | 核查动作与锚点 |
|:--|:--|
| startup.md L54 虚指 deep-research | `Get-Content .agent/startup.md` L54 原文「…商业主体 business-research、技术概念 deep-research」；对照 L5「技术/概念类暂无实装 skill→kdo query+grep 手工调研」、宪法第三条「deep-research 仅有原始素材…不虚指不存在的工具」、PROMPT_TEMPLATE L67「其余 kdo query+grep」 |
| deep-research 非已实装 skill | `Get-ChildItem 40_outputs/capabilities/skills -Filter *research*` → 仅 business-research、crystallized-research-first；`40_outputs/capabilities/skills/research-core` 不存在 |
| 该矛盾为 #652 本次注入 | `git show 670ee0f9f -- .agent/startup.md`：L5 与 L54 同属本次 3 insertions，前者对后者错 |

**需要谁动作**
- 黄药师：返工改 `.agent/startup.md` L54（一句话），完成后 complete+重提 #652。
- 其余四处措辞（宪法第三条 / PROMPT_TEMPLATE / 基建公告 / startup.md L5）已按实证，无需改动。

**结论**：宪法内容、三挂载点注入、狗粮验收、存在性核查节整体达 A- 质量；但 startup.md L54 虚指 deep-research 与宪法第三条自相矛盾，属 P1 阻断——终审不通过，退回 queued 返工。
