# 传送带探针通知契约（#421 · X-1 拍板成文）

> 2026-08-22 会诊 X-1 拍板要素成文。实现：`kdo-tools/conveyor_probe.py`（单扫描器）。
> 更新需经编排层；契约本身只读。

## 一、三类信号

| 信号 | 触发 | 收件人 | 消息形态 |
|:--|:--|:--|:--|
| **新提审** | 队列 REVIEW-PENDING 新增（queue_transition 流转） | 欧阳锋 | "M 个待审"（列任务号） |
| **批次待续** | queued 任务新增（相对上次快照） | 老顽童 | "N 个可领取"（列任务号） |
| **新建议书到达** | diagnosis/ 三元组命中且新登记 PROPOSAL-PENDING | 王语嫣 | "新建议书待裁定"（列文件名） |

不区分三类信号 = 通知变骚扰（欧阳锋，X-1）。

## 二、调度与打扰红线

- **扫描**：Windows 计划任务 `kdo-conveyor-probe`，每 10 分钟（与 kdo-inbox-watch 同频）
- **通知**：变化触发 + 幂等去重（state 记已通知集合，同 id 不重推）；无变化不发
- **夜间静默**：22:00–08:00 不推通知（登记照常做）
- **聚合去抖**：同一信号同批只推一条聚合消息，不逐条轰炸

## 三、状态口径（唯一真相源）

- 队列状态：只认 `queue_transition.py` 的状态机（探针经 `queue_gate.parse_queue` 读队列文件快照，自身零流转能力）
- 建议书检出：只认 `yaml.safe_load` 结构化解析 frontmatter 三元组（`audience: 王语嫣` + `status: pending_orchestration`，`proposal-*` 文件名辅助）——禁 grep/正则（E017）
- 扫描面写死：`60_feedback/diagnosis/`

## 四、边界硬编码（不可突破）

- 探针**只通知、只登记**（PROPOSAL-PENDING 自动登记与 watch_inbox INBOX-PENDING 同类豁免）
- 探针**不领取、不裁决、不流转**——代码层无 claim/review/complete 能力（import 面验证：不引用 queue_transition 写路径）
- 通知≠裁定：探针推给王语嫣，裁定仍是她（B2-1）
- 登记幂等：路径级去重，重跑不重复写

## 五、通道与失败处理

- **通道**：飞书群机器人 webhook，配置 `kdo-tools/.feishu_webhooks.json`（`{"wangyuyan": "<url>", "laowantong": "<url>", "ouyangfeng": "<url>"}`，URL 不进 git）
- 配置缺失 → **dry-run 打印**（不静默失败、不假装已发）
- 发送失败：重试 1 次，仍失败落 `kdo-tools/.conveyor_failures.log`（下次扫描重试幂等）

## 六、同源纪律（E021/E028 同族教训）

- **登记与通知同源**：一次扫描事件 → 检出（单份逻辑）→ 登记 → 通知，禁止第二套扫描器
- #425 健康度指标 8（未登记建议书计数）只读计数不代登记，与本探针职责分离；检出判定口径同源（yaml.safe_load 三元组）
