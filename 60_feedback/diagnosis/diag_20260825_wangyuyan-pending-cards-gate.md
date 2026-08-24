---
id: diag_20260825_wangyuyan-pending-cards-gate
title: pending-cards 待编排区门禁判定（2 张 wechat 偶遇卡）+ 正式卡 frontmatter 异常观察
type: diagnosis
status: done
author: 王语嫣
audience: 王语嫣
date: 2026-08-25
---

# pending-cards 门禁判定（2026-08-25 王语嫣）

> 背景：老朱令「检查还有什么未编排」。待编排区（`00_inbox/pending-cards/`）残留 2 张，逐张过门禁（E037 三步走：判定→隔离→git 固化）。

## 判定明细

### 1. case-wechat-2404c1658025473c（柠檬市场×信任三要素）→ **合并（superseded）**

- **同构映射（W8 先查已有卡）**：同源素材（`src_wechat_2404c1658025473c`）已由老顽童 08-20 编译为正式卡 `30_wiki/frameworks/framework-lemon-market-new-brand-trust`（status: pending_review，confidence 0.85，已入 index）。
- **覆盖比对**：草稿卡全部要素（阿克洛夫柠檬市场/信任三要素=能力+善意+可预测性/触点一致性乘法公式/行动三件事）= 正式卡标题即公式本身，全覆盖无增量。
- **判定**：`status: superseded`，`superseded_by: framework-lemon-market-new-brand-trust`，移 `_processed/`。

### 2. case-wechat-fe60439837f4c93e（PDF 解析工具）→ **维持原判（superseded）**

- 2026-08-21 我已判定合并入 `tool-pdf-inspector`（明细：`diag_20260821_wangyuyan-pdf-inspector-gate.md`），但文件滞留待编排区未隔离——本次补隔离动作（移 `_processed/`），判定不变。

## 副产观察（最小建议书，#460 三行式）

- **现象**：正式卡 `framework-lemon-market-new-brand-trust` frontmatter 结构异常——`source_context` 键重复两次、条目三段重复（同内容×3）。
- **在哪发现**：本次门禁比对读卡时发现（块标量/重复键=老顽童 YAML 格式边界家族病，风清扬晚间审计 F3 同族）。
- **建议方向**：该卡 pending_review 中，欧阳锋终审时一并核 frontmatter；存量同类（重复键）可挂 #512 黄药师存量清理顺带扫。

### 副产观察 2（桥接缺口）

- **现象**：`framework-lemon-market-new-brand-trust` 的 related/关联节未链接 `framework-一堂-转化率黑客-总纲` 与 `framework-一堂-触点本质论`——两卡实质同域互补（信任公式=转化率「阻力」维度的信任子模型 + 触点维度的质量属性），见本次会话王语嫣对老朱的关系解说。
- **建议方向**：该卡 pending_review 中，欧阳锋终审时补 related 桥接（不改内容主体，仅补链）。

## 处置动作

- 两卡 git mv → `00_inbox/pending-cards/_processed/`（00_inbox 只增不删=不删除，隔离到已处理子目录）
- 待编排区清零
