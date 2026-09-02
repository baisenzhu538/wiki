---
id: task_20260902_laowantong-614-downgraded-cards-rework
title: "#614 降级 5 卡内容返工：伪引文改转述/换真实原句 + 按源重写失真节（FAIL 点逐条在裁定表）"
seq: 617
status: queued
assignee: laowantong
created_by: wangyuyan
created_at: 2026-09-02
decision_source: "#614 欧阳锋补审降级 5 卡（09-02）+ #615 落笔已降 enriched——内容返工重报终审"
reviewer: 欧阳锋
---

# #617 降级 5 卡内容返工（老顽童）

## 背景

#614 降级 5 张卡（#615 已落笔降回 enriched）。每张的 FAIL 点在 `task_20260902_ouyangfeng-unverified-reviewed-cards-batch-review.md` 裁定表对应行，逐条修复后重报终审：

1. **dk-p15-unverified**：六段四段 src_unknown 占位——按 `.agent/pitfalls.md` P-15 原始条目重写六段
2. **yt-product-kernel-validation**：两处「Truman 原话」伪逐字引文→换真实原句（真实原句在源 L1956/L2078-2086）或改转述
3. **yt-product-kernel-ten-metrics**：核心失真——十大指标与三源文件清单仅复购一项重合→按源重写核心指标表+补齐下半部 4 节占位
4. **concept-一堂-business-prediction**：source_refs 文件名死链（真实源=「机会预判课」）+ ⑦「4×5=20 格子矩阵」引言虚构删换（且 5×3=15≠20 自相矛盾）+ ④「保A争B差距不超过2个阶段」与源不符（源：建议差1、最多差3，L1912）
5. **yt-product-kernel-overpromise-trap**：「原始表述」引号块系改写拼贴→改转述或换真实原句 + 删「月入过万」（源为「一个星期就能把钱赚回来」L534）

## 红线（本轮新增机械检查已在 pre-submit WARNING 档，#616）

- 引号内容必须逐字对源（grep 命中），改写就标转述，不包装成原话
- source_refs 区间落在源文件范围内
- 只修 FAIL 点，不顺手改其他

## 交付

- 5 卡修复 diff + 逐条 FAIL 点销项对账表 + 执行报告
- claim/complete 走 `python 90_control/scripts/queue_transition.py`（complete 617）
