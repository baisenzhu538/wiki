---
id: 354
assignee: huangyaoshi
status: queued
updated_at: 2026-08-18
title: "MCP 性能（onboard/capabilities 走索引 + read 分页 + 统计动态化）"
priority: P2
dependency: [353]
---

# #354 MCP 性能

## 范围调整（2026-08-18 用户拍板：冷加载治本优先）

- onboard/capabilities 走索引 + read 分页范围**并入 #356**（跨进程索引共享治本任务，同病根）
- 本任务不再单独优先执行；黄药师执行 #356 时吸收本任务范围
- 队列行保留登记（历史留痕），不重复开工

## 任务目标

小昭审查 P2 性能三项 + P4-15——消除 onboard/capabilities 每次全表扫描，read 支持续读，instructions 统计动态化。

## 素材/证据

- 小昭审查 §二 P2-8/9/10 + P4-15
- 先例：**O-15 进程级缓存模式**（08-17 落地：search_index.py `get_shared_index` + mtime 失效策略，首次 5.5s → 二次 0.000s）——onboard/capabilities 复用同模式，不新造轮子

## 修改范围

1. **onboard 走索引**：复用 search_index（或轻量缓存）替代每次 `rglob("*.md")` 全扫 2500 卡（tools.py:236-276）——O(1) 查询
2. **capabilities 走索引**：统计接口不再逐文件读前 500 字符（tools.py:371-391）
3. **read 分页**：10k 截断改 `offset` 参数续读（tools.py:342），长卡可读全
4. **instructions 统计动态化**：server.py 硬编码 "244 frameworks, 106 skills, 10 workflows, 8 agent specs"（L46-48）→ 启动时动态统计或删数字

## 边界

- 不动检索逻辑/索引重建机制（#329 已修）
- 须在 **#351 重启前交付**（合并一次生效，用户拍板 2026-08-18）
- read 分页保持向后兼容（不带 offset 时行为不变）

## 验收标准

1. onboard 二次调用 <100ms（对照修复前秒级）
2. capabilities 二次调用 <100ms
3. read 长卡（>10k）通过 offset 读全
4. instructions 数字与当前实际一致（或动态）
5. 回归：4 工具功能不变（中文 3 例 + onboard 域导览 1 例）

## 交付

1. 修改 + 性能对照证据
2. 送欧阳锋终审

---

## 吸收核验记录（2026-08-18 欧阳锋）

用户拍板 #354 并入 #356 吸收（2026-08-18 范围调整节）。#356 终审核验吸收落地情况：

| #354 范围 | #356 落地 | 核验 |
|:--|:--|:--|
| capabilities 走索引 | ✅ 同进程二次 0.009s | ✅ 达标 |
| read 分页 offset | ✅ offset+more+边界标记 | ✅ 达标 |
| instructions 动态化 | ✅ 272/118/10/13 实测 | ✅ 达标 |
| **onboard 走索引** | ❌ **未落地**：仍 rglob 全扫，实测 5.40s（验收 <100ms，50 倍超标）；#356 报告"domain-routes 轻量无需索引化"与实际代码不符 | 🔴 条件项 |

**条件项跟踪**：onboard 索引化补做（复用 get_shared_index/O-15 模式）——由黄药师在 #356 条件项或本任务补做，完成后复审。#354 队列行保留登记（历史留痕），条件清后本任务闭环。
