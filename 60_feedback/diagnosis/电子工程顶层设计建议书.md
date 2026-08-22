# 电子工程资料整理方案 - 顶层设计建议书

## 文档元信息

| 字段 | 值 |
|-----|-----|
| 文档版本 | 1.0 |
| 目标读者 | AI Agent（Codex / Claude Coding / 代码生成 AI） |
| 文档类型 | 顶层架构设计 |
| 最后更新 | 2026-06-05 |

---

## 1. 问题定义

### 1.1 现状描述

| 属性 | 值 |
|-----|-----|
| 资料规模 | 1-10 GB，1000-10000 个文件 |
| 来源 | 离职电子工程师遗留 |
| 质量状况 | 正确版本与混乱版本混杂 |
| 可咨询人员 | 无 |

### 1.2 文件类型清单

```
原理图: .sch, .SchDoc, .dsn, .kicad_sch
PCB:    .brd, .PcbDoc, .kicad_pcb, .pcb
固件:   .hex, .bin, .elf, .c, .h
BOM:    .xlsx, .xls, .csv, .bom
文档:   .pdf, .docx, .txt, .md
```

### 1.3 混乱类型（必须检测的 6 类问题）

| 类型 | 检测条件 | 证据要求 |
|-----|---------|---------|
| 同名不同内容 | 相同文件名，MD5 不同 | 列出所有路径和 MD5 |
| 版本号矛盾 | 文件名版本 ≠ 内部声明版本 | 两个版本值对比 |
| 时间线异常 | 固件编译时间 < PCB 修改时间 | 具体时间戳 |
| 配套缺失 | 有 sch 无 pcb，或有 pcb 无 bom | 缺失项明确 |
| 重复文件 | MD5 完全相同 | 所有副本路径 |
| 孤儿文件 | 无法匹配任何模块，无版本标识 | 单独列表 |

### 1.4 成功标准

```json
{
  "输出结构": "按第 5 节定义的目录结构",
  "可追溯性": "每个文件有决策记录",
  "人工介入": "仅处理无法自动解决的冲突"
}
```

---

## 2. 处理架构

### 2.1 阶段定义

| 阶段 | 名称 | 输入 | 输出 | 人工需要 |
|-----|------|------|------|---------|
| 0 | 前置准备 | 原始目录路径 | 备份目录 | 是 |
| 1 | 扫描与元数据提取 | 目录路径 | scan_result.json | 否 |
| 2 | 模块分组 | scan_result.json | modules.json | 否 |
| 3 | 冲突检测 | modules.json | conflicts.json | 否 |
| 4 | 版本决策 | conflicts.json + 用户锚点 | recommendations.json | 否 |
| 5 | 目录映射 | recommendations.json | file_mapping.json | 否 |
| 6 | 报告生成 | file_mapping.json | 三份报告 | 否 |
| 7 | 审核 | 所有报告 | 审核结果 | 是 |
| 8 | 执行 | apply_changes.py + --execute | 整理后目录 | 是 |

### 2.2 数据流

```
原始目录
    ↓ [阶段1]
scan_result.json
    ↓ [阶段2]
modules.json
    ↓ [阶段3]
conflicts.json
    ↓ [阶段4 + 用户锚点]
recommendations.json
    ↓ [阶段5]
file_mapping.json
    ↓ [阶段6]
report.json + summary.txt + apply_changes.py
    ↓ [阶段7 人工审核]
确认通过
    ↓ [阶段8]
整理完成目录
```

---

## 3. 核心决策规则

### 3.1 版本优先级（降序）

| 优先级 | 规则 | 置信度 |
|-------|------|-------|
| 1 | 用户提供的已知版本（--known-version） | 1.0 |
| 2 | 内部版本号明确 + 配套文件齐全 | 0.9 |
| 3 | 修改时间最新 + 无冲突标记 | 0.7 |
| 4 | 文件名含 final/release/production | 0.5 |
| 5 | 配套文件数量最多 | 0.4 |

### 3.2 冲突处理策略

| 冲突类型 | 处理动作 | 输出状态 |
|---------|---------|---------|
| IDENTICAL_NAME_DIFF_CONTENT | 全部保留，不自动选 winner | CONFLICT |
| VERSION_MISMATCH | 标记，置信度 -0.3 | CONFLICT 或 CANDIDATE |
| TIMELINE_INVERSION | 标记，需人工确认 | CONFLICT |
| MISSING_DEPENDENCY | 保留现有，标注缺失 | CONFLICT/Missing_Dependency |
| DUPLICATE_HASH | 保留一份，其余标记 | DUPLICATE |
| ORPHAN | 放入 Conflicts/Orphan | CONFLICT |

### 3.3 配套文件判断规则

```python
配套条件 = (
    sch与pcb修改时间差 ≤ 7天 AND
    bom位号与sch匹配率 ≥ 80%
)
```

---

## 4. 输出物规范

### 4.1 目录结构

```
/{项目名}/
  /01_Release/           # 推荐的唯一最终版本
  /02_Candidates/        # 备选版本（多个候选无法确定时）
  /03_Historical/        # 历史版本，按 YYYY-MM-DD_vX 归档
  /04_Conflicts/         # 冲突文件
    /Version_Mismatch/
    /Missing_Dependency/
    /Orphan/
  /05_Duplicates/        # 重复文件
  /06_Reports/           # 生成的报告
```

### 4.2 report.json 结构

```json
{
  "project_name": "string | null",
  "scan_timestamp": "ISO8601",
  "summary": {
    "total_files": "int",
    "total_size_bytes": "int",
    "file_type_counts": {},
    "conflict_counts": {},
    "recommendation_counts": {}
  },
  "modules": {
    "module_name": {
      "files": ["path"],
      "recommended_winner": {"path": "str", "reason": "str", "confidence": 0.9},
      "losers": [{"path": "str", "reason": "str"}],
      "conflicts": [{"type": "str", "files": ["path"], "evidence": "str"}]
    }
  },
  "file_mapping": {
    "original_path": {
      "target_path": "str",
      "status": "release|candidate|historical|conflict|duplicate",
      "conflict_type": "str | null",
      "decision_reason": "str"
    }
  }
}
```

### 4.3 summary.txt 格式

```
=== 电子工程资料整理报告 ===
生成时间: {timestamp}
扫描路径: {path}

--- 统计 ---
总文件数: {n}
总大小: {size}
文件类型分布: {dist}

--- 模块摘要 ---
模块1: {name}
  - 推荐版本: {path} (置信度: {conf})
  - 备选版本数: {n}
  - 冲突数: {n}

--- 冲突清单（需人工处理）---
[1] 类型: {type}
    文件: {paths}
    证据: {evidence}

--- 待确认项 ---
- [ ] {action_item}
```

### 4.4 apply_changes.py 接口规范

```python
# 命令行接口
python整理脚本.py <根目录路径> [选项]

# 选项
--dry-run               # 默认模式，只预览
--execute               # 实际执行移动/重命名
--backup                # 执行前备份整个目录
--conflict-dir PATH     # 自定义冲突目录
--known-version K=V     # 可多次使用
--verbose               # 详细日志
--output-dir PATH       # 报告输出目录
```

---

## 5. 安全机制

### 5.1 必须实现的安全特性

```python
# 所有文件操作必须有 dry-run 判断
def move_file(src, dst, dry_run=True):
    if dry_run:
        print(f"[DRY-RUN] {src} -> {dst}")
    else:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(dst))

# 默认 dry_run = True
# 用户必须显式传入 --execute 才能实际执行
```

### 5.2 备份要求

- 支持 `--backup` 参数
- 备份目录命名：`{原路径}.backup_{YYYYMMDD_HHMMSS}`
- 备份在执行前完成

---

## 6. 错误处理规则

| 错误类型 | 处理行为 | 是否中断 |
|---------|---------|---------|
| 文件无法读取 | 记录警告，跳过 | 否 |
| 编码错误 | 尝试 fallback 编码，失败则跳过内容提取 | 否 |
| 磁盘空间不足 | 抛出异常 | 是 |
| MD5 计算失败 | 重试 3 次 | 否 |
| 目标路径已存在 | 添加 `_conflict_{n}` 后缀 | 否 |

---

## 7. 执行检查清单

### 7.1 执行前（AI 自动检查）

```json
{
  "输入路径存在且可读": false,
  "Python版本 >= 3.8": false,
  "磁盘空间足够（≥1.5倍原始大小）": false
}
```

### 7.2 dry-run 后（人工检查）

- [ ] report.json 已生成且可解析
- [ ] 冲突清单已阅读并理解
- [ ] 无意外的大规模误判

### 7.3 正式执行前（人工确认）

- [ ] 备份已完成
- [ ] 已准备好回滚方案
- [ ] 已通知相关人员

---

## 8. 版本历史

| 日期 | 变更内容 | 版本 |
|-----|---------|------|
| 2026-06-05 | 初始创建 | 1.0 |
