---
id: task_20260802_wangyuyan-global-metadata-p2
task_id: 224
assignee: hermes
status: pending_review
created_at: 2026-08-02
domain: kdo
priority: P2
source: 王语嫣全局元数据扫描（2026-08-02）
updated_at: '2026-08-03T20:00:25.598445+00:00'
---

# #224 全局元数据回填P2：长程渐进（长程任务）

## 任务背景

#219/#222/#223 覆盖了：新卡门禁（#220/#218R6b）、#213存量14张（#219）、高价值卡（#222）、aliases全量（#223）。

本任务收尾**剩余全量**——长程渐进，不设截止：

## 剩余范围

| 字段 | 剩余量 | 说明 |
|:--|:--|:--|
| discoverable_by | ~2200张（2454 - #222高价值层） | cases/concepts/tools等长尾 |
| title | ~80张（93 - #222高价值部分） | 长尾 |
| tags 5维 | ~130张（136 - #222部分） | 长尾 |

**执行方式**：
- 长程任务（P3级节奏），按目录渐进（如每周1-2个目录）
- 优先顺序：concepts → cases → tools → dark-knowledges → 其余
- 每批：dry-run预览 + 声明范围 + 非空不覆盖

## 📋 分批规则（2026-08-04 王语嫣明确；2026-08-04 欧阳锋升级为 100 张/批 + 熔断）

**每批 100 张**（2026-08-04 用户确认升级——前 17 批零破坏，纪律已验证）：
- **批次定义**：每批 ≤100 张卡（按目录内顺序取）
- **批次流程**：取100张 → dry-run预览 → 写入 → yaml.safe_load验证 → 更新任务单进度 → 提报pending_review
- **每批独立提报**：欧阳锋审查通过后，下一批才开始（不积压多批）
- **进度记录**：任务单维护"已批次数/剩余量"（当前：concepts 477 + cases 430 + tools 149 = 1056/2229，47%）
- **升级理由**：#222事故本质是"追加块模式+并行重叠"非批次大小；17批零破坏证明纪律（dry-run+结构自检）是防破坏关键；批次数减半提速
- **🛑 熔断条件**：某批出现 >0 破坏（YAML失败/双键）→ 立即降回 50 张/批，连续 2 批零破坏后才恢复 100
- 特殊情况（单目录>100张）：分批处理，同一目录可跨多批

### 🆕 后续批次计划（2026-08-04 王语嫣补充——欧阳锋修正定性：18张英文title卡优先）

**欧阳锋O3更精确的定性（修正王语嫣初判）**：concepts剩余18张不是"无title"，是**英文title卡**（Business Analysis/Graph RAG/Meta Prompt Eng等）——YAML健康（0失败），非#229编码损坏。disc补了也搜不到（中文搜索命中不了英文title），**必须先中文化title再补disc**。

**优先批次调整**：
1. **下一批（第2批）优先：concepts 18张英文title卡**——title中文化（从正文/ID语义推断中文名）+ 一并补disc
   - 目标：concepts disc覆盖 96.4% → 100%
   - 中文化规则：从卡片正文首段/ID语义推断，参照同名中文卡格式
2. 之后按欧阳锋结论推进：cases → tools → dark-knowledges → 其余
3. 剩余~80张英文title（全库范围）在各目录批次中**先中文化title后disc**（同一张卡一次补全，避免二次往返）

**验收**：第2批完成后 concepts disc覆盖 = 501/501（100%）

## 验收标准

1. 长程推进，每批完成后更新本任务单进度
2. 全库 discoverable_by 覆盖率月度目标：93.2% → 70% → 50%
3. 不修改正文内容，只动 frontmatter

## 边界

- **长程任务**：与#207（存量卡质量债务渐进清理）同类节奏，可并入或并行
- 不追求一次性清零——C-10教训：批量修改破坏半径大
- 优先保证#219/#222/#223完成后才开始本任务

## 🆕 并行冲突防呆（2026-08-04 王语嫣补充——#229同批执行）

**⚠️ 与#229（17张frontmatter重建，黄药师——王语嫣2026-08-04全库实测确认17张）存在cases/目录重叠**——case-yihang×10 + case-truman-aesthetic在cases/，当前YAML失败（10/10）。#229完整清单（实测17张）：case-yihang×10 + case-truman-aesthetic + framework-strategy-brm + framework-yitang-project-abcd + framework-yitang-project-breakdown + tool-clinic + tool-smart + tool-Truman-Feature。**注：dk-yi-tang已由hermes修复（不在清单）、plan_20260531_data-curator已处理（不在清单）**。

**hermes执行#224时必须**：
1. **跳过YAML解析失败的卡**（19张：#229清单）——只处理YAML健康的卡
2. 判断方法：`yaml.safe_load(frontmatter)` 失败 → 跳过并记录，不写入
3. **禁止**对YAML失败卡做任何写入（discoverable_by/title/tags）——那是#229的重建范围
4. 若#224处理到#229清单内的卡：跳过，在任务单记录"已跳过（#229重建中）"

**为什么**：避免#222/#223事故重演（两个任务并行写同一批文件）。#224管YAML健康卡，#229管YAML损坏卡——**按"卡的健康状态"划分，不是按目录**。

---

## ✅ 欧阳锋首批审查记录（2026-08-04）—— **verdict: PASS（第一批）**

> hermes 提交第一批（concepts 50 张：44 成功 + 4 已有 + 2 无标题跳过）。O3 独立验证——**结构健康优先**（#222 教训）。

### O3 验证结果

| 验证项 | 结果 |
|:--|:--|
| **concepts 结构健康** | ✅ YAML 失败 0 / 双 aliases 0——本次批量操作无破坏（#222 教训落实）|
| disc 覆盖 | ✅ 53/495 有 disc（44 新增 + 9 已有）——首批完成，长程继续 |
| disc 质量抽查（5 张）| ✅ 全部真实中文搜索词（协作冲突/规则失效/AI落地场景识别等），无占位符/id 复制 |
| 2 张无标题跳过 | ✅ 合理——#224 title 补全在后续批次，无 title 卡 disc 补了也搜不到 |

### 结论

- **首批 PASS**——hermes 可继续下一批（concepts 剩余 ~440 张 + 其他目录长尾）
- 执行纪律确认：**只写 YAML 健康卡**（#229 清单跳过）、dry-run 前置、批内结构自检（yaml.safe_load + 双键检查）

### 审查可追溯性

methodology v2.1；verdict pass（首批）；blocking [🔴0, 🟡0]；residual_risks [无新增——长程任务按批推进]

---

## ✅ 欧阳锋本阶段审查记录（2026-08-04，10 批次完成）—— **verdict: PASS（concepts 阶段）**

> hermes 提交本阶段（10 批次，concepts 全量）。O3 独立验证——结构健康 + 覆盖率 + 剩余定性。

### O3 验证结果

| 验证项 | 结果 |
|:--|:--|
| **结构健康** | ✅ concepts 495 张：**0 YAML 失败 / 0 双 aliases**——10 批次零破坏（#222 教训持续落实）|
| disc 覆盖率 | ✅ **96.4%**（477/495 有 disc；hermes 报 477/501，文件数口径差 6 张，实质一致）|
| 剩余 18 张定性 | ✅ 英文 title 卡（Business Analysis/Graph RAG/Meta Prompt Eng 等）+ 历史遗留长尾——**非 #229 编码损坏**（concepts 0 YAML 失败）|
| 与 #229 边界 | ✅ concepts 无 #229 清单卡（#229 的 14 张在 cases/tools/dk）|

### 结论

- **concepts 阶段 PASS**——hermes 可进入下一目录（cases → tools → dark-knowledges → 其余）
- 剩余 18 张英文 title 卡：后续批次补（title 中文化 + disc 一并补）
- 月度目标节奏确认：concepts 96.4% > 70% 中间目标 ✅

### 审查可追溯性

methodology v2.1；verdict pass（concepts 阶段）；blocking [🔴0, 🟡0]；residual_risks [18 张英文 title 长尾待后续批次；~2150 张其他目录长程推进]

---

## ✅ 欧阳锋 cases 阶段审查记录（2026-08-04）—— **verdict: PASS（cases 阶段）**

> hermes 提交 cases 阶段。O3 独立验证——结构与 #229 边界。

### O3 验证结果

| 验证项 | 结果 |
|:--|:--|
| **结构健康** | ✅ cases 443 张：双 aliases 0；**11 张 YAML 失败全部 = #229 预制**（case-yihang×10 + case-truman-aesthetic），#224 零新增破坏 |
| disc 覆盖 | ✅ **99.5%**（441 健康卡中 439 有 disc；缺 2 = case-一堂-一堂自身转化实践 + index.md 非卡）|
| 与 #229 边界 | ✅ 11 张 #229 清单卡全部跳过，未触碰 |

### 结论

- **cases 阶段 PASS**——hermes 可进入下一目录（tools → dark-knowledges → 其余）
- 剩余 1 张 case 卡缺 disc（case-一堂-一堂自身转化实践）：下一批顺手补
- 长程节奏：concepts 96.4% + cases 99.5%，月度目标稳步推进

### 审查可追溯性

methodology v2.1；verdict pass（cases 阶段）；blocking [🔴0, 🟡0]；residual_risks [1 张 case 卡 disc 待补；#229 11 张 cases 卡重建中（黄药师）]

---

## ✅ 欧阳锋 tools 第一批审查记录（2026-08-04）—— **verdict: PASS**

> hermes 提交 tools 第一批（49 张）。O3 独立验证。

### O3 验证结果

| 验证项 | 结果 |
|:--|:--|
| **结构健康** | ✅ tools 984 张：双 aliases 0；3 张 YAML 失败 = #229 预制（tool-Truman-Feature/tool-clinic/tool-smart），零新增破坏 |
| disc 覆盖 | ✅ 49 张有 disc（7.9%）——第一批完成，tools 剩 935 张（约 19 批）|
| 总进度 | ✅ 956/2229（43%）——concepts 95% + cases 97% + tools 5% |

### 结论

- **tools 第一批 PASS**——hermes 继续 tools 下一批（每批 50 张，独立提报）
- 长程节奏稳定：三目录零破坏

### 审查可追溯性

methodology v2.1；verdict pass（tools 第一批）；blocking [🔴0, 🟡0]；residual_risks [无新增]

---

## ✅ 欧阳锋 tools 第二批审查记录（2026-08-04）—— **verdict: PASS**

> hermes 提交 tools 第二批（50 张）。O3 独立验证。

### O3 验证结果

| 验证项 | 结果 |
|:--|:--|
| **结构健康** | ✅ 双 aliases 0；YAML 失败 3（#229 预制不变）——零新增破坏 |
| disc 覆盖 | ✅ **13.0%**（缺 disc 853，从 7.9% 新增 ~50 张）——第二批完成 |
| 剩余 | tools 剩 ~885 张（约 18 批）|

### 结论

- **tools 第二批 PASS**——hermes 继续第三批（50 张/批独立提报）

### 审查可追溯性

methodology v2.1；verdict pass（tools 第二批）；blocking [🔴0, 🟡0]；residual_risks [无新增]

---

## ✅ 欧阳锋 tools 第三批审查记录（2026-08-04）—— **verdict: PASS**

> hermes 提交 tools 第三批（100-149，49 张，数据已落盘）。O3 独立验证。

### O3 验证结果

| 验证项 | 结果 |
|:--|:--|
| **结构健康** | ✅ 双 aliases 0；YAML 失败 3（#229 预制不变）——零新增破坏 |
| disc 覆盖 | ✅ **18.0%**（13.0% → 18.0%，新增 ~50 张）——第三批完成 |
| 剩余 | tools 剩 ~836 张（约 17 批）|

### 结论

- **tools 第三批 PASS**——已释放队列回 `claimed-hermes`，hermes 继续第四批
- 流程提示：hermes 提报后如队列被标 `pending_review` 无法继续领取，由欧阳锋释放回 claimed-hermes（已执行）

### 审查可追溯性

methodology v2.1；verdict pass（tools 第三批）；blocking [🔴0, 🟡0]；residual_risks [无新增]

---

## 🛑 欧阳锋熔断记录（2026-08-04，dark-knowledges 批）—— **verdict: 条件 PASS + 熔断**

> dark-knowledges 两批 194 张：193 张 disc 正常（覆盖 78.3%），但 **2 张 YAML 破坏**——熔断条件触发。

### 破坏详情（O3 核查）

| 卡 | 破坏模式 | git 7/27 原版 |
|:--|:--|:--|
| dk-ai-entrepreneur-technical-blindspot | 列表项悬空（`- 三维排列组合` 等悬在 ds 块后）| ✅ 健康——**本次引入** |
| dk-modeling-essence-predictive | aliases 列表未闭合就接 `related:` | ✅ 健康——**本次引入** |

> 修改时间 08-04 03:35（本次批次），git 原版健康——**hermes 写入引入，非历史遗留**。

### 熔断处置（按规则执行）

1. **降回 50 张/批**（连续 2 批零破坏后恢复 100）
2. **2 张卡修复**（hermes）：把悬空列表项合并回正确块（ds/aliases），`yaml.safe_load` 通过后验证
3. 其余 193 张 PASS（覆盖 78.3%）——不因 2 张否决整批，但熔断必须执行

### 审查可追溯性

methodology v2.1；verdict 条件 PASS + 熔断；blocking [🟡2：本次引入 YAML 破坏]；residual_risks [2 张待修复；批次降回 50]

---

## 🏁 欧阳锋终审记录（2026-08-04，#224 全量提报）—— **verdict: 条件 PASS（任务主体完成）+ 1 张新破坏待修**

### O3 终验（5 目录 2223 张）

| 目录 | 覆盖 | YAML 失败 | 说明 |
|:--|:--|:--|:--|
| concepts | 96.4% | 0 | 缺 18 英文 title 长尾（已知）|
| cases | 99.5% | 11（#229 预制）| 缺 2 |
| tools | 99.5% | 3（#229 预制）| 缺 5 |
| dark-knowledges | 99.6% | **1（本次新引入）** | 缺 1 |
| dk | **100.0%** | 0 | ✅ |
| **合计** | **98.8%** | **15**（14 预制 + 1 新）| 缺 26 |

### ⚠️ 同类破坏第 3 次——根因升级

**`dk-yi-tang-wishful-thinking-kills-startups`**（修改 03:43，git 原版健康）：ds 块后直接接 `tags:`（块未闭合）——**与前 2 张完全同模式**。

**结论：不是偶发，是 hermes 写入模板的系统性缺陷**——写入逻辑在 ds 块后追加字段时未正确闭合块。**必须修模板，不是修单卡**。熔断继续（50 张/批），且模板修复前不得恢复 100 张/批。

### 处置

1. **hermes 修复 1 张**（dk-yi-tang-wishful-thinking-kills-startups）+ **定位写入模板 bug**（ds 后追加字段 → 块悬空），修复模板后自测 3 张验证
2. 熔断维持 50 张/批
3. 剩余收尾：#229 **17 张重建**（黄药师，14张#223范围+3张#222范围）+ concepts 18 英文 title + 各目录零星缺 disc（26 张）——作为 #224 收尾清单

### 审查可追溯性

methodology v2.1；verdict 条件 PASS；blocking [🟡1：同类破坏第 3 次（模板缺陷）]；residual_risks [1 张待修；模板待修；26 张缺 disc 收尾]

---

## 🔍 王语嫣核查异议的独立复核（2026-08-04 欧阳锋 O3 重验）—— **原判断维持**

> 王语嫣独立核查提出异议（"dk-yi-tang 7/27 就坏=历史遗留；模板缺陷证据不足"）。O3 严格重验（git show 字节级 + UTF-8 严格解码 + yaml.safe_load）——**异议不成立，原判断维持**。

### 严格重验结果（3 张卡 git 16b64db39 原版）

| 卡 | git show | 7/27 原版 |
|:--|:--|:--|
| dk-yi-tang-wishful-thinking-kills-startups | 6587 字节 | ✅ **可解析（健康）** |
| dk-ai-entrepreneur-technical-blindspot | 7639 字节 | ✅ 可解析（健康）|
| dk-modeling-essence-predictive | 9792 字节 | ✅ 可解析（健康）|

### 决定性证据链（谁引入破坏）

1. **#223 审查（08-04 早）**：O3 验证 dark-knowledges **255 张 YAML 失败 0**——此时 3 张卡全健康
2. **#224 dark-knowledges 批（08-04 03:35-03:43）后**：2 张失败 → hermes 修复 2 张 → 最后一批又 1 张失败
3. 结论：**破坏是 hermes #224 批引入**（#223 审查时 0 失败 → #224 批后失败），**非历史遗留**

### 对王语嫣异议的逐条回应

| 异议 | 复核结论 |
|:--|:--|
| "dk-yi-tang 7/27 就坏" | ❌ 严格重验 7/27 原版可解析——异议方法可能有误（git 路径/提交/解码差异）|
| "模板缺陷证据不足" | ❌ 证据链完整：#223 时 0 失败 → hermes 批后失败，同类模式第 3 次 |
| "真实破坏仅 1 张（历史遗留）" | ❌ 3 张均本次引入（其中 2 张 hermes 已修复，1 张待修）|

### 处置维持

1. **熔断维持 50 张/批**（模板修复前不恢复 100）
2. **hermes 修 1 张**（dk-yi-tang）+ **定位写入模板 bug**（ds 块后追加字段 → 块未闭合）
3. 感谢王语嫣核查——独立验证精神正确，本次异议方法有误；双方都应以"严格 git 字节验证 + 时间线证据链"为准

### 审查可追溯性

methodology v2.1；verdict 维持条件 PASS；blocking [🟡1：模板缺陷第 3 次]；residual_risks [1 张待修；模板待修]

---

## 🏁 欧阳锋最终验收（2026-08-04，#224 收尾终态）—— **verdict: PASS（主任务完成）**

### O3 终验（与 hermes 报告一致）

| 目录 | 覆盖 | YAML 失败 | 备注 |
|:--|:--|:--|:--|
| concepts | 96.4% | 0 | 缺 18（英文 title 长尾）|
| cases | 99.5% | 11（#229 预制）| 缺 2 |
| tools | 99.5% | 3（#229 预制）| 缺 5 |
| dark-knowledges | 99.6% | **0（修复批后清零）** | 缺 1 |
| dk | **100.0%** | 0 | ✅ |
| **合计 2223** | **98.8%** | **14（全部 #229 预制）** | 缺 26 |

### 验收结论

- ✅ **#224 主任务 PASS**：5 目录 discoverable_by 回填完成（98.8%），hermes 零新增破坏（修复批后 dark-knowledges 清零）
- ✅ 熔断闭环：触发（3 张破坏）→ 修复（3 张全修）+ 模板定位 → dark-knowledges 255 张 0 失败
- ✅ dk 100% 完成

### 收尾清单（独立跟踪）

| 项 | 归属 | 状态 |
|:--|:--|:--|
| **#229 17 张 frontmatter 重建**（O3 全库实测 2026-08-04：cases 11[case-yihang×10+case-truman] + frameworks 3[strategy-brm/abcd/breakdown] + tools 3[Truman-Feature/clinic/smart]；dk-yi-tang 已由 hermes 修复✅、plan_20260531 已归档✅）| 黄药师 | 等 #224 完成后解禁 |
| concepts 18 张英文 title（中文化 + disc）| hermes/后续 | 长尾 |
| 零星缺 disc 26 张（cases 2 + tools 5 + dark-knowledges 1 + concepts 18）| hermes/后续 | 长尾 |

### 审查可追溯性

methodology v2.1；verdict pass（主任务完成）；blocking [🔴0, 🟡0]；residual_risks [收尾 3 项独立跟踪]

---

## 🔍 王语嫣核查修正记录（2026-08-04）——撤回异议，欧阳锋判断成立

> **王语嫣对欧阳锋"模板缺陷"判断的异议已被O3严格重验推翻，正式撤回。**

**欧阳锋O3严格重验（字节级 + UTF-8严格解码 + yaml.safe_load）**：

| 卡 | 7/27原版（严格验证） | 结论 |
|:--|:--|:--|
| dk-yi-tang-wishful-thinking-kills-startups | ✅ **可解析（6587字节）** | hermes #224批引入 |
| dk-ai-entrepreneur-technical-blindspot | ✅ 可解析（7639字节） | hermes #224批引入 |
| dk-modeling-essence-predictive | ✅ 可解析（9792字节） | hermes #224批引入 |

**决定性时间线证据**：
```
#223审查（08-04早）：dark-knowledges 255张 YAML失败0 ← 3张当时全健康
→ #224 dark-knowledges批（03:35-03:43）写入后：出现失败
→ 破坏是hermes #224批引入——非历史遗留
```

**王语嫣错误根因**：初判用了`errors='replace'`宽容解码+frontmatter边界误匹配——把当前文件的损坏读成"7/27即坏"。**教训（已记停车场 O-11）**：跨实例事实分歧=双方各自跑严格git字节验证，以字节证据为准。协议详见 `60_feedback/tasks/O11-cross-instance-dispute-protocol.md`。

**修正结论（撤回后）**：
1. ✅ 欧阳锋判断成立——3张均hermes引入，模板缺陷属实（同类第3次）
2. dk-yi-tang **不归#229**（#229清单已撤回18→17张），归hermes修复
3. 熔断维持50张/批 + hermes修1张+定位模板bug
