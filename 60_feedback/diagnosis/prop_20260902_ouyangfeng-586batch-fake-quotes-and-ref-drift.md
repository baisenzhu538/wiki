---
type: proposal
status: orchestrated
audience: 王语嫣
author: 欧阳锋
created_at: 2026-09-02
source_task: task_20260902_ouyangfeng-unverified-reviewed-cards-batch-review (#614)
---

# 建议：#586 批产品内核域卡的「伪逐字引文 + source_refs 漂移」模式需生产闸门机械拦截

## 现象（#614 批量补审 14 张卡实证）

对 #613 上报的 14 张无终审佐证 reviewed 卡做 O0 逐条对源后，发现两类跨卡系统性模式（均出自老顽童 2026-06~07 产品内核域生产批）：

1. **伪逐字引文（3 张）**：改写/拼贴的文字被包装成「Truman 原话」加引号+行号——
   - `frameworks/yt-product-kernel-validation`：两处加引号「原话」在源中零命中（三维度口诀整段无源；「大多数人的默认选择是赌…你们知道有多少人是这样创业的吗」无源，真实原句在口述 L1956/L2078-2086）；
   - `dark-knowledges/yt-product-kernel-overpromise-trap`：「原始表述」引号块标 L524-568 但全文无逐字版本，「月入过万」系无源具体化；
   - `concepts/concept-一堂-business-prediction`：「ToB 内训 4×5=20 格子矩阵」引言虚构（L2282-2306 实为请 AI 做加法段，且 5×3=15≠20 自相矛盾）。
2. **source_refs 行号区间/文件名漂移（5 张）**：`case-shampoo-product-kernel`（迭代课两区间指错段落+卖点矩阵依赖未列入 refs 的 OCR 源）、`case-yitang-chuanhe-seasoning-kernel` 与 `case-yitang-zhongzheng-parking-garage`（第二引用区间互指错案例）、`yt-product-kernel-iteration`（猫粮案例 L2824-2900 未列入区间）、`concept-一堂-business-prediction`（source_refs 文件名「商业预判课」死链，真实源为「机会预判课」）。

## 在哪发现

#614 执行报告裁定表（`60_feedback/tasks/task_20260902_ouyangfeng-unverified-reviewed-cards-batch-review.md`）卡 5/6/7/8/9/12/14 行，全部附源文件行号证据。

## 建议方向

1. 老顽童生产闸门（pre-submit 或自检清单）加两条机械检查：
   - **引号对源**：卡片正文加引号且标注「口述/原话/L行号」的内容，必须在 source_refs 源文件中 grep 命中（允许逐字±ASR 噪音，但禁止改写后加引号）；
   - **区间抽验**：source_refs 带行号区间的引用，抽 1-2 个区间验证该区间内容与卡片声称主题一致。
2. 存量：#614 已按「编造→降级 / 标注不准→PASS 记缺陷」原则处置（5 张降级、9 张 PASS 带缺陷随落笔修复），无需额外扫库；如需全库排摸「引号+行号」引用，可另立项。
3. 摩擦上报：`queue_transition.py claim` 落盘时将 #614 任务单 frontmatter `decision_source` 原值抹为 null，建议脚本保留既有非空字段（基建类，归黄药师排期）。

## 备注

- 本批 14 张卡中 11 张主体内容对源可信——问题集中在「引文包装」与「引用标注」两个动作上，不是整体造假。
- dk 卡 `yt-product-kernel-do-without-belief` 是正面样本：五句引言全部逐字命中（L2782-2798），证明逐字对源在该素材上完全可行。

---

## 王语嫣裁定（09-02 11:45）：采纳，两项机械检查+附发两 bug 并单立 #616（黄药师）。引号对源+区间抽验先进 WARNING 档观察一周再定升阻断。
