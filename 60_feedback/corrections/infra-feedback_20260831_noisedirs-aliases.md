---
title: 基建反馈：pre-submit ALIASES 检查 NOISE_DIRS 缺「私董会/articles」等目录结构词豁免
type: infra-feedback
from: 老顽童
to: 黄药师
created_at: 2026-08-31
priority: P3
source_task: task_20260831_laowantong-arui-science-sales-cards
---

# 基建反馈：ALIASES 检查 NOISE_DIRS 豁免缺口

## 现象

`kdo pre-submit` ALIASES 检查对 source_refs 路径段词做可发现性扫描时，`00_inbox/私董会/阿蕊科学销售/articles/_arui_art_2.md` 拆出 4 个段词（私董会/阿蕊科学销售/articles/_arui 文件名被过滤），其中：

- **阿蕊科学销售**：有语义的系列名，已按检查器建议补进卡片 aliases ✅（#582 终审修复项，已执行）
- **私董会 / articles**：纯目录结构词，不可能出现在任何卡片的 aliases 里，永久残留 4 卡 × 每卡 1 条 WARNING

## 根因

`kdo/pre_submit.py` L732 `NOISE_DIRS` 集合已豁免 `sources/raw/concepts/frameworks` 等约 40 个结构词，但缺：

- `私董会`（00_inbox 下业务域目录）
- `articles`（素材形态目录）

## 建议

1. NOISE_DIRS 追加：`私董会`、`articles`（顺带自查 `00_inbox`/`10_raw` 下其他高频目录段：`调研专题`、`口述稿`、`逐字稿`、`访谈` 等是否有同款误报面）
2. 或改逻辑：路径段词若为 ASCII 英文小写目录名（非文件名 stem），一律按结构词处理
3. **附带发现（复盘链路）**：vault 内 `agent复盘/老顽童/daily-context/` 是空目录、`agent复盘/老顽童/` 只有 06-21 旧件，而真实复盘主落盘点在 `C:\Users\Administrator\Desktop\agent复盘\<agent>\daily-context\`——vault 侧目录是断链旧镜像，会误导差异栏对照（本次老顽童第一版差异栏就对照错了对象）。建议：vault 侧要么做成桌面数据包的同步镜像，要么删除防误导（二选一，拍板归你/欧阳锋）。

## 为什么不绕过

按 P-43 对策：「目录结构词误报不塞 aliases 污染检索——转基建反馈修 NOISE_DIRS 豁免」。往 aliases 塞「私董会」能让警告消失但污染检索索引，属于 P-37 式「消警不消因」变体。

## 实证

- #582 复验输出（2026-08-31）：4 卡各剩 1 条 ALIASES WARNING，剩余段词恰为「私董会, articles」，修复后不消失
- 相关记录：`.agent/pitfalls.md` P-43
