---
title: Hermes WSL/Windows 两侧迁移任务编排建议书
type: proposal
proposer: Codex（系统观察者）
proposed_at: 2026-08-16
status: for-ouyangfeng-review
reviewers: [欧阳锋]
orchestrator: 王语嫣
---

# Hermes WSL/Windows 两侧迁移任务编排建议书

> 呈：欧阳锋（终审）
> 抄送：王语嫣（任务编排）、黄药师（基建执行）
> 提案人：Codex（系统观察者）
> 状态：待会审，通过后由王语嫣下发任务
> 原则：本建议书只做系统稳定性迁移，不替业务 Agent 做业务判断；每批任务必须可验证、可回滚。

---

## 一、背景与证据

### 1.1 问题现象

用户反馈：Hermes 在 WSL 侧运行明显慢，Windows 侧明显快。同时 WSL 侧出现 gateway 反复 auto-restart。

### 1.2 实测性能证据（2026-08-16，只读基准）

| 场景 | Windows 原生 | WSL 访问 `/mnt/c` | WSL 访问 ext4 |
|:--|:--|:--|:--|
| 读取 `30_wiki` 2778 文件前 4KB | **0.316s** | **8.511s（约 27x 慢）** | 0.639s |
| 枚举 `30_wiki` 2778 文件 | 0.011s | 0.077s | — |

结论：**主要瓶颈不是 WSL 本身，而是 WSL2 经 `/mnt/c` 访问 Windows 磁盘的 9P 文件系统开销。**

### 1.3 双管理器冲突证据

当前 beikai / duanwangye / wangyuyan 同时存在 system 级与 user 级 systemd unit，两边均 enabled。

| Profile | 健康实例 | 冲突循环方 | NRestarts |
|:--|:--|:--|:--|
| wangyuyan | system 级 PID 263 | user 级服务循环 | 1563+ |
| beikai | user 级 PID 344 | system 级服务循环 | 1412+ |
| duanwangye | user 级 PID 346 | system 级服务循环 | 1411+ |

日志反复出现：

```text
Gateway already running (PID 263)
Gateway already running (PID 344)
Gateway already running (PID 346)
```

### 1.4 工具链对比结论

- 核心 Python 库两边基本一致：paddleocr / fitz / PIL / cv2 / openai / httpx / pandas / numpy 均可用。
- Windows 侧还多出 tiktoken。
- WSL 侧更完整的是：Linux 浏览器、Linux 生态工具、Feishu/cron/systemd 集成、profile 级定制技能。
- Windows 侧目前缺口主要是：完整 gateway 管理、部分 profile、部分 Linux-only 工具。

---

## 二、目标与非目标

### 目标

1. 先解决 WSL 侧 system/user 双 manager 抢锁，恢复单实例稳定。
2. 将 wiki 读写密集型 Agent 迁到 Windows 原生，降低 `/mnt/c` 开销。
3. 保留 Linux-only 工具链，避免“一刀切”破坏现有多媒体/飞书能力。
4. 每批迁移均具备验收标准、观察窗口和回滚路径。

### 非目标

1. 本轮不重写 Hermes 核心架构。
2. 本轮不改变业务 Agent 的职责、审查标准、角色边界。
3. 本轮不强行把 Linux-only 工具迁到 Windows。
4. 本轮不删除历史数据，只做停用/归档。

---

## 三、建议任务清单

| 任务 | 内容 | 建议执行人 | 建议验收人 | 优先级 | 依赖 |
|:--|:--|:--|:--|:--|:--|
| T0 | WSL system/user 双管理器冲突止血 | Codex | 欧阳锋 | P0 | 用户确认 canonical manager |
| T1 | 三个最慢组合迁 Windows | Codex + 黄药师 | 欧阳锋 | P0 | T0 通过 |
| T2 | 纯 wiki 核心角色迁 Windows | Codex + 各 Agent 冒烟 | 欧阳锋 | P1 | T0/T1 稳定 |
| T3 | 飞书/多媒体重依赖角色处置 | 黄药师 + Codex | 欧阳锋 | P1 | 飞书 Windows 就绪测试 |
| T4 | 过渡 profile 归档/停用 | Codex | 欧阳锋 | P2 | T0-T3 稳定 + 用户确认 |

---

## 四、T0：WSL system/user 双管理器冲突止血

### 目标

让 WSL 侧每个 gateway 只由一个 systemd 管理器管理，消除无限 auto-restart。

### 建议方案

以 **user 级 systemd 为 WSL 侧 canonical manager**：

```text
停用 system 级：
  hermes-gateway-beikai.service
  hermes-gateway-duanwangye.service
  hermes-gateway-wangyuyan.service
  hermes-gateways-boot.service
```

### 执行步骤

```bash
# 1) 备份 unit 文件
mkdir -p ~/hermes-migration-backup/batch0/{system,user}
cp -a /etc/systemd/system/hermes-gateway-*.service ~/hermes-migration-backup/batch0/system/
cp -a ~/.config/systemd/user/hermes-gateway-*.service ~/hermes-migration-backup/batch0/user/

# 2) 记录迁移前状态
systemctl list-units --type=service --all --no-pager | grep hermes
export XDG_RUNTIME_DIR=/run/user/$(id -u)
systemctl --user list-units --type=service --all --no-pager | grep hermes

# 3) 停用 system 级 beikai / duanwangye
sudo systemctl disable --now hermes-gateway-beikai.service
sudo systemctl disable --now hermes-gateway-duanwangye.service

# 4) wangyuyan 从 system 级切到 user 级
sudo systemctl disable --now hermes-gateway-wangyuyan.service
systemctl --user reset-failed hermes-gateway-wangyuyan.service
systemctl --user start hermes-gateway-wangyuyan.service

# 5) 停用旧 boot 机制
sudo systemctl disable --now hermes-gateways-boot.service
```

### 验收标准

- system 级 beikai/duanwangye/wangyuyan 均 `inactive/dead` 且 `disabled`。
- user 级 8 个 gateway 全部 `active(running)`。
- `NRestarts` 不再持续增长。
- 观察 10 分钟，journal 无新增 `Gateway already running`。
- 每个 profile 只有一个 gateway 进程。

### 回滚方案

```bash
sudo systemctl enable --now hermes-gateway-beikai.service
sudo systemctl enable --now hermes-gateway-duanwangye.service
sudo systemctl enable --now hermes-gateway-wangyuyan.service
sudo systemctl enable --now hermes-gateways-boot.service
```

---

## 五、T1：三个最慢组合迁 Windows 原生

### 涉及 profile

```text
basic-skills-coach
coaching-leadership-assistant
meeting-assistant
```

这三个当前是“WSL 运行 + Windows profile”的最差组合。

### 执行步骤（每个 profile 独立执行，不并行）

1. 预检 Windows profile 完整性。
2. 备份 WSL unit 文件 + Windows profile 文件 hash。
3. 停止并禁用 WSL user 服务。
4. 验证旧侧无进程、无锁。
5. Windows 侧注册 Task Scheduler 或 WinSW/NSSM 服务。
6. Windows 侧启动 gateway，隐藏窗口。
7. 冒烟测试：版本识别 + `kdo query` + 读取对应 wiki 文件。
8. 观察 15 分钟，记录 CPU/内存/重启次数。
9. 通过后才处理下一个 profile。

### 验收标准

- WSL 侧对应服务 `inactive/dead` 且 `disabled`。
- Windows 侧 gateway 运行稳定，无崩溃。
- 冒烟任务输出与迁移前一致。
- 15 分钟内无 restart、无 lock 冲突。
- 任务耗时较 WSL 侧明显下降。

### 回滚方案

- 停止 Windows 侧 gateway。
- 重新启用并启动 WSL user 服务。
- 验证 PID、锁、NRestarts 恢复。

### 风险与备选

- 若 Windows 服务管理器未就绪，先使用 Task Scheduler + 隐藏进程过渡。
- 若某 profile 冒烟失败，立即回滚，标记“暂缓迁移”。

---

## 六、T2：纯 wiki 核心角色迁 Windows

### 涉及 profile

```text
wangyuyan
ouyangfeng
laowantong
```

### 前置条件

- T0、T1 已完成且稳定。
- Windows profile 已准备完整；ouyangfeng 缺失时先做只读 hash 核对后迁移。

### 执行步骤

与 T1 相同的单 profile 流程：预检 → 快照 → 停 WSL → 起 Windows → 冒烟 → 观察 → 验收/回滚。

### 冒烟标准

| Agent | 冒烟动作 | 通过标准 |
|:--|:--|:--|
| wangyuyan | 读 production-queue.md + kdo query | 读取结果与迁移前一致 |
| ouyangfeng | 读 1 张卡 + source_refs | 溯源路径正确，无路径漂移 |
| laowantong | 读生产队列 + 模拟领取任务 | 命令链路正常，不实际入队 |

### 验收标准

- 旧侧服务停止，新侧服务稳定。
- 冒烟任务全通过。
- 15 分钟观察窗口无异常。
- 关键文件路径无 `/mnt/c` 间接访问。

### 回滚方案

同 T1：停 Windows，恢复 WSL user 服务。

---

## 七、T3：飞书/多媒体重依赖角色处置

### 涉及 profile

```text
duanwangye
hongqigong
beikai
```

### duanwangye：先做飞书 Windows 就绪测试

若 Windows 侧飞书 MCP / Bitable API / 文档创建 / pre-ship-check 全通过：

- 按 T1 流程迁移 duanwangye。

若不通过：

- duanwangye 暂时留 WSL。
- 单独生成“飞书 Windows 迁移专项任务”，不阻塞其他批次。

### hongqigong / beikai：保持 WSL 为主

这两个依赖 ComfyUI/SD/TTS/ffmpeg/浏览器等 Linux 工具链，本轮不强行迁移。

建议形态：

```text
Windows 侧：负责 wiki 读取、任务下发、结果汇总
WSL 侧：继续作为 Linux 工具执行器，处理 OCR/生图/视频/音频
```

### 验收标准

- duanwangye 若迁移：飞书发布链路冒烟通过。
- hongqigong/beikai：保留 WSL gateway 稳定运行，工具调用无退化。
- 所有多媒体任务可正常访问 Linux 工具链。

### 回滚方案

- duanwangye 迁移失败：回滚 WSL。
- hongqigong/beikai：本轮不改，无需回滚。

---

## 八、T4：过渡 profile 归档/停用

### 涉及 profile

```text
note-coach
kimi-test
duan
```

### 执行原则

1. 先记录用途与最后活跃时间。
2. 用户确认不再使用。
3. 停用服务 + 归档 profile，不删除。
4. 观察 7 天后再决定是否真正删除。

### 验收标准

- 相关服务 inactive 且 disabled。
- 数据归档到指定目录，hash 完整。
- 无其他服务依赖这些 profile。

---

## 九、编排依赖图

```text
用户确认 canonical manager
          ↓
         T0 冲突止血
          ↓
         T1 三个慢组合
          ↓
   T2 纯 wiki 核心角色
          ↓
   T3 飞书/多媒体重依赖
          ↓
   T4 过渡 profile 归档
```

---

## 十、会审决策点（请欧阳锋裁定）

1. **T0 是否同意“WSL 侧以 user 级为 canonical manager”？**
2. **T1 是否先行执行？**
3. **T2 中 ouyangfeng 的 Windows profile 由谁补全：黄药师还是 Codex？**
4. **T3 中飞书 Windows 就绪测试，由黄药师出方案，还是先由 Codex 做只读探测？**
5. **T4 是否本轮入队，还是挂停车场等用户确认？**

---

## 十一、请王语嫣编排建议

若会审通过，建议按以下顺序入队：

```text
P0：T0 → T1
P1：T2 → T3
P2：T4（挂停车场）
```

每个任务均需携带：

- 执行人
- 验收人
- 验收标准
- 回滚方案
- 观察窗口
- 依赖任务

---

*Codex（系统观察者）· 2026-08-16*
---

## 王语嫣编排意见（2026-08-16 会审）

### 会审组成确认（用户：大家一起会审，执行 Codex）

| 角色 | 职责 |
|:--|:--|
| 用户（老朱） | 拍板决策点 1/4/5 |
| 欧阳锋 | 架构终审（reviewers 既定） |
| 王语嫣（我） | 编排裁决 + 任务拆分入队 |
| 黄药师 | 基建执行验证（profile 补全/飞书就绪测试出方案） |
| Codex | **提案人 + 执行人**（用户授权：外部观察者转执行，全局认知）——T0/T1/T2/T4 执行，T3 协助 |

### 决策点意见（5 条）

1. **canonical=user 级：✅ 采纳（#328 实证已 PASS）**——#328 崩溃循环方案 B 已执行完全相同的方案（user 级唯一管理器+boot/system 退役+linger 确认+NRestarts 归零≥10min 验证，欧阳锋已终审）。**T0 与 #328 同向，建议 T0 改为"验收确认"而非重复执行**（补 journal 无新增 Gateway already running 的长观察即可）
2. **T1 先行：✅ 采纳**（/mnt/c 27x 实测是真实瓶颈，三个最慢组合迁移收益最大）
3. **ouyangfeng Windows profile 补全：黄药师**（基建域操作，codex 转执行后仍以黄药师为基建权威）
4. **飞书 Windows 就绪测试：黄药师出方案 + Codex 只读探测协助**（方案归基建域，探测可并行）
5. **T4 挂停车场：✅ 采纳**（等用户确认 + T0-T3 稳定，不本轮入队）

### 编排建议（会审通过后入队）

```
P0：#342 T0 验收确认（#328 实证引用）→ #343 T1 三个慢组合迁移（Codex 执行/黄药师验证）
P1：#344 T2 纯 wiki 核心角色（wangyuyan/ouyangfeng/laowantong）→ #345 T3 飞书多媒体处置（duanwangye 就绪测试先行）
P2：#346 T4 过渡 profile 归档（挂停车场，用户确认后入队）
```

每个任务携带：执行人/验收人/验收标准/回滚方案/观察窗口/依赖（建议书 §11 要求）。

### 与 #338 关系

#338 PatrolKit 设计已解耦挂起（待本迁移会审结论）——迁移稳定后启动，不冲突。

---

## 会审裁决汇总（2026-08-16 王语嫣独立判断——黄药师增量全采纳）

### 黄药师 4 条增量：全部采纳

| 增量 | 裁决 | 理由 |
|:--|:--|:--|
| ①T3 beikai/hongqigong 整体留 WSL 不拆双实例 | ✅ 采纳（修正建议书 T3 表述） | openmontage 886MB Linux 工具链（remotion-composer）Windows 无对应；瓶颈不在 /mnt/c；双实例复杂度（飞书双通道+路由+新部署）> 收益 |
| ②T1 直接 WinSW/NSSM 不用 Task Scheduler | ✅ 采纳（修正建议书 T1） | Task Scheduler 无崩溃自动重启；#328 教训：Restart=always+RestartSec=5+KillMode=mixed 是保命配置 |
| ③飞书就绪测试前置已满足（lark-cli Windows auth ready） | ✅ 采纳 | #306 封装实测（黄药师一手）；就绪测试聚焦 Bitable API/文档创建 |
| ④ouyangfeng 补记忆连续性验收 | ✅ 采纳（补 T2 验收） | 迁移后先跑失忆恢复路径再开始审查（8-15 恢复指引过期教训） |

### T0 修正（三方一致：不重复执行，补进程级检查）

T0 = **验收确认**（#328 已执行同方案且 PASS A）：
- systemd 状态检查（boot disabled / system 级无 active / user 级 8/8 running）
- **补 pgrep 进程级唯一性**（黄药师增量：#328 实测锁冲突是进程级问题，systemd 状态≠进程无残留）：`pgrep -fc "hermes_cli.main.*gateway run"` 应 = 8
- journal 无新增 Gateway already running（长观察）

### 修订后编排方案（会审通过后入队）

```
P0：#342 T0 验收确认（#328 实证+pgrep 进程级检查）→ #343 T1 三慢组合迁 Windows（NSSM 服务化）
P1：#344 T2 核心角色（wangyuyan/ouyangfeng/laowantong；ouyangfeng 含记忆连续性验收）→ #345 T3 duanwangye 飞书就绪测试（Bitable 聚焦）；beikai/hongqigong 整体留 WSL 明确
P2：#346 T4 过渡 profile 归档（停车场，用户确认后入队）
```

执行人：Codex（用户授权）+ 黄药师基建验证；验收：欧阳锋。

---

## 洪七公 CLI 实测意见采纳（2026-08-16 王语嫣独立判断——四方一致）

### 结论：canonical=user 级，证据链闭合（#328 实证 + 洪七公实测 + 黄药师 + 王语嫣 四方一致）

洪七公实测（与 #328 交付完全吻合）：system 级 4 unit 全 disabled / user 级 8/8 running / linger=yes / NRestarts 停 86-89 零增长 / 2542 条 already-running 全集中 #328 切换 5 分钟窗口，之后 10 小时零新增。

### 3 条注意事项：全部采纳（写入 T0 验收 + 运维手册）

1. **system 级 unit 文件保留不删**（disabled 状态）——T0 回滚路径 + 架构变迁文档（与 #328 交付一致）
2. **XDG_RUNTIME_DIR 运维坑**：查 user journal 前必须 `export XDG_RUNTIME_DIR=/run/user/$(id -u)`（洪七公实测第一遍查询踩坑）——写入运维手册/skill
3. **linger 是命门**：`wsl.conf systemd=true` + linger 两条 = **常驻验收检查项**（防 WSL 升级重置），不只 T0 验一次

### T0 确认（四方一致：验收确认不重跑）

- 现状已满足建议书 §四全部验收标准
- 补：Codex 按标准流程做一次**正式 10 分钟观察记录落盘**（洪七公 60 秒零增长 + 10 小时零新增可作证据引用）
- 验收命令含 pgrep 进程级唯一性（黄药师增量）+ XDG_RUNTIME_DIR 前置（洪七公坑）

---

## 架构终审裁定（2026-08-16 欧阳锋）

**verdict: 裁定通过 · canonical=user 级 · methodology v2.3**

O3 独立抽查（XDG_RUNTIME_DIR 前置后）：
1. **NRestarts 零增长确认** ✅：beikai 86/duanwangye 89/wangyuyan 86——与洪七公实测、#328 交付三方一致，10 小时+ 无新增
2. **进程级唯一性确认** ✅：ps 列表 8 个 gateway 进程 = 8 profile 各 1（343/345/347/348/349 + 58481/58502/58682），无锁残留——T0 的 pgrep 标准可执行（pgrep -fc 输出 9 为 shell 模式匹配时序差，ps 实查 8 为准，T0 验收时用 ps 逐行确认）
3. **四方一致采纳**：canonical=user 级与 #328 执行方案完全一致（我当时诊断推荐方案 B），证据链闭合
4. **3 条注意事项全采纳确认**：system unit 保留（回滚路径）/ XDG 前置（洪七公实测坑，我本次抽查即踩到——不 export 查不到 user journal）/ linger 常驻检查（防 WSL 升级重置）

**裁定**：✅ 通过。王语嫣可按 #342-346 拆分入队：
- #342 T0 验收确认（不重跑 + pgrep 进程级 + XDG 前置 + linger 常驻项）
- #343 T1 三慢组合迁 Windows（NSSM 服务化，#328 教训：Restart=always+RestartSec=5 保命配置）
- #344 T2 核心角色（ouyangfeng 含记忆连续性验收——8-15 恢复指引过期教训）
- #345 T3 duanwangye 飞书就绪测试（Bitable 聚焦）
- #346 T4 过渡 profile 归档（P2 停车场，用户确认后入队）

执行人：Codex（用户授权）+ 黄药师基建验证；验收：欧阳锋。beikai/hongqigong 留 WSL 明确（openmontage MCP WSL 专用）。

*欧阳锋 · 2026-08-16 架构终审裁定*

## 架构裁定更新（2026-08-16 欧阳锋·用户新决策）

**变更**：用户拍板"洪七公启动不起来，全量迁 Windows，以后全量都是 Windows，codex 已在操作"——**推翻原裁定"beikai/hongqigong 整体留 WSL"**。

**修订后目标态**：全部 profile 归 Windows 侧（.hermes + AppData），WSL 侧退役。beikai 的 openmontage MCP 需确认 Windows 兼容性（openmontage 原为 WSL 路径 /home/dministrator/kdo/...，迁移需重挂 Windows 路径或确认跨平台）。

**beikai 启动失败观察**（我核查）：19:44:51 已 running（飞书 connected），日志有 SQLite 3.50.4 WAL-reset 漏洞警告（kanban.db）——**可能根因线索**，迁移/修复时关注（`hermes update` 可修嵌入式 runtime）。

**执行人**：codex（用户授权，操作中）。**验证**：欧阳锋——codex 操作完成后按 T0 标准验收（进程级唯一性 + XDG 前置 + linger 常驻 + 飞书连接）。
