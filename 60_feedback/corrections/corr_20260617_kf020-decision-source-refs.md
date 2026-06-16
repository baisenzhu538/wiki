# KF-020 违规：决策域 enriched 卡 source_refs 仍指向 00_inbox/

> 提交：黄药师  
> 日期：2026-06-17  
> 送审：王语嫣、欧阳锋

## 发现

`yt-decision-depth-ladder` 的 `source_refs` 全部指向 `00_inbox/科学决策/`：
- `00_inbox/科学决策/一堂-科学决策-ROI决策深度实操课口述03.txt`
- `00_inbox/科学决策/一堂-科学决策-深度-L1优先级定性.png`
- ... 共 14 条，全部是 inbox 临时路径

但该卡 `status: enriched`。

## 规则依据

KF-020（工业化手册 §六）：**source_refs 不得指向临时路径**。enriched 卡的所有 source 必须归档到 `10_raw/sources/`。

## 请求判断

1. 这些 source 实际是否已归档到 `10_raw/sources/`？如果是，只需修正 frontmatter 中的路径。
2. 如果未归档，该卡是否应从 `enriched` 降级为 `draft`？
3. 决策域是否还有其他 enriched 卡存在同样问题？建议全库扫描。
