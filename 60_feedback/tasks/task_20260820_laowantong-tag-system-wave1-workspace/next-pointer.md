# #393 标签体系 workspace

> 长程任务持久上下文（#402 试点）。换会话续作：**只读本文件 + in-progress/ + excluded/ 即可接续，无需重建上下文**。

## 上次停在哪（2026-08-21 快照）

**W1（本单）已终审 PASS A-（欧阳锋 2026-08-20）**——任务状态：reviewed。本单范围内无待办。

## 下一步（W2+ 波次，未立项）

1. **词表定稿后按域分批回填 573 张缺维度卡**（#399 复扫口径：`full-library-rescan.py --check missing-tags-dim`，2026-08-21 实测 573）
2. 存量清理前基线已封存（`90_control/baseline/rescan-baseline.json`）——回填按批更新基线
3. W2 立项时王语嫣编排（建议单列 #393-W2，引用本 workspace）

## 已排除方向（excluded/，勿重蹈）

| 方向 | 排除原因 |
|:--|:--|
| 大规模回填（全库 739 张原判定） | #393 边界：词表未定稿禁大规模回填，只试点一域 |
| 词表取值凑数（<5 卡支撑） | 欧阳锋 FAIL P2：coaching/leadership 等低频取值须逐条"预期高频"说明或删除 |
| 试点域 ai-collaboration 之外先扩 | #393 只试点 ai-collaboration 一域，W2 再扩 |

## 关键口径（复用，勿再踩）

- **全库复扫口径**：`full-library-rescan.py`（#399）——"清单口径归零"≠"全库归零"（#391/#393 连续复发教训）
- **yitang 域阳性对照**：`--check missing-tags-dim --domain yitang` 须为 0；parse-error 不参与域过滤（一堂.md/yihang YAML 损坏显式可见）
- **domain 精确匹配**：domain 列表含目标域才算（`domain[0]` 漏多 domain 卡——#393 P1 根因）

## 换会话续作实测（#402 验收动作）

- 本文件 + in-progress/ 空（W1 已完成无中间产物）→ 新会话读本文件即可给出"下一步=W2 立项"结论
- 实测记录见任务单 `task_20260821_huangyaoshi-task-workspace.md` 执行报告
