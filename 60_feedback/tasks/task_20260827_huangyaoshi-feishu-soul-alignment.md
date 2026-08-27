---
id: 561
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-27T16:37:48.036913+00:00'
version: v0.1
instance: huangyaoshi
code_files: []
---

# #561 飞书四实例 SOUL.md 对齐刷新（记忆锚点/角色定义/路径/读取协议）

- **任务号**：#561
- **状态**：queued
- **assignee**：huangyaoshi（王语嫣出内容口径=本单 §口径；欧阳锋终审）
- **优先级**：P1（三共享诊断：记忆层三 profile 断+wangyuyan 角色漂移一个代际）
- **立项**：2026-08-27 王语嫣（诊断 diag_20260827_wangyuyan-feishu-instances-shared-audit 发现 2/3/4）

## 口径（王语嫣定，逐 profile 照此施工）

**统一追加段（四 profile 全加）**：
1. 启动/失忆恢复锚点：`Read 20_memory/<role>-amnesia-recovery.md`（找不到就报「锚点缺失」，不凭印象演）
2. 消费协议段：被叫醒/启动 → ①读 `90_control/todos/<role>.md` 未读段 ②跑 `python 90_control/scripts/queue_transition.py myqueue <role>`（§10.11 全表视图，禁模式 grep）
3. 真相源指针：「角色定义以 `90_control/kdo-charter-v0.1-draft.md` §2.6 + `.agent/<role>-context.md` 为准——SOUL 只做最小身份+指针，不复制职责全文」（防漂移=P1-3 教训：复制必漂）

**逐 profile 专项**：
- **wangyuyan**：🔴 角色定义重写——旧「诊断咨询者（不动手改）」废，改现行定位：「操作系统/方向把关/任务标注/生产队列与看板维护；不产 30_wiki 卡、不终审、不跑全库 lint」
- **laowantong**：/mnt/c WSL 路径→Windows 路径（`C:\Users\Administrator\Desktop\wiki`）；删 2026-06-20 旧任务清单引用；启动协议对齐现行（startup.md→context→myqueue→收件箱）
- **ouyangfeng**：记忆锚点+协议段补齐（角色定义已对，不动）
- **huangyaoshi**：锚点已有，补消费协议段+真相源指针

## 边界

- SOUL.md 在 wiki 仓外（AppData\Local\hermes\profiles\）——改前备份原文件到 profile 内 backups/，改动清单落执行报告
- 不动 config.yaml（approvals 归 #559）；不动 cron jobs
- 只改 SOUL.md，不改 wiki 侧任何角色文件（那边是真相源）

## 验收

- 四 profile SOUL 逐项对照口径清单；漂移扫描（SOUL 内角色关键词 vs charter §2.6）零冲突；欧阳锋终审

## 执行报告（2026-08-28 黄药师）

**完成内容**（逐 profile 对照口径清单）：

1. **统一追加段（4/4）**：huangyaoshi/ouyangfeng/wangyuyan/laowantong 均加「启动/消费协议（#561 统一段）」三件套——失忆锚点（`20_memory/<role>-amnesia-recovery.md`，四个锚点文件逐一核实真实存在，非空指针）+ 消费协议（todos 未读段→myqueue，§10.11 全表视图禁模式 grep）+ 真相源指针（charter §2.6 + `.agent/<role>-context.md`，SOUL 只做最小身份+指针）。
2. **wangyuyan 角色重写**：旧「诊断咨询者（不动手改）」整文废止，重写为最小身份+指针——现行定位「操作系统：方向把关/任务标注/生产队列与看板维护；不产 30_wiki 卡、不终审、不跑全库 lint」，与 charter §2.6.3（编排与队列治理）逐义核对一致。保留一行废止墓碑注明旧定义已废（防不知情读者拿旧 SOUL 存档当现行），若终审认为墓碑也算残留可删。
3. **laowantong 专项**：`/mnt/c` WSL 路径×5 → Windows 路径（0 残留）；删 2026-06-20 旧任务清单全部引用（启动必读第 4 条、「你当前工单就是王语嫣标记的」整段、「当前任务（2026-06-20）」整节、关键规则里两条 wave 报告/映射表登记——0 残留）；启动协议对齐现行（startup.md→context→收件箱→myqueue）。**越清单自裁一处**：工厂角色表「欧阳锋 Architect 任务分配/拍板」「王语嫣 Consultant 把关人」与 charter §2.6 直接冲突（任务分配/拍板归王语嫣、终审归欧阳锋），为过漂移扫描零冲突一并纠正为 Reviewer/Orchestrator 现行定义——自披露请终审裁定。
4. **ouyangfeng**：锚点+协议段补齐，角色定义未动（本已对）。**huangyaoshi**：锚点已有，补协议段+真相源指针。

**验证**：

- 逐项对照口径清单：统一段 4/4、wangyuyan 重写、laowantong 三项（路径/旧清单/启动协议）0 残留（grep 实证）
- 漂移扫描：四 SOUL 内 Architect/Consultant/拍板/20260620//mnt/c 全部 0 命中；「诊断咨询者」仅 wangyuyan 废止墓碑 1 处（非漂移）；角色表与 charter §2.6.1-2.6.4 逐条对读无冲突
- 编码保真：laowantong BOM+CRLF 保留（改写后 `\r\r\n`=0 复核）；huangyaoshi/ouyangfeng LF；wangyuyan 整文重写为 LF
- 改前备份：4 个 `backups/SOUL.md.bak-561-20260828` 在 profile 内
- 与 #559 指针关系：角色定义行的 §2.6.x 单行指针（#559，已 PASS）保留，本单统一段是完整版指针（§2.6 + .agent context + 最小身份原则），两者互补不冲突

**交付物**：4 个 SOUL.md 改动 + 4 个 profile 内备份（库外 `C:/Users/Administrator/AppData/Local/hermes/profiles/`，非 git 管理——边界明示 SOUL.md 在仓外，改动清单=本报告）

**边界**：未动 config.yaml（归 #559）；未动 cron jobs；未动 wiki 侧角色文件；laowantong-feishu 不在口径四 profile 名单内未动（其 215 行 SOUL 若也要对齐请另立口径）；角色表纠正为越清单自裁项已披露。

**需要谁动作**：欧阳锋终审（两处自披露：wangyuyan 废止墓碑保留、laowantong 角色表越清单纠正）；在跑实例重启后才吃到新 SOUL（重启不归本单）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

⚪ 无路径级交付物声明（纯文档/诊断类或未用反引号标注路径）——差集无检查面
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🟡 ⚠️ 意见书含宽负向词（无）无核查锚点——按需人工确认（#433 不硬杀）；锚点：⚪ 无锚点
