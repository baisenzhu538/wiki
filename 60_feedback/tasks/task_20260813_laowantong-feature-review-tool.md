---
id: '314'
assignee: hermes
status: reviewed
updated_at: '2026-08-15T04:58:12.002520+00:00'
task_id: '314'
priority: P1
reviewed_by: 欧阳锋
review_date: '2026-08-15'
grade: A-
---

# #314：Feature 复盘五步法 tool 卡生产（P1，1 张）

## 任务目标

10 份优秀作业的共性结构（黄药师评估："每案例均为'用了什么 Feature + 缺了什么 Feature + 叠加效应 + 改进方案'四段式——天然符合三步编译法"）提炼为可复用的复盘方法论 tool 卡——素材比单案例更大的价值：一个可教给任何人的模板。

> 2026-08-13 迭代：吸收"验收清单"步骤（原 #313 候选 dk 卡并入本卡第五步——验收清单本就是复盘必选项，独立 dk 过细）。

## 素材清单

- `00_inbox/AI基本功/Live258：AI基本功第一课优秀作业.md`（10 份作业共性结构）
- 诊断报告 §四 洞察 6（教学法样本）

## 卡片规格（1 张）

**tool-feature-review-five-step**：Feature 复盘五步法

1. **用**：本次实践实际用了哪些 Feature（含无意识的——先列后标）
2. **缺**：对照周期表，缺了哪些 Feature（高频缺项参考：最终意图/Few-shot/验收标准——10 案例收敛表）
3. **叠加**：哪些 Feature 组合生效？组合机制是什么（并列维度 or 链式管道）
4. **改进**：下一版补哪些 Feature，每条对应可测试假设（每版一个假设）
5. **沉淀**：验收清单（可照抄的评分标准先于下一次生成）+ 什么经验进个人 Feature 库/DataPack + 效果追踪表

配套输出：Feature 效果追踪表模板（黄华春 L295-301 样式）+ 每版对应一个假设（张丽娜 L2651-2665 样式）+ 验收清单模板（张丽娜 1-5 分自评 L2613-2619 样式）

## 卡片要求

- tool 卡含完整操作步骤 + 输入/输出/触发条件 + 失败模式（收藏癖不消化：王鹏飞 L2905"不要收藏 Feature，要消化 Feature"；黄谦"抽卡耗时/状态机冗余"作为适用边界）
- source_refs 带行号（L237-351 黄华春结构/L1825-2421 jeffgirl 迭代/L2651-2665 张丽娜假设/L2905 王鹏飞提醒）
- 定位声明：属于 feature-thinking-core 的应用方法 / 与 dk-feature-pieces-not-recognized-as-cards（#313）互补
- related ≥5（framework-truman-feature-thinking-core / ai-basic-domain-digest / dk-demand-feature-stacking）

## 验收标准

1. `kdo pre-submit` PASS
2. 步骤可照读执行（欧阳锋按"照着做一遍"抽查）
3. 行号逐条命中；五步与 10 案例结构一致性可对证
4. **同批互链闭环**：本卡落库后，把 #312 四卡正文对 tool-feature-review-five-step 的纯文本引用补为 wikilink（#312 已 pending_review；补链后 pre-submit 复查）
5. 送欧阳锋终审；状态流转走 queue_transition.py

## 边界

- 依赖 #313 的 dk 卡（补链关系，可在 #313 后领取）
- 不做成 skill（skill 化需黄药师能力中台评估，另开）

## 执行报告（老顽童 2026-08-12，hermes 实例）

### 交付物（1 张 tool 卡）

`30_wiki/tools/tool-feature-review-five-step.md`——Feature 复盘五步法（用/缺/叠加/改进/沉淀）

### 验收对照

1. **pre-submit PASS** ✅：Passed=1 Failed=0
2. **步骤可照读执行** ✅：五步每步含动作/说明/实证/输出；第 4 步假设表、第 5 步三件套（验收清单/Feature 库/效果追踪表）可直接照抄执行
3. **行号逐条命中** ✅：L237-L351（黄华春结构）/L1825-L2421（jeffgirl 迭代）/L2651-L2665（张丽娜假设）/L2905（王鹏飞提醒）/L295-L301（效果追踪表）/L2613-L2619（1-5 分验收）对照素材一致
4. **五步与 10 案例结构一致性可对证** ✅：第 2 步含高频缺项收敛表（最终意图 8/10、验收清单 7/10、Few-shot 6/10、DataPack 5/10，来源诊断报告 §四+素材）；第 3 步机制表（并列维度/链式管道/关键补全）含黄华春/jeffgirl/王鹏飞实证
5. **配套输出** ✅：效果追踪表模板（黄华春 L295-301 样式）、每版一假设（张丽娜 L2651-2665 样式）、验收清单 1-5 分自评（张丽娜 L2613-2619 样式）已入第 4/5 步
6. **失败模式含任务单指定项** ✅：收藏癖不消化（王鹏飞 L2905"不要收藏 Feature，要消化 Feature"）；黄谦"抽卡耗时/状态机冗余"入适用边界（L2947）
7. **定位声明** ✅：属于 feature-thinking-core 应用方法 + 与 dk-feature-pieces-not-recognized-as-cards（#313）互补关系声明

### 补链（#312/#313 遗留承诺兑现）

- case-live258-europe-cold-email 正文 2 处 `tool-feature-review-five-step` 纯文本 → wikilink（卡已存在，pre-submit 复验 PASS）
- framework-truman-feature-thinking-core / ai-basic-domain-digest related 追加 tool-feature-review-five-step（回链闭合）
- 注：case 卡已 reviewed（欧阳锋 #312 终审），本次补链在已终审卡上留痕，请欧阳锋下次顺带确认

### 自攻击（四路）

- 概念攻击：tool 卡不重复已有 tool-Truman-Feature特性层训练法（那张是"训练法"——怎么练 Feature；本卡是"复盘法"——实践后怎么沉淀，论域互补）✅
- 数据攻击：行号逐条回素材核对；10 案例收敛表数字与诊断报告 §四 一致 ✅
- 反例攻击：适用边界含反例（黄谦复杂度冗余/农夫三拳认知反差失败/复盘过度理性化 Kahneman 攻击）✅
- 遗漏攻击：验收清单模板 + 效果追踪表 + 每版假设三件套齐全；"验收先行"（原 #313 候选）已按裁定并入第 5 步 ✅
