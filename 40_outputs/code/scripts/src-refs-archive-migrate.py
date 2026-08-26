# -*- coding: utf-8 -*-
"""#557 批次A迁移：00_inbox 死引原稿 → 10_raw/sources/<主题子目录>/，全库引用同步改写。

安全设计：
- 只改 frontmatter 区域（---...--- 之间），正文不动
- 行级改写：仅当某行剥锚后路径命中映射表才重建该行
- 锚点规范化：` L3018-L3400`→`:3018-3400`，`#L187-L325`→`:187-325`，` - src_unknown` 后缀剥除
- inline-list 形式 source_refs（`source_refs: [...]`）不碰，记入 skips
- dry-run 默认开；--apply 才动手（git mv + 文件改写）
"""
import json, re, sys, subprocess, glob
from pathlib import Path
from collections import defaultdict

WIKI = Path('.')
ANCHOR = re.compile(r'(?:\s+L(\d+)(?:-L(\d+))?|\s*#L(\d+)(?:-L(\d+))?|\s+-\s+src_unknown)+$')
LINE_L = re.compile(r'\s+L(\d+)(?:-L(\d+))?$')
LINE_H = re.compile(r'\s*#L(\d+)(?:-L(\d+))?$')

SLUG = {
    'Handle the business': 'handle-the-business',
    'Case study': 'case-study',
    '销售专题': 'sales',
    'Manage the team': 'manage-the-team',
    '多模态输出': 'multimodal-output',
    '五步法之需求分析': 'demand-analysis',
    '关键假设C-拆解业务公式': 'key-assumptions',
    '利润为王': 'profit-first',
    '解放思想探索营': 'thought-liberation',
    'AI前哨站第2集': 'ai-outpost-ep2',
    '战略专题': 'strategy',
    '半肥猫开放麦-AI知识库': 'banfeimao-openmic',
    '半肥猫月白老朱线下聚会': 'banfeimao-offline',
    'Advanced modeling': 'advanced-modeling',
    'AI-study': 'ai-study',
    '半肥猫': 'banfeimao',
    '个人-深度复盘': 'personal-review',
    '人机协作双三角': 'human-ai-dual-triangle',
    '一堂五步法': 'yitang-five-step',
    '一堂五步法之增长': 'yitang-five-step-growth',
    '调研专题': 'research-topics',
}
ROOT_FILE_SLUG = 'yitang-lectures'

def strip_anchor(ref):
    """剥三种锚，返回 (纯路径, 锚列表)。锚列表=['280-282','392-394',...]（已去 L 前缀），无锚=[]"""
    s = ref
    # src_unknown 污染后缀（可多个）
    s = re.sub(r'(\s+-\s+src_unknown)+$', '', s)
    anchors = []
    m = re.search(r'[\s#]L?(\d+(?:-L?\d+)?(?:,L?\d+(?:-L?\d+)?)*)$', s)
    if m:
        seg = m.group(1)
        s = s[:m.start()]
        for rng in seg.split(','):
            rng = rng.replace('L', '')  # L280-L282 / 280-282 / L280 统一为 280-282
            anchors.append(rng)
    return s, anchors

def load_mapping():
    d = json.load(open('60_feedback/analysis/source-refs-health-latest.json', encoding='utf-8'))
    files = set()
    for c in d['missing_source_cards']:
        for ref in c['missing']:
            r = ref.replace('\\', '/').lstrip('./')
            if r.startswith('00_inbox'):
                p, _ = strip_anchor(r)
                if Path(p).exists():
                    files.add(p)
    mapping = {}
    for p in sorted(files):
        parts = p.split('/')
        sub = parts[1] if len(parts) > 2 else None
        if sub is None:
            slug = ROOT_FILE_SLUG
            rel = parts[-1]
        else:
            slug = SLUG.get(sub)
            if slug is None:
                slug = 'UNMAPPED'
            rel = '/'.join(parts[2:])  # 保留主题下的子目录层级，防同名文件碰撞
        mapping[p] = f'10_raw/sources/{slug}/{rel}'
    return mapping

def main():
    apply = '--apply' in sys.argv
    only = None
    for a in sys.argv[1:]:
        if a.startswith('--only='):
            only = a.split('=', 1)[1]
    mapping = load_mapping()
    if only:
        mapping = {k: v for k, v in mapping.items() if k.split('/')[1] == only or (only == 'ROOT' and len(k.split('/')) == 2)}
    unmapped = [k for k, v in mapping.items() if 'UNMAPPED' in v]
    collisions = [v for v in mapping.values() if list(mapping.values()).count(v) > 1]
    target_exists = [v for v in mapping.values() if Path(v).exists()]

    # 全库引用扫描
    rewrites = defaultdict(list)  # card -> [(old_line, new_line)]
    skips = []
    for cf in glob.glob('30_wiki/**/*.md', recursive=True):
        txt = Path(cf).read_text(encoding='utf-8', errors='ignore')
        if not txt.startswith('---'):
            continue
        end = txt.find('\n---', 3)
        if end == -1:
            continue
        fm_text = txt[:end]
        if re.search(r'^source_refs:\s*\[', fm_text, re.M):
            if any(old in fm_text for old in mapping):
                skips.append(cf)
            continue
        for line in fm_text.splitlines():
            ls = line.strip()
            if not ls.startswith('- '):
                continue
            ref = ls[2:].strip().strip("'").strip('"')
            p, anchors = strip_anchor(ref.replace('\\', '/').lstrip('./'))
            if p in mapping:
                indent = re.match(r'^(\s*)', line).group(1)
                # 多区间锚 → 拆成多行（每行单锚，checker 可识别；信息零丢失）
                new_lines = [f'{indent}- {mapping[p]}:{a}' for a in anchors] or [f'{indent}- {mapping[p]}']
                rewrites[cf].append((line, new_lines))

    n_cards = len(rewrites)
    n_refs = sum(len(v) for v in rewrites.values())
    print(f'mapping={len(mapping)} files | rewrite_cards={n_cards} | rewrite_refs={n_refs}')
    if unmapped:
        print('UNMAPPED subdirs:', [k.split('/')[1] for k in unmapped])
    if collisions:
        print('COLLISIONS:', collisions)
    if target_exists:
        print('TARGET EXISTS (would clash):', target_exists)
    if skips:
        print('SKIPS (inline-list source_refs):', len(skips))
    # 落机读 TSV
    mode = 'apply' if apply else 'dryrun'
    with open(f'_tmp_557_map_{mode}.tsv', 'w', encoding='utf-8') as f:
        for old, new in sorted(mapping.items()):
            f.write(f'{old}\t{new}\n')
    with open(f'_tmp_557_rewrites_{mode}.tsv', 'w', encoding='utf-8') as f:
        for cf, pairs in sorted(rewrites.items()):
            for old_l, new_ls in pairs:
                f.write(f'{cf}\t{old_l.strip()}\t{" || ".join(new_ls)}\n')

    if not apply or unmapped or collisions or target_exists:
        if apply:
            print('ABORT: 存在 UNMAPPED/COLLISION/目标已存在，未执行')
        return

    # ---- apply ----
    moved = 0
    for old, new in sorted(mapping.items()):
        Path(new).parent.mkdir(parents=True, exist_ok=True)
        r = subprocess.run(['git', 'mv', old, new], capture_output=True, text=True)
        if r.returncode != 0:
            print(f'GIT MV FAIL: {old} -> {new}: {r.stderr.strip()[:120]}')
        else:
            moved += 1
    print(f'git mv: {moved}/{len(mapping)}')

    changed = 0
    bad = []
    import yaml
    for cf, pairs in rewrites.items():
        p = Path(cf)
        txt = p.read_text(encoding='utf-8')
        end = txt.find('\n---', 3)
        fm_text = txt[:end]
        for old_l, new_ls in pairs:
            if old_l not in fm_text:
                bad.append((cf, old_l[:60]))
                continue
            fm_text = fm_text.replace(old_l, '\n'.join(new_ls), 1)
        new_txt = fm_text + txt[end:]
        # 验证：frontmatter 可解析
        try:
            yaml.safe_load(new_txt.split('---')[1])
        except Exception as e:
            bad.append((cf, f'YAML FAIL {e}'))
            continue
        p.write_text(new_txt, encoding='utf-8')
        changed += 1
    print(f'cards rewritten: {changed}/{n_cards}; problems: {len(bad)}')
    for b in bad[:10]:
        print('  BAD:', b)

if __name__ == '__main__':
    main()
