---
id: task_20260629_wangyuyan-goat-milk-channel-partnership-bridge
type: task
status: reviewed
assignee: 老顽童(Hermes分身-Claude)
priority: P2
created_at: 2026-06-29
updated_at: 2026-06-29
reviewed_by: 欧阳锋
reviewer: 欧阳锋
source_refs:
- 60_feedback/diag/diag_20260629_wangyuyan-goat-milk-channel-partnership-nine-layer.md
related:
- [[diag_20260629_wangyuyan-goat-milk-channel-partnership-nine-layer]]
- [[tool-strategy-profit-model-comparison]]
- [[tool-yitang-channel-scoring-matrix]]
- [[yt-management-partnership-equity]]
- [[yt-tool-unit-model-construction]]
- [[framework-yitang-channel-unit-economics]]
- [[tool-yitang-channel-agent-interview]]
---

# 羊奶「卖地图」跨域桥接卡生产任务

## 触发背景

用户在对话中追问羊奶销售模式，确认羊奶行业普遍采用「卖地图」式区域代理/阿米巴包干模式。王语嫣已完成九层深挖诊断（见 source_refs），现进入 `method-dialogue-driven-kb-evolution` Ring 4–5，将桥接卡拆入生产队列。

## 目标域

- **主域**：渠道增长（channel-growth / yitang-growth）
- **桥接域**：商业模式选择（strategy / business-model）、激励机制/合伙（management / partnership）
- **案例域**：yitang 实战案例

## 待生产卡片清单

### 1. `framework-yitang-channel-partnership-map`（P0 桥接卡）

- **type**: framework
- **title**: 小众品类渠道合伙人/区域包干决策框架（「卖地图」模式）
- **核心主张**：小众/非标/高教育成本品类，为何需要把区域经营权「卖」给代理商，而非直营或底薪销售。
- **必须包含**：
  - 决策矩阵：品类特征 × 渠道模式选择
  - 「卖地图」模式的 5 个结构要素（厂商/代理商权责利）
  - 适用边界与 6 种失败模式
  - 与 `tool-strategy-profit-model-comparison` 四模式框架的接口
  - 与 `tool-yitang-channel-scoring-matrix` 的接口
  - 跨域双向价值说明
- **related 要求**：≥8，必须包含
  - `tool-strategy-profit-model-comparison`
  - `tool-yitang-channel-scoring-matrix`
  - `tool-yitang-channel-agent-interview`
  - `yt-management-partnership-equity`
  - `yt-tool-unit-model-construction`
  - `framework-yitang-channel-unit-economics`
  - `case-yitang-goat-milk-channel-partnership`

### 2. `case-yitang-goat-milk-channel-partnership`（P1 案例卡）

- **type**: case
- **title**: 羊奶粉「卖地图」区域代理模式案例
- **核心内容**：
  - 案例背景：羊奶 vs 普通婴儿奶粉的渠道差异
  - 关键证据：课堂口述 + itingnao 3979746 转写
  - 模式结构：底价供货 + 区域包干 + 代理商自负盈亏
  - 关键决策点：为什么不能用底薪提成？为什么必须「托付生意」？
  - 结果/影响：厂商轻资产扩张，代理商深度经营本地
  - 教训：窜货、底价设计、品牌控制力弱
- **必须包含标准 case section**：
  - 关键证据
  - 可迁移场景
  - 教训/失败模式
  - 相关方法论
- **related 要求**：≥5，必须包含
  - `framework-yitang-channel-partnership-map`
  - `tool-yitang-channel-agent-interview`

### 3. `tool-yitang-channel-partnership-design`（P2 工具卡）

- **type**: tool
- **title**: 区域代理/底价合伙人模式设计工具
- **核心内容**：
  - 底价设计公式与敏感性分析
  - 区域划分原则（按人口/消费能力/现有资源）
  - 代理商筛选访谈清单
  - 窜货防控与价格体系维护
  - 退出/回购机制
- **必须包含标准 tool section**：
  - 目的
  - 操作步骤
  - 不要用的场景
  - 质疑
- **related 要求**：≥5，必须包含
  - `framework-yitang-channel-partnership-map`
  - `yt-management-partnership-equity`

## 质量标准

- 所有卡片必须通过 `kdo pre-submit`
- framework 卡必须包含闭环图/映射表
- case 卡必须标注 `conf=` 可信度
- 所有外部证据/行业数据必须标注来源或 `[待核实]`
- 不使用 `src_unknown` 占位

## 验收标准

- 3 张卡片全部 status 更新为 reviewed
- `kdo lint` 目标卡无新增 ERROR/WARNING
- framework 卡 related ≥8，case/tool related ≥5
- 相邻域卡片（`tool-strategy-profit-model-comparison` 等）视情况补充 related 回链

## 交付记录

### 2026-06-29 老顽童(Hermes分身-Claude) 交付

**产出文件**：
1. `30_wiki/frameworks/framework-yitang-channel-partnership-map.md` — P0 桥接框架卡（9 related，~350 行正文）
2. `30_wiki/cases/case-yitang-goat-milk-channel-partnership.md` — P1 案例卡（6 related，~210 行正文）
3. `30_wiki/tools/tool-yitang-channel-partnership-design.md` — P2 工具卡（7 related，~330 行正文）

**验收自检**：
- [x] 3 张卡全部创建，类型正确（framework / case / tool）
- [x] framework related ≥ 8（实际 9），case/tool related ≥ 5（实际 6/7）
- [x] framework 包含：决策矩阵 + 五要素结构 + 六种失败模式 + 与 profit-model/scoring-matrix 的接口 + 跨域双向价值
- [x] case 包含：关键证据 + 可迁移场景 + 教训/失败模式 + 相关方法论
- [x] tool 包含：目的 + 操作步骤（五模块）+ 不要用的场景 + 质疑
- [x] 所有外部证据标注 conf= + 待独立核实
- [x] 无 src_unknown 占位
- [ ] kdo pre-submit（kdo CLI 未在本地安装，需黄药师协助跑门禁）
- [ ] kdo lint 目标卡（同上）

**已知待补**：
- 羊奶行业具体财务数字（代理商净利润率、终端零售价、底价区间）需补充行业报告或实地调研数据——素材（课堂口述 + 会议转写）未含具体数字
- pre-submit 门禁待黄药师协助执行
- 相邻域卡片（profit-model-comparison 等）的 related 回链建议在欧阳锋审查后由老顽童补充
