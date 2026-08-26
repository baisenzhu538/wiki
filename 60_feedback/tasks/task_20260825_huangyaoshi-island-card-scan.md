---
id: 528
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-26T12:32:18.056971+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- kdo-tools/
- 90_control/quality-gates/
---

# #528 孤岛卡扫描 lint（无出链无入链卡定期出清单）

- **任务号**：#528
- **状态**：queued
- **assignee**：huangyaoshi（扫描器+定期挂载；欧阳锋终审）
- **优先级**：P2（类比遮蔽检索的治本层——结构上消灭死胡同，不靠人「记得小心」）
- **立项**：2026-08-25 王语嫣（老朱追问「知识卡无法解决，还有什么办法」——裁定补结构层；盲测报告 P1 同族）

## 背景

盲测第 1 问失败的结构根因：OCR 卡是孤岛（related 空、无入链），检索者落在上面=死胡同。#526 手工补了一张，但全库孤岛存量未知。dk 卡管认知、盲测管兜底，本单管结构：定期扫描让孤岛上不了岸。graph 数据现成（30_wiki/.graph），tags-audit 指标族可挂。

## 任务

1. **孤岛扫描器**：30_wiki 卡双无检测——无出链（related 空）且无入链（无他卡 related 指向；graph 数据+related 反查双源核对）；排除 intentionally 孤立类型（agent-spec 类按口径豁免清单）
2. **出清单**：机读 json+人读 md（按域分组，标注「高命中风险」=被 grep 高频命中的孤岛优先挂链）交王语嫣编排挂链批次
3. **定期挂载**：挂 tags-audit 指标族或健康检查（黄药师定，失败可见不静默），孤岛数成趋势指标
4. 回归：构造孤岛/非孤岛/豁免三类用例

## 边界

- 只扫描出清单，不自动改卡（挂链是内容判断走编排批次）；WARNING 制不拦流转
- 10_raw/inbox 层不在扫描范围（转录层路标由 #526 模式处理）；与 #527 分工：#527 管「被依赖却 draft」，本单管「无人依赖的孤岛」

## 验收

- 扫描器+三类用例回归通过；存量孤岛清单交付（数量+路径）；定期挂载点说明
- 欧阳锋终审

## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：孤岛卡扫描 lint 上线。①`island_scan.py`：30_wiki 全库双无检测——无出链（frontmatter related 空）且无入链（related 反查：他卡 related 的 stem/路径片段指向本卡）；豁免口径=agent-spec 类（type 或 agent-specs 目录）+index/log 非卡资产（#527 同款教训：初扫 log.md/README 混入，剔除后 287→285）；扫描面只收有 frontmatter type 的卡（README 类不进面）；②清单双格式落 `60_feedback/auto/island-cards/`（json 机读+md 人读按域分组，framework/tool 卡型标为挂链高优先——检索主靶）；③定期挂载=health-check 每日 02:07（exit 恒 0 WARNING 制，趋势可见于每日巡检输出）；④回归 4 例。

**交付物**：
- `kdo-tools/island_scan.py`（扫描器+清单渲染）
- `kdo-tools/tests/test_island_scan.py`（新：4 例回归）
- `60_feedback/auto/island-cards/islands.{json,md}`（存量清单：285 张/2869 扫描面）
- `90_control/scripts/health-check.py`（挂载）+ `90_control/infrastructure-inventory.md`（登记）

**验证**：
- L1 单测 4 例全过：孤岛检出（双无）/有出链非孤岛/有入链非孤岛/agent-spec 豁免/非卡文件不进面；基线零退步：kdo-tools **160 passed**（156+4）、90_control **157 passed**
- L2 狗粮：真库实跑——孤岛 285 张/2869 卡（约 10%）清单落盘双格式可读；盲测第 1 问的 OCR 卡死胡同型在册可核
- L3 待活体：每日健康检查孤岛数成趋势；王语嫣按清单编排挂链批次后孤岛数应降

**边界**：只扫描出清单零改卡 ✅；WARNING 制 exit 恒 0 不拦流转 ✅；10_raw/inbox 不在扫描面 ✅；与 #527 分工不重叠（被依赖 draft vs 无人依赖孤岛）✅；graph 数据已废弃（.graph/index.json 标 deprecated）未用——入链反查改为 related 全库反查自建，数据新鲜度自愈。

**需要谁动作**：欧阳锋终审本单；王语嫣——存量清单 285 张在 `60_feedback/auto/island-cards/`（按域分组，framework/tool 优先），请编排挂链批次。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 6 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🟡 ⚠️ 意见书含宽负向词（无）无核查锚点——按需人工确认（#433 不硬杀）；锚点：⚪ 无锚点
