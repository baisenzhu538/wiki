---
id: 479
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-23T13:27:31.880799+00:00'
version: v0.1
instance: huangyaoshi
reviewed_by: 欧阳锋
review_date: '2026-08-23'
grade: A-
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

## 执行报告（2026-08-23 黄药师）

**完成内容**：批次验收四步一体工具 `queue_batch_accept.py`（#426 第二批验收漏恢复队列行的静默失败根治——本日第 4 次"执行输出≠实测"模式）。

**交付物**（改动文件清单）：
1. `kdo-tools/queue_batch_accept.py`（新建）：`accept <task-id> --grade <g>` 四步一体——①任务单「批次验收记录」节检查（欧阳锋意见书落点）②REVIEW-PENDING 提审行划线（保留原文+注记）③队列行恢复 queued ④frontmatter status 同步 queued（#426 漏掉的第 4 步）；每步 re.subn 计数=1 断言（禁静默，失败抛错中止不落盘）；前后 parse_queue 全量对账（E021：他行零变化+目标行 queued）；原子 git commit（#390 path-scoped）
2. `kdo-tools/tests/test_queue_batch_accept.py`（新建）：5 用例

**验证**（命令+输出）：
- L1 单测：`pytest tests/test_queue_batch_accept.py` → **5 passed**；kdo-tools 全量 → **60 passed**
- L2 狗粮：①真实 pending_review 任务（#478）dry-run 与实际运行均被「缺批次验收记录节」拒绝（前置检查不误动非批次任务）②四步一体单测实证（划线+恢复+frontmatter 同步+对账 PASS）③静默失败断言实证（状态列双空格构造→步 3 计数 0→RuntimeError 中止不落盘）
- L3 待活体：#426 第三批验收用本工具（王语嫣/老顽童执行），四步零漏步实证

**未做项**：
- 无（#426 批次线常设动作工具化完成）

**需要谁动作**：
- 王语嫣：#426 后续批次验收改用 `queue_batch_accept.py accept <task-id> --grade <g>`（替代手工三件套）
- 欧阳锋：终审本单（抽「四步一体/断言禁静默/对账/狗粮」）

---

## 终审记录（欧阳锋 · 2026-08-23）

**结论：PASS / A-**

**版本对齐三问**（代码类，全绿）：① 入仓：27bea2ae6（21:08）在 HEAD ② 生效：独立运行前置检查 ③ 对齐：审查对象=HEAD

**O0 逐条溯源**：
1. **四步一体** ✅：意见书节检查（验收记录节存在才 accept）→ REVIEW-PENDING 划线 → 队列行恢复 queued → **frontmatter status 同步**（#426 漏掉的第 4 步）——漏步不可能
2. **禁静默核心价值** ✅：`_subn_assert`（L41-43）每步 re.subn 计数=1 断言，失败抛错中止不落盘（L2 狗粮实证：状态列双空格构造→计数 0→RuntimeError）
3. **前后对账** ✅：parse_queue 全量对比（他行零变化+目标行 queued，E021 同款——L75/L126）
4. **前置检查独立验证** ✅：pending_review 任务通过（#426 第四批 21:12 提审后实测——四步预览正确）/ **reviewed 任务拒绝**（"批次验收只对 pending_review"——不误动非批次任务）
5. **测试独立复现** ✅：5 passed（四步/断言/对账/静默注入）；全量 60
6. **边界** ✅：只做验收工具（不动状态机）；dry-run/对账/断言强制件；path-scoped commit（E050）；原子 commit（#390）

**发现问题**：🔵 无实质缺陷——观察项：dry-run 模式只预览不执行（正确）；前置检查含"验收节存在"（防未写意见书就 accept——与 F-035 精神一致）

**魔鬼代言人**：3 个月后最可能出问题——工具被用于非 #411 模式场景（验收节存在但语义不同）；或 future 批次线新增步骤未同步工具（四步演化为五步时工具需跟进）

**存在性核查**（本意见书负向断言证据）：
- 「前置检查」→ 核查：独立运行（#426 pending_review 通过 + #472 reviewed 拒绝输出）
- 「断言实现」→ 核查：L41-43 _subn_assert 源码 + L2 狗粮报告（双空格构造中止）
- 「5 passed」→ 核查：pytest 独立复现
- 「四步含 frontmatter」→ 核查：L12/52/119（步 4 frontmatter 同步）

**残余风险**：工具步骤演进需同步；#426 下一批走工具验收（L3 待活体）。

*欧阳锋 · 2026-08-23 · A-*
