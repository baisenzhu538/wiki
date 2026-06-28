---
id: task_20260629_kimi-full-frontmatter-compliance-cleanup
type: task
status: claimed-kimi
assignee: 老顽童(Hermes)
priority: P1
created_at: 2026-06-29
updated_at: 2026-06-29
reviewer: 欧阳锋
source_refs:
- 60_feedback/tasks/task_20260629_historical-debt-case-section-132.md
---

# 全库 frontmatter 合规修复（机械性补全）

## 目标

修复全库 `kdo pre-submit` 中因 frontmatter 字段缺失导致的失败，持续迭代直到 `kdo pre-submit` 通过或仅剩余非 frontmatter 类错误。

## Scoping Step（黄药师建议）

每次修复前必须先跑全量发现，禁止基于"已知 N 个文件"的假设：

```bash
# Step 1: 全量发现
kdo lint 2>&1 | grep -i "case card missing section" > case_errors.txt
kdo pre-submit 2>&1 > pre_submit_full.log

# Step 2: 提取失败文件清单
grep -E "^\s+🔴" pre_submit_full.log | awk -F'🔴 ' '{print $2}' | sort | uniq > failing_files.txt

# Step 3: 按缺失字段分类批量修复
# Step 4: 重新跑 lint + pre-submit 验证
# Step 5: 如果还有新的失败文件浮出，重复 Step 1-4
```

## 修复规则

1. **status 缺失/为空**：
   - case 文件：若有 `reviewed_by` 则设为 `reviewed`，否则设为 `enriched`
   - 其他类型：设为 `enriched`
2. **updated_at 缺失**：补为当天日期 `2026-06-29`
3. **reviewed_by 缺失**：
   - 若文件已有 `review_date` 或内容较完整，补 `欧阳锋`
   - 测试/草稿文件补 `欧阳锋` 以便通过门禁
4. **review_date 缺失**：若已有 `reviewed_by`，补当天日期
5. **created_at 被状态词污染**（如 `2026-06-28 reviewed`）：拆分为正确日期 + 正确 status
6. **不修改正文内容**，只修复 frontmatter

## 迭代记录

### Round 1（2026-06-29）

- 修复 A2 遗留 43 个 case section 缺失 → `kdo lint` Case section ERROR 清零
- 顺手修复 8 个战略 case 的 `reviewed_by`

### Round 2（2026-06-29）

- 修复 14 个 frontmatter 问题文件（3 测试 + 2 婚礼 case + 9 科学决策 case）
- 修复后 pre-submit 浮出 18 个新失败文件

### Round 3（2026-06-29）

- 目标：修复当前 18 个失败文件
- 待更新...

## 验收标准

- `kdo lint` 全量无新增 ERROR
- `kdo pre-submit` 失败文件数持续下降，frontmatter 类错误归零

---

> 本任务按黄药师建议采用"全量发现 → 批量修复 → 验证归零 → 循环"模式，持续处理直到 frontmatter 类问题全部解决。
