---
title: 残余文案规则门禁化盘点（#401）
type: diagnosis
author: huangyaoshi
created_at: 2026-08-21
source: design_20260821_lobster-employee-insights.md L1
status: draft
---

# 残余文案规则门禁化盘点（#401 · 黄药师建议书 L1）

> 问题：龙虾员工实证"每次靠提醒 = 规则没变成系统能力"。KDO 已门禁化一批（E018/#363/#375/#390），但全库没有"仍靠自觉"清单——本盘点补上这张清单。

## 方法（可复扫）

- **复扫脚本**：`90_control/scripts/rule-gate-inventory.py`（#401 交付物）
- **扫描范围**（26 文件）：PROTOCOL.md / AGENTS.md / rules-core.md / kdo-industrialization-manual.md / tool-card-excellence-standard.md / startup.md / 8 个 agent context / 3 个 SOUL.md / 9 个错误模式库
- **抽取规则**：祈使句/禁令关键词族（必须/禁止/不得/严禁/一律/务必/记得/一定要/不允许/切勿/铁律/红线…），跳过表格/代码块/引用行
- **摩擦计数**：规则文本 2-6 字中文词组与 friction-log 记录行弱匹配
- **结果**：182 条规则候选（`--json` 全量），81 条有 friction 命中
- **复扫保证**：同文件集+同关键词 → 输出一致（验收标准 1）

## 全量清单（182 条归并为 22 个主题簇）

> 数字口径（可复现）：**规则数** = 关键词命中条数（`--json` 全量 182 条中检索），**friction** = 簇内最高单条命中数（非合计）。完整标注在 `rule-gate-inventory.py --json`，本表是人工归并。

### A. 已门禁化（7 簇，20 条）——文案是冗余提醒，可留可精简

| 簇 | 规则数 | friction | 机制位置 |
|:--|--:|--:|:--|
| A1/A5 队列状态变更必须走 queue_transition，禁手工改状态列 | 7 | ×18 | queue_transition.py 硬状态机 + O-3 已修 |
| A2 提审必须附 pre-submit 输出 | 3 | ×15 | #363 提审 git 门禁 + pre-submit 脚本 |
| A3 处置类素材禁止删除（Never delete） | 2 | ×3 | #375 claim 处置门禁 + PROTOCOL §7 工具化 |
| A6 定位声明必填 | 1 | ×6 | #199 新卡 lint 已上线 |
| A7 提审即流转（状态+队列两步） | 4 | ×2 | queue_transition complete/review 自动流转 |
| A8 卡片 source_refs 必填 | 3 | ×7 | kdo_lint F1/R6 + pre-submit |
| A9 检索索引新鲜度（新卡入库必跑 kdo index） | 0 | — | L2 提审门禁 `_check_index_freshness` + L3 巡检（08-19 上线，文案未写成祈使句未抽取） |

### B. 部分门禁化（9 簇，18 条）——有机制但强度/覆盖不足

| 簇 | 规则数 | friction | 现状 | 缺口 |
|:--|--:|--:|:--|:--|
| B1 口述稿引用必须指向 source 文件（非 inbox 临时 MD） | 1 | ×16 | kdo_lint source_refs WARN（指向 00_inbox 仅 WARN） | **WARN 不拦**——口述稿从 inbox 挪 10_raw 后引用断裂无感知 |
| B2 写完卡必须桥接 Hermes 双轨 | 1 | ×2 | #267 bridge status 可查 | 无入库门禁，靠自觉跑 bridge |
| B3/B4 卡片长度与 token 上限（KF-024 ≤3500 / Hub <3000 字） | 3 | ×9 | estimated_tokens 计算器存在 | 未挂 lint 强制 |
| B5 批量操作三问（dry-run/范围声明/非空不覆盖） | 7 | ×2 | P-29/P-30 文案铁律 | 无工具强制（dry-run 靠脚本自身） |
| B6 frontmatter round-trip 校验 | 1 | ×3 | #168 裁定文案 | 脚本可判定（yaml 读回），未工具化 |
| B7 BOM/CRLF 编码处理 | 1 | ×6 | #323/#326 修复 | 无检查项，GBK/BOM 复发靠人 |
| B8 引用卡名必须检索实证（E020 虚假熟悉感） | 1 | ×6 | 检索铁律文案 | 无"引用存在性"检查（related 死链 lint 有但卡名引用无） |
| B9 D4 自我修改门禁 | 2 | ×9 | decisions.md 批准记录（事后） | **无事前/事中检测**——context/skill 被改无感知 |
| B10 新卡 tags 维度（audience/scene） | 0 | — | pre-submit R6 WARN | WARN 级（#393 判定 Warning→ERROR 待议） |

### C. 仍靠自觉（6 簇，19 条）——纯文案，无任何机制

| 簇 | 规则数 | friction | 成本分档 |
|:--|--:|--:|:--|
| C1 口述稿逐字读全文（含末尾 Q&A） | 6 | ×8 | 需语义判断（读没读全无法脚本判定） |
| C2 加载用户模型/先扫信号词再读内容（王语嫣 W2/W3 族） | 1 | ×7 | 需语义判断 |
| C3 严禁凭记忆/凭印象判断（检索铁律） | 8 | ×6 | 需语义判断（本质不可门禁化——回答前检索可部分检测：kdo query 调用痕迹） |
| C4 失败模式自带"症状+修复" | 1 | ×6 | 需语义判断 |
| C5 三方法前置（调研≥2 源/6 层交叉/9 层深挖） | 2 | ×4 | 需语义判断（执行轨迹可检测：报告含调研引用） |
| C6 每踩坑→入库模式→更新 Lint（闭环纪律） | 1 | ×5 | 需语义判断 |
| C8 输出路径纪律（wechat-collect 等） | 1 | ×2 | 脚本可判定（输出路径校验可写） |

> 归并说明：C7（内容价值判断）实为 A3 的文案残留——#375 已门禁化；A4（双仓提交纪律）并入 A2（#363/#390 同一机制族）；B10 与 A9 关键词未抽取到祈使句行，机制存在性从 #393/#399 上下文确认。

## 成本分档统计

- **已门禁化**：20 条 → 文案可精简为指针
- **脚本可判定**（可门禁化）：B1/B2/B3/B4/B6/B7/C8 ≈ 14 条 → 可升级为检查项
- **需语义判断**（门禁化伪命题，诚实标注）：C1-C6 ≈ 19 条 → 只能靠流程/习惯，不硬上

## Top 3 门禁化建议（按 friction 排序 · 改造立项由王语嫣另裁）

### Top 1：口述稿 source 引用断裂检测（B1，friction ×16）
- **现状**：kdo_lint 对"source_refs 指向 00_inbox"仅 WARN；口述稿从 inbox 移入 10_raw/sources 后旧引用全部断裂（#391 修的正是这类）
- **方案**：`full-library-rescan` 新增检查项 `source-refs-inbox`（口述稿类 source_refs 指向 00_inbox → 提示迁移）；配合 dead-source-refs 已是 ERROR 级
- **成本**：低（脚本可判定，规则与 #399 工具同构）

### Top 2：D4 自我修改事前检测（B9，friction ×9）
- **现状**：decisions.md 是事后记录；08-15 已实证 context 路径漂移无人感知
- **方案**：复用 #364 check-runtime-drift 的"进程/文件 vs 基线"模式——.agent/*-context.md 变更检测（git diff 可查，非黄药师本人 commit 的 context 修改即报警）
- **成本**：低（git 可判定提交者；check-derivatives 已有 hash 基线机制可直接扩展）

### Top 3：口述稿全文阅读的半门禁化（C1，friction ×8）
- **现状**：摩擦最高簇之一但**语义判断类**——"读没读全文"无法脚本判定，诚实标注门禁化伪命题
- **可行替代**（半门禁化）：任务单声明字段 `source_reading: full | partial` + 报告须附"已读行数区间"（如 #400 的"逐字读完 L1-L2416"模式）；门禁只校验声明存在性，不校验真实性（真实性靠欧阳锋抽查）
- **成本**：中（声明字段校验是脚本可判定的，但约束力弱于真门禁——如实告知）

## 附：脚本使用

```bash
python 90_control/scripts/rule-gate-inventory.py              # 人类可读
python 90_control/scripts/rule-gate-inventory.py --json       # 结构化（182 条全量）
python 90_control/scripts/rule-gate-inventory.py --list-sources
```

*黄药师 · 2026-08-21*
