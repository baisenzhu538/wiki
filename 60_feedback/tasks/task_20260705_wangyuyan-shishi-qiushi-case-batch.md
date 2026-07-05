---
id: task_20260705_wangyuyan-shishi-qiushi-case-batch
type: task
status: in_progress
assignee: claude
reviewer: 欧阳锋
priority: P1
created_at: 2026-07-05
updated_at: '2026-07-05T03:38:21.769300+00:00'
source_refs:
- 00_inbox/实事求是/_processed/实事求是_整合笔记.md
- 00_inbox/实事求是/实事求是-周子敬-口述.txt
- 00_inbox/实事求是/_processed/实事求是-大坑之*_vlm.md
related:
- '[[framework-yitang-shishi-qiushi]]'
- '[[dk-yitang-over-abstraction]]'
- '[[dk-yitang-over-prediction-danger]]'
---

# 任务 #109：实事求是十坑案例卡批量生产（10 张 case 卡）

## 背景

KDO 已有 `framework-yitang-shishi-qiushi` 框架卡 + 2 张 dk 卡（过度抽象/过度预测）。但"十个大坑"对应的 10 个具体案例一张都没有。

## 十个大坑（5 实事 + 5 求是）

| # | 坑名 | 领域 | 已有覆盖 | VLM 文件 |
|:---:|:---|:---:|:---:|:---|
| 1 | 主观臆测 | 实事 | ❌ | 已提取 |
| 2 | 忽略事实 | 实事 | ❌ | 已提取 |
| 3 | 以偏概全 | 实事 | ❌ | 已提取 |
| 4 | 不会定量 | 实事 | ❌ | 已提取 |
| 5 | 过度预测 | 实事 | dk 已有 | 已提取 |
| 6 | 不信规律 | 求是 | ❌ | 已提取 |
| 7 | 轻视规律 | 求是 | ❌ | 已提取 |
| 8 | 错误类比 | 求是 | ❌ | 已提取 |
| 9 | 金句迷信 | 求是 | ❌ | 已提取 |
| 10 | 过度抽象 | 求是 | dk 已有 | 已提取 |

## 素材

- `00_inbox/实事求是/_processed/实事求是_整合笔记.md`：完整结构 + 段位表
- `00_inbox/实事求是/实事求是-周子敬-口述.txt`：案例细节
- `00_inbox/实事求是/_processed/实事求是-大坑之*_vlm.md`：10 个 VLM 提取

## 产出

10 张 case 卡，每张包含：
- 坑的定义（从整合笔记提取）
- 1 个具体案例（从周子敬口述提取）
- 诊断信号（用户说了什么意味着掉进这个坑）
- 修复方法（实事求是框架的对应步骤）
- 标准 case section

## 对 Agent 建设的价值

实事求是诊断 Agent：读取用户商业分析→识别掉进哪个坑→推荐对应的 case 卡和修复方法。10 张 case 卡就是这个 Agent 的核心数据层。

## 验收标准

- 10 张卡 `kdo pre-submit` PASS
- 每张含 1 个真实案例 + 诊断信号 + 修复方法
- index.md 收录
- 欧阳锋终审通过（可分批）
