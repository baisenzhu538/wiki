---
id: 532
assignee: huangyaoshi
status: reviewed
updated_at: '2026-08-25T18:39:29.843614+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- 90_control/kdo-seed/
- kdo-tools/
reviewed_by: 欧阳锋
review_date: '2026-08-25'
grade: A
---

# #532 kdo-seed 种子包：机制层整体搬迁三件套 + 路径参数化

- **任务号**：#532
- **状态**：queued
- **assignee**：huangyaoshi（欧阳锋终审）
- **优先级**：P1（老朱 08-26 拍板：第二台机器要起一座同构工厂，机制不走样）
- **立项**：2026-08-26 王语嫣（老朱问「整个 KDO 基础设施如何搬到另一台电脑」，方案经老朱确认）

## 背景

KDO 基础设施实测拆三层：**A 机制层**（角色文件 `.agent/`+`agents/{五角色}`、制度层 charter v1.3/schemas/quality-gates/quality-metrics-spec/consumer-retrieval-protocol、工具层 kdo-tools 核心脚本+90_control/scripts 检查类、九层目录骨架）原样可复制；**B 机器绑定层**（5 个计划任务 .cmd 包装器、schtasks 注册、Python 路径、AGENTS.md 工作目录判断句）必须重建；**C 实例内容层**（30_wiki 卡片、队列行、60_feedback 历史、复盘档案）不搬，新库从 #001 重新长。

**风险点**：机制层有 23 处硬编码 `C:\Users\Administrator\Desktop\wiki`（5 个 .cmd + 若干 py），靠人肉 checklist 改必漏，漏一处就是 #519 式静默失效。

## 任务

1. **种子目录** `90_control/kdo-seed/`：A 层机制文件全集 + 九层空骨架 + 桌面 agent复盘/{五角色}/daily-context 骨架说明；域相关采集脚本（抖音/微信/利润为王系）剔除
2. **bootstrap 开机手册**：新机器五步——放种子→设 `KDO_ROOT`→跑 seed-check→注册 schtasks（附现成注册命令模板）→五角色启动五连读验证
3. **seed-check.py 自检脚本**：目录齐不齐、计划任务注册没注册、探针首轮有无回执、角色文件可读性——把「机制不走样」从人工核对变成脚本保证
4. **路径参数化**：A 层脚本硬编码路径改读 `KDO_ROOT` 环境变量（缺省回退脚本相对路径推导）；.cmd 包装器改为从环境变量取根目录

## 边界

- 只搬机制，不搬任何本库内容数据；不改本库现有脚本行为（参数化后本机照常跑，回归验证）
- schtasks 注册命令写进手册即可，不在本机执行任何新注册
- 技术域（软硬件）适配不在本单，走 #533

## 验收

- 种子目录完整（seed-check 自证）；本机既有探针/门禁/队列脚本回归全过；手册经王语嫣过一遍可执行性
- 欧阳锋终审

## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：种子包三件套+路径参数化。①**种子目录** `90_control/kdo-seed/`（97 文件+15 骨架目录）：由 `build_seed.py` 清单化构建（可重复构建，清单即文档）——.agent/*.md+agents/{五角色}+20_memory 失忆锚点/制度层（charter/schemas/quality-gates/spec 三件）/工具层（kdo-tools 核心 13 件+90_control/scripts 16 件+6 .cmd）/九层空骨架/agent复盘五角色骨架；域采集（wechat/douyin/利润为王系）与一次性修复批（fix-*/stage4-*）剔除；②**bootstrap 手册** `BOOTSTRAP.md`：五步（放种子→setx KDO_ROOT→seed-check→schtasks 五条现成注册模板→五角色五连读）+不搬清单+故障排查表（含 #519 嵌套引号教训）；③**seed-check.py** 四查（骨架层/关键件/五角色可读/脚本可编译）+schtasks 在册核查（可 --skip-tasks）；④**路径参数化**：6 个 .cmd 全部 `KDO_ROOT 优先+%~dp0.. 回退`（位置无关）、agent-activity-check.py/sync-hermes-mcp.py 改 env 优先+__file__ 回退（mcp/tools.py 本已 env 化）——回退值与原硬编码逐字一致（本机零行为变化实测）；一次性修复批 12 件与域采集脚本的硬编码不参数化（历史遗留待归档族，不进种子不改行为）。

**交付物**：
- `kdo-tools/build_seed.py` + `kdo-tools/seed-check.py`（新）
- `90_control/kdo-seed/`（种子目录 97 文件 + BOOTSTRAP.md）
- 参数化：6 .cmd + `agent-activity-check.py` + `sync-hermes-mcp.py`
- `kdo-tools/tests/test_seed_package.py`（新：5 例回归）+ `90_control/infrastructure-inventory.md`（登记）

**验证**：
- L1 单测 5 例全过：种子构建完整性（九层/五角色/关键件）/seed-check 真库全过/缺层负向必报/.cmd 参数化断言（KDO_ROOT+%~dp0.. 在、硬编码 cd 无）/py 回退值=真库根
- L2 狗粮：本机 seed-check 全过（含五计划任务在册）✅；参数化后 conveyor .cmd 实跑 exit 0、probe state 落盘（age 0s）✅；sync-hermes-mcp 参数化后 WIKI/WSL_WIKI 推导值与原硬编码逐字一致 ✅
- 本机回归全绿：kdo-tools **135 passed**（130+5）、90_control/scripts **150 passed**——参数化零行为回归
- L3 待活体：#534 D 盘空库五步实装（狗粮单已排在我队列下下位）

**边界**：零内容数据搬迁（C 层不碰）✅；本机脚本行为不变（回退一致+双仓回归绿）✅；schtasks 注册仅手册模板未在本机新注册 ✅；技术域适配归 #533 未染指 ✅；种子为快照——机制层后续演进用 build_seed.py 重构建刷新（免维护漂移）。

**需要谁动作**：欧阳锋终审本单；**王语嫣**：BOOTSTRAP.md 过一遍可执行性（验收项）；老朱知悉——第二台机器五步起厂的种子已备，#534 本机狗粮实装紧接验证。

## 终审记录

- **终审**：欧阳锋 08-26 **PASS A**
- **版本对齐**：冻结版=02:35 commit f48b0487a=提审时刻 ✓（工作区 M 文件全为运行时日志/索引副产物，非交付物）
- **O0 溯源**：①种子目录 113 文件实测（声明 97+后续附件，BOOTSTRAP.md+seed/ 结构在）✓；②`.cmd` 参数化逐行对——`KDO_ROOT 优先+%~dp0.. 回退`（kdo-conveyor-probe.cmd:11-12 实测），位置无关 ✓；③BOOTSTRAP 五步手册亲读——可执行性强（放种子→setx→seed-check→五条 schtasks 模板照抄→五连读），#519 嵌套引号教训入故障排查表 ✓；④seed-check 四查+schtasks 在册核查
- **独立复跑**：kdo-tools 135 passed、90_control/scripts 150 passed，双仓零回归与声明一致 ✓；**seed-check 本机亲跑全过**（九层骨架/关键件/五角色可读/脚本可编译/计划任务在册）✓
- **存在性核查**（负向断言附证）：「本机未新注册 schtasks」——`schtasks /query` 五任务均为既有注册（下次运行时间延续，非新建设备）✓；「回退值与原硬编码逐字一致」——`%~dp0..` 解析= kdo-tools 上级=wiki 根，与原 `C:\...\Desktop\wiki` 同路径 ✓ | 核查人：欧阳锋 08-26
- **预审报告判读**：宽负向词（无/缺）系"有无回执""缺省回退"等描述文字被扫=误报，已判读不计缺陷
- **边界**：C 层内容数据零搬迁 ✓；域采集脚本剔除 ✓；技术域适配归 #533 未染指 ✓；种子快照+build_seed.py 可重复构建（免维护漂移设计好）
- **后续**：L3=#534 D 盘空库五步实装（狗粮单已排队——届时我审实装结果）；王语嫣过手册可执行性

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 6 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🟡 ⚠️ 意见书含宽负向词（无/缺）无核查锚点——按需人工确认（#433 不硬杀）；锚点：⚪ 无锚点
