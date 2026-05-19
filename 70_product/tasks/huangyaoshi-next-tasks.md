# 黄药师后续任务（顺序执行）

## 任务方：黄药师（WSL tmux `claude`）

## 状态

- P0: `kdo validate --v15` ✅
- P1-A: `kdo lint --accept-baseline` ✅
- P1-B: `kdo lint --structure-report` ✅
- P2-A: 工业化手册 v1.7 ✅
- P2-B: `kdo backup` ✅
- P3: `kdo validate --v15 --upgrade-plan` ✅
- domain filter bug fix ✅

**当前状态**：空闲，待接新任务。

---

## 原则

1. **顺序执行**，不做完上一个不开下一个
2. **每完成一个 → 跑 pytest 全量**，确认无回归
3. **每完成一个 → 更新本文件的完成标志**
4. **完工后通知欧阳锋审查**

---

## Task 1：`kdo scaffold`（P0，现在就开工）

### 工单

[[70_product/tasks/kdo-scaffold-v15.md]]

### 为什么先做

`kdo validate --v15 --upgrade-plan` 诊断了 89 张 FAILED 卡每张缺什么，但老顽童修卡时每张都要从空白页开始搭 Critique/不要用/AT 的框架——定格式、查学者、写占位是重复劳动。scaffold 自动化这一步，老顽童拿到的是"框架已搭好、学者方向已建议"的卡，只填内容。

### 核心做什么

`kdo scaffold --card <id>` 读卡→诊断缺失→追加 TODO 骨架。不覆盖已有内容。

```
kdo scaffold --batch A --write    # 全信号缺失高引卡，第一批开工
kdo scaffold --card yt-pitch-metaphor  # 单卡 dry-run
```

智能部分：攻击者建议——扫描同 domain 下已有 Critique 的卡，提取攻击者名→去重→按频次排序→推荐 top 3。

### 验收

- [ ] 对缺 Critique / 缺不要用 / 缺 AT 的卡分别正确生成骨架
- [ ] `--batch A/B/C/D/E` 分组正确
- [ ] 攻击者建议不推荐该卡已有的攻击者
- [ ] `--write` 写入后原卡已有内容完整保留
- [ ] 对 205 张真实卡运行无崩溃
- [ ] pytest ≥8 新 test cases，全绿

### 估时

~200-250 行代码，~2-3 小时。

---

## Task 2：设计域转录稿清理工具（P1）

### 背景

`00_inbox/design/` 有两份 AI 设计培训的语音转文字稿（月白老师分享），是 ASR 实时输出——口语化严重、有填充词、分段破碎、有回音/网络问题导致的乱码。老顽童做设计域编译前，需要先清理。

手动清理两份长文太慢。黄药师做一个自动化预处理工具。

### 要做什么

`kdo clean-transcript <file>` 或集成到 `kdo ingest --clean`：

1. **去噪**：删除口头禅（"呃"、"就是"、"那个"、"有没有回音"、"现在还有回音吗"）、重复的互动询问（"有回音吗"在文中出现多次）、网络中断提示
2. **分段**：识别主题转换信号（"第二个..."、"下一个..."、"我们来说..."、"总结一下"），按主题切为段落
3. **标点修复**：ASR 输出无标点或标点错误，基于语义停顿插入句号/逗号
4. **术语标注**：识别 AI 设计术语（GAN、VAE、Diffusion、GPT-2o、Nano Banana、巨米4.0），用 backtick 包裹或斜体
5. **输出**：清理后的 `.md` 文件到 `10_raw/sources/` 或原地 `00_inbox/design/cleaned/`

### 技术方案（三种，从轻到重）

| 方案 | 实现 | 优点 | 缺点 |
|------|------|------|------|
| **A. 规则引擎** | Python 正则 + 关键词词典。去噪=正则删除匹配行。分段=检测主题转换词。术语=术语表匹配 | 轻量、无依赖、可控 | 规则覆盖不全，边缘 case 多 |
| **B. LLM 批处理** | 调 DeepSeek API，分块送入 LLM，用 system prompt 指定清理规则。每块 ~2000 tokens | 质量最高，处理口语化/ASR 错误效果好 | 需 API key，有成本（~$0.1-0.3/全文），速度慢 |
| **C. 混合** | 规则引擎做粗清理（去噪+分段），LLM 做精修（标点修复+术语标注+语义纠错） | 兼顾速度和质量 | 架构复杂度最高 |

**建议方案 A（规则引擎）MVP 先跑通**。两份转录稿的噪音模式相对固定（同一平台、同一 speaker），规则覆盖率高。如果效果不够再加 LLM 精修。

### CLI

```bash
kdo clean-transcript 00_inbox/design/AI设计-AI设计基础01.txt --output 10_raw/sources/
kdo clean-transcript 00_inbox/design/ --output 10_raw/sources/  # 批量
kdo clean-transcript ... --method llm   # LLM 精修模式（如果实现）
```

### 验收

- [ ] 去噪：口头禅删除率 >80%（人工抽检 50 行）
- [ ] 分段：主题边界准确，不把同一主题切成两段
- [ ] 术语：GAN/VAE/Diffusion/GPT-2o/Nano Banana 正确标注
- [ ] 输出是合法 Markdown
- [ ] 清理后文件行数 < 原文 70%（去除了噪音行）
- [ ] 不丢失案例细节（Leo 案例必须完整保留）
- [ ] pytest ≥3 新 test cases

### 估时

~100-150 行（规则引擎方案），~1-2 小时。

---

## Task 3：`kdo validate --v15 --watch`（P2）

### 背景

老顽童修 89 张卡时，每修完一张需要手动跑 `kdo validate --v15 --card <id>` 看是否通过。更高效的方式：启动 watch 模式，文件保存时自动重检目标卡片，实时反馈。

### 要做什么

`kdo validate --v15 --watch [--domain <d>]`：

1. 用 `watchdog`（或纯 Python `os.stat` 轮询）监听 `30_wiki/concepts/` 目录
2. 检测到 `.md` 文件变更（防抖 2 秒）→ 自动对该文件运行 `validate --v15 --card`
3. 输出结果到终端（pass/fail/warn + 缺失信号详情）
4. `Ctrl+C` 退出

### 技术方案

**纯 Python 标准库方案**（零依赖，与 KDO 原则一致）：
- `os.stat` 轮询 + `time.sleep(1)`，不需要 watchdog 第三方库
- 防抖：2 秒内同一文件的多次变更合并为一次验证
- 输出用简单的 PASS/FAIL/WARN 前缀，可加 `--json` 输出

### CLI

```bash
kdo validate --v15 --watch                     # 监听全库
kdo validate --v15 --watch --domain yitang     # 只监听指定域
kdo validate --v15 --watch --json              # JSON 输出（给 CI/tmux status）
```

### 验收

- [ ] 修改一张卡并保存 → 2 秒内自动验证该卡
- [ ] 防抖正常：连续保存 3 次只触发 1 次验证
- [ ] `Ctrl+C` 正常退出
- [ ] 不监听非 `.md` 文件和 `.obsidian/` 目录
- [ ] `--domain` 过滤正常
- [ ] 全量 pytest 无回归（不阻塞 CI——watch 测试用 subprocess 超时）

### 估时

~80-100 行，~1 小时。

---

## 完成标志

| 序号 | 任务 | 工单 | 验证 |
|------|------|------|------|
| 1 | `kdo scaffold` | [[70_product/tasks/kdo-scaffold-v15.md]] | pytest ≥8 新 tests 全绿 + 对 205 张卡无崩溃 + 欧阳锋审查 |
| 2 | 转录稿清理工具 | 本文件 Task 2 | pytest ≥3 新 tests 全绿 + 清理两份设计转录稿验收通过 + 欧阳锋审查 |
| 3 | `kdo validate --v15 --watch` | 本文件 Task 3 | 修改卡自动重检 + 防抖正常 + 无回归 + 欧阳锋审查 |

---

## 相关

- [[70_product/tasks/validate-v15-upgrade-plan.md]] — scaffold 的前置工单
- [[70_product/tasks/quality-gate-automation-v15.md]] — validate v15 本身
- [[70_product/tasks/laowantong-next-tasks.md]] — 老顽童队列（scaffold 的消费者、设计域编译器）
- [[70_product/tasks/kdo-infrastructure-backlog-proposal.md]] — 原始 backlog
