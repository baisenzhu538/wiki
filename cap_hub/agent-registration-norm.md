# 能力中台 Agent 注册规范

> 当老顽童交付 agent-spec 卡后，黄药师按此规范部署到 cap_hub。目标是 spec 一出即可机械落地。

## 注册三步

### 1. spec 卡落位

老顽童产出 `agent-spec-<agent-name>.md`，落 `30_wiki/agent-specs/`（主目录）。

**最小 frontmatter**：
```yaml
id: agent-spec-basic-skills-coach
title: "基本功教练 Agent"
type: agent-spec
domain: [ai-basic, agent-capability]
status: draft
source_refs: [10_raw/sources/feature-periodic-table-v0.8.json]
```

### 2. cap_hub 注册

`cap_hub/registry.py` 的 `list_manuals()` 已自动扫描 `30_wiki/agent-specs/` 和 `30_wiki/tools/` 两个目录——spec 卡只要落位在其中任一目录，`cap_hub list` 即可发现。无需额外代码改动。

**当前模式（9 个已有 spec 验证）**：
- `30_wiki/agent-specs/` — 3 个（duanwangye/hongqigong/zhu-ai-coach）
- `30_wiki/tools/` — 6 个（含 agent-spec 前缀的文件也被收录）

### 3. kdo feature 数据源接入

agent 启动时调 `python kdo-tools/feature_menu.py pick --n 5 --seed <session_id>` 获取点菜数据。`--seed` 确保同一会话的点菜可复现。

## 部署验证

```bash
python -m cap_hub list | grep agent-spec  # 确认 spec 可见
python kdo-tools/feature_menu.py pick --n 3  # 确认点菜可用
```

## 已有参考

| spec | 路径 | 域 |
|:--|:--|:--|
| duanwangye-publisher | agent-specs/ + tools/ | publishing |
| hongqigong-multimodal | agent-specs/ + tools/ | multimodal |
| dual-triangle-canvas-filler | tools/ | yitang/ai-collaboration |

> 登记：2026-08-08 黄药师 | #251 先行B

## 已注册 Agent

| Agent | 状态 | 注册日期 |
|:--|:--|:--|
| basic-skills-coach | active | 2026-08-09 |
