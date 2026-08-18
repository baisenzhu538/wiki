#!/usr/bin/env python3
"""微信视频号定向采集管线（proj_20260816_wechat-collect 顶层文档）。

按博主名定向收集视频号内容 → 转逐字稿 → 沉淀知识资产。

用法:
  python kdo-tools/collect_wechat.py --scan-wechat --auto-knowledge   # 偶遇一键：扫描+转写+知识化（楚门方式一）
  python kdo-tools/collect_wechat.py --scan-wechat --resdownloader-dir "D:/res-downloader/downloads"
  python kdo-tools/collect_wechat.py --author "博主名" --limit 5 --min-likes 100  # 博主定向（方式二，需 TikHub token）
  python kdo-tools/collect_wechat.py --import-local "C:/path/video.mp4"           # 本地视频导入
  python kdo-tools/collect_wechat.py --url "https://channels.weixin.qq.com/..."   # 链接入口（记录+提示播放嗅探）

通道（2026-08-17 定稿，楚门两种方式对齐）:
  ① res-downloader 嗅探（主力·偶遇）：播放视频号即自动下载 mp4 → 管线扫描转写
  ② 本地导入（--import-local）——无 token 兜底
  ③ TikHub API（--author，需 TIKHUB_API_TOKEN env）——博主定向备选

架构:
  Windows CLI 控制 + WSL GPU 转写（faster-whisper，WSL 无 agent 但工具可用）
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WIKI = Path(__file__).resolve().parent.parent
# 铁律（用户 2026-08-17 纠偏）：新内容第一站必须是 00_inbox/，未经处理不放 10_raw/ 和 30_wiki/
INBOX_DIR = WIKI / "00_inbox" / "wechat-collect"
WORK_DIR = WIKI / "60_feedback" / "wechat-collect"  # 日志/状态，非知识库内容
WSL_WHISPER = "/home/dministrator/wechat-collect/transcribe.py"  # WSL 转写脚本（GPU）

API_BASE = "https://api.tikhub.dev/api/v1/wechat_channels"


def ensure_dirs():
    INBOX_DIR.mkdir(parents=True, exist_ok=True)
    WORK_DIR.mkdir(parents=True, exist_ok=True)


def get_token() -> str:
    token = os.environ.get("TIKHUB_API_TOKEN", "")
    if not token:
        # 尝试从常见位置读
        env_file = Path.home() / ".tikhub_token"
        if env_file.exists():
            token = env_file.read_text(encoding="utf-8").strip()
    return token


# ── 下载路线（爆炸式调研 2026-08-16 结论）──────────────────────────
# 路线 A: MITM 代理+证书（wx_channel/scribe-transcribe/ltaoo/res-downloader）
#   本地化，不依赖第三方 token；需管理员+证书；scribe-transcribe 可编程（Python CLI）
# 路线 B: API 解析+Referer（元宝扫码登录态 / gkgy curl）
#   主力通道（调研建议）；公共 Worker 已失效（1042），需自持登录态
# 路线 C: TikHub API（需 token，第三方）——原主通道降级为备选
REFERER = "https://channels.weixin.qq.com/"


def download_via_referer(url: str, dest: Path) -> bool:
    """路线 B：带 Referer 下载（微信 CDN 要求，否则拒绝）。

    Referer 必须为 channels.weixin.qq.com（调研 §6 反爬情报）。
    """
    import urllib.request
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Referer": REFERER,
        })
        with urllib.request.urlopen(req, timeout=60) as resp, open(dest, "wb") as f:
            f.write(resp.read())
        return dest.stat().st_size > 10_000
    except Exception as e:
        print(f"  ⚠️ 下载失败: {e}")
        return False


def download_via_scribe(url: str, dest: Path) -> bool:
    """路线 A（备用）：调用 scribe-transcribe 下载（如已安装）。

    scribe-transcribe: python main.py serve --download-dir <dir>
    需提前安装（GitHub jun7799/scribe-transcribe），网页版 MITM 免 PC 客户端。
    """
    scribe = shutil.which("scribe") or shutil.which("scribe-transcribe")
    if not scribe:
        print("  ⚠️ scribe-transcribe 未安装（路线 A 备用，可跳过）")
        return False
    try:
        r = subprocess.run([scribe, url], capture_output=True, timeout=120)
        # scribe 下载到其默认目录，此处仅标记可用性
        return r.returncode == 0
    except Exception as e:
        print(f"  ⚠️ scribe 调用失败: {e}")
        return False


def search_author(author: str, limit: int = 10, min_likes: int = 0) -> list:
    """通道 A：TikHub 搜索博主视频。"""
    import urllib.request
    import urllib.parse

    token = get_token()
    if not token:
        print("❌ 未找到 TikHub token（env TIKHUB_API_TOKEN 或 ~/.tikhub_token）")
        print("  注册: https://user.tikhub.io （免费额度）")
        print("  或改用 --import-local 通道 B（手动下载视频 → 转写）")
        return []

    url = f"{API_BASE}/fetch_search_latest?keywords={urllib.parse.quote(author)}"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"❌ TikHub 请求失败: {e}")
        return []

    items = data.get("data", {}).get("items", []) if isinstance(data, dict) else []
    videos = []
    for it in items[:limit]:
        likes = it.get("like_count", 0)
        if likes < min_likes:
            continue
        videos.append({
            "title": it.get("title", ""),
            "author": it.get("nickname", author),
            "likes": likes,
            "download_url": it.get("video_url", "") or it.get("url", ""),
            "cover": it.get("cover_url", ""),
        })
    return videos


def download_video(url: str, dest: Path) -> bool:
    """下载视频（带微信 CDN 要求的 Referer，调研 §6：无 Referer 微信必拒）。"""
    import urllib.request
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Referer": REFERER,
        })
        with urllib.request.urlopen(req, timeout=60) as resp, open(dest, "wb") as f:
            f.write(resp.read())
        return dest.stat().st_size > 10_000  # >10KB 视为有效
    except Exception as e:
        print(f"  ⚠️ 下载失败: {e}")
        return False


def _win_to_wsl(p: Path) -> str:
    """Windows 绝对路径 → WSL /mnt/<盘符>/... 路径（支持任意盘符）。"""
    s = str(p).replace("\\", "/")
    import re
    m = re.match(r"^([A-Za-z]):/(.*)$", s)
    if m:
        return f"/mnt/{m.group(1).lower()}/{m.group(2)}"
    return s


def transcribe_video(video_path: Path, output_md: Path) -> bool:
    """通道：调用 WSL faster-whisper（GPU）转写。"""
    wsl_video = _win_to_wsl(video_path)
    wsl_out = _win_to_wsl(output_md)
    cmd = ["wsl", "-e", "bash", "-c",
           f"python3 {WSL_WHISPER} \"{wsl_video}\" \"{wsl_out}\""]
    try:
        r = subprocess.run(cmd, capture_output=True, timeout=600)
        if r.returncode == 0 and output_md.exists():
            return True
        print(f"  ⚠️ 转写失败: {r.stderr.decode('utf-8', errors='replace')[-200:]}")
        return False
    except Exception as e:
        print(f"  ⚠️ 转写异常: {e}")
        return False


def import_text(text_file: Path):
    """通道 D（手机转文字入库）：小程序转好的文字稿 → 直接知识化。

    手机端路径：视频号 → 小程序转文字 → 文字发到文件传输助手 → PC 微信落盘
    msg/file/ 或 msg/attach/ 的 txt → 本函数读入 → 入 10_raw/sources/。
    """
    ensure_dirs()
    print(f"📝 导入文字稿: {text_file}")
    content = text_file.read_text(encoding="utf-8", errors="replace")
    out_md = INBOX_DIR / f"src_wechat_text_{text_file.stem[:30]}.md"
    out_md.write_text(
        f"# 逐字稿（手机小程序转写）\n\n> 来源: {text_file.name} | 转写: 手机小程序\n\n{content}\n",
        encoding="utf-8")
    print(f"✅ 文字稿已入库: {out_md}")
    print("  下一步: python kdo-tools/wechat_knowledge.py <该文件> 做 LLM 三层次总结")
    return True


def import_url(url: str):
    """路线 B：视频号链接 → 解析 → 下载 → 转写 → 知识化。

    视频号链接（如 https://channels.weixin.qq.com/... 或 finder.video.qq.com/...）
    通过 API 解析 + Referer 下载（调研路线 B）。无 token 时可先人工下载到本地
    再用 --import-local。
    """
    ensure_dirs()
    print(f"🔗 处理视频号链接: {url}")
    # 暂存链接供后续处理
    link_file = WORK_DIR / "pending_links.txt"
    with open(link_file, "a", encoding="utf-8") as f:
        f.write(url + "\n")
    print(f"✅ 链接已记录: {link_file}")
    print("  下一步：用 TikHub/API 解析工具下载该链接视频 → --import-local 转写")
    print("  或：手机端用浏览器打开链接 → 下载视频 → --import-local")


def import_local(video_path: Path):
    """通道 B：本地视频 → 转写 → 入 sources。"""
    ensure_dirs()
    print(f"📥 导入本地视频: {video_path}")
    out_md = INBOX_DIR / f"src_wechat_{video_path.stem[:30]}.md"
    if transcribe_video(video_path, out_md):
        print(f"✅ 逐字稿已生成: {out_md}")
    else:
        print("❌ 转写失败")


def _scan_patterns() -> list:
    """PC 微信接收目录 + res-downloader 下载目录的候选文件模式。"""
    patterns = [
        r"D:/Backup/Documents/xwechat_files/*/msg/video/**/*.mp4",
        r"D:/Backup/Documents/xwechat_files/*/msg/video/**/*.mov",
        r"D:/Backup/Documents/xwechat_files/*/msg/file/**/*.txt",
        r"D:/Backup/Documents/xwechat_files/*/msg/file/**/*.html",
        str(Path.home() / "Documents" / "WeChat Files" / "*" / "FileStorage" / "**" / "*.mp4"),
        # res-downloader 下载目录（可被 --resdownloader-dir 覆盖）
        r"C:/Users/Administrator/Downloads/res-downloader/**/*.mp4",
    ]
    return patterns


def scan_wechat_files(limit: int = 5, res_dl_dir: str | None = None, auto_knowledge: bool = False):
    """通道 C（偶遇）：扫描 PC 微信接收目录 + res-downloader 目录，新内容 → 转写/入库。

    偶遇链路（楚门方式一，2026-08-17 定稿）：
      手机转发链接→文件传输助手 → PC 微信落盘 msg/file/*.txt
      → 本函数提取链接 → 提示用户在微信打开链接播放 → res-downloader 嗅探下载 mp4
      → 下次扫描发现 mp4 → 转写 → （可选）LLM 知识化

    已处理文件记录到 workdir/processed.log（成功才记录，失败下次重试）。
    """
    ensure_dirs()
    import glob

    patterns = _scan_patterns()
    if res_dl_dir:
        patterns.append(str(Path(res_dl_dir) / "**" / "*.mp4"))

    candidates = []
    for p in patterns:
        candidates.extend(glob.glob(p, recursive=True))

    processed_log = WORK_DIR / "processed.log"
    processed = set()
    if processed_log.exists():
        # 规范化后再比较：glob 返回正斜杠（D:/Backup/...），记录是 Path 字符串（D:\Backup\...）
        processed = {os.path.normcase(str(Path(ln))) for ln in
                     processed_log.read_text(encoding="utf-8").splitlines()}

    new_files = [Path(c) for c in candidates if os.path.normcase(str(Path(c))) not in processed]
    new_files.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    new_files = new_files[:limit]

    if not new_files:
        print(f"📭 无新内容（已处理 {len(processed)} 个，扫描 {len(candidates)} 个候选）")
        return

    print(f"📥 发现 {len(new_files)} 个新内容（偶遇通道）：")
    ok = 0
    pending_links = []
    for v in new_files:
        if v.suffix.lower() in (".mp4", ".mov", ".mp3", ".m4a"):
            print(f"  🎬 {v.name}（{v.stat().st_size // 1024 // 1024}MB, 视频文件）")
            out_md = INBOX_DIR / f"src_wechat_{v.stem[:30]}.md"
            if transcribe_video(v, out_md):
                ok += 1
                with open(processed_log, "a", encoding="utf-8") as f:
                    f.write(str(v) + "\n")
            else:
                print(f"    ⚠️ 转写失败——不记录，下次扫描重试")
        else:
            # 链接/文字文件（.txt/.html）——提取视频号链接 或 手机小程序文字稿
            try:
                content = v.read_text(encoding="utf-8", errors="replace")
                links = re.findall(r"https?://[^\s\"'<>]+", content)
                wx_links = [l for l in links if "channels.weixin" in l or "finder" in l or "video" in l]
                if wx_links:
                    print(f"  🔗 {v.name}（视频号链接，已记录）")
                    print("      👉 下一步：在微信中打开该链接播放 → res-downloader 自动嗅探下载 → 再跑本命令")
                    out_md = INBOX_DIR / f"src_wechat_link_{v.stem[:30]}.md"
                    out_md.write_text(
                        f"# 视频号链接采集\n\n> 来源: {v.name}（偶遇转发）\n\n" +
                        "\n".join(f"- {l}" for l in wx_links) + "\n",
                        encoding="utf-8")
                    pending_links.extend(wx_links)
                    ok += 1
                elif len(content) > 200:
                    # 无链接且内容较长 = 手机小程序转好的文字稿（通道 D）
                    print(f"  📝 {v.name}（手机文字稿，入库）")
                    out_md = INBOX_DIR / f"src_wechat_text_{v.stem[:30]}.md"
                    out_md.write_text(
                        f"# 逐字稿（手机小程序转写）\n\n> 来源: {v.name}\n\n{content}\n",
                        encoding="utf-8")
                    ok += 1
                else:
                    print(f"  ⚪ {v.name}（短文本/无效，跳过）")
                with open(processed_log, "a", encoding="utf-8") as f:
                    f.write(str(v) + "\n")
            except Exception as e:
                print(f"    ⚠️ 解析失败: {e}")
    print(f"✅ 偶遇采集完成: {ok}/{len(new_files)} 处理成功")

    if pending_links:
        print(f"🔗 共 {len(pending_links)} 个视频号链接待播放嗅探（见 10_raw/sources/src_wechat_link_*.md）")

    if auto_knowledge and ok > 0:
        print("\n🧠 自动知识化（--auto-knowledge）...")
        knowledge_all()


def knowledge_all():
    """调用 wechat_knowledge.py --all：所有未知识化的 src_wechat_* 做 LLM 三层次总结。"""
    script = Path(__file__).resolve().parent / "wechat_knowledge.py"
    try:
        r = subprocess.run([sys.executable, str(script), "--all"],
                           capture_output=True, timeout=600)
        print(r.stdout.decode("utf-8", errors="replace"))
        if r.returncode != 0:
            print(f"⚠️ 知识化部分失败: {r.stderr.decode('utf-8', errors='replace')[-300:]}")
    except Exception as e:
        print(f"⚠️ 知识化调用异常: {e}")


def main():
    ap = argparse.ArgumentParser(description="微信视频号定向采集管线")
    ap.add_argument("--author", help="博主名（通道 A 定向）")
    ap.add_argument("--limit", type=int, default=5, help="最多采集数")
    ap.add_argument("--min-likes", type=int, default=0, help="最低点赞筛选")
    ap.add_argument("--import-local", help="本地视频路径（通道 B）")
    ap.add_argument("--scan-wechat", action="store_true", help="扫描 PC 微信接收目录 + res-downloader 目录（偶遇通道）")
    ap.add_argument("--resdownloader-dir", help="res-downloader 下载目录（覆盖默认路径，配合 --scan-wechat）")
    ap.add_argument("--auto-knowledge", action="store_true", help="扫描/导入后自动跑 LLM 三层次知识化（楚门方式一全自动）")
    ap.add_argument("--url", help="视频号链接（路线 B 入口，仅记录链接）")
    ap.add_argument("--import-text", help="手机小程序转好的文字稿路径（通道 D）")
    args = ap.parse_args()

    ensure_dirs()

    if args.import_text:
        import_text(Path(args.import_text))
        return

    if args.url:
        import_url(args.url)
        return

    if args.scan_wechat:
        scan_wechat_files(args.limit, args.resdownloader_dir, args.auto_knowledge)
        return

    if args.import_local:
        import_local(Path(args.import_local))
        if args.auto_knowledge:
            print("\n🧠 自动知识化（--auto-knowledge）...")
            knowledge_all()
        return

    if args.author:
        print(f"🔍 搜索博主: {args.author}（通道 A）")
        videos = search_author(args.author, args.limit, args.min_likes)
        if not videos:
            print("未获取到视频（检查 token 或改用 --import-local）")
            return
        print(f"找到 {len(videos)} 个视频:")
        for i, v in enumerate(videos, 1):
            print(f"  {i}. [{v['likes']}赞] {v['title'][:40]}")
        # 下载 + 转写
        author_dir = WORK_DIR / args.author
        author_dir.mkdir(parents=True, exist_ok=True)
        ok = 0
        for i, v in enumerate(videos, 1):
            video_file = author_dir / f"{i:02d}_{v['title'][:20]}.mp4"
            print(f"⬇️  下载 {i}/{len(videos)}: {v['title'][:30]}")
            if download_video(v["download_url"], video_file):
                out_md = INBOX_DIR / f"src_wechat_{args.author}_{i:02d}.md"
                if transcribe_video(video_file, out_md):
                    ok += 1
        print(f"✅ 完成: {ok}/{len(videos)} 转写成功，逐字稿在 {INBOX_DIR}")
        return

    ap.print_help()


if __name__ == "__main__":
    main()
