import json

path_a = r'C:\Users\Administrator\Desktop\wiki\00_inbox\广冷电子\广冷001\广冷资料\广冷\立创源文件\HX-SMJ-03-A_红外光栅（主控）V2.1 修改 f27e2a3e9f83465eb13a40e7738821f1\pcb\PCB_HX-SMJ-03-A_红外光栅（主控）V2.2.json'

with open(path_a, 'r', encoding='utf-8') as f:
    data = json.load(f)

shapes = data['shape']

# Find J2 connector pin assignments
print('=== J2 连接器引脚分配 ===')
for s in shapes:
    parts = s.split('~')
    if parts[0] == 'PAD' and 'J2' in s:
        pin_num = ''
        signal = ''
        for p in parts:
            if p.replace('.','').isdigit() and len(p) < 6 and len(p) > 0:
                pin_num = p
            # Check for signal names
            if any(x in p for x in ['QD', 'SRCLK', 'RCLK', 'VDD', 'GND', 'A_', 'B_', 'C_',
                                     'IN3', 'IN4', 'XA', 'XB', 'Net-', 'EX', '5V', '3V', '24V', 'OUT']):
                signal = p
        if signal:
            print('  J2 pin %s: %s' % (pin_num, signal))

print()
print('=== QD2 在 A 板上的连接 ===')
for s in shapes:
    parts = s.split('~')
    if parts[0] == 'PAD' and 'QD2' in s:
        ref = ''
        for p in parts:
            if len(p) < 8 and p[0] in 'RUJQX' and p[1:].isdigit():
                ref = p
        x = parts[1] if len(parts) > 1 else '?'
        y = parts[2] if len(parts) > 2 else '?'
        print('  PAD %s at (%s, %s)' % (ref, x, y))

# Also check B board
path_b = r'C:\Users\Administrator\Desktop\wiki\00_inbox\广冷电子\广冷001\广冷资料\广冷\立创源文件\HX-SMJ-03-B_红外光栅（外设）V2.1 修改 copy 0db2483e21cd41ffa00c8900a511a5d6\pcb\PCB_HX-SMJ-03-B_红外光栅（外设）V2.2.json'
with open(path_b, 'r', encoding='utf-8') as f:
    data_b = json.load(f)

shapes_b = data_b['shape']
print()
print('=== B 板 J1 连接器引脚分配 ===')
for s in shapes_b:
    parts = s.split('~')
    if parts[0] == 'PAD' and 'J1' in s:
        pin_num = ''
        signal = ''
        for p in parts:
            if p.replace('.','').isdigit() and len(p) < 6 and len(p) > 0:
                pin_num = p
            if any(x in p for x in ['QD', 'SRCLK', 'RCLK', 'VDD', 'GND', 'A_', 'B_', 'C_',
                                     'IN3', 'IN4', 'XA', 'XB', 'Net-', 'EX', '5V', '3V', 'OUT']):
                signal = p
        if signal:
            print('  J1 pin %s: %s' % (pin_num, signal))

print()
print('=== QD4 在 B 板上的连接 ===')
for s in shapes_b:
    parts = s.split('~')
    if parts[0] == 'PAD' and 'QD4' in s:
        ref = ''
        for p in parts:
            if len(p) < 8 and p[0] in 'RUJQX' and p[1:].isdigit():
                ref = p
        x = parts[1] if len(parts) > 1 else '?'
        y = parts[2] if len(parts) > 2 else '?'
        print('  PAD %s at (%s, %s)' % (ref, x, y))
