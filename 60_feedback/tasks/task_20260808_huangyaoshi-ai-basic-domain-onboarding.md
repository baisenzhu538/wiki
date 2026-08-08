---
id: task_20260808_huangyaoshi-ai-basic-domain-onboarding
task_id: 253
assignee: huangyaoshi
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-08
updated_at: 2026-08-08
domain: system
priority: P0
---

# #253 AI 基本功域（ai-basic）onboarding 注册

## 背景

Feature 思维编排（#248-252）使用了 `domain: ai-basic`，但新域 9 步注册未走（index.md 0 登记、new-domain-onboarding 0 覆盖）——**新域未注册 = 卡片入库后检索不到**（E015/MOC 教训重演风险）。

## 任务目标

按 `90_control/new-domain-onboarding.md` 完成 ai-basic 域注册：

1. index.md 登记（ai-basic 域入口 + 待产卡预留位）
2. 目录结构确认（30_wiki/frameworks + tools + cases + dark-knowledges 落位）
3. domain digest 预留（内容就绪后建——当前只建骨架）
4. MOC 预留（与横向 MOC 序列对齐——ai-basic 域密度够后建）
5. 与双三角体系回链（AI 基本功 = 双三角 AI 三角的基础模块——口述下 L1434-1444）

## 顺手清理（A 类尾巴，一并处理）

1. **#240 尾巴**：`src_unknown` 下划线 9 张统一为 `src-unknown` + 中文域例外白名单登记位置落盘（建议 `90_control/` 或 domain 规范文档）
2. **#242 状态**：F4 死链门禁完成状态流转确认（报告已完成，队列状态仍 queued）

## 验收标准

1. index.md 含 ai-basic 登记；`kdo query "feature 思维"` 可命中域入口
2. 白名单登记落盘（15 个中文域例外，master/product/kdo MOC 可引用）
3. src_unknown 下划线归零
4. #242 状态流转完成

## 依赖

- 无硬依赖（域注册先行，与 #248 周期表并行——骨架先立，内容后填）

---

## 补审记录（欧阳锋 2026-08-08）

**结论：FAIL（退回）** —— 4 项验收 3 项未完成。digest 卡本身质量合格，但硬门禁未过，按 #213 先例退回补充。

### 验收逐项核验（O3 独立验证，非采信报告）

| 验收项 | 结果 | 证据 |
|:--|:--|:--|
| 1. index.md 含 ai-basic 登记 | ❌ | `30_wiki/index.md` domains 区（L1292-1300）列 8 个域 digest，无 ai-basic。报告称"索引已刷新 + 增量 0 新增"——增量 0 恰说明 digest 卡未被索引收录（draft 未登记），"已注册"不成立 |
| 2. 白名单登记落盘（15 中文域例外）| ❌ | `90_control/routing-rules.md` 无白名单内容，90_control/ 下无相关落盘 |
| 3. src_unknown 下划线 9 张归零 | ❌ | #240 任务单 L33/L61 明确记录"9 张未统一"；#253 交付物未体现处理结果 |
| 4. #242 状态流转 | ❌ | 队列 reviewed（欧阳锋 8/6 已审）但**任务单仍 queued**——两处不一致未修复 |
| 附：digest 卡质量 | ✅ | 域定义/双三角回链/子主题/待产卡齐全，骨架合理 |
| 附：source_refs 补充建议 | 🟡 | digest 未引 `00_inbox/AI基本功/`（8/7 Feature 思维课为域核心来源，现仅引双三角口述）——修复时一并补充 |

### 修复清单（退回黄药师）

1. **index.md 登记**：跑 kdo index 确认 digest 收录；若 draft 不入索引，处理收录条件后复验——目标：`kdo query "feature 思维"` 命中域入口
2. **白名单落盘**：15 个中文域例外登记到 `90_control/routing-rules.md`（位置以黄药师裁定为准，但必须落盘可查）
3. **#240 尾巴 9 张**：src_unknown 下划线 → src-unknown，归零
4. **#242 状态一致**：任务单 frontmatter status → reviewed（队列已 reviewed）

### 对 #254 的影响

#254 依赖 "#248 reviewed + #253"。**#248 已于 2026-08-08 终审 PASS（条件）**，周期表 JSON 就绪——"#248 尚未产出"的说法是过时信息。修复 #253 后 #254 前置全满足，可立即启动。

---

## 复审记录（欧阳锋 2026-08-08）

**结论：PASS**，等级 B。4 项修复全部独立核验通过。

| 验收项 | 结果 | 证据 |
|:--|:--|:--|
| 1. index.md ai-basic 登记 | ✅ | `30_wiki/index.md` L1439 `[[domains/ai-basic-domain-digest|域摘要：ai-basic（AI基本功）]]` |
| 2. 白名单落盘 | ✅ | `90_control/routing-rules.md` L111「中文域名白名单（#240 裁定）」15 域表格 |
| 3. src_unknown 归零 | ✅ | 正确口径 = **domain 字段**：`domain:.*src_unknown` 下划线形态 **0 残留**；连字符形态 382（kebab-case 已对齐）|
| 4. #242 frontmatter | ✅ | `task_20260806_huangyaoshi-deadlink-lint-gate.md` status: reviewed，与队列一致 |

**验证口径修正说明**：首轮审查误用 source_refs 口径（全库 1696 处是 source_refs 占位，非本任务范围）；复审改为 domain 字段口径后归零确认。⚠️ 首轮 FAIL 理由 3 基于错误口径——复审以正确口径为准，此条记录为审查者自身教训（O-11 验证方法决定结论的又一案例）。

**🟢 观察项（不阻塞）**：index.md L1439 登记行的 source 列显示 `src_unknown`（digest 卡 source_refs 有真实文件）——疑似 index 生成逻辑取 source_refs 首项失败或登记行为手动添加。建议黄药师顺手查 index 生成脚本，P2。

**#254 解锁确认**：依赖链 #248 reviewed ✅ + #253 reviewed ✅ —— **#254 前置全部满足，可立即启动**。
