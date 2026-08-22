---
id: 425
assignee: huangyaoshi
status: queued
updated_at: '2026-08-22T18:35:00+08:00'
---
# #425 KDO 健康度指标集（#399 复扫工具扩展）

- **任务号**：#425
- **状态**：queued
- **assignee**：huangyaoshi（指标定义王语嫣+风清扬会签）
- **优先级**：P1（G4 第 2 步：健康度度量——"不能积累太多问题"的仪器化）
- **立项**：2026-08-22 王语嫣（会诊 G4 拍板）

## 任务目标

把"KDO 健康运营"变成可复扫指标集，扩展 `full-library-rescan.py`（#399 工具同仓演进）：

| 指标 | 口径 | 当前基线（W3） |
|:--|:--|:--|
| draft 占比 | 30_wiki status:draft / 总卡 | 798/2865（27.9%） |
| 空壳卡率 | src_unknown 占位占比 | 待首扫 |
| 图谱孤儿率 | 零入链卡占比 | 20%（08-21 实测） |
| parse-error | YAML 解析失败数 | 58（#409 在修） |
| related-asymmetry | 单向链数 | 5265（#411 第十批后） |
| 复盘覆盖率/深度 | 各角色 daily-context 新鲜度+门禁等级 | 2/7 A 级（08-21 审计） |
| 队列一致性 | 队列行 vs 任务单 frontmatter | 0 漂移（audit_queue_integrity） |

## 动作

1. 七指标全部脚本化（一条命令出健康报告）；不接受人肉口径
2. 输出落 `60_feedback/auto/health-check-YYYYMMDD.md`（已有雏形——注意 W8：该报告第一读者=风清扬）
3. 卡片复用率指标标"待定义"（需检索/引用日志，本期只留接口不硬造）

## 验收

- `python full-library-rescan.py --health` 一条命令出七指标报告（附输出）
- 与 W3 基线数字可对账（draft 798/2865 等）
- 欧阳锋终审；commit 入档

---

## 追加（2026-08-22 王语嫣）：第八指标——未登记建议书数

> 来源：PROPOSAL-PENDING 自动登记改造（#421 追加节，老朱 08-22 拍板「想犯错也犯不了」）的兜底层。

- **指标**：未登记建议书数——`60_feedback/diagnosis/` 内命中三元组（`audience: 王语嫣` + `status: pending_orchestration`）但未在队列 PROPOSAL-PENDING 段登记的文件数，目标 = 0
- **口径纪律**：与 #421 扫描器同一份检出逻辑（yaml.safe_load，E017），健康报告只读计数、不代登记（登记动作归 #421，职责不混）
- **验收追加**：健康报告含第八指标行，附输出；与 #421 投递验收用同一份测试建议书交叉验证计数一致
