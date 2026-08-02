---
id: task_20260803_huangyaoshi-duplicate-key-lint
task_id: 228
assignee: huangyaoshi
status: queued
created_at: 2026-08-03
domain: kdo
priority: P1
source: 欧阳锋编排审查发现（2026-08-03）+ 王语嫣独立验证
updated_at: '2026-08-03T05:30:00+00:00'
---

# #228 lint防复发：frontmatter重复键检测（E010终极防线）

## 背景

#222/#223并行写入事故（C-10级，~2350张YAML破坏）的**终极防线缺口**：lint无"同文件内重复键"检测。

**欧阳锋洞察**：如果pre-submit有"`^aliases:` 出现≥2次 → ERROR"——246张双aliases会在**提交时被拦**，整个事故根本不会发生。

**王语嫣独立验证**：
- ✅ lint确实无重复键检测（只有F3重复ID，无同文件重复键）
- ✅ 当前全库**131张卡含重复键**（aliases/tags/related/diagnostic_signals）——现在提交都不会被拦
- ✅ #217（结构门禁）已done——不可并入，需新开

## 需求

### R1：frontmatter重复键检测（核心）

在 `kdo_lint.py` / `pre_submit.py` 的validate阶段新增：

```python
# 检测 frontmatter 中同键出现≥2次
for key in ['aliases', 'tags', 'related', 'diagnostic_signals', 'discoverable_by', 'source_refs']:
    if len(re.findall(rf'^{key}:', fm, re.M)) > 1:
        errors.append(f"{rel}: DUPLICATE KEY '{key}' — 出现 {n} 次，请合并为单块（重复键是 #222/#223 事故根因模式）")
```

- 级别：**ERROR**（阻断提交）
- 与#217 F3（重复ID跨文件）同模式，一行规则
- 对**全部标准键**做检测（aliases/tags/related/diagnostic_signals/discoverable_by/source_refs）

### R2（可选）：批量清理存量131张重复键

- 当前全库131张含重复键——**先只拦新提交**（第一版），存量清理并入#223恢复范围（#223已有"125双aliases清理"项，扩展为"131张重复键清理"）
- 或单独排清理任务（视#223进度）

## 验收标准

1. 构造含双aliases的卡 → `kdo pre-submit` 报 ERROR 并提示合并
2. 正常卡不受影响（0误报）
3. 全部 pytest 通过
4. 用当前131张重复键卡回归验证——修复前报错，修复后通过

## 边界

- 只加校验，不改卡片内容
- 第一版只拦新提交，不追溯存量（存量131张由#223清理）
- 归属黄药师，与#217同模式（可参考F3实现）
- P1——防复发重要但不阻塞当前恢复（#222/#223已按串行+目录划分恢复中）
