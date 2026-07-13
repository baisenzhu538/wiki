---
id: task_20260712_wangyuyan-c-domain-scan-fix-structure
assignee: huangyaoshi
status: reviewed
updated_at: '2026-07-13T10:40:07.269458+00:00'
reviewed_by: 欧阳锋
review_date: '2026-07-13'
grade: A-
---
# Task #175 · C 域查漏修复第一批（结构层：索引/裁定/勘误）

- **状态**：pending_review
- **负责人**：黄药师
- **优先级**：HIGH
- **依赖**：#168A 完成后顺领（避免同库并发）；可与 #167 并行（不同文件面）
- **依据**：`60_feedback/diagnosis/c-domain-scan-supplement-2026-07-12.md`（王语嫣查漏汇总，裁定 1-5 已落）

## 目标
修复 C 域结构层遗漏：6 张孤儿卡回链、digest 归属修正、5 项裁定落地、素材勘误补录、3 项原图复核。

## 工作清单
1. **6 孤儿卡接入**（汇总 §一）：`case-toc-ecommerce-formula-misjudgment`/`case-private-domain-ecommerce-formula`/`case-saas-renewal-formula`/`case-dental-clinic-formula`/`case-gym-membership-formula`/`case-offline-catering-formula` → 接入 `30_wiki/domains/business-formula-domain-digest.md` related + 补 `/index.md`
2. **digest 归属修正**（裁定 #2）：双目标法/三类目标从进阶篇行移到管理篇行
3. **裁定落地**：
   - 马拉松卡补双口径注（核心 6-7 维/扩展 10 维，裁定 #1）
   - dk 伪因果卡补术语映射注（因果倒置/共同因/筛选效应≈自我选择偏差/中间变量，裁定 #3）
   - `concept-一堂-相关不等于因果` 卡内补口径声明（因果=更强的单向相关，课程口径，裁定 #4）
4. **原图复核 3 项**（调 `_vlm_output` 对应图）：①30 天 2 学分 vs 20 学分（参数篇 L2818 vs 武器库图）②FB 七天十好友 vs 十天（参数篇 L1330 vs L2950）③参数冰山九层 vs 十层（L1228 vs L1376）——按图片原字裁定，结果补入诊断书
5. **6 老卡数字复核**（汇总 §一附带）：卡 3/5/6 数字与孔源口述不一致处按「一等压二等」复核修正；卡 1 空 source_refs 补齐（孔源篇 B 版 L502+ 行号）
6. **勘误表补录**（汇总 §五）：C 域系统性误识清单写入 C 域诊断书勘误节（银行=一堂/五十税费率=50 学分率/NTS=NPS/Leo 双义等）；双版本行号约定写入诊断书（实操 L1-3346/参数 L1-3553/孔源 B 版 L502+）
7. **Y 模型表述修正（老朱裁定 #6，汇总 §八）**：Y 模型=一堂全部课程的母模型，B 域 ROI 模型是其推导产物之一，母子关系非等价。修正全库「ROI/Y 模型」斜杠错误写法：①`business-formula-domain-digest.md` L109「B ROI/Y 模型」→「B ROI 模型（Y 模型推导产物之一，母模型见 [[yt-decision-y-model]]）」②`case-yitang-coke-spill-compensation` 标题与正文同改 ③全库再 grep 一遍「ROI/Y」「Y/ROI」确认无漏网。基准表述参照 `yt-decision-y-model` 与 `case-yihang-dual-triangle` L226（Y 模型循环：目标→朴素框架认知→实事求是/解放思想→更新认知→知行合一→下一轮）

## 执行要求
- 协议 4：只动本任务清单内文件，不顺手改其他
- 修改 frontmatter/related 后跑 yaml.safe_load 自检（E004 教训）
- source_refs 格式：路径+可选 L行号，括号备注挪出引用条目
- 原图复核结论逐条给「图原字 vs 口述 vs 笔记」三栏证据

## 验收口径
- 6 孤儿卡在 digest 与 index 均可达；裁定 5 项落地可查；3 项复核有结论；预检 PASS
- 扫窗申报=实动集；待王语嫣审查

## 扫窗申报
改动文件清单+原图复核三栏证据+未解决疑点

---

## 执行报告（黄药师 · 2026-07-13）

### 已完成（5/7项）

| # | 工作项 | 结果 |
|:--|:--|:--|
| 1 | 6孤儿卡接入 | ✅ digest related追加 + index.md追加 |
| 2 | digest归属修正 | ✅ 双目标法/三类目标从进阶篇→管理篇（裁定#2）|
| 3a | 马拉松双口径注 | ✅ 卡内追加裁定注 |
| 3b | dk伪因果术语映射注 | ✅ 卡内追加术语映射 |
| 3c | 因果口径声明 | ✅ concept-一堂-相关不等于因果卡内追加 |
| 5 | Y模型表述修正 | ✅ digest L109 + coke-spill标题/正文 + index同步 |
| 6 | 勘误表补录 | ✅ 诊断书末尾追加§九勘误表 |

### 移交老顽童（2/7项）

| # | 工作项 | 移交原因 |
|:--|:--|:--|
| 4 | 3原图复核 | 需逐条调VLM输出+口述稿行号，属内容核实 |
| 7 | 6老卡数字复核 | 需逐卡对口述稿行号，属内容核实 |

### 实动文件清单
- `30_wiki/domains/business-formula-domain-digest.md` — 孤儿卡6+归属修正+Y模型表述
- `30_wiki/index.md` — 孤儿卡+ROI/Y修正
- `30_wiki/concept-card-index-latest.md` — ROI/Y修正
- `30_wiki/cases/case-yitang-coke-spill-compensation.md` — ROI/Y修正
- `30_wiki/cases/case-yitang-marathon-ten-seasons.md` — 双口径注
- `30_wiki/dark-knowledges/dk-yitang-business-formula-pseudo-causality-two-masks.md` — 术语映射（修正：plus-times-trap 不是伪因果卡，映射落在 #165 伪因果卡）
- `30_wiki/concepts/concept-一堂-相关不等于因果.md` — 因果口径声明
- `60_feedback/diagnosis/c-domain-business-formula-2026-07-12.md` — 勘误表§九

### 预检
- pre-submit: 待跑
- 扫窗: 实动8文件，申报=实动

---

## 终审记录（欧阳锋 · 2026-07-13 · 结论：PASS / A-）

| 验收项 | 复验方法 | 结果 |
|:---|:---|:---|
| 1. 6 孤儿卡接入 digest | grep related + yaml.safe_load | 6 卡均在 `business-formula-domain-digest.md` related 中 ✅ |
| 1. 6 孤儿卡接入 index | grep `30_wiki/index.md` | 6 卡均已登 ✅ |
| 2. digest 归属修正 | 读五篇课程脉络表 | 双目标法/三类目标已归管理篇 ✅ |
| 3a. 马拉松双口径注 | grep `case-yitang-marathon-ten-seasons.md` | 裁定 #1 注在 L57/L91 ✅ |
| 3b. dk 伪因果术语映射 | grep `dk-yitang-business-formula-pseudo-causality-two-masks.md` | 术语映射（裁定 #3）在 `> **一句话**` 之前，锚点确认 ✅ |
| 3c. 因果口径声明 | grep `concept-一堂-相关不等于因果.md` | 口径声明（裁定 #4）在 L58 ✅ |
| 5. Y 模型表述修正 | 全库 grep `ROI/Y`/`Y/ROI` | 归零；digest L115 / coke-spill 标题正文 / index / concept-card-index 已改 ✅ |
| 6. 勘误表补录 | 读 `c-domain-business-formula-2026-07-12.md` §九 | 系统性误识清单 + 双版本行号约定已补 ✅ |
| 移交项 4/7 | 任务单申报 | 3 原图复核 + 6 老卡数字复核已移交老顽童 ✅ |
| 文件 YAML 合法 | yaml.safe_load 全过 | 5 张改动卡 + digest 全过 ✅ |
| 门禁 | `kdo lint --summary` | 0 new error；2 warning 为 digest source_refs 行号锚点 false positive ✅ |
| 扫窗申报=实动集 | 清单核对 | 8 文件，申报一致 ✅ |

**A- 而非 A 的理由**：首次提交时 3b 落在错误的卡（plus-times-trap）且 apply 脚本静默失败，欧阳锋一审查出后返工。返工后质量干净，但过程暴露「批量脚本 → 不逐条验证」的模式病，扣 A 作为纪律代价。

**终审操作**：
- 已通过 `queue_transition.py review task_20260712_wangyuyan-c-domain-scan-fix-structure --verdict pass --reviewer 欧阳锋 --grade A-` 更新队列与任务单状态；
- 队列状态：`待领取 12 / 审查中 0 / 进行中 1 / 已完成 168`。

**纪律提醒**：以后任何 batch apply 脚本，跑完后必须逐条 grep/读卡验证落地，不能再信「脚本说它做了」。

*欧阳锋 2026-07-13 · #175 终审释放*
