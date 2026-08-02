---
id: task_20260726_wangyuyan-debt-cleanup
task_id: 207
assignee: laowantong
status: pending_review
created_at: 2026-07-26
updated_at: '2026-08-02T23:59:00+00:00'
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

### 标签补全（来源：#206 Phase 2——黄药师建议书）

> 不排专门批量返工。老顽童返工时顺手加。4周自然覆盖，达80%后激活Phase 3 lint门禁。

**标的优先级**：

| 优先级 | 对象 | 数量 | 需标维度 | 触发时机 |
|:--|:--|:--:|:--|:--|
| P0 | framework卡 | ~30张 | method + industry + value-tier | 该卡返工时顺手加 |
| P0 | domain-digest/MOC卡 | ~10张 | content-format + prerequisite-knowledge | 同上 |
| P0 | agent-spec卡 | 8张 | usage-depth + value-tier + method | 同上 |
| P1 | 新域首卡（近30天） | ~15张 | activation_rules要求的所有维度 | 王语嫣出诊断时标注建议维度 |
| P2 | tool卡 | ~960张 | method（如domain推断不出） | 不专门排——等自然返工 |

**操作**：王语嫣新任务单加"建议标签"列。老顽童返工时复制到frontmatter。欧阳锋Phase 0扫描P0卡是否缺method标签（缺=🟡提醒，不阻断）。

### 定位声明补全（来源：#199）

| # | 范围 | 动作 |
|:--|:--|:--|
| 9 | 存量卡缺定位声明 | 该卡返工时顺手补（格式：`> 定位：属于 [[framework-xxx]] 的 Y 步。`）。framework/digest/hub豁免 |

### Agent运行时配置审计（来源：2026-07-26 洪七公vision故障）

| # | 范围 | 动作 |
|:--|:--|:--|
| 13 | 所有Agent config中硬编码的URL/路径/域名 | 黄药师扫描对照当前实际可用端点，输出差异清单。同一故障模式第四次复现——kdo query不索引aliases、queue_transition被手工绕过、Hermes硬编码.io域名——都是配置层和运行层不同步 |

### 历史残留清理（来源：#201 Wave 0.3）

| # | 卡 | 动作 |
|:--|:--|:--|
| 10 | `framework-yitang-jiefang-sixiang.md` | 清理source_refs中000_inbox路径残留 |

### #215讲香新卡欠账（来源：#215复审TODO，2026-08-02）

> 欧阳锋复审#215 PASS/A-时放行的2项🟠TODO，记入本清单（欧阳锋裁决）。

| # | 卡 | 当前状态 | 动作 |
|:--|:--|:--|:--|
| 14 | `tool-jiangxiang-ai-four-levels` | 缺`## Critique`节（只有Synthesis） | 补Critique节——外部攻击者（如"快速迭代派：等你想清楚市场已没"）+内部局限（"最后一步"前置时间成本） |
| 15 | `dk-jiangxiang-boundary-overpromise` | Critique只有内部局限 | 补外部攻击者——如"营销派：讲香就是包装话术""广告法合规视角：断言式金句是否越界" |

### 发现新问题时追加到本清单

新发现的存量质量问题，不单独排任务——追加到本清单。保持主线队列干净。
