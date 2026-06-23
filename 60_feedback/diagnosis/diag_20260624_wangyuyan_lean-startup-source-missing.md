> 王语嫣对老顽童反馈的回复：两张精益创业案例卡源文件缺失的诊断与决策。
> 王语嫣铁律：本文件只写入 `60_feedback/`，不污染 `30_wiki/`。

---

## 问题

老顽童在执行 `task_20260623_laowantong-lean-startup-case-supplement.md` 时发现：

| 卡片 ID | 标题 | 计划来源 | 问题 |
|:---|:---|:---|:---|
| `case-lean-marketing-channel-comparison` | 完美日记 vs 花西子：渠道验证路线对比 | 黄药师诊断的未利用 PPT 案例 | 在 `00_inbox/精益创业/` 中未找到对应 PPT/OCR/VLM |
| `case-lean-b2b-sector-selection` | 建材企业赛道选择验证 | 黄药师诊断的未利用 PPT 案例 | 在 `00_inbox/精益创业/` 中未找到对应 PPT/OCR/VLM |

---

## 王语嫣复核

- [x] 已复核 `00_inbox/精益创业/` 全部 `.png/.jpg` 文件列表，无文件名含“完美日记/花西子/建材/赛道选择”的文件。
- [x] 已用 Grep 搜索 `00_inbox/精益创业/` 全部 OCR/VLM/txt 文件，仅命中 `张磊-精益方法论-AMA-口述-02.txt` 中一处泛化 B2B 讨论，无具体“建材企业赛道选择”案例。
- [x] 已跨目录搜索 `00_inbox/一堂五步法/`、`00_inbox/调研专题/` 等位置，无完整对应 PPT 或案例文本。
- [x] 确认这两张卡在原决策文件 `dec_20260623_wangyuyan-lean-startup-case-supplement.md` 中标记为“未利用 PPT 案例”，其来源信息本身就不完整（仅写“完美日记 vs 花西子 PPT”“建材企业赛道选择 PPT”，无具体文件名）。

**结论**：源文件确实缺失，不是命名问题，不是搜索遗漏。

---

## 决策

**取消生产这两张卡**。将 P1 案例补完批次从 7 张调整为 5 张。

理由：
1. 卡片生产必须基于可验证的源文件，不能凭标题臆造内容；
2. 强行用网络搜索补全会脱离“一堂/Truman 课程体系”这一素材边界，导致卡片与域内其他卡片不一致；
3. 剩余 5 张卡已覆盖张磊 AMA 3 张 + 系统测试曲线 2 张，足以提升案例密度；
4. 如果用户后续找到对应 PPT，可作为独立 P2/P3 批次追加，不影响当前管线。

---

## 执行变更

| 文件 | 变更 |
|:---|:---|
| `60_feedback/decisions/dec_20260623_wangyuyan-lean-startup-case-supplement.md` | 删除/标注 `case-lean-marketing-channel-comparison`、`case-lean-b2b-sector-selection` 两张卡；总数从 7 改为 5 |
| `60_feedback/tasks/task_20260623_laowantong-lean-startup-case-supplement.md` | 删除这两张卡；执行顺序从 7 步改为 5 步；验收标准从 7 张改为 5 张 |
| `wiki/.agent/context.md` | 更新 blockers，记录源文件缺失 |
| `wiki/.agent/wangyuyan-context.md` | 更新当前状态，标记两张卡取消 |

---

## 对老顽童的下一步指示

1. 按更新后的 `task_20260623_laowantong-lean-startup-case-supplement.md` 继续生产剩余 5 张卡；
2. 不再为这两张卡投入时间搜索；
3. 每完成 2-3 张通知王语嫣抽样验收。

---

## 给用户的选择（非阻塞）

如果您后续找到以下任一素材，可以重新唤醒这个决策：
- `完美日记 vs 花西子` 渠道/路线对比 PPT 或截图
- `建材企业赛道选择` PPT 或截图

届时可作为独立 P2/P3 批次追加 1-2 张案例卡。

---

*诊断人：王语嫣 | 日期：2026-06-24*
