---
id: task_20260903_laowantong-template-assetization-batch1
title: 模板资产化批1：Agent 白皮书模板文件化 + 复盘画布/私董会SOP/双三角画布/回款playbook/产品画布族抽模板（落 capabilities/templates/）
seq: 632
status: pending_review
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-03
decision_source: 老朱 09-03 直令「模板是重要资产，按同标准排查全库同样处理」+ 王语嫣全库扫描（子代理严标准：可直接填空/照做才算）
reviewer: 欧阳锋
instance: laowantong
updated_at: '2026-09-03T02:23:37.299569+00:00'
evidence: 60_feedback/tasks/evidence_20260903_632_template-batch1.md
---

# #632 模板资产化批1（老顽童）

## 标准（老朱口径）

模板=可直接使用的资产（填空即产出），落 `40_outputs/capabilities/templates/`（已有先例：template-article/checklist-proposal 等 6 件同目录）。每个模板文件：占位符驱动 + 头部注明来源卡 wikilink（回链知识层）+ 尾部使用说明三行。

## 本批范围（6+3 件）

1. **agent-whitepaper-template.md**（主令）：从 `tool-agent-whitepaper-full-lifecycle-template` 卡抽 11 节填空模板（五要素/权限三层/初始化 16 步/灵魂校验占位符化）。⚠️ 密级：kinda「不要外传」——模板文件头部继承传播限制标注
2. **retrospective-canvas.md** ← `tool-yitang-retrospective-canvas`（项目复盘画布，含 5Why 三层根因填空行）
3. **private-board-facilitation-sop.md** ← `tool-private-board-facilitation-sop`（90 分钟七步+主持人话术+收敛句式）
4. **dual-triangle-canvas.md** ← `tool-yihang-dual-triangle-canvas`（空版六宫格+每格引导问题）
5. **payment-collection-playbook.md** ← `tool-yitang-payment-collection-playbook`（决策表+9条催款 Checklist+关单确认表）
6. **产品画布族三件套**：product-kernel-canvas / business-model-canvas / demand-segmentation-canvas ← `yt-product-kernel-canvas` / `yt-business-model-canvas` / `yt-demand-segmentation-canvas`

## 不在本批（裁决留痕）

- #5 agent 生产检查单 vs 白皮书模板：互补不合并——检查单留卡层，模板文件化时在其「初始化 16 步」节末尾加「配套检查单见 [[tool-kdo-agent-production-checklist]]」引用
- #6 双三角 filler 的 System Prompt/自评表、#9 股权清单、#11 ROI 画布、#12 需求盲区（均有 src_unknown 空洞或重叠）——先补空洞再化，挂下批
- #15 视觉 prompt 模板族（inbox 素材层）——挂下批评估
- 不模板化清单（子代理判定我复核同意）：课程创作 11 步（价值在判断力不在骨架）、反脆弱五问（心智模型优先）、山西调研清单（一次性项目）、行业分析画布（内容不足先回源）

## 交付

- 9 个模板文件落 40_outputs/capabilities/templates/ + 每文件与源卡双向互链 + 执行报告（含逐件占位符可填性自检：假装自己是使用者填一遍关键位）
- claim/complete 走 queue_transition（complete 632）

## 执行报告（2026-09-03 laowantong/cli 实例）

**交付物**
8 个模板文件落 `40_outputs/capabilities/templates/`：
1. `agent-whitepaper-template.md`（200 行，11 节填空+灵魂校验三问+身份断言+初始化16步打勾+三权分立变更表；头部继承密级「内部使用·不要外传」（#322 口径）+「初始化16步」节末挂 [[tool-kdo-agent-production-checklist]] 引用——裁决 #5 留痕执行）
2. `retrospective-canvas.md`（135 行，六区填空，5Why 三层根因逐层填空行+签字区+最小可行版本指引）
3. `private-board-facilitation-sop.md`（155 行，Step 0-7 逐步填空+主持人话术可照念+收敛句式套填+控时表带实际用时列）
4. `dual-triangle-canvas.md`（56 行，2×3 六宫格每格 3 引导问题+填写区+四原则自检位）
5. `payment-collection-playbook.md`（96 行，四部分：决策点定位勾选表+顺序重构决策表（财务/法务复核留痕栏）+9 条催款 Checklist 逐项带日期填空+关单标准确认表）
6. `product-kernel-canvas.md`（87 行，四区填空+正误对照合格标准+功能↔问题对齐自检）
7. `business-model-canvas.md`（84 行，9 要素一句话填空+团队独立填对比流程+5 行匹配检查勾选+迭代排期勾选）
8. `demand-segmentation-canvas.md`（85 行，≥5 层清单表+优先级矩阵+分层后决策表+照示例颗粒度自检）
每件：头部 frontmatter `source_card` wikilink 指源卡 + 尾部「使用说明」三行（来源/进入退出标准或不适用场景/纪律）；8 张源卡 `related` 全部回链模板（git show 2e207340f 可验：8 源卡各 +1 行，product-kernel +3 行含上下游配套链）。

**完成内容**
任务单「本批范围」清单全量执行。⚠️ 计数口径差异留痕：任务单写「9 件/6+3 件」，但文件清单实列 8 个文件名（5 单件+产品画布族三件套）——按文件清单全量交付 8 件，一件不少；「9」与「6+3」疑为编排侧计数口径差（三件套算 1 组时为 6，算 3 件时为 8，均不等于 9），请欧阳锋终审时核对原扫描清单是否有第 9 件被漏列。

**验证**
- L1 机械验证（脚本实跑）：8 件双向互链全通过（源卡 related 含模板 wikilink + 模板头 [[源卡]] + frontmatter source_card + id=文件名一致 + 尾部使用说明存在）；frontmatter YAML 逐件可解析、必填字段（id/title/type/status/source_card）齐；白皮书模板密级标注（「不要外传」+classification 字段）与检查单引用在位。
- L2 狗粮（可填性自检，任务单要求）：复制 8 件到 TEMP 目录假装使用者真实填一遍关键位——每件 4-5 个关键位（表格行/填空线/勾选框三类锚点）全部可定位；白皮书身份断言占位符回填「report-butler」后可直接执行；8/8 通过。自检产物已清理不入仓。
- 交付物已入仓：vault backup 2e207340f（10:22:06）含全部 16 文件（8 模板+8 源卡互链），complete 前 git status 无本单脏文件。

**边界**
- 只做批 1 清单内 8 件；裁决「不在本批」的 #6/#9/#11/#12/#15 空洞族与不模板化 4 件均未动。
- 三件套源卡（yt-product-kernel/business-model/demand-segmentation）正文仍有 src_unknown 空洞（任务单已裁决「先补空洞再化，挂下批」的范围不含这三件本体修复）——模板只抽取了源卡中实证在位的框架部分，src_unknown 内容未进模板。
- 双三角 filler 的 System Prompt/自评表等 filler 配套未模板化（挂下批）。

**需要谁动作**
欧阳锋：终审 8 件模板+互链+计数口径裁决（8 vs 9）。可选：黄药师后续将 templates/ 纳入 kdo index 索引面（本单未擅自跑 index --rebuild，按铁律留给黄药师）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

⚪ 无路径级交付物声明（纯文档/诊断类或未用反引号标注路径）——差集无检查面
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）
