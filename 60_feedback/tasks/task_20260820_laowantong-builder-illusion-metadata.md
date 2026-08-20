---
id: 388
assignee: hermes
status: reviewed
title: 元数据遗留 warning 清理（#385/#386 终审另立项合并）
priority: P3
dependency: []
updated_at: '2026-08-20T04:45:34.245607+00:00'
reviewed_by: 欧阳锋
review_date: '2026-08-20'
grade: A
---

# #388 元数据遗留 warning 清理（#385/#386 终审另立项合并）

## 来源

两个终审各留一条同类尾巴，合并处理（均为历史遗留 frontmatter 元数据问题）：

**#385 终审遗留**——`dark-knowledges/dk-ai-builder-illusion.md`：
1. tags 缺 audience / scene 维度
2. source_refs 指向 pending_archive 不可达路径

**#386 终审遗留**——2 张 yt-* 卡缺 `updated_at`（pre-submit ERROR，#386 边界"frontmatter 零改动"故未补）：
3. `yt-model-questioning-practice-canvas.md` 补 updated_at
4. `yt-personal-thinking-models.md` 补 updated_at

## 任务目标

清理上述 4 项，相关卡 pre-submit 0 ERROR 且 warning 清零。

## 执行范围

1. **tags 补 audience/scene**（builder-illusion）：从卡正文推断合适取值；推断不出宁可少标不瞎标（O0）
2. **source_refs 修正**（builder-illusion）：先查 pending_archive 实际位置/真实素材路径——若素材在 10_raw 或 00_inbox 有真实路径则改指真实路径；若素材确实不存在，source_refs 标注"原始素材待补"而不是留死路径
3. **updated_at 补齐**（2 张 yt-* 卡）：用补正当日日期，只加这一个字段（同 #385 模式）
4. 顺手全库扫一遍同类 warning（tags 缺维度 + source_refs 不可达 + 缺 updated_at），若量小（≤5 卡）一并修，量大则只出清单不扩scope

## 边界

- 只动 frontmatter 元数据，正文零改动
- 改前 diff 预览（批量三问）
- pre-submit 0 ERROR；diff 贴执行报告
- 欧阳锋随下批 spot-check 复终审

## 内容价值判断（PROTOCOL §7 合规声明）

- 仅元数据修正，无删除/移动

## 验收标准

1. dk-ai-builder-illusion pre-submit warning 清零
2. source_refs 指向真实可达路径或明确"待补"标注
3. 同类 warning 扫描结果入报告（修或列清单）

## 交付

1. diff + pre-submit 输出 + 同类扫描结果
2. 送欧阳锋终审（随下批 spot-check）

---

## 执行报告（2026-08-20 老顽童 hermes 实例）

### 完成概要
4 项元数据遗留清理完成（#385/#386 终审另立项合并），pre-submit **✅ PASS 3/3（0 ERROR，warning 清零）**。

### 修复明细
| # | 卡 | 修复 |
|:--|:--|:--|
| 1 | dk-ai-builder-illusion | **tags 补全**：audience:executor / audience:manager / scene:product-planning / skill-level:intermediate（从卡正文推断：受众=AI 做产品/创业者，场景=产品规划/市场验证） |
| 2 | dk-ai-builder-illusion | **source_refs 修正**：2 条 pending_archive 死路径 → `src_unknown`（标准待补标记）；前 2 条真实路径保留（00_inbox/AI前哨站第2集/ 已实查存在）；出处信息正文原始表述节已保留不丢 |
| 3 | yt-model-questioning-practice-canvas | 补 `updated_at: '2026-08-20'`（同 #385 模式） |
| 4 | yt-personal-thinking-models | 补 `updated_at: '2026-08-20'` |

### 同类扫描结果（全库，量大出清单不扩 scope）
| 类别 | 数量 | 说明 |
|:--|:--|:--|
| 缺 updated_at | 16 张 | 如 concept-streaming-extraction-pattern / dk-yb19 等——建议另立项批量补 |
| tags 缺 audience/scene | 739 张 | 历史卡大量缺 tags 维度——建议按域分批立项（如 batch-frontmatter-backfill skill 流程） |
| source_refs pending_archive 死路径 | 189 张 | 如 case-gudong-tea-shop-foresight / case-milktea-five-step 等——建议另立项统一改 src_unknown |

### 验证
- pre-submit ✅ PASS 3/3：YAML/WIKILINK/DOMAIN/DK_SECTION/OUTLINK/ALIASES/POSITION/SOURCE_REACHABILITY 全 0（kdo index 已重建）
- 只动 frontmatter 元数据，正文零改动

### 待欧阳锋
- 随下一批 spot-check 复终审
- 3 类遗留清单（16/739/189）建议按域分批立项

---

## 欧阳锋终审（2026-08-20 · 元数据修复抽查）

**裁定：PASS A。**

**O3 验证**：
- dk-ai-builder-illusion tags 补全 4 维度（audience×2/scene/skill-level）✓
- source_refs 修正：2 条真实路径**实查存在**（00_inbox/AI前哨站第2集/）+ 2 条 src_unknown 标准待补标记 ✓
- yt 两卡 updated_at 补 2026-08-20 ✓ / pre-submit 实测 3/3 ERROR 0 ✓ / 正文零改动 ✓

**边界纪律加分**：同类扫描出清单不扩 scope（缺 updated_at 16 / tags 缺维度 739 / pending_archive 死路径 189——三类建议按域分批立项）——修复者知道"清单是弹药不是本单任务"。
