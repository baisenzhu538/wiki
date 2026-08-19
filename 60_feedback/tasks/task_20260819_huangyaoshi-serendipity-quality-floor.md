---
id: 380
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-19T18:58:27.246805+00:00'
title: 偶遇管线收口质量门（P1，A 方案）——自动转正只到素材层，卡片一律过王语嫣编排门禁
priority: P1
dependency: []
code_files:
- kdo-tools/wechat_promote.py
- 90_control/scripts/health-check.py
- 90_control/scripts/check-draft-aging.py
- kdo-tools/mcp/tools.py
- C:/Users/Administrator/Knowledge Delivery OS 0.0.1/kdo/commands/delivery.py
- C:/Users/Administrator/Knowledge Delivery OS 0.0.1/tests/test_query_label.py
---

# #380 偶遇管线收口质量门（P1，A 方案）

## 任务背景与裁定记录

wechat_promote.py 自动转正直写 `30_wiki/cases/`（知识库正式层），绕过质量门——王语嫣 2026-08-19 核实实锤。

**裁定变更记录**：
- 08-19 王语嫣初裁 B 强化版（自动转正保留+三配套）——**已撤销**
- 08-20 老朱纠正："任务编排门禁是王语嫣，欧阳锋只做终审"→ 王语嫣改判 **A 方案**
- 改判依据：①门禁判定是编排者日常低成本动作（4 张卡几分钟判完），不等同于终审重活，B 的"人工确认会退化"担忧不成立；②实证污染率 75%（4 张入仓 3 张不合格），不是低污染流，不能直通；③与 watch_inbox 新规则"任何素材不得绕过质量门"一致性要求——B 是规则自开的例外口子

## A 方案行为定义

**素材段零摩擦保留，知识段一律过门**：
- 逐字稿/研究文档 → 自动入 `10_raw/sources/`（零摩擦不变）
- case 卡 → **不进 30_wiki**，落在待编排区，经王语嫣编排门禁判定（退回/留存）后才可能入正式库，正式入库走既有生产流（任务单→生产→欧阳锋终审）

## 执行范围

1. **wechat_promote.py 改版**：case 卡输出目的地从 `30_wiki/cases/` 改为待编排区（建议 `60_feedback/inbox-queue/` 或 `00_inbox/wechat-collect/` 下专用子目录，实现者选定并在执行报告说明）；同步把新卡登记进 production-queue.md 的 INBOX-PENDING 看板段（复用 watch_inbox 既有机制，保证王语嫣能看到）
2. **最小内容校验前置**：生成时检测标题乱码/LLM 总结失败占位/正文下限——不合格的卡直接落 `_needs_rerun/` 并输出原因，不占待编排区
3. **存量 draft 超龄巡检**（挂 `kdo-tools/health-check.py`）：30_wiki 内 status=draft 超 24h 未审出清单，**接收方=王语嫣**（我分流判定去留，值得留的才送欧阳锋终审）；定位=存量 646 张+例外监控，只报警不自动改
4. **检索层 draft 标注**：kdo search/MCP 结果中 status=draft 卡带"未审"标记（只标注不降权，护存量 646 张可用性；search_index.py 现无 status 过滤，draft 与 reviewed 同权可见——标注是底线）

## 顺手收口（小，一并做）

- `watch_inbox.py` 双拷贝（kdo-tools/ + 40_outputs/code/scripts/）违反 #359"副本禁放+指针引用"：删 40_outputs 副本，README 登记指针

## 已完成的前置处置（王语嫣门禁，2026-08-19，不需重做）

- 3 张问题卡已退回 `00_inbox/wechat-collect/_needs_rerun/`：Top10（LLM 总结失败空壳）、e7536（标题乱码）、费曼4（ASR 噪音含"2015年中循"事实污染）
- 1 张留存：dy_766683 Skill 卡（内容合格，走巡检→终审正常流）

## 边界

- 不动存量 646 张 draft 卡（#373 Wave 系列的活）
- 不改检索排序算法；A 方案落地后新 draft 不进 30_wiki，检索标注只为存量兜底
- 素材段（10_raw）保持零摩擦，不加任何门禁

## 内容价值判断（PROTOCOL §7 合规声明）

- 本任务只改脚本+删一个已裁定违规的副本文件（watch_inbox.py 40_outputs 副本，双内容已 diff 验证一致），不动任何卡片与素材

## 验收标准

1. 正向实测：新偶遇素材跑 promote → 逐字稿入 10_raw，case 卡落在待编排区且 INBOX-PENDING 有登记；30_wiki 零新增
2. 反向实测：构造标题乱码/空壳卡 → 落 _needs_rerun 且原因可见
3. health-check 输出存量 draft>24h 清单（Skill 卡 dy_766683 超龄后应在列）
4. kdo search 检索到存量 draft 卡带"未审"标注
5. 40_outputs 副本删除 + README 指针登记；全量 lint 无新增 ERROR

## 交付

1. 改版脚本 + 正反向实测记录
2. 送欧阳锋终审

---

# 执行报告（黄药师 2026-08-20 02:26，待欧阳锋终审）

## 一、落地清单

| 件 | 文件 | 实现 |
|:--|:--|:--|
| ① promote 改版 | `kdo-tools/wechat_promote.py` | case 卡目的地 `30_wiki/cases/` → `00_inbox/pending-cards/`（待编排区）；逐字稿 → `10_raw/sources/` 不变。选 pending-cards 的理由：在 watch_inbox 扫描范围内（wechat-collect 是排除目录），新卡 10 分钟内自动登记 production-queue.md 的 INBOX-PENDING 看板段——零新通知代码，复用既有机制。幂等去重：pending-cards/30_wiki/_needs_rerun 三处同名即跳过 |
| ② 内容校验前置 | 同上 `_content_issues()` | 三类拦截：标题乱码（U+FFFD 替换符 / Latin-1 补充区 U+0080–U+00FF 连续≥2——对准 UTF-8→latin-1 误读形态）、正文 <200 字（空壳）、LLM 失败占位（"LLM 总结失败，请重试"等 4 个 marker，对准 wechat_knowledge.py 真实失败形态）。不合格 → `_needs_rerun/` + `.reason.txt` 原因文件 |
| ③ draft 超龄巡检 | `90_control/scripts/check-draft-aging.py`（新）+ 挂入 `health-check.py` | 扫 30_wiki 内 status=draft 且创建超 24h 的卡，输出清单（默认前 20 条防刷屏，--all/--json 全量）。advisory 恒 exit 0——存量 744 张是常态，不该让 health 整体 FAIL；接收方=王语嫣 |
| ④ 检索未审标注 | CLI `kdo/commands/delivery.py::_label_unreviewed`（cmd_query 输出前统一标注）+ MCP `kdo-tools/mcp/tools.py::search`（结果加 status 字段，draft 卡标题前缀【未审】） | 只标注不降权不排除，存量 draft 可用性不受影响 |
| ⑤ 顺手收口 | 删 `40_outputs/code/scripts/watch_inbox.py`（删前 diff 验证与活代码一致）+ `40_outputs/code/scripts/README.md` 登记指针，并补登 wechat_promote/check-draft-aging 两条 | #359 副本禁放裁定落实 |

## 二、正反向实测记录（2026-08-20 02:1x–02:2x）

**反向（验收②）**：构造两张假卡跑 promote（真实行非 dry-run）——
- 乱码卡（标题 `æµ‹è¯•æ ‡é¢˜…`）→ 🚫 落 `_needs_rerun/`，原因"标题疑似乱码+正文过短"双命中
- 空壳卡（LLM 占位+21 字正文）→ 🚫 落 `_needs_rerun/`，原因"正文过短+LLM 总结失败占位"双命中

**正向（验收①）**：构造合规卡 `case-wechat-test380good.md` → 📥 落 `00_inbox/pending-cards/`，`30_wiki/` 零新增；手动跑一次 watch_inbox → INBOX-PENDING 看板段出现该卡登记行 ✅。测试夹具（3 卡+reason 文件+看板行+dispatch 文件+inbox_state 键）已全部清理。

**验收③**：`check-draft-aging.py` 实跑输出"扫描 30_wiki: 744 张 draft 超 24h 未审"；已挂入 health-check（报告内 `[PASS] 存量 draft 超龄巡检（#380）` 在列）。

**验收④**：CLI `kdo query "蒸馏 书单"` → draft 卡 tool-yizhan-shendeng 结果带`【未审 draft】`前缀，reviewed 卡无标记；MCP `kdo_search` 同查询 → 该卡 `status: "draft"` 字段外露 + 标题前缀`【未审】`。

**验收⑤**：40_outputs 副本已删 + README 指针登记 ✅。

## 三、测试中抓到并修掉的实现缺陷

1. **乱码正则初版 `[À-ÿ]{2,}` 不命中真实 mojibake**：µ(U+00B5)‹(U+2039) 等 continuation-byte 字符在 À(U+00C0) 之下/之外——放宽为 `[U+0080–U+00FF]{2,}` 后命中（反向实测逼出来的）
2. **`_needs_rerun` 未纳入幂等去重**：已退回卡每次 promote 都会重复处理——已修（三处同名即跳过）

## 四、顺手发现的预存在 bug（未改，报裁决/立项）

1. **`delivery.py` 全模块无 `import os`，`_filter_by_trust` 的 posix 分支 NameError 被 except 吞掉** → 绝对路径结果（BM25 全部结果都是绝对路径）**静默绕过 trust≥medium 过滤**——trust 过滤对 BM25 从未生效。我的 `_label_unreviewed` 用函数内局部 `import os` 规避，**刻意不改 _filter_by_trust 现状**（修复会让存量 trust_level=low 的卡突然被过滤，改变检索结果集，超出本任务"不改排序/过滤"边界）。建议单独立项。
2. **3 张退回卡（dy_7654/dy_7671/e7536）在 `30_wiki/cases/` 仍有同名文件**——王语嫣 08-19 的"退回 _needs_rerun"是复制未移除，正式层残留与任务单 §已完成前置处置 的描述不一致。按"不动卡片"边界未处理，请编排门禁补一刀。
3. 运行时漂移巡检报 PID 7752（kdo MCP server）比源码旧 0.4h——正是本次 delivery.py 改动所致，**重启 MCP server 进程即消**（未擅自杀进程）。

## 五、验证

- CLI 仓 `tests/test_query_label.py` 新增 3 个 `_label_unreviewed` 单测（draft 打标/reviewed 不动/文件缺失不炸），10 passed
- health-check 全量：新检查在列 PASS；其余 FAIL 项（lint 存量 domain 格式、VLM、MCP 挂载抽查）与 08-19 基线报告一致，非本次引入；运行时漂移 FAIL 见 §四.3
- 改动未触碰任何卡片与素材（git diff 可证）

## 六、留裁决事项

1. `_filter_by_trust` 静默失效的修复时机（§四.1）
2. 30_wiki 残留 3 张退回卡的移除（§四.2）

---

## 退回意见（2026-08-20 欧阳锋 · FAIL 结构化协议 · #362 三问①）

**P0/P1/P2 清单**：
- 🔴 **P0：KDO 仓改动未提交**——`kdo/commands/delivery.py`（+34，_label_unreviewed）+ `tests/test_query_label.py`（+30）工作区脏（git status M），无 commit。#362 三问①"入仓了吗"答否——**修复未提交=不存在，不予终审**。

**字段级定位**：KDO 仓 `git status --porcelain` → ` M kdo/commands/delivery.py` / ` M tests/test_query_label.py`；`git diff` 内容为 `_label_unreviewed` 函数体（#380 核心逻辑）。

**证据**：KDO 仓 git log 最新 1f165bb（L1 增量索引）不含 #380 改动；wiki 侧 tools.py/check-draft-aging/wechat_promote 已被 backup/commit 收净（9e8acbff8 等）。

**附带发现**：任务单 frontmatter `code_files` 仅声明 `kdo-tools/health-check.py`——**未声明 KDO 仓路径**（delivery.py 属"Knowledge Delivery OS"仓），#363 提审门禁因此漏检。门禁盲区：code_files 声明不完整时无法兜底。

**期望形态**：① `git add` + commit KDO 仓（delivery.py + tests，message 引 #380）② 任务单 code_files 补 KDO 仓路径（跨仓声明全量）③ 重新提审。wiki 侧已入仓无需重提。

**留裁决（修复复审时一并定）**：§四.1 `_filter_by_trust` 静默失效（BM25 未过滤 trust）修复时机；§四.2 30_wiki 残留 3 张退回卡移除。

---

## 退回意见补充（2026-08-20 欧阳锋 · 双仓未提交实锤）

**补充 P0 证据**：#363 提审门禁在 complete 时拦截——`kdo-tools/wechat_promote.py`（wiki 仓）也存在未提交改动（git status M）。**FAIL 清单最终为双仓**：
- KDO 仓：`kdo/commands/delivery.py`（+34）+ `tests/test_query_label.py`（+30）
- wiki 仓：`kdo-tools/wechat_promote.py`

**门禁行为记录**：#363 门禁正常工作（code_files 声明范围内逮住 wechat_promote 脏）；KDO 仓 delivery.py 因 code_files 未声明 KDO 路径而漏检（前文已述）。

**状态**：任务已 release 回 queued（队列与任务单状态对齐）。黄药师补齐两个仓的 commit + code_files 补全 KDO 路径后，重新 claim → complete（门禁验证）→ 提审。
