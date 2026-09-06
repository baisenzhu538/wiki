---
id: task_20260906_huangyaoshi-kdoquery-first-gate

title: "kdo query 第一优先门禁：知识检索强制规则（宪法第六条+pre-submit 检索记录检查）——老朱「不信自律信门禁」"

seq: 669

status: reviewed
assignee: huangyaoshi

created_by: wangyuyan

created_at: 2026-09-06

decision_source: 老朱 09-06 直令「kdo query 是第一优先级，我不相信自律只相信门禁和强制规则，找不到再采用 grep」

reviewer: 欧阳锋

instance: huangyaoshi

updated_at: '2026-09-06T14:30:55.422797+00:00'
evidence: 60_feedback/tasks/task_20260906_huangyaoshi-kdoquery-first-gate.md
reviewed_by: 欧阳锋
review_date: '2026-09-06'
grade: A-
---

# #669 kdo query 第一优先门禁（黄药师）

## 背景
王语嫣标签治理调研时未用 kdo query（用 grep 沿自己足迹搜），漏掉库内已有方法卡两周——W11 写在锚点里照样违例。老朱裁定：**不信自律，信门禁**。规则=kdo query 第一优先，grep 是兜底不是首选。

## 任务
1. **宪法增补第六条**（90_control/agent-behavior-constitution.md，v1.0→v1.1）：「知识类问题第一动作=kdo query（检索词做同义/中英扩展）；0 命中或证据不足才降级 grep 兜底；诊断/调研类产出必须附 kdo query 检索记录节（查询词+命中数+日期），无检索记录=不闭环」
2. **pre-submit 检查项**：诊断/调研/报告类文件提交时，检查器校验存在「kdo query 检索记录」节——缺失=WARNING（先软一周）→ 升 HARD（门禁化，与 F-035 同级）
3. **grep 降级口径写进 constitution 与各角色 context 模板**：grep 只用于①kdo query 之后补充定位②非知识类检索（代码/配置/日志）
4. **回归**：模拟无检索记录的报告→检查器拦截；有记录→通过；现有测试不红

## 验收
- 检查器两态（WARNING→HARD）生效实证
- 宪法 v1.1 diff+三挂载点同步（startup/拉起器模板/公告）
- 回归不红

---

## 执行报告（黄药师 2026-09-06）

**交付物**
- 宪法 v1.1：`90_control/agent-behavior-constitution.md` 增补第六条「知识问题第一动作 = kdo query」（修订单已登记 v1.1，frontmatter version 1.0→1.1）
- pre-submit 门禁：`Knowledge Delivery OS 0.0.1/kdo/pre_submit.py` 新增 `_check_kdo_query_log` + `KDO_QUERY_LOG` 展示登记（该仓 commit `2dfb4f5`，2 files，+178/−1）
- 回归测试：`Knowledge Delivery OS 0.0.1/tests/test_pre_submit_kdo_query_log.py` 8 例
- grep 降级口径挂载：`agents/agent-os.md` 新增 §10.4.2（OS 层共享单点）；`.agent/startup.md`（L5+步骤 6.5）；`90_control/scripts/kimi-headless-launch.py`（PROMPT_TEMPLATE 宪法行）；`.agent/infrastructure-bulletin.md`（#669 公告条目）；hermes SOUL.md ×6（hermes 侧，不在 vault git，核验命令见验证节）

**完成内容**
- ①宪法第六条：第一动作=kdo query（同义/中英扩展 ≥2 变体）；0 命中或证据不足才降级 grep；诊断/调研/报告产出必附「kdo query 检索记录」节（查询词+命中数+日期），无记录=不闭环
- ②检查器两态：缺节=WARNING（软期至 2026-09-13）→ 之后 ERROR 拦截（与 F-035 同级）；`KDO_QUERYLOG_HARD_DATE` env 可提前门禁化；适用面=frontmatter type ∈ {diagnosis,research,report,诊断,调研,报告} 或路径落 `60_feedback/diagnosis|diag|diags|analysis/`（建议书多无 frontmatter，靠路径兜住）
- ③grep 降级双口径（①kdo query 后补充定位②非知识类检索：代码/配置/日志）落 constitution 第六条 + agent-os §10.4.2 + 拉起器 PROMPT_TEMPLATE + hermes SOUL ×6

**验证**
- 两态实证【实证】：真实库文件 `60_feedback/diagnosis/diag_20260906_wangyuyan-audit-pilot-report.md`（无检索记录节）默认档 → `[KDO_QUERY_LOG]: 1 warnings`（软期至 2026-09-13）；同文件 `KDO_QUERYLOG_HARD_DATE=2026-09-01` → `[KDO_QUERY_LOG]: 1 errors`（HARD）
- 通过态实证【实证】：带检索记录节样本（`_tmp` 透传样本，已清理）→ `[KDO_QUERY_LOG]: 0 issues` + `✅ Result: PASS`
- 库内先例识别【实证】：`## 知识库检索记录（§10.4.1）`/`#### 检索记录（§10.4.1）`/`## 前置：wiki/技能检索记录` 等既有节名变体均判通过（测试 test_existing_library_heading_variants_pass）
- 回归不红【实证】：`python -m pytest tests/ -q` → **633 passed, 1 skipped**（skip 为既有），exit 0；新门禁单测 8/8 过
- 挂载点交叉核查【实证】：宪法挂载链内「五条行为底线」残留 0 处；宪法/startup×2/公告/拉起器模板/agent-os/SOUL×6 第六条口径全在场；SOUL fence 配对全偶数、v1.0 标记残留 0、v1.1 标记 6/6；PROMPT_TEMPLATE `.format()` 离线渲染通过
- 现状摸底【实证】：`60_feedback/diagnosis/` 343 个文件 **0 个**带检索记录节——软期一周即全量补记录窗口，硬门禁首日若不补将大面积被拦

**边界**
- 各角色 `.agent/<role>-context.md` 未逐一改动（B4/D4 铁律：不碰其他角色 context）——grep 降级口径走共享单点挂载（宪法第六条+startup 6.5+拉起器模板+SOUL×6+agent-os §10.4.2），先例=#652 欧阳锋终审认可的同款挂载法
- 存量不回扫：检查器只对提交中的文件生效（只向前，#517 同款）；`60_feedback/` 根层散落报告（如 itingnao-*）无 frontmatter type 且不在诊断目录，本版不覆盖，待 WARNING 期实测噪声后再定是否扩词表
- 检查器只查节存在性，不查查询词/命中数真实性（#433：机器做存在性，人做正确性；内容对不对归欧阳锋终审）
- vault 内 `90_control/scripts/pre_submit.py` 保持 deprecated 不动（#377 收敛决议）；KDO CLI 仓按一门禁一提交惯例落 commit `2dfb4f5`

**需要谁动作**
- 欧阳锋：终审本单（门禁代码 diff `2dfb4f5` + 宪法 v1.1 diff + 三挂载点）
- 王语嫣/全 agent：软期内（至 2026-09-13）诊断/调研/报告类产出补「kdo query 检索记录」节；若 09-13 前发现误伤面过大，提建议书裁决是否推迟 HARD 或加豁免口径
- 老朱（可选）：`KDO_QUERYLOG_HARD_DATE` 可提前门禁化，无需等一周

### kdo query 检索记录（宪法第六条自证）

- 2026-09-06 `kdo query "知识库检索记录 调研 门禁"` → 3 命中（分库与映射表/触点减法/人脉库检索，均低相关）——库内无「检索记录门禁」专卡，节名惯例源头在 `agents/agent-os.md` §10.4.1（grep 定位，非知识类检索：规范文件）
- 2026-09-06 grep（代码/配置/日志类，第六条②口径）：检索记录先例 40+ 文件（session-archives 为主）；pre_submit 检查器定位 2 处（vault deprecated 版 + KDO CLI 法定版）

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 7 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🔴 意见书含负向断言（「无记录」）但无 `**存在性核查**` 锚点（#433：'我没看到'≠'不存在'，负向判词必须附核查节，否则不闭环）（生产侧同口径，供终审对照）

**存在性核查**（宪法第二条：负向判词逐条附锚，2026-09-06 实测）

| 负向判词 | 核查动作 | 锚点结果 |
|:--|:--|:--|
| `60_feedback/diagnosis/` 343 文件 0 个带检索记录节 | `grep -rl "检索记录" 60_feedback/diagnosis/ \| wc -l` | 0（对照组：`grep -rl "检索记录" 60_feedback/session-archives/ \| wc -l` = 40+，工具不失效） |
| 库内无「检索记录门禁」专卡 | `kdo query "知识库检索记录 调研 门禁"` + `grep -rn "检索记录" agents/agent-os.md` | 3 命中均低相关；规范源头仅 `agents/agent-os.md:250` §10.4.1（复盘要求，无产出门禁） |
| 挂载链「五条行为底线」残留 0 处 | `grep -rn "五条行为底线" .agent/startup.md .agent/infrastructure-bulletin.md 90_control/agent-behavior-constitution.md 90_control/scripts/kimi-headless-launch.py agents/agent-os.md \| wc -l` | 0；同命令改搜「六条」各挂载点 ≥1 |
| SOUL.md v1.0 标记残留 0 | `grep -l "constitution: v1.0" C:/Users/Administrator/.hermes/profiles/*/SOUL.md \| wc -l` | 0；v1.1 标记 6/6；`grep -c '^```'` 各文件偶数配平 |
| 回归 skip 为既有、与本门禁无关 | `python -m pytest tests/ -q -rs` | skip= `tests\test_validate_v15.py:955`（catalog-index 豁免用例，与 pre_submit 无关）；633 passed |

## 终审记录

**终审人**：欧阳锋
**终审日期**：2026-09-06
**结论**：PASS A-
**methodology_version**：v2.3

### 四重点核查（逐项实证）

① 宪法第六条表述精度【实证】通过。三要素齐备且措辞精确：第一动作定义（第一动作=`kdo query`，检索词同义/中英扩展 ≥2 变体，单一命中不下定论）、降级条件（0 命中或证据不足才降级 grep 兜底 + grep 双口径①kdo query 之后补充定位②非知识类检索：代码/配置/日志/脚本）、检索记录节要求（诊断/调研/报告类产出必附「kdo query 检索记录」节=查询词+命中数+日期，无记录=不闭环；WARNING 软一周至 2026-09-13 → 升 HARD，与 F-035 同级）。

② 检查器两态真实生效【实证】通过。本终审独立复跑全链路 `run_pre_submit`+`format_report`（真实库文件 `60_feedback/diagnosis/diag_20260906_wangyuyan-audit-pilot-report.md`，frontmatter type: diagnosis，无检索记录节）：默认档→`[KDO_QUERY_LOG]: 1 warnings`（不占 error 计数）；`KDO_QUERYLOG_HARD_DATE=2026-09-01`→`[KDO_QUERY_LOG]: 1 errors`（error 计数 +1，Result 由 4 errors 变 5 errors）。两态实证成立，非仅单测。

③ grep 降级口径三挂载点【实证】通过。双口径全文在场：宪法第六条、`agents/agent-os.md` §10.4.2、拉起器 `90_control/scripts/kimi-headless-launch.py` PROMPT_TEMPLATE、基建公告 `.agent/infrastructure-bulletin.md` #669 条目、hermes SOUL.md ×6（v1.1=6/6、v1.0 残留 0）；挂载链「五条行为底线」残留 0。startup.md 6.5 为开机引导摘要，含降级触发条件（0 命中才降级 grep）与宪法指针、未逐字列①②——非阻断，见注记。

④ 回归不红【实证】通过。`python -m pytest tests/ -q` → 633 passed, 1 skipped（skip=`tests/test_validate_v15.py:955` catalog-index 豁免，与本门禁无关）；新门禁单测 `tests/test_pre_submit_kdo_query_log.py` 8/8。

### **存在性核查**（宪法第二条：负向判词逐条附锚）

| 负向判词 | 核查动作 | 锚点结果 |
|:--|:--|:--|
| startup.md 未逐字列 grep ①②双口径 | `Select-String startup.md "①|补充定位|非知识类"` | 0 命中；仅 6.5 行「0 命中才降级 grep」+宪法指针 |
| SOUL.md v1.0 残留 0 | 六 profile grep `constitution: v1.0` | 0；v1.1=6/6 |
| 挂载链「五条行为底线」残留 0 | 五挂载点 grep `五条行为底线` | 0 |
| 回归 skip 与本门禁无关 | `pytest -rs` | skip=`test_validate_v15.py:955` |
| 检查器只查节存在性、不查查询词真实性 | 读 `_check_kdo_query_log` 源码 | 仅 `_QUERY_LOG_HEADING_RE.search(body)` 判存在性，无内容校验——符合 #433 机器存在性/人正确性分工，已声明边界 |

### 非阻断注记（无 🟠/🟡，无需落点）

- startup.md 6.5 摘要未逐字列 grep ①②双口径，建议下次修订时补齐或显式标注「详见宪法第六条」；权威口径已在宪法/公告/拉起器/agent-os/SOUL 全在场，不阻断。
- 宪法 frontmatter「挂载点」行声明 startup/拉起器/SOUL 三注入通道，与任务验收「三挂载点=startup/拉起器/公告」存在术语差异；公告与 agent-os §10.4.2 为同步点未列入该声明。属注入通道 vs 文档同步点两种语义，建议后续统一术语，不阻断。


