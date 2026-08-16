# Hermes Gateway 锁冲突崩溃循环诊断备忘（2026-08-16）

> 状态：**已拍板方案 B**（2026-08-16 用户拍板，任务 #328 入队执行）
> 诊断：欧阳锋 + Codex 观察者（独立核查，结论一致）
> 未执行任何服务/进程操作

---

## 一、现象

8 个 Hermes gateway 中 3 个（beikai/duanwangye/wangyuyan）陷入崩溃循环：
- journal 反复出现 `Gateway already running (PID xxx)` → exit 1 → Restart=always 5s → 再拉起
- NRestarts 计数：wangyuyan user 级 1583 / beikai system 级 1429 / duanwangye system 级 1428
- 用户曾尝试"迁移到 Windows 侧"，表现为"反复重启"——与本次锁冲突同机制（迁移只是触发，不是根因）

## 二、根因：三套启动机制同时管理同一批 profile

```
① system 级 systemd（/etc/systemd/system/）：hermes-gateway-{beikai,duanwangye,wangyuyan}.service enabled
② user 级 systemd（~/.config/systemd/user/）：同名 3 个 + 其余 5 个（basic-skills-coach/coaching-leadership-assistant/laowantong-feishu/meeting-assistant/ouyangfeng）enabled
③ hermes-gateways-boot.service（system 级 enabled）→ /usr/local/bin/start-hermes-gateways：
   pkill -f "hermes_cli.main.*gateway run"   ← 全局杀所有 gateway！
   → screen 会话拉起 duanwangye/wangyuyan/beikai
```

**崩溃机制**：③ 的 pkill 杀掉 ①② 拉起的进程 → ①② 的 Restart=always 又拉起 → 新进程发现另一边健康实例持锁（gateway.pid）→ exit 1 → 循环。

**当前健康实例归属**（"最后活下来的那方"）：
| profile | 健康实例 | 归谁管 | 循环方 |
|:--|:--|:--|:--|
| wangyuyan | PID 263（system 级 cgroup） | system 级 | user 级同名服务循环 |
| beikai | PID 344 | user 级 | system 级同名服务循环 |
| duanwangye | PID 346 | user 级 | system 级同名服务循环 |
| 其余 5 个 | 343/345/347/348/349 | 仅 user 级 | 无冲突，NRestarts=0 |

## 三、证据链

- `/etc/systemd/system/hermes-gateway-{beikai,duanwangye,wangyuyan}.service` 存在且 enabled
- `systemctl list-unit-files` 与 `systemctl --user list-unit-files` 均显示 3 profile 双端 enabled
- `hermes-gateways-boot.service` enabled；`/usr/local/bin/start-hermes-gateways`（root，7-04 创建）含 `pkill -f "hermes_cli.main.*gateway run"` + 删 gateway_state.json + screen 拉起
- journal 三组 `Gateway already running (PID 263/344/346)` 反复出现
- user 级 beikai/duanwangye NRestarts=0；system 级 wangyuyan NRestarts=0——健康方重启计数为 0，循环方计数 1400+

## 四、待决策方案（用户拍板，未执行）

| 方案 | 内容 | 评估 |
|:--|:--|:--|
| A | 三个 profile 全归 system 级，禁 user 级同名 | ❌ 5 个健康 profile 在 user 级，动得最多 |
| **B（欧阳锋推荐）** | **全归 user 级**：禁 system 级 3 个 + 禁 hermes-gateways-boot.service | ✅ 8 个中 5 个已在 user 级健康；boot 脚本 pkill 隐患必须根除 |
| C | 按现状分治（wangyuyan→system、beikai/duanwangye→user） | ⚠️ 三套机制共存，boot pkill 隐患不除 |

**无论哪案，必须处理 hermes-gateways-boot.service**——其 pkill 全局杀进程，下次开机仍会杀掉 user 级进程。

**方案 B 执行清单**（确认后执行）：
1. `systemctl disable --now hermes-gateways-boot.service`
2. `systemctl disable hermes-gateway-{beikai,duanwangye,wangyuyan}`（system 级退役）
3. user 级 3 个 `systemctl --user restart` 对齐健康实例
4. 验证：8 profile 仅 user 级 service、NRestarts 归零

## 五、关联

- **O-12（WSL→Windows 迁移）**：本冲突是"迁移反复重启"表象的真因；迁移本身（双位置 profile）是独立问题，王语嫣"单一真相源"方案（#326 补充任务 2）照常推进，与崩溃循环解耦
- **#325 空挂教训**：双位置部署 + 多套管理器 = 配置与进程双重漂移源；观察者（Codex）发现 system/user 双 systemd 是本诊断增量——此前欧阳锋只查 user 级
- **待办**：用户拍板方案 → 执行 → 观察者记录修复前后对比（其首份观察样本）

*欧阳锋 · 2026-08-16（备忘，未动手）*
