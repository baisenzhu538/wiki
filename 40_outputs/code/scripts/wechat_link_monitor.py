#!/usr/bin/env python3
"""微信视频号偶遇全自动采集监控（proj_20260816_wechat-collect 顶层文档·方式一）。

链路（2026-08-17 定稿）：
  手机转发链接到文件传输助手 → PC 微信数据库（SQLCipher 4）
  → 本脚本：解密+读文件传输助手消息 → 提取视频号链接
  → 调本地 wx_channels_download parse_sph（元宝 Cookie）拿直链
  → 下载 mp4 → WSL faster-whisper 转写 → LLM 三层次知识化
  → 全部产物落 00_inbox/wechat-collect/（铁律：第一站 inbox，未经处理不入库）

用法:
  python kdo-tools/wechat_link_monitor.py            # 跑一轮
  python kdo-tools/wechat_link_monitor.py --once     # 跑一轮（同默认）
  # 定时：Windows 计划任务每小时跑一次

依赖:
  - wx_channels_download 本地服务: http://127.0.0.1:2022（config.yaml cloudflare.sphCookie 已配）
  - wechat-decrypt 密钥: C:\\Users\\Administrator\\wechat-decrypt\\build_keys.py 的 passphrase
  - WSL 转写: /home/dministrator/wechat-collect/transcribe.py
"""
import argparse
import hashlib
import json
import os
import re
import sqlite3
import subprocess
import sys
import time
import urllib.parse
import urllib.request
import zstandard
from html import unescape as html_unescape
from pathlib import Path

# 系统代理(MITM 工具)会拦 API 直连——LLM/解析调用必须绕过代理
os.environ.setdefault("NO_PROXY", "api.deepseek.com,api.minimaxi.com")
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

WIKI = Path(__file__).resolve().parent.parent
INBOX_DIR = WIKI / "00_inbox" / "wechat-collect"
WORK_DIR = WIKI / "60_feedback" / "wechat-collect"
SEEN_FILE = WORK_DIR / "seen_links.txt"

WECHAT_DECRYPT_DIR = Path(r"C:\Users\Administrator\wechat-decrypt")
PASSPHRASE = bytes.fromhex("301c21c6a0ba4d28a8263a80193ba91bbe2aedb5b68646c3ba78f9ab96c29681")
DB_STORAGE = Path(r"D:\Backup\Documents\xwechat_files\wxid_53kdj7ep82rv22_ffd5\db_storage")
DECRYPTED_MSG_DB = WECHAT_DECRYPT_DIR / "decrypted" / "message" / "message_0.db"
FILEHELPER_TABLE = "Msg_9e20f478899dc29eb19741386f9343c8"  # MD5("filehelper")

PARSE_API = "http://127.0.0.1:2022/api/channels/parse_sph"
LINK_PATTERN = re.compile(r"https?://(?:weixin\.qq\.com/sph/|channels\.weixin\.qq\.com)[^\s\"'<>]+")


def ensure_dirs():
    INBOX_DIR.mkdir(parents=True, exist_ok=True)
    WORK_DIR.mkdir(parents=True, exist_ok=True)


def decrypt_current_db() -> bool:
    """用 passphrase 重新派生密钥并解密 message_0.db（数据库随微信同步更新）。"""
    try:
        sys.path.insert(0, str(WECHAT_DECRYPT_DIR))
        from key_scan_common import collect_db_files, verify_enc_key
        from Crypto.Cipher import AES
    except ImportError as e:
        print(f"⚠️ 依赖缺失: {e}")
        return False

    PAGE_SZ, SALT_SZ, IV_SZ, RESERVE_SZ = 4096, 16, 16, 80
    SQLITE_HDR = b"SQLite format 3\x00"

    target_rel = "message\\message_0.db"
    db_files, _ = collect_db_files(str(DB_STORAGE))
    for rel, path, size, salt_hex, page1 in db_files:
        if rel.replace("/", "\\") != target_rel:
            continue
        db_salt = bytes.fromhex(salt_hex)
        enc_key = hashlib.pbkdf2_hmac("sha512", PASSPHRASE, db_salt, 256000, dklen=32)
        if not verify_enc_key(enc_key, page1):
            print("⚠️ 密钥验证失败")
            return False
        out = DECRYPTED_MSG_DB
        out.parent.mkdir(parents=True, exist_ok=True)
        with open(out, "wb") as fout, open(path, "rb") as fin:
            for pgno in range(1, os.path.getsize(path) // PAGE_SZ + 1):
                page = fin.read(PAGE_SZ)
                if len(page) < PAGE_SZ:
                    break
                iv = page[PAGE_SZ - RESERVE_SZ: PAGE_SZ - RESERVE_SZ + IV_SZ]
                enc = page[SALT_SZ: PAGE_SZ - RESERVE_SZ] if pgno == 1 else page[:PAGE_SZ - RESERVE_SZ]
                dec = AES.new(enc_key, AES.MODE_CBC, iv).decrypt(enc)
                fout.write((SQLITE_HDR + dec + b"\x00" * RESERVE_SZ) if pgno == 1 else (dec + b"\x00" * RESERVE_SZ))
        print(f"✅ 数据库已解密: {out}")
        return True
    print("⚠️ message_0.db 未找到")
    return False


# 视频号卡片消息(XML type 51)里的媒体直链——自带 encfilekey，无需 parse_sph
XML_MEDIA_URL = re.compile(r"<url>(https?://wxapp\.tc\.qq\.com/[^<]*stodownload\?[^<]*)</url>")
# 公众号文章链接（纯文本 + 卡片 XML url；路径式 /s/xxx 和查询式 /s?__biz= 都要匹配）
MP_LINK = re.compile(r"https?://mp\.weixin\.qq\.com/s[/?][^\s\"'<>]+")
XML_MP_URL = re.compile(r"<url>(https?://mp\.weixin\.qq\.com/s[/?][^<]*)</url>")
# 今日头条链接（视频 + 图文文章）：m.toutiao.com/video/xxx（视频）、m.toutiao.com/group/xxx（文章旧格式）、
# m.toutiao.com/isXXX/（微信分享短链，重定向到 /group/ 或 /article/）、m.toutiao.com/article/xxx（文章新格式）
TTOUTIAO_LINK = re.compile(r"https?://(?:m|www)\.toutiao\.com/(?:video|group|article|is)[^\s\"'<>]+")


def extract_links(cutoff_ts: int) -> list:
    """读文件传输助手新消息，解压 ZSTD，提取视频号链接/直链/公众号链接。

    消息形态 → 提取结果：
      - 纯文本 weixin.qq.com/sph 链接 → parse_sph 解析
      - XML 视频号卡片(type 51 finderFeed) → 自带直链（直接下载，附标题/作者）
      - 公众号链接 → 抓取文章
    """
    if not DECRYPTED_MSG_DB.exists():
        print("⚠️ 解密库不存在，先解密")
        return []
    conn = sqlite3.connect(f"file:{DECRYPTED_MSG_DB}?mode=ro", uri=True)
    cur = conn.cursor()
    dctx = zstandard.ZstdDecompressor()
    links = []
    try:
        cur.execute(f"SELECT create_time, message_content FROM [{FILEHELPER_TABLE}] WHERE create_time > ? ORDER BY create_time", (cutoff_ts,))
        for ct, content in cur.fetchall():
            text = ""
            if isinstance(content, bytes):
                try:
                    text = dctx.decompress(content).decode("utf-8", errors="replace")
                except Exception:
                    continue
            elif isinstance(content, str):
                text = content
            # 1) 视频号卡片 XML 自带直链（同消息多个 media 只取第一个）
            media = XML_MEDIA_URL.findall(text)
            if media:
                links.append((ct, media[0].replace("&amp;", "&")))
            # 2) 纯文本 sph 分享链接
            for m in LINK_PATTERN.findall(text):
                links.append((ct, m))
            # 3) 公众号文章（纯文本或卡片 XML）——注意 XML 里 &amp; 需转义为 &，否则抓取 404
            mp_links = [u.replace("&amp;", "&") for u in list(MP_LINK.findall(text)) + list(XML_MP_URL.findall(text))]
            for m in dict.fromkeys(mp_links):
                links.append((ct, m))
            # 4) 今日头条视频
            for m in dict.fromkeys(TTOUTIAO_LINK.findall(text)):
                links.append((ct, m))
    except Exception as e:
        print(f"⚠️ 读取消息失败: {e}")
    finally:
        conn.close()
    return links


def parse_link(url: str) -> dict | None:
    """调本地 parse_sph 拿视频直链（不走 MITM 代理，直连本地 API）。"""
    q = urllib.parse.quote(url, safe="")
    req = urllib.request.Request(f"{PARSE_API}?url={q}")
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    try:
        with opener.open(req, timeout=60) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        if data.get("code") != 0:
            print(f"  ⚠️ parse_sph: {data.get('msg')}")
            return None
        d = data["data"]["data"]
        feed = d.get("feedInfo", {})
        video_url = feed.get("h264VideoInfo", {}).get("videoUrl") or feed.get("videoUrl", "")
        return {
            "url": video_url,
            "title": (feed.get("description") or "")[:60],
            "author": d.get("authorInfo", {}).get("nickname", ""),
            "likes": feed.get("likeCountFmt", ""),
        }
    except Exception as e:
        print(f"  ⚠️ parse_sph 调用失败: {e}")
        return None


def download(url: str, dest: Path) -> bool:
    """下载直链（带 CDN 要求的 Referer，直连不走 MITM 代理——代理会中断大文件）。"""
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))  # 无代理直连
    referer = "https://channels.weixin.qq.com/"
    if "toutiaovod.com" in url or "toutiao" in url:
        referer = "https://m.toutiao.com/"  # 头条 CDN 要求头条 Referer，否则 403
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Referer": referer,
    })
    for attempt in range(2):
        try:
            with opener.open(req, timeout=180) as resp, open(dest, "wb") as f:
                f.write(resp.read())
            if dest.stat().st_size > 10_000:
                return True
            print("  ⚠️ 文件过小，重试...")
        except Exception as e:
            print(f"  ⚠️ 下载失败(第{attempt+1}次): {str(e)[:100]}")
    return False


def parse_toutiao(url: str) -> dict | None:
    """今日头条视频解析：info 接口拿 token → vod API 拿直链（2026-08-18 打通）。

    链路: m.toutiao.com/i<id>/info/ → play_auth_token_v2(base64) → GetPlayInfoToken
          → vod.bytedanceapi.com/?token → Result.Data.PlayInfoList[].MainPlayUrl
    """
    import base64
    m = re.search(r"/video/(\d+)", url)
    if not m:
        return None
    item_id = m.group(1)
    try:
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        hdr = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X)"}
        req = urllib.request.Request(f"https://m.toutiao.com/i{item_id}/info/", headers=hdr)
        with opener.open(req, timeout=30) as resp:
            info = json.loads(resp.read().decode("utf-8"))
        data = info.get("data", {})
        token_b64 = data.get("play_auth_token_v2", "")
        title = data.get("title", "")
        if not token_b64:
            return None
        raw = base64.b64decode(token_b64 + "==").decode("utf-8")
        mm = re.search(r'"GetPlayInfoToken":"([^"]+)"', raw)
        if not mm:
            return None
        token = mm.group(1).encode().decode("unicode_escape")
        req2 = urllib.request.Request("https://vod.bytedanceapi.com/?" + token, headers={"User-Agent": "Mozilla/5.0"})
        with opener.open(req2, timeout=30) as resp2:
            play = json.loads(resp2.read().decode("utf-8"))
        pil = play["Result"]["Data"].get("PlayInfoList", [])
        for item in pil:
            if isinstance(item, str):
                try:
                    item = json.loads(item)
                except Exception:
                    continue
            if item.get("MainPlayUrl"):
                return {"url": item["MainPlayUrl"], "title": title, "author": ""}
    except Exception as e:
        print(f"  ⚠️ 头条解析失败: {str(e)[:100]}")
    return None


def fetch_toutiao_article(url: str) -> tuple:
    """抓头条图文文章 → (标题, 正文纯文本)。

    支持链接形态：
      - m.toutiao.com/group/<gid>/ （旧格式文章）
      - m.toutiao.com/article/<gid>/（新格式文章）
      - m.toutiao.com/isXXX/        （微信分享短链 → 跟随 302 拿到 gid）
    链路：提取 gid → m.toutiao.com/i<gid>/info/ → data.content(HTML) → 清洗为纯文本。
    与 parse_toutiao（视频）共用 info 接口，靠 content 字段区分文章/视频。
    """
    import re as _re
    # 1) 短链 isXXX → 跟随重定向拿最终 URL（含 gid）
    m = _re.search(r"m\.toutiao\.com/is([A-Za-z0-9]+)", url)
    if m:
        try:
            opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X)"})
            with opener.open(req, timeout=30) as resp:
                url = resp.geturl()
        except Exception as e:
            print(f"  ⚠️ 头条短链跟随失败: {str(e)[:100]}")
            return "", ""
    # 2) 提取 gid（/group/<gid>/ 或 /article/<gid>/）
    m = _re.search(r"/(?:group|article)/(\d+)", url)
    if not m:
        print(f"  ⚠️ 无法从头条链接提取文章 gid: {url[:80]}")
        return "", ""
    gid = m.group(1)
    # 3) info 接口
    try:
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        hdr = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X)"}
        req = urllib.request.Request(f"https://m.toutiao.com/i{gid}/info/", headers=hdr)
        with opener.open(req, timeout=30) as resp:
            info = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"  ⚠️ 头条文章 info 调用失败: {str(e)[:100]}")
        return "", ""
    data = info.get("data") or {}
    if not data.get("content"):
        print(f"  ⚠️ 头条文章无正文（可能为视频或已删）: {url[:80]}")
        return "", ""
    title = data.get("title", "")
    body = _re.sub(r"<[^>]+>", "\n", data["content"])
    body = _re.sub(r"\n{3,}", "\n\n", body).strip()
    # HTML 实体（&amp; &quot; &#34; 等）转回纯文本
    try:
        body = html_unescape(body)
    except Exception:
        pass
    return title, body


def fetch_mp_article(url: str) -> tuple:
    """抓公众号文章 → (标题, 正文文本)（无代理直连，MITM 代理会拦 https）。"""
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    try:
        with opener.open(req, timeout=60) as resp:
            html = resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"  ⚠️ 公众号抓取失败: {e}")
        return "", ""
    import re as _re
    m = _re.search(r"<h1[^>]*>(.*?)</h1>", html, _re.S)
    title = _re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else ""
    m2 = _re.search(r'id="js_content"[^>]*>(.*?)</div>', html, _re.S)
    body = ""
    if m2:
        body = _re.sub(r"<[^>]+>", "\n", m2.group(1))
        body = _re.sub(r"\n{3,}", "\n\n", body).strip()
    if not body:
        m3 = _re.search(r"<div class=\"rich_media_content[^>]*>(.*?)</div>", html, _re.S)
        if m3:
            body = _re.sub(r"<[^>]+>", "\n", m3.group(1))
            body = _re.sub(r"\n{3,}", "\n\n", body).strip()
    return title, body


def scan_downloaded_videos() -> int:
    """扫描 wx_channels_download 下载目录的新 mp4（播放拦截自动下载的）→ 转写 → 知识化。

    返回处理成功数。已处理记录在 seen_links.txt（前缀 file:）。
    """
    dl_dir = Path(r"D:\Backup\Downloads")
    if not dl_dir.exists():
        return 0
    seen = set()
    if SEEN_FILE.exists():
        seen = set(SEEN_FILE.read_text(encoding="utf-8").splitlines())
    ok = 0
    for v in sorted(dl_dir.glob("*.mp4"), key=lambda p: p.stat().st_mtime, reverse=True):
        if v.stat().st_mtime < int(time.time()) - 3 * 24 * 3600:
            continue  # 只处理 3 天内
        mark = f"file:{v.name}"
        if mark in seen:
            continue
        print(f"🎬 发现下载器产物: {v.name}（{v.stat().st_size//1024//1024}MB）")
        stem = hashlib.md5(v.name.encode()).hexdigest()[:16]
        out_md = INBOX_DIR / f"src_wechat_{stem}.md"
        wsl_v = str(v).replace("\\", "/")
        import re as _re
        m = _re.match(r"^([A-Za-z]):/(.*)$", wsl_v)
        wsl_v = f"/mnt/{m.group(1).lower()}/{m.group(2)}" if m else wsl_v
        wsl_out = str(out_md).replace("\\", "/")
        m2 = _re.match(r"^([A-Za-z]):/(.*)$", wsl_out)
        wsl_out = f"/mnt/{m2.group(1).lower()}/{m2.group(2)}" if m2 else wsl_out
        cmd = ["wsl", "-e", "bash", "-c", f"python3 /home/dministrator/wechat-collect/transcribe.py \"{wsl_v}\" \"{wsl_out}\""]
        r = subprocess.run(cmd, capture_output=True, timeout=600)
        if r.returncode == 0 and out_md.exists():
            print(f"  ✅ 转写完成: {out_md}")
            kscript = WIKI / "kdo-tools" / "wechat_knowledge.py"
            subprocess.run([sys.executable, str(kscript), str(out_md)], capture_output=True, timeout=300)
            ok += 1
            with open(SEEN_FILE, "a", encoding="utf-8") as f:
                f.write(mark + "\n")
        else:
            print(f"  ⚠️ 转写失败: {r.stderr.decode('utf-8', errors='replace')[-120:]}")
    return ok


def main():
    ensure_dirs()
    cutoff = int(time.time()) - 3 * 24 * 3600  # 最近 3 天
    # 0) 先处理下载器产物（播放拦截下载的已解密视频）
    scan_downloaded_videos()
    if not decrypt_current_db():
        return
    links = extract_links(cutoff)
    seen = set()
    if SEEN_FILE.exists():
        seen = set(SEEN_FILE.read_text(encoding="utf-8").splitlines())
    fresh = [(ct, u) for ct, u in links if u not in seen]
    print(f"🔗 新链接 {len(fresh)} 个（共扫 {len(links)}）")
    for ct, url in fresh:
        ts = time.strftime("%m-%d %H:%M", time.localtime(ct))
        print(f"  [{ts}] {url[:80]}")

        # 公众号文章：抓 HTML → 入库（不走视频管线）
        if "mp.weixin.qq.com" in url:
            title, body = fetch_mp_article(url)
            if not body:
                print("  ⚠️ 公众号抓取失败（可能需登录态）——已记录，不再重试")
                with open(SEEN_FILE, "a", encoding="utf-8") as f:
                    f.write(url + "\n")
                continue
            stem = hashlib.md5(url.encode()).hexdigest()[:16]
            out_md = INBOX_DIR / f"src_wechat_article_{stem}.md"
            out_md.write_text(f"# {title or url}\n\n> 来源: {url}（公众号·偶遇转发）\n\n{body[:30000]}\n", encoding="utf-8")
            print(f"  ✅ 公众号文章入库: {out_md}（{len(body)} 字）")
            with open(SEEN_FILE, "a", encoding="utf-8") as f:
                f.write(url + "\n")
            continue

        # 今日头条：区分图文文章 vs 视频
        #   文章形态：/group/<gid>/、/article/<gid>/、/isXXX/（短链）→ 直接抓正文入库
        #   视频形态：/video/<gid>/ → parse_toutiao 解析直链走视频管线
        if "toutiao.com" in url:
            if "/video/" not in url:
                title, body = fetch_toutiao_article(url)
                if not body:
                    print("  ⚠️ 头条文章抓取失败——已记录，不再重试")
                    with open(SEEN_FILE, "a", encoding="utf-8") as f:
                        f.write(url + "\n")
                    continue
                stem = hashlib.md5(url.encode()).hexdigest()[:16]
                out_md = INBOX_DIR / f"src_wechat_article_tt_{stem}.md"
                out_md.write_text(f"# {title or url}\n\n> 来源: {url}（今日头条·偶遇转发）\n\n{body[:30000]}\n", encoding="utf-8")
                print(f"  ✅ 头条文章入库: {out_md}（{len(body)} 字）")
                with open(SEEN_FILE, "a", encoding="utf-8") as f:
                    f.write(url + "\n")
                continue
            info = parse_toutiao(url)
            if not info:
                print("  ⚠️ 头条解析失败——已记录，不再重试")
                with open(SEEN_FILE, "a", encoding="utf-8") as f:
                    f.write(url + "\n")
                continue
        elif url.startswith(("http://wxapp.tc.qq.com", "https://wxapp.tc.qq.com")):
            # 卡片直链是加密视频（前 131072 字节 ISAAC），无解密密钥（仅播放时暴露）——
            # 标记 seen 跳过，提示走播放兜底，避免每次重试下载大文件
            print("  ⚠️ 卡片直链（加密视频）——需电脑播放拦截兜底，跳过（已记录）")
            with open(SEEN_FILE, "a", encoding="utf-8") as f:
                f.write(url + "\n")
            continue
        else:
            info = parse_link(url)
        if not info or not info["url"]:
            continue
        stem = hashlib.md5(url.encode()).hexdigest()[:16]
        video_file = WORK_DIR / f"{stem}.mp4"
        print(f"  ⬇️ 下载 {info['title'][:40]}（作者: {info['author']}）")
        if not download(info["url"], video_file):
            continue
        # 转写 → inbox
        wsl_v = str(video_file).replace("\\", "/")
        import re as _re
        m = _re.match(r"^([A-Za-z]):/(.*)$", wsl_v)
        wsl_v = f"/mnt/{m.group(1).lower()}/{m.group(2)}" if m else wsl_v
        out_md = INBOX_DIR / f"src_wechat_{stem}.md"
        wsl_out = str(out_md).replace("\\", "/")
        m2 = _re.match(r"^([A-Za-z]):/(.*)$", wsl_out)
        wsl_out = f"/mnt/{m2.group(1).lower()}/{m2.group(2)}" if m2 else wsl_out
        cmd = ["wsl", "-e", "bash", "-c", f"python3 /home/dministrator/wechat-collect/transcribe.py \"{wsl_v}\" \"{wsl_out}\""]
        r = subprocess.run(cmd, capture_output=True, timeout=600)
        if r.returncode == 0 and out_md.exists():
            print(f"  ✅ 转写完成: {out_md}")
            # 知识化
            kscript = WIKI / "kdo-tools" / "wechat_knowledge.py"
            subprocess.run([sys.executable, str(kscript), str(out_md)], capture_output=True, timeout=300)
            print(f"  ✅ 知识化完成 -> {INBOX_DIR / 'knowledge'}")
            # 成功才记录（失败下次重试）
            with open(SEEN_FILE, "a", encoding="utf-8") as f:
                f.write(url + "\n")
        else:
            print(f"  ⚠️ 转写失败（不记录，下次重试）: {r.stderr.decode('utf-8', errors='replace')[-150:]}")
    # 自动转正：已知识化产物入仓（10_raw/sources + 30_wiki/cases）
    pscript = Path(__file__).resolve().parent / "wechat_promote.py"
    r = subprocess.run([sys.executable, str(pscript)], capture_output=True, timeout=600)
    if r.returncode == 0:
        print("📦 自动转正完成")
    else:
        print(f"⚠️ 转正失败: {r.stderr.decode('utf-8', errors='replace')[-200:]}")
    print("🏁 本轮完成")


if __name__ == "__main__":
    main()
