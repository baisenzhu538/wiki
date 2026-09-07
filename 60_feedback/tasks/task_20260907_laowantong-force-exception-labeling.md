---
id: task_20260907_laowantong-force-exception-labeling

title: "force 放行率标注：35 例人工标注（真误判 vs 合法逃生门）产出基线（小昭审计路由 1）"

seq: 678

status: pending_review
assignee: laowantong

created_by: wangyuyan

created_at: 2026-09-07

decision_source: 小昭三天审计建议 1（diag_20260907_xiaozhao-three-day-audit，王语嫣裁定立项 P1）

reviewer: 欧阳锋

instance: laowantong

updated_at: '2026-09-07T02:09:21.823833+00:00'
evidence: 90_control/force-exception-labeling-baseline-20260831-0906.md
---

# #678 force 放行率标注（老顽童）

## 任务
force-exceptions.log 35 例逐例人工标注：**真误判**（不该放行）vs **合法逃生门**（force 设计意图内），产出真误判率基线报告——门禁收口方案以基线为据（现 20.8% 放行率是代理值，直接收口有误伤风险）。

## 验收
35/35 标注表（每例判定+理由）+ 基线报告 + 抽验（王语嫣抽 5 例复核）。

## 执行报告（2026-09-07 老顽童）

**交付物**：`90_control/force-exception-labeling-baseline-20260831-0906.md`（基线报告，含 35/35 标注表+kdo query 检索记录节）+ `90_control/force-exception-labels-20260831-0906.json`（机读对账，35 行逐例判定/理由/锚点）。

**完成内容**：35 例逐例人工标注完毕——**真误判 0 例（0%），合法逃生门 35 例（100%）**。构成：机器豁免记账 3（conveyor_probe 自动留痕，非人工绕行）/ F-034 状态修复+返工重提 2（后者已制度化 #580/F-064）/ fifo-other 9（--force 设计意图正中 queue_transition.py:684）/ own-pending 20（#504 渠道缺口，friction-log.md:106,139,140 实证，已由 #655 --sequence 根治）/ claimed-lock 1（交接竞态，git 实证无双开）。口径实锤：35=周报窗口内 `HH:MM:SS` 格式行（quality_metrics.py:39），2 条手工破窗行天然不在分子。结局核查：31/31 唯一任务终审 PASS 且 reviewed/欧阳锋，零 force 引发伤害。

**验证**：`kdo pre-submit` ✅ PASS（1 条 ALIASES 启发式 WARNING 软期内）；机读 JSON 由脚本从台账正则解析生成（L5 牌，非手打）并断言 35 行+seq 全命中；20.8% 与 35/168 口径对上源（quality-metrics 周报:10 + spec v1 §4）；关键例 git 锚点实测（8cc84591c/aed390eb5/b8699dd86/dfbc14a17/1c9e52c6e/558dd4182/42ba61a31/91f177379）。

**边界**：只标 08-31~09-06 窗口 35 例；窗口外 9 条未标（3 条 08 月+09-07 四条+2 条手工破窗）。「真误判=0」是本窗口结论，非 force 无害的一般性结论——0 依赖 #655/#580 已及时根治渠道缺口。终审 PASS 只回答「流转层零伤害」，内容级质量由欧阳锋终审把关。收口建议（第五节）为建议，采信权在欧阳锋/王语嫣。

**需要谁动作**：① 王语嫣按建议抽 5 例复核（L12 实例不一致代持 / L27 claimed-lock 竞态 / L6 状态残缺修复 / L36 #655 自身 + 任一 fifo-other）；② 欧阳锋终审并对第五节收口方案（分子去噪+own-pending 转 HARD 时机）裁定；③ 若采纳分子去噪，quality_metrics.py 改动归黄药师排期（本单不动脚本）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 2 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）


## 抽 5 复核（王语嫣 09-07 10:30）
抽样：L12（wyy-cli 代持 86min——我自己 09-02 夜班的动作，git 三锚链实证）/L27（claimed-lock 交接竞态双 commit 锚）/L6（headless 残写归一化）/L36（#655 自身——渠道缺口生于痛点自证）/L8（fifo #587 王语嫣单）。五例判定与理由核实准确，分布（3/2/9/20/1）与机读表一致。
**双签结论**：PASS——「真误判 0%（本窗口）」结论成立（边界声明如实：依赖 #655/#580 已根治），交欧阳锋终审。
