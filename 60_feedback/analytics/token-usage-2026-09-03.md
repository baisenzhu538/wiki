# 全厂 token 日计量 2026-09-03（#549）

| 引擎 | 会话/角色 | input | output | cache_read | cache_write | 计
|---|---|---|---|---|---|---|
| hermes | laowantong | 355371 | 77925 | 28422336 | 0 | 28855632 |
| hermes | skills-assistant | 86930 | 28520 | 5742848 | 0 | 5858298 |
| hermes | wangyuyan | 84429 | 13768 | 1310208 | 0 | 1408405 |
| **合计** | — | 526730 | 120213 | 35475392 | 0 | 36122335 |

> hermes 行=角色（profile 名）；claude/kimi 行=会话文件（角色归因=cwd 粒度，混合角色会话为估算口径）。
> #514 接口：周聚合 = 本周日 JSON 合计 ÷ 同期 reviewed 单数（质量基线周报同源）。