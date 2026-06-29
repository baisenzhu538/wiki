import re

with open('_tmp_fix_strategy_cases_part2.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    # Match lines like:     "key": "value with inner quotes",
    # or:     "key": "value",
    m = re.match(r'^(\s*"[^"]+":\s*"(.*)"),?\s*$', line)
    if m:
        prefix = m.group(1)[:-1]  # includes opening quote, remove trailing quote
        value = m.group(2)
        value = value.replace('"', '')
        # determine if there was comma
        comma = ',' if line.rstrip().endswith(',') else ''
        new_line = prefix + value + '"' + comma + '\n'
        new_lines.append(new_line)
    else:
        new_lines.append(line)

with open('_tmp_fix_strategy_cases_part2.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
print('fixed inner quotes per line')
