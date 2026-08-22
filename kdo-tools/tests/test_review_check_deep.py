"""#419 复盘门禁深度四条硬指标测试（B3-3 拍板口径）。

运行：python -m pytest kdo-tools/tests/test_review_check_deep.py -q
"""
import importlib.util
import sys
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "review_check", Path(__file__).resolve().parent.parent / "review-check.py"
)
rc = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(rc)

GOOD = """## 差异栏
这次不是重复自审：我首次处理会诊批次任务链，从单任务交付升级为七单连续交付，且经历了第一次"文件丢失"事故处理。

## 概要
交付七单任务并处理幻影丢失事故。

## 关键决策

| 决策 | 理由 | 结果 |
|:--|:--|:--|
| 执行报告落任务单 | 欧阳锋批量审不追外部文件 | 复审 PASS |

## 思维盲点

1. bash 中文路径是陷阱。为什么漏：明知中文目录 ls 报过编码错误，仍用 bash 链式 mv。根因是惯性使用 bash 命令。
2. 报丢失前没验证存在证据。为什么漏：看到文件消失直接脑补被删。根因是情绪优先于证据。

## 顿悟
以前以为执行层的"方式"不重要，只要"内容"正确即可——这次被推翻：方式错误可以制造不存在的"事故"。

## 过程资产

| 新增/更新 | 路径 |
|:--|:--|
| #409 YAML 修复 | kdo-tools/review-check.py |
| 执行报告 | 60_feedback/tasks/task_20260822_huangyaoshi-health-metrics-set.md |

## 元反思
下次先验证存在证据再报丢失。

## Truman复盘

### 逐轮映射

| 轮次 | 人做了什么 | 双三角 | AI做了什么 | 双三角 |
|:--|:--|:--|:--|
| 1 | 领取任务 | 决策 | 执行 | 数据 |

### 飞轮效应
会诊到落地不到 12 小时。

### 对照实验
- 无人协作：人工数天
- 无AI协作：无法批量修复
- 合在一起：12 小时交付

### 下次改进
- Agent自身：中文路径一律 Python
- 方法论卡更新：幻影丢失模式入错误模式库
"""

BAD = """## 差异栏
同上。

## 概要
今天做了任务。

## 关键决策

| 决策 | 理由 | 结果 |
|:--|:--|:--|
| 无 | — | — |

## 思维盲点

1. 时间分配不均。

## 顿悟
今天学到了很多。

## 过程资产
无。

## 元反思
下次注意。

## Truman复盘

### 逐轮映射
（空白）

### 飞轮效应
无

### 对照实验
（空白）

### 下次改进
无
"""


def test_deep_good_passes_all():
    d = rc.deep_check(GOOD)
    for k, v in d.items():
        assert v["verdict"] == "pass", f"{k}: {v['detail']}"


def test_deep_bad_fails_four():
    d = rc.deep_check(BAD)
    assert d["blindspot_rooted"]["verdict"] == "fail"   # 盲点无根因
    assert d["epiphany_reversal"]["verdict"] == "fail"  # 顿悟无推翻
    assert d["diff_specific"]["verdict"] == "fail"      # 差异栏套话"同上"


def test_deep_asset_paths_manual_when_no_paths():
    d = rc.deep_check(BAD)
    assert d["asset_real_paths"]["verdict"] in ("fail", "manual")  # "无。" 无路径 → manual
    assert d["asset_real_paths"]["ok"] is True  # manual 不拦


def test_grade_A_requires_deep():
    ok = rc.check_content_depth(GOOD, size=3200)
    assert ok["grade"] == "A", ok["deep"]
    bad = rc.check_content_depth(BAD, size=3200)
    assert bad["grade"] != "A"


def test_diff_cliche_word_detected():
    d = rc.deep_check("## 差异栏\n和上次一样。\n")
    assert d["diff_specific"]["verdict"] == "fail"


# ── 官方校准样本回归（王语嫣 2026-08-22 提供，frontmatter 含期望判定）──
SAMPLE_DIR = Path(__file__).resolve().parent.parent.parent / "60_feedback" / "eval-results" / "review-gate-419-samples"


def _judge(name):
    content = (SAMPLE_DIR / f"{name}.md").read_text(encoding="utf-8")
    r = rc.check_content_depth(content, len(content.encode("utf-8")))
    return r["grade"], [v["verdict"] for v in r["deep"].values()]


def test_sample_a_expected_pass():
    grade, deep = _judge("sample-a-wangyuyan-2026-08-22")
    assert grade == "A"
    assert deep == ["pass", "pass", "pass", "pass"]


def test_sample_b_expected_partial():
    grade, deep = _judge("sample-b-laowantong-2026-08-22")
    assert grade == "B"
    assert deep == ["fail", "fail", "pass", "pass"]  # 盲点无根因 + 顿悟无推翻 = 王语嫣标注


def test_sample_c_expected_fail():
    grade, deep = _judge("sample-c-huangyaoshi-2026-08-22")
    assert grade == "C"
    assert deep[-1] == "fail"  # 差异栏空 = C 级红线
