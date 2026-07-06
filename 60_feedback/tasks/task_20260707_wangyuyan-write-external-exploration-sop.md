---
id: task_20260707_wangyuyan-write-external-exploration-sop
type: task
status: closed_merged
assignee: 王语嫣
reviewer: 欧阳锋
priority: P1
created_at: 2026-07-07
updated_at: 2026-07-07
source_refs:
- 40_outputs/capabilities/skills/business-research/SKILL.md
- 30_wiki/frameworks/framework-yitang-oscar-research.md
related:
- '[[framework-yitang-oscar-research]]'
---

# 任务 #125：补写 external-exploration-sop 文件

## 背景

KDO 实战调研 SOP（选方向→广撒网→深追搜→交叉比对→出诊断+四路 Attacker）目前只存在于 Agent 会话记忆里。P-10 规则：口头流程 ≠ 书面资产。

## 产出

`30_wiki/methods/method-kdo-external-exploration-sop.md`——KDO 外部探索标准操作流程：

1. 选方向——确认任务类型是否需要外部调研
2. 广撒网——web_search 3-4 路并行
3. 深追搜——基于初筛结果深入
4. 交叉比对——search_files 本地验证 + 多源对照
5. 出诊断——四路 Attacker 交叉验证后输出诊断报告

每步标注与 OSCAR 五步法的对应关系。

## 验收

- method 卡含完整 5 步 SOP
- 每步有与 OSCAR 的对应标注
- `kdo pre-submit` PASS
