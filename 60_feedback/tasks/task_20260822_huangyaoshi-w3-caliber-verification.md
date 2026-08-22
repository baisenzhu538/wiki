---
id: 412
assignee: huangyaoshi
status: queued
updated_at: '2026-08-22T12:50:00+08:00'
---
# #412 W3 口径核实（会诊硬前置：三个数字工具重跑）

- **任务号**：#412
- **状态**：queued
- **assignee**：huangyaoshi
- **优先级**：P1（会诊关键路径：数字未出，B4 批表态冻结）
- **立项**：2026-08-22 王语嫣（老朱拍板入列；会诊专案前置动作 W3，三方已一致）
- **来源**：风清扬建议书审计数字 vs "统计数字工具计"纪律——用他自己的纪律核他自己的数字

## 任务目标

重跑三个数字，输出到 `60_feedback/consultation/2026-08-22-kdo-systemic-upgrade/w3-verification.md`，每个数字附**命令+工具输出原文**：

1. **"1354 卡 888 draft（65.6%）"分母口径**（风清扬 §12.2）：全库 markdown 文档数 vs 30_wiki 卡数 vs status:draft 计数——1354 是什么的分母？888 是哪种口径的 draft？（对照：kdo index 当前 4069 docs）
2. **production-queue.md 当前体积**（风清扬 §4.6 称 207KB）：`ls -la` / `wc -c` 实测
3. **5 处字节级副本清单**（风清扬 维度 5）：`40_outputs/code/scripts/` vs `kdo-tools/` 逐文件 diff/hash 对比，列出确实字节一致的具体文件清单（是 5 个还是更多/更少）

## 验收标准

- 三数字各附命令+输出原文，不接受目测/转述（风清扬自己的纪律）
- 结论三态逐条标：**属实 / 口径差异（写清两种口径各是多少）/ 不属实**
- 产出文件落盘后 commit（E040）

## 边界

- 只核实只读，不改任何文件（副本清理是 B4 批拍板后的事）
- 结果写会诊专案 w3-verification.md，不进队列正文
- 与 #409（parse-error 修复）无冲突：W3 是只读扫描，可先做
