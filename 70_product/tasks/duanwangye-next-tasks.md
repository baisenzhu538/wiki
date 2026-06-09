# 段王爷后续任务（临时）

> 临时任务：熟悉 KDO 新基础设施管线（produce → validate → ship 闭环）。
> 做完后回归发布本职工作。

---

## ?? 发布预备 + 交付审计

### 任务 1：50_delivery/ 发布审计

审计现有发布记录的完整性：

1. 检查每条发布记录是否有对应的 `kdo validate` 状态
2. 检查缺失的 `delivery-manifest.yaml`
3. 补全缺失项

### 任务 2：产品内核域发布预备

根据产品内核 5 课的预期产出（concept + skill + case + dk），预先建立每条产出的发布清单：

- 目标渠道（wiki / 飞书 / 其他）
- 交付 manifest 骨架
- 预期的 validate 门禁标准

### 验收

- 50_delivery/ 现有记录全部补全交付 manifest
- 产品内核域发布预备清单完成
- 全部完成后通知欧阳锋审查
