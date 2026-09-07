# #679 审计路由机制双件验证证据（2026-09-07 huangyaoshi）

## 0. 初判核验（本单自身触发新门禁 WARNING——claim 活体实证，见 §2.3）

- 任务一前提「派工模板**增补**字段」→ 核查：开工前 `ls 90_control/templates/` 仅 5 件（agent-context / agent-decisions / agent-pitfalls / deep-synthesis-article / domain-index-template），**任务单模板不存在**——初判修正为「新建」而非增补【实证】
- 任务二前提「三例截写+复跑锚系自创非成文」→ 核查：kdo query 两条 0 相关命中（§5）+ grep 规范文档（90_control/*.md、.agent/*.md、30_wiki/agent-specs/）「引用语境豁免|截写」仅命中 `.agent/friction-log.md:154/:155`（老顽童 09-06 两条建议行）与 diagnosis 文件，**无任何规范文档成文**——证实【实证】

## 1. 任务一交付：派工模板「初判=待证命题」字段

1. **新建** `90_control/templates/task-dispatch-template.md`——frontmatter 含 `initial_assessment: 待证命题（附存在性核查锚）`（锚点三选一：文件:行 / git rev / grep 命中数）+ 使用说明三条（编排侧复制口径 / 待证命题语义=执行者以实证证实或证伪 / 两态门禁与生效日）
2. **claim 门禁** `90_control/scripts/queue_transition.py` 新增 `_check_initial_assessment_gate`，接线 `action_claim`（处置门禁之后）：
   - 存量任务（created_at < 生效日）缺字段 → **WARNING 放行 + `_log_gate_warning` 台账**
   - 新派任务（created_at ≥ `INITIAL_ASSESSMENT_HARD_DATE="2026-09-14"`，env `KDO_INITIAL_ASSESSMENT_HARD_DATE` 可提前）→ **硬拦**（charter §3.10 口径：存量不回改，新格式仅对生效日后生效）
   - 防货物崇拜：模板占位符原样照抄（`待证命题（附存在性核查锚）`/TODO/TBD）= 按缺失处理
   - 逃生门：`claim --force --reason`（#504 force 台账留痕）

### 2. 生效实证（验收项①）

- **活体**：本单 claim 实跑输出 `⚠️ task_20260907_huangyaoshi-audit-mechanisms 缺 initial_assessment（初判=待证命题+核查锚）——WARNING 台账已记…（#679；软期至 2026-09-14）`【实证】
- **台账落盘**：`90_control/gate-warning.log` 新增行 `2026-09-07 10:10:25｜task_20260907_huangyaoshi-audit-mechanisms｜初判字段门禁｜缺 initial_assessment（软期至 2026-09-14，存量既往不咎）｜huangyaoshi`【实证】
- **回归**：`90_control/scripts/tests/test_queue_transition.py` 新增 `TestInitialAssessmentGate` 6 例——存量 WARNING 放行 / 新派硬拦 / 占位符原样硬拦 / 回填后零提示通过 / env 翻转硬拦 / 模板字段存在且占位值被门禁识别——**82 passed** 全绿

## 3. 任务二交付：词表门禁「引用语境豁免」成文（验收项②）

`90_control/kdo-industrialization-manual.md` 新增 **§3.5.1**（小昭审计建议 3）：

- 根因成文：词表级门禁字面/启发式匹配无法区分「提及」（引用坏形态举证）与「患有」（本身有缺陷）；三例同源锚点：E040 交付物入仓（#522，`queue_transition.py` L819）/ BODY_SRC_UNKNOWN（#517，`pre_submit.py` L1422）/ QUOTE_VERBATIM（`_check_quote_verbatim`，`pre_submit.py` L1308；第三例形态=ASR 噪声元注记误判引语，friction-log L155）
- 合法补救路径四条：**截写**（`src_unknown`→`src_unk*`）/**复跑锚**（复跑命令+命中数，例 `grep -c "src_unk" 30_wiki/log.md`=218）/**三禁**（不删证据、不改写证据、不加零宽字符）/**留痕**（存档头部声明截写位置与还原方式）
- 实证源锚：`60_feedback/session-archives/2026-09-06/laowantong.md:28`（截写+显式声明决策全句）/:56（"现状是我自己发明的"原文）、`.agent/friction-log.md:154/:155`
- 同文件 **§3.5.2** 派工模板字段口径成文（初判失真定律 5/5 锚点+模板路径+门禁参数+两态节奏与 #669/#677 一致）

**回归不红（验收项③）**：`pytest 90_control/scripts/tests/test_queue_transition.py` 82 passed；KDO 仓 `655 passed 1 skipped`（本轮 KDO 仓零改动，三例门禁检查器语义未动——本单成文的是提交侧补救路径合法性，不是放行面扩宽）。

## 4. 边界

- **门禁代码语义零改动**：quote_verbatim / body_src_unknown / E040 检查器照旧拦截——豁免是"引用坏形态举证"时提交侧的合法写法成文，非门禁判断逻辑修改（#429 只拦机械项、#444 例外留痕契约不破）
- **任务单 frontmatter 不代改**：`initial_assessment` 回填责任在编排侧（王语嫣）；本单任务单缺字段事实由 WARNING 台账留痕，执行报告代偿初判核验（§0），不改编排派工记录（E046 append-only 精神）
- **存量任务单不回填**模板字段（charter §3.10 存量不回改）；模板为本单新建，非对既有文件增补

## 5. kdo query 检索记录（宪法第六条，#669）

| 检索词 | 变体 | 命中 | 日期 | 结论 |
|:--|:--|:--|:--|:--|
| 词表门禁 引用语境 豁免 截写 | 中文 | top5（0.15-0.18：审计判词库/五维标注深挖法/知识库vs本体论等，均无豁免条款） | 2026-09-07 | 豁免条款未成文（证实） |
| 初判 待证命题 派工 模板 任务单前提核查 | 中文 | 5 chunks（无初判字段相关卡） | 2026-09-07 | 无既有口径（证实） |

grep 降级均为许可类：①kdo query 后定位模板/规范落点 ②代码/配置/日志非知识检索。

## 6. 存在性核查（负向判词锚点，#433）

- 「豁免条款此前未成文」→ grep `90_control/*.md + .agent/*.md + 30_wiki/agent-specs/`「引用语境豁免\|截写」命中仅 friction-log L154/L155 与 diagnosis/session-archives（建议与实证侧），规范文档零命中
- 「任务单模板此前不存在」→ 开工前 `ls 90_control/templates/` = 5 件，无 task-dispatch-template
- 「台账已落盘」→ `90_control/gate-warning.log` 2026-09-07 10:10:25 行（本单 task_id + 门禁名 + 软期）
- 「三例门禁编号」→ `pre_submit.py` L1422（#517）/ L1308（`_check_quote_verbatim`）；`queue_transition.py` L819（#522 E040）
- 「回归不红」→ 82 passed（queue_transition）+ 655 passed 1 skipped（KDO 仓全量）
