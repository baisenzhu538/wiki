# 最小建议书：todos/wangyuyan.md 含非法 UTF-8 字节导致 Read 工具拒读

- **现象**：`90_control/todos/wangyuyan.md` 在字节偏移 112612 处有非法 UTF-8 序列（0xe6 无续字节），Read 工具整体拒读报 "not valid UTF-8 or UTF-16"，只能走 python errors=replace 绕过。
- **在哪发现**：2026-09-10 18:34 值守拍第①步"读 todos/wangyuyan.md 未读段"时。
- **建议方向**：黄药师跑一次性修复脚本（定位偏移 112612 附近的坏字节、按 GBK/替换符修复为合法 UTF-8），修复前各角色读该文件需用 python 兜底；写入不受影响（append 正常）。
