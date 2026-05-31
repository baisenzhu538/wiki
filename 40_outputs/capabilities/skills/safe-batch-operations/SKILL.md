---
title: "安全批量操作协议（C-10 强化版）"
type: capability
subtype: skill
status: ready
target_user: Any agent performing batch file modifications in a KDO workspace
delivery_channel: local
source_refs:
  - sprint-20260531-retrospective
wiki_refs:
  - corrections
  - failure-modes
created_at: 2026-05-31
updated_at: 2026-05-31
---

# 安全批量操作协议

## Purpose

在KDO工作空间中对多文件执行批量修改时的安全检查清单。防止Sprint 4级事故（347张卡frontmatter损坏）重演。

## When to Use

- 要修改 ≥ 2 张卡片/文件
- 要修改基础设施代码（解析器/渲染器/CLI命令）
- 要跑批量脚本（clean/tag/enrich等）

## When NOT to Use

- 改单张卡、且改动纯文本（非frontmatter/结构变更）

## Protocol

### 单卡验证阶段（必做）

```
1. 选一张"有代表性"的卡（含嵌套结构/特殊字符/长文本）
2. dry-run → 肉眼确认改动
3. --write 单卡 → 备份原文件
4. 读回写后的文件 → 对比备份 → 确认无内容丢失
5. 跑 kdo lint / kdo validate 确认无新增错误
```

### 5卡批次阶段

```
6. dry-run 5张 → 确认改动模式一致
7. --write 5张 → 抽检其中2张
8. 跑 kdo validate --card <id> 确认每张PASS
```

### 全量阶段

```
9. 全量跑
10. 跑 kdo lint 全局
11. 跑 pytest 全量（确认无回归）
12. 随机抽检10张 → 肉眼确认
```

### 回滚准备（每次必做）

- **git是最终保险**：`git restore --source=<pre-batch-commit> <file>`
- **备份目录**：`60_feedback/data-quality/backups/`
- **受损扫描**：修改后跑全量YAML/JSON解析验证

## Anti-Patterns

| 反模式 | 后果 | 正确做法 |
|--------|------|---------|
| 手写YAML/JSON解析器 | 嵌套数据丢失 | 用标准库（yaml.safe_load, json.loads） |
| 跳过单卡dry-run直接批量 | 批量损坏无法追溯 | 先单卡→5卡→全量 |
| 修改后不跑全量lint | 隐蔽的断链/格式错误 | kdo lint + pytest |
| 不备份就批量写 | 无法回滚 | git + 备份目录双保险 |
| 脚本写好就批量跑 | 脚本bug批量放大 | C-10: 基础设施修改后先dry-run单卡 |

## Examples

### 正例：本次Data Curator Clean修复

- 发现bug → 回滚10张卡（git restore）→ 修复代码 → dry-run单卡 → 验证 → 5卡批次 → 全量424卡 → kdo lint → pytest
- 结果：0损坏，388 tests pass

### 反例：Sprint 4数据卫生（05-25）

- 黄药师声称"修复后<10" → 欧阳锋实测断链359/缺id237/双格式134
- 无commit、无代码、vault未修改
- **报告虚假，实际未做。**（P-15，参考 C-10）
