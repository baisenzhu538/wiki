---
id: 417
assignee: kimi
status: pending_review
updated_at: '2026-08-22T14:14:20.787864+00:00'
---
# #417 工业化手册整改（王语嫣主笔，持续迭代机制）

- **任务号**：#417
- **状态**：pending_review（已提审，等欧阳锋终审）
- **assignee**：wangyuyan（主笔；当前实例 kimi；终审=欧阳锋；终稿=老朱）
- **优先级**：P0
- **依赖**：#416（基本法框架稿——角色表对齐它）
- **立项**：2026-08-22 王语嫣（会诊 B4-1 拍板+分工裁定）

## 任务目标

`90_control/kdo-industrialization-manual.md` 整改：版本漂移收口（正文 v1.6/frontmatter 1.9/内容含 KF-025 三口径）+ 角色表更新（旧三角色→入宪六方，对齐基本法）。

## 动作

1. 版本号归一：frontmatter/正文同号，写版本规则（改一次升一次）
2. 角色表重写：对齐 #416 基本法六方职责
3. 内容与现实对账：手册描述的流程 vs 现行机制（queue_transition/门禁/终审链）逐节核对，过时段落修订或标注
4. **防复发机制**：frontmatter/正文版本号一致性脚本校验（黄药师配合入 lint——"想犯错也犯不了"）；风清扬定期审计"手册 vs 现实"差距（挂定期洞察报告）
5. 附 #399 复扫输出（全库对手册的引用口径）

## 验收

- 版本号唯一+脚本校验可查
- 角色表与基本法逐字一致
- 欧阳锋终审抽"手册 vs 现实一致性"；commit 入档

---

## 追加（2026-08-22 王语嫣）：spec↔context 两套真话收敛

> 来源：风清扬五角色建议书组织层建议 2（采纳）。实锤：黄药师 context 停旧双轨、4 张 spec 卡停在 B2 拍板前——spec 管"是什么/边界"，context 管"怎么跑"（#370 已定分工），口径必须一致。

- **整改动作 6**：六角色 `agent-spec` 卡与 `.agent/<role>-context.md` 逐角色对账，分歧点列清单（手册对账节记录）
- **防复发**：同口径脚本校验（黄药师配合入 lint）——以 `memory-registry.md` 表 1「角色定义」行为准
- 注意：90_control/AGENTS.md 角色表（"欧阳锋唯一协调节点/王语嫣只看不改"）与现实脱节为已确认靶子，本单对账范围含该文件

---

## 整改记录（2026-08-22，kimi 实例执行）

**改动文件与收口**（仅 2 个内容文件；手册单独 path-scoped commit，任务单/队列/看板由 `queue_transition.py complete` 自动收口）：

1. `90_control/kdo-industrialization-manual.md` → v2.0（commit `a1dc99d39`）
   - A 版本归一：frontmatter `version: "2.0"` / `updated_at: "2026-08-22"`；正文标题 v2.0；编制行加 v2.0 标注；文首加版本规则（改一次升一次、frontmatter/正文同号、脚本校验，溯源 #416 附则/B4-1）
   - B §1.2 审而不改：改为「生产者（老顽童）修正内容卡 / 建设者（黄药师）修正基建；欧阳锋复审」，90_control 变更仍受 KF-001 双重签发约束
   - C §二角色体系整节替换为入宪六方，核心表逐字采用 charter §2.1；补权责分界、执行前三问、挂起角色（段王爷/洪七公/历史业务 agent）、资产落点表（风清扬 spec 标在途 #428）；删除旧三角色分工与「复合编译执行/高质量内容提炼」表述
   - D §3.4 新增「现行任务队列与提交门禁口径」：`queued → claimed-{instance} → pending_review → reviewed/退回 queued`；REVIEW-PENDING（#389/#413）/INBOX-PENDING（watch_inbox）/PROPOSAL-PENDING（#421）三自动登记段；提交链=王语嫣编排门禁 → `kdo pre-submit -f` → 欧阳锋终审 → 老朱终稿拍板；注明 L2 警告 ≠ pre-submit 阻断
   - E L2 节补注：`kdo pre-submit` 为独立阻断提交门禁，未被 L2 豁免
   - F 铁律：章首与附录 C 改 KF-001~026；KF-010 加入 `kdo pre-submit`；KF-011 扩为「审而不改 + 写审分离（author≠reviewed_by，lint 强制）」；KF-024 保留=行为转化三要件；原第二个 KF-024「卡片体量上限」改编号 KF-026，§1.13 与附录 D 引用同步；KF-025 域完成四问保持不动
   - G §10.2：`revision（生产者/建设者按域修正）`、`verify（Architect（欧阳锋）复审关闭）`
   - H 附录 A 改 F-KDO-001~016；附录 B 标历史快照（停在 2026-05，现行队列以 production-queue.md 为准）；附录 D 加 2026-08-22 v2.0 行
   - I 新增附录 E「2026-08-22 现实对账记录」：AGENTS.md 角色旧制、铁律数 22 过时（AGENTS.md:386 / rules-core.md:34）、context 卡 KF-025 三问口径落后、spec 卡 draft/#428 在途、#399 复扫缺手册引用口径检查项——均列为外部漂移不直接改
2. 本任务单：正文状态与整改记录同步为提审后口径；frontmatter 由脚本流转为 `pending_review`

**提审记录**：`queue_transition.py complete task_20260822_wangyuyan-industrialization-manual-revamp --instance kimi --evidence 90_control/kdo-industrialization-manual.md` 已执行，队列状态 `pending_review`（等欧阳锋终审）；queue/dashboard/task 自动收口 commit `2428dabe2`。

**自检结果**：grep 确认手册无 `v1.6` 标题、无 `KF-001~022`、无第二个 `KF-024` 体量上限、无「复合编译执行」；存在 `v2.0`、`KF-026`、「入宪六方」、`queued → claimed`；Python 读 frontmatter 确认 `version == "2.0"`。输出摘要见会话记录。
