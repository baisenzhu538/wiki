---
id: 434
assignee: huangyaoshi
status: queued
updated_at: '2026-08-23T01:05:00+08:00'
---
# #434 记忆胶囊 L0 自动写入端（daily-context-save 挂钩，方案 A）

- **任务号**：#434
- **状态**：queued
- **assignee**：huangyaoshi（基建单一实例；终审=欧阳锋；编排=王语嫣）
- **优先级**：P1（F-027 下一阶段；老朱 08-23 拍板：自动化提取是必须的，L0 不能靠手动 log）
- **立项**：2026-08-23 王语嫣（黄药师建议书 `diag_20260823_huangyaoshi-capsule-l0-automation-proposal.md` 裁定采纳；序列：#433 → #434）

## 任务目标

把 L0 从「手动 log 能写」升级为「会话结束自动留痕」：每次 `daily-context-save.py` 保存成功（🟢/🟡 自检）即自动写一条 L0 事件（agent/session/复盘路径/hash）。单写入面，不新造扫描器。

## 范围

1. **方案 A 先行**：改 `kdo-tools/daily-context-save.py`，save 成功后调用 `memory_capsule.py log` 写 L0 事件；字段含 agent_id/session_id/ts/event_type=review_saved/复盘路径/content_hash/自检等级。
2. **不重复建设**：不做 conveyor_probe 式新扫描器（方案 B 缓议，仅作 A 失效兜底）；不做 Hermes gateway 回调（方案 C 挂 F-033 同族）。
3. **失败可见**：L0 写入失败不阻断复盘保存，但必须 stderr 醒目报警 + 写 `90_control/pending-git-commits.log` 同级的待收口记录（或既有失败通道），禁止静默吞。
4. **权责登记**：黄药师=胶囊建设/维护；风清扬=胶囊数据与成果的维护检查与审计（不实施）。该划分写入 `20_memory/memory-registry.md` 或 F-027 后续任务单口径，不写 KB 卡。

## 边界

- 只做写入端自动化；L1 摘要/L2 洞察/L3 沉淀仍留 F-027 后续。
- 不改复盘正文格式；不影响 review-check 自检；不改 #433 负向判词门禁范围。
- 风清扬不实施；老朱确认前不注册镜像常驻计划任务（#432 遗留项仍待确认）。

## 验收

- 狗粮：跑一次 `daily-context-save.py save --agent <test> --truman --file <sample>`（或等效测试），L0 自动新增一条事件；`memory_capsule.py status/verify` 能看到。
- 正反向：save 成功写 L0；L0 路径暂时不可写时报警可见且复盘保存不被静默吞。
- 交付五字段（F-034）+ 审查意见落盘（F-035）+ commit 入档；欧阳锋终审抽「单写入面/失败可见/不越权」。

## 关联

- F-027：#432（L0 最小实现，待终审）→ 本单 #434（自动写入端）；L1-L3 后续另单。
- #427 拍板 A+B/C 缓议；#433 负向判词门禁先序；F-033 只收方案 C 同族，不开工。
