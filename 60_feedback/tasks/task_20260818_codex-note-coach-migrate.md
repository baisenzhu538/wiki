---
id: 360
assignee: codex
status: queued
updated_at: '2026-08-19T05:00:00+00:00'
title: note-coach 归档（P2，#346 拆分项）——老朱 2026-08-19 改判：暂不迁移激活，归档处理，未来重做升级时另立项
priority: P2
dependency: []
reviewed_by: 欧阳锋
---

# #360 note-coach 归档（P2）

## 任务目标

note-coach 停在旧 `.hermes\profiles\note-coach`（未迁 AppData\Local、未服务化、gateway_state 06-07 陈旧）。**老朱 2026-08-19 改判：暂不迁移激活，归档处理——note-coach 未来需要时会重新迭代升级，届时另立项，不在旧目录上修。**

## 素材/证据

- codex #346 收尾核验（2026-08-18）：note-coach 未迁 AppData\Local、未服务化、gateway_state 06-07 陈旧
- 老朱改判（2026-08-19）："note-coach 到时需要重新搞，需要迭代升级的。暂时先归档了"
- 归档先例：duan/kimi-test → `~/.hermes/profiles_archive/`（不真删，T4 纪律）

## 修改范围

1. 旧目录归档：`.hermes\profiles\note-coach` → 归档位置（不真删，留痕）
2. 确认无残留引用：无 NSSM 服务（已确认未服务化）、无 config 指向、cap_hub 登记状态标注"已归档"
3. 归档记录：归档时间/原因/位置 + "未来重做时另立项"注明

## 边界

- 只归档不删除；不做迁移、不做服务化（老朱已改判，原迁移方案作废）
- 未来 note-coach 重建=新任务，不 reuse 本任务

## 验收标准

1. 旧目录移入归档位置，原位置无残留
2. 全库 grep 无活跃引用指向 note-coach 旧路径
3. 归档记录落盘

## 交付

1. 归档执行 + 证据
2. 送欧阳锋终审
- 王语嫣抽查实证（2026-08-18）：`AppData\Local\hermes\profiles\` 无 note-coach；9 个 hermes-gateway 服务无 note-coach；旧目录仍在 `.hermes\profiles\note-coach`
- 先例：#343/#344 迁移 5 项清单（skills 补拷 / config 路径修复 / WinError 87 补丁 / memories 同步 / 服务化）

## 修改范围

1. note-coach profile 迁 `AppData\Local\hermes\profiles\note-coach`（按 #344 迁移 5 项清单执行：skills/config/补丁/memories）
2. NSSM 服务化（hermes-gateway-note-coach）+ 冒烟
3. 旧目录处置：归档不真删（同 duan/kimi-test 先例）
4. 若判定 note-coach 实际无人用，回报证据由老朱改判归档——不擅自归档

## 验收标准

1. `hermes-gateway-note-coach` 服务 Running/Automatic
2. AppData\Local profile 目录齐全（SOUL/config/memories）
3. 冒烟：agent 应答正常
4. 旧目录归档留痕

## 交付

1. 迁移 + 服务化 + 冒烟证据
2. 送欧阳锋终审

---

## 执行结论（2026-08-19 codex 核验 + 用户裁定）

**现状核验（08-19 只读）**：note-coach 已被完整归档至 `.hermes\profiles_archive\note-coach`（SOUL.md 10223B / config.yaml 9032B / memories / skills / state.db 齐全），`.hermes\profiles\note-coach` 已不存在，`AppData\Local\hermes\profiles\note-coach` 不存在，无 `hermes-gateway-note-coach` 服务。

**归档溯源**：归档动作约发生在 08-18 深夜 ~ 08-19 00:02（`profiles_archive` 时间戳），与欧阳锋 #346 T4 终审收官时间吻合；用户 08-19 推测为欧阳锋执行（待确认）。

**瘫痪态证据**：gateway_state.json 06-07 陈旧、state.db 06-30、logs 最后 06-30——自 06-30 起未运行，与「要用但瘫痪」描述一致。

**用户裁定（08-19）**：「归档了，以后再来重新迭代」——note-coach 保持归档，暂不迁 AppData、不服务化。

**结论**：本任务（迁 AppData + 服务化激活）改判为「已归档，暂不迭代」；重新迭代另立新任务。

**纪律**：未擅自迁移/恢复/删档；队列状态流转（改判）交王语嫣/欧阳锋。


---

## 关闭记录（2026-08-19 王语嫣）

老朱改判"暂时先归档"（未来重做升级另立项）后，归档已被执行（应为欧阳锋）。
王语嫣实证（2026-08-19）：`.hermes/profiles/` 无 note-coach 残留 ✅；`.hermes/profiles_archive/note-coach` 在位 ✅；AppData 侧无 note-coach ✅。
任务关闭（closed_no_action）——目标已由改判+归档执行覆盖，迁移激活方案作废。
