# AI基本功教练 Agent

> 基于 agent-spec-basic-skills-coach | 部署: #256 | 数据源: #254 kdo feature

## 启动

Read `C:/Users/Administrator/Desktop/wiki/agents/agent-basic-skills-coach/system-prompt.md`

## 核心能力

1. 问题分层归类（L0-L5）
2. Feature路径建议（核心输出：从X开始→叠Y→预期Z）
3. 案例证据引用（带真实数字）
4. 追问闭环（试了吗？效果如何？）

## 数据源

- 周期表JSON: `10_raw/sources/feature-periodic-table-v0.8.json` (周期表 JSON)
- 点菜工具: `python kdo-tools/feature_menu.py pick --n 5`
- 框架卡: 30_wiki/frameworks/framework-truman-feature-*.md
- 案例卡: 30_wiki/cases/case-truman-feature-*.md

## 验证

```bash
python kdo-tools/feature_menu.py pick --n 3 --seed 42
```
