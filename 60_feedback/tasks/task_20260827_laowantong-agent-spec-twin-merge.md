---
id: 570
assignee: laowantong
status: pending_review
updated_at: '2026-08-27T16:12:58.154821+00:00'
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

## 建模方案（L1 出牌，2026-08-28 老顽童）

依赖链：`[素材] → [边界] → [结构] → [质量]`

| 位 | 牌号 | 一句话理由 |
|:--|:--|:--|
| 素材 | #14 先跑脚本确认 | diff 实测两对孪生：hongqigong 差 76 行（tools/ 版缺 §0 冷启动+终审记录，多垃圾 aliases）；duanwangye 差 55 行（正文逐字节一致，仅 frontmatter+终审记录分叉） |
| 边界 | #5 先判归属 | agent-specs/=权威主线（#319 前提已反转）；tools/ 版吸收后删除 |
| 边界 | B1 写读对账 | 删除 tools/ 版前必须全库 grep 引用面（路径引用+wikilink），全部改指 agent-specs/ 版，不留死链 |
| 结构 | 不碰在途缺陷 | 两卡带 #544 批次二「退回」终审记录（P1/P2 内容缺陷落点=洪七公/段王爷本人修）——合并只做字段级机械并集，不修内容缺陷、不静默取舍，对照表留痕 |
| 质量 | L3/L4 | 改后两卡跑 pre-submit；引用面 grep 复核零死链 |

**关键决策点（对照表素材）**：tools/ 版 aliases 5 条中 3 条是砍头退化前缀（#494 不合法，随删除清除），1-2 条合法词评估并入主线；related 重复行（hongqigong 卡 framework-truman-agent-team-architecture×2）机械去重。

## 验收

- 两对合一+引用无死链+对照表留痕；欧阳锋终审

## 执行报告

**改动文件**（清单）：`30_wiki/agent-specs/agent-spec-hongqigong-multimodal.md`（合并主线）；`30_wiki/agent-specs/agent-spec-duanwangye-publisher.md`（合并主线）；`30_wiki/index.md`（删两行 tools/ 版导航——45-46 行已有 agent-specs/ 版条目，防重复）；删除项（git rm 已入 commit 不含路径校验）：30_wiki/tools/agent-spec-hongqigong-multimodal.md、30_wiki/tools/agent-spec-duanwangye-publisher.md
**完成内容**（一句话）：两对 agent-spec 孪生卡合一——agent-specs/ 版为权威主线吸收 tools/ 版有效字段，tools/ 版 git rm 删除，库内活引用清扫归零，同 id 重复（DUPLICATE ID 隐患）随删除消除。
**验证**（命令+输出）：
  - `diff agent-specs/版 tools/版`（合并前实测）：hongqigong 差 76 行 / duanwangye 差 55 行（正文逐字节一致，差异全在 frontmatter+§0 冷启动节+终审记录节，均在主线侧）
  - `kdo pre-submit -f <两卡>` → 双 PASS（均 75 分；警告=存量 ALIASES 误报族 + #542 CONCEPT_CROSSCHECK 提示制，非本次引入）
  - 引用清扫验证：Grep `tools/agent-spec-(hongqigong|duanwangye)` 活目录（30_wiki/70_product/.agent/agents）→ 零命中；残留命中全在历史快照/机器产物（eval-results/health-check 日志/lint baseline/depended-draft inventory——随下次重生成自然更新）
  - `kdo index --incremental` → `-2`（tools/ 版出索引）
**未做项**（边界）：①两卡 #544 批次二「退回」终审记录中的内容级缺陷（P1 署名升格/引语出处、P2 死链 content-production-polish 等）按落点归洪七公/段王爷本人修，本单不碰 ②lint baseline / depended-draft inventory 中的 tools/ 版条目属机器产物，随下次重生成消，不手改 ③垃圾 aliases 生成源排查挂 #569（本单仅随删除清除存量）
**需要谁动作**：欧阳锋终审；洪七公/段王爷按 #544 终审落点修内容缺陷（合并后主线在 agent-specs/，修那里）

### 合并有损判断对照表（不静默取舍）

**hongqigong 孪生**：

| 字段 | agent-specs/ 版 | tools/ 版 | 取舍 |
|:--|:--|:--|:--|
| aliases | 无 | 5 条（2 合法+3 垃圾前缀） | 吸收 2 条合法（多模态渲染与视觉资产生产引擎/洪七公）；3 条砍头前缀随删除清除（#494 不合法） |
| discoverable_by | 5 条 | 3 条 | 并集=7 条（补"洪七公 Multimodal Agent — KDO 多模态"+"多模态渲染与视觉资产生产引擎"） |
| related | framework-truman-agent-team-architecture×2 重复 | wikilink 形式无重复 | 机械去重，留主线平铺形式 |
| tags | Agent/方法 | article/beikai/capabilities | 留主线（tools/ 三条与卡片类型不匹配，弃） |
| §0 冷启动节+终审记录节 | 有 | 无 | 主线保留（#472/#475 新制+终审留痕） |

**duanwangye 孪生**：

| 字段 | agent-specs/ 版 | tools/ 版 | 取舍 |
|:--|:--|:--|:--|
| aliases | 无 | 5 条（2 合法+3 砍头/断尾） | 吸收 2 条合法（内容发布与渠道分发引擎/段王爷）；3 条随删除清除 |
| discoverable_by | 5 条 | 3 条 | 并集=7 条 |
| related | dk-publish-collapse-to-iterate×2 重复 | 无重复 | 机械去重 |
| tags | 文章/卡片 | capabilities/content/outputs | 留主线 |
| 正文 | 与 tools/ 逐字节一致 + 终审记录节 | — | 主线保留 |

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 5 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🟡 ⚠️ 意见书含宽负向词（无/缺）无核查锚点——按需人工确认（#433 不硬杀）；锚点：⚪ 无锚点
