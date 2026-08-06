---
id: task_20260806_huangyaoshi-domain-cleanup-final
task_id: 240
assignee: huangyaoshi
status: queued
updated_at: 2026-08-06
domain: system
priority: P2
---

# #240 域名收尾：中文域语义查重 + 残留清理

## 背景

#239 交付后王语嫣独立扫描（E017 教训：排除字段名误读）确认：非标准英文域 0 ✅，但发现 3 项待收尾项。

## 收尾项（裁定）

### 1. 23 个中文域语义查重（王语嫣裁定：保留 + 查重）

中文域不是无条件保留——**逐一检查与已有英文域是否语义重叠**：

| 检查项 | 处理 |
|:--|:--|
| 语义重叠（如"产品"vs `product`、"团队"vs `management`、"泛产品设计"vs `panproduct`、"认知"vs `modeling`/`decision-science` 等） | **合并到英文域**（防止 MOC 聚合再次分裂） |
| 语义独立（如"心理学"、无英文域对应） | **保留 + 登记中文域例外白名单**（写入 MOC 模板的系统卡或工业化手册） |

输出：一张对照表（23 个中文域 → 合并目标 / 保留+理由），脚本列出卡清单，人工判断归属（同 #239 粘连拆解纪律：宁可不改，不可猜错）。

### 2. 粘连残留：`learning-methodology- 中文`（1 张）
按 #239 粘连拆解纪律处理（看卡内容归 learning-methodology 或中文域）。

### 3. 下划线占位：`src_unknown`（9 张）→ 统一为 `src-unknown`
格式对齐（#237 口径：kebab-case）；值本身仍属占位单列跟踪（不填真实域）。

## 执行纪律

同 #237/#239：dry-run → git diff → yaml.safe_load ≥99% 才 apply；串行；#228 重复键护栏。

## 验收标准

1. 中文域对照表产出（23 项：合并/保留 + 理由）
2. 语义重叠的中文域清零；独立中文域登记白名单
3. 粘连残留归零；src_unknown 下划线归零
4. yaml 全库 ≥99%；lint 0 新增 ERROR

## 依赖 / 边界

- #239 reviewed 后启动（串行）
- **不阻塞 #238**（design MOC 聚合不受中文域影响——design 域纯英文干净；但 #238 建卡时须引用中文域白名单，标注例外）
- 白名单登记位置：`90_control/` 或 MOC 模板系统卡（黄药师定，建议对齐 decisions.md 记录）
