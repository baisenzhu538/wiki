# 全厂 token 日计量 2026-08-27（#549）

| 引擎 | 会话/角色 | input | output | cache_read | cache_write | 计
|---|---|---|---|---|---|---|
| kimi | session_6c3ded32-0e90-4822-a93c-a9b506cd9685/main | 261681 | 132239 | 80305152 | 0 | 80699072 |
| kimi | session_b4f040ba-62c4-491c-9ca8-820fb840f445/main | 110462 | 58545 | 20628224 | 0 | 20797231 |
| kimi | session_d389a44a-5161-433b-9ae2-9ebc9c0feb19/agent-0 | 17733 | 8833 | 102912 | 0 | 129478 |
| kimi | session_d389a44a-5161-433b-9ae2-9ebc9c0feb19/agent-1 | 42254 | 9537 | 193792 | 0 | 245583 |
| kimi | session_d389a44a-5161-433b-9ae2-9ebc9c0feb19/agent-2 | 45752 | 11482 | 355840 | 0 | 413074 |
| kimi | session_d389a44a-5161-433b-9ae2-9ebc9c0feb19/agent-3 | 40818 | 6872 | 114432 | 0 | 162122 |
| kimi | session_d389a44a-5161-433b-9ae2-9ebc9c0feb19/main | 257107 | 107923 | 36819456 | 0 | 37184486 |
| kimi | session_e47b0886-2b35-40ca-ab68-be1302787f47/main | 135658 | 59066 | 32991488 | 0 | 33186212 |
| **合计** | — | 911465 | 394497 | 171511296 | 0 | 172817258 |

> hermes 行=角色（profile 名）；claude/kimi 行=会话文件（角色归因=cwd 粒度，混合角色会话为估算口径）。
> #514 接口：周聚合 = 本周日 JSON 合计 ÷ 同期 reviewed 单数（质量基线周报同源）。