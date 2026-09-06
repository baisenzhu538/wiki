# 最小建议书：generate-dashboard.py 独立 parse_queue 副本与 queue_gate 已分叉

- **现象一句话**：#647 修复 queue_gate.parse_queue 断表 bug（队列 229→241 行，#647/#648 曾整体不可见）后，`queue_transition.py` 流转触发的看板刷新仍显示「229 个任务」——generate-dashboard.py 维护着独立 parse_queue 副本，未吃到同源修复。
- **在哪发现**：2026-09-06 #647 施工时，claim 647 成功后 dashboard.html 输出行（`90_control/scripts/queue_transition.py` `_refresh_dashboard` → `kdo-tools/generate-dashboard.py`）。
- **建议方向（可选）**：generate-dashboard 改为 `from queue_gate import parse_queue`（B3 牌：先统一而非叠加），或在 #647 终审时裁定是否立项；不立则此单留痕即可。
