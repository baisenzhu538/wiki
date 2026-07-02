# -*- coding: utf-8 -*-
"""Re-test customer-segmentation and performance-monitor after v1.1 prompt fixes."""

import os
import re
import time
from pathlib import Path
from datetime import datetime
import requests

VAULT = Path(__file__).resolve().parent.parent.parent
TRACES_DIR = VAULT / "60_feedback" / "agent-traces" / "2026-07-02"

BASE_URL = os.environ.get("ANTHROPIC_BASE_URL", "https://api.deepseek.com/anthropic").rstrip("/")
AUTH_TOKEN = os.environ.get("ANTHROPIC_AUTH_TOKEN", "")
MODEL = os.environ.get("ANTHROPIC_MODEL", "deepseek-v4-pro")


def extract_system_prompt(md_text: str) -> str:
    m = re.search(r"##\s+System Prompt 模板\s*\n+(```[\s\S]*?\n```)", md_text, re.IGNORECASE)
    if not m:
        raise ValueError("System Prompt section not found")
    code = m.group(1)
    code = re.sub(r"^```\w*\n", "", code)
    code = re.sub(r"\n```\n?$", "", code)
    return code.strip()


def call_model(system: str, user: str) -> dict:
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": MODEL,
        "max_tokens": 4096,
        "system": system,
        "messages": [{"role": "user", "content": user}],
    }
    resp = requests.post(f"{BASE_URL}/v1/messages", headers=headers, json=payload, timeout=300)
    resp.raise_for_status()
    data = resp.json()
    text_parts = [b.get("text", "") for b in data.get("content", []) if b.get("type") == "text"]
    return {
        "response_text": "\n".join(text_parts),
        "model": data.get("model", MODEL),
        "usage": data.get("usage", {}),
    }


RETESTS = [
    {
        "card": "tool-agent-spec-yitang-customer-segmentation",
        "scenario": "医药零售 B2B 线索分级 v1.1",
        "input": """请对以下 5 条脱敏线索做 S/A/B/C 分级，并给出跟进策略：
1. 某省会城市连锁药店集团采购总监，年营业额约 3 亿，主动在官网提交试用申请，关注智能药柜医保结算功能。
2. 地级市单体药店老板，月营业额约 30 万，从公众号文章扫码进群，询问"你们这个柜子和友商有什么区别"。
3. 某区医保局信息科负责人，公开招标文件中出现智能药柜关键词，但联系人未回复私信。
4. 医药流通商销售代表，手上有 200+ 家基层诊所资源，想谈区域代理，目前只发了名片。
5. 个人诊所医生，门诊量每天约 30 人，在朋友圈看到产品视频，私信问价格。""",
    },
    {
        "card": "tool-agent-spec-yitang-sales-performance-monitor",
        "scenario": "智能药柜月度 Pipeline 复盘 v1.1",
        "input": """月度目标：签约 10 家连锁药店，合同额约 200 万。
当前 Pipeline（脱敏）：
1. A 连锁 80 店，POC 已通过，待报价，预计 50 万，阶段 付款
2. B 连锁 30 店，方案已发，待反馈，预计 30 万，阶段 购买
3. C 单体药店 1 家，试用中，预计 5 万，阶段 接触
4. D 连锁 150 店，初访完成，待演示，预计 80 万，阶段 接触
5. E 区域代理，资质审核中，预计 40 万，阶段 接触
6-15. 若干小线索，合计约 20 万，多数在接触阶段
请做 Gap 分析、重点客户推荐、下周策略。""",
    },
]


def main():
    for item in RETESTS:
        card_path = VAULT / "30_wiki" / "tools" / f"{item['card']}.md"
        system_prompt = extract_system_prompt(card_path.read_text(encoding="utf-8"))
        print(f"Running {item['card']} v1.1 ...")
        out = call_model(system_prompt, item["input"])
        trace_file = TRACES_DIR / f"{item['card']}__{item['scenario'].replace(' ', '_').replace('/', '_')}.md"
        trace_content = f"""# Trace: {item['card']} / {item['scenario']}

- **Model**: {out['model']}
- **Timestamp**: {datetime.now().isoformat()}
- **Usage**: {out['usage']}

## Input

{item['input']}

## Agent Output

{out['response_text']}
"""
        trace_file.write_text(trace_content, encoding="utf-8")
        print(f"  saved {trace_file} ({len(out['response_text'])} chars)")
        time.sleep(1)


if __name__ == "__main__":
    main()
