---
name: stage-3-tooling
description: 域工具化——Tool卡+Claude Code Skill+AI提示词（老顽童+黄药师模式）
version: 1.0.0
author: 黄药师
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [KDO, 工具化, Skill, 提示词, tooling]
    related_skills: [domain-iteration, stage-2-skeleton, stage-4-validate]
---

# Stage 3: 域工具化

将域内框架和素材转化为可执行的工具。

## 触发词

工具化、写工具卡、做skill、tooling、把框架变成工具、生成skill

## 三类产出

| 类型 | 路径 | 何时用 |
|:--|:--|:--|
| Tool 卡 | `30_wiki/tools/` | 需人工判断的流程 |
| Skill | `40_outputs/capabilities/skills/shared/` | 可自动化执行的流程 |
| 提示词 | `00_inbox/<域>/` | 固定模板的 AI 分析 |

## Skill 格式

```yaml
---
name: skill-name
description: 一句话
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [...]
    related_skills: [...]
---
# 标题
## 触发词 / 约束 / 执行步骤 / 输出规范
```

## Tool 卡结构
- When to Use（触发场景）
- Steps（操作步骤）
- Failure Modes（≥3 种失败模式）
- Constraints & Boundaries

## 完成标准
- [ ] Tool 卡包含失败模式和适用边界
- [ ] Skill 可通过名称调用
- [ ] 域索引入口卡已更新
- [ ] `kdo lint` 通过
