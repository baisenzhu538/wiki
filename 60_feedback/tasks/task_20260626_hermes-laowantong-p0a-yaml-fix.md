---
id: task_20260626_hermes-laowantong-p0a-yaml-fix
type: rework_task
created_at: 2026-06-26
author: 王语嫣
assignee: Hermes 老顽童
priority: P1
scope: P0-A 单元模型域 10 张卡 frontmatter YAML 解析失败
---

# Hermes 老顽童返工任务：P0-A 单元模型域 10 张卡 YAML 修复

> 王语嫣铁律：本指令仅写入 `60_feedback/`，不污染 `30_wiki/`。老顽童负责按此指令在 `30_wiki/` 修补卡片。
> 前置诊断：`60_feedback/diagnosis/diag_20260626_wangyuyan-p0a-yaml-parser-failures.md`

---

## 0. 元信息

| 项目 | 内容 |
|------|------|
| 任务类型 | 返工（新增） |
| 返工来源 | P0-A 单元模型域 YAML 全量扫描发现 10 张卡 frontmatter 解析失败 |
| 优先级 | P1（建议在 science 域生产间隙处理） |
| 质量负责人 | 王语嫣（CLI） |
| 生产方 | Hermes 老顽童 |

---

## 1. 问题描述

10 张 P0-A 单元模型域卡片的 frontmatter 中，`related:` 字段列表缩进断裂，导致 `yaml.safe_load` 解析失败。

**错误模式**：
```yaml
related:
  - '[[A]]'
  - '[[B]]'
- "[[C]]"
- "[[D]]"
```

**正确模式**：
```yaml
related:
  - '[[A]]'
  - '[[B]]'
  - "[[C]]"
  - "[[D]]"
```

所有 `related` 列表项必须统一缩进在 `related:` 之下。

---

## 2. 待修复的 10 张卡

| # | 卡片路径 | 类型 |
|---|:---|:---|
| 1 | `30_wiki/concepts/ai单元模型口述蒋老师.md` | concept |
| 2 | `30_wiki/concepts/concept-单元模型-学练用.md` | concept |
| 3 | `30_wiki/dk/dk-单元模型-找全成本实操难点.md` | dk |
| 4 | `30_wiki/dk/dk-单元模型-找单元模型实操难点.md` | dk |
| 5 | `30_wiki/dk/dk-单元模型-找基准值实操难点.md` | dk |
| 6 | `30_wiki/dk/dk-单元模型-规模对抗实操难点.md` | dk |
| 7 | `30_wiki/frameworks/framework-单元模型-外部对抗地图.md` | framework |
| 8 | `30_wiki/frameworks/yt-unit-model-ladder.md` | framework |
| 9 | `30_wiki/tools/tool-单元模型-单城市.md` | tool |
| 10 | `30_wiki/tools/tool-单元模型-壁垒预判.md` | tool |

---

## 3. 修复要求

### 3.1 最小改动原则

- **只修 frontmatter 中的 `related` 缩进**，不要改动正文内容。
- 保持原有 `related` 项不变（不要增删条目，除非发现明显的 broken link）。
- 保持单引号/双引号风格统一（本次以修复缩进为首要目标，引号风格可保留原样）。

### 3.2 修复后必须满足

1. `yaml.safe_load(frontmatter)` 不报错。
2. `id` 字段与文件名一致。
3. `related` 解析为列表，长度与原文一致。
4. 所有 `[[...]]` 链接目标在 `30_wiki/` 中存在（王语嫣复核时会二次确认）。

---

## 4. 自查脚本

修复后，在仓库根目录运行以下命令验证：

```bash
python -c "
import yaml, glob, sys
files = [
    '30_wiki/concepts/ai单元模型口述蒋老师.md',
    '30_wiki/concepts/concept-单元模型-学练用.md',
    '30_wiki/dk/dk-单元模型-找全成本实操难点.md',
    '30_wiki/dk/dk-单元模型-找单元模型实操难点.md',
    '30_wiki/dk/dk-单元模型-找基准值实操难点.md',
    '30_wiki/dk/dk-单元模型-规模对抗实操难点.md',
    '30_wiki/frameworks/framework-单元模型-外部对抗地图.md',
    '30_wiki/frameworks/yt-unit-model-ladder.md',
    '30_wiki/tools/tool-单元模型-单城市.md',
    '30_wiki/tools/tool-单元模型-壁垒预判.md',
]
fail = 0
for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as fh:
            text = fh.read()
        fm = text.split('---', 2)[1]
        data = yaml.safe_load(fm)
        assert isinstance(data.get('related'), list), f'{f}: related is not list'
        print(f'OK: {f}')
    except Exception as e:
        print(f'FAIL: {f} -> {e}')
        fail += 1
sys.exit(1 if fail else 0)
"
```

---

## 5. 提交方式

- 修复完成后，在当前会话或 `.agent/context.md` 中通知王语嫣复核。
- 王语嫣将：
  1. 对 10 张卡逐一跑 `yaml.safe_load`；
  2. 检查 broken link；
  3. 确认无新增问题后，通知欧阳锋审查 `dk-单元模型-对抗小抄`。

---

## 6. 注意事项

- 不要借修复之机调整正文或重命名卡片。
- 如果某张卡的 `related` 中存在已确认不存在的链接，先按原样保留缩进，在汇报中单独列出，由王语嫣判断如何处理。
- 建议修复后顺手检查一下同批次其他卡（如 `tool-单元模型-单商圈`、`concept-最简单元模型` 等）是否也有同类问题，一并修复。

---

*任务下达：王语嫣 | 日期：2026-06-26*
