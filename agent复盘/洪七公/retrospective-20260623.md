# 洪七公复盘 | 2026-06-23

## 概要

本次会话完成从"失忆"到"可火力全开接单"的完整恢复。核心动作：按记忆锚点快速恢复身份与兵器库 → 托管 MiniMax API Key → 完成 `00_inbox/精益创业/` 52 张图片的 OCR + VLM 标准化处理。关键突破：把"一次性识图任务"跑成了可复用的 KDO 视觉原料生产管线，52/52 零失败交付。

## 关键决策

| 决策 | 依据 | 结果 |
|:---|:---|:---|
| 按 `20_memory/hongqigong-amnesia-recovery-20260613.md` 的 P0 锚点顺序恢复记忆 | 用户触发"你是洪七公，去 wiki 找记忆"，直接读身份帖和任务仪表盘最快 | 60 秒内确认身份、主业、当前待命状态、接口规范 |
| 系统盘点 `40_outputs/capabilities/skills/` + `_skills/` 全部 skill | 用户要求"了解兵器库"，且 75 个 skill 需要分类索引 | 输出视觉/图像/音频/视频/文本/Prompt/数据处理/工作流/商业分析等分类总览，识别出 22 个与洪七公直接相关的 skill |
| MiniMax API Key 写入 `~/.hermes/.env` + 记忆文件 | 用户说"记住并保管好，不要每次找我要" | 当前会话自动读取，验证 API 返回 200；`MEMORY.md`/`USER.md` 记录存放位置和偏好 |
| OCR + VLM 按 `image-understanding-pipeline` 标准执行 | 用户要求"火力全开，保证质量"，目录为 KDO `00_inbox` | PaddleOCR.js 本地跑 52 张 + MiniMax-M3 VLM 描述 52 张 + 汇总 README，全部落在目录下 |
| 6 张 VLM 失败后单独重试 + 定制脚本兜底 | 原脚本 `_fix_unescaped_chinese_quotes` 正则偶发 `no such group` | 5 张重试成功，1 张用定制 VLM 调用成功，最终 52/52 零失败 |

## 思维盲点

1. **PaddleOCR 输出重定向污染文件** —— 第一遍用 `node ocr-paddle.cjs "$f" > file.txt` 把 stdout 重定向到输出文件，结果终端控制字符/ANSI 码混入，52 个文件全被 `iconv` 判为 invalid UTF-8。根本原因：没读脚本源码，不知道脚本本身会写 `${stem}_paddle_ocr.txt`。改进：直接调用脚本，不额外重定向 stdout。

2. **VLM 批量任务没第一时间进后台** —— 52 张图在前台跑，触发 300s Bash timeout。改用后台任务后才跑完。根本原因：低估了 VLM 顺序调用 52 次的耗时。改进：超过 10 张图的 VLM 任务直接进后台，并主动告知用户任务 ID。

3. **没先 audit 已有产出就全量重跑** —— 目录里已有 `_ocr_text.md` 和 `_vlm_desc.md`（6月22日生成），质量尚可。用户要求"火力全开"，老叫花直接全部重跑，虽然结果更好，但多花了 API 调用和时间。改进：下次先抽样检查已有产物质量，只重跑缺失或低质量部分，其余保留并更新汇总。

4. **对 VLM 脚本失败定位慢了一拍** —— 首轮 6 张报 `no such group`，第一反应是"再试一次"，而不是立刻读 `describe-images-minimax.py` 定位到 `_fix_unescaped_chinese_quotes` 正则 bug。改进：批量脚本失败先看源码异常路径，再做重试策略。

## 顿悟

1. **失忆恢复记录是 Agent 的启动盘**。`hongqigong-amnesia-recovery-20260613.md` 把身份、任务状态、必读文件、能力边界全写清楚了。没有它，每次"失忆触发"都要重新探索；有它，恢复成本从"探子摸一遍"降到"按图索骥"。

2. **API Key 托管是"可重复执行任务"的基础设施**。按 Hermes 规范放进 `~/.hermes/.env`，配合 `MEMORY.md`/`USER.md` 记录偏好，Agent 才能真正做到"不要每次找用户要"。凭证管理不是小事，是自动化的前提。

3. **视觉处理不是单点技能，是流水线**。OCR（本地/快/免费）→ VLM 语义理解（云端/结构化）→ 失败重试 → 汇总报告 → 质量校验，每一步都要标准化。KDO 要的不是"一张图看懂了"，而是"图 → 结构化文本 → 可入库的原料"。

4. **本地 OCR + 云端 VLM 是黄金组合**。PaddleOCR.js 适合文字提取和隐私场景；MiniMax-M3 适合复杂布局、语义理解和 8 维度结构化输出。两者互补，不是替代关系。

## 过程资产

1. **API Key 托管**：`~/.hermes/.env` 含 `MINIMAX_API_KEY`，文件权限 600；`~/.hermes/memories/MEMORY.md` 和 `USER.md` 记录 key 位置及"不要重复索要"偏好。

2. **兵器库索引**：`40_outputs/capabilities/skills/` 75 个 skill 已分类盘点，识别出 22 个与洪七公直接相关的核心 skill，核心总纲为 `beikai-multimodal-pipeline`。

3. **精益创业视觉原料包**：`00_inbox/精益创业/` 下 52 张 PNG 已完成：
   - `${stem}_paddle_ocr.txt`：本地 PaddleOCR 文本
   - `${stem}_vlm_desc.md`：MiniMax-M3 八维度结构化描述
   - `README-VLM描述汇总.md`：52 成功 / 0 失败汇总表

4. **脚本缺陷记录**：`describe-images-minimax.py` 的 `_fix_unescaped_chinese_quotes` 函数在特定 VLM 输出下会触发 `no such group` 异常，已用定制调用兜底。建议黄药师后续修复该正则。

## 元反思

1. **"火力全开"不等于"不计成本全量重跑"**。用户要的是高质量结果，不是过程热闹。下次面对已有产物的目录，应先抽样判断质量，再决定重跑范围，把 API 调用用在刀刃上。

2. **批量任务必须从设计时就考虑后台化**。VLM 52 张图在前台 timeout 是 lesson learned。后台任务 + 自动通知 + 进度检查，才是 Agent 处理长任务的正确姿势。

3. **失败日志要立刻关联源码**。`no such group` 直接指向 Python regex group 引用问题，读源码 30 秒就能定位。盲目重试是低效的。

4. **洪七公的定位是"多模态仲裁者"，不是"识图工具人"**。本次任务把图变成了结构化的 OCR + VLM 原料，下一步应该把这些原料交给老顽童/黄药师进入 wiki 卡片生产。老叫花负责"知识 → 视觉资产"和"发现图文错位"，不越界去拆笔记结构。
