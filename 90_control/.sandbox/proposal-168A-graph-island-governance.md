# #168A 图谱孤立团治理方案 v2（黄药师 A 段）

> 送欧阳锋签审 · 2026-07-13
> v1 退回原因：三子任务事实基础偏差。v2 对齐任务单实际口径。

---

## 子任务 A-1：OCR 飞地物理迁移

### 事实基础

- `30_wiki/raw/ocr/` 184 卡（draft/low trust/confidence 0.6）
- 团内 827 条机器边（related 列表系半肥猫 OCR 管道批量生成，非策展）
- 46 张卡 domain 字段混入 `needs-review` 状态标签
- #163 已摘除正式卡→OCR 的 655 条引用，需复扫确认零残留

### 方案

**① 物理迁移**：`30_wiki/raw/ocr/` → `10_raw/ocr-cards/`

实施步骤：
1. 创建 `10_raw/ocr-cards/` 目录
2. Python 脚本批量 `mv` 184 卡
3. 文件名保持不变（保留 OCR 溯源标识）
4. `templates.py` 的 `REQUIRED_DIRS` 中移除 `30_wiki/raw/ocr`、追加 `10_raw/ocr-cards`
5. 更新 `kdo_lint.py` 中的搜索路径排除（`raw` 已在过滤列表，迁移后自然不再扫描）

**② 827 条机器边处置**：

移出后处置：**清空 related 列表**（改为空数组 `[]` 或完全删除 related 字段）。

理由：
- 827 条边系机器自动生成（OCR 管道按同课程/同主题批量写入 related），非人工策展
- OCR 卡作为素材层（非知识节点），related 没有语义价值
- 清空而非保留原样：避免迁移后 related 中的相互引用在 `10_raw/` 下继续产生死链警告

**③ source_refs 溯源保持**：

OCR 卡的 `source_refs` 指向 `10_raw/sources/` 的原始文件路径——迁移不改变这些路径。不动 source_refs。

**④ 正式卡→OCR 残留复扫**：

`#163` 已摘 655 条。迁移前跑一次全量 lint 确认 `F2 BROKEN LINK: ocr-*` = 0（当前确认为 0）。

**⑤ 46 张 needs-review 伪域清洗**：

这 46 张卡的 domain 字段值为 `needs-review`（应为 `status` 字段值）。处置：
- 将 domain 中的 `needs-review` 条目移除
- 如果 domain 为空，不补——OCR 卡作为素材层不需要 domain
- 确认每张卡的 `status` 字段正确（应为 `draft` 或实际状态）

**⑥ 迁移后引用链修复**（欧阳锋补）：

a) **15 条正式卡 source_refs 路径更新**：
15 张正式卡的 source_refs 指向 `30_wiki/raw/ocr/...`，迁移后批量替换为 `10_raw/ocr-cards/...`：

| 路径特征 | 数量 |
|:---|:---|
| `30_wiki/cases/case-科学决策-*` | 6 |
| `30_wiki/concepts/concept-单元模型-学练用.md` | 1 |
| `30_wiki/dk/dk-单元模型-*` | 5 |
| `30_wiki/frameworks/framework-TCPR底层网络协议.md` | 1 |
| `30_wiki/frameworks/framework-单元模型-外部对抗地图.md` | 1 |
| `30_wiki/frameworks/yt-decision-abcd-model.md` | 1 |

b) **5 处脚本/文档硬编码路径更新**：

| 文件 | 行号 | 更新内容 |
|:---|:---|:---|
| `90_control/ingestion-pipeline.md` | 124,133,140 | `30_wiki/raw/ocr/` → `10_raw/ocr-cards/` |
| `90_control/scripts/fix_cb_ew.py` | 182 | 同上 |
| `90_control/scripts/label-quality-migrate.py` | 71 | 同上 |
| `90_control/.sandbox/_ocr_final_cleanup.py` | 67-68 | skiplist 路径同步更新，加注释注明迁移记录 |
| `.agent/context.md` | 98 | 同上 |

c) **templates.py 定位修正**：v2 方案中提到的 `templates.py REQUIRED_DIRS` 经欧阳锋确认不存在。实际配置位置为 `90_control/ingestion-pipeline.md`（已在上表）。迁移脚本不依赖 templates.py，改为直接操作文件系统 + 更新 ingestion-pipeline.md。

### 验收（更新）

- `30_wiki/raw/ocr/` 目录为空（0 文件）
- `10_raw/ocr-cards/` 有 184 卡
- 全量 lint 无 OCR 飞地相关错误
- 46 张卡 domain 字段无 `needs-review`
- **全库 `grep 30_wiki/raw/ocr/` 仅保留历史任务文档/审计记录，无活跃 source_refs / 脚本 / 配置指向**

---

## 子任务 A-2：ai-saas 复合 domain 拆分

### 事实基础

全库 domain 字段扫描结果（欧阳锋提供，黄药师实跑确认后再 apply）：

| 变体 | 出现次数 | 说明 |
|:---|:---|:---|
| `ai-saas` | 85 | 标准格式，不动 |
| `yitang- ai-saas` | 43 | 复合字符串（含空格），需拆为 `['yitang', 'ai-saas']` |
| `ai-saas- yitang` | 4 | 同上，拆为 `['ai-saas', 'yitang']` |
| `learning-methodology- ai-saas` | 4 | 拆为 `['learning-methodology', 'ai-saas']` |
| `ai-saas- ai` | 2 | 拆为 `['ai-saas', 'ai']` |

**总计 138 次，非 187 张卡**（同一卡可能有多个复合 domain）。

### 方案

**拆分映射表**：

| 原值 | 拆分后 |
|:---|:---|
| `yitang- ai-saas` | `yitang` + `ai-saas`（两个独立 domain） |
| `ai-saas- yitang` | `ai-saas` + `yitang` |
| `learning-methodology- ai-saas` | `learning-methodology` + `ai-saas` |
| `ai-saas- ai` | `ai-saas` + `ai` |

**实施**：
1. 脚本扫描全库 domain 字段
2. 匹配包含 ` - ` 或 `- ` 连字符的复合 domain 字符串
3. 拆分为多个独立 domain 条目（YAML list 格式，去重）
4. Dry-run 出 diff（每张卡前后对比）
5. 欧阳锋确认 → apply

**不动的**：`ai-saas` 85 次标准格式——无大小写/下划线变体，不需处理。

### 验收

- 全库 domain 字段中不含连字符复合字符串
- 拆分后 domain 为合法 YAML list
- 门禁通过

---

## 子任务 A-3：AI 簇 pending_unknown 出链处置

### 事实基础

口径修正（与 v1 的关键差异）：

| 类别 | v1 错误口径 | 实际数据 |
|:---|:---|:---|
| 处置范围 | 全库 frontmatter 占位 3126 处 | **AI 簇出链死链** |
| AI 簇 related 中 `[[pending_unknown]]` | — | **29 条** |
| AI 簇 frontmatter 占位 | — | 50 处（source_refs 39 = `src_unknown` + query_triggers 11 = `src_unknown`） |
| 全库 related 中 `[[pending_unknown]]` | — | 1280 条（不在本次范围） |

本次 scope：**AI 簇的 pending_unknown 出链**（29 条 related wikilink + 50 处 frontmatter 占位）。全库 1280 条 related 死链不在本次范围——需要王语嫣后续另立任务。

### 方案

按 #163 模式逐条分类：

| 分类 | 处置 | 适用条件 |
|:---|:---|:---|
| **补链** | 替换为真实卡 ID | 存在明确的对应卡片 |
| **摘** | 从 related 列表中移除该条目 | 无对应卡、占位无意义 |
| **登记** | 保留 + 在 manifest 中注明原因 | 确实待定、有合理的未决理由 |

**29 条 related 死链处置**：
1. 提取 AI 簇范围内 `related` 字段中指向 `pending_unknown` 的条目
2. 逐条判定：目标卡是否存在？语义是否匹配？
3. 存在+匹配 → 补链；不存在 → 摘；边界 → 登记

**50 处 frontmatter 占位处置**：
- source_refs 中的 `src_unknown`（39 处）：**摘**（移除该条目，无实际来源）
- query_triggers 中的 `src_unknown`（11 处）：**摘**（移除该条目，无实际触发场景）
- 摘除后若 source_refs 为空：卡片不降级（AI 簇卡为 draft 状态，本身即未完成）

### 验收

- AI 簇 related 中 `[[pending_unknown]]` 归零（或全部登记原因）
- AI 簇 frontmatter 占位归零
- 全量 lint 增量 = 0

---

## 执行顺序

```
A-1（OCR迁移）→ A-2（domain拆分）→ A-3（pending_unknown）
```

A-1 体量最大、影响面最广，先做。A-2 最轻量（138 次替换）。A-3 最精细（29+50 条逐条判定）。

三个子任务 #163 模式：签审方案 → dry-run → 欧阳锋确认 → apply → 复扫闭环。

---

## 签审请求

欧阳锋请确认：
1. A-1：物理迁移路径 `30_wiki/raw/ocr/` → `10_raw/ocr-cards/` + 机器边清空 + 伪域清洗 是否认可
2. A-2：复合 domain 拆分映射表 是否正确
3. A-3：scope 限定为 AI 簇（29 条 related + 50 处 frontmatter）是否与任务单一致

签审通过后按顺序执行。

---

*黄药师 · 2026-07-13 · v2*

---

## 欧阳锋签审记录（2026-07-13）

**结论：方案签审通过，按 #163 模式执行**

| 子任务 | 签审意见 |
|:---|:---|
| A-1 OCR 物理迁移 | ✅ 通过。迁移路径 `30_wiki/raw/ocr/` → `10_raw/ocr-cards/` 正确；机器边清空、46 张 needs-review 伪域清洗、15 条 source_refs 更新、5 处硬编码路径更新均纳入方案。 |
| A-2 ai-saas 复合 domain 拆分 | ✅ 通过。映射表基于实测 138 次变体，`yitang- ai-saas` 等复合字符串拆分为独立 domain list 正确。 |
| A-3 AI 簇 pending_unknown/src_unknown 处置 | ✅ 通过。scope 限定为 AI 簇 29 条 related 死链 + 50 处 frontmatter `src_unknown` 占位，术语已修正，不扩大至全库 1280 条。 |

**执行纪律**：
- 每子任务必须 **dry-run → 欧阳锋确认 → apply → 复扫闭环**
- A-1 apply 后验收必须包含：全库 `grep 30_wiki/raw/ocr/` 无活跃 source_refs / 脚本 / 配置指向
- A-2 apply 后验收必须包含：`yaml.safe_load` 可通过，domain 为合法 list
- A-3 apply 后验收必须包含：AI 簇 related `[[pending_unknown]]` 归零或全部登记原因；frontmatter `src_unknown` 归零

**签审人**：欧阳锋 · 2026-07-13
