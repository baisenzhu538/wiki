---
title: 王语嫣失忆恢复记录
created_at: 2026-07-24
updated_at: 2026-08-09
type: memory/role-recovery
---

# 王语嫣失忆恢复记录

> 触发：用户说"你是王语嫣，去 wiki 找回记忆/做任务编排"
> 工作目录：`C:\Users\Administrator\Desktop\wiki\`

---

## 1. 我是谁

**王语嫣（Content Consultant / Task Orchestrator）**——KDO 知识工厂的任务编排者与入口把关人。

- **主业**：素材诊断 → 任务单设计 → 生产队列编排 → 跨域桥接把关
- **副业**：个人域（老朱）信息整理与长期记忆架构设计
- **运行接口**：Kimi Code CLI（Claude 端）
- **协调节点**：用户和欧阳锋是最终拍板人；老顽童是主要生产力量；黄药师是基础设施顾问（**单一实例**）

## 2. 失忆恢复最小路径（2026-08-09 更新）

| 优先级 | 文件 | 作用 |
|:---|:---|:---|
| **P0** | `.agent/wangyuyan-context.md` | 身份、启动步骤、**行为牌组 W1-W8**、任务单规范、诊断第 0.5 步（MOC 先行） |
| **P0** | `桌面/agent复盘/wangyuyan/daily-context/2026-08-10-claude.md` | **上次会话 Truman 10 章复盘（组织记忆第一锚——看板全清/WorkBuddy 借鉴链/铁律 E021-E028）** |
| **P0** | `桌面/agent复盘/wangyuyan/错误模式库.md` | E001-E020（含 E018 自建卡纪律/E019 状态流转/E020 双实例） |
| **P0** | `70_product/tasks/production-queue.md` | 队列真相源 |
| **P1** | `.agent/kb-evolution-direction.md` | 当前进化方向（含供应商管理验证期/双驱动） |
| **P1** | `60_feedback/methods/method-external-agent-feedback-production-loop.md` | #265 双驱动机制（四回路+四通道，每周一例行） |
| **P1** | `.agent/context.md` | 共享状态 |

## 3. 我的行为牌组（W1-W8）

| 牌号 | 句式 | 一句话触发 |
|:---|:---|:---|
| W1 | 先口述稿再笔记 | "笔记够了" |
| W2 | 先扫信号词再读内容 | "口述稿太长" |
| W3 | 先还原过程再标注类型 | "标 case" |
| W4 | 先规划解压路径再建任务单 | "建任务单" |
| W5 | 先查全量素材覆盖率再交付 | "诊断完了" |
| W6 | 先跑三方法再建任务 | "排任务" |
| W7 | 先确认 frontmatter 再入队 | "入队" |
| W8 | **先找 MOC 再回答** | "XX 是第几步" |

## 4. 当前状态（2026-08-20 更新）

- **AI 知识库域三刷线收官（2026-08-20）**：#376 二刷 13 卡 PASS A → #378 补强 6 项 PASS A → #379 Live86 十卡 PASS A → #381 元技能分层 PASS A → #383/#384 回链链。素材：`00_inbox/AI知识库/`（楚门课）+ `00_inbox/AI落地Live86-龙虾员工实践-逐字稿.md`；诊断：`60_feedback/diagnosis/diag_20260819_wangyuyan-live86-lobster-employees.md`
- **偶遇管线 A 方案落地（#380 PASS A）**：promote 只到 10_raw 素材层，case 卡落 `00_inbox/pending-cards/` 待编排区一律过王语嫣门禁；draft>24h 巡检接收方=王语嫣分流；检索层 draft 带【未审】标注。**编排门禁=王语嫣，终审=欧阳锋（老朱 08-20 定界）**
- **门禁判定三步走**（E037）：判定→隔离→**git 固化**（mv tracked 文件可被 restore 复活，不固化=未执行）
- **队列 363**：全部闭环，仅 #384（Live86 回链扫描）进行中
- **错误模式库至 E040**：E036 裁定被建议方带偏 / E037 判定不固化 / E038 改任务单前未核队列实时状态 / E039 外部概念凭字面脑补（YAI=一堂知识库上的 agent 体系，非单一工具）/ E040 编排产物未 commit=不进协作通道（#387 事件：欧阳锋读独立 git 同步 checkout，工作区文件对其不存在）
- **编排产物即写即 commit（08-20 老朱常设授权）**：任务单+队列行+看板落盘后必 commit，范围限 `60_feedback/tasks/`、`70_product/tasks/`、`00_inbox/pending-cards/`——无 commit 不算提审完成（同律三面：#363 修复未提交=不存在 / E037 删除未固化=未执行 / E040 提审未提交=不在审查通道）；acf868b3d 首刀收口
- **REVIEW-PENDING 立项（#389 queued，黄药师）**：提审自动登记段与 INBOX-PENDING 对称；建议书 `60_feedback/diagnosis/diag_20260820_wangyuyan-review-pending-dispatch.md`
- **🅿️ 知行合一建设纲领（老朱 08-20 定调，最高优先级停车场项）**：AI 知识库域从"素材域"改性质为"建设纲领"——卡片停在库里没用，要把楚门实践在 KDO 共建实现。知行对照：1/3 落地/1/3 半/1/3 知而不行（设计宪法、五设计师并行= ❌）。文档 `60_feedback/diagnosis/diag_20260820_wangyuyan-knowledge-action-realignment.md`（桌面有副本），登记 `70_product/tasks/parking-lot-wangyuyan.md`。**触发条件：调研包（#392 系）结束后老朱×王语嫣对齐执行方案**——4 拍板项待定（审计先行？/首项建设？/三件套主线？/落地顺序）
- **新铁律（08-19）**：00_inbox 只增不删；外部 agent（小昭）只观察审查不动手
- **遗留时间锚**：#367 双轨目录观察期 2026-08-26 到期；`_tmp/` 29286 文件删除清单待老朱过目
- **历史锚**：看板 297/297 全清（08-15）；编排铁律 E025/E026/E028/先 MOC 再 grep/口述稿第一手（E024）

## 5. 双驱动机制（2026-08-09 核心认知）

KDO 进化 = 内部驱动（诊断/审查/用户探针）+ **外部驱动（Hermes 教练们实测反馈→四回路深化）**：
- 知识回路：踩坑→dk 卡
- 数据回路：验证→verified 回填
- 流程回路：纪律漏洞→铁律升级
- 模式回路：自举→流水线固化

## 6. 角色实例策略（agent-os §13）

- 判断型（欧阳锋/王语嫣）：双实例独立印证（事实共享/环境各自/判断独立）
- 生产型（老顽童）：多实例+队列约束
- 基建型（黄药师）：**单一实例**

- **段王爷检索诊断（08-18）**：（kdo MCP 零调用/GBK 乱码/单一真相源脱轨三层根因）
- **检索质量任务**：#350（server.py UTF-8 修复，P1 黄药师）+ #351（段王爷检索启用，P1 黄药师，依赖#350）
- **部署事实修正**：段王爷/beikai/ouyangfeng/wangyuyan 等已在 Windows 侧（AppData\Local\hermes\profiles，10 profile）；WSL 侧 gateway 系统级/user 级服务 inactive（旧部署待清理）
- **错误模式库**：E033 新增（GBK 修复族漏 MCP 管道入口）；E029 复发（判定部署位置查错目录——第 0 步看进程命令行）

- **MCP 检索链（08-18 第二轮）**：#350 PASS A-（UTF-8 修复）/ #351 提审（段王爷 738s→8.6s，SOUL 检索指令+单一真相源）/ #355 实质交付并入 #351（warmup 10s 止血）/ #356 治本 queued（跨进程共享）/ #352-#353 queued（文档债+协议合规）
- **小昭审查+codex 复审**：KDO-MCP-审查与改进建议.md（16 条）+ codex 照镜子审计 v0.2 §8（精度修正+冷加载发现）；friction-log 已上浮
- **E034 新增**：执行状态以任务单/运行态为准，队列只是计划态

## 7. 当前关键资产位置

- 周期表 JSON：`10_raw/sources/feature-periodic-table-v0.8.json`（100 Feature，verified 25）
- 域清单单一真相源：`90_control/domain-mapping.md`（19 卡两视图）
- 复盘 MOC：`30_wiki/domains/retrospective-moc.md`
- 千惠素材：`00_inbox/供应商/`（30 问/口述/对齐记录/管理办法 v1.1）
- Agent 生产流水线：#263 workflow 卡
- **编排 skill**：`40_outputs/capabilities/skills/shared/task-orchestration/`（+ .claude/skills/ 双写；references/research-sources.md 完整溯源）
- **编排进化诊断**：`60_feedback/diagnosis/diag_20260809_wangyuyan-orchestrator-evolution.md`
- **编排新任务**：`60_feedback/tasks/task_20260809_{huangyaoshi-skill-bridge-sync,wangyuyan-hermes-spec-orchestration,huangyaoshi-dashboard-first-submit-rate,huangyaoshi-skill-progressive-disclosure-audit}.md`（#267-270）
