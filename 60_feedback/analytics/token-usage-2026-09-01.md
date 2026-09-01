# 全厂 token 日计量 2026-09-01（#549）

| 引擎 | 会话/角色 | input | output | cache_read | cache_write | 计
|---|---|---|---|---|---|---|
| hermes | duanwangye | 102957 | 45242 | 9733120 | 0 | 9881319 |
| hermes | ouyangfeng | 121204 | 14964 | 2199616 | 0 | 2335784 |
| hermes | wangyuyan | 542371 | 67713 | 6633216 | 0 | 7243300 |
| kimi | session_471d197c-742d-4b28-8964-ae47bb5df891/main | 40642 | 1615 | 229632 | 0 | 271889 |
| kimi | session_683d8e5d-c466-4f53-afe2-34337e851619/main | 116456 | 13076 | 5008896 | 0 | 5138428 |
| kimi | session_addf1b47-4524-4cfb-8fd7-8306a94d372a/main | 15834 | 2026 | 235776 | 0 | 253636 |
| kimi | session_c121c0d8-b048-48ab-a932-8be2e9a9458b/agent-0 | 96061 | 7785 | 539648 | 0 | 643494 |
| kimi | session_c121c0d8-b048-48ab-a932-8be2e9a9458b/agent-1 | 20125 | 5396 | 81920 | 0 | 107441 |
| kimi | session_c121c0d8-b048-48ab-a932-8be2e9a9458b/main | 172811 | 62922 | 15208448 | 0 | 15444181 |
| kimi | session_cc768dbf-2ad8-4efe-82b9-6fe6cae0a60c/main | 48088 | 1842 | 181760 | 0 | 231690 |
| **合计** | — | 1276549 | 222581 | 40052032 | 0 | 41551162 |

> hermes 行=角色（profile 名）；claude/kimi 行=会话文件（角色归因=cwd 粒度，混合角色会话为估算口径）。
> #514 接口：周聚合 = 本周日 JSON 合计 ÷ 同期 reviewed 单数（质量基线周报同源）。