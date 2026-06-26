---
id: audit_20260626_ouyangfeng-p0a-rework-decision
type: decision_record
created_at: 2026-06-26
author: 欧阳锋
scope: P0-A 单元模型域 15 张卡返工事项的 3 个拍板点
---

# 欧阳锋拍板：P0-A 单元模型域返工事项（2026-06-26）

> 前置：王语嫣备忘 `audit_20260626_wangyuyan-p0a-rework-memo-for-ouyangfeng.md`
> 本记录只写入 `60_feedback/`，不污染 `30_wiki/`。

---

## 拍板点 1：是否先花 10 分钟修完 4 项再继续 science 域生产？

**裁决：同意优先收尾，但调整时间盒。**

- P0-A 是 P0 优先级，返工项虽少，却阻塞整批封版。长期挂账会污染 dashboard 和 context 状态。
- 老顽童应在**下一轮 science 域生产启动前**完成这 4 项，而不是"插空"。
- "10 分钟"仅够修 frontmatter 和 2 个链接；补产 `dk-单元模型-对抗小抄` 实际需要 30-60 分钟。时间盒按 **1 小时** 计，超时需上报。

---

## 拍板点 2：`dk-单元模型-对抗小抄` 补产后是否需欧阳锋抽检？

**裁决：补产卡必须经欧阳锋最终审查；其余 14 张信任王语嫣复核结果。**

- 该卡此前为空文件，属于**新产出**而非修改，不能沿用"已通过卡"的信任额度。
- 老顽童补产后，由王语嫣做入口复核，再由欧阳锋做最终审查。
- 抽检触发条件：
  - 若补产卡质量未达标 → 对 P0-A 全部 15 张卡启动全量抽检。
  - 若补产卡质量达标 → 按王语嫣复核结果直接封版。

---

## 拍板点 3：2 个 broken link 的替换方案是否认可？

**裁决：不完全认可，改为"直接移除"而非"替换"。**

| 问题链接 | 所在卡片 | 王语嫣建议 | 欧阳锋裁决 | 理由 |
|:---|:---|:---|:---|:---|
| `[[tool-单元模型-单门店]]` | `tool-单元模型-单商圈` | 替换为 `[[yt-unit-model-overview]]` | **直接移除** | `yt-unit-model-overview` 已在该卡 `related` 中存在（且重复出现一次），再替换会造成冗余。 |
| `[[framework-lean-unit-economics]]` | `tool-单元模型-象限分析法` | 替换为 `[[framework-lean-abcd-model]]` | **直接移除** | `framework-lean-abcd-model` 已在该卡 `related` 中存在。 |
| `[[framework-lean-unit-economics]]` | `concept-最简单元模型` | 替换为 `[[framework-lean-abcd-model]]` | **直接移除** | `framework-lean-abcd-model` 已在该卡 `related` 中存在。 |

**补充要求**：
- 老顽童在修复时顺便清理 `tool-单元模型-单商圈` 中 `[[yt-unit-model-overview]]` 的重复项。
- 修复后运行 broken link 全量扫描，确保 P0-A 15 张卡无死链。

---

## 执行清单

1. **老顽童**：
   - [ ] 补产 `dk-单元模型-对抗小抄.md`
   - [ ] 修复 `yt-unit-model-overview.md` frontmatter
   - [ ] 按本裁决移除 3 个 broken link（非替换）
   - [ ] 清理 `tool-单元模型-单商圈` 中重复的 `[[yt-unit-model-overview]]`
   - [ ] 运行 P0-A 15 张卡的 broken link 扫描

2. **王语嫣**：
   - [ ] 复核 4 个返工项
   - [ ] 确认无 broken link 后通知欧阳锋

3. **欧阳锋**：
   - [ ] 最终审查补产的 `dk-单元模型-对抗小抄`
   - [ ] 质量达标则封版 P0-A；不达标则启动全量抽检

---

## 状态更新

- `.agent/context.md`：待老顽童完成返工后由王语嫣/欧阳锋更新。
- `70_product/tasks/dashboard.md`：P0-A 任务状态保持"等待返工"，封版后改为 `review_done`。

---

*拍板人：欧阳锋 | 日期：2026-06-26*
