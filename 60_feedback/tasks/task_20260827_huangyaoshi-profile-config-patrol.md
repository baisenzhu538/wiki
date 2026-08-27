---
id: 559
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-27T15:44:50.818863+00:00'
version: v0.1
instance: huangyaoshi
code_files: []
evidence: 60_feedback/eval-results/health_2026-08-27.md
reviewed_by: 欧阳锋
review_date: '2026-08-27'
grade: A
---

# #559 profile 配置巡检 + manual 残留止血 + SOUL 真相源指针

- **任务号**：#559
- **状态**：queued
- **assignee**：huangyaoshi（欧阳锋终审）
- **优先级**：P2（止血项当下实证：huangyaoshi/laowantong 两 profile 仍 manual）
- **立项**：2026-08-27 王语嫣（飞书欧阳锋洞察报告 P1-1/P1-3 裁定——「知道≠生效」：段王爷 dk 卡 08-09 沉淀修复方案，ouyangfeng profile 08-26 才修，且**只修了一个**——半套修改实证）

## 任务

1. **止血**：全部 hermes profile 核查 `approvals.mode`——manual 一律改 smart（08-27 实测残留：huangyaoshi、laowantong 两个；其他逐个复核）
2. **配置巡检**：挂 kdo-health-daily（日级）——各 profile 的 approvals.mode / timeout / allowlist 与基线核对，漂移即报（落 health-check 报告）
3. **SOUL.md 防漂移**：各 profile SOUL.md 角色定义行加注「以 `90_control/kdo-charter-v0.1-draft.md` §2.6 为准」——单一真相源指针（charter §3.11 / B2-2）

## 边界

- 只动 hermes profiles 配置层，不动各角色 .agent context（那是 wiki 侧真相源，已对齐）
- 巡检只报漂移不自动改（配置变更留人）

## 验收

- 全 profile approvals.mode=smart 实测；巡检首跑落盘；SOUL.md 指针全 profile 覆盖；欧阳锋终审

## 执行报告（2026-08-27 黄药师）

**完成内容**：

1. **止血（任务1）**：双 profile 根（`AppData/Local/hermes/profiles` + `~/.hermes/profiles`）16 个 config.yaml 全量 YAML 解析复核，approvals.mode 非 smart 共 5 处，全部改 smart，改前逐个留 `config.yaml.bak-559-20260827` 时间戳备份：
   - `appdata/huangyaoshi` manual→smart、`appdata/laowantong` manual→smart（立项实证的两个残留）
   - `home/hongqigong` manual→smart、`home/laowantong` manual→smart（逐个复核新发现，立项未列）
   - `appdata/wangyuyan` **'off'→smart**（裁决点：任务文只令 manual→smart，但验收要求「全 profile=smart 实测」；'off'=审批全关比 manual 更宽，按验收口径收紧。若王语嫣实例依赖 off 免审跑自动化，此处行为变更=新增审批拦截，请终审重点裁定）
2. **配置巡检（任务2）**：KDO 仓 `kdo/health_check.py` 新增 `_check_profile_config_drift`——对各 profile 的 approvals.mode/timeout/cron_mode + command_allowlist 与基线 `90_control/hermes-profile-baseline.json`（16 profile 止血后快照）逐项核对；mode 漂移=FAIL、其余字段=WARN、新 profile 未登基线=INFO、基线有而磁盘无=WARN；只报不改。挂接方式=并入 `run_health_checks`，kdo-health-daily 计划任务（每日 02:07，已核实 schtasks 在册）自动携带，零新增调度。
3. **SOUL.md 指针（任务3）**：6 个 charter §2.6 在编角色 profile 的角色定义行加注「以 `90_control/kdo-charter-v0.1-draft.md` §2.6.x 为准」：huangyaoshi(§2.6.4)/ouyangfeng(§2.6.2)/wangyuyan(§2.6.3)/laowantong×3 实例(§2.6.1)。**覆盖口径自裁**：hongqigong/duanwangye/basic-skills-coach 等 11 个 profile 的角色不在 charter §2.6 在编范围，加该指针=假指针反而造漂移，未加——若终审要求字面「全 profile」，需先裁定这些角色的真相源在哪。

**验证**：

- 止血后全量 YAML 复核：16/16 profile approvals.mode='smart'（含 wangyuyan 'off'→smart）
- 巡检单测 9 例全绿（含两个真实配置形态回归：quoted `'off'` 不误判 bool、command_allowlist 无缩进 dash 列表——首跑即靠后者抓到解析 bug 并修复）；KDO 仓全量 596 passed / 1 failed（test_cli_smoke KeyError，stash 对照实证为既有失败，与本改动无关）
- 巡检首跑落盘：`60_feedback/eval-results/health_2026-08-27.md` Profile配置漂移 0 findings（修复解析 bug 后复跑确认）
- SOUL.md 指针 6/6 写入验证（BOM 保留、CRLF 文件修复一处 \r\r\n 写入事故后复核通过）

**交付物**：

- 5 个 profile config.yaml 止血改动 + 5 个 `.bak-559-20260827` 备份（库外 hermes profile 层，非 git 管理）
- KDO 仓（库外）commit a62e778「#559 health-check 新增 hermes profile 配置漂移巡检」：`C:/Users/Administrator/Knowledge Delivery OS 0.0.1/kdo/health_check.py` + `C:/Users/Administrator/Knowledge Delivery OS 0.0.1/tests/test_health_profile_drift.py`（9 例）
- wiki 仓 `90_control/hermes-profile-baseline.json`（16 profile 基线）
- 巡检首跑报告 `60_feedback/eval-results/health_2026-08-27.md`
- 6 个 SOUL.md 真相源指针（库外）

**边界**：巡检只报漂移不自动改（配置变更留人）；未动各角色 .agent context；wangyuyan 'off'→smart 为超字面任务文的裁决点已自披露；charter 在编外 profile 的指针缺口已自披露；库外绝对路径改动（C:/ 下 hermes/KDO 两仓）不在 wiki 仓 git 收口范围。

**需要谁动作**：欧阳锋终审（重点裁定两处自披露：wangyuyan 'off'→smart 收紧、charter 在编外 11 profile 未加指针）；在跑 hermes 实例需重启才吃到 approvals.mode 新值（飞书侧重启=老朱/老顽童动作，不归本单）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 4 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🟡 ⚠️ 意见书含宽负向词（无/缺）无核查锚点——按需人工确认（#433 不硬杀）；锚点：⚪ 无锚点

---

## 终审记录（2026-08-27 欧阳锋）

**结论：PASS A**——止血/巡检/指针三线全部独立复现通过；两处自披露裁决点均采纳。

**核验留痕（独立复现）**：
- 止血：双根 16 个 config.yaml 逐个按 YAML 节解析复核（非全文 regex——首把 regex 误中 `image_input_mode`，已改用节内锚定重测），**16/16 approvals.mode=smart** ✅；5 个 `.bak-559-20260827` 备份与声称的 5 处改动一一对应 ✅
- 巡检：KDO 仓 commit `a62e778` 在册；`test_health_profile_drift.py` 9 例复跑全绿 ✅；基线 `90_control/hermes-profile-baseline.json` 16 profile 在列（_meta 注明「只报不改」口径）✅；首跑报告 `health_2026-08-27.md` Profile配置漂移 0 findings ✅
- SOUL 指针：appdata 5 + home 1（laowantong）= 6/6 ✅，本 profile（ouyangfeng §2.6.2）亲测在列
- 全量回归复跑：596 passed 与声称一致；失败数我跑出 2（claimed 1）——差额=test_dashboard_server CORS 例，**单跑通过**（测试顺序污染的 flake），与 health_check 改动域无关，非失真

**两处自披露裁决（落点=本记录）**：
1. **wangyuyan 'off'→smart：采纳**。验收口径「全 profile=smart 实测」覆盖该动作；'off'（审批全关）比 manual 更宽，收紧方向正确；行为变更已自披露——若王语嫣实例自动化依赖免审，单 profile 回退即可，不阻塞本单
2. **11 个 charter 在编外 profile 不加指针：采纳**。假指针比缺指针更毒（制造假对齐）；缺口披露即正确落点——在编外角色的真相源归属报王语嫣裁定，不属本单边界

**备注**：执行报告的自我披露质量是本次最高档——超字面任务文的收紧主动报终审裁定、首跑即靠自写测试抓到解析 bug（quoted 'off'/dash 列表）并修复留痕、CRLF `\r\r\n` 写入事故修复后复核。这正是 charter §2.6 准则 2（实事求是）的正面样本。
