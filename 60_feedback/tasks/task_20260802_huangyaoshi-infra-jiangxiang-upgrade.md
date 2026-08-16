---
id: task_20260802_huangyaoshi-infra-jiangxiang-upgrade
task_id: 220
assignee: huangyaoshi
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-09
created_at: 2026-08-02
domain: kdo
priority: P0
source:
  - 60_feedback/diagnosis/diag_20260802_huangyaoshi-kdo-infra-communication-upgrade.md
  - 60_feedback/diagnosis/diag_20260802_huangyaoshi-mcp-external-agent-experience.md
updated_at: '2026-08-09T00:00:00+00:00'
claimed_at: 2026-08-09
---

## 执行报告（2026-08-09 黄药师补交）

### 状态盘点：8 项中 7 项已实现（08-03 完成），本次补齐剩余 2 项

| 项 | 状态 | 说明 |
|:--|:--:|:--|
| P0-1 HINT_MAP 场景化 | ✅ 已实现 | kdo_lint.py ERROR_HINT_MAP（08-03） |
| P0-2 cap_hub one_liner | ✅ 已实现 | registry.py 读 frontmatter one_liner（08-03） |
| **P0-3 title/aliases/tags 门禁** | ✅ **本次补齐** | 新增 `_check_frontmatter_metadata`（见下） |
| P0-4 MCP description 场景化 | ✅ 已实现 | tools.py（08-03） |
| **P1-5 输出情绪化+路径感** | ✅ **本次补齐** | format_report PASS/FAIL 文案（见下） |
| P1-6 query scene 分组 | ✅ 已实现 | delivery.py RRF scene boost（08-03，#208） |
| P1-7 kdo_search 诊断字段 | ✅ 已实现 | tools.py score_label/diagnosis（08-03） |
| P1-8 MCP 互引路由网 | ✅ 已实现 | tools.py Related tools 段（08-03） |

### 本次实现明细
1. **P0-3** `_check_frontmatter_metadata`（pre_submit.py）：title 空 → ERROR / aliases 无中文 → WARN / tags 缺 audience/scene → WARN。注册到主流程（run_pre_submit 追加调用）
2. **P1-5** format_report 尾部：PASS 给成就感+下一步（"一次通过！欧阳锋这轮会很省心"）/ FAIL 给路径感（"先修 YAML 结构错误→再修内容错误→重跑看到 ✅ PASS 再提交"）

### 狗粮测试（全过）
| 场景 | 结果 |
|:---|:---|
| P0-3 正常卡 | ✅ 0 issue |
| P0-3 缺 title | ✅ ERROR 阻断 |
| P0-3 aliases 无中文 | ✅ WARN |
| P0-3 tags 缺维度 | ✅ WARN |
| P1-5 FAIL 文案 | ✅ 路径感 + 修法指引 |
| P1-5 PASS 文案 | ✅ 成就感 + 下一步 |
| 回归（validate_deep/ship_gate/workspace） | ✅ 78 passed |
| 真实卡验证（3 张 framework） | ✅ 0 新增 P0-3 报 |

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

## 终审记录（2026-08-09 欧阳锋·孤儿补审）

**verdict: PASS A- · blocking: 无 · methodology v2.2**

O3 独立验证：
1. P0-3 实现确认：_check_frontmatter_metadata（kdo/pre_submit.py L177）三条件（title 空 ERROR/aliases 无中文 WARN/tags 缺 audience/scene WARN）
2. P1-5 文案确认（L964 PASS"一次通过！修得干净，欧阳锋这轮会很省心"/L969 FAIL 路径感"先修 YAML 结构错误再修内容错误"）
3. **缺 title 实测阻断**：kdo pre-submit 对无 title 测试卡输出 3 处 🔴 ERROR
4. P0-1/P0-2/P0-4/P1-6/P1-7/P1-8 已实现（08-03）——8/8 全齐
5. 边界遵守：纯输出/提示文本改动，CLI 行为逻辑未动；回归 78 passed

🟢 观察：90_control/scripts/pre_submit.py 为旧版（无 P0-3）——`kdo pre-submit`（CLI 主命令）才是生效入口，建议旧脚本标注 deprecated 避免双入口混淆

五维：溯源 90/逻辑 90/暗知识 80/可操作 90/表达 85 → 总分 88（A-）
