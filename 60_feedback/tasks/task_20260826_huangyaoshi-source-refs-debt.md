---
id: 543
assignee: huangyaoshi
status: queued
updated_at: '2026-08-26T11:40:00+00:00'
version: v0.1
instance: huangyaoshi
code_files:
  - 90_control/scripts/check-source-refs.py
---

# #543 source_refs 死引治理：1024 条缺失存量 + 扫描器挂例行 + json 输出修复

- **任务号**：#543
- **状态**：queued
- **assignee**：huangyaoshi（lint 挂载+报告落盘；治理批次方案报王语嫣裁定）
- **优先级**：P1（ADUCIT 事件深挖实证：全库 4224 条路径类 source_refs 中 1024 条文件缺失=24% 死引率，原稿在 inbox 而卡片引虚空——「找不到原稿反复索要的根）
- **立项**：2026-08-26 王语嫣（老朱追问「原稿就在，为什么找不到」）

## 背景

check-source-refs.py 扫描器早已存在，但**没进任何例行**：不跑、不报、不拦。08-26 王语嫣实跑：2877 卡/5908 条 source_refs，1024 条文件缺失+8 条已知污染引用；src_id 类引用（如 src_20260531_ai-data-lecture-02）连 source_id_map.json 都未注册。工具存在≠在回路里——与通知矩阵教训同构。

## 任务

1. **修 json 输出 bug**（--json 输出 line 2245 格式错误，agent 消费面断的）
2. **报告落盘+挂例行**：扫描报告落 `60_feedback/analysis/`，挂周例行（或随 daily-audit-digest），缺失数>阈值报警
3. **死引分批治理方案**：1024 条按域/卡片 status 聚类出报告，参照 #426 分批模式提治理方案（reviewed 卡优先——已审卡带死引=终审漏项）；方案报王语嫣裁定后分批执行
4. **inbox 未归档检测**：死引中指向 00_inbox 的（原稿在 inbox 未入 raw 型，ADUCIT 同款）单独聚一类——这类修复成本最低（归档即可，不用补内容）
5. §3.19：新例行信号→同步通知覆盖矩阵

## 边界

- 本单只出报告+挂例行+提方案，不直接批量修卡（治理批次裁定后另立执行单）
- src_id 注册表（source_id_map.json）补登记机制是否在 pre-submit 挂钩，随方案一并报裁

## 验收

- json 输出修复实测；报告落盘+例行挂载证明；分类治理报告交王语嫣；欧阳锋终审
