---
id: 479
assignee: huangyaoshi
status: queued
updated_at: '2026-08-23T23:30:00+08:00'
version: v0.1
---
# #479 批次验收工具化 queue_batch_accept.py（#426 批次线，静默失败根治）

- **任务号**：#479
- **状态**：queued
- **assignee**：huangyaoshi（基建单一实例；终审=欧阳锋；编排=王语嫣）
- **优先级**：P1（#426 剩余 100+ 张 tags 批次，批次验收是常设动作，静默失败已实证）
- **立项**：2026-08-23 王语嫣（欧阳锋建议书 `diag_20260823_ouyangfeng-batch-accept-tool` 裁定采纳立项）

## 背景（#426 第二批验收静默失败实证）

#426 长程分批（#411 模式）第二批验收时：批次验收动作三件套（终审记录+划段行+恢复 queued）**漏恢复队列行**——脚本 `text.replace(row_old, row_new)` 静默失败（row_old/row_new 同值且未 assert），打印"✅ 已 queued"实际未改；frontmatter 也未同步。直至第三批提审痕迹异常才被追出。

**这是本日第 4 次"执行输出与实测不符"**（#444 测试数/#460 插桩数/#463 registry/#426 批次）——静默失败模式（打印成功 ≠ 动作完成）在手工脚本中系统性存在。

## 任务

### queue_batch_accept.py（复用 queue-archive #453 成熟模式）

实现 `kdo-tools/queue_batch_accept.py`，~100 行，复用 #453 queue-archive.py 的成熟模式（parse_queue 对账 E021 + 原子 commit + dry-run）：

**四步一体**（`queue_batch_accept.py accept <task-id> --grade <等级>`）：
1. 任务单批次验收记录节检查（意见书已写）
2. REVIEW-PENDING 提审行划线
3. 队列行恢复 queued
4. **任务单 frontmatter status 同步 queued**（#426 漏掉的第 4 步）

漏步不可能——四步一体。

**每步断言**：划线/恢复均 `re.subn` 计数=1 assert，失败即报错退出（**禁静默**——本工具核心价值）。

**前后对账**：accept 前/后 `parse_queue` 对比——活跃数一致 + 目标行状态 queued 才输出 PASS（E021 同款全量对账）。

**dry-run**：演练模式（同 queue-archive）。

**原子 commit**：队列+任务单一次 commit（#390，path-scoped 禁 add -A，E050）。

## 受益面

- #426 剩余 100+ 张 tags 批 + 未来所有长程分批任务（批次验收是常设动作）
- 审查者/生产者共用一个工具（验收动作无歧义）
- 静默失败在工具层被断言+对账双保险拦住（行为层纪律为辅，工具层为主——B2-4 想犯错也犯不了）

## 验证（验证分层）

- L1：单测——构造批次验收场景，四步全 assert + 静默失败注入测试（text.replace 同值场景）应报错退出
- L2 狾粮：副本演练——#426 历史批次数据 dry-run，diff 验证四步全动
- L3 待活体：#426 下一批真实验收走工具，前后对账 + frontmatter 同步验证

## 边界

- 只做批次验收工具；不动 queue_transition 状态机（accept 是队列文件直改，同 #411 现行模式工具化）
- dry-run/对账/断言为强制件（非可选）
- 不改 #426 任务单本体（上板冻结 E047，验收标准升级走 #480 口径单）

## 关联

- 欧阳锋建议书 `diag_20260823_ouyangfeng-batch-accept-tool`（裁定采纳立项）
- #426（tags 判断类分批治理，pending_review 分批验收中）；#411（分批模式先例）；#453（queue-archive 复用模式）；#480（#426 验收标准升级口径单）
- #390（原子 commit）；E021（全量对账）；E040（编排产物即写即 commit）；E050（commit path-scoped）；B2-4（想犯错也犯不了）
- 顺序：黄药师单 **#479(P1)→#477(P2)→#478(P2)**，禁同轮 ≥3 独立单并发领取（禁止清单第 7 条）

## 内容价值判断（#375 处置门禁补充节）

- 本任务为新建工具脚本：queue_batch_accept.py + 单测，不删内容/不动队列状态机
- 无内容删除；PROTOCOL §7 不触发（工具新建非内容处置）

## 需要谁动作

- **黄药师**：实现 queue_batch_accept.py（~100 行，复用 #453 模式）+ 单测 + dry-run 演练
- **王语嫣**：编排核验（#426 下一批走工具验收 + 对账）
- **欧阳锋**：工具上线后批次验收全走工具（行为层断言纪律已入 context 兜底过渡期）+ 终审本单
