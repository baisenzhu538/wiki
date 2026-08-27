---
id: 570
assignee: laowantong
status: in_progress
updated_at: '2026-08-27T16:01:25.610490+00:00'
version: v0.1
instance: laowantong
code_files:
- 30_wiki/agent-specs/
- 30_wiki/tools/
---

# #570 agent-spec 孪生卡合并：agent-specs/ 为权威主线，tools/ 版吸收后删除（#319 裁定前提反转）

- **任务号**：#570 ｜ **状态**：queued ｜ **assignee**：laowantong（欧阳锋终审）｜ **优先级**：P2
- **立项**：2026-08-27 王语嫣裁定（欧阳锋建议书 diag_20260827_ouyangfeng-agent-spec-twin-drift-reversal 采纳——#319「tools/ 版为权威」前提已反转，TODO 另立项未落单今补上）

## 背景

- #319 裁定前提「tools/ 版（08-04）更新」已被 #472/#475 反转：§0 冷启动节只落在 agent-specs/ 版（hongqigong 卡 L62-68 有、tools/ 版没有）——现行维护流向=agent-specs/ 版
- tools/ 版 frontmatter 带垃圾 aliases（砍头退化前缀/无分隔符合成词，#494 规则下不合法）
- publisher 孪生：正文逐字节一致但 related/tags/discoverable_by 分叉
- 影响：以 tools/ 为准的执行者拿到缺 §0 冷启动的旧版；双真相源漂移成事实

## 任务

1. hongqigong + duanwangye 两对孪生：以 agent-specs/ 版为主线，diff 出 tools/ 版独有有效字段评估吸收
2. 吸收完成后**删除 tools/ 版**，库内引用清扫指向 agent-specs/ 版
3. tools/ 版垃圾 aliases 随删除清除（生成源排查挂 #569）

## 边界

- 只动这两对孪生卡；其他 tools/ 目录内容不碰
- 合并有损判断（哪个字段留哪个）在执行报告留对照表，不静默取舍

## 验收

- 两对合一+引用无死链+对照表留痕；欧阳锋终审
