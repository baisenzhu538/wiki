---
id: task_20260802_huangyaoshi-review-infra
task_id: 218
assignee: huangyaoshi
status: queued
created_at: 2026-08-02
domain: kdo
priority: P0
source: 欧阳锋 #213/#214 终审全程观察
updated_at: '2026-08-02T23:55:00+00:00'
---

# KDO 终审基础设施迭代：状态同步自动化 + 校验补强

> **来源**：2026-08-02 欧阳锋终审 #213（14 张）+ #214（5 张）全程观察——19 张卡、4 轮终审暴露的**终审侧**基础设施缺口
> **修复人**：黄药师
> **优先级**：P1

---

## 一、背景：终审是 KDO 最人工的环节

终审通过 = 手动同步 **4 处**：①任务单 frontmatter ②production-queue 状态列 ③dashboard ④**卡片自身 frontmatter**（status/reviewed_by/review_date）。今天 19 张卡 PASS 后，第 4 处漏同步——卡片仍 `status: draft` + `reviewed_by: 待审`，入库后检索/图谱都按 draft 处理。人工同步的固有风险，需要工具兜底。

---

## 二、需求

### R1（P0）：`kdo review-mark` —— 终审状态批量同步命令

```
kdo review-mark <task-id> --reviewer 欧阳锋 --grade A-
```

- 从任务单读取关联卡片清单（卡片 id 列表）
- 批量写卡片 frontmatter：`status: reviewed` / `reviewed_by: <reviewer>` / `review_date: <today>`（已存在则跳过）
- 输出变更清单（文件路径 + 改动字段），**dry-run 模式**默认开启，`--write` 才落盘
- 对接 queue_transition.py 的 review 流程：`review --verdict pass` 后可链式调用

> 若 R1 排期较晚，最低限度：`kdo lint` 增加"任务队列 reviewed 但关联卡片 frontmatter 仍 draft"的一致性 WARNING（数据源：production-queue.md + 任务单 frontmatter 的卡片清单——任务单可能不列卡片清单，则退化为扫描最近 N 天 created_at 的 draft 卡）

### R2（P0）：queue_transition.py 可靠性 + 提报一致性校验

- **task_id 匹配 bug（O-3）**：review 路径用纯数字匹配任务，队列 task 列是 `task_YYYYMMDD_...` 字符串 → 匹配失败。修复为同时支持两种格式
- **提报一致性校验**：`complete`/`claim` 时自动校验"队列状态 vs 任务单 frontmatter 状态"是否一致，不一致则报错并提示（今天老顽童提报时只改队列不改任务单 frontmatter，状态不一致反复出现）

### ✅ O-3 根因定位（2026-08-03 欧阳锋补充，供黄药师修复）

**复现步骤**：
1. 队列 #213 为 `pending_review`；任务单 `60_feedback/tasks/task_20260802_wangyuyan-innovators-dilemma-qinpeng.md` frontmatter：`id: task_20260802_wangyuyan-innovators-dilemma-qinpeng`、`task_id: 213`
2. 执行 `python 90_control/scripts/queue_transition.py review 213 --verdict pass --reviewer 欧阳锋`
3. 实际：`_find_task_file_dual("213")` → ①按文件名找 `213.md`（不存在）→ ②按 frontmatter `id` 匹配 `"213"`（frontmatter id 是 `task_20260802_...`，不匹配）→ 返回 None → 报错"任务未找到/不在队列"
4. 而传全名 `task_20260802_wangyuyan-innovators-dilemma-qinpeng` 时工作正常——**这就是"时好时坏"的根源：纯数字 task_id 时挂，全名时好**

**根因**：`find_task_file_by_frontmatter_id()`（queue_transition.py L120-134）只匹配 frontmatter 的 `id` 字段，**未匹配 `task_id` 字段**。task_id 有 3 种形态（纯数字 `213` / frontmatter `id` / 文件名），当前只支持后两种。

**修复方案**（一行）：
```python
# find_task_file_by_frontmatter_id 中：
if fm.get("id") == task_id or str(fm.get("task_id")) == task_id:
```

### R3（P0）：`kdo pre-submit --files <path...>` / `--task <task-id>`

- 现状：pre-submit 只能跑全库（333+ 文件），无法只验证新卡/修复卡——审查时无法快速确认"修复后通过"
- 建议：支持文件级/任务级参数，只对目标卡做全部校验

### R4（P1，2026-08-02 升级）：source_refs 存在性 + 路径规范校验

- **#214 观察**：source_refs 指向 `00_inbox/`（暂存区）——路径不规范但文件存在（溯源链通）
- **#215 观察（升级触发）**：9 张卡 source_refs 全部指向 `10_raw/sources/src_20260802_讲香基本功-李頔-口述.txt` 但**文件不存在**（搬运未完成）——路径规范但溯源链断。镜像问题说明"搬运"动作经常被跳过，且 lint 无存在性校验
- 建议：
  1. **存在性校验**（P1）：lint 检查 source_refs 指向的本地文件是否存在，不存在 → ERROR `"source_refs 指向的文件不存在：<path>"`（这是 #215 的直接教训——9 张卡全部断链靠人工终审才发现）
  2. **路径规范校验**（P2）：source_refs 不应指向 `00_inbox/`（暂存区不是长期溯源层），命中 → WARNING `"source_refs 指向 00_inbox，应搬运至 10_raw/sources/"`

### R5（P2，可选）：aliases 双向同步校验

- 现状：#214 K12 儿童名（换位读心/魔法沙盘…）标注"应加入对应成人卡 aliases"（见 tool-panproduct-kids-card-naming 操作步骤 6），但无校验/无自动同步 → 搜索断层风险
- 建议：对"命名翻译类"卡（related 指向成人卡且 body 有对照表），WARNING 提示"儿童名是否已同步到成人卡 aliases"（弱校验，人确认）

### R6（P1，2026-08-02 小昭诊断触发）：搜索可达性校验 + 索引刷新机制

> **触发**：小昭（外部 agent）用 kdo_search 搜"创新者的窘境"→ 0 条匹配，但卡片存在且已终审。诊断报告：`60_feedback/diagnosis/2026-08-02-search-reachability-diagnosis.md`。王语嫣独立验证后确认**直接根因是索引 7/27 后未刷新**（search_index.json 最后修改 07-27，卡 08-02 入库），**放大因素是 #213 全部 14 张卡 title 为空**（BM25 最高权重字段失分）+ "创新者的窘境"未进 aliases。

- **R6a（P0）索引刷新机制**：新卡入库后自动触发增量索引，或至少 production-queue 完成批次后统一 rebuild。当前索引 5 天未刷新 = 当天入库卡当天搜不到，外部 agent 协作通道断裂
  - **✅ 2026-08-03 状态（完成）**：手动 `kdo index` 已重建——`.kdo/search_index.json` Aug 3 01:52，doc_count 3755。**欧阳锋 O3 验证通过**：词表含"窘境"（24 文档）+ christensen 卡 id（5 张）+ dilemma。三层闭环合上（#219 卡片侧 → #218 R6 门禁 → R6a 索引）。
  - **遗留（O-9 停车场）**：索引刷新仍手动——建议 pre-submit hook / review-mark 后自动触发增量索引，否则下批入库又会过期
  - **O-10（2026-08-03 王语嫣核查#221发现，黄药师修复中）**：`kdo-tools/mcp-reachability-check.py` L23-24 `from mcp.tools import search` 被 site-packages 官方 MCP SDK 劫持（`import mcp` 解析到 `C:\...\site-packages\mcp\`，而非 `kdo-tools/mcp/`）→ ImportError → 自查脚本无法运行。**修复建议**：①脚本内绝对路径 import `kdo-tools/mcp/tools.py`；②或 `kdo-tools/mcp/` 包改名 `kdo_mcp/`（涉及所有引用方，需评估）。影响：#221 自查工具=老顽童新卡提交前可发现性自检，工具坏=防增量闭环缺一环
- **R6b（P1）搜索可达性 lint**：title 非空校验（缺失 → ERROR）+ aliases 应包含中文搜索词（书名/概念名）校验（缺失 → WARNING）。全库已有 97/2632 张卡 title 缺失，第一版只拦新提交不追溯存量
- **R6c（P2）中英文同义词映射**：card id 英文 ↔ 中文标题/别名映射表，搜索时自动扩展（"innovator's dilemma" ↔ "创新者的窘境"）

---

## 三、验收标准

1. `kdo review-mark --dry-run` 输出预期变更；`--write` 后卡片 frontmatter 三字段落盘正确
2. `queue_transition.py review <task-id字符串>` 不再报"任务不在队列中"；提报时状态不一致 → 报错提示
3. `kdo pre-submit --files <卡路径>` 只校验目标卡，输出通过/失败
4. `kdo lint` 对 `00_inbox/` source_refs 报 WARNING
5. R6a：新卡入库后索引自动刷新或批次完成后统一 rebuild（当天入库当天可搜到）
6. R6b：title 缺失卡 pre-submit 报 ERROR；aliases 缺中文搜索词报 WARNING
7. 全部 pytest 通过；用 #213/#214 的 19 张卡回归验证

---

## 四、边界

- 只做校验和状态写入，**不改卡片正文内容**
- R1 的批量写 frontmatter 只动 `status`/`reviewed_by`/`review_date` 三字段，不动其他（避免 C-10 批量破坏教训）
- 存量 draft 卡不追溯（仅新终审流程生效）

---

## 五、参考

- 停车场 O-3：queue_transition.py task_id 匹配 bug（2026-07-21 记录，持续复现）
- 2026-07-21 复盘：pre-submit 无文件级参数（已记录）
- #213/#214 终审记录：`60_feedback/tasks/task_20260802_wangyuyan-innovators-dilemma-qinpeng.md` / `task_20260802_wangyuyan-live84-kids-panproduct.md`

*欧阳锋 · 2026-08-02*
