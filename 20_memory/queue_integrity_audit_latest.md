# 队列完整性审计报告

- 审计范围: `C:\Users\Administrator\Desktop\wiki\60_feedback\tasks`
- reviewed 任务单总数: 109
- 任务单元数据异常数: 32
- 队列/任务单状态不一致数: 25

## 任务单元数据异常列表（缺 review_date / reviewer / review 文件）
- `task_20260627_laowantong-deliberate-practice-cards`: reviewed 但缺少 review_date
- `task_20260627_laowantong-deliberate-practice-cards`: reviewed 但缺少 reviewer/reviewed_by
- `task_20260627_laowantong-deliberate-practice-cards`: reviewed 但无对应 review/audit 文件且无 review_date
- `task_20260627_laowantong-lanyi-panproduct-organization`: reviewed 但缺少 review_date
- `task_20260627_laowantong-lanyi-panproduct-organization`: reviewed 但缺少 reviewer/reviewed_by
- `task_20260627_laowantong-lanyi-panproduct-organization`: reviewed 但无对应 review/audit 文件且无 review_date
- `task_20260628_laowantong-case-section-standardization`: reviewed 但缺少 review_date
- `task_20260628_laowantong-case-section-standardization`: reviewed 但缺少 reviewer/reviewed_by
- `task_20260628_laowantong-case-section-standardization`: reviewed 但无对应 review/audit 文件且无 review_date
- `task_20260628_laowantong-dark-knowledges-batch8`: reviewed 但缺少 review_date
- `task_20260628_laowantong-dark-knowledges-batch8`: reviewed 但缺少 reviewer/reviewed_by
- `task_20260628_laowantong-dark-knowledges-batch8`: reviewed 但无对应 review/audit 文件且无 review_date
- `task_20260628_laowantong-link-repair-b1-frontmatter-related`: reviewed 但缺少 review_date
- `task_20260628_laowantong-link-repair-b1-frontmatter-related`: reviewed 但无对应 review/audit 文件且无 review_date
- `task_20260628_laowantong-link-repair-b2-synthesis-section`: reviewed 但缺少 review_date
- `task_20260628_laowantong-link-repair-b2-synthesis-section`: reviewed 但无对应 review/audit 文件且无 review_date
- `task_20260628_laowantong-link-repair-b3-island-cards`: reviewed 但缺少 review_date
- `task_20260628_laowantong-link-repair-b3-island-cards`: reviewed 但无对应 review/audit 文件且无 review_date
- `task_20260628_wangyuyan-wave6-blindspot-diagnosis`: reviewed 但缺少 review_date
- `task_20260628_wangyuyan-wave6-blindspot-diagnosis`: reviewed 但无对应 review/audit 文件且无 review_date
- `task_20260629_kimi-lint-mechanical-noise-reduction`: reviewed 但缺少 review_date
- `task_20260629_kimi-lint-mechanical-noise-reduction`: reviewed 但无对应 review/audit 文件且无 review_date
- `task_20260629_laowantong-expand-ai-learning-concept-cards`: reviewed 但缺少 review_date
- `task_20260629_laowantong-expand-ai-learning-concept-cards`: reviewed 但缺少 reviewer/reviewed_by
- `task_20260629_laowantong-expand-ai-learning-concept-cards`: reviewed 但无对应 review/audit 文件且无 review_date
- `task_20260629_wangyuyan-goat-milk-channel-partnership-bridge`: reviewed 但缺少 review_date
- `task_20260629_wangyuyan-goat-milk-channel-partnership-bridge`: reviewed 但无对应 review/audit 文件且无 review_date
- `task_20260701_wobeirushen-validation`: reviewed 但缺少 review_date
- `task_20260701_wobeirushen-validation`: reviewed 但无对应 review/audit 文件且无 review_date
- `task_20260703_huangyaoshi-agent-prompt-compiler-report`: reviewed 但缺少 review_date
- `task_20260703_huangyaoshi-agent-prompt-compiler-report`: reviewed 但无对应 review/audit 文件且无 review_date
- `task_20260704_wangyuyan-agent-card-skill-execution-pattern`: reviewed 但 reviewed_by='pending' 不合法

## 队列/任务单状态不一致（双向）
### 任务单已 reviewed，但队列未 reviewed
- `task_20260704_wangyuyan-patch-canvas-risk-judgment`: 任务单 status=reviewed，但队列 status=done
### 队列已 reviewed，但任务单未 reviewed
- `task_20260701_wangyuyan-time-management-domain-orchestration`: 队列 status=reviewed 但任务单 status=closed_merged
- `task_20260703_laowantong-yitang-Y-model-os`: 队列 marked reviewed 但任务单文件不存在
- `task_20260703_huangyaoshi-agent-prompt-compiler`: 队列 status=reviewed 但任务单 status=queued
- `task_20260704_wangyuyan-agent-self-flywheel-review`: 队列 status=reviewed 但任务单 status=queued
- `task_20260705_huangyaoshi-lint-warning-infra`: 队列 status=reviewed 但任务单 status=queued
- `task_20260707_wangyuyan-project-management-domain-production`: 队列 marked reviewed 但任务单文件不存在
- `task_20260707_wangyuyan-project-management-domain-phase2`: 队列 marked reviewed 但任务单文件不存在
- `task_20260708_wangyuyan-ai-outpost-episode2-production`: 队列 marked reviewed 但任务单文件不存在
- `task_20260708_wangyuyan-claude-retrospective-p0-fix`: 队列 marked reviewed 但任务单文件不存在
- `task_20260708_wangyuyan-claude-retrospective-p1-supplement`: 队列 marked reviewed 但任务单文件不存在
- `task_20260708_wangyuyan-sales-domain-deep-dive-supplement`: 队列 marked reviewed 但任务单文件不存在
- `task_20260708_wangyuyan-pan-product-domain-supplement`: 队列 marked reviewed 但任务单文件不存在
- `task_20260708_wangyuyan-product-kernel-domain-supplement`: 队列 marked reviewed 但任务单文件不存在
- `task_20260708_wangyuyan-time-management-agent-supplement`: 队列 marked reviewed 但任务单文件不存在
- `task_20260708_wangyuyan-demand-analysis-agent-supplement`: 队列 marked reviewed 但任务单文件不存在
- `task_20260708_wangyuyan-five-step-method-orchestrator-supplement`: 队列 marked reviewed 但任务单文件不存在
- `task_20260708_wangyuyan-y-model-cross-domain-fusion-and-coach-agent`: 队列 marked reviewed 但任务单文件不存在
- `task_20260708_wangyuyan-dual-triangle-cross-domain-agent`: 队列 marked reviewed 但任务单文件不存在
- `task_20260708_huangyaoshi-capability-hub-phase1`: 队列 marked reviewed 但任务单文件不存在
- `task_20260709_wangyuyan-key-assumptions-business-formula-agent`: 队列 marked reviewed 但任务单文件不存在
- `task_20260709_wangyuyan-personal-learning-method-agent`: 队列 marked reviewed 但任务单文件不存在
- `task_20260709_wangyuyan-opportunity-foresight-agent`: 队列 marked reviewed 但任务单文件不存在
- `task_20260709_wangyuyan-expression-pitch-agent`: 队列 marked reviewed 但任务单文件不存在
- `task_20260710_wangyuyan-business-formula-conversion-case-round`: 队列 marked reviewed 但任务单文件不存在
