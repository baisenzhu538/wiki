---
id: task_20260816_wangyuyan-snapshot-migration-pilot
assignee: wangyuyan
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-16
priority: P2
wsjf: 3.0
created_at: 2026-08-16
updated_at: 2026-08-16
source: #326 终审 PASS A（2026-08-16 欧阳锋）→ P3 立项输入就绪
related: #326 #324 #320 #321
---

# P3 快照迁移试点：销售对话助理（#327）

## 背景

#324 诊断确认：快照型 agent（编译产物）是知识传导的**最后一个静态依赖**——P3 目标 = 消灭它。机制已就绪（#325 MCP 全挂 + #326 单一真相源/digest 门禁/巡检），现在把快照 agent 迁移到"检索+引用"模式。**试点：销售对话助理**（最典型的快照型：7-04 编译、CLAUDE.md 写死 5 卡路径、8-16 已加"先 kdo query"指令）。

## 任务

1. **重编译工作手册**：`.agent/prompts/sales-dialogue-assistant.md`——域层纳入 #320 新卡（AI 销售协同/销售漏斗全貌/异议处理）+ 销售域 digest 导航（#321），frontmatter `compiled_at` 更新，源卡版本记录
2. **CLAUDE.md 路径表升级**：5 张写死卡路径 → digest 导航（"先 kdo query → 查 digest → 路径表兜底"），保留兜底不删
3. **试点验证**：真实销售问题（如"客户说太贵怎么回"）→ 验证检索优先命中 #320 新卡（协议级）
4. **迁移模式沉淀**：试点经验（重编译流程/导航升级/验证方法）→ 输出迁移模式，供推广（AI 基本功教练 + 其余快照 agent）

## 依赖

- #320 reviewed ✅（新卡素材——进行中，hermes 生产）
- #321 销售域 digest（#320 配套，纳入导航）
- #326 reviewed ✅（机制就位）

## 验收标准

- 重编译落盘（compiled_at + 源卡版本）+ CLAUDE.md 导航升级
- 试点验证：真实问题检索命中新卡（非旧快照内容）
- 迁移模式文档落盘（供 P3 推广）

## 边界

- 单角色单任务（E026）：王语嫣执行（编译产物为编排侧维护），欧阳锋终审
- 不动快照 agent 之外的部署（Hermes profile/服务不动）
- 推广阶段另立项（本任务只试点 + 沉淀模式）

---

## 执行报告（2026-08-16 王语嫣）

### 1. 重编译落盘 ✅
`.agent/prompts/sales-dialogue-assistant.md`：compiled_at 7-04 → **2026-08-16**；source_hash 纳入 #320 五张新卡；域层新增「检索优先」节（先 kdo query 再路径表）+「增量知识」节（AI 销售协同双条件/形容词禁忌/漏斗全貌/异议处理承认→稀释→转化/痛点库·大单小单·客户讨厌AI 三 dk）——首轮即用防检索失败；保留 OPC 原工作流为底座；estimated_tokens 3500→4500

### 2. CLAUDE.md 路径表升级 ✅
`agents/sales-dialogue-assistant/CLAUDE.md`：新增 4 行（AI 销售协同/漏斗全貌/异议处理/新 dk）+ 检索优先声明；原 5 卡路径表保留为兜底

### 3. 试点验证 ✅（真实问题 → 新卡命中）
- 先发现 **E028 复发**：新卡不在检索索引（8-16 终审后未索引）——搜"异议处理"命中旧 OPC spec 而非新卡
- 排查发现 **KDO 源码 bug**：`kdo index --rebuild` 提前 return 0，**跳过 search_index.json 重建**（只重建 index.md/backlinks）——#325/#326 文档 Step 4 写的命令用法错误（friction-log 已记录，待黄药师修源码/文档）
- 用 `kdo index`（无 --rebuild）重建：doc_count 3894→3904，5/5 新卡 IN
- 真实问题检索：①"客户说太贵了怎么回应"→ tool-sales-objection-dilution 命中 ②"AI销售协同"→ framework-ai-sales-collaboration + sales-funnel-full 命中 ③"销售漏斗 复购"→ framework-sales-funnel-full 第 1 位 ✅

### 4. 迁移模式沉淀（供推广）
**快照 agent 迁移三步**：
1. 重编译 prompts（compiled_at 更新 + source_hash 纳新卡 + 增量知识内嵌节——首轮即用）
2. CLAUDE.md 加"检索优先"声明 + 路径表补新卡（原表兜底）
3. 验证闭环：真实问题 kdo query 命中新卡（**注意用 `kdo index` 重建索引，不是 `kdo index --rebuild`**）

### 验收对照
| 验收标准 | 结果 |
|:--|:--|
| 重编译落盘（compiled_at + 源卡版本） | ✅ |
| CLAUDE.md 导航升级 | ✅ |
| 试点验证：真实问题检索命中新卡 | ✅（3 问全命中，附 E028 修复） |
| 迁移模式文档 | ✅（本报告 §4） |

### 遗留
- KDO 源码 cmd_index 行为修正（friction-log 已记，建议黄药师评估：--rebuild 应包含 search_index 或改名）
- #263 Step 4 文档命令修正（`kdo index --rebuild` → `kdo index`）

## 终审记录（2026-08-16 欧阳锋）

**verdict: PASS A- · methodology v2.3**

O3 独立验证（全部字节级重跑）：
1. **KDO 源码 bug 源码级确认**：`search_index.py cmd_index` L234-241——`--rebuild` 分支只调 auto_update_index 重建 30_wiki/index.md 后提前 `return 0`，**search_index.json 不重建**。cli.py L806 help 也证实（"--rebuild Rebuild 30_wiki/index.md and backlinks"）。**王语嫣发现属实，且 #325/#326 文档 Step 4 命令用法确实错误**
2. **索引修复实证**：协议级 kdo_search 3 真实问题全命中新卡（异议处理→tool-sales-objection-dilution / AI销售协同→framework-ai-sales-collaboration+funnel-full / 漏斗复购→funnel-full）
3. **重编译落盘**：compiled_at 8-16 + source_hash + 检索优先节（L66）+ 增量知识节（L78）首轮即用
4. **CLAUDE.md 导航升级**：检索优先声明 + 4 行新卡路径，原 5 卡兜底保留
5. **迁移模式沉淀**：三步走含"kdo index 非 --rebuild"陷阱标注

**遗留两项裁定**：
- ① **KDO 源码 cmd_index 修正**：✅ 批准立项（黄药师）——`--rebuild` 应重建 search_index.json（语义与直觉对齐）或改名 `--rebuild-nav`。**P0 级**：当前所有文档/脚本的 `kdo index --rebuild` 都是错的，索引失效是静默的
- ② **#263 Step 4 文档命令修正**：✅ 批准——`kdo index --rebuild` → `kdo index`（已实测正确命令），黄药师改文档时一并做

**等级 A-**（试点 + 抓真 bug + 模式沉淀完整；扣半档原因：E028 复发说明 #326 Step 4 首次执行即漏——机制写对但执行没跟上，且文档命令错误是 #325/#326 审查时未捕获的连带问题）

**结论**：PASS A-，P3 快照迁移试点成功，推广模式就绪。

## 编排联动（2026-08-16）

遗留两项（源码 P0 + 文档修正）已批入建议书 `60_feedback/diagnosis/diag_20260816_ouyangfeng-task-orchestration-proposal.md`（#329/#330 建议编号），请王语嫣审核编排入队。
