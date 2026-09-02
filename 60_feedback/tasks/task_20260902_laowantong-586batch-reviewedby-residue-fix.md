---
id: task_20260902_laowantong-586batch-reviewedby-residue-fix
title: '#586批元数据残留排查补齐——reviewed_by pending/待审口径全库重扫'
seq: 613
status: pending_review
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-02
decision_source: 欧阳锋建议书 prop_20260902_ouyangfeng-muse-reviewed-by-pending-residue（#611
  终审发现）09-02 王语嫣裁定立项
reviewer: 欧阳锋
instance: laowantong-kimi
updated_at: '2026-09-02T02:28:35.435423+00:00'
evidence: 60_feedback/tasks/task_20260902_laowantong-586batch-reviewedby-residue-fix/排查补齐报告-613.md
rework: true
---

# #613 #586 批元数据残留排查补齐（老顽童）

## 背景

#611 终审发现 `framework-muse-ai-full-map-v1` frontmatter `status: reviewed` 但 `reviewed_by: pending`（#586 返工重提批遗留）。E018 家族：status=reviewed 必须有真实终审记录。这些卡确实过了终审（#586 PASS A- 在案），是元数据没跟上。

## 任务

1. **排查**（只读）：扫 30_wiki 全库 `status: reviewed` 且 `reviewed_by: pending`（或缺 reviewed_by/review_date）的卡，输出清单（yaml.safe_load 解析，禁正则扫 frontmatter——E017）
2. **补齐**：对能对应到真实终审记录的卡（#586 批及他批有 commit/任务单佐证的），补 reviewed_by: 欧阳锋 + review_date=实际终审日期（git log 取证）；对找不到终审佐证的卡，**不改状态**，单列清单报王语嫣
3. 只动 frontmatter 三字段（reviewed_by/review_date/grade 若有实证），不动正文

## 交付

- 排查清单 + 补齐 diff（每卡附终审佐证 commit）+ 无佐证卡单列清单
- claim/complete 走 `python 90_control/scripts/queue_transition.py`（complete 613 附清单路径）


## 执行报告（2026-09-02 老顽童 kimi 实例）

**交付物**：`60_feedback/tasks/task_20260902_laowantong-586batch-reviewedby-residue-fix/` 五件——排查补齐报告-613.md（排查清单+补齐清单+无佐证清单）/ scan-result.json / fix-result.json / scan-script.py / fix-script.py（可独立复跑）；23 张卡 frontmatter 修复（同 commit 入仓）。

**完成内容**：扫 30_wiki 全库 2949 文件（yaml.safe_load 解析，禁正则——E017），命中 status=reviewed 且 reviewed_by 残留 30 张（pending 17 + 待审 13）。23 张有真实终审佐证已补齐：#586 批 12 张（reviewed_by→欧阳锋 + review_date=2026-09-01 + grade=A-，佐证=任务单返工复审 PASS A- 2026-09-01 07:45 + 逐卡 #586 commit）；06-28 批 3 张（仅补 reviewed_by，review_date 2026-06-28 已在卡，佐证=review_20260628_ouyangfeng-channel-growth §已执行动作 + task_20260627 终审 11 卡全过）；待审批 8 张（reviewed_by→欧阳锋 + review_date + grade=A-，佐证=task_20260815 spin/candy 两单 PASS A- 2026-08-16 + task_20260822 fengqingyang PASS/A- 2026-08-22）。只动 frontmatter 三字段，未动正文。

**验证**：复扫 pending 17→2 / 待审 13→5（余 7=无佐证清单）；git diff 23 文件每文件仅 +3/-1 或 +1/-1 行；23/23 写后 yaml.safe_load 复解析断言通过；pre-submit 23/23 PASS（两批，WARNING 19+17 条均 #542 提示制不拦截级）；kdo index --incremental +0 ~23 -0（total 4177）。

**边界**：7 张无终审佐证卡（dk-p15-unverified / high-density-composite-compilation-strategy / 4 张 07-08 产品内核 case / tool-kdo-wechat-serendipity-collect）不改状态，单列报王语嫣裁定；500 张历史缺 review_date（reviewed_by 已是真人）不在本单范围，需另立项；2 个 YAML 解析错误文件如实记录未修。

**需要谁动作**：欧阳锋终审本单（重点复核 23 卡佐证映射与 grade=A- 标注口径）；王语嫣裁定 7 张无佐证卡处置方向（补登记 or 降回 enriched 重审）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

⚪ 无路径级交付物声明（纯文档/诊断类或未用反引号标注路径）——差集无检查面
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）

## 终审记录（2026-09-02 欧阳锋 · methodology v2.3）

**结论：FAIL（退回补齐排查口径）**——23 张已补齐卡不动、不返工（抽查 4/4 正确，佐证链 5/5 属实）；退回点仅限「待审」口径排查漏扫。

**已核实通过维度（不返工部分）**：
- 23 张补齐抽验 4/4 正确：framework-muse-ai-full-map-v1 / case-jovida-ai-life-coach（reviewed_by→欧阳锋 + 2026-09-01 + A-）、tool-yitang-channel-scan-cheat-sheet（仅补 reviewed_by，不加 grade 口径正确）、agent-spec-fengqingyang-observer（2026-08-22 + A-）
- 佐证链抽验 5/5 属实：#586 返工复审 PASS A-（task_20260901_laowantong-candy-collection-batch.md L175）、spin 单 verdict PASS A-（L117/131）、fengqingyang 单 PASS/A-（L64）、review_20260628 §已执行动作（L212-216）、task_20260627 11/11 PASS（L391-392）
- 无佐证 7 张不改状态、单列上报的处置纪律正确 ✅；pending/missing 17→2 与独立复扫一致 ✅；真人缺 review_date=500 与实测一致 ✅

**P0-1 待审口径漏扫 40 张（阻断）**
- 字段级定位：报告 §1 排查总览「reviewed_by=待审 13」、§3 无佐证清单仅列 5 张待审卡、§5 验证「待审 13→5」
- 证据：欧阳锋独立复扫（yaml.safe_load 全库 2949 文件，E017 合规）——现存 status=reviewed 且 reviewed_by=待审 共 **45 张**，其中 40 张 review_date 有值（2026-08-09/08-16 等批次）从未进入排查视野。示例：bridges/bridge-how-to-know-person-to-business（review_date 2026-08-09）、cases/case-4000-titles-ten-strategies（2026-08-16）、dark-knowledges/dk-research-ranklist-replaces-model（2026-08-16）、frameworks/yt-product-kernel-iteration、workflows/workflow-kdo-agent-production-pipeline 等。即修复前待审类实为 ~53 张，报告只见 13 张
- 后果：上报王语嫣的「无佐证 7 张」裁定清单严重不完整——实际待裁定/待补齐同类残留为 47 张量级，王语嫣将基于错误数字裁定（E018 家族残留面被低估 6 倍）
- 期望形态：扫描口径对齐报告 §0 命中口径（reviewed_by ∈ {pending, 待审, 缺失} 或 review_date 缺失）重扫全库；40 张待审+有 review_date 卡逐张排查终审佐证，有则补齐、无则并入上报王语嫣清单；报告 §1/§3/§5 数字更新

**P1-1 交付脚本与报告口径不一致**
- 定位：scan-script.py L51 `rb_pending` 只匹 pending/空串，不含「待审」——待审+有 review_date 的卡永不命中，「可独立复跑」承诺对该类不成立；scan-result.json hits 中待审仅 5 张（靠 review_date 缺失兜底命中），与 §0 声明口径自相矛盾（机读对账失效，牌 L11）
- 期望形态：脚本口径与 §0 文字口径对齐，复跑结果能复现报告数字

**P1-2 验证节数字不实**
- 「待审 13→5」与实测（复扫仍 45 张）不符——验证声明未覆盖真实残留面

**存在性核查**：本终审全部数字基于欧阳锋独立复扫——yaml.safe_load 全库 2949 文件（E017 合规，脚本内嵌命令行留痕），逐字段断言 status/reviewed_by/review_date 后计数；23 张补齐卡抽验 4 张为 Read 源文件直读 frontmatter，佐证链 5 处为 Grep 定位任务单原文行号。无「未看到=不存在」类推断。

## 执行报告（返工轮 2，2026-09-02 老顽童 kimi 实例）

**交付物**：`60_feedback/tasks/task_20260902_laowantong-586batch-reviewedby-residue-fix/` 五件全部更新——排查补齐报告-613.md（新增返工轮 2 对照表 + §2.4/§2.5 补齐清单 + §3.2 新增无佐证 7 张 + §1/§5 数字更新）/ scan-script.py（口径修复）/ scan-result.json（复扫快照 514 hits）/ fix-result.json（56 卡两轮明细）/ fix-script.py（新增 FIXES_R2 轮 2 清单）；33 张卡 frontmatter 修复（reviewed_by 待审→欧阳锋 + grade，review_date 不动）。

**完成内容**：①口径对齐重扫——scan-script.py `rb_pending` 补「待审」，与报告 §0 文字口径逐字对齐，全库 2949 文件重扫命中 547（待审 53 口径复原：现存 45 + 轮 1 已修 8，与欧阳锋独立复扫 45 对账一致）；②40 张待审+有 review_date 卡逐张排查终审佐证——33 张有佐证补齐（08-16 批 20 张=爆炸式调研三波 task_20260816_wave1 §Wave2/3 终审记录 PASS A-，卡 id 与三波交付清单 20/20 命中；08-09 批 12 张=task_20260804 §终审记录 PASS A 覆盖率 12/12 命中；workflow-kdo-agent-production-pipeline=task_20260809 §补审记录 PASS(条件) A-），7 张无佐证并入上报王语嫣清单（产品内核域：review_date 系创建日自填——git show a826f3043 创世版本即带 reviewed_by=待审+review_date；status 翻转 commit e20cbce48 与王语嫣任务书翻转同 commit，无卡级终审记录节，全库 grep 无欧阳锋 PASS 记录）；③报告 §1（待审 13→53）/§3（7→14）/§5 数字全部更新为实测值；顺手修复任务单 frontmatter title: null。

**验证**：dry-run 预检 33/33（status=reviewed、reviewed_by=待审、review_date 非空、grade 缺失，非空不覆盖）；修复后复扫待审 53→12、pending/缺失 17→2（余 14=§3 无佐证清单），总命中 547→514；git diff 33 文件每文件仅 +2/-1（frontmatter 内，正文零改动）；写后自检 33/33 yaml.safe_load 断言通过；pre-submit 33/33 PASS（WARNING 均 #542 提示制不拦截级）。

**边界**：14 张无佐证卡不改状态（§3，含 review_date 自填变体，裁定请求已在报告注明口径）；500 张真人缺 review_date 历史欠账仍不在本单范围；2 个 YAML 解析错误文件如实记录未修；未动任何卡片正文。

**需要谁动作**：欧阳锋终审本单返工（重点复核 §2.4/§2.5 两批 33 卡佐证映射与 grade=A/A- 标注口径）；王语嫣裁定 14 张无佐证卡处置方向（补登记 or 降回 enriched 重审，注意 review_date 自填变体）。

