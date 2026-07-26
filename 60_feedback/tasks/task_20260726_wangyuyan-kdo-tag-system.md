---
id: task_20260726_wangyuyan-kdo-tag-system
task_id: 206
assignee: huangyaoshi
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-07-26
phase1: done
notes: "Phase 1 PASS——标签自动推断基线建立，覆盖率96%。Phase 2/3待王语嫣编排。scaffold模板(#2)+lint规则(#3)待黄药师补充。"
created_at: 2026-07-26
updated_at: 2026-07-26
domain: system
priority: P0
source: 00_inbox/半肥猫月白老朱线下聚会/ + 飞书王语嫣标签缺口诊断
---

# KDO多维标签体系恢复

## 背景

半肥猫的Agent体系靠多维标签（行业/场景/成熟度/输出类型）快速路由到正确Skill。KDO当前只有`domain`单维分类——244张framework+106个skill靠关系网检索，规模越大噪音越大。

`90_control/tag-registry.yaml`（4维27标签）已设计但归档。恢复它。

## 任务

| # | 动作 | 执行者 | 说明 |
|:--|:--|:--|:--|
| 1 | 恢复 `tag-registry.yaml` | 黄药师 | 从归档恢复，评审4维27标签是否仍适用，增补`discoverable_by`对接 |
| 2 | `kdo scaffold` 模板新增 tags 字段 | 黄药师 | 新卡生成时默认带空tags，lint检查非空 |
| 3 | `kdo lint` 新增 tags 检查 | 黄药师 | 新卡 tags 非空→WARNING（同#199定位声明级别），存量卡不触发 |
| 4 | 存量卡补标签策略 | 黄药师（定规则） | 不排批量任务——该卡因其他原因返工时顺手补。与#199牌L8同逻辑 |

## 标签维度参考（从半肥猫体系+tag-registry提取）

| 维度 | 示例值 | 用途 |
|:--|:--|:--|
| 场景 | 诊断/执行/参考/审查 | Agent判断何时调用此卡 |
| 角色 | 一号位/管理者/执行者/设计师 | 谁用这张卡 |
| 成熟度 | draft/reviewed/stable/deprecated | 可信度信号 |
| 输入→输出 | 口述→框架/案例→工具/理论→操作 | 素材类型→卡类型映射 |

## 验收

1. `tag-registry.yaml` 已恢复，维度≥3
2. `kdo scaffold` 生成的新卡含tags字段
3. `kdo lint` 对新卡缺tags报WARNING
4. 存量卡不触发——不排批量返工

## Phase 1 ✅ 已完成

黄药师完成自动推断：2,337张卡标注 audience + scene + skill-level 三维标签，覆盖率 9.9%→96%。`tag-registry.yaml` 已恢复并扩展至 27 维度。

## Phase 2：高价值卡人工精标（王语嫣+老顽童，4周自然覆盖）

| 优先级 | 对象 | 数量 | 方式 |
|:--|:--|:--:|:--|
| P0 | framework卡 | ~30张 | 老顽童返工时顺手加 method+industry+value-tier |
| P0 | domain-digest/MOC卡 | ~10张 | 同上 |
| P0 | agent-spec卡 | 8张 | 同上 |
| P1 | 新域首卡（近30天） | ~15张 | 王语嫣诊断时标注建议维度 |
| P2 | tool卡 | ~960张 | 等自然返工，不专门排 |

**王语嫣动作**：每份任务单的卡片规格节追加一行"建议标签：xxx"。老顽童建卡时写入 frontmatter。

**欧阳锋动作**：Phase 0 扫描新增"P0卡是否有 method 标签？"提醒（🟡不阻断）。

## Phase 3：pre-submit 强制门禁（黄药师，等覆盖≥80%后激活）

门禁规则见 `60_feedback/diagnosis/diag_20260726_huangyaoshi-tag-system-phase2-3.md` §3。黄药师先写 `_check_tags()` 函数，暂不激活。4周后统计P0卡覆盖→达标激活。

## 边界

- **不批量补存量卡标签**——该卡返工时顺手补
- **不替代domain**——tags补充domain，不替代
- **门禁等覆盖达标再开**——避免存量warning海啸
