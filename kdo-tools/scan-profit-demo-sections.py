#!/usr/bin/env python3
"""扫描利润为王口述稿，标记信号词段落（高价值可复用内容）。"""
import re, sys, os

SIGNAL_WORDS = [
    "我给你演示", "举个例子", "这是我真实的", "我给你们看",
    "你们感受一下", "准备好", "惊喜来了", "来，我现场",
    "实操中", "我们有一个学员", "之前有一个", "比如",
    "举个例子来说", "失败的原因是", "关键是什么",
    "为什么？", "怎么做的", "本质是什么", "核心问题",
    "最关键的", "最容易犯的", "很多人不知道",
    "千万不要", "反直觉", "反常识", "注意这个细节",
    "重点来了",
]

def scan_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    output = []
    output.append(f"## 扫描：{os.path.basename(filepath)}（共 {len(lines)} 行）\n")
    
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if not stripped:
            continue
        # 检查是否含信号词
        for word in SIGNAL_WORDS:
            if word in stripped:
                # 取前后3行上下文
                start = max(0, i-4)
                end = min(len(lines), i+3)
                output.append(f"\n### L{i} [信号词: {word}]\n")
                for j in range(start, end):
                    prefix = "▶ " if j+1 == i else "  "
                    output.append(f"{prefix}L{j+1}: {lines[j].rstrip()}")
                break
    
    output.append(f"\n---\n共命中 {len(output)-2} 个信号段落\n")
    return "\n".join(output)

if __name__ == "__main__":
    base = "/mnt/c/Users/Administrator/Desktop/wiki/00_inbox/利润为王/"
    files = [
        "经营课：利润认知与企业生存-口述.txt",
        "企业利润经营分析_智能优化.txt",
    ]
    for fname in files:
        path = os.path.join(base, fname)
        if os.path.exists(path):
            print(scan_file(path))
