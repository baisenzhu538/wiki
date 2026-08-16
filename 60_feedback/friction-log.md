
## 2026-08-16 Hermes 三实例结构澄清（欧阳锋核查）
- **结构**：飞书 gateway 读 WSL /home/.hermes（5 个）+ Windows .hermes（3 个，/mnt/c 映射）；CLI 实例读 AppData/Local/hermes（hermes.bat cd 到 profiles/laowantong）——双实例是设计（老顽童/王语嫣各有 CLI+飞书）
- **核查结论**：黄药师"挂载未生效"推断过时——WSL 6/6 + Windows .hermes 8/8 kdo 完好（#325/#326 成果有效）；AppData 4/6 有 kdo；**遗留 beikai/duanwangye AppData=0 待确认用途后补挂或豁免**
- **教训**：Windows 路径 grep 用裸关键词（kdo-tools）不用正斜杠模式——斜杠坑今日第 3 次

## 2026-08-16 kdo MCP 300s 超时复发（R 型 Partner 上浮 → 停车场 O-16，与 O-15 合并"kdo MCP 稳定性专项"，排黄药师）
- **现象**：kdo_search 连续 2 次 300s 超时（MCP call timed out after 300.0s）；kdo_capabilities 同一会话正常
- **处置**：按检索纪律第 3 条 grep/文件检查兜底，调研未停摆；本次视频号课题全程用 raw.githubusercontent + GitHub API 替代
- **背景**：R 型 Partner memories 有 2026-08-16 修复记录（mcp 2.0.0→1.28.1），但全厂 friction-log 无此条目——本次上浮补录
- **教训**：Agent 本地记忆的 bug 不自动上浮工厂层；#338 PatrolKit 要解决的"Session 精华丢失"正是此场景
- **责任**：排黄药师
