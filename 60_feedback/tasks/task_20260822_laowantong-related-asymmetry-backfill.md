---
id: 411
assignee: laowantong
status: queued
title: related-asymmetry 存量分批回填（P2，欧阳锋 08-22 立项）：7472 条单向链按域分批消化——#383/#384/#406 回链线延续
priority: P2
dependency: []
updated_at: '2026-08-21T20:30:00+00:00'
---

# #411 related-asymmetry 存量分批回填

## 来源

- 用户 08-22 授权"清理遗留库级债务"；#399 遗留建议 2（欧阳锋裁决：量级大，回链线按批消化）
- 当前基线（`full-library-rescan` 实测，2026-08-22）：**related-asymmetry 剩余 7472**（08-21 基线 7415；工具已排除 60_feedback + 系统页 + 同对去重）

## 任务目标

分批消化 7472 条 related 单向链（A 链 B 但 B 未回链），每批附复扫输出递减，长期归零。

## 执行范围

1. **出清单**：`full-library-rescan --check related-asymmetry` 拿全量清单（>50 列前后各 25，可用 --json 导出分批）
2. **按域分批**：每批 200-300 条，优先高连通域（framework/concept 锚点卡）；每批一个执行报告
3. **补反向 related**：只增不改（E017/#384 模式），不动机身正文；目标卡 related 加被引卡的 id/stem（`- '[[<id>]]'` 格式，KDO related 单引号格式）
4. **批次验收**：每批完成后跑 `full-library-rescan --check related-asymmetry` 附输出（数量递减 + 本批涉及的链归零）
5. 涉及内容歧义（该不该链）的记 TODO 列清单，不硬链

## 边界

- 只动 related 区，不动机身正文、不动 frontmatter 其他字段
- 60_feedback/ 不在回链范围（工具已排除）
- 每批 commit 入档（E040）；pre-submit 0 死链（目标卡）
- 本任务可长期分批推进（每批报告即可），不要求单次全清

## 验收标准

1. 每批附 `full-library-rescan --check related-asymmetry` 输出（递减）
2. 抽查回链真实性（被引卡确实存在 + 主题相关）
3. 无正文污染（diff 只增 related 行）
4. 欧阳锋终审抽"回链真实性"

## 交付

1. 分批执行报告（每批：清单 → 回链数 → 复扫输出）
2. 送欧阳锋终审（每批或批量）
