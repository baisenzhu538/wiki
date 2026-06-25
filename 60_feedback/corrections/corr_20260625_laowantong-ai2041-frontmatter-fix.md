# AI 2041 全 22 张卡 frontmatter 整改确认

> 触发：`60_feedback/audit/ai2041-p2-production-audit-20260625.md` 有条件通过，要求整改 2 个系统性 schema 问题。
> 任务文件：`60_feedback/tasks/task_20260625_laowantong-ai2041-frontmatter-fix.md`

---

## 整改内容

### 1. `confidence` 改为单一数值

| 批次 | 卡片 | 改后值 |
|:---|:---|:---:|
| P1 | `concept-ai-chair-determines-view` | 0.78 |
| P1 | `concept-ai-neutrality-bias` | 0.78 |
| P1 | `tool-ai2041-source-verification-checklist` | 0.80 |
| P2 | `concept-ai-information-quality-ladder` | 0.78 |
| P2 | `case-deepfake-market-misuse` | 0.80 |
| P2 | `case-ai-companion-emotional` | 0.80 |
| P2 | `case-roblox-ai-npc-education` | 0.80 |
| P2 | `case-ai-job-displacement-wef` | 0.80 |
| P2 | `dk-ai-social-progress-not-automatic` | 0.78 |

> 其余 13 张卡原本即为单一数值，未改动。

### 2. 移除 frontmatter 中 `source_person` / `source_context`

| 批次 | 卡片 | 正文是否已有来源节 |
|:---|:---|:---:|
| P1 | `case-compas-racial-bias` | 是 |
| P1 | `case-apple-card-gender-bias` | 是 |
| P1 | `case-dutch-childcare-scandal` | 新增 |
| P1 | `case-cambridge-novelists-survey` | 新增 |
| P1 | `case-chen-qiufan-ai-writing` | 新增 |
| P2 | `case-deepfake-market-misuse` | 是 |
| P2 | `case-ai-companion-emotional` | 是 |
| P2 | `case-roblox-ai-npc-education` | 新增 |
| P2 | `case-ai-job-displacement-wef` | 是 |
| P2 | `dk-ai-prediction-expiry-date` | 新增 |
| P2 | `dk-ai-social-progress-not-automatic` | 新增 |
| P2 | `dk-ai-scarcest-resource-is-self` | 新增 |

### 3. lint schema 同步

- `Knowledge Delivery OS 0.0.1/kdo/workspace.py`
  - case 卡不再强制检查 `source_person` / `source_context`
  - dk 卡 `_DK_REQUIRED_FRONTMATTER` 仅保留 `dark_knowledge_type`
- `Knowledge Delivery OS 0.0.1/kdo/commands/quality.py`
  - `kdo produce` 默认模板不再生成 `source_person` / `source_context`

### 4. `30_wiki/index.md` 补漏

新增以下 4 张此前未登记卡的入口：

- `case-chen-qiufan-ai-writing`
- `case-dutch-childcare-scandal`
- `concept-ai-amara-law-business-judgment`
- `tool-tech-probability-80-filter`

---

## 验证结果

- Python `yaml.safe_load` 全量解析 22/22 通过。
- `kdo lint` 针对 22 张卡过滤检查：**无 ERROR / FATAL / WARNING**。
- 全库历史债务未扩大。

---

## 下一任务

等待王语嫣随机抽查 2 张卡确认后，AI 2041 域 22 张卡视为正式收工，随后启动：

> `60_feedback/tasks/task_20260625_laowantong-synthesis-dk-cards.md`

生产 strategy / research / yitang 三域跨案例 synthesis dk 卡 9 张。

---

*整改人：老顽童 | 日期：2026-06-25*
