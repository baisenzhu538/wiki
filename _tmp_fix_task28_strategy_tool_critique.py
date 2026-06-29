#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
任务 #28：为 11 张 strategy 域 tool 卡补充 Critique 关键术语并统一 frontmatter。
"""
import re
from pathlib import Path
import yaml

ROOT = Path("C:/Users/Administrator/Desktop/wiki")

FILES = [
    "30_wiki/tools/tool-lean-leverage-traffic.md",
    "30_wiki/tools/tool-lean-minimum-test-volume.md",
    "30_wiki/tools/tool-lean-minimum-version.md",
    "30_wiki/tools/tool-lean-premium-service.md",
    "30_wiki/tools/tool-lean-presell.md",
    "30_wiki/tools/tool-lean-product-kernel-metrics.md",
    "30_wiki/tools/tool-lean-stealth-service.md",
    "30_wiki/tools/tool-strategy-logistics-cost-planning.md",
    "30_wiki/tools/tool-strategy-market-opportunity-matrix.md",
    "30_wiki/tools/tool-strategy-value-capture.md",
    "30_wiki/tools/tool-yitang-channel-partnership-design.md",
]

# 需要在 Critique/质疑 section 末尾追加关键术语提醒的文件
KEY_TERMS_APPENDIX = {
    "tool-lean-leverage-traffic.md": (
        "使用本工具前，应明确其**获客渠道假设**、流量池与真实目标用户画像的**边界**、"
        "把互动当付费意愿的**反例**，以及「用户已产生行动意愿」这一隐含**前提**，"
        "避免把借流量的局部信号直接当作全局需求成立的证据。"
    ),
    "tool-lean-minimum-version.md": (
        "使用本工具前，应明确其**具体假设**（用户愿为最小功能集付费）、适用**边界**"
        "（如合规/安全/信任硬门槛）、把尝鲜者反馈当市场信号的**反例**，"
        "以及「最小版本能独立交付完整价值」这一隐含**前提**。"
    ),
    "tool-lean-premium-service.md": (
        "使用本工具前，应明确其**具体假设**（高接触 VIP 服务能映射标准化产品价值）、"
        "适用**边界**（如服务可拆解为 SOP）、把创始人亲自服务的好感当普遍需求的**反例**，"
        "以及「人工溢价可被剥离」这一隐含**前提**。"
    ),
    "tool-lean-product-kernel-metrics.md": (
        "使用本工具前，应明确其**具体假设**（三环节指标能真实反映产品内核健康度）、"
        "适用**边界**（如数据口径统一、团队不把指标当 KPI）、把虚荣指标当验证信号的**反例**，"
        "以及「指标能驱动每周实验决策」这一隐含**前提**。"
    ),
    "tool-lean-stealth-service.md": (
        "使用本工具前，应明确其**具体假设**（人工后台能等价模拟系统交付体验）、"
        "适用**边界**（如对延迟/合规/披露无刚性要求）、把 VIP 人工体验当产品化后体验的**反例**，"
        "以及「用户价值归因于服务结果而非具体实现方式」这一隐含**前提**。"
    ),
}


def parse_frontmatter(text):
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            fm = yaml.safe_load(parts[1])
            body = parts[2]
            return fm, body
    return None, text


def dump_frontmatter(fm, body):
    fm_str = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False)
    return f"---\n\n{fm_str}---{body}"


def add_key_terms(body, appendix):
    """在最后一个 ## 质疑 / ## Critique section 末尾追加关键术语提醒。"""
    # 按标题切分，保留标题行
    sections = re.split(r"(?=^## \w+)", body, flags=re.MULTILINE)
    new_sections = []
    appended = False
    for sec in sections:
        if not appended and (
            sec.startswith("## 质疑") or sec.startswith("## Critique")
        ):
            # 如果已经包含全部四个关键术语，则不再追加
            if all(t in sec for t in ["具体假设", "边界", "反例", "前提"]):
                new_sections.append(sec)
            else:
                sec = sec.rstrip() + "\n\n" + appendix + "\n"
                new_sections.append(sec)
            appended = True
        else:
            new_sections.append(sec)
    return "".join(new_sections)


def process_file(rel_path):
    path = ROOT / rel_path
    text = path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)

    if fm is None:
        print(f"SKIP (no frontmatter): {rel_path}")
        return

    # 更新 frontmatter
    fm["status"] = "enriched"
    fm["author"] = "老顽童"
    fm["reviewed_by"] = "pending"
    fm["updated_at"] = "2026-06-29"

    filename = path.name
    if filename in KEY_TERMS_APPENDIX:
        body = add_key_terms(body, KEY_TERMS_APPENDIX[filename])

    new_text = dump_frontmatter(fm, body)
    path.write_text(new_text, encoding="utf-8")
    print(f"Updated: {rel_path}")


def main():
    for rel in FILES:
        process_file(rel)


if __name__ == "__main__":
    main()
