# 实测11.78亿Token 仅92元，开源记忆系统让DeepSeekV4Pro暴降97.4%

> 来源: https://m.toutiao.com/article/7672617566786830875/?app=news_article&amp;category_new=__all__&amp;module_name=Android_tt_others&amp;share_did=MS4wLjACAAAA-i_qzLzAa-RINhYSIl4K4CkWm1oCgVQPHjDmmagTAuw&amp;share_uid=MS4wLjABAAAAR2y3T7WQuS8j2yI7_gS55ipZcg34YaYA4hY8Ldje234&amp;timestamp=1788055952&amp;tt_from=wechat&amp;upstream_biz=Android_wechat&amp;utm_campaign=client_share&amp;utm_medium=toutiao_android&amp;utm_source=wechat&amp;share_token=6c04e8c6-2919-4df9-b7ca-676915e4c822（今日头条·偶遇转发）

大模型虽强，Token成本是最大痛点。DeepSeek-V4-Pro 能力顶尖，官方定价输入 3元/百万Token、输出 6元/百万Token。常规场景下，大规模持续调用普通开发者根本扛不住。

我在 GitHub 首发了全球首款 Mnemosyne 记忆系统，全程使用 DeepSeek-V4-Pro 进行了为期一个月的实测。结果如下：

累计消耗 1,178,660,751 Token（约11.78亿） 累计消费 ¥92.08 折合百万Token仅 0.078元——成本降到原生输入价格的 2.6%，压缩率 97.4%。

原理：记忆预检索架构，而不是"把全部历史塞进模型"

市面上常见的做法是把全部历史上下文扔进模型上下文窗口，token 全额计费，成本惊人。即便是 RAG 方案，冗余载入记忆片段也是常态，通常只能做到 30%–70% 的 Token 压缩。

Mnemosyne 的做法：新请求到来时不直接投喂全部上下文给大模型，而是通过向量检索、关键词检索、记忆筛选，从长期记忆库里抽取极小一部分最相关的片段，只将这部分高度相关记忆 + 用户当前 query 送入模型。绝大多数历史对话不进入 LLM 上下文、不产生计费 Token。

关键概念：计费Token ≠ 全部历史Token

外界容易混淆两个概念：

计费Token：实际送入模型、产生账单的 Token（本次 11.78亿全部为此口径）

存储Token：系统处理和存储的全部历史对话原始 Token（不进模型不计费，远大于 11.78亿）

本次统计严格按 DeepSeek 后台计费口径计算，未做任何文字游戏。

行业横向对比

按成本压缩率来看：

原生长上下文窗口方案：0% 压缩，全额计费

基础 RAG 方案：30%–70% 压缩

高级记忆系统（分层记忆/摘要/遗忘机制）：85%–95% 压缩

Mnemosyne：97.4% 压缩

同级别使用 DeepSeek-V4-Pro 的前提下，公开渠道几乎看不到同量级压缩效果。属于第一梯队水平。

这套架构的商业价值

昂贵大模型平民化——V4-Pro 这类高端模型，大规模持续调用从此具备经济可行性；

同时解决成本和上下文窗口两个痛点——既省钱，又避免上下文过载导致的模型遗忘和速度变慢；

通用架构——不绑死 DeepSeek，可平滑迁移 GPT-4o、Claude 等更高价模型，溢价空间更大。

关于 Mnemosyne

全球唯一基于纯 Python 标准库、零外部依赖的 AI Agent 记忆引擎。单文件部署，100% 本地运行。Hindsight 14 维评分 9.58/10，LongMemEval Session Recall 85%。

 论文 Zenodo：10.5281/zenodo.21870436 源码：github.com/FrankHu-HK/mnemosyne SHA256 绑定，不可篡改实测11.78亿Token 仅92元——开源记忆系统Mnemosyne让DeepSeek-V4-Pro成本暴降97.4%
