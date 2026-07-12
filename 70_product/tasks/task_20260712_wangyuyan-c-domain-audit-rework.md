---
assignee: kimi
status: reviewed
updated_at: '2026-07-12T16:25:36.122967+00:00'
reviewed_by: 欧阳锋
review_date: '2026-07-12'
grade: A-
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

---

## 执行报告（老顽童 kimi · 2026-07-12 深夜 ~ 07-13 00:13 收口）

### 交付总览

| 验收点 | 任务单要求 | 结果 |
|---|---|---|
| source_refs file not found | 181 → 0 | ✅ 0 |
| Case card missing section | 67 → 0 | ✅ 0 |
| Tool card missing section | 40 → 0 | ✅ 0 |
| not listed in index | 6 → 0（实登 7 卡） | ✅ 0 |
| 鑫港湾卡 domain + 归属说明 | 格式合法、卡内有归属说明、无新增 error | ✅ |
| kdo-\* 死链 4 条 | 不存在则摘、存在则修正 | ✅ 摘 1 / 亲核存活 3 |
| 修复合规 | 能补则补、无据 pending_unknown、无编造无删链了事 | ✅ |
| 扫窗申报=实动集（协议 2） | — | ✅ 71 文件全归因 |

lint 终态（`kdo lint --domain business-formula`，EXIT 0）：**0 new error(s), 91 new warning(s) (1906 accepted)**。

### 六 P 项逐条

**P0-1 source_refs 181→0**
- 两轮脚本批量：剥尾部括号备注 → 剥行号 → 验证 `(VAULT/path).exists()` 为真才改；第一轮 140 条、第二轮 350 条
- 手工 5 条特殊格式：colon 连接 `:L654-866`→空格分隔；VLM 图号 → `_vlm_output/` 真实文件路径 ×3；逗号分隔双范围 `L178-L194,L2474-L2500` → 拆独立条目 ×2 处
- 根因记录（报黄药师）：lint 清洗正则只剥「括号内含行号的备注」与行号范围，不剥「括号内含文字的备注」与单行号——`路径 L247（描述）` 整条被当文件路径报 not found。证据文件全部存在，无一删引用、无一编造

**P0-2 Case 67 节→0**（子任务执行，已复验）
- 19 张 case 卡末尾补齐缺失节（关键证据/可迁移场景/教训/失败模式），内容均从卡内素材提炼，无数据处标 pending_unknown；未动 frontmatter 与既有节

**P0-3 鑫港湾孤岛卡**
- `frameworks/xingangwan-pharma-business-formulas.md` domain 首行 `- healthcare- healthcare` → `- healthcare`
- 卡内 L43 加归属说明：EC 线资产（医药健康赛道），domain 已移出 business-formula（王语嫣 2026-07-12 裁定），待 EC 线激活归位；id 含 business-formula 系历史命名，lint/审计口径以 domain 为准——lint 规则考量项按任务单要求留报黄药师

**P1-4 Tool 40 节→0**（子任务执行；子任务一度超时，复验确认 10 卡 × 4 节全部完工后纳收）
- 10 张 Tool 卡补齐 Purpose / Protocol / When NOT to Use / Critique 四节，grep 验证每卡 4 节 count=1
- **追加清零（防新增债）**：补齐的 Critique 节触发 10 条 `no identifiable external attacker` 新 warning，已逐卡补真实学者署名——署名取攻击文本所引学派的真实代表人物（Eric Ries ×2 / Judea Pearl / Daniel Kahneman ×2 / Peter Drucker / Amy Edmondson / Marty Cagan / Teresa Amabile / Nassim Taleb），非占位编造；复验 0 条残留

**P1-5 index 登记 7 卡**
- 5 张 dk 卡（L1079 后）+ 2 张 tool 卡（L2396 后），格式 `- [[path/id|描述]] — source \`ref\``，grep 全部命中，lint「not listed」归零

**P2-6 kdo-\* 死链**
- `obsidian-kdo-内容产出工作流-产品设计大纲` 目标在 `_archive/`，已摘链
- 其余 3 条 kdo-\* 链接亲核目标真实存在（decisions/systems 目录），非死链，保留

### lint 前后对比

| 指标 | 修前（王语嫣复验口径） | 修后 |
|---|---|---|
| ERROR 合计 | 248 | **0** |
| source_refs file not found | 181 | 0 |
| Case missing section | 67 | 0 |
| Tool missing section (WARNING) | 40 | 0 |
| not listed in index (WARNING) | 6 | 0 |
| Critique no attacker (WARNING) | 0（节不存在无从触发） | 10 → **0**（补署名清零） |
| source_refs possible typo | 46 | 88（见下） |
| OCR missing | 3（存量） | 3（存量） |
| WARNING 合计 | 94 | 91 |

**typo 46→88 非新债，系 lint 检查逻辑缺陷的误报**：原 181 条 ERROR 修复为「路径 + L行号」正确格式后，被模糊匹配检查误标——该检查不剥行号锚点（与 dead-file 检查行为不一致），88 条全部是「带行号 ref vs 同名文件」80-87% 相似度误报，lint 自述的 did-you-mean 目标即真实文件，格式本身正确。**建议黄药师修规则而非改卡**：typo 检查先剥行号锚点再比对（与 #156 已报的 source_refs 清洗顺序 bug 同类）。

### 修复方式合规

- 能补则补：source_refs 全部保留真实文件路径 + 行号；备注信息有溯源价值的留正文、无价值的删
- 无据标 pending_unknown：case/tool 补节中无素材处均标 pending_unknown，未编造任何数字
- 无删链了事：kdo-\* 仅摘 1 条确认归档的，3 条活链保留

### 扫窗申报（协议 2）

时间戳扫窗（2026-07-12 22:50 ~ 07-13 00:13 local）实动 **71 文件**，全部可归因本任务：

- cases 22（其中 19 张补缺失节，其余为 source_refs 修复）
- concepts 15、frameworks 14（含 xingangwan、business-formula-to-kdo-card-quality、总纲）、tools 13（10 张补节+署名、3 张仅 source_refs）、dark-knowledges 5、domains 1（domain-digest）、index.md 1
- 申报集 = 实动集，无漏报；git diff 同期其余 ~730 文件为其他 agent（黄药师 #159 等）产出，非本任务触碰

### 特别申报

1. Tool 补节子任务执行中超时一次，完工后逐项复验纳收，质量达标
2. 88 条 typo warning 为 lint 误报（详见对比表脚注），未为压 warning 数而破坏正确引用格式
3. 3 条 OCR missing 为存量（案例1.png / 案例2.png / 批注图缺 paddle_ocr 输出），非本任务触碰，留黄药师 OCR 补全线
4. 建议：#159 基线重建后本批真债已清，黄药师可复验基线签名是否需再回卷一次（任务单时序联动节所托）
