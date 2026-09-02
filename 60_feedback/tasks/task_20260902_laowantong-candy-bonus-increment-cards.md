---
id: task_20260902_laowantong-candy-bonus-increment-cards
title: Candy 课后加餐增量补产：Live260 口喷 ROI 搭档私密案例（原始课稿零覆盖实证）+ 探索营 Candy 增量复核
seq: 624
status: in_progress
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-02
decision_source: 老朱 09-02 纠偏「有的东西是课后的 candy，你需要复核」→ 王语嫣实证：Candy 版=课后作业奖励文档非课稿同源（原始稿 L708 宣告+Candy 内容课稿零命中）
reviewer: 欧阳锋
source_refs:
- 00_inbox/Live260-AI口喷基本功内测candy-逐字稿.md
- 00_inbox/AI知识管理探索营内测Candy-逐字稿.md
instance: laowantong-kimi
updated_at: '2026-09-02T16:09:16.720941+00:00'
---

# #624 Candy 课后加餐增量补产（老顽童）

## 背景（王语嫣判定错误更正）

09-01 我把内测 Candy 版判为「同源整理版沿用旧诊断」——错。实证：Candy 版是一堂课后的**作业奖励/加餐文档**（原始课稿 L708：「🎁 作业奖励 Candy：《Truman教研内部Partner口喷私密案例》」），内容不在课里：ROI 搭档拆成本收益（TOP3 对 TOP3/乐观悲观情形）在 103KB 原始课稿中零命中。**教训：「整理版」三个字不等于同源，Candy=课后加工产物，须当独立素材诊断。**

## 任务

1. **Live260 Candy 加餐**（36KB 逐字读）：产 case/method 卡——Truman 科学决策 ROI 搭档私密案例（口喷原文一等+清单体版本，决策分层：定性/局部定量/严格定量；TOP3 对 TOP3；关键项定量测算乐观悲观情形）。域=decision-making。**传播限制**：文件标「仅限内部不要外传」，按 #322/#611 先例双标注
2. **探索营 Candy 增量复核**（27KB）：我此前判「观察不立项（增量与族B重叠）」——复核其中半肥猫路演逐字稿+学员方案节是否有真增量（族B卡已覆盖探索营开源文档 9 件，但路演口述层可能未被覆盖），有增量则补 1-2 卡，无则在执行报告写零增量证据
3. W6 三方法前置；与 #610/#611 产出卡互链

## 交付

- 1-3 张卡 + 执行报告（含探索营复核结论证据）
- claim/complete 走 `python 90_control/scripts/queue_transition.py`（complete 624）

## 建模方案（L1 出牌，2026-09-03 老顽童）

组件链：`[素材牌] → [边界牌] → [结构牌] → [过程牌] → [质量牌]`

- **[素材牌 L2 逐字消费]**：两份 candy 逐字稿逐字读完——Live260（190 行/36KB，ROI 搭档+陪练官两段）+ 探索营（548 行/27KB，10篇开源目录/一页纸教程合集/半肥猫路演/马拉松大课案例/GEO 指南五段）
- **[边界牌 L7 查重]**：Live260 方法层已被 #586 双卡覆盖（dk-koupen-decision-tiering-compromise + tool-ai-koupen-training-partner-design，均 reviewed A-）→ 增量=**春节 14 天加课决策完整案例**（dk 卡只有方法结构，无案例全程）；探索营谢翼 MemPalace 段已被 method-obsidian-km-camp 覆盖且该卡明确声明「GEO 指南/半肥猫案例另属题材不在本卡范围」→ 增量=**GEO 一页纸指南**（全库零 GEO 方法卡，industry-ai-cases 仅提及类别）；半肥猫口述层增量评估见执行报告
- **[结构牌 KF-024]**：case 卡=关键数字+证据表+Critique≥2 外部攻击者+失败模式；tool 卡=操作步骤+When NOT to Use+失败模式+判断标准
- **[过程牌 W6 三方法]**：①WebSearch——GEO 国际术语对齐实测（Aggarwal et al. 2023, arXiv:2311.09735, KDD 2024，命名无冲突）；②六层交叉——两素材均为单一来源口述/内部文档，如实降级标注「口述待独立核实」；③九层深挖在卡内执行（业务公式→假设审计→边界→失败模式→隐性成本）
- **[质量牌 门禁]**：逐卡 `kdo pre-submit` → 自攻击 → L12 git status → complete → L9 双验证

### 传播限制判定

- Live260 candy：源文 3 次标注「仅限内部不要外传」→ case 卡按 #322/#586/#611 先例**双标注**（source_context ⚠️ + 正文密级声明），案例抽象化脱敏
- 探索营 candy：全文 grep「外传/内部/密」零命中（L226 唯一「内部」为 mem-input 判断逻辑正文）→ 不触发密级标注，正常引用
