---
id: '315'
assignee: huangyaoshi
status: reviewed
claimed_at: 2026-08-13
reviewed_by: 欧阳锋
updated_at: '2026-08-13T11:39:39.057484+00:00'
task_id: '315'
priority: P1
review_date: '2026-08-13'
grade: A-
---

# #315：Feature 周期表 aliases 增强 v0.9（P1，基建 0.25-0.5d）

## 任务目标

解决 Feature 命名不统一——从 Live258 10 案例 + 周期表 v0.8 中提取 20-30 个别名族，补入周期表 JSON 的 aliases 字段，**并让 feature_menu 搜索命中别名**（JSON 字段进检索，否则"不登记=不存在"的检索版半截）。

> 来源：黄药师建议书 #C + 基建迭代洞察 P1-1（2026-08-13 两轮），王语嫣裁定采纳。
> ⚠️ **阻塞关系**：#312/#313 生产前置——case 卡"反向教学"不映射到周期表 F100（反向确认族），溯源链即断。

## 素材清单

- `00_inbox/AI基本功/Live258：AI基本功第一课优秀作业.md`（命名漂移实例）
- `10_raw/sources/feature-periodic-table-v0.8.json`（100 Feature，L2:38/L4:18/L1:14/L3:14/L5:13/L0:3）
- **顺手并入 #255 C4 遗留**：F045/F057/F087 三选一处理（周期表 JSON 层同批操作）

## 已知命名漂移实例（作业中）

| 族 | 同义名 | 周期表现状 |
|:--|:--|:--|
| 反向确认/反向教学 | 反向确认/反向教学/反向教我/反向提示/让 AI 自我复盘 | F100 反向确认（L2）——"反向教学"查不到 |
| Few-shot | Few-shot/参考案例/风格样本/示例教学/好坏样本库 | 周期表 Few-shot 族 |
| 多版本 | 抽卡/多版本输出/分支测试/N 版选 1 | 周期表多版本族 |
| 设定角色 | 设定角色/角色设定/设定身份/专属角色/专业角色 | 周期表角色族 |

## 产出

- `feature-periodic-table-v0.9.json`（aliases 增强版，不破坏 v0.8 已有字段）
- `feature_menu.py` 搜索命中别名（list/query/pick 检索走 aliases）
- 变更说明（新增 aliases 清单 + 原文件备份/版本路径）
- #255 C4 遗留处置（F045/F057/F087 三选一 + 结论）

## 验收标准

1. `kdo query "反向教学"` 命中"反向确认/反向教学"族 Feature（原验收）
2. `feature_menu` 检索（list/query/pick）能命中别名关键词
3. 现有 100 Feature 全部保留，aliases 纯增量不覆盖
4. #255 C4 三选一处置有结论落盘（处理内容+理由）
5. 登记：cap_hub/README 数据源路径同步（如适用）

## 边界

- 本任务只做 aliases/命名层 + C4 遗留，不做 Feature 内容增删
- DataPack/事实约束类新 Feature 补建（作业暴露缺口）另开任务（王语嫣/欧阳锋裁定后）
