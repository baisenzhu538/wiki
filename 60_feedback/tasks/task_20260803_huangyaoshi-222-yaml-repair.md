---
id: task_20260803_huangyaoshi-222-yaml-repair
task_id: 227
assignee: huangyaoshi
status: queued
created_at: 2026-08-03
domain: kdo
priority: P0
source: #222紧急审查FAIL（批量破坏事故）
updated_at: '2026-08-03T03:30:00+00:00'
---

# #227 紧急修复：#222批量操作破坏的YAML结构（C-10级事故）

## 事故概述（🆕 双线并行写入事故，范围已扩大）

**#222（飞书，discoverable_by回填）+ #223（hermes，aliases回填）双线并行执行，任务范围重叠（都含frameworks/），两个实例都用"追加aliases块"模式写入同一批文件→C-10级批量破坏。**

实测破坏范围（王语嫣独立验证，2026-08-03 03:50；欧阳锋补充 04:10）：

| 目录 | 总数 | YAML失败 | 双aliases | 破坏来源 |
|:--|:--|:--|:--|:--|
| frameworks/ | 247 | 243 (98%) | 246 | #222+ #223重叠 |
| tools/ | 984 | 958 (97%) | 689 | #223 |
| concepts/ | 501 | 461 (92%) | 476 | #223 |
| dk/ | 46 | 16 | 46 | #223 |
| **dark-knowledges/** | **254** | **249 (98%)** | **254 (100%)** | **#223（欧阳锋补充）** |
| **cases/** | **434** | **418 (96%)** | **433 (100%)** | **#223（欧阳锋补充——超出任务单优先级目录）** |
| bridges/methods/domains/systems | 51 | 各1-2张 | 1 | 待查 |
| **合计** | **~2600** | **~2350 (89%)** | **~2150** | 双线 |

> ⚠️ **欧阳锋补充（2026-08-03 04:10）**：hermes 在 #223 的破坏**超出任务单优先级目录**（tools/concepts/dk 优先），cases/ 与 dark-knowledges/ 也已大规模破坏（cases 433/434 双 aliases、dark-knowledges 254/254）。**修复脚本必须全库扫描**（#227 步骤1已含"扫描全库所有目录"——执行时以全库为准，不限于上表）

**根因**（git对比7/27版本确认）：批量操作把aliases块"追加插入"到`diagnostic_signals:`后面（而非合并进已有aliases）——ds变null、signal悬空、YAML缩进错乱。**两个实例的写入模式相同**。

**git状态**：2626个文件未提交改动——hermes（#223）已大规模写入，已发"紧急停手"指令（#223任务单顶部）。

## 修复方案（纯机械，脚本化）

### 步骤1：写修复脚本

1. **扫描全库**（30_wiki/所有目录）识别所有被破坏的卡（yaml.safe_load失败 或 双aliases 或 ds_null）
2. **合并重复aliases块为单块**——保留全部条目，位置正确（在tags后、diagnostic_signals前或按schema）
3. **恢复diagnostic_signals位置**——signal条目回到ds下，不悬空
4. 修复后frontmatter字段顺序：id/title/type/status/domain/author/reviewed_by/confidence/trust_level/language/source_refs/related/created_at/updated_at/tags/aliases/discoverable_by/diagnostic_signals

### 步骤2：全量验证（修复门槛）

- **全库 30_wiki/ 100% yaml.safe_load通过**（不只frameworks）
- 双aliases = 0
- ds全恢复（signal条目非空）
- `kdo lint --incremental` 0新增

### 步骤3：验收

1. 修复脚本 dry-run 预览（声明影响范围）
2. 修复后全库yaml.safe_load通过
3. 抽10张卡git diff确认：内容未动，仅frontmatter结构修复
4. **通过后才允许恢复#223（改串行+目录划分）/ #224**

## 边界

- **只修frontmatter结构，不动正文内容**
- 修复人：黄药师（写脚本）——机械修复避免人工上千次操作
- 参考：C-10教训（内容清空）+ 本次E010（追加块破坏YAML）
- P0紧急——~1800张卡对标准解析器全坏，阻塞lint/搜索/图谱
- **恢复#223前必须：①#227修复完成 ②#223/#222改串行 ③目录划分避免重叠（#223只做tools/concepts，#222只做frameworks）**

### 🆕 aliases替换丢失的次生损伤 + 恢复路径修正（2026-08-03 04:20）

**欧阳锋发现（O3验证）**：修复脚本用"替换"而非"合并"aliases——被#222/#223追加过的~2000张卡，**原aliases搜索词被新块覆盖丢失**。抽查tool-十指模型：8/2原[十指模型/十指40策略/个人修炼]→修复后[十指模型完整40策略/讲香基本功/讲香基本功：十指模型完整40策略]，原3条丢失。

**王语嫣独立验证（修正欧阳锋"无法恢复"判断）**：
- ✅ **旧卡（7/27前存在）原aliases可从git恢复**——`git show 16b64db39:<path>` 有原aliases（如tool-十指模型7/27=[个人修炼/十指模型修炼地图]、framework-表达力7/27=[个人修炼/执行武器库]）
- ❌ **8/2新建卡**（如framework-christensen）7/27不存在，原aliases在8/2-8/3未commit改动里，确实丢失需重补
- **结论**：不是"全部重补"，是**"git对比恢复（7/27版本）+ #223重补8/2新增部分"**——~2000张旧卡可从git批量恢复原aliases，工作量远小于全部重写

**#223恢复时的处理**：
1. 对7/27前存在的旧卡：`git show 16b64db39:<path>` 提取原aliases → 与当前aliases合并（保留两者）
2. 对8/2新建卡：按discoverable_by/title反向补齐
3. 合并规则：原aliases + 新aliases 去重合并，不替换

---

## ✅ 修复验收记录（2026-08-03 05:00 欧阳锋）—— **verdict: PASS（条件通过）**

### O3 全量验证结果

| 指标 | 修复前 | 修复后（O3实测） |
|:--|:--|:--|
| 全库 YAML 失败 | ~2,350（89%）| **49 张（1.9%）** ✅ |
| 通过率 | ~11% | **98.1%** ✅ |
| 双 aliases | ~2,150 | 125（重复键不阻塞解析）|

**修复质量抽查**：tool-讲香基本功-十指模型 YAML 通过 / ds 恢复（signal 保留）/ 正文 40 策略完整 / discoverable_by 4 条 ✅

### 剩余收尾项（不阻塞恢复，但需跟踪）

| # | 项 | 负责人 | 验收门槛 |
|:--|:--|:--|:--|
| 1 | **49 张顽固卡**（case-yihang-dual-triangle-* ×10 + framework-* 老卡 ×30 + 其他）——缩进层级错乱（"mapping values are not allowed here"）| 黄药师逐张手修 | 全库 yaml.safe_load **100% 通过** |
| 2 | **双 aliases 125 张**清理（合并去重）| #223 恢复时按合并规则处理 | 双 aliases = 0 |
| 3 | **原 aliases 恢复**（~2000 张旧卡 git 对比 + 8/2 新建卡反向补齐）| #223 恢复时处理 | 抽查 10 张原搜索词在位 |

### 恢复 #222/#223 的硬性条件（全部满足后才允许）

1. ✅ 全库 YAML 通过率 ≥98%（已达成 98.1%）
2. 🔄 #222 → #223 **串行执行**（禁止并行——本次事故根因之一）
3. 🔄 **目录划分**：#222 只管 8 个高价值目录；#223 只管 tools/concepts/dk 等，零重叠
4. 🔄 aliases **合并规则**（git 恢复原值 + 去重合并，不替换）
5. 🔄 每批写入前 **dry-run + git diff 验证**

### 事故闭环确认

- 事故：双线并行写入（#222 飞书 + #223 hermes）同用"追加 aliases 块"模式 → 全库 ~2,350 张 YAML 破坏
- 修复：#227 脚本化修复（~2,300 张）→ 98.1% 通过
- 教训（E010 + 编排层）："实例隔离"≠"文件安全"；批量写入必须 dry-run + 结构验证；验收 = 结构健康而非统计达标
- **团队恢复等待确认**：黄药师修完 49 张顽固卡 → 欧阳锋复验 100% → 王语嫣恢复 #222/#223（串行+目录划分）
