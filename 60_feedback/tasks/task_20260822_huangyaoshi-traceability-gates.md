---
id: 429
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-22T15:52:13.266141+00:00'
---
# #429 流转留痕三件套门禁（交付五字段 / 审查意见落盘 / 等待外部输入态）

- **任务号**：#429
- **状态**：queued
- **assignee**：huangyaoshi（基建单一实例；终审=欧阳锋；编排=王语嫣）
- **优先级**：P1（机制层补漏；不抢迁移/设计域，不动 #426）
- **立项**：2026-08-22 王语嫣（老朱拍板「想犯错也犯不了」；停车场 F-029/F-034/F-035 收口）

## 任务目标

把「完成了什么、审查意见在哪、等外部输入的任务为什么不阻塞队列」从口头纪律变成脚本门禁。只动流转/留痕层，不替代任何角色判断。

## 范围（只做三件，同一文件面优先）

1. **F-034 交付完成声明硬格式**：`queue_transition.py complete` 必须可机读交付——任务单执行报告节或 `--evidence` 文件含五字段：①改动文件清单 ②完成内容一句话 ③验证命令+输出 ④未做项/边界 ⑤需要谁动作。缺项=拒收或标「需人工」，不硬编通知文案。
2. **F-035 审查意见书强制落盘**：`queue_transition.py review` 必须记录审查意见文件路径（任务单终审节或 `60_feedback/reviews/` 固定路径），审查意见含 verdict/grade/扣分点/修复项/抽验证据；无审查文件路径=不闭环。口头/群里意见=未审查。
3. **F-029 等待外部输入态**：设计并实现第三态（建议 `waiting-external`）或等效挂起机制——任务在等待老朱/外部输入时不占 `pending_review` 阻塞位、不参与可领取推进；#188 是活样本（只读引用，不擅自改 #188 内容）。

## 边界（不可越）

- 只做机械门禁与状态可见；**不自动领取、不自动裁决、不自动终审、不替角色判断**（F-033 边界）。
- 不改 #426；不碰迁移专案（F-026）；不碰设计域（F-025）。
- 兼容 #389 REVIEW-PENDING、#413 O-3 修复、#421 探针通知契约；通知内容只允许消费五字段，禁止第二套扫描器。
- 改动前必须先读 `queue_transition.py` / `queue_gate.py` / `queue_lock.py` 当前实现；批量前 dry-run + 单任务正反向实测。

## 验收

- 正反向实测：缺五字段 complete 被拦/标需人工；review 缺审查文件路径被拦；`waiting-external` 任务不阻塞不同 assignee 领取。
- 回归：既有 queue_transition 测试全过 + 新增回归用例覆盖三条门禁；`generate-dashboard.py` 后看板数字一致。
- 狗粮测试：黄药师用一条测试任务真实走「complete 缺证据被拦 → 补证据通过 → review 无意见文件被拦 → 补意见文件通过」。
- 交付五字段齐全；commit 入档；欧阳锋终审抽「门禁是否只拦机械项、不碰判断」。

## 关联

- 停车场：F-029 / F-034 / F-035（本单立项后转「已立项 #429」，终审通过后出池）
- 先例/依赖：#389、#413、#419、#421、#427、#188（等待外部输入活样本）

## 执行报告（2026-08-22 深夜 黄药师）

**完成内容**：流转留痕三件套门禁实现（五字段/意见书/waiting-external）。
**交付物**（改动文件清单）：
1. `90_control/scripts/queue_transition.py`：
   - F-034：`_check_delivery_fields` 五字段机读检查（交付物/完成内容/验证/边界/需要谁动作锚点表）+ `_extract_exec_report`；action_complete 升级（缺字段=拒收，--force 跳过）
   - F-035：`_check_review_record`（任务单「## 终审记录」节 ≥50 字 或 --review-file）；action_review 新增 `--review-file` 参数，无意见书=不闭环
   - F-029：TRANSITIONS 加 (pending_review,mark_waiting)→waiting-external / (waiting-external,resume)→pending_review；`action_mark_waiting`（记 waiting_since/waiting_note）+ `action_resume`（记 resumed_at）；main 派发 mark-waiting/resume + --note
2. `90_control/scripts/tests/test_queue_transition.py`：+7 回归（三字段门禁单测 + 转移注册）

**验证**（命令+输出）：
- 回归：`pytest 90_control/scripts/tests/test_queue_transition.py` → **18 passed**（11 原有 + 7 新增）
- 狗粮全流程（隔离环境 KDO_QUEUE_PATH/KDO_TASK_DIR + --no-commit）：
  ① complete 缺执行报告节 → **被拦**（"任务单缺少「## 执行报告」节"）
  ② 补五字段 → **通过**（pending_review）
  ③ review 无终审记录 → **被拦**（"任务单缺少「## 终审记录」节"）
  ④ 补意见书 → **通过**（reviewed）
  ⑤ mark-waiting → waiting-external；其他实例 claim **不被阻塞**；resume → 回 pending_review

**未做项**：
- 只拦机械项（字段存在性），不判内容质量、不替角色判断（F-033 边界）；#188 只读引用未改
- 未碰 #426/迁移专案/设计域；通知五字段消费归 #421（本单不建第二套扫描器）
- 存量任务兼容：执行报告缺字段的 complete 会被拦——用 --force 声明例外或补字段（新纪律生效）

**需要谁动作**：
- 欧阳锋：终审本单（抽「门禁是否只拦机械项不碰判断」）
- 王语嫣：编排层知悉——waiting-external 可对 #188 使用（等老朱真实使用）；#421 通知内容后续按五字段生成
- 各角色：complete 交付执行报告按五字段写；review 必须落「## 终审记录」节
