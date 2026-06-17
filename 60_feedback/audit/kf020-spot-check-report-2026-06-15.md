# KF-020 全修验收报告

**验收时间**：2026-06-15  
**验收角色**：王语嫣（代欧阳锋抽检）  
**扫描范围**：30_wiki 全库 1193 张卡片  
**抽检样本**：10 张 enriched/reviewed 状态卡片

---

## 1. KF-020 目标

确保所有 `status ∈ {enriched, reviewed}` 的卡片，`source_refs` 中不再引用 `00_inbox/` 临时路径，全部归档到 `10_raw/sources/`。

## 2. 验收结果

| 指标 | 结果 | 说明 |
|------|------|------|
| KF-020 violations | **0** | 全库 enriched/reviewed 卡已无非归档 source_refs |
| 全库 P0 阻塞问题 | **0** | `kcard-quality-gate.py` 通过 |
| 全库 P1 修复问题 | **0** | 无待处理 P1 问题 |
| YAML 解析错误 | **0** | 无 YAML 语法问题 |

**结论：KF-020 全修验收通过。**

## 3. 抽检详情

随机抽检 10 张卡，结果如下：

| 卡片 ID | status | source_refs 总数 | 指向 00_inbox | 备注 |
|---------|--------|------------------|---------------|------|
| case-纪浩-from-zip-to-five-layers | draft | 2 | **2** | draft 状态，不在 KF-020 约束范围 |
| case-toy-cabinet-business-model | reviewed | 2 | 0 | 已归档 ✅ |
| case-five-step-growth-first-lever | enriched | 2 | 0 | 已归档 ✅ |
| yt-barrier-analysis-cheat-sheet | reviewed | 4 | 0 | 已归档 ✅ |
| case-zhihu-vs-degetao-network-effect | reviewed | 1 | 0 | 已归档 ✅ |
| case-xiaolong-ecommerce-foresight | enriched | 2 | 0 | 已归档 ✅ |
| case-treadmill-demand-analysis | reviewed | 2 | 0 | 已归档 ✅ |
| case-toy-cabinet-barrier | reviewed | 2 | 0 | 已归档 ✅ |
| yt-tool-foresight-canvas | enriched | 5 | 0 | 已归档 ✅ |
| case-shampoo-product-kernel | reviewed | 2 | 0 | 已归档 ✅ |

> 抽检脚本：`python 90_control/scripts/kcard-quality-gate.py` + 自定义抽检脚本交叉验证。

## 4. 发现的改进项（非 KF-020 阻塞）

### 4.1 source_refs 使用 hash 前缀而非完整文件名

黄药师在修复时，将 `source_refs` 写成了 `src_YYYYMMDD_<hash>` 形式（例如 `src_20260610_91556342`），而非完整文件名（例如 `src_20260610_91556342-一堂=一堂五步法-商业模型-线下玩具柜案例.md`）。

- **影响**：引用仍可解析（通过 hash 前缀能唯一定位文件），但可读性和可追溯性下降；依赖 `10_raw/sources/` 目录下无 hash 冲突。
- **统计**：全库约 705 张卡存在 partial source_refs，其中 enriched/reviewed 状态约 130 张。
- **建议**：作为后续任务 **KF-021** 批量补全为完整文件名。

### 4.2 1 张 draft 卡仍引用 00_inbox

- `case-纪浩-from-zip-to-five-layers`（status=draft）仍有 2 条 `00_inbox` 引用。
- 因 status=draft，不违反 KF-020；建议在进入 enriched 前完成归档。

### 4.3 decisions 域 lint 错误

`kdo_lint.py` 当前仍有 **84 errors**，集中在 `30_wiki/decisions/` 域：

- `status` 字段值多为 `draft`，但 decisions 域只允许 `proposed / accepted / superseded`。
- 多张 decision 卡缺少 `decision_date` 字段。

**建议**：作为后续任务 **KF-022**，由黄药师统一修复 decisions 域 frontmatter，使其符合 `kdo_lint.py` 规则。

---

## 5. 下一步建议

1. **KF-020 关闭** — 验收通过，violations = 0。
2. **KF-021** — 批量补全 source_refs 为完整文件名（全库约 705 张卡，可分期处理）。
3. **KF-022** — 修复 `30_wiki/decisions/` 域 lint 错误（84 errors → 0）。
4. **case-纪浩-from-zip-to-five-layers** — 进入 enriched 前补齐 source 归档。

---

**签字**：王语嫣  
**状态**：KF-020 验收通过，建议开启 KF-021 / KF-022。
