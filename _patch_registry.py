"""Quick patch: add CJK keywords to tag-registry.yaml for pre-screen to work on Chinese text."""
import yaml
from pathlib import Path

REGISTRY = Path(r"C:\Users\Administrator\Desktop\wiki\90_control\tag-registry.yaml")

with open(REGISTRY, "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

# CJK keywords to append to existing includes for key dimensions
CJK_PATCH = {
    "chunk_type": {
        "claim": " 主张 命题 断言 核心观点 可证伪 结论是 我认为",
        "constraint": " 边界 限制 前提 不适用 不适合 不要用 不能 做不到 条件是 只有 必须",
        "procedure": " 步骤 操作 做法 方法 流程 第1 第一 首先 然后 最后 怎么做 如何做",
        "definition": " 定义 概念 术语 是什么 指的是 含义 是指",
        "example": " 案例 实例 例如 比如 场景 举例 如 某个",
        "reference": " 来源 引用 参考 出处 详见 来自",
        "critique": " 攻击 批判 质疑 批评 挑战 反对 认为 不同 争议",
        "synthesis": " 综合 跨域 对标 整合 连接 关联 统一 归纳",
        "question": " 问题 待探索 未解 开放 不知道 疑问 困惑",
        "action_trigger": " 触发 场景 时机 当 每次 一旦 如果 就必须 在什么情况下",
        "process_data": " 过程 决策理由 修改记录 之前 之后 为什么选 改为",
        "error_data": " 错误 失败 踩坑 纠偏 事故 教训 不要 别 禁止 违规",
        "original_quote": " 原话 原文 引用 口述 逐字稿 说",
        "use_case": " 使用场景 适用场景 在什么情况下 用途",
        "operation": " 操作方法 怎么做 具体做法 执行",
        "boundary": " 适用边界 边界 反例 前提 不适用的场景",
        "why_valuable": " 为什么值钱 AI语料 独有 稀缺 护城河 没人知道",
        "cross_reference": " 关联 链接 参见 参考 相关",
        "extraction_guide": " 萃取 方法论 指南 统领 摘要",
    },
    "method_family": {
        "thinking-tool": " 思维 认知 框架 模型 思考方式 思维工具",
        "decision-framework": " 决策 ROI 评估 选择 判断 五步法 权重 评分",
        "learning-method": " 学习 方法 IPO Y模型 刻意练习 科学学习",
        "research-method": " 调研 研究 访谈 调查 分析 尽职调查",
        "product-design": " 产品设计 泛产品 MVP 用户 需求",
        "management-tool": " 管理 团队 OKR 招聘 组织 领导",
        "execution-method": " 执行 落地 实施 交付 推进",
        "evaluation-method": " 评估 审核 审计 评分 检查 检验 对标",
        "communication-method": " 表达 演讲 路演 叙事 沟通 说服",
        "prompt-engineering": " 提示词 AI协作 系统提示 LLM交互",
        "knowledge-engineering": " 知识管理 KDO wiki 知识图谱 RAG 本体",
    },
    "audience": {
        "ceo": " 老板 CEO 创始人 一号位 战略 定方向",
        "manager": " 管理 团队 负责人 主管 总监 中层",
        "executor": " 执行 操作 落地 一线 实施者",
        "designer": " 设计 视觉 审美 构图 设计师",
        "developer": " 开发 工程师 代码 API 技术",
        "beginner": " 入门 新手 零基础 第一次 初级",
        "expert": " 进阶 高级 专家 深度 资深",
        "general": " 通用 所有人 无特定",
    },
    "perspective": {
        "professional": " 专业 术语 技术 领域 行业",
        "compliance": " 合规 法律 隐私 监管 红线 版权",
        "platform-policy": " 平台 规则 违禁 限流 封号 审核",
        "roi": " ROI 成本 收益 投入产出 值不值 划算",
        "user-experience": " 体验 NPS 满意度 好用 用户感受",
    },
}

dims = data.get("dimensions", {})
for dim_name, values_patch in CJK_PATCH.items():
    if dim_name not in dims:
        continue
    dim_values = dims[dim_name].get("values", [])
    for entry in dim_values:
        val = entry.get("value", "")
        if val in values_patch:
            entry["includes"] = (entry.get("includes", "") + values_patch[val]).strip()

with open(REGISTRY, "w", encoding="utf-8") as f:
    yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)

print("✅ tag-registry.yaml patched with CJK keywords for:")
for dim, vals in CJK_PATCH.items():
    print(f"  {dim}: {len(vals)} values")
