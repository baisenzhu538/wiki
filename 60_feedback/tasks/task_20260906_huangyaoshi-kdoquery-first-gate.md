---
id: task_20260906_huangyaoshi-kdoquery-first-gate
title: "kdo query 第一优先门禁：知识检索强制规则（宪法第六条+pre-submit 检索记录检查）——老朱「不信自律信门禁」"
seq: 669
status: in_progress
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-06
decision_source: 老朱 09-06 直令「kdo query 是第一优先级，我不相信自律只相信门禁和强制规则，找不到再采用 grep」
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-06T13:39:00.714935+00:00'
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
