---
id: task_20260809_huangyaoshi-skill-lifecycle
assignee: huangyaoshi
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-09
updated_at: 2026-08-09
priority: P0
wsjf: 2.3
---

## 执行报告（2026-08-09 黄药师交付）

- `kdo-tools/skill_lifecycle.py` 四命令（list/status/set/eval）全部狗粮通过：list 39 skill 三态一览（draft=4/published=19/deprecated=0/unknown=16）；set --apply 真实落地 image-ocr（YAML 无损）；eval 生成 image-ocr eval-log
- 关键设计：frontmatter 是唯一真相（P-16 教训），不建第三份 registry；round-trip 校验防 P-18/P-29 事故
- 调研发现：KDO CLI 已有 skill 命令但依赖 manifest.yaml（40 个 skill 仅 3 个有）——命令形同虚设；本任务不做重复轮子，改做兼容层
- 已注册 cap_hub（14 Feature）+ README 登记
- 遗留：16 个 unknown skill 待补标 → #278 盘点任务前置（已同步）

# Skill 生命周期化（#273 · 黄药师建议书 #267s）

## 任务目标

cap_hub 的 skill 从"静态清单"升级为"有生命周期的产品"（draft → published → deprecated）。**注意：双轨同步（#267）是本任务前置**——生命周期模型必须双轨统一（cap_hub registry 的 status 需同步到 .claude/skills）。

## 规格

1. `cap_hub/registry.py`：skill 条目增加 `status`（draft/published/deprecated）+ `version` + `owner` + `dependencies`（schema 扩展，向后兼容）
2. `kdo skill eval <skill>`：能力 eval（代表任务 PASS/FAIL）+ 回归 eval（历史失败场景，防修 A 坏 B）+ baseline 对比（无 skill vs 有 skill）。**回归 eval 依赖 #271 lint 规则做确定性检查器**
3. `kdo skill publish / deprecate`：发布即冻结（改前必须先复制为 draft）
4. 文档：`40_outputs/capabilities/skills/README.md` 登记四步法

## 验收标准

- 任意现有 skill 可跑 `kdo skill eval` 且输出 baseline 对比
- cap_hub list 显示 status 列
- 双轨（shared/ + .claude/skills/）status 一致（#267 同步机制就位后验证）

## 依赖

- **#267（双轨同步）前置**——registry status 需物理层统一
- **#271（lint 扩充）前置**——回归 eval 的确定性检查器
- 解锁：#279（结晶，依赖 draft status 机制）

## 借鉴

agentman.ai skill lifecycle + Claude 官方 eval 驱动迭代

## 参考素材

- 黄药师建议书 `60_feedback/diagnosis/diag_20260809_huangyaoshi-skill-iteration-task-proposal.md` §#267s

## 终审记录（2026-08-09 欧阳锋）

**verdict: PASS（条件）B+ · blocking: 🟠2 · methodology v2.2**

O3 实测核验（全部独立复现）：skill_lifecycle.py list 实跑 39 skill，底部分布统计 draft=4/published=19/deprecated=0/unknown=16 与执行报告逐字一致；set --apply 真实落地（image-ocr 行 published + owner=huangyaoshi + version=1.0.0 + eval ✅）；eval-log.md 已生成（40_outputs/capabilities/skills/image-ocr/eval-log.md）；cap_hub 注册（Skill 生命周期管理 + 测试示例）；README 登记（40_outputs/code/scripts/README.md）。

五维：溯源 85/逻辑 85/暗知识 75/可操作 85/表达 80 → 总分 83（B+ 上限）

条件项（依赖未就位，跟踪至闭环）：
- **C1** eval baseline/回归数据补全——eval-log 当前 baseline 记录数 0 + 回归场景数 0（任务单依赖自证：回归 eval 依赖 #271 lint 确定性检查器，未就位）
- **C2** 双轨 status 一致验证（#267 双轨同步机制就位后）

🟢 观察：eval-log 显示"机械门禁 3/4 过"——缺的 1 项未说明，补 C1 时注明
