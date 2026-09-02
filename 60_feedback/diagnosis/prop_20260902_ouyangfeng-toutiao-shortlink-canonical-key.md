# 最小建议书：头条 is 短链 canonical_key 未跟随 302，同文不同短链码会重复采集

- **现象**：`kdo-tools/wechat_link_monitor.py` canonical_key() 对 toutiao 仅识别 `/video|group|article/<gid>` 形态；is 短链（isXXX / is/XXX）落到 `return u` 原样分支。同一篇文章经头条两次分享产生不同短链码（如 is/AAA/ 与 is/BBB/），canonical_key 不同 → 重复采集落 inbox。
- **在哪发现**：2026-09-02 #621 终审（头条短链正则修复），复核 seen 登记口径时确认 seen_links.txt L34 只能记原样短链 URL。
- **建议方向（可选）**：fetch_toutiao_article 已跟随 302 拿到 gid，可把解析出的 gid 回填为 seen 键（tt:<gid>），与 group/article 形态同口径去重；优先级低，非阻塞。
