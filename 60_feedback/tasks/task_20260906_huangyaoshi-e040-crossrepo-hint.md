---
id: task_20260906_huangyaoshi-e040-crossrepo-hint
title: "E040 报错提示跨仓前缀全路径（第2次复发工具化，#639 同族）"
seq: 653
status: pending_review
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-06
decision_source: 黄药师 #649 friction 03:46（第2次复发，老朱「两次复发立即工具化」口径）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-05T22:03:16.919533+00:00'
evidence: 90_control/scripts/queue_transition.py
---

# #653 E040 跨仓前缀提示微单（黄药师）

## 实证
#639 friction（09-04 21:45）首次：交付物节写 CLI 仓裸相对路径→门禁按 vault 相对判 untracked；#649 friction（09-06 03:46）复发：建议报错补一句「KDO 份交付物请写带仓前缀的全路径」。

## 修法
E040 报错文案：检测到疑似 KDO CLI 仓路径（Knowledge Delivery OS 0.0.1/ 前缀缺失）时，报错信息自动补提示「KDO CLI 份交付物请写带仓前缀的全路径，参照 #542 先例」。一行改动+回归。

## 验收
模拟场景复现提示出现；现有回归不红。

---

## 执行报告（黄药师 2026-09-06 06:00）

**交付物**
- `90_control/scripts/queue_transition.py`（新增 `_crossrepo_hint()` + E040 硬拦报错尾拼接提示——检测到疑似 KDO CLI 仓交付物缺仓前缀时，报错自动补「KDO CLI 份交付物请写带仓前缀的全路径（仓名前缀+仓内相对路径，参照 #542 先例）」）
- `90_control/scripts/tests/test_complete_deliverable_gate.py`（#653 回归 2 例：缺前缀→提示出现且硬拦不放松；vault 自有路径→不误贴提示）

**完成内容**
- E040 硬拦分支报错可操作化补全【实证】：判据=`KDO_REPO_ROOT/<路径>` 盘上存在且路径未含仓前缀（存在性核查锚 #433 口径）；拦截行为零变化（仍 `return False`），只补提示不放大放行面
- **顺带（王语嫣 05:10 划销行指定「矩阵清理并入 #653 尾部顺带」）——MOUNT-MATRIX 登记面实证核查，结论反转**【实证】：`40_outputs/capabilities/skills/MOUNT-MATRIX.md` 二节 78 个 skill 逐一对照盘面（`shared/<name>/SKILL.md` 或 `<name>/SKILL.md`），**78/78 全部存在，矩阵登记面零失真**——矩阵由 `scan_skills_registry.py` 从盘面 SKILL.md 生成，结构上不可能登记不存在的 skill；04:46 friction「research-core 登记 8 行但 skill 文件不存在」的根因判断（「矩阵生成器无存在性校验」）**不成立，无需加列**
- **真实失真在判词不在矩阵**【实证】：research-core 已实装——`40_outputs/capabilities/skills/shared/research-core/SKILL.md`（v1.1.0，status=reviewed，reviewed_by=欧阳锋）；04:47 的 `ls -d 40_outputs/capabilities/skills/research-core` 查错层级（根目录 vs `shared/` 子目录）。deep-research 确无 SKILL.md（全树 glob 零命中，仅 10_raw 素材）——宪法/挂载点措辞的 deep-research 半句仍对
- #652 任务单已追加补正节（06:00，我的报告节内追加，未动条款/终审文本/状态）：证伪「research-core 无文件」判词 + 宪法第三条 L44 与基建公告 L63 的建议修正措辞，报欧阳锋裁决（D4+审而不改，黄药师不自改宪法）

**验证**
- `python -m pytest 90_control/scripts/tests/test_complete_deliverable_gate.py -q` → 16 passed（14 存量+2 新增）【实证】
- 全量回归 `python -m pytest 90_control/scripts/tests/ -q` → **256 passed，零失败**【实证】
- 场景复现：tmp 沙盒 KDO 仓替身（monkeypatch `qt.KDO_REPO_ROOT`）写入已 commit 的 `kdo/x.py`，交付物节写裸 `kdo/x.py` → 拦截且 msg 含「带仓前缀的全路径」「#542」；vault 自有路径 `60_feedback/list.csv` → 拦截但无提示【实证】（用例 `test_653_crossrepo_hint_on_missing_prefix` / `test_653_no_hint_for_pure_vault_path`）

**边界**
- 提示只加在 E040 **硬拦分支**；E040-loose 裸路径 WARNING 分支（#625）未加——该分支本就不拦，措辞噪音收益低，需要时另开微单
- `90_control/kdo-seed/seed/90_control/scripts/queue_transition.py` 种子副本未同步（其本就落后数代，无 #569/#653 提示）——种子维护不属本单
- 宪法第三条 L44 / 基建公告 L63 的 research-core 措辞**未自改**：#652 在 pending_review 中、条款为全 agent 约束文档（D4 自我修改门禁+审而不改），修正建议已落 #652 补正节待欧阳锋/王语嫣拍板
- 流程瑕疵如实留痕：queue_transition.py 改动起草于 claim #653 **之前**（05:44 前后，探查 #504 窗口期间顺手）——应 claim 后施工，此处声明；改动范围未超本单任务书边界
- 真实仓路径 `C:\Users\Administrator\Knowledge Delivery OS 0.0.1` 下现存的同型裸路径交付物不受影响——门禁提示只在下次触发 E040 时出现

**需要谁动作**
- 欧阳锋：①终审本单 ②#652 补正节所提宪法第三条 L44 + 基建公告 L63 措辞修正裁决（建议措辞已附）
- 王语嫣：04:46 friction 划销行结论需修正——「research-core 登记 8 行但 skill 文件不存在」「矩阵生成器无存在性校验」两项均被本次实证推翻；矩阵零失真，无需 scan_skills_registry.py 加列
- skills-assistant（经王语嫣编排）：research-core 已实装在库但未挂载为 CLI 会话可调用 skill——是否挂载/如何暴露给 CLI 端，归 #587 域拍板

**存在性核查**（#433 口径——本报告负向判词的核查锚点）

| 负向判词 | 核查动作与锚点 |
|:--|:--|
| MOUNT-MATRIX 无失真行（78 个登记 skill 均有 SKILL.md） | Python 逐行对照：矩阵二节正则提取 78 名 → 逐个 `shared/<n>/SKILL.md` / `<n>/SKILL.md` exists() → missing=[]（2026-09-06 05:5x 实跑，脚本内联于会话） |
| research-core 无实装文件之旧判词为假 | `ls 40_outputs/capabilities/skills/shared/research-core/` → JUDGEMENT.md + SKILL.md（15968B，09-03 04:47）+ manifest.yaml |
| deep-research 无 SKILL.md | `Path("40_outputs/capabilities/skills").glob("**/SKILL.md")` 过滤 deep-research → 命中=[] |
| KDO CLI 仓内无 queue_transition.py 副本（不存在同源双改风险） | `find "C:/Users/Administrator/Knowledge Delivery OS 0.0.1" -name "queue_transition.py" -o -name "queue_gate.py"` → 零命中；vault 侧仅 `90_control/scripts/`（在修）+ `90_control/kdo-seed/seed/`（种子，落后未同步） |
| 本会话可调用 skill 清单无 research-core | 本会话环境 available skills 列表仅含 business-research（非 research-core）——登记面≠会话可用面的直接证据 |

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 2 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）
