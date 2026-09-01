# 王语嫣 Relay turn finalization 失败 — 证据记录

- 时间: 2026-09-01 23:07:21
- 会话: 20260901_220852_b0927f61 (wangyuyan profile)
- 现象: turn 正常结束（`Turn ended: reason=text_response ... response_len=777`）后，Relay finalization 抛异常：

```
WARNING agent.relay_runtime: Hermes Relay turn finalization failed
File "...\hermes-agent\agent\relay_runtime.py", line 644, in end_turn
    lease.host.run_in_session(...)
File "...\hermes-agent\agent\relay_runtime.py", line 217, in run_in_session
    return context.run(invoke)
File "...\hermes-agent\agent\relay_runtime.py", line 213, in invoke
    return callback(*args, **kwargs)
File "...\nemo_relay\scope.py", line 144, in pop
    _native_pop_scope(handle, output=output, metadata=metadata, timestamp=timestamp)
RuntimeError: invalid argument: scope handle is not at the top of the stack
```

- 影响: turn 结束后 gateway 没有 response ready 记录（上一条 ready 是 23:03:35），777 字符的最终回复疑似未投递到飞书。用户 23:08:26 又发消息追问，疑似没看到回复。
- 背景: 该 turn 之前有多次「Watch pattern notification — injecting」+ 后台进程完成通知注入（23:03:40、23:07:05 等），疑似 scope 栈被通知注入扰乱 → pop 顺序错乱。**注意 22:53 也发生过 watch pattern 注入，22:53:01 的 follow-up 处理正常**，但 23:07 这次 turn 结束时注入节奏更密（23:03:40 注入 + 23:07:05 注入夹着一个 turn）。
- 复现环境: Windows NSSM 服务 hermes-gateway-wangyuyan, Hermes Relay (nemo_relay scope 栈)
- 疑似触发模式: turn 进行中多次 watch-pattern/后台进程通知注入后，turn 结束时 scope 栈顶不是本 turn 的 handle
- 上游报障建议: hermes-agent 仓, relay_runtime.py end_turn / nemo_relay scope.py pop
- 修复方向(建议): end_turn 对 scope pop 做 try/except 兜底，finalization 失败时仍执行消息投递 fallback；或注入通知时不嵌套 push scope

关联: 当晚同一会话 1163.5s 慢响应根因 = 会话膨胀（247 条消息仅 8 条 user，其余为后台进程/watch pattern 注入）+ cron wangyuyan-clock-v4 deliver=origin 每 30 分钟喂会话。已改 deliver=local + 挂看护等 turn 结束后重置会话。
