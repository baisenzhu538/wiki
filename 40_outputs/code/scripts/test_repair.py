import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

content = open('00_inbox/战略专题/冉鹏PPT截图/引擎点火20260110 战略破局（冉鹏）(1)_16_vlm_desc.md', 'r', encoding='utf-8').read()
fences = list(re.finditer(r"```(?:json)?\s*\n?(.*?)```", content, re.DOTALL))
candidate = fences[0].group(1).strip()

def fix_unescaped_quotes(text):
    """Escape unescaped double quotes inside JSON string values."""
    result = []
    i = 0
    n = len(text)
    in_string = False
    while i < n:
        ch = text[i]
        if ch == '\\' and i + 1 < n:
            result.append(ch)
            result.append(text[i+1])
            i += 2
            continue
        if ch == '"':
            if not in_string:
                in_string = True
                result.append(ch)
            else:
                # Check if this looks like a string-ending quote
                j = i + 1
                while j < n and text[j] in ' \t\n\r':
                    j += 1
                if j >= n or text[j] in ',:}\]':
                    in_string = False
                    result.append(ch)
                else:
                    result.append('\\"')
            i += 1
        else:
            result.append(ch)
            i += 1
    return ''.join(result)

fixed = fix_unescaped_quotes(candidate)

try:
    parsed = json.loads(fixed)
    print('json success:', parsed.get('category'), parsed.get('title'))
except Exception as e:
    print('json failed:', e)
    try:
        json.loads(fixed)
    except json.JSONDecodeError as je:
        print(f'Error at line {je.lineno}, col {je.colno}')
        line = fixed.split('\n')[je.lineno - 1]
        print('Line:', line)
        print('Around:', line[max(0, je.colno-20):je.colno+20])
