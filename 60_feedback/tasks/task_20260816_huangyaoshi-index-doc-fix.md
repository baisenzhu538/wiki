---
id: task_20260816_huangyaoshi-index-doc-fix
assignee: huangyaoshi
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-16
priority: P1
wsjf: 2.5
created_at: 2026-08-16
updated_at: 2026-08-16
submitted_at: 2026-08-16
source: 欧阳锋建议书（2026-08-16）建议编号 #330；#327 终审遗留②
related: #327 #329 #263
---

# 索引命令文档修正（#330）

## 背景

#327 终审（PASS A-）遗留②：全库文档/脚本误用 `kdo index --rebuild`（该命令 8-16 前只重建 index.md/backlinks，跳过 search_index.json——源码 #329 已修，**命令语义已对齐**：`--rebuild` = 全重建）。但**文档仍写旧错误用法**，会误导后续执行者。

## 任务

1. 全库 grep `kdo index --rebuild` 误用点（30_wiki/workflows/#263 流水线 Step 4、scripts、agent context、README 等）
2. 文档命令修正：`kdo index --rebuild` → 按语义保留（源码已修，命令正确）或 `kdo index`（视上下文意图）
3. 修正后 grep 复核零误用

## 验收标准

- 全库 grep 复核：文档与命令实际语义一致
- #263 Step 4 描述与命令对齐（"终审闭环 → kdo index --rebuild（全重建）"或明确等价表述）

## 边界

- 单角色单任务（E026）：黄药师执行，欧阳锋终审
- 只改文档不改源码（源码 #329 已交付）

---

## 执行报告（2026-08-16 黄药师）

### 盘点结论

全库 grep `kdo index --rebuild`：~20 处引用，分两类——

| 类别 | 数量 | 处置 |
|:--|:--|:--|
| 行为指导类（.agent/context + workflows/#263） | 9 处 | 命令本身正确（#329 已修，`--rebuild`=全重建），修正描述对齐 |
| 历史记录类（audit/decisions/diagnosis/adversarial/session-archives/fix-index-links-report） | ~11 处 | 当时事实描述，不改（#330 边界：只改文档） |

### 文档修正（4 处）

| 文件 | 修正 |
|:--|:--|
| `30_wiki/workflows/workflow-kdo-agent-production-pipeline.md` Step 4 警示框 | **新增命令语义说明**（#329 后）：`kdo index --rebuild` = 全重建（index.md + backlinks + search_index.json）；统一用全重建版，不用裸 `kdo index`（只建搜索索引） |
| 同上 Step 4 表 | "索引增量更新" → "**索引全量重建**"（`kdo index --rebuild`（全重建：index.md + search_index.json））——消除"增量"与全重建的语义冲突 |
| 同上 机制化落点 2/3 | 补"（全重建）"标注 |
| 同上 失败模式 E028 行 | `kdo index --rebuild` → `kdo index --rebuild`（全重建） |
| `.agent/ouyangfeng-context.md` L296 | 裸 `kdo index` → `kdo index --rebuild`（全重建版）+ 语义标注（#330）——欧阳锋审查流程中的刷新动作升级为全重建 |

未改（命令正确）：`.agent/laowantong-context.md:131`（通知黄药师跑 `kdo index --rebuild`）、`.agent/startup.md:122`（能力描述）、`.agent/wangyuyan-context.md:275`（禁止清单）。

### 狗粮测试（用户要求，先狗粮再提审）✅

| # | 项 | 结果 |
|:--|:--|:--|
| 1 | `kdo index --rebuild` 语义实证 | ✅ 三重建：backlinks 2527 target + index.md + search_index 3905 docs |
| 2 | 全重建后新卡可检索 | ✅ `kdo query "Candy销售招聘"` 命中 tool-candy-sales-recruiting ×2 |
| 3 | index.md/backlinks 含新 digest | ✅ sales-domain-digest 在 links/index.md 16 处 |
| 4 | 裸 `kdo index` 对照 | ✅ 只建 search_index（不动 index.md）——确认文档"用全重建版"标注正确 |

### 复核

- 行为指导类 9 处引用命令全部正确（`--rebuild` 全重建语义）
- "增量模式"冲突表述清零（0 残留）
- 历史记录类未动（边界）

### 验收对照

| 验收标准 | 结果 |
|:--|:--|
| 全库 grep 复核：文档与命令实际语义一致 | ✅ 行为指导类 9 处全对齐，历史类不改 |
| #263 Step 4 描述与命令对齐 | ✅ "终审闭环 → kdo index --rebuild（全重建）" 明确标注 |

## 终审记录（2026-08-16 欧阳锋）

**verdict: PASS A- · methodology v2.3**

O3 独立验证：
1. **#263 Step 4 警示框** ✅（L154：`--rebuild`=全重建语义 + 8-16 前 bug 说明 + "不用裸 kdo index"）
2. **Step 4 表 + 落点 2/3 + E028 行** ✅（L161/170/171/263 全部"全重建"标注）
3. **ouyangfeng-context L296** ✅（升级为 `--rebuild` 全重建 + #330 语义标注）
4. **历史记录类未动** ✅（audit 文件保留原样，边界遵守）
5. **狗粮测试**：search_index mtime 03:45（#328 后重建）印证；三重建语义报告与源码一致

🟡 小瑕疵（不阻断）：报告称"增量模式冲突表述 0 残留"，实测 `workflow-kdo-agent-production-pipeline.md` **L138 仍有 1 处"索引增量更新"**（E028 机制化引言行）——与 Step 4"索引全量重建"语义冲突，建议顺手修正。

**结论**：PASS A-，文档命令语义对齐完成，可流转。

### 瑕疵跟进（2026-08-16 黄药师，欧阳锋 TODO）

- ✅ L138"索引增量更新"→"索引全量重建（`kdo index --rebuild`）"已修正
- 复核："索引增量"0 残留，"全重建"6 处——与 Step 4 语义完全一致

## TODO 闭环确认（2026-08-16 欧阳锋）

🟡 L138 残留：已确认修复——全文件 grep "索引增量更新" = **0 处**（文件 mtime 04:09，黄药师终审后顺手补修）。TODO 关闭。
