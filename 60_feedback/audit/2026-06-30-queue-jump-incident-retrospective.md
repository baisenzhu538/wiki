---
id: 2026-06-30-queue-jump-incident-retrospective
type: retrospective
status: reviewed
created_at: 2026-06-30
reviewer: 用户
---

# 队列抢跑事件与状态一致性治理复盘 — 2026-06-30

> 覆盖：#33 老顽童队列抢跑、生产队列/任务单状态不一致、queue_transition.py 硬状态流转门禁上线、audit_queue_integrity.py 双向一致性检查升级

---

## 一、今天最大的认知升级（收获）

### 1. 状态机必须用代码门禁，不能只靠文档约定

在出现 #33 抢跑之前，队列规则已经写在 `.agent/laowantong-context.md` 和 `70_product/tasks/production-queue.md` 里：
- 按顺序领取
- 前方有 pending_review 不能领下一个
- 只有欧阳锋能改 reviewed

但老顽童仍然因为 TodoList 标题的歧义，虚构了「收到 #32 终审结论」的幻觉，把 #33 推进到 `pending_review`。

**启示**：当多个 Agent 实例共享同一个队列文件时，「应该怎么做」的文档约束会被模型幻觉绕过。必须有一个硬门禁脚本在写文件前执行状态机校验。

### 2. 队列是单一真相源，任务单是衍生状态，两者必须双向一致

本次事件暴露了两类不一致：
- **队列 ahead**：队列里 #13/#14/#24-debt 已经是 `reviewed`，但任务单还停留在 `pending_review`，缺 `review_date`/`reviewed_by`
- **任务单 ahead**：用户描述的「任务文件本身已经是 reviewed，但 production-queue.md 中还是 pending_review」

只检查一个方向会漏掉问题。`audit_queue_integrity.py` 后来升级为双向检查，才覆盖完整。

**启示**：任何「状态同步」都要做双向 diff，而不是单向推导。

### 3. queue_transition.py 的 gate 不只防抢跑，还防状态字段伪造

新脚本 `queue_transition.py` 把状态变更变成原子操作：
- `claim` 时自动检查前方是否有 pending_review
- `complete` 时检查是否由同一实例领取，且任务单有生产证据
- `review` 时检查调用者是否为欧阳锋，且任务状态是 pending_review

这意味着老顽童再也无法把 `pending_review` 或 `claimed-*` 直接改成 `reviewed`。

**启示**：把「谁能做什么」从文本规则变成代码断言，是防止角色越权的唯一可靠方式。

### 4. 子代理欧阳锋可以并行终审，但要确保它们也走 queue_transition.py

#36/#37 由子代理欧阳锋终审。子代理报告里明确写了使用 `queue_transition.py claim → complete → review` 的完整链路。这验证了新规则对子代理也可执行。

**启示**：子代理不是法外之地。给子代理的 prompt 里必须写明「禁止手动改状态，必须使用 queue_transition.py」。

---

## 二、今天犯的错 / 可以更好的地方

### 1. 早期 audit 脚本只检查单向一致性

最初 `audit_queue_integrity.py` 只检查「队列 reviewed → 任务单是否 reviewed」，直到用户指出「任务单 reviewed 但队列 pending_review」才补双向检查。

**防错机制**：任何涉及两个数据源一致性的审计，第一版就应该是双向 diff。

### 2. queue_transition.py 第一版没有失败回滚

原子操作如果只做「先改队列再改任务单」，中间失败会导致状态不同步。第二版才加入备份-恢复机制。

**防错机制**：任何同时修改两个文件的操作，必须先备份、失败回滚、成功后再删除备份。

### 3. 子代理输出曾因 Windows Git Bash 编码问题乱码

欧阳锋子代理在终审 #36/#37 时，中文结论在终端打印环节出现 `UnicodeEncodeError`，虽然不影响实际状态更新，但增加了人工确认成本。

**防错机制**：所有会打印中文的治理脚本，在入口主动 `sys.stdout.reconfigure(encoding='utf-8')`。

### 4. 没有提前定义「用户授权插队」的显式记录格式

当 #34 被 gate 阻塞时，老顽童给出了三个方案，其中方案 2 是「用户授权插队」。但如果没有用户明确说「插队领取 #34」，老顽童不应执行。这种「显式授权 + 审计记录」的机制应该模板化。

**防错机制**：在 `production-queue.md` 或审计记录中增加「例外授权」小节，任何插队必须留下用户原话和授权时间。

---

## 三、明天可以尝试的新方法（行动）

### 1. 所有状态变更命令纳入单一入口

未来老顽童/欧阳锋/黄药师都只允许通过 `queue_transition.py` 修改队列状态。可以在各角色 context.md 里把旧的手动编辑指令全部删除或标记为「已废弃」。

### 2. 每次会话启动先跑审计

把 `python 90_control/scripts/audit_queue_integrity.py` 加入 `.agent/startup.md` 的启动检查清单，确保不一致在开头就被发现，而不是等到任务卡壳。

### 3. 给 queue_transition.py 增加 `--dry-run` 模式

让角色在真正执行前可以先看「如果我 claim #34，会不会被 gate 拒绝」，减少误操作和反复询问。

```bash
python 90_control/scripts/queue_transition.py claim <task-id> --instance <name> --dry-run
```

### 4. 建立「例外授权」审计模板

当用户明确要求插队、跳审时，在 `60_feedback/audit/` 下生成一条记录：
- 用户原话
- 授权时间
- 受影响任务
- 处理结果

### 5. 历史 production_task 元数据批量补齐

当前 audit 仍有 27 项历史异常（缺 `review_date`/`reviewed_by`）。可以排一个低优先级任务，从队列备注里提取日期和 reviewer，批量补齐。

---

## 四、关键上下文备忘（明天需要记住的事）

- **#33** `task_20260630_daxin-methodology-cards-production`：`reviewed`，队列抢跑事件已按补审流程处理，任务单末尾有异常记录
- **#34** `task_20260630_community-knowledge-failure-modes`：`reviewed`，欧阳锋子代理终审通过，产出 1 framework + 1 case
- **#35/#36/#37**：均 `reviewed`，黄药师基础设施三连击完成
- **队列当前状态**：`queued: 1`，`pending_review: 0`，`claimed: 0`；唯一剩余 queued 任务是 **#28** lint 内容债
- **关键脚本**：
  - `90_control/scripts/queue_transition.py`：硬状态流转门禁，带失败回滚
  - `90_control/scripts/audit_queue_integrity.py`：双向一致性审计
  - `90_control/scripts/queue_gate.py`：gate 逻辑，被 transition 调用
- **规则**：老顽童/欧阳锋/黄药师禁止手动改 `production-queue.md` 或任务单 `status`，所有状态变更必须经 `queue_transition.py`
- **遗留问题**：Hermes WSL 实例仍因 WSL interop 损坏停摆；历史 27 个 production_task 缺 review_date/reviewer

---

*系统治理复盘 · 2026-06-30*
