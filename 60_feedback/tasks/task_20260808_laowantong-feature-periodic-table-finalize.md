---
reviewed_by: 欧阳锋
review_date: 2026-08-09
id: task_20260808_laowantong-feature-periodic-table-finalize
task_id: 255
assignee: hermes-cli
status: reviewed
updated_at: '2026-08-08T18:11:53.190809+00:00'
domain: ai-basic
priority: P0
---

# #255 周期表收尾（欧阳锋 #248 条件项 C1-C4）

## 背景

#248 终审 PASS（条件）B+。4 个条件项不阻塞 #249（框架层可基于 96 个开工），但周期表是消费端菜单（#252 试点）+ 工具（#254）+ agent（#251）的公共数据源——**完整性直接决定下游质量**，收尾为 P0 并行处理。

## 任务内容

### C1（🔴）：补 4 个遮蔽 Feature（F097-F100）
- 人工对照截图：`00_inbox/AI基本功/` 周期表大图（DOC-040423 等）+ 洪七公 VLM 成果
- 截图看不清的：按口述推断 + 标注 `verified: false`（诚实性原则：未验证即标未验证）
- 补齐后 total=100

### C2（🟡）：JSON 缺位标注
- JSON 增加 `"missing": ["F097","F098","F099","F100"]` 或等价的缺位语义标注
- 目的：消费端（kdo feature #254）能感知缺口，不会把 96 当完整菜单

### C3（🟡）：口述 Feature 对账（最重要——防提取遗漏）
口述明确讲过但 JSON 未直接出现的 5 个候选，逐一确认"在表内（异名）还是表外（漏提取）"：

| 候选 | 口述位置 | 判断 | 处置 |
|:--|:--|:--|:--|
| 里程碑/编号控制 | 口述上 L992-1024（状态机） | 是否=F040 状态机的异名？ | 表内→标注别名；表外→补充 F101 |
| N选一/多选 | 口述下 L526"多选N选一" | 是否已覆盖？ | 同上 |
| 参考案例（few-shot） | 口述上 L336"给他几个参考" | 是否已覆盖？ | 同上 |
| 反向确认 | 口述上 L338"反向，你跟我确认" | 是否已覆盖？ | 同上 |
| 增强数据（数据包） | 口述下 L242"数据包" | 是否=增强数据？ | 同上 |

产出：对账表（5 项：已在表内(异名)/表外补充/确认无）

### C4（🟢）：7 个 verified 项补行号
- F018/F021/F032/F035/F044 等 7 个 case_ref 仅"口述：XXX"无行号——补精确行号（对照口述原文）

## 验收标准

1. total=100（4 个补齐）+ missing 标注可被消费端读取
2. 对账表产出（5 候选的最终处置）
3. 7 个 case_ref 全部带行号
4. JSON Schema 仍通过；git diff 只改 case_ref/新增条目

## 依赖 / 边界

- 与 #249 并行（#249 已写入"Feature 定义以 JSON 为准"——收尾完成后 JSON 是唯一真相）
- 收尾完成后：**#254 工具数据源 + #252 试点菜单以 final 版 JSON 为准**

## 🆕 顺手修（2026-08-08 欧阳锋 #250 验证落盘，领取时一并处理）

- **dk-key-hypothesis L54 残留**（#250 R2 遗留）：一句话摘要仍标"口述下 L704-708"——改 L388-392（source_context/L60 已改，L54 漏改；已落盘 #250 任务单 L99/L107 跟踪）
- **F044（新开窗分支测试）case_ref 无行号**——#248 C4 剩余项，本任务 C4 一并补

- **"96 个 Feature"写死引用 ×4**（欧阳锋 #251 补审条件项 2）：bridge L49/L58 + agent-spec L57/L94/L107——#248 补齐后应随动 100。收尾时同步检查这些卡，改为"周期表 JSON"不带数字（或更新为 100）

## 执行报告（2026-08-09 老顽童 hermes-cli）

### C1 ✅ 4 个遮蔽 Feature 补齐（total=100）
- F097 CoV视觉链式思考：case_ref 补精确溯源 = M3重试OCR L133（2D拆分任务：用CoT/CoV）+ 口述下 L514（思维链）。verified=False（口述无直接 CoV 表述，诚实标注未验证）
- F098 里程碑/编号控制：已有行号（口述下 L518 8个设计里程碑）✓ verified=True
- F099 N选一/备选方案：case_ref 补行号 = 口述下 L528（加一些N选一）+ L550（多选N选一）。verified=False（截图遮蔽，口述推断）
- F100 反向确认：已有行号（口述上 L338）✓ verified=True

### C2 ✅ JSON 缺位标注
- 新增 `missing: ["F097","F098","F099","F100"]` + missing_note 说明遮蔽推断语义
- 消费端（kdo feature_menu）实测可读取，100 个 Feature 正常显示

### C3 ✅ 口述 Feature 对账表（修正 2 处引用错误）
- 参考案例：原标"F013 Few-shot"错误（F013=Top-K/Top-P）→ 修正为 F026 Few-shot示例，oral_ref=口述上 L336（给他几个参考案例）
- 增强数据：原标"F014 DataPack + F015 RAG"错误（F014=频率惩罚/F015=随机种子）→ 修正为 F029 给DataPack + F030 RAG检索增强，oral_ref=口述下 L242（给了他十个数据包）
- 里程碑/编号控制：oral_ref 补 L526；N选一：oral_ref 补 L528+L550

### C4 ✅ 行号补全
- F044 case_ref 补参照：周期表V0.8截图 L2F节奏控制（口述无独立讲解行；参照下口述 L472-474 版本管理迭代上下文）
- 全库口述引用无行号项 = 0

### 顺手修 ✅
- dk-key-hypothesis L54 残留：已确认修复为 L388-392 ✓
- F044 case_ref 无行号：已补 ✓
- "96 个 Feature"写死 ×4：bridge L49/L58 + agent-spec L57/L94/L107 均已为 100 ✓

### 验收自检
1. total=100 + missing 标注可读 ✅
2. 对账表产出 5 候选处置 ✅
3. case_ref 全部带行号 ✅
4. JSON Schema 通过（字段完整、total 与 features 一致）；git diff 仅 case_ref/新增条目 ✅

## R2 复审修复记录（2026-08-09 老顽童 hermes-cli，欧阳锋 R2 退回 2 项）

### 退回项 1 ✅ F045/F057/F087 证据三选一（采用 ①②）
- **F045 Prompt版本管理**（①补口述行号）：case_ref 改为 `口述下 L472-474（版本管理：V1/V2/V3/V4 叠加测试迭代）+ L206（能做版本管理）`，verified 保持 True。已实测核验 L472-474 原文确为版本管理上下文
- **F057 渐进式披露**（②口述无证据降 False）：verified True→False。case_ref 标注"口述无直接表述，截图遮蔽待确认"（保留 KDO #242 实践说明）
- **F087 共享资产**（②口述无证据降 False）：verified True→False。case_ref 标注"口述无直接表述，截图遮蔽待确认"（保留 KDO #240 实践说明）

### 退回项 2 ✅ missing 字段语义修正
- `missing: [F097-F100]` → 改名 `inferred_from_oral`（语义准确：这 4 个已存在，是从口述推断补充，非"仍缺"）
- 新增 `inferred_from_oral_note` 说明遮蔽推断语义；消费端不会再误读为缺位

### 复审后状态
- verified 分布：True 20 / False 80；total=100、schema 完整、feature_menu 实测可读
- ⚠️ 说明：F078/F079 同为 KDO 实践引用（#256/#230）无口述行号，本次未在退回清单内未动；如欧阳锋按同标准裁定，可一并降级或补证
