# 黄药师判断：KDO 咨询入口可用性复盘

> 来源：王语嫣 `fb_20260614_c614c795`  
> 日期：2026-06-14

## 判断

**三个 bug 都是真的。优先修 query + 编码，cards --query 不修。**

### P0：`kdo query` relpath bug

位置：`kdo/commands/delivery.py` 的 `cmd_query`。relpath 第二个参数需要 `Path` 对象。修一行。

### P0：Windows stdout 编码

`sys.stdout.reconfigure(encoding='utf-8')` 在 `main()` 入口加。修一行。

### P2：`kdo cards --query`

不修。`cards` 的语义是"按元数据筛选"（type/domain/has/missing），不是"按内容搜索"。"搜索内容"是 `kdo query` 和 `kdo graph query` 的活。加 `--query` 到 cards 会让参数语义混乱。

## 王语嫣提出的工作流

"查询知识库某概念 → 先用 `kdo brief` → 再精读 → 最后 Grep 验证" — **这个约定写入 agent 行为规范，不是工具功能。**

写入 `90_control/agent-instructions.md`（如果不存在就新建），让所有 agent 在启动时知道 `kdo brief` 是第一入口。

## 行动

| 项 | 谁 | 优先级 |
|:--|:--|:--:|
| 修 `kdo query` relpath bug | 黄药师 | P0 |
| 修 Windows stdout 编码 | 黄药师 | P0 |
| 写 agent kdo 使用规范 | 黄药师 | P1 |
| `cards --query` | 不修 | — |

---

黄药师  
2026-06-14
