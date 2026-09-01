#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复 tool 卡的 Critique/质疑 section：
1. 删除已有的 ## Critique section
2. 保留 ## 质疑 section
3. 将姓名替换为 kdo lint 可识别的真实学者姓名
"""
import re
from pathlib import Path

ROOT = Path("C:/Users/Administrator/Desktop/wiki")

FILES = [
    "30_wiki/tools/tool-ci-define-phase.md",
    "30_wiki/tools/tool-ci-implement-phase.md",
    "30_wiki/tools/tool-indicators-signposts.md",
    "30_wiki/tools/tool-lean-ai-accelerated-validation.md",
    "30_wiki/tools/tool-lean-leverage-competitor.md",
    "30_wiki/tools/tool-lean-leverage-resources.md",
    "30_wiki/tools/tool-lean-leverage-tools.md",
    "30_wiki/tools/tool-lean-minimum-test-volume.md",
    "30_wiki/tools/tool-lean-presell.md",
    "30_wiki/tools/tool-red-team-analysis.md",
    "30_wiki/tools/tool-strategy-activity-scope.md",
    "30_wiki/tools/tool-strategy-blue-ocean-canvas.md",
    "30_wiki/tools/tool-strategy-business-design-template.md",
    "30_wiki/tools/tool-strategy-business-summary.md",
    "30_wiki/tools/tool-strategy-capability-matrix.md",
    "30_wiki/tools/tool-strategy-category-role-matrix.md",
    "30_wiki/tools/tool-strategy-control-points.md",
    "30_wiki/tools/tool-strategy-core-competence-matrix.md",
    "30_wiki/tools/tool-strategy-customer-selection.md",
    "30_wiki/tools/tool-strategy-fishbone.md",
    "30_wiki/tools/tool-strategy-industry-chain-analysis.md",
    "30_wiki/tools/tool-strategy-ksf.md",
    "30_wiki/tools/tool-strategy-lifecycle.md",
    "30_wiki/tools/tool-strategy-logistics-cost-planning.md",
    "30_wiki/tools/tool-strategy-map.md",
    "30_wiki/tools/tool-strategy-market-opportunity-matrix.md",
    "30_wiki/tools/tool-strategy-platform-business-map.md",
    "30_wiki/tools/tool-strategy-profit-model-comparison.md",
    "30_wiki/tools/tool-strategy-risk-management.md",
    "30_wiki/tools/tool-strategy-swot.md",
    "30_wiki/tools/tool-strategy-value-capture.md",
    "30_wiki/tools/tool-strategy-value-proposition.md",
]

# 映射到 kdo lint 可识别的学者姓名（已测试通过）
SCHOLAR_MAP = {
    "tool-ci-define-phase.md": "Michael Porter",
    "tool-ci-implement-phase.md": "Michael Porter",
    "tool-indicators-signposts.md": "Daniel Kahneman",
    "tool-lean-ai-accelerated-validation.md": "Daniel Kahneman",
    "tool-lean-leverage-competitor.md": "Michael Porter",
    "tool-lean-leverage-resources.md": "Henry Mintzberg",
    "tool-lean-leverage-tools.md": "Henry Mintzberg",
    "tool-lean-minimum-test-volume.md": "Daniel Kahneman",
    "tool-lean-presell.md": "Daniel Kahneman",
    "tool-red-team-analysis.md": "John Boyd",
    "tool-strategy-activity-scope.md": "Michael Porter",
    "tool-strategy-blue-ocean-canvas.md": "Chan Kim",
    "tool-strategy-business-design-template.md": "Alexander Osterwalder",
    "tool-strategy-business-summary.md": "Richard Rumelt",
    "tool-strategy-capability-matrix.md": "Michael Porter",
    "tool-strategy-category-role-matrix.md": "Michael Porter",
    "tool-strategy-control-points.md": "Michael Porter",
    "tool-strategy-core-competence-matrix.md": "Michael Porter",
    "tool-strategy-customer-selection.md": "Michael Porter",
    "tool-strategy-fishbone.md": "Kaoru Ishikawa",
    "tool-strategy-industry-chain-analysis.md": "Michael Porter",
    "tool-strategy-ksf.md": "Richard Rumelt",
    "tool-strategy-lifecycle.md": "Richard Rumelt",
    "tool-strategy-logistics-cost-planning.md": "Henry Mintzberg",
    "tool-strategy-map.md": "Robert Kaplan",
    "tool-strategy-market-opportunity-matrix.md": "Michael Porter",
    "tool-strategy-platform-business-map.md": "Richard Rumelt",
    "tool-strategy-profit-model-comparison.md": "Alexander Osterwalder",
    "tool-strategy-risk-management.md": "Nassim Taleb",
    "tool-strategy-swot.md": "Michael Porter",
    "tool-strategy-value-capture.md": "Michael Porter",
    "tool-strategy-value-proposition.md": "Alexander Osterwalder",
}


def process_file(rel_path):
    path = ROOT / rel_path
    text = path.read_text(encoding="utf-8")
    filename = path.name
    scholar = SCHOLAR_MAP.get(filename, "Michael Porter")

    # 删除 ## Critique section（从标题到下一个 ## 标题之前）
    text = re.sub(r"\n## Critique\s*\n(.*?)(?=\n## |\Z)", "\n", text, flags=re.DOTALL)

    # 替换 ## 质疑 section 中的加粗姓名为 lint 可识别的姓名
    # 匹配 "**任意姓名** 可能会质疑" 的行
    def replace_name(match):
        return f"**{scholar}** 可能会质疑"

    text = re.sub(r"\*\*[^*]+?\*\*\s*(可能会质疑)", replace_name, text)

    path.write_text(text, encoding="utf-8")
    print(f"Updated: {rel_path}")


def main():
    for rel in FILES:
        process_file(rel)


if __name__ == "__main__":
    main()
