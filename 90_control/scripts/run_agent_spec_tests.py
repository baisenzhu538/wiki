# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Run Wave 1 real-model tests for OPC sales agent-spec cards."""

import os
import re
import json
import time
from pathlib import Path
from datetime import datetime
import requests

VAULT = Path(__file__).resolve().parent.parent.parent
TRACES_DIR = VAULT / "60_feedback" / "agent-traces" / "2026-07-02"
TRACES_DIR.mkdir(parents=True, exist_ok=True)

BASE_URL = os.environ.get("ANTHROPIC_BASE_URL", "https://api.deepseek.com/anthropic").rstrip("/")
AUTH_TOKEN = os.environ.get("ANTHROPIC_AUTH_TOKEN", "")
MODEL = os.environ.get("ANTHROPIC_MODEL", "deepseek-v4-pro")

AGENT_FILES = {
    "tool-agent-spec-yitang-customer-segmentation": VAULT / "30_wiki" / "tools" / "tool-agent-spec-yitang-customer-segmentation.md",
    "tool-agent-spec-yitang-value-proposition": VAULT / "30_wiki" / "tools" / "tool-agent-spec-yitang-value-proposition.md",
    "tool-agent-spec-yitang-sales-process-tracker": VAULT / "30_wiki" / "tools" / "tool-agent-spec-yitang-sales-process-tracker.md",
    "tool-agent-spec-yitang-sales-performance-monitor": VAULT / "30_wiki" / "tools" / "tool-agent-spec-yitang-sales-performance-monitor.md",
    "tool-agent-spec-yitang-opening-3min": VAULT / "30_wiki" / "tools" / "tool-agent-spec-yitang-opening-3min.md",
    "tool-agent-spec-yitang-objection-handler": VAULT / "30_wiki" / "tools" / "tool-agent-spec-yitang-objection-handler.md",
    "tool-agent-spec-yitang-self-motivation": VAULT / "30_wiki" / "tools" / "tool-agent-spec-yitang-self-motivation.md",
}

SCENARIOS = {
    "tool-agent-spec-yitang-customer-segmentation": [
        {
            "name": "医药零售 B2B 线索分级",
            "domain": "医药零售 B2B",
            "input": '''请对以下 5 条脱敏线索做 S/A/B/C 分级，并给出跟进策略：
1. 某省会城市连锁药店集团采购总监，年营业额约 3 亿，主动在官网提交试用申请，关注智能药柜医保结算功能。
2. 地级市单体药店老板，月营业额约 30 万，从公众号文章扫码进群，询问"你们这个柜子和友商有什么区别"。
3. 某区医保局信息科负责人，公开招标文件中出现智能药柜关键词，但联系人未回复私信。
4. 医药流通商销售代表，手上有 200+ 家基层诊所资源，想谈区域代理，目前只发了名片。
5. 个人诊所医生，门诊量每天约 30 人，在朋友圈看到产品视频，私信问价格。''',
        },
        {
            "name": "SaaS 线索分级",
            "domain": "SaaS / 企业服务",
            "input": '''请对以下 5 条脱敏线索做 S/A/B/C 分级，并给出跟进策略：
1. 某连锁剧本杀品牌运营总监，全国 80+ 门店，在行业峰会上听完 demo 后主动加微信，要求下周约产品演示。
2. 独立桌游吧老板，单店 6 个房间，从知乎文章点进官网，只注册了试用账号但 3 天未登录。
3. 某商场招商经理，管理 20+ 娱乐业态商户，询问是否可以做"商场级解决方案"。
4. 剧本杀 DM 个人博主，粉丝 5 万，想申请免费试用做测评，未说明是否付费意愿。
5. 同行 SaaS 公司销售，伪装成客户索要报价单。''',
        },
    ],
    "tool-agent-spec-yitang-value-proposition": [
        {
            "name": "智能药柜卖给连锁药店",
            "domain": "医药零售 B2B",
            "input": '''产品：智能药柜，支持 24 小时自助购药、医保扫码结算、远程药师审方、库存自动预警。
客户画像：某省会城市连锁药店集团采购总监，年营业额约 3 亿，门店 150 家，目前在试点夜间售药，但人工夜班成本高、医保合规风险大。
当前阶段：接触后首次方案沟通。
目标：产出针对该客户的 Top3 差异化卖点 + 微信/电话/邮件/PPT 四版话术。''',
        },
        {
            "name": "剧本杀 SaaS 卖给桌游吧",
            "domain": "SaaS / 企业服务",
            "input": '''产品：剧本杀 SaaS，支持拼组、房间管理、剧本库、会员体系、数据报表。
客户画像：某连锁桌游品牌运营经理，全国 12 家门店，目前用微信群拼组，店长手动排房，客户流失严重。
当前阶段：购买阶段，客户已试用 7 天。
目标：产出针对该客户的 Top3 差异化卖点 + 微信/电话/邮件/PPT 四版话术。''',
        },
    ],
    "tool-agent-spec-yitang-sales-process-tracker": [
        {
            "name": "智能药柜多轮推进",
            "domain": "医药零售 B2B",
            "input": '''销售：张经理（智能药柜厂商）
客户：李总（连锁药店采购总监）

对话记录：
张经理：李总，上次您提到夜间售药成本高，我们这套智能药柜可以把夜班人工降到零。
李总：降到零不太可能吧，顾客有问题找谁？
张经理：我们有远程药师审方和 7×24 客服中心，合规也有我们法务团队兜底。
李总：法务团队兜底？这个话可不能随便说。
张经理：我的意思是系统流程符合当前监管框架，具体落地会配合您法务再确认。
李总：嗯，那把方案发我，我下周给老板看。
张经理：好的，我周四前发您一版，您看周三下午我们先过一遍？
李总：周三我没空，周四上午吧。

请判断阶段、卡点、下一步建议。''',
        },
        {
            "name": "剧本杀 SaaS 多轮推进",
            "domain": "SaaS / 企业服务",
            "input": '''销售：小王（剧本杀 SaaS 销售）
客户：陈店长（桌游吧老板，单店 6 房）

对话记录：
小王：陈店长，试用这一周拼组成功率有变化吗？
陈店长：确实省事，但会员功能感觉不如我现在的微信表格灵活。
小王：会员功能您可以自定义字段，我安排客户成功帮您配一次。
陈店长：那要额外收费吗？
小王：首年免费，后续按模块收。
陈店长：我先看看，最近店里忙。
小王：我理解，那下周二我带您过一遍报表，10 分钟就够。
陈店长：下周二可以。

请判断阶段、卡点、下一步建议。''',
        },
    ],
    "tool-agent-spec-yitang-sales-performance-monitor": [
        {
            "name": "智能药柜月度 Pipeline 复盘",
            "domain": "医药零售 B2B",
            "input": '''月度目标：签约 10 家连锁药店，合同额约 200 万。
当前 Pipeline（脱敏）：
1. A 连锁 80 店，POC 已通过，待报价，预计 50 万，阶段 付款
2. B 连锁 30 店，方案已发，待反馈，预计 30 万，阶段 购买
3. C 单体药店 1 家，试用中，预计 5 万，阶段 接触
4. D 连锁 150 店，初访完成，待演示，预计 80 万，阶段 接触
5. E 区域代理，资质审核中，预计 40 万，阶段 接触
6-15. 若干小线索，合计约 20 万，多数在接触阶段
请做 Gap 分析、重点客户推荐、下周策略。''',
        },
        {
            "name": "美容院连锁月度 Pipeline 复盘",
            "domain": "门店零售 / 美业",
            "input": '''月度目标：签约 8 家美容院，客单价 3 万，合计 24 万。
当前 Pipeline（脱敏）：
1. 美丽佳人连锁 5 店，已体验产品，待方案，预计 15 万，阶段 购买
2. 小雅工作室，老板犹豫价格，预计 3 万，阶段 购买
3.  premium 医美中心，决策链复杂，预计 9 万，阶段 接触
4. 社区小店 3 家，只咨询未试用，预计各 1 万，阶段 接触
5. 老客户转介绍 2 家，口头有意向，未见面，阶段 接触
请做 Gap 分析、重点客户推荐、下周策略。''',
        },
    ],
    "tool-agent-spec-yitang-opening-3min": [
        {
            "name": "首条消息给连锁药店采购总监",
            "domain": "医药零售 B2B",
            "input": '''模式：A（首条消息草稿）
场景：通过行业峰会拿到李总微信，对方已通过好友但尚未说话。
产品：智能药柜。
请输出 50-80 字首条消息。''',
        },
        {
            "name": "首通电话攻略给 SaaS 潜在客户",
            "domain": "SaaS / 企业服务",
            "input": '''模式：B（首通电话攻略）
场景：剧本杀 SaaS 销售预约了陈店长周三 15:00 电话，对方单店 6 房，目前用微信群拼组。
请输出完整首通电话攻略。''',
        },
    ],
    "tool-agent-spec-yitang-objection-handler": [
        {
            "name": "智能药柜价格异议",
            "domain": "医药零售 B2B",
            "input": '''产品：智能药柜。
客户：连锁药店采购总监李总。
异议："你们一台柜子 8 万，比我们预算高 60%，我先看看别家。"''',
        },
        {
            "name": "剧本杀 SaaS 时机异议",
            "domain": "SaaS / 企业服务",
            "input": '''产品：剧本杀 SaaS。
客户：桌游吧老板陈店长。
异议："最近淡季，等过完年再考虑系统吧。''',
        },
    ],
    "tool-agent-spec-yitang-self-motivation": [
        {
            "name": "周目标落后 + 倦怠",
            "domain": "OPC 创始人",
            "input": '''本周目标：完成 10 个新客户触达、跟进 5 个 A 级客户、发 3 份方案。
当前进度：新客户触达 3/10，A 级客户跟进 1/5，方案 0/3。
状态自述："最近一直被拒绝，有点不想打开 CRM，明知道该做但提不起劲。"''',
        },
        {
            "name": "月度目标超前 + 防松懈",
            "domain": "OPC 创始人",
            "input": '''本月目标：签约 8 家客户，回款 20 万。
当前进度：已签约 7 家，回款 18 万，距离月底还有 10 天。
状态自述："感觉这个月差不多能完成，想歇两天，但又怕后面掉链子。''',
        },
    ],
}


def extract_system_prompt(md_text: str) -> str:
    """Extract the first ``` code block under '## System Prompt 模板'."""
    m = re.search(r"##\s+System Prompt 模板\s*\n+(```[\s\S]*?\n```)", md_text, re.IGNORECASE)
    if not m:
        raise ValueError("System Prompt section not found")
    code = m.group(1)
    # strip ```markdown or ```
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
    text_parts = []
    for block in data.get("content", []):
        if block.get("type") == "text":
            text_parts.append(block.get("text", ""))
    return {
        "response_text": "\n".join(text_parts),
        "model": data.get("model", MODEL),
        "usage": data.get("usage", {}),
    }


def main():
    results = {}
    for agent_id, agent_path in AGENT_FILES.items():
        md_text = agent_path.read_text(encoding="utf-8")
        system_prompt = extract_system_prompt(md_text)
        results[agent_id] = []
        for scenario in SCENARIOS.get(agent_id, []):
            print(f"Running {agent_id} / {scenario['name']} ...")
            try:
                out = call_model(system_prompt, scenario["input"])
            except Exception as e:
                out = {"response_text": f"ERROR: {e}", "model": MODEL, "usage": {}}
            trace_file = TRACES_DIR / f"{agent_id}__{scenario['name'].replace(' ', '_').replace('/', '_')}.md"
            trace_content = f"""# Trace: {agent_id} / {scenario['name']}

- **Domain**: {scenario['domain']}
- **Model**: {out['model']}
- **Timestamp**: {datetime.now().isoformat()}
- **Usage**: {json.dumps(out.get('usage') or {}, ensure_ascii=False)}

## Input

{scenario['input']}

## Agent Output

{out['response_text']}
"""
            trace_file.write_text(trace_content, encoding="utf-8")
            results[agent_id].append({
                "scenario": scenario["name"],
                "domain": scenario["domain"],
                "trace": str(trace_file.relative_to(VAULT)),
                "status": "ok" if not out["response_text"].startswith("ERROR") else "error",
            })
            time.sleep(1)

    summary_file = TRACES_DIR / "_summary.json"
    summary_file.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nDone. Traces saved to {TRACES_DIR}")
    for agent_id, runs in results.items():
        ok = sum(1 for r in runs if r["status"] == "ok")
        print(f"  {agent_id}: {ok}/{len(runs)} ok")


if __name__ == "__main__":
    main()
