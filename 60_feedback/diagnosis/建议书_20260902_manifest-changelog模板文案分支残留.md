# 建议书：manifest 生成器 changelog 文案需随 adapted_from 分支切换（#597 终审发现）

- **现象**：`40_outputs/capabilities/skills/shared/research/manifest.yaml` 的 changelog 文案写「无来源卡 adapted_from=null 待复核」，但该 manifest 的 `adapted_from` 实际已填 `business-research-skill-oscar-13-weapon-system`——生成器（`_tmp/gen_manifests_597.py`）模板文案对所有 72 个 manifest 用同一句，未随非 null 分支切换，文案与字段自相矛盾。
- **在哪发现**：#597 终审（2026-09-02，欧阳锋 CLI 实例）触发词质量抽样时。
- **建议方向**：下批补 manifest（或 skills-assistant 顺手单）修该条 changelog 文案使其与 adapted_from 实值一致；生成器模板加分支判断。字段本身正确，纯注释文案瑕疵，不阻断。
