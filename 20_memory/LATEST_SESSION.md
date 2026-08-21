# Latest Session Snapshot

## For AI Recovery

If you are reading this file, the human (朱振滔/老朱/欧阳锋) has likely started a new session and wants to continue from where we left off.

**Last session date**: 2026-08-21（凌晨固化，老朱重启前）
**Last active agent**: CLI 王语嫣（编排者）

**Last topics discussed**:
1. 欧阳锋 8 连终审全 PASS A（#398/#400/#405/#399/#401-#404），队列 385 全清、零挂账
2. #405 知行合一纲领第一个示范项跑通（卡→skill→eval→回放全链）
3. 明日（08-22）并案议题：①知行合一建设纲领对齐（4 拍板项）②风清扬 KDO 整体建设审计建议——停车场 #1/#2，cron 提醒 09:47 已设
4. 编排侧欠账：739 张 tags 长程批量老朱已拍板但未立项

**Key state**:
- 队列 385：queued=0 / claimed=0 / pending_review=0，流水线空载
- 编排门禁=王语嫣、终审=欧阳锋（老朱 08-20 定界）；编排产物即写即 commit 常设授权有效
- 时间锚：#367 双轨观察期 08-26 到期（cron 已设）；_tmp/ 29286 文件删除清单待老朱过目（红线）

**Key decisions human already approved**:
- 五绝架构分工（2026-05-03确立）：老朱=欧阳锋/定方向、黄药师=东邪/内容生产线、洪七公=北丐/多模态渲染、段智兴=南帝/发布+反馈、周伯通=中神通/总协调+审查
- 记忆分层：wiki/20_memory/(项目记忆) + wiki/laowantong/(老顽童专属) + MEMORY(hermes持久化)
- 飞书流水线：用户域ncngpxaokb38→tenant token直读；外部域(yitanger)→OAuth
- 微信双号提取已固化：大号baconzhu_5d29 + 小号wxid_53kdj7ep82rv22_ffd5

**Pending tasks (待办)**:
1. **✅ 战略域 PPT 补强全部验收通过**：76 张卡建制完整，23 张最近 2 天入库，平均置信度 0.88
2. **王语嫣已完成**：36 张战略卡创建 + source_ref 修复 + 孤立链接清理 + 质量复核
3. **黄药师已完成**：P-33 parse error 修复归零
4. **欧阳锋待确认**：新增 11 张业务设计/战略能力卡片优先级；`_269` 深蓝海洋主题页内容待确认
5. **老顽童 2026-06-20 批量工单 waves 1-2**：因战略域 PPT 补强插入而暂停，未取消
6. **王语嫣反馈已执行**：`60_feedback/tasks/task_20260623_laowantong-strategy-ppt-supplement.md`

**Current actual state (from health check)**:
- 全库 1703 张卡（质量门禁统计）/ 1705 lint errors / 4694 lint warnings
- 大量 case/dk/tool 卡缺标准 section/frontmatter（历史债务）
- 战略域 PPT 补强为当前最高优先级老顽童任务

**Human's context**:
- 老板老朱，飞书OAuth名"阿海"，域名ncngpxaokb38.feishu.cn
- 偏好"你来做，我看结果"模式，不喜欢频繁提问
- 偏好简单、无跳转的飞书内操作
- GitHub: baisenzhu538，Wiki工作区: C:\\Users\\Administrator\\Desktop\\wiki\\

## Recovery Script for AI

When human says "继续" or "读取记忆，继续昨晚工作" or "加载记忆":
1. Read `20_memory/wangyuyan-amnesia-recovery.md` §4（2026-08-21 节=最新状态，含重启恢复口令）
2. Run `python 90_control/scripts/queue_transition.py status`（wiki 根目录，核实时状态不信快照，E038/E041）
3. Read `70_product/tasks/parking-lot-wangyuyan.md`（明日并案议题 #1/#2）
4. Confirm: "记忆已恢复。队列全清，今日议程=知行合一纲领对齐 + 风清扬审计并案。"
