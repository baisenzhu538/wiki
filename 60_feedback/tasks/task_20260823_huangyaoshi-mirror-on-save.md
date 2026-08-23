---
id: 464
assignee: huangyaoshi
status: queued
updated_at: '2026-08-23T10:35:00+00:00'
version: v1.0
doc_id: D-20260823-005
---
# #464 记忆胶囊镜像保存后联动（save→log→mirror 一条链）

- **任务号**：#464
- **状态**：queued
- **assignee**：huangyaoshi（基建单一实例；终审=欧阳锋；编排=王语嫣）
- **优先级**：P1（老朱 2026-08-23 拍板镜像时间锚：**保存后联动**——#427 拍板 A+B 时所欠时间锚就此结清）
- **立项**：2026-08-23 王语嫣（B 镜像过期 P1 事件的根治：手动 mirror 只补当前窗口，联动才是长期机制）

## 设计（事件联动，非 cron）

- **挂钩点**：daily-context-save.py 成功保存后 → 现有动作「写 L0 事件」之后追加「自动 mirror」——save→log→mirror 一条链
- 失败可见（#434 同款）：mirror 失败不阻断 save 返回，但 stderr 醒目报警+落失败日志（下次 save 重试或手动补）
- 不注册常驻计划任务（schtasks 零依赖——事件驱动；#432 边界「不注册常驻计划任务」与老朱时间锚口径一致收敛）
- verify 联动提示：mirror 后顺带跑轻量 verify，不一致即报警（治 backup-stale 复发）

## 验证（验证分层声明）

- L1 单测（联动触发/失败可见/幂等）；L2 狗粮=一次真实 daily-context-save 后 B 镜像 ts 追平 A+verify PASS；L3 待活体=次日复盘保存后镜像自动追平

## 边界

- 只动 daily-context-save 挂钩链，不碰 memory_capsule.py 核心命令；与 #463（L1 全量采集）分线并行
- 当前窗口的手动 mirror 补缺已另行通知（修 #460 同批）——本单是长期机制

## 执行报告（F-034 五字段+验证分层声明，complete 前必填）

（生产者填写）
