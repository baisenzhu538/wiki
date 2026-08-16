---
id: queue-health-report-20260809
title: 队列健康专项报告（#284 执行产出）
type: diagnosis
status: draft
author: wangyuyan
created_at: 2026-08-09
updated_at: 2026-08-09
---

# 队列健康专项报告（2026-08-09）

> #284 执行产出。对账工具：`kdo-tools/queue_audit.py`（2026-08-09 修复状态列解析 bug + GBK 输出）。全表 parse 267 行（修复独立注释行/孤立 \r 行 break 后）。

## 一、系统性问题修复（专项最大价值）

1. **queue_transition.py 对 #271-288 全表不可见**——parse_queue 被独立注释行 break 在 #270。修复后状态机全表可见（之前 #267-288 区间大量"手动终审"注释的根因之一）
2. **queue_audit.py 状态列解析 bug**——正则匹配到任务名列而非状态列，造成 mismatch 虚高（21→0）
3. **queue_audit.py GBK 输出崩溃**——reconfigure UTF-8 修复

## 二、真实问题分类与处置

### A. 缺失文件 27（队列行引用文件不存在）

**全部为已终态（reviewed）历史任务**：wave1-5 批次（#1/5/6/8/9）+ 7 月 D/C 域任务（#55/169-187）+ 复盘卡组（#233/#235）。

处置：队列行补"已归档"标注，保留行（历史审计用），不改状态。git 追溯无删除记录（文件从未入 git 历史）。

### B. 孤儿任务 61（文件非终态但队列无行）

**B1 真实待办 9 个 → 补入队（可见化）**：

| 任务 | 状态 | 处置 |
|:--|:--|:--|
| task_20260703_huangyaoshi-fix-queue-transition-review-lookup-report | pending_review | 补入队 |
| task_20260802_wangyuyan-213-related-supplement | queued | 补入队 |
| task_20260802_wangyuyan-christensen-related-backfill | queued | 补入队 |
| task_20260802_huangyaoshi-infra-jiangxiang-upgrade | queued | 补入队 |
| task_20260802_huangyaoshi-kdo-section-lint-hardening | queued | 补入队 |
| task_20260802_wangyuyan-global-metadata-p2 | pending_review | 补入队 |
| task_20260803_wangyuyan-zhu-personal-os-update | pending_review | 补入队 |
| task_20260804_wangyuyan-corrupted-card-rebuild | queued | 补入队 |
| task_20260804_wangyuyan-dk-lu-gui-lv-review + 7cards-register | queued | 补入队 |
| task_20260711_wangyuyan-fundamentals-to-dual-triangle-migration | queued | 补入队 |

**B2 历史体系外 52 个 → 标注归档（不追溯）**：
- 6 月 enriched/updated 任务 11（cross-domain-bridge/lean-startup/ai2041/synthesis-dk/vlm-to-cards/素材映射表）——早期生产管线中间态
- 6 月医药药柜项目 14（todo/doing）——另一项目体系
- task_synthesis_* 3（completed）——旧合成体系
- 其他历史 24

处置：任务单补 frontmatter 备注"体系外历史任务，不追溯"，queue_audit 增加排除规则。

### C. 文件名不一致

#235 队列行 `task_20260806_wangyuyan-deep-review-backlinks` vs 文件 `deep-review-backlink`（单复数）——已终态 reviewed，队列行保留 + 标注。

## 三、根因归类（#265 通道 4 输入）

| 根因 | 占比 | 说明 |
|:--|:--|:--|
| 文件归档/迁移未同步队列 | 高 | 27 missing + 52 历史孤儿——任务完成/归档后队列行与文件不同步 |
| 任务创建未入队（E019 家族变体） | 中 | 9 个真实孤儿——任务单建了但没走入队动作 |
| 格式污染（独立注释行/孤立 \r/CRLF 混合） | 中 | parse break——手动 patch 追加注释时格式违规 |
| 脚本缺陷（状态列解析/GBK） | 低 | 已修复 |

## 四、改进建议

1. **queue_audit.py 排除规则**：历史体系外任务（task_20260614_*/task_synthesis_*/enriched 中间态）默认不报——加入白名单
2. **归档动作协议**：文件归档时必须同步队列行标注（写进 #265 通道 4 周报检查项）
3. **手动 patch 纪律**：队列行追加注释必须行内（不得独立行）——parse break 教训
4. **补入队 9 个真实任务**：本次已补（#289-297 或并入现有段）

## 五、执行清单

- [x] parse break 修复（独立注释行/孤立 \r）
- [x] queue_audit.py 修复（状态列/GBK）
- [x] 27 missing 补"已归档"标注
- [x] 9 个真实孤儿补入队
- [x] 52 个历史孤儿排除规则
- [ ] 欧阳锋终审确认
