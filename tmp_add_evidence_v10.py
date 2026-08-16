#!/usr/bin/env python3
"""#317 verified 证据分级：verified 语义漂移修正——新增 evidence 字段 {grade: 实测|引用|推演, source, metric}。
输出 feature-periodic-table-v1.0.json（v0.9 保留备份不动）。首批 13 条三级证据回填（仅标具体数字条目）。
设计：verified 布尔保留（#272 stale 逻辑兼容）；evidence 缺省 = 未标注证据等级（待回填）。
语义边界：verify_note=验证结论文本；evidence.grade=证据性质；evidence.metric=指标；evidence.source=出处。
"""
import json, sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SRC = Path(r"C:/Users/Administrator/Desktop/wiki/10_raw/sources/feature-periodic-table-v0.9.json")
DST = Path(r"C:/Users/Administrator/Desktop/wiki/10_raw/sources/feature-periodic-table-v1.0.json")

# id -> evidence（首批 13 条，source 指向 Live258 作业集行号）
EVIDENCE = {
    # === 实测 ===
    "F018": {"grade": "实测", "source": "Live258 作业集 L2871（王鹏飞 40→65 分分水岭）",
             "metric": "只给身份=通用课程 40 分；身份+上下文=专属课程 65 分"},
    "F026": {"grade": "实测", "source": "Live258 作业集 L243-244（黄华春）",
             "metric": "阅读量 3800→6500（+71%）"},
    "F031": {"grade": "实测", "source": "Live258 作业集 L1987（jeffgirl 6/27 双目标冲突事件）",
             "metric": "拉新+复购双目标同场 → 曝光增但 GPM 降；V3 目标锚定后修正"},
    "F033": {"grade": "实测", "source": "Live258 作业集 L2016-2017（jeffgirl V4 六层漏斗）",
             "metric": "V4 六层漏斗定位断点（曝光→进入→商品曝光→点击→提单→成交）"},
    "F016": {"grade": "实测", "source": "Live258 作业集 L1017-1023（农夫三拳控制变量）",
             "metric": "5 关键帧仅 1 成功 → 3 关键帧稳定输出 60 分（音画同出/字幕正常）"},
    "F099": {"grade": "实测", "source": "Live258 作业集 L245（黄华春三篇数据对比）",
             "metric": "第三篇阅读 4200（降）但私信 3 人/签约 1 人/转化率 33%（升）——指标分离实证"},
    # === 引用 ===
    "F003": {"grade": "引用", "source": "Live258 作业集 L2385（jeffgirl 引课程案例）",
             "metric": "温度调优案例：生成报告成本从 2w 降到 2k（课程转述，非本人实验）"},
    "F029": {"grade": "引用", "source": "Live258 作业集 L1737（雍博引行业数据）",
             "metric": "工业零样本成功率 30-65%；叠加 20 条真机 Few-shot → 70-80%（行业数据引用）"},
    # === 推演 ===
    "F022": {"grade": "实测", "source": "试点#252（KDO 内部）：HINT_MAP 场景化提示上线",
             "metric": "lint 报错附场景化修复提示（功能上线实证，无量化指标）"},
    "F057": {"grade": "推演", "source": "Live258 作业集 L127-137（黄华春多阶段渐进规划）",
             "metric": "预期：四阶段渐进（价值判断→大纲→正文→优化）降低风险（规划中未实测）"},
    "F030": {"grade": "推演", "source": "Live258 作业集 L589-591（行知 RAG 素材库预期）",
             "metric": "预期：从业案例 RAG 库解决'AI 只会输出网络通用理论'（补全方案未实测）"},
    "F070": {"grade": "推演", "source": "Live258 作业集 L2207-2208（行知长期记忆预期）",
             "metric": "预期：记录往期发布内容，规避重复选题/观点（补全方案未实测）"},
    "F094": {"grade": "推演", "source": "Live258 作业集 L2321-2323（jeffgirl 主副模型可补项）",
             "metric": "预期：一个模型产出、一个模型校验提升稳定性（课后待补清单，未实测）"},
}


def main():
    data = json.loads(SRC.read_text(encoding="utf-8"))
    feats = data["features"]
    assert len(feats) == 100

    verified_count = 0
    for f in feats:
        if f["id"] in EVIDENCE:
            f["evidence"] = EVIDENCE[f["id"]]
        if f.get("verified"):
            verified_count += 1

    data["version"] = "V1.0"
    data["evidence_note"] = (
        f"#317 (2026-08-13): verified 证据分级——{len(EVIDENCE)} 条证据回填"
        "（grade=实测/引用/推演；verified 布尔保留兼容 #272；缺省 evidence=待回填）。"
        "语义边界: verify_note=验证结论；evidence=证据性质/指标/出处。v0.9 保留备份。"
    )

    DST.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ v1.0 已生成: {DST}")
    print(f"   evidence 回填 {len(EVIDENCE)} 条（实测 {sum(1 for e in EVIDENCE.values() if e['grade']=='实测')} / "
          f"引用 {sum(1 for e in EVIDENCE.values() if e['grade']=='引用')} / "
          f"推演 {sum(1 for e in EVIDENCE.values() if e['grade']=='推演')}）")
    print(f"   verified 条目 {verified_count} 条全部保留")
    d2 = json.loads(DST.read_text(encoding="utf-8"))
    assert len(d2["features"]) == 100
    assert sum(1 for f in d2["features"] if f.get("verified")) == verified_count
    print("   ✅ 完整性校验通过：100 Feature 全保留，verified 计数一致")


if __name__ == "__main__":
    main()
