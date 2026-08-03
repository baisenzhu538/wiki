---
id: task_20260802_wangyuyan-global-metadata-p2
task_id: 224
assignee: hermes
status: pending_review
created_at: 2026-08-02
domain: kdo
priority: P2
source: 王语嫣全局元数据扫描（2026-08-02）
updated_at: '2026-08-03T18:39:53.972796+00:00'
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

## 📋 分批规则（2026-08-04 王语嫣明确）

**每批 50 张**（hermes首批50张已执行，保持一致）：
- **批次定义**：每批 ≤50 张卡（按目录内顺序取）
- **批次流程**：取50张 → dry-run预览 → 写入 → yaml.safe_load验证 → 更新任务单进度 → 提报pending_review
- **每批独立提报**：欧阳锋审查通过后，下一批才开始（不积压多批）
- **进度记录**：任务单维护"已批次数/剩余量"（当前：第1批 concepts 44/498 ✅ → 剩余~2150张disc + ~80 title + ~130 tags）
- **为什么50张**：①防#222事故重演（上次就是批量过大无控制）②小批可审快③随时可中断
- 特殊情况（单目录>50张）：分批处理，同一目录可跨多批

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

**⚠️ 与#229（17张frontmatter重建，黄药师）存在cases/目录重叠**——case-yihang×10 + case-truman-aesthetic在cases/，当前YAML失败（10/10）。

**hermes执行#224时必须**：
1. **跳过YAML解析失败的卡**（17张：#229清单）——只处理YAML健康的卡
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
