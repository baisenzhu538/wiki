---
name: domain-iteration
description: KDO域迭代五阶段法总入口——将原始素材转化为可复用资产（卡片/Skill/Workflow/模板）
version: 1.0.0
author: 黄药师
license: MIT
platforms: [cli, feishu]
metadata:
  hermes:
    tags: [KDO, 域迭代, 新域上线, 素材验收, 知识工程]
    related_skills: [stage-1-diagnose, stage-2-skeleton, stage-3-tooling, stage-4-validate, stage-5-assetize]
---

# KDO 域迭代五阶段法

将 `00_inbox/<新域>/` 下的原始素材转化为 wiki 卡片 + Skill + Workflow + 模板。

## 触发词

新域上线、素材补齐了、这个域怎么建、域迭代、domain iteration、开个新域

## 约束

- 严禁跳过阶段：diagnose → skeleton → tooling → validate → assetize
- 每个阶段结束必须产出指定文件
- 阶段1必须先查已有卡片避免重复
- 调研先行：每阶段第一步 WebSearch 查最佳实践

## 五阶段总览

```
阶段1: 诊断(王语嫣) → 阶段2: 骨架(老顽童) → 阶段3: 工具化 → 阶段4: 验证 → 阶段5: 资产化
```

| 阶段 | Skill | 主力 | 输出 |
|:--|:--|:--|:--|
| 1 | stage-1-diagnose | 王语嫣 | 诊断记录 + 任务清单 |
| 2 | stage-2-skeleton | 老顽童 | 框架卡 + 索引入口 |
| 3 | stage-3-tooling | 老顽童+黄药师 | Tool卡 + Skill + 提示词 |
| 4 | stage-4-validate | Agent+用户 | 验证报告 + 补缺 |
| 5 | stage-5-assetize | 老顽童+段王爷 | Workflow + 模板 + Ship |

## 快速启动

```
收到新域任务 → /domain-iteration
  → Stage 1: 王语嫣诊断素材
  → Stage 2: 老顽童建框架
  → Stage 3: 工具化
  → Stage 4: Agent实测
  → Stage 5: 发布
```

> 欧阳锋在每个阶段结束时审查闸门。
