---
title: 各角色夜班复盘指令（#582/#583 闭环后触发）
type: task-instruction
author: 王语嫣
created_at: 2026-08-31
context: 老朱直令——全部完成后手头没有在飞任务时，各角色按 Truman 11 章规定格式复盘并内化迭代
---

# 复盘指令（老顽童/欧阳锋/黄药师 各自执行）

你是 KDO 知识工厂的 <角色名>。2026-08-31 夜班你完成了下述任务，现在按《agent-os》§10.2 Truman 11 章标准格式写复盘并内化迭代。

## 你本夜班做的事

- **老顽童**：#582 阿蕊科学销售体系 4 卡生产（framework/method/case/entity 各 1），素材 `00_inbox/私董会/阿蕊科学销售/articles/`，已 PASS A-。执行报告在任务单 `60_feedback/tasks/task_20260831_laowantong-arui-science-sales-cards.md`
- **欧阳锋**：#582 终审 PASS A-（溯源 5 组锚点抽验/门禁三连/撞车面核查纠正编排者误记/4 处 commit）
- **黄药师**：#583 Mnemosyne 记忆缓存试点+狗粮测试（50 真卡语料 A/B 查询集 vs kdo query 四维对比，结论落 diagnosis）

## 复盘要求（11 章缺一不可）

1. 读 `agents/agent-os.md` §10.2 拿准格式（差异栏/概要/关键决策/思维盲点/顿悟/过程资产/元反思 + Truman 四节）
2. **差异栏必须非空**：对照你上次复盘（`agent复盘/<你的拼音>/daily-context/` 最新一份）找「本次 vs 上次哪里不同——新视角/复发模式/被打破的假设」，空白=重复自审降 C 级
3. **内化迭代双动作**（写完复盘同一动作内完成）：
   - 错误模式库（`.agent/pitfalls.md` 或 `agent复盘/<你的拼音>/错误模式库.md`）——有新错误模式才追加，编号顺延
   - 技能/纪律更新——本班学到的方法论固化进你名下 skill 或 SOUL，注明实证来源
4. 跑收尾自检：`python kdo-tools/daily-context-save.py save --agent <你的拼音> --truman --file "agent复盘/<你的拼音>/daily-context/2026-08-31.md"`，输出必须 🟢/🟡，🔴 C 级=重写
5. 落盘后 git commit（署名只用角色名）

## 本夜班可参照的教训素材

- 老朱三次纠正：自动化盲区（素材进 inbox 无人消费）/ 浅验证（表面工作批评）/ 看板 token 成本——各自映射什么机制缺口，对你的角色有何镜像教训？
- #582 指令误记事件（编排者引用了错误背景事实）：审查者/生产者如何防「上游指令本身有错」？
- 心跳/完工通知链路：你的实例退出后通知是否准时到达编排者？
