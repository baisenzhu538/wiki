---
id: task_20260802_huangyaoshi-infra-jiangxiang-upgrade
task_id: 220
assignee: huangyaoshi
status: queued
created_at: 2026-08-02
domain: kdo
priority: P0
source:
  - 60_feedback/diagnosis/diag_20260802_huangyaoshi-kdo-infra-communication-upgrade.md
  - 60_feedback/diagnosis/diag_20260802_huangyaoshi-mcp-external-agent-experience.md
updated_at: '2026-08-02T23:59:00+00:00'
---

# #220 KDO基础设施"讲香"升级：CLI触点 + MCP外部Agent体验（合并两份建议书）

## 任务背景

黄药师从讲香基本功口述稿提取基础设施升级方案，落盘两份建议书：
1. `diag_20260802_huangyaoshi-kdo-infra-communication-upgrade.md` — KDO CLI全部触点（lint/query/pre-submit/cap_hub/MCP/dashboard）
2. `diag_20260802_huangyaoshi-mcp-external-agent-experience.md` — MCP外部Agent（小昭/Codex）端到端体验

**王语嫣合并判断**：两份建议书是同一件事的两面（CLI面向人/MCP面向Agent），底层共用HINT_MAP模式，**合并为一个任务**。与#218 R6b（搜索可达性校验）+ #219（存量title修复）直接联动——本任务P0-1是"防增量"，#219是"补存量"。

## 需求清单（8项，P0+P1）

### P0（黄药师，~50行总改动）

| # | 触点 | 改动 | 验收 |
|:--|:--|:--|:--|
| 1 | `kdo lint` 错误消息场景化 | HINT_MAP字典（~15行）——缺Critique等错误附💡场景化提示（"补上再提交省一轮往返"） | 跑lint对缺Critique的dk卡输出带💡提示 |
| 2 | `cap_hub list` 场景化 | registry.py读取frontmatter one_liner/description（~20行）——输出每个工具一句话用途 | 跑cap_hub list输出含一句话描述 |
| 3 | **pre-submit title/aliases/tags门禁** | validate阶段新增3条schema检查：title空→ERROR；aliases无中文→WARN；tags缺audience/scene→WARN（~30行） | 空title卡报ERROR阻断；缺aliases/tags报WARN |
| 4 | **MCP kdo_search tool description场景化** | tools.py替换description字符串（~5行）——场景化描述+搜不到时的3条替代路径 | 外部Agent按description建议尝试替代路径 |

### P1（黄药师，~170行）

| # | 触点 | 改动 | 验收 |
|:--|:--|:--|:--|
| 5 | `kdo pre-submit` 输出情绪化+升华化 | pre_submit.py输出段（~30行）——通过给成就感/失败给路径感 | 通过/失败分别输出带路径感描述 |
| 6 | `kdo query` 结果场景路由 | delivery.py RRF后按scene分组（~50行） | query结果按scene分组展示 |
| 7 | **kdo_search结果诊断字段** | tools.py search handler+delivery.py结果增强（~60行）——score_label/scene/audience/source_path/one_liner；0结果返回diagnosis体 | 0结果带suggestion；正常结果含新字段 |
| 8 | **MCP工具间互引路由网** | tools.py各tool description追加"相关工具"段（~20行） | 每个MCP tool description末尾有路由段 |

## 边界

- **只改输出格式/提示文本/description，不改CLI行为逻辑**（参数/返回值/协议不变）
- 零新增依赖（纯文本修改）
- P0项不跨角色（都在黄药师职责内）
- 不追溯旧输出
- **与#218 R6b协调**：本任务P0-3（title门禁）与#218 R6b（搜索可达性lint）同源——建议黄药师在#218做R6b时一并实现本任务P0-3，避免重复开发

## 验收标准

1. P0-1~P0-4 全部按上表验收
2. P1-5~P1-8 全部按上表验收
3. 全部 pytest 通过
4. 用 #213/#214/#215 卡片回归验证：修好的卡 lint/pre-submit 输出带场景化提示

## 参考

- 讲香口述稿：`00_inbox/讲香基本功-李頔-260731/讲香基本功-李頔-260731-口述.txt`
- 搜索诊断：`60_feedback/diagnosis/2026-08-02-search-reachability-diagnosis.md`
- 依赖文件：`90_control/scripts/kdo_lint.py` / `pre_submit.py` / `cap_hub/registry.py` / `kdo-tools/mcp/tools.py`
