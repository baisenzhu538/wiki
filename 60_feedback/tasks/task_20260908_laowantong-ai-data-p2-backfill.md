---
id: task_20260908_laowantong-ai-data-p2-backfill
title: "P2 补强补挂：半肥猫口述回填+两组互链+KDO桥接素材+src_unknown 溯源补挂（合并工单，#682 编排）"
seq: 685
status: queued
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-08
decision_source: 老朱 09-08 19:25 拍板全做（#682 编排）
reviewer: 欧阳锋
instance: laowantong
updated_at: ''
---

# #685 P2 补强补挂单（老顽童）

> 规格源=诊断报告 `60_feedback/diagnosis/diag_20260908_wangyuyan-ai-data-ai-basic-deep-dig.md` §五-P2 表全量。指认落点卡，**不新产卡**；溯源补挂只追加不替换（F-KDO-015）。

## 工作项（8 项，前 4 项补强、5-6 项补挂、7-8 项为终审移交增补）

| # | 素材增量 | 落点动作 | 素材锚点 |
|:-:|:--|:--|:--|
| 1 | 半肥猫口述版标注维度细节+语录（标注密度降幻觉/模型无关性） | 回填 `framework-AI知识库-五阶段演进` + `tool-ban-fei-mao-yaml原子化标注`（只追加口述版增量，不改已有骨架） | 口述01 L414-640（00_inbox/AI-study/AI数据/一堂-AI数据第一课口述01.txt） |
| 2 | 处理8动作三层+黄金测评集 | 与 `concepts/数据标注维度最佳实践调研报告` 互链（related 双向） | 口述02 L1256-1300 |
| 3 | 清单体笔记=人机API（人机最大公约数） | 与 `tool-note-one-line-one-point` 互链（related 双向） | 口述02 L1350-1438 |
| 4 | 闲聊篇 AI使用三循环/默认不依赖记忆/skill-prompt-agent辨析/多Agent文件夹协同 | KDO 实践域桥接素材登记（bridge 候选，写入落点卡的 related 或桥接候选清单，不单独成卡） | 闲聊篇 L210-574 |
| 5 | `concepts/ai数据理解第一课` source_refs=src_unknown | **溯源补挂**：追加 `00_inbox/AI-study/AI数据/AI数据理解第一课表格.md` + `src_20260601_ba8ea2f0` + 口述02（使用五层出处 L1564-1590）；src_unknown 标注 superseded 不删除 | 报告 §2.1/§五-P2 |
| 6 | 马易族 6 数据卡 source_refs=src_unknown | **溯源补挂**：逐卡定位真实上游源追加补挂（与 #5 合并为一个补挂工单执行；逐卡列补挂对照表，找不到实源的如实标注待考，不编造） | 报告 §一 grep 兜底【实证】 |
| 7 | 口述01/闲聊篇归档并挂（#682 终审移交项①：编排单边界声称随本单但原表漏列） | **归档落账**：旧 src `src_20260614_a25ca678` / `src_20260614_64015d4d` 不删，其页面追加标注「干净转写版=00_inbox/AI-study/AI数据/一堂-AI数据第一课口述01.txt / 闲聊篇口述.txt」互挂引用指向 | #682 编排单拍板范围第 7 条 |
| 8 | 徐建新旧卡互挂补双向（#683 终审移交项①：互挂实际单向，旧卡为已审件） | **王语嫣编排授权回填**：旧卡 `case-yitang-xujian-invoice-saas-channel` 的 related 追加 `case-xujian-invoice-data-asset`（只追加不动其他字段，已审件的最小回填） | #683 新卡族 |

## 验收标准

1. 8 项全落；source_refs 只追加不替换（F-KDO-015），旧 src_unknown 标 superseded
2. 回填/互链后落点卡 `kdo pre-submit` PASS，输出随提审附
3. 补挂对照表（卡 id × 新挂 source × 依据锚点）随提审附；马易族找不到实源的卡单列「待考」清单
4. 负向判词附存在性核查锚（宪法第二条）；欧阳锋终审

## 边界

- 不新产任何卡；不动 P0/P1 在产卡（#683/#684）
- 马易族 6 卡若实源确实无法定位，如实标待考交欧阳锋裁定，禁止编造 source
