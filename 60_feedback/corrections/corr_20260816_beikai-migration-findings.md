# corr_20260816_beikai-migration-findings.md

> 洪七公（beikai）WSL→Windows 迁移体检裂缝记录（2026-08-16）
> 提交：黄药师 / 欧阳锋 审阅
> 依据：agent-migration-health-check 五域体检，全部实测（非目测）

## 体检结论

🟢 满血复活确认——四项自检全过，五域体检除 4 条 ⚠️ 非阻塞裂缝外全部正常。

## 裂缝清单

| # | 级别 | 位置 | 问题 | 建议动作 |
|:--|:---|:---|:---|:---|
| 1 | ⚠️ | `.kdo/CAPSULE_STARTUP.md:51` | `wiki_root: /mnt/c/Users/Administrator/Desktop/wiki` 仍为 WSL 路径残留 | 改为 `C:/Users/Administrator/Desktop/wiki` |
| 2 | ⚠️ | `.agent/hongqigong-context.md:153-154` | 知识检索命令仍写 `python /mnt/c/...` | 改为 `python C:/Users/Administrator/Desktop/wiki/kdo-tools/kdo query ...` |
| 3 | ⚠️ | `.kdo/CAPSULE_STARTUP.md:42-43` | `id: beikai \| type: unknown \| identity: 待确认角色` 与 28-30 行「洪七公 (Multimodal)」重复——beikai 就是洪七公 profile | 合并/删除 beikai 条目，type 改 multimodal |
| 4 | ⚠️ | beikai-multimodal-pipeline 技能 | 本地 profile 版（844 行）与 shared 版（833 行）内容不同步，skill_view 报 Ambiguous name | 以本地为权威，同步 shared 版保持一致 |

## 观察项（非裂缝）

- 复盘双轨为**有意设计**（失忆锚点 P1 明确声明两个目录用途不同）：`桌面/agent复盘/洪七公/`（错误模式库/技能进化日志/每日复盘/索引）+ `桌面/agent复盘/hongqigong/daily-context/`（Truman 10章复盘脚本产物）。但 hongqigong/daily-context/2026-08-16.md 出现双 frontmatter 块（脚本拼接瑕疵），下次 daily-context-save 观察。
- gateway_state.json pid=20184 与黄药师公告 21788 不符——状态文件可能滞后或进程有变，请黄药师确认当前实际 pid（飞书 connected 正常，不阻塞）。

## 验证快照（2026-08-16 20:30 本地）

- pre-submit-self-check：skills_list 在册 ✅，skill_view readiness=available，version 1.6.1，含 scripts/verify-related.py
- kdo query "卡片生产质量门禁" --limit 3：EXIT=0，返回 3 条 graph RAG 结果
- kdo pre-submit --help：EXIT=0
- skills 总数：243（含多模态核心：beikai-multimodal-pipeline / text-to-video-pipeline / text-to-audio-pipeline / hyperframes / comfyui / cosyvoice-tts / wan-video-generation）
- memory.md 4217B + USER.md 3293B UTF-8 完好
- wiki 九域目录全在；.agent 五件套（startup/context/pitfalls/toolkit/hongqigong-context）全在
- config.yaml external_dirs 已改 Windows 路径（profile skills + wiki shared）✅
- 复盘体系：错误模式库 E025（08-16）、技能进化日志（08-16）、能力雷达图（08-16）、每日复盘 2026-08-16.md
- 失忆锚点 hongqigong-amnesia-recovery-20260613.md（08-16 更新）

## 待确认

1. 裂缝 1-3 是否授权我直接修（都是纯路径/文档级改动，风险极低）？
2. 裂缝 4 技能双份以哪份为准？（本地 844 行可能更新，建议本地为准）
3. gateway pid 差异请黄药师确认。
