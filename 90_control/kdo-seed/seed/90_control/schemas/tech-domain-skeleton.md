# 技术域分层骨架模板（#533 技术域适配包）

> 用途：软硬件全栈技术库的 30_wiki 域骨架。核心原则（王语嫣定）：**知识卡管认知，不管工件**——工件（EDA 工程/代码仓/固件/协议原文）留原仓，卡只装设计意图/接口契约/版本变更/踩坑/故障案例，frontmatter `artifact_path` 引用工件。

## 分层（按系统栈）

```
30_wiki/
├── specs/         # 协议/接口规格卡（spec.yaml）——跨层契约层
├── modules/
│   ├── hardware/     # 硬件/电路模块（module.yaml）
│   ├── firmware/     # 固件模块
│   ├── backend/      # 平台后端模块
│   └── edge/         # 端侧（Android/Windows）模块
├── fault-cases/   # 故障排查案例卡（fault-case.yaml）——全层通用
└── domains/       # 域地图/MOC（既有卡型不动）
```

## 层间接口关系（卡间最该建的链接）

五层栈：**硬件/电路 → 固件 → 通讯协议 → 平台后端 → 端侧**。
层间唯一合法的耦合点=接口契约：

- 模块卡的 `interface_contract` 必须写明对上游/下游的承诺；
- 跨层承诺若涉及协议 → 建 spec 卡，模块卡 `dependencies` 链到 spec 卡；
- 故障案例卡的 `prevention` 若落到契约变更 → 回链 spec/module 卡（闭环证据）。

判读口诀：**层内靠职责，层间靠契约，跨界靠 spec 卡。**

## 建卡顺序建议（接管既有技术库时）

1. 先跑存量盘点脚本（kdo-tools/tech_inventory.py）出三堆清单；
2. fault-case 卡优先（最值钱暗知识，散在聊天记录/记忆里的先捞）；
3. module 卡按层补齐（接口契约是重点）；
4. spec 卡最后固化（协议变动史问 owner）。
