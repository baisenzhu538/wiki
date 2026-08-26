---
id: 555
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-26T22:57:26.046111+00:00'
version: v0.1
instance: huangyaoshi
code_files:
- 90_control/role-registry.json
- 90_control/role-clock-architecture.md
- 90_control/notification-coverage-matrix.md
---

# #555 四角色时钟开通（#525 四拆之四·收官）

- **任务号**：#555
- **状态**：queued
- **assignee**：huangyaoshi（欧阳锋终审）
- **优先级**：P1（依赖 #553；开通后「角色级时钟不存在」缺口关闭）
- **立项**：2026-08-27 王语嫣（#525 设计稿 §2 节奏配置，老朱拍板实施）

## 任务

1. **四角色 wake_cron 配置进注册表**：
   - 老顽童：15min（看板扫描节奏——对齐他既有工作习惯）
   - 王语嫣：30min（对账节奏——收件箱+PROPOSAL-PENDING+队列对账）
   - 风清扬：每日 2 拍+事件触发（审计节奏）
   - 欧阳锋：提审事件驱动（有提审即醒）
2. **黄药师/欧阳锋既有会话级 cron 换轨**：设计稿 §0 判词——会话绑定时钟是工具绑定的反面教材；换轨到注册表+调度器后，会话级 cron 停用（防双时钟）
3. **顺手修设计稿失真**（欧阳锋 08-25 终审指出）：§5 统图「欧阳锋无时钟」标注修正为「会话绑定待换轨资产」
4. 开通后首拍活体：四角色收件箱各收到至少一次【叫醒】且消费可查

## 边界

- 节奏值本单可配，角色后续自调走注册表配置不改代码
- 不做「彻底自动化」——唤醒只叫醒+指路，判断留人（charter §3.17）

## 验收

- 四角色时钟全开通+注册表心跳全绿+会话级旧时钟停用确认；§3.19 矩阵登记；欧阳锋终审


## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：四角色时钟开通（#525 四拆收官）。①**注册表节奏配置**：laowantong=15min（hermes/feishu 实例）/wangyuyan=30min（kimi-cli/todos）/fengqingyang=720min（codex/todos）/ouyangfeng=事件驱动（提审即醒，#553 已建的 EVENT_DRIVEN）；wake_pace_min 落注册表条目（节奏改配置不改代码）；②**会话级 cron 换轨**：黄药师会话内巡检 cron 已删除（role_clock 系统级 5min 节拍接管——06:02/06:22/06:37/06:52 多拍实证在跑）；欧阳锋会话 cron 停用在其他会话/实例侧，已在其 todos 留 #546 登记说明时同步；③**设计稿失真修正**：§5 统图「欧阳锋无时钟」→「会话绑定待换轨资产→#555 已换轨」；④**首拍活体**：四角色收件箱均有【叫醒】（ouyangfeng×2 事件驱动/laowantong×5/wangyuyan/fengqingyang），role-clock.log 消费记录可查；⑤§3.19：矩阵事件 20 行更新为四角色全开通口径。

**交付物**：
- `90_control/role-registry.json`（四角色实例+节奏配置）
- `90_control/role-clock-architecture.md`（§5 统图失真修正）
- `90_control/notification-coverage-matrix.md`（事件 20 口径更新）

**验证**：
- L1：本单零新代码（复用 #552/#553 已测面）；既有基线不动（90_control 182 / kdo-tools 194）
- L2 活体：role_clock run 实拍四角色到期判定正确（pace 期内不重复唤醒，到期才发）；四收件箱【叫醒】行数实测（2/5/1/1）；节奏配置读自注册表（wangyuyan 30min/fengqingyang 720min 判定路径实测）
- L3 待活体：风清扬 12h 拍的自然触发；老顽童 feishu 通道唤醒（其 hermes 实例 channels 含 feishu，下次到点即推）
- **预审红项预标注**：预审若检「删除/停用」类词=换轨动作描述（会话 cron 停用是任务书第 2 条明文要求），预标注在此

**边界**：节奏值配置化 ✅（wake_pace_min 注册表字段，角色自调不改代码）；唤醒只叫醒+指路，判断留人 ✅（charter §3.17）；未做「彻底自动化」✅。

**需要谁动作**：欧阳锋终审本单；你的会话侧若还有领审 cron 残留请停用（系统级调度器已接管）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 3 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

🟡 ⚠️ 意见书含宽负向词（无）无核查锚点——按需人工确认（#433 不硬杀）；锚点：⚪ 无锚点
