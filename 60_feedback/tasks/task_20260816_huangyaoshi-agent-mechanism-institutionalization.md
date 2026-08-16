---
id: task_20260816_huangyaoshi-agent-mechanism-institutionalization
assignee: huangyaoshi
status: reviewed
reviewed_by: 欧阳锋
review_date: 2026-08-16
priority: P2
wsjf: 3.0
created_at: 2026-08-16
updated_at: 2026-08-16
submitted_at: 2026-08-16
source: #325 终审 PASS A（2026-08-16 欧阳锋）→ P2 立项；停车场 P2-DYN-01 出池
related: #325 #324 #263 #321
---

# P2 机制制度化：agent 出生模板 + 健康检查巡检 + digest 门禁（#326）

## 背景

#324 诊断 + #325 终审（PASS A）确认：P1 存量补齐完成（检索接入已铺开）。P2 = **把机制制度化**，让两个持续变量（新 agent 产出、知识库增长）由机制吸收而非人工维护——这正是用户质询的"机制要动态变化"的落点。P2-DYN-01 设计（停车场，2026-08-16 王语嫣）出池执行。

## 任务

1. **agent 出生模板固化**（吸收"持续产出 agent"变量）：
   - #263 生产流水线部署步骤加**固定动作"挂 kdo MCP"**（参照 #325 挂载模板：mcp_servers.kdo + WIKI_ROOT/KDO_SRC env）——新 agent 出生即带检索能力，不再依赖"照先例手工补"
   - agent spec 模板（王语嫣编排侧）部署检查项同步：spec 验收清单加"MCP 挂载"项
2. **健康检查升级为持续巡检**（机制出问题的校验）：
   - 08-14 health-check（60_feedback/auto/）加巡检项：①每个 Hermes profile 的 mcp_servers.kdo 挂载检查（新增 5 个 + 已有 3 个）②新卡可检索抽查（终审闭环后 `kdo query` 命中验证）
   - 巡检结果进 friction-log/健康报告（持续化，非一次性快照）
3. **digest 门禁入流水线**（吸收"知识库增长"变量）：
   - #263 流水线 Step 4（#325 已加索引增量）配套：终审闭环时检查"新卡①挂域 digest ②kdo query 可检索"，缺则打回补挂
   - domain-mapping 挂接 digest（#321 销售域 digest 为先例样板）

## 验收标准

- #263 流水线文档：部署步骤含"MCP 挂载"固定动作 + Step 4 含 digest 门禁检查项
- agent spec 模板（如 60_feedback 侧 spec 模板文件）含 MCP 挂载检查项
- health-check 巡检项落盘 + **按实际运行 gateway 的 profile 位置（8 个 systemd service WorkingDirectory）逐挂载验证**（挂载检查全过或明确豁免）——⚠️ 2026-08-16 欧阳锋修正：#325 补挂的 Windows 侧副本对 5 个 WSL gateway 是空挂，巡检必须验证"运行进程读的配置文件"而非目录名同名文件
- 新卡可检索抽查命令实证（如终审闭环模拟 → kdo query 命中）

## 补充任务（2026-08-16 欧阳锋·#325 遗留修正并入）

**P1 收尾：5 个 WSL 侧运行中 gateway 补挂 kdo MCP**（beikai/duanwangye/laowantong/laowantong-feishu/ouyangfeng/wangyuyan——config 路径 `~/.hermes/profiles/<name>/config.yaml`，非 Windows 侧副本）。详见 #325 任务单"遗留修正"节。验证标准：修改后 `systemctl --user cat hermes-gateway-<name>` 的 WorkingDirectory 指向的文件含 mcp_servers.kdo。

## 补充任务 2：MCP 配置单一真相源化（2026-08-16 王语嫣·用户批准）

**背景**：双位置部署（WSL 侧实际运行 + Windows 侧副本）是长期结构性状态（O-12 迁移失败已回退，原因待查）。手工维护 16 个 profile 的 mcp_servers 节 = 漂移必然（#325 空挂已实证）。**用户提出更高层解法：不决策"哪侧运行"，消除"两侧差异"本身**——无论 gateway 从哪侧启动都能正确调用。

**技术事实**：`kdo-tools/mcp/server.py` 已跨平台（WIKI_ROOT 检测已修，兼容 /mnt/c/ 与 C:\）；唯一平台相关点 = config.yaml `mcp_servers.kdo` 的 command/args 路径。

**任务**：
1. **前置验证**：Hermes config.yaml 是否支持环境变量展开（若支持 → 方案可简化为单份配置 + 两侧 env；不支持 → 模板渲染）
2. **单一真相源模板**：`wiki/agents/hermes-mcp-template.yaml`（mcp_servers.kdo 定义一次，平台差异用占位符）
3. **sync-hermes-mcp.py**：按平台渲染分发到 16 个 profile（Windows 侧 command=Windows Python、WSL 侧 command=python3；args 引用 WIKI_ROOT 相对解析）
4. **一次性全量分发 + 验证**：16 个 profile 渲染后，按 systemd WorkingDirectory（WSL）与 Windows 侧实际消费方逐一验证 mcp_servers.kdo 生效

**验收**：①环境变量支持结论落盘（支持/不支持，实测依据）②模板 + sync 脚本落地 ③16 个 profile 全部为生成物（手改不再需要）④任一 profile 从 WSL/Windows 两侧启动 kdo_search 均可用（各抽 1 个实测）⑤漂移根治：改模板重跑脚本即可全量更新

**边界**：不改变 MCP 挂载的既有语义（只挂 kdo 检索 server，不扩散 feishu_doc）；O-12 迁移不依赖本任务（双位置共存下漂移已根治）；单角色单任务（E026）黄药师执行，欧阳锋终审

## 边界

- 机制文档/巡检脚本落地，不改运行中服务（#325 同款边界）
- 单角色单任务（E026）：黄药师执行，欧阳锋终审
- #321（销售域 digest）为配套内容任务，不阻塞本机制设计（可并行；门禁验证时引用其产出）

## 遗留联动

- P3 快照迁移（销售对话助理等 38 个编译产物→检索模式）未立项，本任务完成后作为 P3 立项输入

---

## 执行报告（2026-08-16 黄药师）

### 主任务 1：agent 出生模板固化 ✅

`30_wiki/workflows/workflow-kdo-agent-production-pipeline.md` Step 2 部署件表加 **"MCP 挂载 = 固定动作，不是可选件"**：
- 新 profile 名加入 `sync-hermes-mcp.py` 的 WINDOWS_PROFILES/WSL_PROFILES 列表 → 重跑 `--apply` → 跑 `check-mcp-roaming.py` 验证
- 模板/脚本 = MCP 配置唯一真相源（16 profile 全为生成物，改模板重跑即全量更新）
- 已从"照先例手工补"改为固定动作（#325 交付格式即模板格式，回归验证 SAME）

### 主任务 2：health-check 巡检升级 ✅

- 新脚本 `90_control/scripts/check-mcp-roaming.py`：16 profile 挂载检查（按 systemd WorkingDirectory 实证，非目录同名）+ 新卡可检索抽查（kdo query）
- 挂入 `health-check.py` 统一入口（非 quick 模式第 6 项，含 hints）
- 实测：17/17 PASS（16 profile + 检索抽查）

### 主任务 3：digest 门禁入流水线 ✅

`workflow-kdo-agent-production-pipeline.md` Step 4（索引事件驱动化）加 **digest 门禁检查项**：终审闭环时检查新卡①挂域 digest ②kdo query 可检索，缺则打回补挂（#321 销售域 digest 为先例样板，domain-mapping 挂接）

### 补充任务 1：WSL 5 个运行中 gateway 补挂 ✅

systemd 实证（8 个运行中 gateway）：**5 个读 WSL 原生 profile**（duanwangye/wangyuyan/ouyangfeng/beikai/laowantong-feishu，`/home/dministrator/.hermes/`）+ 3 个读 Windows 副本（basic-skills-coach/coaching/meeting，`/mnt/c/...`——#325 已挂）。
- WSL 原生 5 个全部补挂 kdo（sync 脚本渲染），备份 `.bak-mcp-sync-20260816`
- 老顽童无 systemd（已迁 Windows CLI）——WSL 侧 laowantong profile 一并挂载（统一生成物）
- duan/kimi-test 豁免（#325 已定：废弃/测试）——但 sync 全量渲染也带上（16/16 统一为生成物）

### 补充任务 2：MCP 配置单一真相源 ✅

| 项 | 结果 |
|:--|:--|
| 前置验证：env 展开 | ✅ Hermes 支持（`_interpolate_env_vars` 递归展开 MCP cfg 含 command/args，`${VAR}`/`${env:VAR}`，从 profile secret scope 解析）——但"单份配置+两侧 env"会把维护点分散到 16×2 个 .env，漂移转移；采用任务书主方案（模板渲染） |
| 单一真相源模板 | `wiki/agents/hermes-mcp-template.yaml`（mcp_servers.kdo 定义一次） |
| sync 脚本 | `kdo-tools/sync-hermes-mcp.py`：按平台渲染（Windows Python / WSL venv python + 各自路径）+ 文本级替换 kdo 子节（**其他 MCP 逐字保留**）+ 备份 + yaml 验证 + 幂等（重跑 SAME） |
| 一次性全量分发 | 16/16 profile 渲染（Windows 8 SAME=已一致；WSL 8 全 DIFF→已挂） |
| 双侧实测 | WSL + Windows 各跑 kdo_search("SPIN 销售") 协议级 **HIT** ✅ |

### 狗粮测试（用户要求，先狗粮再提审）✅

**抓出 3 个真问题，2 个已修 + 1 个历史遗留**：
1. ✅ **WSL 跨平台路径 bug**（delivery.py `_filter_by_trust`）：Windows 侧构建的 BM25 索引存 `C:/...` 格式，WSL 侧 `root / path` 拼接畸形 → 全滤空。已 patch（Windows 盘符路径 POSIX 下转 `/mnt/<盘符>/`）——patch 后 WSL kdo_search 从 MISS→HIT
2. ✅ **check-agent-config.py GBK 误报**：`open()` 无 encoding → 8 个 P0 阻塞中 5 个是编码误报。已修 `encoding="utf-8"`（P0 8→3，剩 3 个是 duan/kimi-test 的 kimi-coding 既定豁免）
3. ⚠️ **test_cli_smoke 历史失败**：text=True 无 encoding（GBK decode 崩）+ state.json `sources` 断言过期（SQLite 迁移后键移入 state.sqlite）——已修 encoding，state 断言是历史既有（工作区 460 行未提交改动的累积），记 friction-log 待排

**回归**：Windows kdo_search HIT 无回归；pytest 561 passed（1 历史失败如上）；sync 幂等 16/16 SAME；巡检 17/17 PASS。

### 验收对照

| 验收标准 | 结果 |
|:--|:--|
| #263 部署步骤含 MCP 挂载固定动作 + Step 4 含 digest 门禁 | ✅ 两处落盘 |
| health-check 巡检项落盘 + 按 WorkingDirectory 验证 | ✅ check-mcp-roaming.py 挂入，systemd 实证 |
| 新卡可检索抽查命令实证 | ✅ kdo_search("SPIN") 双侧 HIT |
| 补充 1：5 个 WSL gateway 补挂 | ✅ 5 原生 + 1 老顽童统一，备份 + 验证 |
| 补充 2：env 结论落盘 + 模板 + sync + 16 生成物 + 双侧实测 + 漂移根治 | ✅ 全过（幂等重跑 SAME 证明"改模板重跑即全量更新"） |
| 回归：不改变既有挂载语义 | ✅ beikai openmontage/laowantong wechat 逐字保留 |

### 遗留

- test_cli_smoke 的 state.json `sources` 断言过期——历史失败，建议排期修（低优先）
- delivery.py patch 是 KDO 源码修改——工作区未提交改动多（460 行历史累积），patch 已含 #326 注释，commit 时机由用户决定
- WSL gateway 重启后生效（不动运行中服务，边界）——重启后巡检自动验证
- P3 快照迁移：本任务完成后作为立项输入（任务书既有）

## 终审记录（2026-08-16 欧阳锋）

**verdict: PASS A · methodology v2.3**

O3 独立验证（全部字节级重跑，不采信报告）：
1. **#325 空挂修复确认**：WSL 侧 6 profile（duanwangye/wangyuyan/ouyangfeng/beikai/laowantong-feishu/laowantong）config.yaml 均含 kdo-tools/mcp/server.py 引用 + 备份 .bak-mcp-sync-20260816 存在——#325 遗留修正闭环
2. **单一真相源**：hermes-mcp-template.yaml（占位符 {{PYTHON}}/{{WIKI_ROOT}}/{{SERVER_PY}}/{{KDO_SRC}}）+ sync-hermes-mcp.py（--verify 16/16 已挂）+ 幂等重跑 SAME
3. **其他 MCP 保留**：beikai openmontage / laowantong wechat 逐字保留（挂载语义不变）
4. **巡检**：check-mcp-roaming.py 实测 17/17 PASS（按 systemd WorkingDirectory 实证 + 检索抽查命中）
5. **#263 文档**：Step 2 MCP 挂载=固定动作（L116/119）+ Step 4 digest 门禁（L160/164）落盘
6. **狗粮修复实证**：delivery.py L321-325 /mnt/ 盘符转换 patch 存在；check-agent-config.py L60 encoding 修复
7. **双侧 kdo_search**：Windows HIT（报告）+ WSL 侧独立重跑 HIT（需 KDO_SRC env——首次 MISS 为测试环境缺 env，非报告问题）

遗留确认（低优先不阻断）：test_cli_smoke state 断言过期；delivery.py patch 未提交（commit 时机用户定）；WSL gateway 重启后生效。

**结论**：PASS A，#325 空挂 + 双位置漂移根治闭环，机制制度化完成。
