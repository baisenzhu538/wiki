import os
import re
import yaml

BASE = "C:/Users/Administrator/Desktop/wiki/30_wiki"
RECOV = "C:/Users/Administrator/AppData/Local/Temp/ai-collab-recovery/ai-collaboration"

def parse_fm(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    if not text.startswith("---"):
        return {}, text
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.DOTALL)
    if not m:
        return {}, text
    fm = yaml.safe_load(m.group(1))
    return (fm if fm else {}), m.group(2)

def unique(seq):
    seen = []
    for x in seq:
        if x not in seen:
            seen.append(x)
    return seen

configs = {
    "framework-ai-video-production-aesthetics-first": {
        "dir": "frameworks",
        "prepend": "# AI产品开发·审美与体系的分工\n\n> 一句话：\"审美负责定义结果（这个东西应该长什么样），体系负责让结果重复发生（每次都能做成这样）。\" ——付则宇口述 L1786-1794\n\n> 本卡双面呈现：§A 复盘后的认知框架 + §B 真实过程的教训。\n\n---\n",
        "append": "\n---\n\n## 迭代日志\n\n- **2026-07-20 v1.0**：来自付则宇 AI 口播工具开发经验分享。",
        "signals": [
            {"signal": "技术方案先于审美标准", "lens": "开发团队先追 Hyper Friends / 数字人，做了一个月才发现方向错误", "follow_up": "先拆解 300+ 条视频建立审美标准，再选技术路线"},
            {"signal": "把复盘框架当执行顺序", "lens": "方法论呈现为线性四步法，第一步就卡住", "follow_up": "标注 §A 为复盘结构、§B 为真实过程，预期第一圈是乱的"},
            {"signal": "AI 产出视频\"总差一点\"", "lens": "组件化不彻底或审美标准未量化", "follow_up": "回到拆解层补组件库，人工验证\"愿不愿发出去\""},
        ]
    },
    "concept-ai-video-wanggan-componentization": {
        "dir": "concepts",
        "prepend": "# 网感组件化：9类视频分类 + 四要素可量化体系\n\n> 一句话：付则宇拆了 300+ 条口播视频后发现——网感不是玄学，是可以拆成四要素、九类模板的组件体系。\"剪映几百个动画，常用就小几十个。\"\n\n---\n",
        "append": "\n---\n\n## 迭代日志\n\n- **2026-07-20 v1.0**：来自付则宇 AI 口播工具开发经验分享。",
        "signals": [
            {"signal": "网感靠感觉说不清", "lens": "无法量化什么是好视频", "follow_up": "用 9 类分类 + 画面节奏/元素搭配清单建立组件库"},
            {"signal": "剪映功能太多不知用哪个", "lens": "几百个动画/音效选择过载", "follow_up": "固定 20 个模板池和 40 种常用音效"},
            {"signal": "用 AI 自动分析视频网感", "lens": "让 AI 描述动态画面，输出文字不准确", "follow_up": "人工拆 50 条建立第一手审美，AI 仅辅助归纳"},
        ]
    },
    "tool-ai-video-market-gap-assessment": {
        "dir": "tools",
        "prepend": "# AI工具市场信息差评估矩阵\n\n> 一句话：付则宇做AI口播工具前，先建立了审美标准（什么是80分网感视频），再用这个标准量现有工具——发现信息差巨大，才决定自建。三步决策链。\n\n---\n",
        "append": "\n---\n\n## 迭代日志\n\n- **2026-07-20 v1.0**：来自付则宇 AI 口播工具开发经验分享。",
        "signals": [
            {"signal": "市面已有类似工具", "lens": "看到已有产品就认为没机会", "follow_up": "去评论区查\"怎么买/多少钱\"频率，判断渗透率"},
            {"signal": "调研工具凭感觉", "lens": "没有量化标准对比", "follow_up": "先建审美标准清单，再逐项测工具能力边界"},
            {"signal": "80分 vs 100分选择犹豫", "lens": "追求完美效果导致进度慢", "follow_up": "判断零门槛+80分是否大于专业工具+100分"},
        ]
    },
    "tool-ai-video-cost-optimization": {
        "dir": "tools",
        "prepend": "# AI工具开发成本优化清单\n\n> 一句话：付则宇的两个实操技巧——企业认证多账号薅羊毛 + 中转商API按次付费——把API成本从正规渠道的\"几十元/条\"压到\"几元/条\"，差距10-50倍。\n\n---\n",
        "append": "\n---\n\n## 迭代日志\n\n- **2026-07-20 v1.0**：来自付则宇 AI 口播工具开发经验分享。",
        "signals": [
            {"signal": "API成本太高做不起", "lens": "正规API价格使测试期负担重", "follow_up": "用中转商按次付费，测试期压到 10-20 元/周"},
            {"signal": "一直用中转商不切正规API", "lens": "忽视稳定性与合规", "follow_up": "验证效果后切正规API，保留中转商兜底"},
            {"signal": "企业认证额度未充分利用", "lens": "只用一个账号付费", "follow_up": "多账号薅免费额度，建立额度跟踪表"},
        ]
    },
    "dk-ai-video-common-pitfalls": {
        "dir": "dark-knowledges",
        "prepend": "# AI视频工具开发五大失败模式\n\n> 一句话：付则宇踩过的坑——每个坑都是一个月的时间和几万块的教训。\n\n---\n",
        "insert_table": True,
        "append": "\n---\n\n## 迭代日志\n\n- **2026-07-20 v1.0**：来自付则宇 AI 口播工具开发经验分享。",
        "signals": [
            {"signal": "做了一个月发现方向错了", "lens": "技术先于审美", "follow_up": "先建网感组件库再开始技术调研"},
            {"signal": "AI 分析视频网感输出文字", "lens": "过度依赖 AI 建审美", "follow_up": "人工拆解 50 条形成组件清单"},
            {"signal": "调研结论是市面已有工具", "lens": "忽略市场信息差", "follow_up": "查评论区高频问价判断渗透率"},
            {"signal": "测试期直接上正规 API", "lens": "成本失控", "follow_up": "先用中转商验证，效果通后切正规 API"},
        ]
    },
    "dk-post-hoc-framework-vs-messy-reality": {
        "dir": "dark-knowledges",
        "prepend": "",
        "append": "\n---\n\n## 迭代日志\n\n- **2026-07-20 v1.0**：来自付则宇 AI 口播工具开发经验分享。",
        "signals": [
            {"signal": "方法论步骤完美线性", "lens": "框架里没有回环、失败、情绪", "follow_up": "检查是否事后重构，补真实过程时间线"},
            {"signal": "框架第一步太\"高级\"", "lens": "要求初学者先建立完整认知", "follow_up": "标注这是复盘结构，执行时应先小范围试错"},
            {"signal": "案例分享只有正确做法", "lens": "缺少踩坑细节", "follow_up": "单独列出真实过程与在坑里学到的认知"},
        ]
    },
    "dk-market-info-gap-to-product-strategy": {
        "dir": "dark-knowledges",
        "prepend": "",
        "append": "\n---\n\n## 迭代日志\n\n- **2026-07-20 v1.0**：来自付则宇 AI 口播工具开发经验分享。",
        "signals": [
            {"signal": "市面已有工具=没机会", "lens": "把存在等同于被使用", "follow_up": "去目标社区查\"怎么买/多少钱\"频率"},
            {"signal": "产品追求 100 分效果", "lens": "忽视用户认知门槛", "follow_up": "评估零门槛+80分是否大于专业 100 分"},
            {"signal": "讨论热火朝天=大众在用", "lens": "圈内热度误判为渗透率", "follow_up": "区分圈内讨论与圈外实际接触"},
        ]
    },
    "case-fuzeyu-ai-koubo-tool-dev": {
        "dir": "cases",
        "prepend": "# 付则宇AI口播工具：从16小时到零门槛\n\n> 一句话：首条口播视频 1700 播放带来 20 咨询+1 海外订单。但制作耗时 16 小时。付则宇用 300+ 视频拆解→组件化→AI串联，把制作时间压到零门槛。\n\n---\n",
        "append": "\n---\n\n## 迭代日志\n\n- **2026-07-20 v1.0**：来自付则宇 AI 口播工具开发经验分享。",
        "signals": [
            {"signal": "首条视频制作耗时 16 小时", "lens": "制作门槛高难以规模化", "follow_up": "拆解→组件化→AI串联降低门槛"},
            {"signal": "1700 播放带来 20 咨询", "lens": "口播视频获客有效", "follow_up": "用自动化工具放大产能"},
            {"signal": "工具效果能做但用户不愿发", "lens": "数字人等方案网感差", "follow_up": "以\"愿不愿发朋友圈\"作为 80 分标准"},
        ]
    },
}

summary_table = """\n## 失败模式速查表\n\n| # | 失败模式 | 症状 | 付则宇的代价 | 修复 |\n|:---:|:---|:---|:---|:---|\n| 1 | **调研无标准** | 凭感觉判断工具好坏，没有审美标准 | 差点选了数字人方案 | 先拆 300 条视频建审美标准，再量化工具 |\n| 2 | **技术先于审美** | 上来就追 Hyper Friends，做了一个月才发现方向错了 | 一个月时间 | 先建审美→再选技术路线。不是\"什么技术新用什么\" |\n| 3 | **过度依赖AI分析** | 以为AI能自动判断\"什么是好视频\" | — | AI做执行，人做审美判断。审美不能被AI替代 |\n| 4 | **工具边界不清** | 试图做一个\"万能视频工具\" | — | 80分口播视频够用。不要试图覆盖所有视频类型 |\n| 5 | **忽略市场信息差** | 以为\"市面上已经有工具了\"就不做 | — | 老工具渗透率极低+用户不要认知要结果=信息差窗口 |\n\n"""

for fid, cfg in configs.items():
    std_path = os.path.join(BASE, cfg["dir"], f"{fid}.md")
    rec_path = os.path.join(RECOV, f"{fid}.md")
    fm_s, body_s = parse_fm(std_path)
    fm_r, body_r = parse_fm(rec_path)

    merged = dict(fm_s)
    for k in ["id", "title", "type", "status", "author", "reviewed_by", "review_date", "created_at", "domain"]:
        if k in fm_s:
            merged[k] = fm_s[k]
    merged["updated_at"] = "2026-07-20"
    if "confidence" in fm_r:
        merged["confidence"] = max(fm_s.get("confidence", 0), fm_r.get("confidence", 0))
    if "trust_level" in fm_r:
        merged["trust_level"] = fm_r.get("trust_level") or fm_s.get("trust_level")

    merged["related"] = unique(list(fm_s.get("related", [])) + list(fm_r.get("related", [])))
    if len(merged["related"]) < 5:
        extras = ["framework-一堂-基本功-四字诀拆建推练", "framework-yitang-shishi-qiushi", "framework-一堂五步法-单元模型", "dk-market-info-gap-to-product-strategy", "tool-ai-video-cost-optimization"]
        for e in extras:
            if e not in merged["related"]:
                merged["related"].append(e)
            if len(merged["related"]) >= 5:
                break

    merged["quality_labels"] = unique(list(fm_s.get("quality_labels", [])) + list(fm_r.get("quality_labels", [])))
    merged["tags"] = unique(list(fm_s.get("tags", [])) + list(fm_r.get("tags", [])))
    merged["query_triggers"] = unique(list(fm_s.get("query_triggers", [])) + list(fm_r.get("query_triggers", [])))
    merged["source_refs"] = fm_s.get("source_refs", fm_r.get("source_refs", []))
    merged["diagnostic_signals"] = cfg["signals"]

    body = body_r.strip("\n")
    if cfg.get("prepend"):
        body = cfg["prepend"].rstrip("\n") + "\n\n" + body
    if cfg.get("insert_table"):
        body = body.replace("## 原始表述", summary_table.lstrip() + "## 原始表述", 1)
    if cfg.get("append"):
        body = body + cfg["append"]

    fm_text = yaml.dump(merged, allow_unicode=True, sort_keys=False, default_flow_style=False)
    out = f"---\n{fm_text}---\n{body}\n"
    with open(std_path, "w", encoding="utf-8") as f:
        f.write(out)
    print(f"Merged {fid}: related={len(merged['related'])} signals={len(merged['diagnostic_signals'])}")

print("Done")
