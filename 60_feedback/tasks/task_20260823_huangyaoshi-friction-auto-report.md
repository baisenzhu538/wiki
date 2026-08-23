---
id: 458
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-23T05:59:43.911171+00:00'
version: v0.1
instance: huangyaoshi
---
# #458 问题主动上报自动化（friction 统一记录 + 探针第四探针 + 复盘强制节）

- **任务号**：#458
- **状态**：queued
- **assignee**：huangyaoshi（基建单一实例；终审=欧阳锋；编排=王语嫣）
- **优先级**：P1（老朱 2026-08-23 核心关切：「有什么办法让 agent 发现问题主动上报，最好也是自动化提交……如果不说，也就沉没下去了」——#454 门禁误判靠老朱翻老顽童上下文才浮出）
- **立项**：2026-08-23 王语嫣（编排设计：记录零成本 → 传输全自动 → 消费编排决策）

## 问题本质（沉没链分析）

现状通道：agent 发现问题→自觉写建议书（diagnosis/，需完整格式+三元组 frontmatter）→探针自动登记+通知。断点在**第一步**：写完整建议书太重（老顽童 #454 误判是靠老朱翻上下文才发现——问题没进任何通道）；且格式错（status: pending ≠ pending_orchestration）探针就不登记——本次老顽童建议书即漏登记实例。

## 方案（三层，治「发现后不提交」）

### 1. 记录端零成本：friction-log 统一化

- 每个 agent 一个 `Desktop/agent复盘/<agent>/friction-log.md`（部分角色已有，全角色统一）
- 格式=一行式（发现即 append，成本≈0）：`YYYY-MM-DD HH:MM｜场景｜问题一句话｜（可选）建议方向`
- 六角色 context 加硬话术：「执行中遇到任何摩擦/误判/工具问题，当场 friction-log append 一行——写建议书是加分项不是必选项，friction 一行是必选项」（话术统一口径由王语嫣出，各角色 context 维护者写入——挂本单动作）

### 2. 传输端全自动：探针第四探针（friction 增量扫描）

- `conveyor_probe.py` 增加摩擦探针：扫六角色 friction-log 增量（按行 hash/mtime 记状态）→ 命中新行自动登记 PROPOSAL-PENDING（**类型=「问题线索」**，区别于完整建议书）+ 通知王语嫣
- **不依赖建议书 frontmatter 格式**——friction-log 是纯 append 文本，无格式门槛（根治 status 写错导致漏登记一类问题）
- 登记行格式：`[friction] <agent>｜<问题一句话>｜<时间>`——王语嫣复核后处置（立案/忽略/转完整建议书）划掉

### 3. 强制端兜底：复盘必填「问题」节

- 复盘模板（`templates/daily-context-template.md`）加必填节「本会话发现的问题/摩擦」——必须显式声明（有则列，无则写「无」；零摩擦会话极罕见）
- `review-check.py` 检查该节存在（缺失=形式主义降级，#419 深度四指标同款）
- 复盘问题节与 friction-log 双通道：复盘节保证「想过」，friction 行保证「上浮」——复盘归档时脚本可提示「复盘问题节有 N 条，friction-log 未对应的有 M 条」防漏记

## 验证（验证分层声明）

- L1：单测（friction 增量检测/幂等/六文件扫描）
- L2 狗粮：手工 append 一行测试 friction → 探针跑一轮 → PROPOSAL-PENDING 出现 [friction] 行+通知到达
- L3 待活体：下一单真实摩擦（如再遇门禁误判）30 分钟内自动浮到我面前

## 边界

- 只拦机械项：探针只搬运不判断（处置仍归王语嫣）；friction 行不强制建议书格式
- 建议书通道保留不变（有方案的问题仍走完整建议书）——本单补的是「轻量问题」的上浮面
- 与 #421 探针架构一致：单扫描器纪律（第四探针与前三探针同一次扫描事件），禁第二套扫描器

## 执行报告（F-034 五字段+验证分层声明，complete 前必填）

（生产者填写）
