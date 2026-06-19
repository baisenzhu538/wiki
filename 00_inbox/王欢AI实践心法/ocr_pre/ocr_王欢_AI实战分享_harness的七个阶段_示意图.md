---
source_id: "src_ocr_王欢_AI实战分享_harness的七个阶段_示意图"
kind: image_ocr
captured_at: "2026-06-19T08:43:06.694"
original_image: "00_inbox/王欢AI实践心法/王欢-AI实战分享-harness的七个阶段-示意图.png"
ocr_engine: rapidocr
char_count: 854
trust_level: medium
---

# OCR: 王欢-AI实战分享-harness的七个阶段-示意图

原图: `00_inbox/王欢AI实践心法/王欢-AI实战分享-harness的七个阶段-示意图.png`

## OCR 原文

七个阶段，从规划到交付
Harness把一次构建分解为严格定义的阶段，每个阶段有明确的输入、输出和质量门控。
PHASE 0
初始化&预检
创建harness/目录、检测CLI工具、生成budget.ymL（默认：50轮选代，8个Sprint，4小时墙时）。自动检测是否需要从checkpoint
恢复。
PHASE 1
Planner:产品规划（Opus模型）
用最强推理模型做产品规划—只跑一次，成本可控。输出product-spec.md（功能优先级、审美方向、送代计划），同时标出所有高风险歧
义等待解决。
PHASE 1.5
TechStackSelector：技术栈选型（Opus模型）
Planner结束后立即确定技术栈。输出tech-stack.md一语言、框架、测试工具、构建工具、部署目标、选型理由。Generator不得自行引l入
未列出的顶层依赖。
PHASE2-5（循环)
Sprint对抗循环
每轮Sprint：写Sprint Contract→启动Workflow→Generator构建→四个Evaluator并行评分→决策引擎判断是继续、修复、还是裁剪范
围。
评分通过条件：没有维度低于3分、加权平均≥4.0分（取两个代码审查者中更严那个）、零CRITICAL对抗发现。
PHASE 5.5
PolishSprint:审美精修
所有PO功能完成后，自动插入一轮PolishSprint：空状态、错误状态、加载动画、字体节奏、微交互。评分权重自动切换（审美维度上调到
3，功能维度下调到1）。
PHASE 6
ShipPipeline：最终交付
顺序执行，每步互为门控：
①AestheticReviewer（Opus）整体审美评分≥4.0才过
②文档生成器写README+CHANGELOG+KNOWN_LIMITATIONS并提交
③FreshCloneTester从零克隆、按README操作，确认真的能跑
④AuditTrail生成从spec到ship的完整旅程记录

## 备注

- 本文件由 RapidOCR 自动提取，可能存在误识
- 视觉结构信息未在 OCR 中体现，需结合原图理解
