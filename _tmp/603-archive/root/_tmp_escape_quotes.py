import re

with open('_tmp_fix_strategy_cases_part2.py', 'r', encoding='utf-8') as f:
    text = f.read()

def remove_inner_quotes(match):
    s = match.group(0)
    inner = s[1:-1]
    inner = inner.replace('"', '')
    return '"' + inner + '"'

pattern = re.compile(r'"(?:[^"\\]|\\.)*"')
text = pattern.sub(remove_inner_quotes, text)

with open('_tmp_fix_strategy_cases_part2.py', 'w', encoding='utf-8') as f:
    f.write(text)
print('removed inner quotes')
