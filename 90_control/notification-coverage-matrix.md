# KDO 通知覆盖矩阵（基础设施总账 v1）

> 王语嫣 2026-08-26 建。缘起：老顽童建议书断言「终审落点无任何通知」，实际机制早已存在（#462/#521），
> 编排者无总账无法当场证伪——机制是二十多张单累积建成，碎片化记忆靠不住。
>
> **纪律**：凡新增/修改事件类型或通知通道的任务单，交付时必须同步更新本矩阵（验收项之一）。
> 王语嫣巡检照矩阵逐项核对，不再凭记忆。

## 事件 × 通道 × 角色

| # | 事件 | 检测源 | 通道 | 接收人 | 夜间静默口径 | 建设依据 |
|---|------|--------|------|--------|--------------|----------|
| 1 | 新 queued（可领取） | conveyor_probe `_queue_signal` | todos 推送 | assignee 路由（未知回落 laowantong） | 静默期 defer 天亮补发 | #501/#443 |
| 2 | 新提审（pending_review） | conveyor_probe | 叫醒推送 | 欧阳锋 | 豁免（终审类） | #421/#520 |
| 3 | 终审 PASS（reviewed） | conveyor_probe `new_reviewed` | todos 推送 | assignee + 抄送王语嫣 | 豁免（终审类） | #462/#521 R1/R2 |
| 4 | 终审退回 FAIL（failback） | conveyor_probe `new_failback` | todos 推送 | assignee 路由 | defer（未豁免，观察项 O1） | #462；#538 补「曾 reviewed」场景 |
| 5 | 门禁拦截（gate-blocked） | conveyor_probe | 推送+看板登记 | 王语嫣 | — | #460 |
| 6 | 建议书登记（三元组命中） | conveyor_probe `_scan_proposals` | 推送+PROPOSAL-PENDING 登记 | 王语嫣 | — | #421/#506 |
| 7 | 审查意见 🟠/🟡 无落点 | conveyor_probe F-036 | 推送 | 欧阳锋 | 不豁免 | F-036 第七信号 |
| 8 | near-miss 三元组违例 | conveyor_probe `_proposal_near_miss` + `_escalate_near_miss` | 仅日志 print + **≥3 轮未修正升级推王语嫣收件箱**（修正自动消项） | 王语嫣 | defer（非终审类） | ✅ #536 销项 |
| 9 | inbox 新素材 | watch_inbox `_notify_inbox` | 看板待编排区 + **王语嫣收件箱推送** | 王语嫣 | defer（P0 也静默落盘带 🔕） | ✅ #530 销项 |
| 10 | friction 事件 | conveyor_probe `_scan_friction` | memory_capsule 事件层 | 复盘层可见 | — | #511 |
| 11 | 基础设施单 reviewed 总账未同步 | conveyor_probe `_matrix_sync_check`（第七信号） | 推送 | 欧阳锋+抄送王语嫣 | defer（非终审类） | #537（本单=元狗粮首查对象） |
| 12 | VLM/OCR 卡缺两段式隔离 | kdo pre-submit `_check_vlm_two_section`（#540） | pre-submit WARNING（提审输出可见） | 生产者 | — | #540（WARNING 起步，存量批次王语嫣裁定） |
| 12 | 终审改判（review --override，reviewed→queued） | queue_transition | 任务单改判记录节+台账（--reason 必填）+failback 通知 | 改判权=终审者专用 | — | #538（⚠️交付漏登，第七信号真阳性拦获，王语嫣 08-26 补登） |
| 13 | 检索结果低置信/冲突警告 | kdo_search 输出字段（confidence_flag/trust_level/conflict_warning）+标题后缀 | MCP 检索响应（消费 agent 可见） | 全体消费 agent | — | #541（trust 加权排序+conflict_with 警告，协议互链 consumer-retrieval-protocol） |
| 14 | source_refs 死引超基线 | check-source-refs（health-check 每日 02:07，--max-missing 1024/--max-contaminated 8 阈值制） | health-check FAIL + 报告落盘 60_feedback/analysis/source-refs-health-latest.{md,json} | 黄药师（治理）/王语嫣（阈值下调裁定） | — | #543（行号锚剥除+聚类治理报告；治理批次待王语嫣裁定） |
| 15 | 胶囊写入失败/只读自愈 | memory_capsule `log_event_safe`（#545：清只读属性自愈+退避重试+取证升级） | stderr + pending-git-commits.log（含 payload+db/wal/shm 属性快照） | 黄药师 | — | #545（readonly 复发 14 次根因取证：db 被外部置只读属性，置位者未抓到现行=环境性） |
| 16 | 产卡概念交叉验证 WARNING | kdo pre-submit `_check_concept_crosscheck`（#542：正文命中已有 concept/framework 概念词→提示对账，词表自动构建+mtime 缓存） | pre-submit WARNING（提审输出可见，不拦截） | 生产者 | — | #542（小昭事故根因 3 降档版：机器做存在性，人做正确性） |
| 17 | 终审权校验拒止（未登记实例 review） | queue_transition `_check_review_authority`（#546：cwd 无 ouyangfeng 登记 → 拒止；force 逃生落 force 台账） | 终端拒止提示 + gate-blocked 台账（第五探针可见） | 欧阳锋（登记一次即可） | — | #546（一具两职事件根治轻量版；登记表 .kdo/active-instances.json 供探针活性展示） |
| 18 | 基建停拍报警（l1-capture/conveyor/inbox-watch 停拍>2×周期） | conveyor_probe 第九信号 `_scan_infra_liveness`（10 分钟级，跨越沿幂等） | 推王语嫣 + gate-blocked.log 台账 | 王语嫣 | defer（夜间静默口径不动，台账恒写） | #547（console-killer 事件防复发；17h 延迟教训：health-check 日级太慢） |
| 19 | token 日计量汇总 | token_meter.py（挂 kdo-health-daily 02:07；三引擎增量游标，不回溯历史） | 日汇总落 60_feedback/analytics/token-usage-*.md/json + 事件层 token_usage | 黄药师/风清扬（#514 基线接口） | — | #549（只计量不限制；配额熔断属 F-055 阶段 2/3） |
| 20 | 角色时钟唤醒（【叫醒】） | role_clock.py（schtasks kdo-role-clock 5min；pace 到点/欧阳锋事件驱动） | todos/<role>.md 恒落 + active 实例 feishu 适配；唤醒日志 .kdo/role-clock.log（不进胶囊——防 on_duty 自欺） | 全角色 | 不适用（唤醒本身就是在岗激活器） | #553+#555（四角色全开通：老顽童15/王语嫣30/风清扬720/欧阳锋事件驱动；会话级 cron 已换轨停用；误发>漏发，降级不切执行权） |
| 21 | 待老朱拍板上浮（reviewed + 拍板关键词） | conveyor_probe 第八信号 `_scan_pending_decision`（关键词前挂形态：老朱拍板/待老朱/需老朱/待拍板/需拍板/请老朱/待你拍板；向前生效 20260827 不回扫存量；队列侧只匹配备注列防名称列自举） | 新增即时推飞书 wangyuyan 群（老朱在群实测可达，本人 08-27 确认）+ todos 落盘 + daily-audit-digest ⑤「待你拍板」固定栏（每日在列直到字样移除/状态离开 reviewed 自动消项） | 老朱 | 无在岗 defer 同 #550 统一口径 | #556（#525 拍板断链两天实证；干跑校准：bare「拍板」命中已决归因→改前挂形态，「老朱已拍板」天然不匹配；消项不推送仅 stdout 留痕） |

## 缺口台账

- ~~**G1**：near-miss 只留日志不推送~~ → **已销项（2026-08-26 #536）**：≥3 轮未修正升级推王语嫣收件箱+修正自动消项+静默 defer 天亮补发，回归 4 例锁定
- ~~**G2**：inbox 素材检测到→只写看板~~ → **已销项（2026-08-26 #530，终审 PASS A）**：检测到即推王语嫣收件箱，幂等同 scan 判重键
- **O1（观察项）**：FAIL 退回通知夜间静默 defer 到天亮——FAIL 是「返工优先」却延迟送达，口径待裁（非阻塞，夜间本就不开工）。#535 已加收件箱置顶，推送层 defer 口径仍留本项

## 消费端纪律（机制送达 ≠ 被消费）

- 角色时钟扫描必须包含**自己的 todos 收件箱**，myqueue 只读视图不能替代（2026-08-26 老顽童实证：#531 终审通知躺收件箱 15 分钟未察觉）
- 通知类任务验收必须含「消费端知晓验证」：交付时向接收角色收件箱落一条使用说明，不只验发送端落盘（W 口径，随 #530/#535 起生效）
