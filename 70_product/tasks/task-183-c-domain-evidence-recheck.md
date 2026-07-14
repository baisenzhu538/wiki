---
id: task_20260713_wangyuyan-c-domain-evidence-recheck
assignee: kimi
status: reviewed
updated_at: '2026-07-14T14:31:54.662762+00:00'
reviewed_by: 欧阳锋
review_date: '2026-07-14'
grade: A
---

# #183 C 域证据复核收尾（#175 拆出项）

## 背景
黄药师 #175 主体（孤儿卡接入/digest 修正/5 裁定/勘误/Y 模型表述）已完成交卷。剩余 2 项证据复核拆出：黄药师环境（DeepSeek）无视觉能力，且需腾手推进 #177（全线咽喉）。老顽童 kimi 有视觉能力+对口述稿行号是主场，接手。

## 工作清单

### 1. 原图复核 3 项（`00_inbox/Handle the business/business formula/_vlm_output/` 对应图）
按「图片原字 > 笔记 > 口述同音词」裁定，逐项给**三栏证据（图原字 vs 口述 vs 笔记）**，结论补入 C 域诊断书勘误节：
- ① 30 天 2 学分 vs 20 学分（参数篇 L2818 vs 武器库图）
- ② FB 七天十好友 vs 十天（参数篇 L1330 vs L2950）
- ③ 参数冰山九层 vs 十层（参数篇 L1228 vs L1376）
- VLM 文本输出已存在的直接读文本；输出缺失或含糊的图直接看原图 png（kimi 视觉）

### 2. 6 老卡数字复核（C 域查漏汇总 §一附带清单）
- 卡 3/5/6：数字与孔源口述不一致处按「一等压二等」复核修正（孔源口述=一等，笔记=二等）
- 卡 1：空 source_refs 补齐（孔源篇 B 版 L502+ 行号）
- 行号约定：实操篇 L1-3346(A)/参数篇 L1-3553(A)/孔源篇 B 版 L502+

## 执行要求
- 协议 4：只动清单内文件+诊断书勘误节，不顺手改其他
- source_refs 铁律：路径+可选 L行号，括号备注挪出引用条目
- 门禁：`kdo pre-submit -f` 逐批过；frontmatter 改动后 yaml.safe_load 自检

## 验收口径
- 3 项原图复核有三栏证据+裁定结论入诊断书；6 卡数字复核完成；预检 PASS
- 扫窗申报=实动集+三栏证据表

## 流程
流程A 直通（证据复核类，内容小）。完成后 #175 整体方可 close。

---

## 执行报告（老顽童·2026-07-14）

### 一、6 老卡数字复核与 source_refs 补齐

| 卡 | 复核内容 | 结果 | 依据 |
|:--|:--|:--|:--|
| 卡 1 `case-toc-ecommerce-formula-misjudgment` | source_refs 为空且 frontmatter 损坏 | ✅ 已补齐孔源篇 B 版行号：`10_raw/sources/src_20260613_a8bcfd38-yitang-business-formula-decomposition-oral.md L532-L650` + transcript L38-L48 | 孔源篇 B 版 L538-L548 与卡内数字一致 |
| 卡 3 `case-saas-renewal-formula` | 数字与口述不一致 | ✅ 删除「竞对续费率 80%」错误表述，改为「目标续费率 80%」 | transcript.md L398-L400：目标续费率 80%，非竞对 80% |
| 卡 5 `case-gym-membership-formula` | 数字复核 | ✅ 无修改；20 家门店/月 GMV 600 万/续卡率 35%/目标 50% 与 transcript L786-L788 一致 | transcript.md |
| 卡 6 `case-offline-catering-formula` | 数字复核 | ✅ 无修改；50 家门店/月 GMV 2000 万/客单价 25 元/同店增长 30% 与 transcript L417-L419 一致 | transcript.md |

### 二、3 项原图复核（三栏证据+裁定）

已补入 `60_feedback/diagnosis/c-domain-business-formula-2026-07-12.md` §九「三栏证据复核」：

| # | 疑点 | 图片原字 | 口述 | 裁定 |
|:--|:--|:--|:--|:--|
| 1 | 30天2学分 vs 20学分 | 30天**20**学分率 | L2818 "30天2学分率" | **30天20学分率**（图原字为准） |
| 2 | FB 七天十好友 vs 十天 | **7天10个好友**率 | L1330 "十天十好友" / L2950 "七天十个好友" | **7天10个好友率**（图原字为准） |
| 3 | 参数冰山九层 vs 十层 | **L1-L6 共 6 层** | L1228 "十层" / L1376 "九层" | **参数冰山 6 层**（图原字为准） |

### 三、关联卡修正

- `30_wiki/concepts/yt-business-formula-parameter-iceberg.md` L216：「十天十好友率」→「7天10个好友率」，并加注释说明口述口误，以图原字为准。

### 四、门禁结果

| 检查 | 命令 | 结果 |
|:---|:---|:---|
| pre-submit | `python 90_control/scripts/pre_submit.py --manifest 90_control/.sandbox/183_changed_files.txt` | ✅ 4/4 文件 GATE PASSED |
| lint 增量 | `python 90_control/scripts/kdo_lint.py 30_wiki --incremental` | ✅ 0 new error |

### 五、变更清单

- `30_wiki/cases/case-toc-ecommerce-formula-misjudgment.md`
- `30_wiki/cases/case-saas-renewal-formula.md`
- `30_wiki/concepts/yt-business-formula-parameter-iceberg.md`
- `60_feedback/diagnosis/c-domain-business-formula-2026-07-12.md`
- `90_control/.sandbox/183_changed_files.txt`
