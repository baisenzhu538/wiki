---
id: task_20260906_laowantong-audit-batch1bc
title: "暗知识体检 A1 批 1b/1c 放行 + 28 候选 grep 重跑出清单（老朱拍板：继续挖+清单他拍板）"
seq: 662
status: pending_review
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-06
decision_source: 老朱 09-06 六项拍板（1继续挖/2清单他拍板）；#659 终审条件（产卡立项前 grep 重跑）
reviewer: 欧阳锋
instance: laowantong
updated_at: '2026-09-06T07:09:31.927612+00:00'
evidence: 60_feedback/diagnosis/working/a1-batch1c-goldmine-ledger.md
---

# #662 A1 批 1b/1c + 候选清单重跑（老顽童）

## 任务一：grep 重跑出拍板清单（先做，老朱等着拍板）
批 1a 的 22 项+试金石 6 项=28 条漏挖候选，按 #659 终审条件**统一重跑 grep 存在性核查**（防与既有卡重复），产出《漏挖候选拍板清单》：每条=候选内容一句话+行号锚+建议形态（dk 挂靠/新卡/case）+grep 重跑结果。交老朱拍板产卡范围。

## 任务二：批 1b（王欢×2 178KB + 转化率黑客 80KB）
同批 1a 标准：逐字读→金矿台账（行号锚）→形态路由→覆盖率自评→提审。

## 任务三：批 1c（收官路演 527KB + AI剧本 128KB + Codex PPT 107KB + AI native 46KB + 拆书 24KB）
同上标准。收官路演体量最大（527KB），允许内部再分两次提审。

## 纪律
- 逐字读全文（W1）；金矿台账必附（E049）；负向判词带核查锚（宪法）
- 每小批提审一次；#659 的 B 级终审条件随本单闭环

## 执行报告（老顽童 09-06 15:10）

**交付物**：①《漏挖候选拍板清单》`60_feedback/diagnosis/working/a1-batch1bc-greprerun-decision-list.md`（28 条 grep 统一重跑，含机读对账 json+复跑工具）②批 1b 台账 `a1-batch1b-goldmine-ledger.md`（3 件 5805 行，106 锚）③批 1c 台账 `a1-batch1c-goldmine-ledger.md`（5 件 14707 行 100% 读毕，190+ 锚，分两次提审均已落盘）

**完成内容**：任务一 grep 重跑——12 维持/3 部分/12 翻案/1 撤出；试金石 6 条 5 翻案（漏挖率 30%→~5%【实证】）；两大系统发现（批 1a 六条 0 命中判词失真+试金石同簇漏查 122 行 case 卡漏 211 行 method 卡）。任务二批 1b——词根复检证伪 Phase0 A 级零产出 3/3（王欢族 31 卡/晓莉专卡在库），漏挖 24 条，X-32 数字修正级（专卡声明无数字 vs 口述两处 1000 家分校）。任务三批 1c——拆书/AI native/Codex PPT/AI剧本/收官路演全读毕；三大整件级空白（阿迪亚 AI Native Benchmark/方振义 Codex PPT 工作流/路演 18 场全量）；新增候选约 100 条；"AI+场景才有价值"四源同构；伦理敏感 1 条不立卡交老朱裁定。

**验证**：全部判定可复跑（行号锚+grep 命中数+机读 json）；负向判词均附存在性核查锚（宪法第二条）；自攻击四路已过（批 1c 含重复结构复核）；pre-submit 全程 PASS；三份台账均已 commit 入仓。

**边界**：不产新卡（产卡待老朱对拍板清单拍板后另行立项）；讲者自述数字需产卡时标"待独立核实"；AI剧本与收官路演为重复拼接结构（已声明，按去重计）；路演合集第一遍与第二遍微小文本差异未逐字 diff。

**需要谁动作**：王语嫣——三份台账抽验双签（注意件 8 行号两遍分界 L2600/L2601）；欧阳锋——终审三份台账；老朱——对拍板清单拍板（批 1a 维持 12+批 1b 新增 24+批 1c 新增约 100，建议 A 优先 20 条）；知识仲裁者——新增冲突组（词变体/双版本数字/同人物三名）。

## pre-submit 输出（三份台账最终轮，均 PASS）

- 拍板清单：✅ Result: PASS（YAML/WIKILINK/DOMAIN/DK_SECTION/OUTLINK/POSITION/SOURCE_REACHABILITY 等 0 issues，1 info 为 quality pre-score）
- 批 1b 台账：✅ Result: PASS（同上 0 issues）
- 批 1c 台账：✅ Result: PASS（同上 0 issues）

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 1 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）
