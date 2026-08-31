---
id: "584"
title: "wechat-collect 管线 DeepSeek 推理模型 max_tokens 修复 + 注册副本路径锚点修复"
type: bugfix
status: queued
priority: P1
assignee: 黄药师
created_by: 王语嫣
created_at: 2026-08-31
updated_at: 2026-08-31
source_refs:
- 00_inbox/wechat-collect/_needs_rerun/_done-20260831/case-wechat-68004aecb3d913a5.reason.txt
---

# #584 wechat-collect 管线 LLM 空总结根因修复（已由王语嫣应急落地，本单做回归+固化）

## 事故经过（2026-08-31 22:09）

老朱视频号采集 2 篇新素材（68004aecb3d913a5 / 346efef2737b383b），自动管线转写✅→骨架✅→**LLM 三层次总结失败**（`<!-- LLM 总结失败，请重试 -->` 占位）→ #380 内容校验正确拦截退回 `_needs_rerun/`。

## 根因（探针实测实锤）

**deepseek-v4-flash 是推理模型**：思考链（reasoning_content）计入 completion_tokens，原脚本 `max_tokens: 1500` 被思考链烧光 → `finish_reason=length, content=''`。02:08 批次能过纯属思考短的运气；22:09 两篇思考长即爆。**不是额度问题**（API 调用成功计费正常）。

## 已应急修复（王语嫣 08-31 晚，git 本 commit）

1. `kdo-tools/wechat_knowledge.py`：max_tokens 1500→8192 + system 提示「直接输出不要思考过程」+ 空 content 显式打印 finish_reason/usage（不再静默落骨架）+ timeout 120→180
2. `40_outputs/code/scripts/wechat_{knowledge,promote}.py` 注册副本：路径锚点 `parent.parent` → 向上搜索 wiki 根（修复产出歪写 `40_outputs/code/00_inbox/` 的 bug），llm_summarize 已同步
3. 5 篇卡（08-31 两篇 + 02:08 遗留 3 篇）重产成功，已补 domain 轴/aliases/discoverable_by 落 `00_inbox/pending-cards/`
4. `_needs_rerun/` 7 件归档至 `_done-20260831/`

## 待黄药师

- [ ] 回归：跑 wechat_knowledge.py --all 全量 15+ 篇，确认无新失败
- [ ] 评估是否需要在管线里对 reasoning 模型换用非推理端点或显式 reasoning_effort 参数
- [ ] 双副本同步机制：kdo-tools/（真身）与 40_outputs/code/scripts/（注册副本）目前手工同步，考虑单一真身+软链或复制时校验
- [ ] 域轴修正（王语嫣 08-31 建议，老朱已批 inbox 自动化）：管线产出 frontmatter 的 `domain: wechat-video` 是来源轴不是知识域轴——建议管线默认写 `domain: pending-domain`，wechat-video 挪进 source_context；真实 domain 由编排层（王语嫣）按内容判定后改写（参照已入库 5 卡先例：strategy/ai-collaboration/kdo）

## 验收标准

- `python kdo-tools/wechat_knowledge.py --all` 0 失败占位
- 40_outputs 注册副本单独调用时产出路径正确
