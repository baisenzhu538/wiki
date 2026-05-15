# Hermes Gateway 排障记录（2026-05-16）

## 1. 飞书收到 Gateway 启动 Banner

**现象**：飞书对话里收到一条消息，内容是 Hermes Gateway 启动界面 + `[Lark] connected to wss://...`

**根因**：默认的 `hermes-gateway.service`（不带 profile）在系统重启后和 profile 服务抢同一个飞书 app_id。

**解决**：
```bash
systemctl --user stop hermes-gateway.service
systemctl --user disable hermes-gateway.service
```

> 只保留带 profile 的服务（`hermes-gateway-laowantong`、`hermes-gateway-beikai`、`hermes-gateway-duanwangye`）。

---

## 2. Lark SDK INFO 日志压不住

**现象**：journalctl 里每次启动都有 `[Lark] [INFO] connected to wss://...`，改了 `config.yaml` 仍然有。

**根因**：Lark SDK 的日志级别是在 `gateway/platforms/feishu.py` 中硬编码的 `lark.LogLevel.INFO`，不受 `config.yaml` 控制。

**解决**（两步）：

第一步——改 Hermes 自身日志：
```yaml
# ~/.hermes/config.yaml
logging:
  level: WARNING
```

第二步——改 Lark 硬编码（必须）：
```python
# ~/.hermes/hermes-agent/gateway/platforms/feishu.py 第 3502 行
# 原来：log_level=lark.LogLevel.INFO,
# 改成：log_level=lark.LogLevel.WARNING,
```

然后重启所有 gateway：
```bash
for p in laowantong beikai duanwangye; do
  systemctl --user restart hermes-gateway-$p.service
done
```

---

## 3. Claude Code DeepSeek → Kimi 切换挂掉

**根因**：两个配置错误
1. `ANTHROPIC_AUTH_TOKEN` → 应该是 `ANTHROPIC_API_KEY`（DeepSeek 用 AUTH_TOKEN，Kimi 用 API_KEY）
2. Base URL 缺尾斜杠：`https://api.kimi.com/coding` → `https://api.kimi.com/coding/`

**解决**：修改 `.bashrc` 中的环境变量，重新 source 后启动 Claude Code。
