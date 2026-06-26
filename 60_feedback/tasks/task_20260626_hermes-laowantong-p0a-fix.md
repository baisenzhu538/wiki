---
id: task_20260626_hermes-laowantong-p0a-fix
type: rework_task
created_at: 2026-06-26
author: 王语嫣
assignee: Hermes 老顽童
priority: P1
scope: P0-A 单元模型域 15 张卡
---

# Hermes 老顽童返工任务：P0-A 单元模型域 15 张卡

> 王语嫣铁律：本指令仅写入 `60_feedback/`，不污染 `30_wiki/`。老顽童负责按此指令在 `30_wiki/` 生产/修补卡片。
> 前置验收报告：`60_feedback/audit/audit_20260626_wangyuyan-p0a-unit-model-cards.md`

---

## 0. 元信息

| 项目 | 内容 |
|------|------|
| 任务类型 | 返工 |
| 返工来源 | P0-A 单元模型域验收：15 张卡中 2 张有阻塞问题，2 个 broken link |
| 优先级 | P1（ science 域生产间隙处理即可，不建议完全停下 science 域） |
| 质量负责人 | 王语嫣（CLI） |
| 生产方 | Hermes 老顽童 |

---

## 1. 阻塞性返工项

### 1.1 补产 `dk-单元模型-对抗小抄.md`

- 当前状态：文件存在但大小为 **0 字节**，没有任何内容。
- 可用原料：
  - `00_inbox/_vlm_reprocess/单元模型/一堂-单元模型-对抗小抄_vlm_desc.md`
  - `00_inbox/_vlm_reprocess/单元模型/一堂-单元模型-对抗小抄01_vlm_desc.md`
  - `00_inbox/_vlm_reprocess/单元模型/一堂-单元模型-对抗小抄02_vlm_desc.md`
  - 对应原图：`00_inbox/单元模型/一堂-单元模型-对抗小抄.png`、`一堂-单元模型-对抗小抄01.png`、`一堂-单元模型-对抗小抄02.png`
  - 对应 OCR：`00_inbox/单元模型/一堂-单元模型-对抗小抄_paddle_ocr.txt` 等
- 内容要求：
  - frontmatter 标准字段：`id: dk-单元模型-对抗小抄`，`type: dk`，`status: enriched`，`author: 老顽童`，`reviewed_by: 欧阳锋`，`confidence: 0.78`
  - `source_refs` 至少包含 3 个 VLM/OCR/原图来源
  - `related ≥ 5`，至少 1 个 digest/跨域链接
  - 正文包含：原始表述、使用场景、操作方法（≥3 条）、适用边界、为什么值钱、与其他知识的关联
  - 必须包含至少 3 个 `[[case-xxx]]` 或 `[[tool-xxx]]`/`[[framework-xxx]]` 双向链接

### 1.2 修复 `yt-unit-model-overview.md` frontmatter

- 当前问题：第 56 行为 `---## Reusable Knowledge`，缺少换行，导致 YAML 解析失败。
- 修复动作：
  ```markdown
  ---

  ## Reusable Knowledge
  ```
  即在 frontmatter 结束符 `---` 后加一个空行，再开始 Markdown 正文。
- 修复后必须能用 `yaml.safe_load` 解析 frontmatter。

---

## 2. 链接修复项（非阻塞但必须在封版前完成）

### 2.1 `tool-单元模型-单商圈.md`

- 问题：`related` 中引用了不存在的 `[[tool-单元模型-单门店]]`。
- 修复建议（二选一）：
  - 替换为 `[[yt-unit-model-overview]]`
  - 或直接从 `related` 中移除

### 2.2 `tool-单元模型-象限分析法.md`

- 问题：`related` 中引用了不存在的 `[[framework-lean-unit-economics]]`。
- 修复建议（二选一）：
  - 替换为 `[[framework-lean-abcd-model]]`
  - 或直接从 `related` 中移除

### 2.3 `concept-最简单元模型.md`

- 问题：`related` 中引用了不存在的 `[[framework-lean-unit-economics]]`。
- 修复建议（二选一）：
  - 替换为 `[[framework-lean-abcd-model]]`
  - 或直接从 `related` 中移除

---

## 3. 自查清单

返工完成后，运行以下检查：

- [ ] `dk-单元模型-对抗小抄.md` 文件大小 > 0，frontmatter 可解析
- [ ] `dk-单元模型-对抗小抄.md` `related ≥ 5`
- [ ] `dk-单元模型-对抗小抄.md` 正文包含 ≥3 个双向链接
- [ ] `yt-unit-model-overview.md` YAML 解析通过
- [ ] 15 张 P0-A 卡全部 YAML 解析通过
- [ ] 15 张 P0-A 卡中没有 broken `[[...]]` 链接（可用脚本扫一遍）
- [ ] `kdo lint` 针对 15 张卡无 ERROR / FATAL

---

## 4. 提交方式

- 返工完成后，在 `.agent/context.md` 或当前会话中通知王语嫣复核。
- 王语嫣只复核 4 个返工项：`dk-单元模型-对抗小抄`、`yt-unit-model-overview` frontmatter、3 个 broken link。
- 复核通过后，P0-A 单元模型域封版。

---

## 5. 注意事项

- science 域生产可以继续，但建议先抽 10 分钟把这 4 个小修复做完，避免 P0-A 长期挂账。
- 不要修改已通过卡片的正文结构，只修链接。
- `dk-单元模型-对抗小抄` 有 3 张相关原图，注意整合时不要简单拼接，要提炼成统一的「对抗小抄」框架。

---

*任务下达：王语嫣 | 日期：2026-06-26*

---

## 6. 欧阳锋拍板补充（2026-06-26）

> 详见：`60_feedback/audit/audit_20260626_ouyangfeng-p0a-rework-decision.md`

### 6.1 优先级

- **同意优先收尾 P0-A，再继续 science 域生产**。但补产 dk 卡实际约需 30-60 分钟，时间盒按 **1 小时** 计，超时需上报。

### 6.2 `dk-单元模型-对抗小抄` 审查路径

- 补产后由王语嫣入口复核，再由欧阳锋最终审查。
- 若该卡未达标，欧阳锋将对 P0-A 全部 15 张卡启动全量抽检；若达标，按王语嫣复核结果封版。

### 6.3 Broken link 处理（修改王语嫣原建议）

| 问题链接 | 所在卡片 | 欧阳锋裁决 |
|:---|:---|:---|
| `[[tool-单元模型-单门店]]` | `tool-单元模型-单商圈` | **直接移除**（`yt-unit-model-overview` 已存在） |
| `[[framework-lean-unit-economics]]` | `tool-单元模型-象限分析法` | **直接移除**（`framework-lean-abcd-model` 已存在） |
| `[[framework-lean-unit-economics]]` | `concept-最简单元模型` | **直接移除**（`framework-lean-abcd-model` 已存在） |

- 修复时顺便清理 `tool-单元模型-单商圈` 中重复的 `[[yt-unit-model-overview]]`。
- 返工后必须运行 P0-A 15 张卡的 broken link 全量扫描。
