---
id: 421
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-22T14:42:44.102521+00:00'
reviewed_by: 欧阳锋
review_date: '2026-08-22'
grade: A-
---
# #421 传送带探针（通知契约先定，探针后建）

- **任务号**：#421
- **状态**：queued
- **assignee**：huangyaoshi（单一实例；契约条款已拍板，本单含实现）
- **优先级**：P1（可先行项，O-3 前置已交付 #413）
- **立项**：2026-08-22 王语嫣（会诊 X-1 拍板）

## 通知契约（已拍板要素，本单成文）

- **频次**：低打扰批处理（每小时级，状态变化触发+定时聚合兜底）
- **两类信号区分**：新提审（REVIEW-PENDING 新增）vs 批次待续（分批任务 queued 待领）——不区分则通知变骚扰（欧阳锋）
- **状态口径**：只认队列状态机（queue_transition 输出为唯一真相源）
- **去重**：状态 id+已通知集合，幂等
- **不打扰红线**：无变化不发/夜间静默/聚合去抖
- **边界硬编码**：只通知、不领取、不裁决、不流转（watch_inbox 登记除外）

## 探针三处

①王语嫣探针（watch_inbox 新素材→推"待编排"）②老顽童探针（queued 新增→推"N 个可领取"）③欧阳锋探针（REVIEW-PENDING 新增→推"M 个待审"）

## 验收

- 契约文档落盘（90_control/）先于探针实现
- 探针实测：三处各触发一次真实通知（飞书通道），边界测试（探针试图领取/裁决=被拒）附输出
- commit 入档；欧阳锋终审抽"边界硬编码真实性"

---

## 追加（2026-08-22 王语嫣，老朱拍板）：PROPOSAL-PENDING 自动登记

> 追加不改上文（协议 4：queued 单优先追加说明节）。背景：08-20 欧阳锋建议书落盘 20 分钟靠老朱转达才发现；现行机制依赖"作者自登"=人肉纪律。老朱 08-22 拍板：按 B2-4「想犯错也犯不了」改为系统检测自动登记；**建议书投递点维持 `60_feedback/diagnosis/` 现状，不单开目录**。

- **扫描面（写死）**：`60_feedback/diagnosis/`；检出条件=frontmatter 三元组 `audience: 王语嫣` + `status: pending_orchestration`（文件名 `proposal-*` 为辅助信号）
- **解析纪律**：必须 `yaml.safe_load` 结构化解析，禁止 grep/正则读 frontmatter（E017）
- **登记动作**：命中且未在段内的 → 自动写入队列 PROPOSAL-PENDING 段一行（链接+一句话+日期），幂等去重；段改为自动维护（对称 INBOX-PENDING，加「勿手改」标注）；王语嫣复核立项后划掉的流程不变
- **边界不变**：自动登记属于 watch_inbox 同类豁免，探针仍只通知/登记，不领取、不裁决、不流转
- **配套门禁（同单交付）**：pre-submit 加规则——`proposal-*` 或含 `audience:` 字段的文件必须带齐三元组，缺字段拦截（写侧防漏标）
- **验收追加**：①构造一份带齐三元组的测试建议书落 diagnosis/ → 扫描器自动登记附输出；②构造一份缺 `status` 字段的 → pre-submit 拦截附输出；③两份测试文件测试后由王语嫣裁定处置

### 兜底（王语嫣侧，不占本单）

- 王语嫣收尾 mtime 终扫（协议 1 第四道防线）将 diagnosis/ 纳入输入目录扫描清单
- #425 健康度指标集加「未登记建议书数 = 0」一条（挂 #425 验收，本单不重复实现）

---

## 内容价值判断（#375 处置门禁补充节，2026-08-22 黄药师领取时补）

- **本任务为纯基建**：扫描器/登记/通知/门禁实现，**无任何素材处置动作**（不删、不改、不动 diagnosis/ 现有文件）
- 唯一涉及"处置"的是验收测试的两份构造建议书——由王语嫣裁定处置（任务单追加原文），本单只负责构造测试和报告
- 测试建议书为新建文件，非存量素材；测试后原地保留等王语嫣裁定，不自行删除
- 无删除动作，无需老朱逐件审批

## 追加二（2026-08-22 老朱拍板）：建议书/报告到达即时通知，与探针统一建设

> 背景实证：08-22 晚风清扬编排审计 17:29 落盘并规范自登，王语嫣直到老朱点破才知道——自动登记解决「不丢」，不解决「马上知道」。老朱拍板：到达通知编排进本单，与探针统一建设，不另起炉灶。

- **①王语嫣探针扩展为两路输入**：watch_inbox 新素材（既有）+ PROPOSAL-PENDING 新登记/新检出（新增）→ 即时推「新建议书待裁定」
- **统一建设硬约束**：同一扫描事件驱动「登记+通知」两个动作，**禁止建第二套扫描器**——检出逻辑单份，登记与通知同源，防两处口径漂移（E021/E028 同族教训）
- **信号分类**：通知契约「两类信号」扩为三类——新提审 / 批次待续 / **新建议书到达**；低打扰、幂等、不打扰红线同样适用
- **边界不变**：通知≠裁定——探针推给我，裁定制裁仍是我（B2-1）
- **验收追加**：构造测试建议书落 diagnosis/ → 段内自动登记 **且** 王语嫣侧收到即时通知，双动作同源附输出（登记与通知必须是同一次扫描的产物）

## 执行报告（2026-08-22 黄药师）

**交付物**：
1. **契约文档**：`90_control/conveyor-probes-contract.md`（先于探针实现落盘）——三类信号/调度/状态口径/边界硬编码/通道/同源纪律
2. **扫描器**：`kdo-tools/conveyor_probe.py`——单扫描器一次扫描事件驱动「检出→登记→通知」；队列 diff（queue_gate.parse_queue 只读）+ diagnosis 三元组检出（yaml.safe_load，E017）+ PROPOSAL-PENDING 自动登记（幂等）+ 飞书通知（配置驱动）
3. **pre-submit 三元组门禁**：KDO `pre_submit.py` 新增规则——含 `audience:` 字段的文件必须带齐三元组（audience: 王语嫣 + status: pending_orchestration），缺字段拦截
4. **测试**：`kdo-tools/tests/test_conveyor_probe.py` 5 测试（三元组检出/登记幂等/历史行保留/边界无流转能力/通知 dry-run）

**实测（附输出）**：
- **验收① 自动登记**：构造 `diag_20260822_probe-test-1-proposal.md`（带齐三元组）落 diagnosis/ → 扫描器检出并自动登记进 PROPOSAL-PENDING 段（幂等：重跑 registered=[]）；段头旧"作者自登"注释已迁移为"自动维护"标注（勿手改）
- **验收② pre-submit 拦截**：构造 `diag_20260822_probe-test-2-missing-status.md`（缺 status）→ `kdo pre-submit` 拦截：`建议书 status 必须是 pending_orchestration（三元组，#421）` + Missing required field: status
- **通知三类信号 dry-run**：重置 state 重跑——新提审 1（欧阳锋）/ 新 queued 7（老顽童）/ 新建议书 0（已登记）；**夜间静默实测生效**（22:0x 静默跳过，契约红线验证）
- **边界测试**：探针源码无 `import queue_transition`、无 claim/complete/review 函数（AttributeError 证明=试图领取被拒）；测试固化

**修复记录（实测抓出的 3 个缺陷当场闭环）**：
1. 去重键不统一（旧行完整路径 vs 新行文件名）→ 同文件重复登记 → 归一化键修复
2. 段内重复行清理逻辑误删同文件多条历史裁定记录（orchestration-audit 两条裁定）→ 从 git HEAD 恢复该行 + 策略改为"保留全部历史行，只防新增"
3. `_extract_section` 类缺陷（无；此单无）——保持诚实，仅前两条

**KDO 回归**：pytest 567 passed / 1 failed（`test_end_to_end_smoke` KeyError 'sources'——state.json 缺 sources 键，**ingest 侧历史失败**，与本次改动无关，08-16 已记录）

**待用户拍板（超出本会话授权）**：
- **计划任务注册** `kdo-conveyor-probe`（每 10 分钟，契约 §调度）——schtasks 注册动作被权限分类器拦截，需用户确认后注册
- **飞书凭证**：通知通道配置 `kdo-tools/.feishu_webhooks.json`（webhook URL 或 app_id/secret），凭证后补即上线（用户已选 dry-run 验收）
- **测试建议书 2 份**：`diag_20260822_probe-test-1-proposal.md` / `diag_20260822_probe-test-2-missing-status.md` 由王语嫣裁定处置（任务单追加原文）

**边界声明**：只通知/登记，不领取/不裁决/不流转（代码层验证）；未动 diagnosis/ 存量文件；登记动作与 watch_inbox 同类豁免（任务单追加明确）

### 补充：真实通知测试完成（2026-08-22 深夜，用户提供凭证后）

- **通道**：飞书群机器人 webhook（加签模式，用户提供 URL + 签名密钥），配置落 `kdo-tools/.feishu_webhooks.json`（git 已忽略）；`_send_hook` 支持 HMAC-SHA256 签名（timestamp+sign）
- **通道测试**：单条测试消息发送成功（用户确认收到）
- **三类信号真实通知（附输出）**：
  1. 欧阳锋「🔔 KDO 新提审 3 单：…请终审」✅
  2. 老顽童「📥 KDO 可领取 6 单：…」✅
  3. 王语嫣「📬 KDO 新建议书 1 份待裁定：diag_20260822_probe-test-3-notify.md」✅（登记与通知同次扫描产物，同源验证）
- **测试建议书③**：`diag_20260822_probe-test-3-notify.md`（第 3 份，同前两份由王语嫣裁定处置）
- 新增 `--force-notify`（仅测试/验收用，跳过夜间静默；生产红线不变）；5 测试回归通过
- **✅ 计划任务已注册**（2026-08-22 用户明确授权）：`kdo-conveyor-probe` 每 10 分钟（PowerShell Register-ScheduledTask，Execute python.exe + WorkingDirectory wiki 根），`schtasks /run` 实测 LastTaskResult=0——通知全自动；夜间静默在任务运行时自动生效（登记照常、通知不发）
- **待办清零**：本单全部验收项完成
