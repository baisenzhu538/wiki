# KDO 卡片质量门禁报告

**扫描时间**：2026-06-15  
**扫描范围**：30_wiki 全库 1192 张卡片  
**P0 阻塞问题卡片**：13 张  
**P1 修复问题卡片**：1 张  
**完全干净卡片**：1178 张  
**YAML 解析错误**：13 张  

---

## P0 阻塞问题清单

| 文件 | P0 问题 |
|---|---|
| `concept-card-index-latest.md` | YAML 解析错误: None |
| `concepts\skill-ai-four-elements-validation.md` | YAML 解析错误: while scanning a block scalar
  in "<unicode string>", line 37, column 1:
    > **来源**：纪浩（AI俱乐部-AI协作方法论-口述）
    ^
expected a comment or a line break, but found '*'
  in "<unicode string>", line 37, column 3:
    > **来源**：纪浩（AI俱乐部-AI协作方法论-口述）
      ^ |
| `concepts\skill-ai-info-literacy-three-layer.md` | YAML 解析错误: while scanning a block scalar
  in "<unicode string>", line 38, column 1:
    > **来源**：基于 master-ai-info-liter ... 
    ^
expected a comment or a line break, but found '*'
  in "<unicode string>", line 38, column 3:
    > **来源**：基于 master-ai-info-literac ... 
      ^ |
| `concepts\skill-ai-landing-five-steps.md` | YAML 解析错误: while scanning a block scalar
  in "<unicode string>", line 38, column 1:
    > **来源**：马易（AI俱乐部-AI落地场景识别-口述）
    ^
expected a comment or a line break, but found '*'
  in "<unicode string>", line 38, column 3:
    > **来源**：马易（AI俱乐部-AI落地场景识别-口述）
      ^ |
| `concepts\skill-ai-problem-question-check.md` | YAML 解析错误: while scanning a block scalar
  in "<unicode string>", line 35, column 1:
    > **来源**：纪浩（AI俱乐部-AI协作方法论-口述）
    ^
expected a comment or a line break, but found '*'
  in "<unicode string>", line 35, column 3:
    > **来源**：纪浩（AI俱乐部-AI协作方法论-口述）
      ^ |
| `concepts\skill-ai-research-five-steps.md` | YAML 解析错误: while scanning a block scalar
  in "<unicode string>", line 37, column 1:
    > **来源**：半肥猫（AI俱乐部-AI学习落地-口述）
    ^
expected a comment or a line break, but found '*'
  in "<unicode string>", line 37, column 3:
    > **来源**：半肥猫（AI俱乐部-AI学习落地-口述）
      ^ |
| `concepts\skill-ai-scene-four-elements.md` | YAML 解析错误: while scanning a block scalar
  in "<unicode string>", line 37, column 1:
    > **来源**：马易（AI俱乐部-AI落地场景识别-口述）
    ^
expected a comment or a line break, but found '*'
  in "<unicode string>", line 37, column 3:
    > **来源**：马易（AI俱乐部-AI落地场景识别-口述）
      ^ |
| `concepts\skill-cognitive-bias-12-check.md` | YAML 解析错误: while scanning a block scalar
  in "<unicode string>", line 37, column 1:
    > **来源**：基于 master-cognitive-bia ... 
    ^
expected a comment or a line break, but found '*'
  in "<unicode string>", line 37, column 3:
    > **来源**：基于 master-cognitive-bias- ... 
      ^ |
| `concepts\skill-decision-delay-intuition.md` | YAML 解析错误: while scanning a block scalar
  in "<unicode string>", line 39, column 1:
    > **来源**：基于 master-decision-hygi ... 
    ^
expected a comment or a line break, but found '*'
  in "<unicode string>", line 39, column 3:
    > **来源**：基于 master-decision-hygien ... 
      ^ |
| `concepts\skill-decision-outside-view.md` | YAML 解析错误: while scanning a block scalar
  in "<unicode string>", line 34, column 1:
    > **来源**：基于 master-decision-hygi ... 
    ^
expected a comment or a line break, but found '*'
  in "<unicode string>", line 34, column 3:
    > **来源**：基于 master-decision-hygien ... 
      ^ |
| `concepts\skill-first-principles-assumption-classify.md` | YAML 解析错误: while scanning a block scalar
  in "<unicode string>", line 36, column 1:
    > **来源**：基于 master-first-princip ... 
    ^
expected a comment or a line break, but found '*'
  in "<unicode string>", line 36, column 3:
    > **来源**：基于 master-first-principle ... 
      ^ |
| `concepts\skill-半肥猫-ai-research-validation.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 39, column 1:
    半肥猫在AI俱乐部分享中说："我觉得AI给的回答越丝滑，问题越大 ... 
    ^
could not find expected ':'
  in "<unicode string>", line 41, column 1:
    本技能将半肥猫在调研纠偏中的实践沉淀为一套可复用的结构化流程。
    ^ |
| `concepts\skill-半肥猫-course-to-skill-workflow.md` | YAML 解析错误: while scanning a simple key
  in "<unicode string>", line 39, column 1:
    半肥猫在AI俱乐部分享中说："我最近在做的一件事情就是试图把一堂 ... 
    ^
could not find expected ':'
  in "<unicode string>", line 41, column 1:
    本技能将半肥猫的课程转Skill实践沉淀为一套可复用的八步工作流。
    ^ |

---

## P1 修复问题清单

| 文件 | P1 问题 |
|---|---|
| `tools\mineru-pdf-parsing-setup.md` | dangling 链接: paddle-ocr-setup; confidence=0.95 但 source 仅 1 个; trust_level=high 但 source 仅 1 个 |

---

## 使用说明

运行门禁脚本：
```bash
python 90_control/scripts/kcard-quality-gate.py
```

P0 问题必须在卡片进入 enriched/reviewed/stable 前修复。
P1 问题应在发布前修复。