---
id: 548
assignee: huangyaoshi
status: queued
updated_at: '2026-08-26T23:10:00+00:00'
version: v0.1
instance: huangyaoshi
code_files:
  - kdo-tools/l1_capture.py
---

# #548 trace-index 按日轮转 + 自我喂养排除（无界增长治理）

- **任务号**：#548
- **状态**：queued
- **assignee**：huangyaoshi（欧阳锋终审）
- **优先级**：P2（不阻断，但 153MB 且日增 ~50MB，一个月吃掉 5000MB 红线 30%）
- **立项**：2026-08-26 王语嫣（风清扬建议书 diag_20260826_fengqingyang-capsule-infra-self-audit 裁定：择案 **B 按日轮转**——A「取消索引」会静默废掉 append 式历史回溯的设计意图（#491 配套），find 只有当前态替代不了历史；B 保意图+治增长）

## 背景

`D:/KDO-memory/L1-full/trace-index.md`（l1_capture.py:295 写入）无界增长：08-26 01:00 实测 106MB → 22:37 实测 153.2MB（~22h +47MB），活跃层总量 282MB，索引占 54%。且 trace-index 自身躺在 L1-full 里、每拍 mtime 必变 → 被下一轮采集追加，自我喂养。

## 任务

1. **按日轮转**：trace-index-YYYY-MM-DD.md 当日卷追加，跨日开新卷；旧卷随 #523 L1 日归档 zip 走（活跃层只留当日卷）
2. **自我喂养排除**：trace-index*.md 排除出 l1_capture 采集面（索引不进采集对象清单）
3. 存量 153MB 单卷：切为归档首卷处理（不删，归档保留历史）
4. 回归：模拟跨日 + 验证活跃层只留当日卷 + 采集面不含索引自身

## 边界

- 不动 trace-index 记录格式（路径|mtime|size），只动切分与排除
- 不改 L1 采集其他逻辑；与 #547 同文件区（l1_capture.py），施工顺序自取但分开 commit

## 验收

- 跨日轮转 + 排除自我喂养 + 存量归档，回归用例全过；l1-size.log 次日拍体积回落可观测；欧阳锋终审
