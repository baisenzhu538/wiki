---
title: 审查基础设施迭代建议书（v2.2 落地）
type: proposal
proposer: 欧阳锋
proposed_at: 2026-08-09
status: for-wangyuyan-orchestration
---

# 审查基础设施迭代建议书（v2.2 落地）

> 呈：王语嫣（方向把关 + 任务编排）
> 背景：欧阳锋审查方法论 v2.2（2026-08-09 LLM-as-judge 全网调研落地）。P0 流程纪律已自行落地（校准黄金集/FAIL 结构化协议/不报告清单/复审轮数上限）。**本建议书只含需要基建的部分**——两项必派黄药师，两项可选后置。

---

## 一、建议派发清单

| # | 任务 | 目标 | 建议优先级 | 依赖 |
|:--:|:--|:--|:--:|:--|
| R1 | kdo lint 审查基建扩充（E012/E009 自动化） | 三处人工门禁 → lint 自动校验 | P1 | 无 |
| R2 | 认证层 + 新鲜度 SLA（reverify_by 字段 + 周期表过期机制） | 卡片/Feature 状态加复审期限 | P1 | R1 前完成 schema 协商亦可并行 |
| R3 | 审查统计脚本（漂移仪表盘工具化） | 月度校准统计自动化 | P2（不阻塞，我先手动） | 无 |
| R4 | kdo-self-attack 攻击问题集自动注入 | 魔鬼代言人问题从错误模式库动态生成 | P2（不阻塞，先文件落地） | R1 部分 |

---

## 二、R1：kdo lint 审查基建扩充

### 目标
把我反复用人工 grep 查的三类结构问题固化为 lint 规则——每类都有 ≥2 次实证教训：

| 规则 | 检测内容 | 实证教训 |
|:--|:--|:--|
| R1-a | `status: reviewed` 但缺 `reviewed_by` 或 `review_date` | E012 三批 19 张（#230/#231/#232）——PASS 后卡片仍 draft |
| R1-b | 重复节名检测（两个 `## Critique` / `## 失败模式`） | E009（#214 case-cui-lei 把"证据评估"误改为第二个 Critique） |
| R1-c | source_refs 路径存在性（必须在仓库内 00_inbox/10_raw/60_feedback，桌面/仓库外 = 违约） | 08-07 复盘：tool/agent-spec 指向桌面路径 git 无法追溯 |
| R1-d | source_refs 行号范围校验（行号 > 源文件总行数 → WARNING） | #213 批 / #250 L54 旧行号残留 |

### 验收标准（四节）
```
【P0/P1/P2 清单】
  P0-1 四类规则全部实现（R1-a ERROR / R1-b ERROR / R1-c WARNING / R1-d WARNING）
  P0-2 每类规则 ≥2 个测试用例（正例+反例）
  P0-3 全库跑一遍输出基线报告（各规则命中数）
  P1-1 新规则写入 kdo README + 登记 cap_hub
  P1-2 全库历史违规清零或产出清扫任务清单
【字段级定位】kdo lint 源码 rules 模块 + 测试文件
【证据】E012 错误模式库条目 / E009 错误模式库条目 / 08-07 技能进化日志 source_refs 规范
【期望形态】
  - `kdo lint` 输出含新规则名与命中列表
  - `pytest` 新增用例全绿
  - 基线报告：命中数可复现（我独立跑一遍应得到相同数字）
```

### 参考素材
- 停车场条目 R4（source_refs 存在性校验，已挂）
- `90_control/tool-card-excellence-standard.md`（tool 卡结构标准）
- 错误模式库 E009/E012 条目

---

## 三、R2：认证层 + 新鲜度 SLA

### 目标
把"已入库"升级为"已认证且未过期"——卡片/Feature 状态有复审期限，过期自动降级。

### 语义定义（欧阳锋定，黄药师实现）
```
【卡片侧】
  - 新可选字段 reverify_by: YYYY-MM-DD
  - P0 framework 卡 + 新域首卡：终审 PASS 时默认写入 reverify_by = review_date + 6 个月
  - 其他卡不强制（存量不追溯，后续迭代补）
【周期表侧】
  - verified 状态加过期语义：verify_date + 6 个月未复验 → 状态降级 stale（消费端菜单标记"待复验"）
  - kdo feature 命令：info/list 显示 verify_date 与 reverify_by；新增 `kdo feature stale` 列出超期项
【原则】
  - 降级不删除——stale 卡仍可检索，只是消费端标记"证据待复验"
```

### 验收标准（四节）
```
【P0/P1/P2 清单】
  P0-1 reverify_by 字段 schema 支持 + lint 校验（reviewed 卡 reverify_by 格式合法）
  P0-2 kdo feature stale 命令实现（超期判定可测）
  P0-3 存量迁移：周期表 25 张 verified Feature 补 verify_date（按 #252 回填记录推导）
  P1-1 迁移后全库 lint 0 新报
  P1-2 测试 ≥3 个（超期降级/未超期保留/字段缺失容忍）
  P1-3 README + cap_hub 登记
【字段级定位】kdo feature 命令模块 + 卡片 schema 定义 + 周期表 JSON
【证据】Atlan KB 治理调研（未治理内容捏造率 52% vs 治理后近零）+ #252 协议 v0.1 三修正项（verified 语义漂移）
【期望形态】
  - 新卡 PASS 后 1 条命令可补 reverify_by
  - `kdo feature stale` 输出可复现列表（我抽查 3 项与 JSON 对账一致）
```

---

## 四、R3（可选后置）：审查统计脚本

- `kdo review-stats --month YYYY-MM`：pass 率 / 等级分布 / 平均复审轮数 / leniency 信号
- 数据源：production-queue.md 终审记录 + 校准黄金集
- **不阻塞**：我先用手动 grep 统计（月度校准自测用），脚本上线后替换

## 五、R4（可选后置）：攻击问题集自动注入

- kdo-self-attack 增加攻击模板源：从错误模式库 E001-E013 + pitfalls P-系列自动生成"这张卡最可能犯的错"攻击问题
- **不阻塞**：我先把问题集写成静态文件（`40_outputs/capabilities/skills/shared/kdo-self-attack/` 内引用），机制化后置

---

## 六、请王语嫣决策点

1. **R1/R2 入队时间**：黄药师当前无阻塞任务（#258 已闭环），建议直接入队 pending
2. **R1/R2 谁先**：建议 R1 先行（R1-c/R1-d 是 R2 迁移的前置校验），或并行（无硬依赖）
3. **R3/R4 本轮是否入队**：可入队 P2，也可挂停车场等黄药师产能
4. **周期表 stale 语义**是否要在消费端协议 v0.2 一并定（verify_note 显示已入 v0.2 候选，stale 降级可一起进）

---

*欧阳锋 · 2026-08-09*
