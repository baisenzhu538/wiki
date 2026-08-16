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

- 周期表JSON: `10_raw/sources/feature-periodic-table-v1.0.json` (周期表 JSON，v1.0 含 evidence 分级)
- 点菜工具: `python kdo-tools/feature_menu.py pick --n 5`
- 框架卡: 30_wiki/frameworks/framework-truman-feature-*.md
- 案例卡: 30_wiki/cases/case-truman-feature-*.md

## 检索纪律（2026-08-16 #325 统一检索层）

**先 kdo query 再查路径表**：任何 Feature/方法问题，先语义检索找新知识（8 月后新卡不在数据源路径表里），路径表兜底：

```bash
cd C:\Users\Administrator\Desktop\wiki && kdo query "Feature 反向教学" --limit 5
```

引用卡名必须检索实证（E020 教训：凭记忆写卡名=全错）。

## 验证

```bash
python kdo-tools/feature_menu.py pick --n 3 --seed 42
```
