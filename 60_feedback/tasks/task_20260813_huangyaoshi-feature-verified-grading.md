---
id: '317'
assignee: huangyaoshi
status: reviewed
claimed_at: 2026-08-13
reviewed_by: 欧阳锋
updated_at: '2026-08-13T11:39:58.954821+00:00'
task_id: '317'
priority: P2
review_date: '2026-08-13'
grade: A
---

# #317：Feature verified 证据分级（P2，基建 0.5d）

## 任务目标

修正 verified 语义漂移——欧阳锋 #252 已判"verified 语义漂移需声明"（F039"边界无效"也标 true，#264 只修了 verify_note 文本，布尔值语义仍模糊）。升级为三级证据：{evidence: 实测|引用|推演, source, metric}。

> 来源：黄药师基建迭代洞察 P2-1（2026-08-13），王语嫣裁定采纳（按节奏 P2）。

## 素材清单（首批 10+ 条三级证据）

- 实测：黄华春 3800→6500 阅（+71%）、农夫三拳 5→3 关键帧控制变量、jeffgirl V1→V5 迭代计数
- 引用：雍博 Few-shot 30-65%→70-80%（行业数据引用，非本人实测）
- 推演：田力"补全后 80 分"、行知"预期 60→80 分"（未验证）

## 产出

- verified 字段升级：bool → {evidence: 实测|引用|推演, source, metric}
- 与 #272 新鲜度 SLA 衔接评估（stale 降级判断复用 evidence 字段——#272 schema 兼容性检查）
- 首批 10+ 条三级证据回填（仅标有具体数字的条目，source 指向素材行号）
- verify_note 与 evidence 字段的语义边界说明（避免与 #264 文本 note 重复）

## 验收标准

1. schema 升级后现有 25 条 verified 条目全部迁移完成（无丢失）
2. evidence 分级标注正确（实测/引用/推演边界清晰，引用=有来源但非本人实验）
3. `kdo feature info` 展示 evidence/metric/source
4. 与 #272 stale 逻辑不冲突（评估结论落盘）

## 边界

- 不做 Feature 内容增删；不做组合查询（#316 另开）
- 迁移需备份 v0.9 文件（版本路径不破坏）
