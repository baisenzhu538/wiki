#!/usr/bin/env python3
"""偶遇采集产物自动转正（inbox → 知识库仓库）。

铁律（用户 2026-08-17 纠偏）：新内容第一站 00_inbox/，未经处理不入库。
本脚本 = 转正流程：把已知识化的产物按 KDO 规范流转——
  逐字稿 → 10_raw/sources/（素材层，source_id 文件名登记，零摩擦不变）
  case 卡 → 00_inbox/pending-cards/（待编排区——#380 A 方案，王语嫣 2026-08-20 改判：
    case 卡不再直入 30_wiki/cases/ 正式层，一律过王语嫣编排门禁后走既有生产流；
    watch_inbox 每 10 分钟扫描 pending-cards 并登记到 production-queue.md 的
    INBOX-PENDING 看板段，保证王语嫣可见）

内容校验前置（#380）：生成质量不合格的卡（标题乱码/LLM 总结失败占位/正文空壳）
不落待编排区，直接落 00_inbox/wechat-collect/_needs_rerun/ 并输出原因。

用法:
  python kdo-tools/wechat_promote.py            # 转正所有已知识化产物
  python kdo-tools/wechat_promote.py --dry-run  # 预览不执行
"""
import argparse
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WIKI = Path(__file__).resolve().parent.parent
INBOX_DIR = WIKI / "00_inbox" / "wechat-collect"
SOURCES_DIR = WIKI / "10_raw" / "sources"
CASES_DIR = WIKI / "30_wiki" / "cases"
PENDING_DIR = WIKI / "00_inbox" / "pending-cards"
RERUN_DIR = INBOX_DIR / "_needs_rerun"

# 内容校验（#380 最小实现）：对准 wechat_knowledge.py 的真实失败形态
MIN_BODY_CHARS = 200
LLM_FAIL_MARKERS = [
    "LLM 总结失败，请重试",  # wechat_knowledge.py 骨架占位（实测 Top10 空壳卡）
    "无法生成总结",
    "总结失败",
    "抱歉，我无法",
]
# 标题乱码：UTF-8 被按 latin-1 误读时标题会堆满 Latin-1 补充区字符（U+0080–U+00FF，
# 含 continuation byte 落在 80-BF 的 µ‹› 等——实测 e7536 乱码卡形态）
_MOJIBAKE_RE = re.compile("[-ÿ]{2,}")


def promote_transcript(f: Path, dry_run: bool) -> bool:
    """逐字稿 → 10_raw/sources/（文件名带 source_id：src_<date>_wechat_<hash>）。

    支持前缀：src_wechat_<hash> / src_wechat_tt_<hash>（头条视频）/ src_wechat_article_<hash>（公众号）
    / src_wechat_article_tt_<hash>（头条文章）。任意小写前缀均可，取最后一段字母数字为 hash。
    """
    m = re.search(r"src_wechat_(?:[A-Za-z]+_)*([A-Za-z0-9]{8,20})", f.name)
    if not m:
        return False
    hash_id = m.group(1)
    target = SOURCES_DIR / f"src_{date.today().isoformat()}_wechat_{hash_id}.md"
    if target.exists():
        print(f"⏭️  已转正: {target.name}")
        return True
    if dry_run:
        print(f"  [dry-run] {f.name} → {target.name}")
        return True
    shutil.copy2(f, target)
    print(f"✅ 逐字稿入仓: {target.name}")
    return True


def _content_issues(content: str) -> list[str]:
    """最小内容校验：返回问题清单（空列表=合格）。不通过的卡落 _needs_rerun。"""
    issues: list[str] = []

    m = re.search(r'^title:\s*"?([^"\n]+)"?', content, re.M)
    title = m.group(1).strip() if m else ""
    if not title:
        issues.append("title 为空")
    elif "�" in title or _MOJIBAKE_RE.search(title):  # U+FFFD 替换符 = 解码失败痕迹
        issues.append(f"标题疑似乱码: {title[:30]}")

    # 正文 = frontmatter 第二个 --- 之后
    parts = content.split("---", 2)
    body = parts[2] if content.startswith("---") and len(parts) >= 3 else content
    body_text = body.strip()
    if len(body_text) < MIN_BODY_CHARS:
        issues.append(f"正文过短（{len(body_text)} 字 < {MIN_BODY_CHARS}，疑 LLM 空壳卡）")
    for marker in LLM_FAIL_MARKERS:
        if marker in body_text:
            issues.append(f"LLM 总结失败占位: 「{marker}」")
            break
    return issues


def promote_case(f: Path, dry_run: bool) -> str:
    """case 卡 → 待编排区（#380 A 方案：不进 30_wiki，过王语嫣编排门禁再入库）。

    返回 "pending"（落待编排区）/ "rerun"（内容不合格退回）/ "skip"（跳过）。
    """
    content = f.read_text(encoding="utf-8")
    required = ["title:", "type:", "domain:", "source_refs:", "created_at:"]
    missing = [k for k in required if k not in content]
    if missing:
        print(f"⚠️ 跳过（缺 frontmatter {missing}）: {f.name}")
        return "skip"

    # 已流转过的卡不重复登记：待编排区/正式层/退回区已有同名卡 → 跳过
    if (PENDING_DIR / f.name).exists() or (CASES_DIR / f.name).exists() or (RERUN_DIR / f.name).exists():
        print(f"⏭️  已流转: {f.name}")
        return "skip"

    issues = _content_issues(content)
    if issues:
        reason = "; ".join(issues)
        if dry_run:
            print(f"  [dry-run] {f.name} → _needs_rerun/（{reason}）")
            return "rerun"
        RERUN_DIR.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, RERUN_DIR / f.name)
        (RERUN_DIR / f"{f.stem}.reason.txt").write_text(
            f"{f.name}\n退回原因（#380 内容校验，{date.today().isoformat()}）：{reason}\n",
            encoding="utf-8",
        )
        print(f"🚫 内容不合格 → _needs_rerun: {f.name}（{reason}）")
        return "rerun"

    if dry_run:
        print(f"  [dry-run] {f.name} → 00_inbox/pending-cards/（待王语嫣编排门禁）")
        return "pending"
    PENDING_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(f, PENDING_DIR / f.name)
    print(f"📥 case 卡落待编排区: {f.name}（等王语嫣门禁，watch_inbox 10 分钟内登记看板）")
    return "pending"


def main():
    ap = argparse.ArgumentParser(description="偶遇采集产物自动转正")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    print("📦 转正开始" + ("（dry-run 预览）" if args.dry_run else ""))
    t_ok = 0
    c_stats = {"pending": 0, "rerun": 0, "skip": 0}

    # 1) 逐字稿 → 素材层
    for f in sorted(INBOX_DIR.glob("src_wechat_*.md")):
        if promote_transcript(f, args.dry_run):
            t_ok += 1

    # 2) case 卡 → 待编排区（#380 A 方案）/ _needs_rerun（内容校验不合格）
    kdir = INBOX_DIR / "knowledge"
    if kdir.exists():
        for f in sorted(kdir.glob("case-wechat-*.md")):
            c_stats[promote_case(f, args.dry_run)] += 1

    print(f"\n📊 逐字稿 {t_ok} 个，case 卡 待编排 {c_stats['pending']} / 退回 {c_stats['rerun']} / 跳过 {c_stats['skip']}"
          + ("（dry-run，未写入）" if args.dry_run else ""))

    if not args.dry_run and t_ok:
        # 逐字稿入 10_raw/sources（检索索引覆盖层）→ L1 入库即增量更新检索索引
        # （2026-08-19）：不写"记得跑 kdo index"，让"要记得"这件事不存在
        # （pre-submit 的 L2 新鲜度门禁仍兜底）。
        # case 卡只到 00_inbox/pending-cards（不在索引覆盖层），不触发索引更新；
        # 待编排门禁通过、走既有生产流入 30_wiki 时由对应流程更新索引。
        r = subprocess.run(
            [sys.executable, "-m", "kdo", "index", "--incremental"],
            cwd=str(WIKI), capture_output=True, timeout=600,
        )
        if r.returncode == 0:
            print(f"🔍 检索索引已增量更新: {r.stdout.decode('utf-8', errors='replace').strip().splitlines()[-1] if r.stdout else 'ok'}")
        else:
            print(f"⚠️ 索引增量更新失败（不阻断转正，L3 巡检会抓到）: {r.stderr.decode('utf-8', errors='replace')[-150:]}")

    if not args.dry_run and c_stats["pending"]:
        print("✅ case 卡已落 00_inbox/pending-cards/——watch_inbox 将登记到 production-queue.md 待编排区，等王语嫣编排门禁")


if __name__ == "__main__":
    main()
