---
id: task_20260726_wangyuyan-debt-cleanup
task_id: 207
assignee: laowantong
status: queued
created_at: 2026-07-26
updated_at: 2026-07-26
domain: system
priority: P3
---

# 存量卡质量债务渐进清理

> P3长程任务。老顽童碎片时间做，不设deadline，不阻塞主线。每做完一项勾一项。

## 规则

- **不批量返工**：该卡因其他原因返工时顺手处理
- **每次只做一小批**：5-10张，做完即停
- **每批可独立验证**：跑 `kdo pre-submit` 确认无新增ERROR

## 待清理清单

### 命名卡升级（来源：#204深挖）

| # | 卡 | 当前状态 | 动作 |
|:--|:--|:--|:--|
| 1 | `tool-月白-设计文件八要素命名法` | draft/low-trust | upgrade→reviewed，补source_refs |
| 2 | `tool-月白-文件命名与图层命名规范` | draft/low-trust | upgrade→reviewed |
| 3 | `tool-月白-文件命名与存档规范` | draft/low-trust | upgrade→reviewed |
| 4 | `tool-月白-文件命名与平台适配规范` | draft/low-trust | upgrade→reviewed |
| 5 | `tool-月白-课程资料文件命名规范` | draft/low-trust | upgrade→reviewed |
| 6 | `tool-月白-设计师AI资产四类型沉淀` | draft/low-trust | upgrade→reviewed |

### 标签补全（来源：#206标签诊断）

| # | 范围 | 动作 |
|:--|:--|:--|
| 7 | 所有 `tags: null` 或 `tags: []` 的卡 | 该卡因其他原因返工时顺手补tags（按tag-registry维度） |
| 8 | 半肥猫相关卡（`case-半肥猫-*`/`tool-kdo-agent-production-*`） | 补行业/场景/成熟度标签 |

### 定位声明补全（来源：#199）

| # | 范围 | 动作 |
|:--|:--|:--|
| 9 | 存量卡缺定位声明 | 该卡返工时顺手补（格式：`> 定位：属于 [[framework-xxx]] 的 Y 步。`）。framework/digest/hub豁免 |

### 历史残留清理（来源：#201 Wave 0.3）

| # | 卡 | 动作 |
|:--|:--|:--|
| 10 | `framework-yitang-jiefang-sixiang.md` | 清理source_refs中000_inbox路径残留 |

### 发现新问题时追加到本清单

新发现的存量质量问题，不单独排任务——追加到本清单。保持主线队列干净。
