---
id: task_20260823_laowantong-role-special-ouyangfeng-完成报告
title: "#441 欧阳锋岗位说明书定稿——完成报告"
type: completion_report
assignee: laowantong
created_at: 2026-08-23
status: pending_review
---

# #441 角色专场第二场：欧阳锋岗位说明书定稿——完成报告

## 一、产出

升级 `30_wiki/agent-specs/agent-spec-ouyangfeng-reviewer.md`（约 50 行旧版 → 7671 字节五要素可执行卡，只升级不推倒，created_at 08-19 保留 + updated_at 08-23）。

## 执行报告

**文件清单**：`30_wiki/agent-specs/agent-spec-ouyangfeng-reviewer.md`（唯一改动文件）；本报告。

**完成内容**：欧阳锋岗位说明书 v1.0——五要素齐全（内核/职责/边界/工作流/Trigger+Interface）+ G1/G2 两铁律 + 自迭代双回路（内省/外部/曝光三栏）+ 审查端新门禁（F-035 + #433 存在性核查锚点 + KF-024 三要件抽点）。

**验证**：`kdo pre-submit -f 30_wiki/agent-specs/agent-spec-ouyangfeng-reviewer.md` → Passed 1 / Failed 0 / ✅ PASS（YAML/WIKILINK/DOMAIN/DK_SECTION/OUTLINK/POSITION/SOURCE_REACHABILITY 全 0；ALIASES 1 warning 为 source 文件名——F-040 禁路径词口径下预期内，不阻塞）。`kdo index` → Indexed 4087。

**未做项**：不改《KDO 基本法》正文；其余角色专场（黄药师/风清扬/王语嫣/老朱）不提前拆单；老朱终稿拍板后才由王语嫣并入 §2.6.2。

**需要谁动作**：欧阳锋终审（结构与证据核验；涉及自身边界放宽表述须标「需老朱拍板」）；老朱终稿拍板后开下一场（黄药师）。

---

## 二、验收对照

| 验收项 | 结果 |
|:--|:--|
| 五要素齐全 | ✅ 内核/职责/边界/工作流/Trigger+Interface 独立节 |
| Trigger+Interface | ✅ Trigger=REVIEW-PENDING 段有行即审；上游=王语嫣任务单/老朱直令；下游=老顽童返工/王语嫣再编排/老朱终局拍板 |
| 终审判「做得好不好」 | ✅ 内核/职责 1（PASS 必给等级，禁止只写 PASS） |
| 审而不改 | ✅ 边界 1（不动手/不代提交/不改别人卡片）+ 内核写审分离 |
| 批次验收≠整单终审 | ✅ 职责 6 + 工作流 6 + 基线用例 3 |
| 审查者不直接编排 | ✅ 边界 2（立项须走王语嫣复核，#409-411 教训） |
| 建议书抽 1 条回查数据层 | ✅ 职责 5（O0 溯源逐条对原文；建议书类文档回查数据层——幻影丢失事件增补） |
| F-035 + #433 门禁 | ✅ 职责 5 + 工作流 6（意见书落盘 + 负向判词 `**存在性核查**` 锚点） |
| KF-024 三要件抽点（#189 教训） | ✅ 职责 5（Synthesis 表 + Action Triggers + Critique 抽点） |
| aliases 禁路径词（F-040） | ✅ aliases 仅 6 条角色别名（欧阳锋/reviewer/终审官/审查者/终审执法者/ouyangfeng-reviewer），零路径词——#431 终审教训直接应用 |
| 自迭代双回路三栏不空 | ✅ 内省（误判率/黄金集 15→30）/ 外部（Anthropic evaluator 季度对标 + 最小动作）/ 曝光（spec diff/终审记录/技能日志）+ D4 不自放行边界 |
| 与 charter §2.1/§2.2 不冲突 | ✅ 欧阳锋=终审判"做得好不好"逐条对齐 |

## 三、边界说明

- 底本全消费：建议书 §角色 2 / charter §2.1/§2.2/§2.4/§2.6.1/§3.13 / ouyangfeng position B2-3 / #431 任务单终审记录（口径+aliases 教训）/ 旧 spec 全量吸收
- aliases 保持 F-040 干净：ALIASES 1 warning（source 文件名）为固有冲突，不加路径词（#431 终审"aliases 路径污染"教训）
- 未碰其他角色文件

## 四、遗留

- 待欧阳锋终审（结构与证据核验）；老朱终稿拍板后王语嫣并入 §2.6.2；下一场（黄药师）待老朱拍板

---

## 复审修复记录（2026-08-23 欧阳锋 FAIL 退回 → 修复）

**审查意见**：P1 spec 缺必写项「建议书断言回查数据层」（任务单动作 2 第 6 条）；其余全达标（aliases 干净/自迭代双回路/无自批扩权 ✅）。

**修复**：
- 职责节补第 7 条：建议书/诊断类文档终审必抽 ≥1 条建议节断言回查数据层（引 #418 幻影丢失裁定；例 #427 D 盘空间、#430 备份机制存在性——断言证据在数据层而非文档自述）
- 迭代日志同步补 v1.1

**复审证据**：`kdo pre-submit -f agent-spec-ouyangfeng-reviewer.md` → Passed 1 / Failed 0 / ✅ PASS；本次 complete **未走 --force**（F-034 五字段齐全直接过）。
