---
id: task_20260908_huangyaoshi-ai-data-domain-infra
title: "基建：ai-data-domain-digest 补建 + 本域散卡注册 domain-mapping + 双三角AI数据重复卡去重（#682 编排）"
seq: 686
status: in_progress
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-08
decision_source: 老朱 09-08 19:25 拍板全做（#682 编排）
reviewer: 欧阳锋
instance: huangyaoshi
updated_at: '2026-09-08T12:58:25.925054+00:00'
---

# #686 黄药师基建单：AI数据域 MOC 补建 + 注册 + 重复卡去重

> 规格源=诊断报告 `60_feedback/diagnosis/diag_20260908_wangyuyan-ai-data-ai-basic-deep-dig.md` §〇（MOC 先行结论）+ §五-基建缺口登记【实证】。

## 背景（存在性核查锚，报告已实证）

- AI数据域 digest **缺失**：`30_wiki/domains/` 14 张 digest 无该域；`90_control/domain-mapping.md` 未注册；5 张 MOC 均不覆盖；相关卡散挂 ai-collaboration/kdo/yihang 域下
- **重复卡实锤**：`case-yihang-dual-triangle-AI数据.md` 与 `case-yihang-dual-triangle-AI三角-数据.md` 双卡同图源（`00_inbox/人机协作双三角/AI数据.png` 两次 VLM 提取）

## 工作项（3 项）

1. **ai-data-domain-digest 补建**：`30_wiki/domains/ai-data-domain-digest.md`，骨架参照 `30_wiki/domains/ai-basic-domain-digest.md`；资产路标覆盖本域现有散卡（concepts×2/tool×7/case×3/article×1，清单见诊断报告 §五-基建缺口登记）+ 在产新卡族（#683 P0 八张，产毕后回填路标可二次补）
2. **domain-mapping 注册**：本域 12+ 散卡注册进 `90_control/domain-mapping.md`（ai-data 域条目新建），同步 `30_wiki/index.md` digest 索引
3. **重复卡去重合并**：`case-yihang-dual-triangle-AI数据` vs `case-yihang-dual-triangle-AI三角-数据` 合并为一卡——保留信息更全者为主卡，另一卡做 redirect/合并标注；两卡全部被引处（grep related/source_refs）改指主卡；source_refs 只追加不替换（F-KDO-015）

## 验收标准

1. digest 骨架与 ai-basic-domain-digest 同构；`kdo pre-submit` PASS
2. domain-mapping 注册后 `kdo query` 该域可召回 digest
3. 去重合并后 grep 全库无指向被并卡的死链（`check_dead_links.py` 或 grep 复核）
4. 基建改动先单卡 dry-run→单卡 write→验证→再批量（F-KDO-013）；批量写入需人工批准（F-KDO-014）
5. 欧阳锋终审

## 边界

- 只做基建/注册/去重，不做内容判断与卡片正文改写（内容归老顽童/欧阳锋）
- #683 在产新卡的路标回填可等 P0 终审后二次补，本单先注册存量散卡
