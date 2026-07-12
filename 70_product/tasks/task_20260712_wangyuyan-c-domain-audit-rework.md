---
assignee: kimi
status: in_progress
updated_at: '2026-07-12T14:54:51.834569+00:00'
---
# 任务 #167：C 域质量审计返工（欧阳锋审计报告返工清单落地）

> 编排：王语嫣 | 生产：老顽童 | 终审：欧阳锋
> 优先级：P0（溯源铁律受损 + 增量门禁失盲，直接影响反向蒸馏素材可信度）
> 审计报告：`60_feedback/audit/c-domain-quality-audit-20260712.md`（欧阳锋，2026-07-12）
> lint 明细（复验快照）：`60_feedback/audit/cdomain-lint-detail-after159-20260712.log`（248 ERROR / 94 WARNING 全量逐条清单，生产时以此为准）

## 背景

欧阳锋 C 域整体质量审计发现：双基线口径差异导致增量门禁对 C 域失盲（`.lint_baseline.json` 0 error vs `kdo lint --domain business-formula` 220 new error）。**王语嫣 2026-07-12 独立复验（#159 基线重建后，lint 明细口径）**：**248 ERROR = source_refs file not found 181 + Case card missing section 67；94 WARNING = source_refs typo 46 + Tool 卡缺四节各 10（Purpose/When NOT/Protocol/Critique）+ 未入 index 6**。

死引用 181 条构成（python 全库扫描佐证）：大部分为「路径带备注」格式债（`文件.md（备注）`、`文件.md L429-619（备注）`——证据文件都在，备注括进了引用条目）+ 少量「非路径文本」（如「VLM 图号 004557」）+ 仅约 1 条真·文件缺失。**性质裁定：不是溯源链断裂，是引用格式不规范。**

**两个必须申报的漏项（协议 5）**：
1. **#165 的 6 张新卡全部未入 index**（lint WARNING 6 条，清单见 lint 明细）——#165 终审 A 级时漏检，机械项进本任务修复，同时报欧阳锋作为终审检查项改进
2. **#165 新卡的 source_refs 沿用了提案文档的「路径+行号+（备注）」格式，全部触发 file not found**——污染源是王语嫣提案文档的引用格式习惯，lint 正确写法：路径与行号之外不得带括号备注（备注应写入正文或删除）。tool 卡 `tool-yitang-business-formula-l5-mining-and-verification` 另缺 ## Purpose / ## Protocol 两节

## 交付清单（按审计 §六返工清单，负责人以本任务单为准）

### P0（本任务必做）

1. **修正 181 条 source_refs 死引用**（老顽童）——lint 明细口径为准：
   - 主类「路径带备注」格式债：`文件.md（备注）` 或 `文件.md L429-619（备注）`——**备注一律挪出引用条目**（写入正文或删除），条目只保留 `路径 + 可选 L行号`。证据文件都在，不许删引用、不许编造
   - 次类「非路径文本」：如 `VLM 图号 004557（六层逻辑关系）`——规范化为真实文件路径（`_vlm_output/` 下实际文件），找不到的改 `pending_unknown`
   - 约 1 条真·文件缺失：查补或标 `pending_unknown`/`pending_archive`
   - **含 #165 六张新卡**（沿用了提案文档的错误格式，一并修正）
   - 重灾区 Top8：l6-essence-formulas 6 / abc-model 6 / plus-times-trap 6 / fupanying 6 / session-20260619-xingangwan 5 / digest 4 / ten-paradigms 3 / six-level-logic 3（python 扫描口径，lint 口径全量 181）
   - 验收：`kdo lint --domain business-formula` source_refs file not found 归零

2. **补齐 67 条 case 卡缺失 section**（老顽童，lint 明细清单为准）
   - 缺 `## 关键证据` 等结构化段落，按既有 case 卡骨架补齐；内容无据可补的标 `pending_unknown`，不许编造
   - 验收：lint Case card missing section 归零

3. **鑫港湾孤岛卡收尾**（裁定已落地，残留两处格式修复，老顽童执行）
   - 现状：`frameworks/xingangwan-pharma-business-formulas` domain 已不含 business-formula（移出 C 域已生效，符合王语嫣裁定）
   - 残留修复：①domain 首行格式损坏 `- healthcare- healthcare` → 改为 `- healthcare`；②该卡 id 含 business-formula，按「domain 或 id」口径仍被算入 C 域卡池——卡内加一行归属说明（EC 线资产，待 EC 线激活归位），lint/审计口径以 domain 为准的问题报黄药师纳入 lint 规则考量
   - 验收：domain 格式合法；该卡 lint 无新增 error

### P1（本任务必做）

4. **补齐 Tool 卡缺失 section**（老顽童）——lint 明细：**10 卡 × 4 节**（Purpose / When NOT to Use / Protocol / Critique），含 #165 新 tool 卡 `tool-yitang-business-formula-l5-mining-and-verification`（缺 Purpose / Protocol 两节）。无据可补标 `pending_unknown`，不许编造——验收：lint Tool card missing section 归零
5. **index 登记 7 卡**（老顽童）——`tool-一堂-业务公式-L1L6参数分层自检`（审计漏登记）+ **#165 全部 6 张新卡**（5 dk + 1 tool，终审漏检项）。验收：7 卡 grep 命中 `30_wiki/index.md`，lint「not listed in index」归零

### P2（本任务必做）

6. **清理 `business-formula-to-kdo-card-quality` 的 4 条 kdo-\* 死链**（老顽童）——目标卡确认不存在则摘链，存在则修正链接

### 不在本任务（审计清单中的其他项）

- 总纲 `framework-一堂-业务公式拆解-总纲` 终审 → 欧阳锋自有节奏（审计 P0-3，非生产任务）
- 51 张 enriched 卡分批终审 → 欧阳锋（审计 P2，建议顺序：framework/concept → tool → case）

## ⚠️ 与 #159 的时序联动（更新）

~~#159 基线重建前完成~~ —— **#159 已 reviewed A-（基线签名 10380→8142），本任务变为「基线重建后的真债清扫」**：复验证实基线重建未吸收这批引用格式债（lint 全量 248 error 仍在），本任务正常推进即可，清扫完成后建议黄药师复验基线签名是否需再回卷一次。

## 验收点（欧阳锋用）

1. `kdo lint --domain business-formula`：source_refs dead 归零、Case/Tool missing section 归零
2. 修复方式合规：能补则补，无据标 pending_unknown/pending_archive，无编造无删链了事
3. 鑫港湾卡 domain 格式修复后合法、卡内有归属说明、无新增 lint error
4. index 登记 grep 可验证
5. 扫窗申报=实动集（协议 2）

## 依赖

- 与 #166（agent 迭代）可并行；#166 引用本任务修复后的卡更准确
- #159 基线重建被本任务阻塞（见时序联动）
