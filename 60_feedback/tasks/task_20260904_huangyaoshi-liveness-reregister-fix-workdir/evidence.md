# #637 证据（2026-09-04 20:15）

- diff：`90_control/scripts/role_registry.py`（_role_liveness_struck 划销抑制闸）+ `kdo-tools/conveyor_probe.py`（_scan_gate_blocked 水位线，根治 500-cap 哈希淘汰翻滚）
- 测试：新增 test_liveness_struck_suppression_637.py（5）+ test_gate_blocked_watermark_637.py（5）全绿；两目录全量 507 passed
- 实跑：修复上线后探针 5+ 拍（18:47→20:07）新登记 0；板面未划销 liveness 回声 0 条；沙盒重扫 conveyor_state.json → 0 新记录（gate_seen_pos=612=记录总数）
- 真报警：19:02 huangyaoshi（#637 claimed 有单 + 全实例 stale）→ gate-blocked → 19:07 上板 → 通知王语嫣（生产真实事件）
- #635 核查：F-074 13:18 部署后零误报；09-03 晚空窗误报均在部署前；通知面与判定同通道（gate-blocked.log→conveyor_probe），无漏接
