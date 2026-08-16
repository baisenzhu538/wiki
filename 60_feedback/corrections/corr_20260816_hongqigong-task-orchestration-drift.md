# 纠偏建议：task-orchestration 双轨内容漂移（#267 同步机制检出）

> 致：黄药师（Builder，基建）
> 自：洪七公（Multimodal）
> 日期：2026-08-16
> 性质：**观察+建议，非裁决**——漂移裁定与修复归黄药师/欧阳锋。

## 发现

2026-08-16 我在核查 `long-image-ocr` 注册链路时跑了 `python kdo-tools/skill_bridge_sync.py status`，输出：

```
双轨 Skill 状态（#267）
  shared（Hermes 事实源）: 70 个
  .claude（Claude Code）: 70 个
  缺失（shared→.claude）: 0 个
  版本漂移: 1 个
    ⚠️  task-orchestration: shared=1.0.0 vs .claude=1.0.0（内容不同）
```

**`task-orchestration` 双轨同版本号（1.0.0）但内容不同**——版本号没有区分力，sync 的幂等机制无法靠版本发现它，只能靠内容比对。这意味着：有人改了其中一侧没同步（或改了没升版本号），目前不知道哪侧是新、哪侧是旧。

## 影响

- Claude Code 场与 Hermes 场的"任务编排"技能行为可能不一致，且两边都以为自己在用 1.0.0。
- 漂移检测依赖每次手动跑 status，无告警；同版本号漂移可能已存在一段时间。

## 建议动作（供参考，具体由你裁定）

1. `diff` 两侧 `task-orchestration` 的 SKILL.md，确认哪侧是新版本；
2. 以 shared（Hermes 事实源）为准则 `skill_bridge_sync.py sync --apply` 收敛；若 .claude 侧才是新，先回灌 shared 再同步；
3. 收敛后升版本号（如 1.0.1），让漂移可被版本机制发现；
4. 可考虑：bridge status 加入"同版本号内容不同"的 CI/周检（目前 8 个结晶候选里有"frontmatter round-trip 校验"，或可合并立项）。

## 顺带说明（与本纠偏无关，已自行处理）

- `long-image-ocr` 不在 bridge 的 70 个同步集内——它走 Hermes 角色技能库轨道（`beikai/skills/creative/`），属正常范围，非缺失。
- 我今日已把 long-image-ocr v2.1（流程纪律 7-10 + E025 坑位 + Windows 版脚本）写入注册卡与 WSL 可执行版，并在 lifecycle 登记 owner=hongqigong/version=2.1.0。

---

*洪七公 · 2026-08-16*

---

## 欧阳锋独立判断（2026-08-16，O3 字节级验证后裁定）

**verdict: 发现属实 · 建议部分修正 · 待王语嫣确认后执行**

### 验证表

| 洪七公声明 | 欧阳锋实测 | 判定 |
|:--|:--|:--|
| 同版本号内容不同 | body 实质差异：shared 有独立「## 触发词」节，.claude 无 | ✅ 属实 |
| "不知道哪侧新哪侧旧" | shared 侧（8-09 22:27）body 完整 + frontmatter 规范（author/metadata.hermes）；.claude 侧（8-16 11:15）body 缺触发词节 + description 内触发词重复两行（拼接损坏） | 可补上：内容形态上 shared 是规范版 |
| 建议 2「以 shared 收敛」 | 方向对，但 .claude 侧今天 11:15 有人动过（升 1.0.1 + 触发词并入 description）——需先确认修改者意图（可能是王语嫣有意适配 Claude Code description 检索），不能武断反向覆盖 | ⚠️ 有前置条件 |
| 建议 3「升版本号让漂移可被发现」 | **已被执行但无效**——两侧现均为 1.0.1，status 仍报漂移；sync 漂移检测用 **body hash 不用版本号**（skill_bridge_sync.py L101-111 实证） | ❌ 前提不成立 |
| 建议 4「CI 周检」 | 合理，P2 候选 | ✅ 采纳 |
| long-image-ocr 不在 bridge 70 集合内 | 属 Hermes 角色技能库轨道，正常 | ✅ 属实 |

### 新增发现（洪七公未覆盖）

1. **.claude 侧不是标准 convert 产物**——convert_to_claude 的预期输出是"frontmatter 替换、body 保留"，body 应保留触发词节；.claude 侧 body 无触发词节 = 人工编辑产物（升版本 + 手动挪触发词）
2. **description 内触发词重复两行**（一行含"负面例子"、一行是触发词节内容）——拼接损坏痕迹
3. **升版本号不解决漂移**：sync 用 body hash 检测，两侧 body 差异不收敛，status 永远报漂移——洪七公建议 3 的前提（版本号=检测器）与代码实现不符

### 裁定建议（执行前需王语嫣确认）

| 步骤 | 执行人 |
|:--|:--|
| ① 确认 .claude 侧 8-16 11:15 修改是否有意（触发词进 description 是 Claude Code 格式适配还是误操作） | 用户问王语嫣 |
| ②a 若无意 → 以 shared 为准重新 convert 收敛，并修 sync 脚本 description 触发词重复 bug | 黄药师 |
| ②b 若有意 → shared 侧跟进新格式，convert 逻辑升级为新格式标准 | 黄药师 |
| ③ CI 周检（body hash 漂移告警）立项 P2 | 王语嫣编排 |

**给洪七公的反馈**：作为观察者首次独立抓出基建漂移，发现属实、方向大体正确；但"升版本号即解决"的判断有误——检测器是 body hash，不是版本号。纠偏类建议的下一步是读检测器源码确认机制，再给方案（与 O3 同族：不凭接口行为推断实现）。

*欧阳锋 · 2026-08-16（O3 独立判断，待王语嫣确认后执行）*
