# 周期表 v1.0 verified 证据分级 — 变更说明（#317，2026-08-13）

> 任务：`60_feedback/tasks/task_20260813_huangyaoshi-feature-verified-grading.md`（#317）
> 背景：欧阳锋 #252 已判"verified 语义漂移需声明"（F039"边界无效"也标 true）——#264 只修了 verify_note 文本，布尔值语义仍模糊。本轮升级为三级证据。

## 一、Schema 升级

| 字段 | v0.9（旧） | v1.0（新） |
|:---|:---|:---|
| `verified` | bool | bool（保留——#272 stale 逻辑兼容） |
| `evidence` | 无 | `{grade: 实测\|引用\|推演, source, metric}`（新增，缺省=待回填） |

**版本链**：v0.8（#248）→ v0.9 aliases（#315）→ v1.0 evidence（#317）。v0.8/v0.9 均保留备份未覆盖。

## 二、首批证据回填（13 条）

| grade | 条数 | 代表条目 |
|:---|:---|:---|
| 实测 | 7 | F026（3800→6500 +71%）、F018（40→65 分）、F016（5→3 关键帧控制变量）、F031（6/27 双目标冲突）、F033（V4 六层漏斗）、F099（指标分离实证）、**F022（#252 试点：HINT_MAP 上线）** |
| 引用 | 2 | F003（温度案例 2w→2k，课程转述）、F029（雍博引行业数据 30-65%→70-80%） |
| 推演 | 4 | F057/F030/F070/F094（补全方案预期，未实测） |

> **修订记录（2026-08-13 终审）**：F022 原标"推演"（黄华春假设）——狗粮测试 `test_verified_never_inference` 抓出与 verified=true 冲突（#252 语义漂移重演），修正为"实测"（证据 = #252 试点 HINT_MAP 上线）。数字以 JSON 为准：实测 7 / 引用 2 / 推演 4（欧阳锋终审独立重数一致）。

**约定**：verified=true 的条目 evidence.grade 应为实测/引用；推演条目 verified=false（推演=未验证，只标注预期）。

## 三、与 #272 新鲜度 SLA 衔接评估

**结论：兼容，无冲突。**

- #272 stale 逻辑：`verified + verify_date + 6 个月 → stale`（降级不删除）
- evidence 是纯增量字段，不改 verified 布尔——stale 判断路径不受影响
- 实测数据：`feature_menu.py stale` 回归通过（25 条 verified 全在复审期）

## 四、verify_note 与 evidence 语义边界

| 字段 | 回答什么 | 示例（F039） |
|:---|:---|:---|
| `verify_note`（#264） | 验证结论是什么 | "边界验证：CoV 对门禁体系不适用，标记为跨域无效" |
| `evidence.grade` | 证据怎么来的（多硬） | 实测（试点真的跑过）/ 引用 / 推演 |
| `evidence.metric` | 具体指标数字 | 阅读量 3800→6500（+71%） |
| `evidence.source` | 出处（素材+行号） | Live258 作业集 L243-244（黄华春） |

**不重复原则**：verify_note 写结论，evidence 写证据性质——同一验证事件两边各写各的，不互相复制。

## 五、验证记录

- ✅ 100 Feature 全保留，25 条 verified 计数一致（迁移无丢失）
- ✅ `feature_menu info F026` 显示证据等级/指标/来源
- ✅ list/query 行内显示 [实测]/[推演] 标记
- ✅ stale / combo / query 别名命中全部回归通过
