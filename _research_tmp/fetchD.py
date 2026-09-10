# -*- coding: utf-8 -*-
"""Deep-fetch key pages from outD/outA searches using so360 session resolver."""
import sys, json, time, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, r"C:\Users\Administrator\Desktop\wiki\_research_tmp")
import so360_pipeline as P

targets = [
    ("mkt_share_21", "https://www.360kuai.com/pc/954f89e098e220dbc?cota=3&kuai_so=1&sign=360_57c3bbd1&refer_scene=so_1"),
    ("track_3500yi", "https://www.360kuai.com/pc/99774323954540f6b?cota=3&kuai_so=1&sign=360_57c3bbd1&refer_scene=so_1"),
    ("yaoshibang_pricing_right", "https://www.360kuai.com/pc/9674198c1759f51e1?cota=3&kuai_so=1&sign=360_57c3bbd1&refer"),
    ("erp_rank", "https://www.so.com/link?m=b5zNt44ozXzaeZFM2tb5sLg6nP4qsiX5WDlce8g5CLJeBgnoLDHinK9%2BlyxpKz"),
    ("changjietong_price", "https://www.so.com/link?m=brrLiCNhg8Hh8SyrYqenBdIyFhgy%2FpPyncT7wZ7Fmz3JfJMNe8Mlt2%2FIktTr"),
    ("tangruan_price", "https://www.so.com/link?m=uX%2F%2Br9rJJ%2FizmGFUUXMPJVXxEsbM3wv1J1EwCs3mvKdBUSyuPOa18WNwzo"),
    ("youzan_price", "https://www.so.com/link?m=zYkvX956NkS1LpoYLN3tN6wHd%2FJilwHdXErsXBMHs11TWLdjytqKPTT3%2Bdhg"),
    ("wangyi_close_100k", "https://www.so.com/link?m=ujnp%2BR92lK9v8PkA%2B33USM5i0Px3leD7js2sTHXeKM9bbAfW3zu1eL1iS%2F"),
    ("yiyigou_fund", "https://www.so.com/link?m=zu6qQIqbI%2F5w94aETR2gyRaNK%2FI9Kd1OXwvOH6ECIcNOCeczHCVWkLG"),
    ("yiyigou_loss_fix", "https://www.so.com/link?m=z4neNz8QSzDsCBMLBBcgP%2FG3qpVnGcLXYD0TQ0Rmqyp1j%2FO4rH%2FLY"),
    ("chuangye_frontline", "https://www.so.com/link?m=zRR6z%2BJHfqmg5qFqDeVjoyKG7Llcw0VG3Hfb3zPW0IO5XS%2BAw05WVuR"),
    ("huauling_funding", "https://www.so.com/link?m=evCbxu412mC1qWmh%2FDKUaX5wiGQF0ZQyGaSzVE0NAcHjPd8B4iRQMDpjeYYOuj"),
]
out = {}
for tid, u in targets:
    try:
        real, text = P.resolve_fetch(u)
        out[tid] = {"url": real, "text": text}
        print(f"{tid}: len={len(text)} {real[:100]}", flush=True)
    except Exception as e:
        out[tid] = {"url": u, "error": str(e)[:120]}
        print(f"{tid}: ERR {e}", flush=True)
    time.sleep(1.5)
json.dump(out, open(r"C:\Users\Administrator\Desktop\wiki\_research_tmp\deepD.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("saved deepD.json")
