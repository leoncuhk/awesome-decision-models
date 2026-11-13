# 2026-11-13：补入 Google Gemini Decision 1

[中文首页](../README.zh-CN.md) · [模型卡](../docs/models.md#gemini-decision-1) · [应用净效用](2026-11-13-jev-utility.md)

Google于11月11日发布`gemini-decision-1`及Decisions API，已由[官方发布说明](https://aistudio.google.com/docs/changelog)交叉核查。本次补入独立核心模型条目，修正此前11月13日更新遗漏这一主要发布的问题。原更新是有边界的研究选择，不应视为完整新品盘点。

## 影响选型的增量

[模型规格](https://aistudio.google.com/docs/models/gemini-decision-1)支持文本、图片、音频、视频、PDF；每请求最多1000题，共享输入与全部问题合计262144 tokens。模型不生成正文，也不直接执行工具。其有用增量是同一份多模态证据可承担多个有界检查，适合把“音视频先转文本再用大模型分类”的现有路径作为对照；是否省掉了必要信息或降低完整成本仍需实验。

[API指南](https://aistudio.google.com/docs/decisions-api)定义noul、choice、score。confidence取最高选项概率，二元题为`max(p,1-p)`；rubric的score是索引期望，最高等级概率不能解释为这个连续期望值恰好正确的概率。该字段定义与其他服务不同，不能复制同一个阈值。题目隔离是接口约定，不保证误差独立；安全拦截返回HTTP400，必须计入失败与回退。每题指令仅文本，媒体放共享输入。

[价格表](https://aistudio.google.com/docs/pricing#gemini-decision)在核查日列付费输入每百万tokens $0.10、无输出tokens。共享输入每请求计费一次，每题仍增加指令、criteria及格式tokens；重复请求的输入重新计费，不支持缓存、Batch、Flex或Priority。免费与付费层的数据使用条款不同。价格是API费用，不包含上传、检索、人工复核和失败重试。

## 效果证据保留在何处

[发布博客](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/)宣称基准与校准优势，并列举Gemini Notebook路由、Stitch交互、CC表情选择、Search的MCP安全检查等内部使用。它为真实应用方向提供厂商一手线索，但未在本次核查中取得可独立审计的对照分配、逐样本输出及完整成本。延迟描述限定输入长度和题数区间，不能外推到最大上下文或1000题；本文不导入排名、倍数或内部业务提升数值。

最值得先做的匹配实验是：相同工单附图/录音，比较原有ASR/OCR＋分类器、生成式多模态LLM、该API；固定业务硬规则与错误上限，测完整延迟、复核率及总损失。更多模态与更多题只是能力接口，不能代替目标领域验收。

## 维护与检查边界

新增5条官方来源及1个核心模型，更新canonical JSON后生成双语文档。Google域名目前不在source watcher允许域中，因此本次保留人工复查来源，未扩大抓取权限、修改运行代码或定时设置。未调用API、安装SDK、审计权重或复现性能。结构验证与单元测试结果在交付报告中记录。

English: Added the November11 Gemini Decision1 release from official release notes, model/guide/pricing pages and launch post. Shared-input multimodal judgments are a new comparator, while calibration and internal deployment claims remain vendor-reported. Confidence semantics, safety errors and full billing boundaries need target-task validation. No model execution or watcher permission changes.
