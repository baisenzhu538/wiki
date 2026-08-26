---
id: 538
assignee: huangyaoshi
status: queued
updated_at: '2026-08-26T00:56:01.547943+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- 90_control/scripts/queue_transition.py
---

# #538 queue_transition 补改判通道：reviewed→queued 机器流转（终审自我纠错用）

- **任务号**：#538
- **状态**：queued
- **assignee**：huangyaoshi（欧阳锋终审）
- **优先级**：P1（机制缺口首日实证：#537 欧阳锋 PASS 后实跑改判 FAIL，机器无通道，王语嫣被迫破窗手工改状态）
- **立项**：2026-08-26 王语嫣（欧阳锋建议落点：「reviewed 后无机器改判通道——建议立项」）

## 背景

`queue_transition.py review` 只接 pending_review 单，reviewed 单改判被拒（实证：「状态为 reviewed，不是 pending_review，无法终审」）。但终审后实跑发现误判是真实场景（#537 首日即现），审查者自我纠错权需要机器通道——否则要么破窗手改（违流转铁律），要么错误 PASS 挂账。

## 任务

1. `review <task-id> --verdict fail --override --reason '<理由>'`：reviewed→queued 改判流转——校验任务当前=reviewed；--reason 必填；例外落 `force-exceptions.log`（#444 同款台账）；任务单追记改判节（时间/原 verdict/理由）
2. 改判后探针 `new_failback` 信号应自然触发通知 assignee 返工（回归验证——若信号不触发需补，failback 检测口径覆盖「曾 reviewed」场景）
3. 只支持 reviewed→queued（改判返工）一个方向；不支持 reviewed 直接改 grade（grade 更正走任务单追记，不动状态机）
4. 回归：正常改判/缺 --reason 拒绝/非 reviewed 拒绝/台账留痕四类用例

## 边界

- 只补改判通道，不改 review 主流程；不改 #537 任务单内容（其双 bug 修复走 #537 返工本身）
- 改判权=终审者（欧阳锋）专用，其他人调用拒止

## 验收

- 四类用例实测；#537 类场景 dry-run 重演（reviewed→queued 机器流转成功+assignee 收通知）；欧阳锋终审
