#!/usr/bin/env python3
"""channel_health.py — 通道健康预检（#656，F-073 落地：kimi 403 周额度 / codex 余额尽两墙连撞的工具化根治）。

探针形态（09-06 12:00 前后实弹验证，全部实测非推断）：
  claude → HTTP POST {base}/v1/messages  max_tokens=1   正key 200/1.2s，坏key 401/0.1s
  codex  → HTTP POST relay/v1/responses  max_output_tokens=16   200/0.9s（relay 不校验调用方 key）
  kimi   → CLI kimi.exe -p 最小prompt    OAuth 由 CLI 自刷（HTTP 探针会拿过期 token 撞 401 假阴性，
                                          实测 credentials 里 token 08:21 已过期→401）
  hermes → 无独立探针：上游=kimi（~/.hermes/config.yaml: provider kimi-coding），
            按 kimi 探测结果判定，不重复撞同一堵墙。

分类：2xx=健康；401/402/403/429=上游级不健康（额度/认证，同上游通道连坐）；5xx/不可达/超时=工具级不健康。
"""
import json
import re
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path

WIKI = Path(__file__).resolve().parents[2]
HEALTH_LOG = WIKI / "logs" / "channel-health.log"

# 工具 → 真实上游（认知表 90_control/channel-model-map.md 的机器可读面）。
# hermes 与 kimi 同上游（api.kimi.com）——kimi 403 周额度时 hermes 同死，fallback 必须按上游去重。
TOOL_UPSTREAM = {
    "claude": "zhipu-glm",
    "codex": "deepseek",
    "kimi": "kimi",
    "hermes": "kimi",
}

CLAUDE_SETTINGS = Path.home() / ".claude" / "settings.json"
CODEX_AUTH = Path.home() / ".codex" / "auth.json"
KIMI_EXE = r"C:\Users\Administrator\.kimi-code\bin\kimi.exe"
# codex 通道实际端点：.codex/config.toml [model_providers.relay] base_url + model，与 config 漂移时以 config 为准
RELAY_URL = "http://127.0.0.1:4444/v1/responses"
RELAY_MODEL = "deepseek-v4-pro"

HTTP_TIMEOUT = 12
CLI_TIMEOUT = 45

# 响应体里出现即判「余额/配额类死亡」（防上游用 200 包错误体）
DEAD_KEYWORDS = (
    "insufficient balance", "quota", "usage limit", "exceeded",
    "余额不足", "额度", "配额",
)


class ProbeResult:
    def __init__(self, tool, healthy, scope, reason, latency=0.0, detail=""):
        self.tool = tool
        self.healthy = healthy
        self.scope = scope      # "upstream"=上游级（额度/认证，同上游连坐）| "tool"=工具级（本机路径）
        self.reason = reason
        self.latency = latency
        self.detail = detail

    def __repr__(self):
        flag = "OK " if self.healthy else "DEAD"
        return f"[{flag}] {self.tool}({TOOL_UPSTREAM.get(self.tool,'?')}) {self.reason} {self.latency:.1f}s"

    def to_json(self):
        return {
            "tool": self.tool, "upstream": TOOL_UPSTREAM.get(self.tool),
            "healthy": self.healthy, "scope": self.scope, "reason": self.reason,
            "latency_s": round(self.latency, 1), "detail": self.detail[:200],
        }


def classify_status(status, body=""):
    """HTTP 状态码 → (healthy, scope, reason)。纯函数，测试直接覆盖。"""
    low = (body or "").lower()
    if status == 200:
        for kw in DEAD_KEYWORDS:
            if kw in low:
                return False, "upstream", f"200 但响应体报额度/余额类错误（含「{kw}」）"
        return True, "upstream", "200 OK"
    if status == 401:
        return False, "upstream", "401 认证失败（key 无效/过期）"
    if status == 402:
        return False, "upstream", "402 余额不足"
    if status == 403:
        return False, "upstream", "403 拒绝（额度墙/权限）"
    if status == 429:
        return False, "upstream", "429 限流/配额"
    if 500 <= status < 600:
        return False, "tool", f"{status} 上游服务端错误"
    return False, "tool", f"{status} 非预期状态"


def _load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _post_json(url, key, body, timeout):
    t0 = time.time()
    req = urllib.request.Request(
        url, data=json.dumps(body).encode(),
        headers={"Authorization": "Bearer " + key, "content-type": "application/json",
                 "anthropic-version": "2023-06-01"},
    )
    try:
        r = urllib.request.urlopen(req, timeout=timeout)
        body = r.read(2000).decode("utf-8", "replace")
        healthy, scope, reason = classify_status(r.status, body)
        return ProbeResult("", healthy, scope, reason, time.time() - t0, body[:200])
    except urllib.error.HTTPError as e:
        body = e.read(2000).decode("utf-8", "replace")
        healthy, scope, reason = classify_status(e.code, body)
        return ProbeResult("", healthy, scope, reason, time.time() - t0, body[:200])
    except Exception as e:  # URLError / timeout / 连接拒绝
        return ProbeResult("", False, "tool", f"不可达：{type(e).__name__}: {e}", time.time() - t0)


def probe_claude(timeout=HTTP_TIMEOUT, key_override=None):
    """claude.exe 通道 = 智谱 GLM（settings.json ANTHROPIC_BASE_URL/AUTH_TOKEN/MODEL）。"""
    env = _load_json(CLAUDE_SETTINGS).get("env", {})
    key = key_override or env.get("ANTHROPIC_AUTH_TOKEN", "")
    url = env.get("ANTHROPIC_BASE_URL", "").rstrip("/") + "/v1/messages"
    body = {"model": env.get("ANTHROPIC_MODEL", "glm-5.3-flash"), "max_tokens": 1,
            "messages": [{"role": "user", "content": "hi"}]}
    r = _post_json(url, key, body, timeout)
    r.tool = "claude"
    return r


def probe_codex(timeout=HTTP_TIMEOUT, key_override=None):
    """codex.exe 通道 = 本地 relay:4444 → api.deepseek.com（relay 不校验调用方 key，
    key_override 只能模拟「上游 key 死」——模拟本通道探针故障请用本地 stub URL）。"""
    key = key_override
    if key is None:
        key = _load_json(CODEX_AUTH).get("OPENAI_API_KEY", "")
    body = {"model": RELAY_MODEL, "input": "hi", "max_output_tokens": 16}
    r = _post_json(RELAY_URL, key, body, timeout)
    r.tool = "codex"
    if r.healthy:
        return r
    # relay 挂了 → 上游 deepseek 未必死：上游级降级为工具级，避免连坐误杀
    if r.scope == "upstream":
        r.scope = "tool"
        r.reason += "（经 relay，降级为工具级）"
    return r


def probe_kimi(timeout=CLI_TIMEOUT, key_override=None):
    """kimi.exe 通道 = kimi-for-coding（OAuth 文件态，CLI 自刷 token）——只能 CLI 级探测。"""
    t0 = time.time()
    try:
        r = subprocess.run(
            [KIMI_EXE, "-m", "kimi-code/k3", "-p", "只回复数字1"],
            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return ProbeResult("kimi", False, "tool", f"CLI 探针超时（>{timeout}s）", time.time() - t0)
    except Exception as e:
        return ProbeResult("kimi", False, "tool", f"CLI 起不来：{type(e).__name__}: {e}", time.time() - t0)
    out = ((r.stderr or "") + "\n" + (r.stdout or "")).strip()
    flat = re.sub(r"\s+", " ", out)[:160]
    if r.returncode == 0:
        return ProbeResult("kimi", True, "upstream", "CLI 探针 exit 0", time.time() - t0, out[:200])
    scope = "upstream" if re.search(r"40[123]|429|quota|usage limit|额度|余额", out, re.I) else "tool"
    return ProbeResult("kimi", False, scope, f"CLI exit {r.returncode}: {flat}", time.time() - t0, out[:200])


PROBERS = {"claude": probe_claude, "codex": probe_codex, "kimi": probe_kimi}


def probe_channel(tool, timeout=None, key_override=None, prober=None, force_dead=False):
    """单通道探测。force_dead=True（测试钩）直接判死不发包；prober=注入探针（测试）。"""
    if force_dead:
        return ProbeResult(tool, False, "tool", "force_dead（模拟死通道）")
    if prober is not None:
        return prober(tool)
    fn = PROBERS.get(tool)
    if fn is None:
        return ProbeResult(tool, False, "tool", "无独立探针（上游随其他通道判定）")
    kw = {}
    if timeout is not None:
        kw["timeout"] = timeout
    if key_override is not None and tool in ("claude", "codex"):
        kw["key_override"] = key_override
    return fn(**kw)


def probe_chain(tools, timeout=None, key_override=None, prober=None, force_dead=()):
    """按序探测 fallback 链，同上游去重：上游级死亡的墙不撞第二次。"""
    results, upstream_verdict = [], {}
    for tool in tools:
        up = TOOL_UPSTREAM.get(tool)
        if up in upstream_verdict:
            prev = upstream_verdict[up]
            results.append(ProbeResult(
                tool, prev.healthy, prev.scope,
                f"同上游 {up} 已判定（{prev.reason}），未重复探测", 0.0))
            continue
        r = probe_channel(tool, timeout=timeout, key_override=key_override,
                          prober=prober, force_dead=tool in force_dead)
        results.append(r)
        upstream_verdict[up] = r
    return results


def first_healthy(results):
    for r in results:
        if r.healthy:
            return r
    return None


def log_results(results, decision):
    """探测留痕：logs/channel-health.log 一行 JSON。返回人读摘要行。"""
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    rec = {"ts": ts, "decision": decision, "results": [r.to_json() for r in results]}
    try:
        HEALTH_LOG.parent.mkdir(parents=True, exist_ok=True)
        with open(HEALTH_LOG, "a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    except OSError:
        pass
    return " | ".join(
        f"{r.tool}={'OK' if r.healthy else 'DEAD(' + r.reason + ')'}" for r in results)
