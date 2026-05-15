---
id: sprint-13-kdo-mechanism-iterations
title: "Sprint 13：KDO 机制迭代——lint 基线、卡片清册、变更 diff、理解门禁辅助"
status: pending
priority: P1
assigned_to: 黄药师
reviewer: 欧阳锋
domain: master
created: 2026-05-16
target: 2026-05-25
---

## 背景

Sprint 12 Batch A 执行过程暴露了四个 KDO 工具链的改进点，全部来自真实摩擦：

1. **lint 噪音**：591 条预存 warning，每次跑 `kdo lint` 都要人工判读"有没有新增"
2. **卡片清册手工维护**：Batch B 的 85 张 tool 卡列表是手工写的，无法按 type/domain/缺失节 查询
3. **审查时看不到变更**：Architect 只能看最终状态，无法快速定位 Builder 追加了什么
4. **理解门禁抽检靠手工**：C-8 防御靠人工翻卡，没有工具辅助

## 任务列表

### 1. `kdo lint --baseline` / `--diff` 模式（P0）

**问题**：当前 `kdo lint` 输出全量结果。预存 warning 多时，Builder 无法判断是否有新增问题。

**需求**：
- `kdo lint --baseline <git-ref>`：以指定 git 引用为基线，只报告该引用之后引入的新 lint 问题
- `kdo lint --diff`：等价于 `--baseline HEAD~1`（与上一次 commit 比较）
- 输出格式与 `kdo lint` 一致，但在末尾追加一行 `N new issues (M pre-existing suppressed)`

**验收标准**：
- [ ] `kdo lint --baseline HEAD~5` 只显示最近 5 次 commit 引入的新问题
- [ ] 不改变 `kdo lint`（无参数）的现有行为
- [ ] 不影响 KDO 源码中已有的 lint 规则

**实现提示**：
- 核心逻辑：跑两遍 lint（baseline ref 的 checkout + 当前 working tree），diff 结果
- 建议用 `git stash` + `git checkout <ref>` + lint + `git checkout -` + lint 的方式，避免真正切换工作树
- 或者用 git worktree 做隔离

### 2. 卡片清册查询（P1）

**问题**：批量升级时需要知道"还有多少张 tool 卡没加 Action Triggers"，目前要手工维护列表。

**需求**：
- `kdo cards list --type tool --domain yitang`：列出符合条件的卡片
- `kdo cards list --type tool --missing "Action Triggers"`：列出缺少指定节的卡片
- `kdo cards list --type framework --has "外部攻击"`：列出包含指定节的卡片
- 输出为卡片 ID 列表，可选 `--count` 只出数量

**验收标准**：
- [ ] `kdo cards list --type tool --domain yitang` 正确返回 85 张卡（与 Batch B 手工列表一致）
- [ ] `kdo cards list --type framework --missing "Action Triggers"` 当前返回 0 张（Batch A 已完成）
- [ ] `--has` / `--missing` 的匹配逻辑是基于 Markdown heading 的字符串匹配（`## Action Triggers`），不需要完整解析

**实现提示**：
- 扫描 `30_wiki/concepts/` 下所有 .md 文件
- 解析 frontmatter 的 `type` 和 `domain` 字段
- `--has` / `--missing` 用 Grep 检查 body 中是否存在指定 heading

### 3. `kdo card diff`（P2）

**问题**：Architect 审查时需要知道 Builder 具体追加了哪些节。当前靠 git diff + 人眼过滤。

**需求**：
- `kdo card diff <card_id> --since <git-ref>`：显示指定卡在两个版本间的**节级别**变更摘要
- 输出为三列：`| 节名称 | 变更类型 | 说明 |`
  - 变更类型：`新增` / `删除` / `修改`
  - 对新增/删除节：说明为该节的 heading
  - 对修改节：说明修改的行数范围（如 "+12/-3 行"）

**验收标准**：
- [ ] `kdo card diff yt-model-deep-review-iceberg --since <Batch-A之前的ref>` 显示三个新增节（外部攻击、不要用的场景、Action Triggers）
- [ ] 不新增 KDO 依赖（纯 Python 标准库 + git 命令）
- [ ] 不输出完整 diff（那不是本节的目标——审查者看表就够了）

**实现提示**：
- 核心逻辑：`git show <ref>:<path>` 取旧版本 → 解析 heading 结构 → 与当前版本对比
- Heading 解析：匹配 `## ` / `### ` / `#### ` 级别，提取节名称
- 不需要行级别 diff——节级别变更摘要即可

### 4. 理解门禁抽检辅助（P2）

**问题**：C-8 防御（批处理产生空洞卡片）靠人工抽检。但抽检哪几张、看什么，没有工具辅助。

**需求**：
- `kdo review --sample 5 --domain entrepreneur`：从指定域随机抽 N 张卡
- 对每张抽检卡，输出简化摘要：
  ```
  ## yt-entrepreneur-xxx
  Constraints: 2 条 boundary claims
  外部攻击: Freire (被压迫者教育学) + Papert (建构主义)
  不要用的场景: 3 行
  Action Triggers: 4 个触发项
  ```
- 审查者看摘要即可判断三信号（反例具体性、案例筛选、跨域连接），不用逐张翻卡

**验收标准**：
- [ ] 抽检结果包含卡片 ID + Constraints 条数 + 外部攻击来源 + 不要用场景行数 + Action Triggers 条数
- [ ] `--sample N` 的随机抽样可复现（用固定 seed，如卡片 ID 的 hash）
- [ ] 不替代人工审查——只做信息提取和格式化

**实现提示**：
- 解析 body section 结构，提取各节关键信息
- 外部攻击来源：从"外部攻击"子节中提取 `**Name**` 模式（粗体人名）
- Constraints 条数：计数 `claim:boundary-` 前缀行
- 不要用场景行数：计数 markdown table 中的非表头行

## 执行约束

- **顺序**：P0 → P1 → P2（优先级顺序，非强制依赖）
- **单次实现**：一次只做一个功能，测试通过后再做下一个
- **不碰已有 lint 规则**：所有改动只新增命令/flag，不修改已有逻辑
- **KDO 源码路径**：`C:\Users\Administrator\Knowledge Delivery OS 0.0.1\kdo\`

## 不做

- ❌ 不重构 KDO 源码架构——只追加增量功能
- ❌ 不新增 Python 依赖（纯标准库）
- ❌ 不改 KDO 的数据模型（state.json schema 等）

## 相关

- 工业化手册 v1.6 §1.9（本 Sprint 的触发来源）
- C-8 / C-9（批处理空洞卡片——理解门禁的防御对象）
- KF-022（单次会话上限——`kdo cards list` 帮助 Builder 在 ≤5 张约束下选卡）
