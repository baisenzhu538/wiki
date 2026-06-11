---
id: "corr_20260611_laowantong-design-domain-island-bridges"
type: "correction"
target_role: "老顽童（Producer）"
source: "王语嫣诊断 + 欧阳锋任务 #32"
severity: "P0"
status: "closed"
created_at: 2026-06-11
---

# 纠正：Design 域 5 对孤岛桥接 —— 按内容重标 domain + 补 related

> 王语嫣 2026-06-11 概念卡地图诊断发现：design 域 32 张卡片全部单域，约 50% 内容已超越纯设计范畴。
> 根因是 `domain` 字段只按来源（月白口述稿）标注，未按内容标注。
> 老顽童已按 P0 5 对桥接执行修正。

---

## 执行依据

- 源诊断：`60_feedback/diagnosis/diag_20250611_design-island-bridge-analysis.md`
- 执行规范：`70_product/tasks/laowantong-next-tasks.md` §🔴 执行规范：domain 标注规则（强制）
- Schema 定义：`90_control/schemas/concept.yaml` §domain

## 核心原则

**标内容，不标出身。**

`domain` 字段标注的依据是卡片内容讨论了什么域，而不是来源是谁。

---

## 修改清单

### Design 卡片侧（5 张）

| 卡片 | 旧 domain | 新 domain | 新增 related |
|:---|:---|:---|:---|
| `dk-yb7-design-demand-80-10-10` | `["design"]` | `design, yitang, business-strategy` | `yt-entrepreneur-needs-analysis`, `yt-barrier-identification-skill` |
| `dk-yb19-visual-strategy-price-match` | `["design"]` | `design, yitang` | `yt-model-conversion-optimization` |
| `dk-yb21-ecommerce-pricing-independent-model` | `["design"]` | `design, business-strategy` | `yt-entrepreneur-unit-model` |
| `dk-yb9-cubox-deployment-failure` | `["design"]` | `design, management, ai-collaboration` | `yt-management-toolkit-overview`, `concept-纪浩-ai-collaboration-methodology` |
| `dk-yb10-theory-moat-designer` | `["design"]` | `design, business-strategy` | `yt-barrier-identification-skill` |

### 目标卡片侧反向链接（5 张）

| 目标卡片 | 新增 related | 备注 |
|:---|:---|:---|
| `yt-entrepreneur-needs-analysis` | `dk-yb7-design-demand-80-10-10` | 修复 `related: {'series': False}` 为合法列表 |
| `yt-model-conversion-optimization` | `dk-yb19-visual-strategy-price-match` | 修复 `related: {'level': 'intermediate'}` 为合法列表 |
| `yt-entrepreneur-unit-model` | `dk-yb21-ecommerce-pricing-independent-model` | 修复 `related: {'series': True}` 为合法列表 |
| `yt-management-toolkit-overview` | `dk-yb9-cubox-deployment-failure` | 原有 related 列表格式正确，追加 |
| `yt-barrier-identification-skill` | `dk-yb7-design-demand-80-10-10`, `dk-yb10-theory-moat-designer` | 修复 `related: {'series': False}` 为合法列表 |

---

## 判定说明

- `dk-yb7` 讨论"80% 运营需求可模板化"——本质是需求分层（yitang 需求分析）+ 资源配置策略（business-strategy）。
- `dk-yb19` 讨论"视觉策略与价格带匹配"——直接影响转化率（yitang 转化率优化）。
- `dk-yb21` 讨论"线上价格带独立建模"——本质是单元模型在商业场景的应用（business-strategy）。
- `dk-yb9` 讨论"AI 工具团队部署失败"——本质是管理工具选型（management）+ 人机协作（ai-collaboration）。
- `dk-yb10` 讨论"设计师理论护城河"——本质是壁垒识别（business-strategy）。

---

## 验证结果

- 5 张 design 卡的 domain 均在新 schema 枚举内。
- 5 张 design 卡的 related 字段均为字符串列表。
- 5 张目标卡均已反向链接。
- 所有相关卡片 `updated_at` 更新为 2026-06-11。

---

## 未来要求

1. 产新卡时按"内容而非出身"标注 domain；多 domain 是推荐做法。
2. 涉及跨域内容时，必须同时修改对应目标卡的 related，建立双向链接。
3. 不再使用 `— 暂无（待后续卡片补充关联）` 这类占位符——要么空数组，要么填真实链接。
4. 遇到 `related: {...}` 这种扫描器错误格式时一并修复。

---

## 执行人签名

> 执行人：老顽童
> 日期：2026-06-11
> 状态：已完成，待欧阳锋抽检
