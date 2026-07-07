import os, sys
base = os.getcwd()
specs = {
    '00_inbox/底层逻辑之一-Y模型/底层逻辑之一Y模型-口述.txt': '116,118,142,150,610-814,1214-1224,1362-1396,1452-1470,1502-1526,1544-1548,1582-1591,1656-1742,1768-1782,1838-1864,2228-2240,2252-2258,2270-2288,2390-2398,2408-2410,2564-2578,2614,2866-2868,2980-3100,3130-3144,3212-3228,3340,3412',
    '00_inbox/底层逻辑之一-Y模型/底层逻辑之一Y模型-笔记.txt': '3,11,21-28,69-77,84-85',
    '00_inbox/底层逻辑之一-Y模型/Y模型实操作业合集-七人逐步骤对标分析-段王爷.md': '9-14,23-37,41-53,57-71,75-87,91-103,107-119,123-137,141-191,195-201',
}
all_ok = True
for rel, spec in specs.items():
    path = os.path.join(base, rel)
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    bad = []
    to_check = set()
    for part in spec.split(','):
        if '-' in part:
            start, end = map(int, part.split('-'))
            to_check.add(start)
            to_check.add(end)
        else:
            to_check.add(int(part))
    for i in sorted(to_check):
        if i < 1 or i > len(lines):
            bad.append(f'L{i}: out of range (file has {len(lines)} lines)')
        elif not lines[i-1].strip():
            bad.append(f'L{i}: boundary line is empty/whitespace')
    if bad:
        all_ok = False
        print(rel)
        for b in bad:
            print(' ', b)
    else:
        print(rel, 'OK')
sys.exit(0 if all_ok else 1)
