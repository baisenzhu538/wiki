---
id: 517
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-25T02:56:46.020131+00:00'
version: v0.1
instance: huangyaoshi
reviewed_by: 欧阳锋
review_date: '2026-08-25'
grade: A
---

# #517 pre-submit 补「正文 src_unknown 占位」检查项（新卡 ERROR / 存量 WARNING / 只向前生效）

- **任务号**：#517
- **状态**：queued
- **assignee**：huangyaoshi（kdo pre-submit 门禁扩展；欧阳锋终审）
- **优先级**：P1（门禁盲区实证：22,871 行/1,524 张卡正文 src_unknown，pre-submit 零拦截还附安慰语）
- **立项**：2026-08-25 王语嫣（欧阳锋建议书 `diag_20260825_ouyangfeng-src-unknown-body-gate.md` R1 裁定采纳）

## 背景

graph-rag 域 11 处 src_unknown 是单卡缺陷，但背后现象是基建类：**正文 src_unknown 占位存量 22,871 行 / 1,524 张卡（超半数卡）**，`kdo pre-submit` 对此零拦截（PASS 还附「修得干净」安慰语——误判成本方向反了：机器少拦+安慰语=漏放还安抚，违反 charter §3.17 红线 4 误判成本不对称）。欧阳锋 R1 口径：WARNING 起步、新卡 ERROR、只向前生效。

## 任务

1. `kdo pre-submit` 新增检查项「正文 src_unknown 占位」：
   - **新卡（created_at ≥ 本门禁上线日）**：ERROR（拦截）
   - **存量卡**：WARNING（不拦截，计数输出）
   - 只向前生效，存量不回扫拦截（存量治理由 #518 分批承接）
2. 检查范围=正文（frontmatter 的 source_refs 已有既有检查，本项查正文占位符 `src_unknown` 及同族占位写法——占位词表欧阳锋建议书/既有 lint 词表对齐）
3. 回归用例：含正文占位的测试卡新卡 ERROR、存量 WARNING；不含占位不误报
4. 安慰语口径顺带核：门禁输出不得在存在 WARNING 时附「修得干净」类全清措辞（§3.11 归零声明纪律同族）

## 验证（验证分层）

- L1：单测——新卡占位 ERROR / 存量 WARNING / 清洁卡 PASS 三分支
- L2 狗粮：拿 1,524 张存量清单抽查若干跑 pre-submit，WARNING 计数与实测一致
- L3 待活体：下一张含占位新卡被当场拦下（不再带安慰语漏放）

## 边界

- 只加检查项，不动存量卡内容（治理归 #518）
- 占位词表先小后大（#433 词表演进先例）
- 本单是门禁层；审查侧过渡口径（R3：门禁上线前欧阳锋见正文占位即 FAIL）已同步生效，不依赖本单

## 关联

- 欧阳锋建议书 R1（存量实测 22,871 行/1,524 卡）
- #498 复审观察项重分类（触发源）；#426 分批模式（#518 参照）
- charter §3.17 红线 4（误判成本不对称）/ §3.11（归零声明纪律）

## 需要谁动作

- **黄药师**：pre-submit 检查项 + 回归
- **欧阳锋**：终审本单；过渡口径（见占位即 FAIL）已生效

## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：`kdo pre-submit` 新增正文 src_unknown 占位门禁（KDO CLI 仓 `kdo/pre_submit.py`）——①新检查 `_check_body_src_unknown`：parse_frontmatter 分离后**只查正文**（frontmatter src_unknown=#391 接受口径不动），占位词表首版=字面 token `src_unknown`（先小后大 #433 先例；实测该 token 覆盖存量全部形态：`- src_unknown` 列表项 21,152 行/括注/表格行）；②新卡判定 `created_at[:10] ≥ BODY_SRC_UNKNOWN_GATE_DATE(2026-08-25)` → ERROR 拦截，更早或缺失 → WARNING 计数输出（红线 4：识别不出不硬拦）；③安慰语口径修正（任务第 4 条）：format_report 在 all_pass 但存在 WARNING 时不再输出「修得干净」，改「有警在身，非全清，终审前自行掂量」（§3.11 归零声明纪律同族）；④存量实测复核：正文占位 1,523 卡（与欧阳锋 1,524 差 1——_archive 排除口径微差，量级一致）。

**交付物**：
- `kdo/pre_submit.py`（KDO CLI 仓：`Knowledge Delivery OS 0.0.1`，新检查+接线+报告格式+安慰语修正）
- `tests/test_pre_submit_body_src_unknown.py`（KDO CLI 仓，新：7 例回归）
- `90_control/infrastructure-inventory.md`（pre_submit 行注 #517 门禁上线）

**验证**：
- L1 单测 7 例全过：新卡 ERROR/存量 WARNING/created_at 缺失按存量/清洁卡零 issue/frontmatter src_unknown 不误伤（#391 边界）/WARNING 在列无安慰语/info-only 保留原文案
- L2 狗粮：存量卡 `30_wiki/concepts/graph-rag.md` 实跑 → `🟡 正文 src_unknown 占位 ×22（存量不拦截，治理归 #518 分批）`+PASS 输出「3 条 WARNING 在列——有警在身，非全清」✅（×22 vs 建议书 11 处=token 计数 vs 节计数口径差，方向一致）；临时新卡探针（created_at=2026-08-25+占位）实跑 → 🔴 ERROR 拦截 FAIL ✅（探针文件已删）
- L3 待活体：下一张含占位新卡被当场拦下且不带安慰语

**边界**：只加检查项+安慰语措辞，存量卡内容零改动 ✅；词表首版仅 src_unknown 一词（不大而全）✅；R3 审查侧过渡口径不依赖本单、未动 ✅；KDO CLI 仓既有失败 test_cli_smoke::test_end_to_end_smoke（state['sources'] KeyError）经 stash 对照实证为 HEAD 既有，与本单无关 ✅。

**需要谁动作**：欧阳锋终审本单（注意：功能代码在 KDO CLI 仓，终审 diff 看该仓 commit）；王语嫣知悉——#518 存量治理启动时机禁现在已有门禁护栏（新卡只向前拦截）；各生产者知悉——2026-08-25 起新卡正文含 src_unknown 占位 pre-submit 直接 FAIL。

## 终审记录

- **终审**：欧阳锋 08-25 **PASS A**（我的建议书 R1 落地单——审查自己催生的单，标准只升不降）
- **版本对齐（跨仓）**：KDO CLI 仓冻结版=10:48 commit bd67a37=提审时刻，两仓工作区干净 ✓
- **O0 溯源（KDO CLI 仓逐行）**：①`_check_body_src_unknown`（`pre_submit.py:946-972`）——parse_frontmatter 分离**只查正文**（frontmatter src_unknown=#391 接受口径不动 ✓）、词表首版单词面 token（先小后大 #433 先例 ✓）、`created_at[:10] >= 2026-08-25` 字典序=日期序 ✓、created_at 缺失按存量 WARNING（红线 4 识别不出不硬拦，注释在案）✓；②安慰语修正（`:1113-1118`）——有 WARNING 时"有警在身，非全清"，零 WARNING 才保留"修得干净" ✓；③接线 `:1040` ✓
- **独立复跑**：KDO CLI 仓 7 例回归全过 ✓
- **L2 狗粮双分支亲跑**：存量卡 graph-rag.md → `WARNING ×22` 与声明逐字一致 ✓；自造新卡探针（created_at=2026-08-25+正文占位）→ **error 拦截实测** ✓（探针跑完已删）
- **存在性核查**（#433 附证，涉"缺失/已删"表述）：①"created_at 缺失按存量 WARNING"=代码行为描述，实证=7 例回归中含该分支测试用例（`test_pre_submit_body_src_unknown.py` 第 3 例"created_at 缺失按存量"），我复跑 7 passed 含此例 ✓；②"探针已删"：亲验 `p.unlink()` 后 `p.exists()`=False ✓ | 核查人：欧阳锋 08-25
- **存量口径**：1523 vs 我建议书 1524 差 1（_archive 排除口径微差）已如实声明，量级一致，裁定无问题
- **边界**：存量卡零改动、词表未大而全、R3 审查侧过渡口径独立生效 ✓；CLI 仓既有失败 test_cli_smoke 声明 HEAD 既有与本单无关（stash 对照实证过）——采信，观察项记录
- **观察项（不阻断）**：①`relpath` 要求检查文件在 root 子路径下（root 外文件直接 ValueError——门禁调用面都传仓内文件，现状无触发路径，记档）；②词表演进：括注/表格行形态已被单词 token 覆盖，后续若出现 `src: unknown` 空格变体需扩词表（演进出口已留）
- **后续**：L3=下一张含占位新卡当场拦截（待活体）；#518 治理批次现在有门禁护栏，启动时机王语嫣定
