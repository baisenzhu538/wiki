---
id: 529
assignee: laowantong
status: pending_review
updated_at: '2026-08-25T15:32:53.771561+00:00'
version: v0.1
instance: kimi-cli
code_files:
- 30_wiki/tools/tool-oral-spray-demo-prompts-3samples.md
- 30_wiki/tools/tool-oral-spray-into-doc-not-chatbox.md
- 30_wiki/dark-knowledges/dk-oral-spray-training-vs-task-optimal.md
- 30_wiki/frameworks/framework-oral-spray-cultivation-map.md
- 30_wiki/dark-knowledges/dk-oral-spray-newcomer-blockers.md
- 30_wiki/concepts/concept-oral-spray-multi-agent-parallel.md
---

# #529 口喷全阶指南口述补充生产（示范提示词资产+操作层暗知识）

- **任务号**：#529
- **状态**：queued
- **assignee**：laowantong（W1 逐字读+同构映射；欧阳锋批次验收）
- **优先级**：P2（口喷域收官补强——老朱判定「比以前逐字稿可能有更多暗知识」，诊断属实）
- **立项**：2026-08-25 王语嫣（素材=`00_inbox/AI口喷能力训练全阶指南-口述.txt` 6424 行；诊断结论：~95% 与 Live260 重复，增量=示范提示词原文+操作层暗知识+独家数据）

## ⚠️ 素材风险（开工必读）

- 文件系**两遍 STT 转写首尾拼接**：1–2801 行=A 版，2802 行起 B 版从头重转写（~95% 重复），**B 版独有内容约从 5614 行起**；引用优先 A 版行号，>2802 先去重
- 专名错识别且 A/B 矛盾（「智谱/质谱/搜狗」输入法、「九字诀/九四九/单元模型」、「文生图/文身图」）——**专名一律以 `00_inbox/直播Live260-AI口喷必修课-逐字稿.md` 精编版为准校核**，STT 版只做行号定位

## 任务

**新增 3 张**：
1. `tool-oral-spray-demo-prompts-3samples`：三段即兴示范提示词完整原文（调研类 A264-308／方案类「不要执行先写顶层方案」A378-436／封装类「原文附到最后不要改字」A502-568）——Live260 已删提示词本体，此为全库唯一原文；定位=可抄的教科书级口喷样本
2. `tool-oral-spray-into-doc-not-chatbox`：喷文档里不喷聊天框（A1622-1672，含配套提示词原文「保留在最后附录…不要删」）——L1→L2 两大卡点的同一个操作解，5 张现有卡射程外
3. `dk-oral-spray-training-vs-task-optimal`：喷干净=训练最优≠任务最优（A2716-2726）+500条和5000条没差别=停舒适区（A1094-1098）——目标函数切换的练习方法论

**补强 3 张（追加不覆写）**：
4. `framework-oral-spray-cultivation-map`：L3 主动控场≥50% 可检测线（A2184/A2448）+L4 单轮 5 分钟判定（B5616-5630）+L5 五配套要素（B6066-6082）+独家数据（150 分钟喷 2 万次/均 153 字/191 页 PPT，B6010-6016）
5. `dk-oral-spray-newcomer-blockers`：错别字二分标准（只改无上下文交叉的事实性错误，A1500-1506）+防丢稿四招细节（A1864-1880）
6. `concept-oral-spray-multi-agent-parallel`：00 顶层文档工作法（开局一篇 00 文档喂所有窗口，B5812-5840）+设备贡献度<10%（B6126）

## 边界

- ~95% 重复内容**不重复建卡**——同构映射表先行（贴任务单执行报告），逐条标注「已有卡覆盖/补强/新增」
- P1 卡级：三方法按 P1 口径（6 层交叉必过来源/逻辑两层；9 层深挖过 L4 失败模式）
- 行号引用格式：A 版 `口述.txt:A264`／B 版 `口述.txt:B6010`

## 验收

- 同构映射表+新增 3 张+补强 3 张；专名校核记录（哪些按 Live260 改正）
- pre-submit 通过；欧阳锋批次验收

---

## 执行报告（F-034 五字段 · 2026-08-25 老顽童 kimi-cli）

**文件清单**：新增 3 张（tool-oral-spray-demo-prompts-3samples / tool-oral-spray-into-doc-not-chatbox / dk-oral-spray-training-vs-task-optimal）+ 补强 3 张（framework-oral-spray-cultivation-map / dk-oral-spray-newcomer-blockers / concept-oral-spray-multi-agent-parallel，均追加节不覆写）。

**完成内容**：新增 3 张卡（示范提示词三样本/喷文档不喷聊天框/训练 vs 任务最优 dk）+ 补强 3 张卡（段位判据/错别字二分+防丢稿/00 文档工作法），同构映射表+专名校核记录如下；~95% 重复内容未重复建卡。

**同构映射表**（口述 6424 行 ~95% 与 Live260 重复部分逐条去向）：

| 素材内容 | 处置 | 落点 |
|:--|:--|:--|
| 五大优势/四难/五次飞跃/段位地图/OPT/战略级基本功（A+B 版主体 ~95%） | 已有卡覆盖，不重复建卡 | Live260 卡组（#487 已终审 PASS A） |
| 三段即兴示范提示词原文（A264-308/A378-436/A502-568） | **新增** | tool-oral-spray-demo-prompts-3samples |
| 喷文档不喷聊天框+配套提示词（A1622-1672） | **新增** | tool-oral-spray-into-doc-not-chatbox |
| 喷干净=训练最优≠任务最优（A2716-2726）+500=5000（A1094-1098） | **新增** | dk-oral-spray-training-vs-task-optimal |
| L3 可检测线/L4 五分钟判定/L5 五配套/独家数据（A2184/A2448/B5616-5630/B6066-6082/B6010-6016） | 补强 | framework-oral-spray-cultivation-map（追加节） |
| 错别字二分标准（A1500-1506）+防丢稿四招细节（A1864-1880） | 补强 | dk-oral-spray-newcomer-blockers（追加节） |
| 00 顶层文档工作法（B5812-5840）+设备贡献<10%（B6126） | 补强 | concept-oral-spray-multi-agent-parallel（追加节） |

**专名校核记录**（按 Live260 精编版口径校，STT 仅作行号定位）：Open Cloud→OpenClaw / harmless、C Harness→Hermes / Abacc、SBC→ABACC（SBC 待核已注明）/ 九四九→九字诀 / 智谱·质谱→智谱、搜狗说法→搜狗输入法 / 文身图→文生图 / A 站→Agent / 《麻烦脑》文档名待核未改原文。校注表嵌在 tool-oral-spray-demo-prompts-3samples 卡内。

**诚实标注**：B6014「150 分钟喷两万多次」与「均 153 字」乘积不合理（≈300 万字），按口述原文引用并加注「数字待核」（疑为「两万多字」或「一百三十多次」——130×153≈2 万字自洽）。

**验证**：`kdo index` 重建（4149 docs）→ pre-submit 6 文件 **Passed 6 / Failed 0**（WARNING 为存量级不阻断）；锚点区间逐字精读（A264-568/A1094/A1500-1506/A1622-1672/A1864-1880/A2184/A2448/A2716-2726/B5616-5630/B5812-5840/B6010-6016/B6066-6082/B6124-6128）；feat commit 先行（6 文件 path-scoped）。

**未做项**：无（B 版 >2802 已按任务书先去重，仅取 5614 起 B 独有段）。

**需要谁动作**：欧阳锋批次验收（P1 口径：6 层交叉过来源/逻辑两层——来源=口述原文逐字锚，逻辑=同构映射不重复建卡）。
