---
id: 2026-09-04-duanwangye-glm-migration
title: "段王爷模型迁移记录：DeepSeek → 智谱 GLM（2026-09-04）"
type: change-record
status: done
author: 小昭
created_at: 2026-09-04
updated_at: 2026-09-04
confidence: 0.95
domain:
  - kdo
  - infrastructure
  - hermes
  - model-routing
source_refs:
  - "profiles/duanwangye/config.yaml (AppData\\Local\\hermes)"
  - "profiles/duanwangye/.env (AppData\\Local\\hermes)"
  - "profiles/duanwangye/auth.json (AppData\\Local\\hermes)"
  - "logs/headless-ouyangfeng-20260903-021100.log"
  - "70_product/tasks/role-model-routing.md"
related:
  - [[role-model-routing]]
  - [[incident-impact-assessment-hermes-wiki-2026-06-29]]
  - [[codex-kimi-setup-20260606]]
---

# 段王爷模型迁移记录：DeepSeek → 智谱 GLM（2026-09-04）

> 触发链：小昭盘点「飞书 Hermes 各角色用什么模型」→ 发现段王爷与已迁移 agent 不一致 → 老板指令「把他和其他 Agent 都用同样 API」→ 本记录 = 执行 + 验证全案。

## 一、根因：8/30 GLM 迁移批次漏了段王爷

2026-08-30 ~ 09-01 有一批「DeepSeek → 智谱 GLM」迁移（主模型切 `glm-5.3-flash` / provider `zai`，.env 补 GLM/ANTHROPIC 兼容端点），覆盖了欧阳锋/黄药师/老顽童/王语嫣这条生产咨询主线，**段王爷（发布）与洪七公（beikai）不在批次内**。

迁移前段王爷三层配置全部停留在旧态：

| 配置层 | 段王爷旧态 | 已迁移者（如王语嫣） |
|:--|:--|:--|
| `.env` | 7/19 版：仅 DEEPSEEK_API_KEY，无 GLM key | 8/30 19:47 版：补 `GLM_API_KEY` + `ANTHROPIC_*`（智谱兼容端点） |
| `auth.json` credential pool | 仅 deepseek | deepseek + zai(GLM) + anthropic |
| `config.yaml` | 8/18 版：`deepseek-v4-flash` / deepseek / fallback 空 | 8/30-9/1：`glm-5.3-flash` / zai + deepseek fallback |

**直接后果**：段王爷 auth.json 里 DeepSeek 共用 key 于 2026-09-04 15:53 被打上 `402 Insufficient Balance`——他既无 GLM key 兜底、fallback 又是空 → 派发布任务会直接模型调用失败（"半瘫"）。15:53 飞书消息「妙计继续」即因 402 触发 transient failure，消息被持久化待重试。

## 二、全厂模型现状（2026-09-04 实测 · Windows 侧 config.yaml 为准）

| Hermes Agent | Profile | 主模型 | Provider | Fallback | config 最后修改 |
|:--|:--|:--|:--|:--|:--|
| **段王爷** | duanwangye | **glm-5.3-flash** | zai（智谱） | deepseek-v4-pro | **2026-09-04（本次迁移）** |
| 王语嫣 | wangyuyan | glm-5.3-flash | zai（智谱） | deepseek-v4-pro | 2026-09-01 23:37 |
| 老顽童 | laowantong | glm-5.3-flash | zai（智谱） | deepseek-v4-flash | ~8/30-31 |
| 老顽童-feishu | laowantong-feishu | glm-5.3-flash | zai（智谱） | deepseek-v4-flash | ~8/30 |
| 黄药师 | huangyaoshi | glm-5.3-flash | zai（智谱） | deepseek-v4-pro | 2026-08-31 00:39 |
| 欧阳锋 | ouyangfeng | glm-5.3-flash | zai（智谱） | deepseek-v4-flash | ~8/30 |
| 洪七公 | beikai | deepseek-v4-flash | deepseek | 无 | 未迁移（旧路径 .hermes） |

> ⚠️ 修正历史误读：欧阳锋 9/3 headless 日志「四角色共用 deepseek-v4-pro」为过时复述；真实 config 里王语嫣/黄药师/老顽童/欧阳锋主模型已是 glm-5.3-flash，段王爷当时为 flash。

## 三、改动明细（本次执行）

改动文件：`AppData\Local\hermes\profiles\duanwangye\` 下两个文件，逐字对齐王语嫣模板。

1. **`config.yaml`**（L1-11）：
   - `model.default`: `deepseek-v4-flash` → `glm-5.3-flash`
   - `model.provider`: `deepseek` → `zai`
   - `model.base_url`: `https://api.deepseek.com` → `https://open.bigmodel.cn/api/coding/paas/v4/`
   - `fallback_providers`: `[]` → `[{provider: deepseek, model: deepseek-v4-pro}]`
   - 补 `providers: {}`、`credential_pool_strategies: {}`（对齐新 schema 结构）
2. **`.env`**（追加 4 行）：
   - `GLM_API_KEY=9af804…`（与其他 agent 同一把智谱共用 key）
   - `GLM_BASE_URL=https://open.bigmodel.cn/api/coding/paas/v4`
   - `ANTHROPIC_API_KEY`（同智谱 key）+ `ANTHROPIC_BASE_URL=https://open.bigmodel.cn/api/anthropic`
   - **保留**：段王爷专属 `FEISHU_APP_ID/SECRET` + 原 DEEPSEEK key + KIMI_BASE_URL
3. **`auth.json`**：未手改（hermes 运行时自动从 .env 发现新凭据）。

## 四、重启与验证

⚠️ 关键坑：`hermes gateway restart` 无 profile 参数，默认重启「当前 profile」（huangyaoshi）。正确姿势：**`HERMES_HOME="C:\...\hermes\profiles\duanwangye" hermes gateway restart`** 精准定位，勿动 `active_profile`。

| 验证项 | 结果 |
|:--|:--|
| gateway 进程 | 旧 PID 6452 优雅退出 → 新 PID **15340** running |
| 飞书连接 | `gateway_state.json`: feishu **connected**（16:05:38）|
| 模型生效 | `hermes profile list`: duanwangye → **glm-5.3-flash** |
| 凭据就绪 | `hermes auth list`: **zai GLM_API_KEY ← 就绪**（anthropic 同步就绪）|
| 其他 agent | 全部原 PID 未动（huangyaoshi 20780 / wangyuyan 25780 等）|
| YAML 语法 | `yaml.safe_load` 校验通过 |

## 五、副作用与残留风险

1. **⚠️ 自动创建计划任务**：restart 非交互环境下走默认，创建 Windows 计划任务 `Hermes_Gateway_duanwangye`（开机自启，脚本在 `profiles\duanwangye\gateway-service\`）。段王爷由「手动 run」变为「计划任务托底」。如不需要：`hermes gateway uninstall`。
2. **DeepSeek fallback 暂失效**：共用 DeepSeek key 仍 402 欠费（exhausted，reset 倒计时 ~47min），fallback 到 deepseek 仍会失败直至 key 充值/自动重置。**主模型 GLM 不受影响。**
3. 15:53「妙计继续」消息已持久化，下次触发会带上下文重试（切 GLM 后即可成功）。

## 六、段王爷模型时间线

| 时间 | 模型 | 依据 |
|:--|:--|:--|
| ~2026-05 | Kimi（kimi-for-coding，订阅制） | role-model-routing.md（8 月建议稿仍记此规划） |
| 2026-06-29 | Kimi→DeepSeek 切换中配置出错 | incident-impact-assessment-hermes-wiki-2026-06-29 |
| 2026-08-02 | DeepSeek V4 Pro | session-archives/2026-08-02/duanwangye.md |
| 2026-08-09 | DeepSeek V4 Flash（临时档） | session-archives/2026-08-09/duanwangye.md |
| 2026-08-18 | DeepSeek V4 Flash（config 定格） | profiles/duanwangye/config.yaml mtime |
| **2026-09-04** | **GLM-5.3-Flash（zai）+ deepseek-v4-pro fallback（当前）** | 本次迁移记录 |
