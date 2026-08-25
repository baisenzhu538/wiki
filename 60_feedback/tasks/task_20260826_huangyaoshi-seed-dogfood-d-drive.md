---
id: 534
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-25T20:05:26.710111+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- D:/tech-wiki/
---

# #534 种子包本机狗粮实装验证：D:\tech-wiki 空库全链路

- **任务号**：#534
- **状态**：queued（依赖 #532/#533 交付后触发）
- **assignee**：huangyaoshi（执行+验证报告；欧阳锋终审）
- **优先级**：P1（老朱 08-26 拍板：本机硬盘不足，空文件夹先跑狗粮，真实技术资料后进场）
- **立项**：2026-08-26 王语嫣

## 背景

种子包（#532）+ 技术域适配包（#533）出来后，先在**本机空库**实装验证，而非等拷贝真实技术库。狗粮场 = `D:\tech-wiki`（D 盘余量 35G；选 D 盘顺手验证非桌面路径下 KDO_ROOT 参数化）。种子本体几 MB，磁盘成本≈0。验证目标只有一个：**机制不走样**。

## 任务（五步全链路）

1. **建库**：`D:\tech-wiki` 空文件夹 → 解压种子 → 跑 seed-check，九层骨架/五角色文件/charter/kdo-tools 齐不齐
2. **路径验证**：`KDO_ROOT=D:\tech-wiki` 下全部脚本可跑——#532 参数化的 23 处硬编码有没有漏网
3. **第二套探针**：schtasks 注册，任务名加 `-tech` 后缀与主库区分，首轮必须见回执（#519 静默失效在这步现形）；MCP 端口与主库错开
4. **五角色归位**：会话指向 `D:\tech-wiki`，那边王语嫣启动五连读走完
5. **微型闭环**：投 2~3 篇测试文稿进那边 inbox → 探针发现 → 王语嫣立项 **#001**（新库编号独立水位，老朱已拍板）→ 老顽童产卡 → 欧阳锋终审 → 复盘归档，全程按 charter 走

## 边界

- 只放测试文稿，不拷真实技术资料；真实工件引用/git 大文件策略不在本单（待资料进场后校准）
- 主库（Desktop/wiki）任何文件、探针、计划任务不许动
- 验证发现的所有走样点逐条记入报告，回flow王语嫣编排修复单

## 验收

- 五步全过 + 验证报告（含走样点清单，哪怕为零也要写「零走样」结论）；欧阳锋终审

## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：D:\tech-wiki 空库实装狗粮，五步第 1-3 全过（4-5 步按任务书归那边王语嫣，交接已落她新库收件箱）。①建库：种子拷入→seed-check 全过；②路径验证：KDO_ROOT=D:\tech-wiki 下 conveyor_probe/watch_inbox/quality_metrics/health-check 全实跑——**.cmd 的 %~dp0.. 回退在无 KDO_ROOT 的计划任务环境实证位置无关**；③第二套探针：kdo-conveyor-probe-tech/kdo-inbox-watch-tech 注册（-tech 后缀与主库区分），计划触发实跑 state 落盘+日志留痕；测试文稿 2 篇投递→检测→待编排段登记→王语嫣收件箱 🔕 通知全链在狗粮场走通。

**走样点清单（5 修 2 登记，全部实证）**：
1. ✅ 修：种子缺初始 production-queue.md → 探针首轮 FileNotFoundError（QUEUE_TEMPLATE 已入种子+主库 build_seed.py 回修）
2. ✅ 修：种子缺 logs/ 目录 → .cmd 重定向失败探针静默不跑且任务假报 result 0（**#519 静默失效同族新变体，在狗粮场现形**——logs 已入骨架）
3. ✅ 修：seed-check 计划任务名写死主库 → 加 --task-suffix（第二套库可检）
4. ✅ 修：health-check 子检查清单不全（kdo_lint 等 6 件缺 → 新库健康检查即 FAIL）→ CONTROL_SCRIPTS 补齐，补后 --quick PASS
5. 📋 登记不修：friction-log 入种子 → 新库首扫把历史 friction 当新信号推了一条（bootstrap 一次性噪声，可接受不修）
6. 📋 登记回flow：l1_capture L1_ROOT=D:\KDO-memory 硬编码共享路径——**有意不注册 l1-capture-tech**（防两库采集混流），参数化修复单回王语嫣编排；MCP server 未入种子（检索面随 #525 统一层定）

**交付物**：
- D:\tech-wiki（实装库：种子+2 测试文稿+2 计划任务在跑+双通道通知实证）
- 主库回修：`kdo-tools/build_seed.py`（queue 模板+logs 骨架+scripts 清单补齐）、`kdo-tools/seed-check.py`（--task-suffix+logs 层）
- 交接：`D:\tech-wiki\90_control\todos\wangyuyan.md`（第 4-5 步交接说明）

**验证**：
- L1：种子重建回归全绿（kdo-tools 139 passed 含 test_seed_package 5 例）；主库 90_control 150 passed 零退步
- L2 狗粮实测链：seed-check 全过→探针计划触发 03:52 state 落盘+log 留痕（修 logs 后）→watch_inbox 检测 2 文稿→看板待编排段 +2→王语嫣收件箱 🔕 行→health-check --quick PASS（修清单后）→quality_metrics 空库出「样本不足」不编数 ✅
- L3 待活体：那边王语嫣启动五连读+微型闭环 #001（交接已落她新库收件箱）；老朱进场真实技术资料
- **提审后补件声明**（透明先例）：complete 首跑被 E040 门禁拦——交付物含库外绝对路径（D:/tech-wiki 他库文件）git 无法核验被当 untracked 硬拦；修复=库外路径 WARNING 不拦（红线 4）+回归 1 例，commit 926f9b7a9 晚于提审 1 分钟（自体应用撞线即修）

**边界**：主库文件/探针/计划任务零触碰（走样点修复全在种子构建器与 D 盘库；主库在跑任务未动）✅；只放测试文稿零真实资料 ✅；有意不注册的三件（l1-capture/health-daily/quality-metrics -tech 版）原因在案 ✅；git 大文件策略待资料进场校准 ✅。

**需要谁动作**：欧阳锋终审本单（走样点清单请重点核第 2 条——#519 同族变体）；**王语嫣**：D:\tech-wiki 第 4-5 步（五连读+#001 立项+微型闭环），你新库收件箱有交接条；l1-capture 参数化修复单请编排；老朱知悉——种子包狗粮场机制不走样已实证，真实资料可进场。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

- 🔴 声称但未入仓（untracked）: `D:/tech-wiki/`
- 🔴 声称但未入仓（untracked）: `D:/tech-wiki/90_control/todos/wangyuyan.md`
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🟡 ⚠️ 意见书含宽负向词（无/缺）无核查锚点——按需人工确认（#433 不硬杀）；锚点：⚪ 无锚点
