---
name: queue-transition
title: "queue-transition——生产队列唯一状态流转入口（claim/complete/release/review）"
description: |
  KDO 生产队列唯一状态流转入口：claim / complete / release / review / status / myqueue。
  所有队列状态变更必须走本脚本——手改 production-queue.md 状态列或任务单 status = 违规。
  含完整 task_id 寻址、F-034 五字段执行报告门禁、E040 交付物入仓门禁、--evidence 传文件口径。
  领单失败/提审被拦时先读本 skill，不要猜参数形态。
category: kdo-infrastructure
version: 1.0.0
related_skills:
  - review-chain
  - kimi-headless-launch
encapsulates: 90_control/scripts/queue_transition.py
tags:
  - audience:all-agents
  - scene:queue-transition
  - 队列状态流转
  - 领单提审
status: draft
reviewed_by: 待审
review_date:
grade:
updated_at: 2026-09-06
trigger:
  natural_language:
    - 领任务/领单/claim
    - 完工提审/complete/交卷
    - 释放任务/release
    - 队列状态流转/队列状态机
    - 报错「任务不在生产队列中」
    - complete 被 F-034 / E040 拦截
    - --evidence 怎么传
    - 任务单 status 怎么改
---

# queue-transition：生产队列唯一状态流转入口

> **一句话**：队列状态只此一条路——`python 90_control/scripts/queue_transition.py <动作> <task-id> --instance <角色名>`。脚本拒绝 = 绝对不能执行，更不能手改文件绕过。

## 何时用

- 领取队列任务（`queued` → `claimed-<实例>`）
- 生产完成提审（`claimed-<实例>` → `pending_review`）
- 做不完释放回队列（`claimed-<实例>` → `queued`）
- 终审（欧阳锋/王语嫣专属：`pending_review` → `reviewed`）
- 任何「我想改 production-queue.md 的状态列」的念头——**改法就是跑本脚本，不是编辑文件**

## 怎么调（命令 + 参数）

前置：`cd C:\Users\Administrator\Desktop\wiki`（vault 根目录）。PyYAML 必需。

```bash
# 看队列全景（只读，安全）
python 90_control/scripts/queue_transition.py status

# 看某角色名下的任务（只读，安全）
python 90_control/scripts/queue_transition.py myqueue laowantong

# 领取（合法前置状态：queued）
python 90_control/scripts/queue_transition.py claim <task_id> --instance <角色名>

# 完成提审（合法前置：claimed-<同一实例>）
python 90_control/scripts/queue_transition.py complete <task_id> --instance <角色名> --evidence <文件路径>

# 释放回队列（合法前置：claimed-<同一实例>）
python 90_control/scripts/queue_transition.py release <task_id> --instance <角色名>

# 终审（审查者专属）
python 90_control/scripts/queue_transition.py review <task_id> --verdict pass|fail --reviewer 欧阳锋 --grade A|A-|B+|B|B-|C --review-file <意见书路径>
```

### 参数表

| 参数 | 语义 | 红线 |
|:--|:--|:--|
| `<task_id>` | 完整任务文件名，如 `task_20260906_laowantong-encapsulation-t1` | 纯数字 seq（`658` / `#658`）现也可解析（#647 修）——但只认**队列行里存在**的 seq；最稳姿势仍是传完整 id |
| `--instance` | 实例名 = **裸角色名**（`laowantong`，不是 `kimi-laowantong`） | #620 老朱铁律：工具=变量不进名字；claim/complete/release 必填，且必须同一实例 |
| `--evidence <路径>` | 佐证附件，**只收文件路径，不收内联文本** | 只验证可读性，不能替代任务单里的五字段执行报告（#444）；惯用值=任务单自身路径 |
| `--sequence` | 同执行者多单连发窗口（#655）：编排指令含多单、complete 前单后接下一单时用 | 只豁免「自己的 pending_review 阻塞」；他单 pending / 他人 claimed 锁照旧拦截，不走 force 台账 |
| `--force` | 跳过拦截（claim 跳过队首阻塞；complete 允许 queued 直跳 pending_review） | 例外动作，配 `--reason '<理由>'` 留痕台账 `90_control/force-exceptions.log`（#444） |
| `--no-commit` | 跳过流转后的自动 git 收口 | #390 逃生门，特殊场景才用 |
| `--override` | reviewed → queued 改判通道（#538） | 仅 review 动作，需 `--verdict fail --reason` |

### 其他动作

```bash
python 90_control/scripts/queue_transition.py register <instance>   # 纯审查角色上岗登记（不 claim）
python 90_control/scripts/queue_transition.py mark-waiting <task_id> --note '<原因>'  # 长任务挂等待
python 90_control/scripts/queue_transition.py resume <task_id>      # 解除等待
python 90_control/scripts/queue_transition.py cancel <task_id> --instance <角色名> --reason '<原因>'
```

## 边界与红线

1. **禁止手改** `production-queue.md` 状态列、任务单 frontmatter `status`/`reviewed_by`/`review_date`。原子性和合法性由脚本保证。
2. **脚本拒绝 = 不能执行**。常见拒绝：目标状态不合法 / 队首有 `pending_review` 未清 / 前方有 `claimed-*` 未释放 / 任务不是你的 `claimed-<实例>` / 五字段或交付物门禁未过。逐条对照处理，不要换路径硬闯。
3. **角色边界**：`review` 只有审查者能跑；生产者把任务推进到 `pending_review` 即止。TodoList 标题用动作性写法（「#N 完成生产并更新为 pending_review」），禁写「#N 终审通过」。
4. **`complete` 两道硬门禁**（被拦是常态，按提示补即可）：
   - **F-034 五字段执行报告**：任务单必须有「## 执行报告」节，五个粗体锚词各起一行——`**交付物**`、`**完成内容**`、`**验证**`、`**边界**`、`**需要谁动作**`（别名见脚本 `DELIVERY_FIELDS`）。缺项=拒收，`--force --reason` 可声明例外但留台账。
   - **E040 交付物入仓**：执行报告「交付物」节反引号路径必须已 git commit（未 commit=未发生）。跨仓交付物（KDO CLI 仓）写**含仓名的全路径**（`Knowledge Delivery OS 0.0.1/kdo/...`），否则被判 untracked（#639/#649 两次实证）。
5. **流转成功 ≠ 流转已发生**：`complete` 跑完必须回验（见下「调用后验证」）——E019 家族 6 次实证「状态停在 claimed，欧阳锋看不到待审项」。

## 调用后验证（30 秒，跳过=白干）

```bash
python 90_control/scripts/queue_transition.py status        # ① 队列行应显示目标状态
```
② 用 Read 回读任务单 frontmatter `status:` 字段确认（如 `pending_review`）。两处都对才算提审完成。

## 常见坑（症状 → 修复）

| 症状 | 根因 | 修复 |
|:--|:--|:--|
| `claim 645` 报「不在生产队列中」 | 传了 seq 号而任务单在 `60_feedback/tasks/`（#645 friction 实证；#647 已修 seq 解析，但队列行外仍查不到） | 传完整 task_id；或先 `myqueue <角色>` 查名下任务 |
| `--evidence` 传一段文字被拒「文件不可读」 | 该参数只收文件路径（#615/#624/#638/#640 四次实证） | `--evidence 60_feedback/tasks/<任务单>.md`；先把要附的说明写进任务单执行报告 |
| complete 报「执行报告缺 N 个字段」 | 五字段锚词没顶格写或漏写 | 按脚本报错里的样例补全（粗体锚词开头各起一行） |
| complete 报 E040 交付物未入仓 | 交付物改了没 commit，或跨仓路径没带仓名前缀 | `git add <具体路径> && git commit` 后重跑；KDO CLI 仓交付物写含仓名全路径 |
| complete 成功但看板没变 | 没回验，状态其实停在 claimed | 跑 `status` + 回读任务单（L9 牌） |
| `claim` 被队首 pending_review 拦 | 队列 FIFO 纪律 | 同执行者多单连发用 `--sequence`；跨执行者并行用 `--force --reason`（留台账） |

## 失败模式（本技能特有）

| 失败 | 可识别信号 | 今晚能做的修复 |
|:--|:--|:--|
| 凭直觉猜参数 | 想直接敲 `complete 658 --instance 我` | 先跑 `python 90_control/scripts/queue_transition.py`（无参数打印用法），再照抄 |
| 手改文件救火 | 门禁拦了想直接编辑队列 md | 停手。门禁提示什么就补什么（commit/五字段），补完重跑脚本 |
| 提审即宣告完成 | 脚本输出 ✅ 就去干别的 | 强制 30 秒回验（status + 回读 frontmatter） |

## 相关协议与卡

- 行为宪法：`90_control/agent-behavior-constitution.md`（断言三级标注/负向判词附锚点）
- 角色队列纪律：`.agent/<角色>-context.md`（各角色同款状态机表）
- 门禁锚点细节：`90_control/file-flow-protocol.md`（F-034 执行报告节例外条款）
- 姊妹 skill：`review-chain`（收尾复盘链 → complete --evidence 的证据从哪来）
