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
