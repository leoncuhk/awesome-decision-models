# MIRE / WWW2025: multimodal intent competition case study

[简体中文](mire-case-study.zh-CN.md) · [Adaptation guide](multimodal-decision-finetuning.md#quick-route) · [Evidence E33](evidence.md#e33)

Reviewed 2026-10-18. This case consolidates public task definitions, pinned code, organizer results and method literature. It records source review, not model execution or production validation. The two tasks are **parallel**; scene classification is not a mandatory first stage of intent recognition. Final prizes and online scores describe different evaluations.

<a id="tasks"></a>
## 1. Problem and task contracts

The contest asks how to identify e-commerce image scenes and current user intent when evidence spans images and dialogue and model/data/inference resources are limited. It evaluates classification labels, not reply quality, permission to execute a transaction or downstream handling success. Sources: [official task page](https://tianchi.aliyun.com/competition/entrance/532277/information), [organizer paper](https://doi.org/10.1145/3701716.3719642) §2 and [fixed README](https://github.com/liujunwen23/MIRE/blob/d101287af90d114c5bf0cbfbd56fe9c52358e3bb/README.md).

| | A: image-scene classification | B: dialogue-intent classification |
| --- | --- | --- |
| Question | What e-commerce scene does the image show? | What is the user currently asking or reporting? |
| Input | Image plus task instruction and label definitions | Dialogue history, current user expression and relevant historical image(s), plus task/label definitions |
| Output | One scene-label string, 23 active classes | One intent-label string, 23 classes |
| Image role | Main classification object | Evidence helping interpret dialogue |
| Boundary | A page/object type is not a user goal | Same page can accompany different goals; context may be indispensable |

These are separately posed tasks, not a requirement to output two labels for every record. The public baseline is generative label SFT, not a verified D3/Intern candidate-logit implementation.

<a id="labels"></a>
## 2. Complete active labels

Exact Chinese labels are retained because label-string identity matters to scoring. The following groups are **editorial reading aids, not official superclass targets**. [Official definitions](https://tianchi.aliyun.com/competition/entrance/532277/information) remain authoritative. The current README scene table has 25 rows with two struck-through items (`消费者与客服聊天页面`, `个人信息页面`); the active list below contains 23, including `评论区截图页面`.

| Scene group | Active labels |
| --- | --- |
| Product presentation / 商品展示 | `商品分类选项`、`商品头图`、`商品详情页截图` |
| Order and payment / 下单支付 | `下单过程中出现异常（显示购买失败浮窗）`、`订单详情页面`、`支付页面`、`购物车页面` |
| Logistics / 物流 | `物流页面-物流列表页面`、`物流页面-物流跟踪页面`、`物流页面-物流异常页面` |
| After-sales and disputes / 售后争议 | `退款页面`、`退货页面`、`换货页面`、`投诉举报页面`、`平台介入页面` |
| Store, promotion, reviews, account / 店铺活动评价账户 | `店铺页面`、`活动页面`、`优惠券领取页面`、`评论区截图页面`、`账单/账户页面` |
| Other images / 其他图像 | `实物拍摄(含售后)`、`外部APP截图`、`其他类别图片` |

| Intent group | Labels |
| --- | --- |
| Attributes and variants / 属性区别 | `商品材质`、`商品规格`、`包装区别`、`版本款型区别`、`适用季节`、`上市时间` |
| Function and usage / 功能使用 | `是否好用`、`功效功能`、`排水方式`、`能否调光`、`控制方式`、`用法用量`、`养护方法` |
| Quality and feedback / 品质反馈 | `是否会生锈`、`是否易褪色`、`反馈密封性不好`、`反馈用后症状`、`信号情况`、`气泡` |
| Recommendation and supply / 推荐供给 | `单品推荐`、`套装推荐`、`发货数量`、`何时上货` |

An explicit other-image category is not a general unknown-intent or clarification guarantee. `控制方式` versus `能否调光`, or `包装区别` versus `商品规格`, needs the published definitions and current context. This taxonomy is not the full universe of customer-service requests.

<a id="competition-design"></a>
## 3. Data, phases and resource boundaries

| Phase | Officially described provision / evaluation |
| --- | --- |
| Training | 1000 labeled dialogue/image samples in total; no inferred 1000 per task or exact task allocation |
| Preliminary | 10000 unlabeled test examples; automatic platform evaluation |
| Semifinal / later algorithm round | 10000 additional new unlabeled examples; online score board, best rows dated Jan18–19 2025 |
| Final composite review | Code/model/data/technical-material review, reproducibility/compliance checks and defense; expert evaluation Jan22–27 2025 contributes alongside online results |

[Official rules](https://tianchi.aliyun.com/competition/entrance/532277) require private deployment and inference code, under-10B models, at most three model calls and total output within 100 tokens per sample; they also restrict private-domain training data and commercial LLM APIs in the contest. README/PDF boundary wording is not perfectly identical (≤ versus <; the paper describes the API case), so preserve the specific source rather than converting every wording into an interchangeable tested condition. The baseline's `max_new_tokens=128` is an example inference setting, not proof of contest compliance. Dataset access/use and rights outside the contest require separate review.

The organizer paper describes de-identification and expert label review; this repository did not audit those processes or obtain the full dataset/images. Resolution, class support, task proportions, exact image–turn alignment, independent-group counts and overlap remain unknown.

<a id="data-and-code"></a>
## 4. Data → full-SFT baseline → generation → submission → scoring

| Component | Actual pinned code / interpretation |
| --- | --- |
| Data fields | [data_info.json](https://github.com/liujunwen23/MIRE/blob/d101287af90d114c5bf0cbfbd56fe9c52358e3bb/mire_baseline/configs/data_info.json): `instruction`→prompt, `input`→query, `image`→images, `output`→response; `id` identifies the sample and `image` is a one-or-more image-path list. Empty `input` does not mean no text: demo dialogue and candidates are in `instruction`. `output` is supervision/reference, never inference evidence. |
| Training | [qwen2_vl_full_sft.yaml](https://github.com/liujunwen23/MIRE/blob/d101287af90d114c5bf0cbfbd56fe9c52358e3bb/mire_baseline/configs/qwen2_vl_full_sft.yaml): Qwen2-VL-7B-Instruct, `finetuning_type: full`, LLaMA-Factory, 3 epochs, LR 5e-6, validation fraction 0.1, training cutoff 1024. `max_samples: 10000` is a read cap, not a labeled-data count. Actual train.json/task mixing/group split and trained weights were not audited. |
| Prediction | [predict.yaml](https://github.com/liujunwen23/MIRE/blob/d101287af90d114c5bf0cbfbd56fe9c52358e3bb/mire_baseline/configs/predict.yaml): generation of a label string; example dataset/model paths must be set for the intended run. Inference cutoff 2048 and generation cap 128 are separate from training/contest limits. |
| Submission | [convert2submit.py](https://github.com/liujunwen23/MIRE/blob/d101287af90d114c5bf0cbfbd56fe9c52358e3bb/mire_baseline/convert2submit.py): reads JSONL `predict`, assigns by row order, writes CSV. Preserve identity/order and validate lengths; the script is not an ID-safe join. Official CSV requires at least `id` and `predict`. |
| Local metrics | [cal_acc.py](https://github.com/liujunwen23/MIRE/blob/d101287af90d114c5bf0cbfbd56fe9c52358e3bb/mire_baseline/cal_acc.py): `output` versus `predict` strings; sklearn weighted F1/P/R and accuracy. Its multilabel docstring does not turn the actual single-string records into set-valued multilabel evaluation. |

[Official scoring](https://tianchi.aliyun.com/competition/entrance/532277/information) is weighted F1 across **all classification labels**, not macro-F1 or an equal mean of the two task scores. The exact aggregate is kept from the official `score` column; no class counts/weights are reverse-engineered from rounded values. Weighted scores can conceal rare-class failures. README baseline F1 and accuracy are different quantities and are not used here to manufacture a matched improvement estimate.

<a id="public-examples"></a>
## 5. Public examples and missing evidence

[demo_test.json](https://github.com/liujunwen23/MIRE/blob/d101287af90d114c5bf0cbfbd56fe9c52358e3bb/data/demo_test.json) contains ten text/label records with image references. In its second record, lamp dimming/mobile-connection history and the current switch-control expression lead to `控制方式`. In its eighth, “这个是哪个地方” follows material discussion and is labeled `商品材质`. These are **paraphrases of real public text examples**, not new model predictions or paired counterfactual experiments. The referenced original images were not read; no invented picture is presented as a competition original.

A logistics-exception screenshot→scene label or a simplified bubble-example JSON can explain the format, but must be labeled a self-made illustration unless the actual public asset is inspected. Missing decisive text, an unreadable crop or absent contemporaneous context can make intent underdetermined. This contest's fixed-label score does not independently validate a new clarify/unknown policy.

<a id="finalists"></a>
## 6. Final prizes, online ranks and methods

### Official final awards versus semifinal scores

The [final-results table](https://tianchi.aliyun.com/competition/entrance/532277/customize583) and [later algorithm leaderboard](https://tianchi.aliyun.com/competition/entrance/532277/rankingList) were read as rendered public pages. The English board calls the algorithm phase “Final Round”; it is the **复赛/later algorithm test**, not the subsequent composite prize review. [Competition rules](https://tianchi.aliyun.com/competition/entrance/532277) explicitly combine online results and expert assessment for final placement.

| Composite final rank / award | Official team | Associated method | Semifinal online rank | Official score | intent_score | image_scene_score |
| --- | --- | --- | --- | --- | --- | --- |
| 1 / gold | Dynamic Challengers | IntentionGPT | 3 | 0.9051 | 0.9365 | 0.8339 |
| 2 / silver | 拥抱LLM / EmbraceLLM | EcomMIR | 2 | 0.9070 | 0.9420 | 0.8278 |
| 3 / bronze | scale | CuSMer | 1 | 0.9085 | 0.9265 | 0.8676 |

See [E33](evidence.md#e33) for the full provenance/protocol. These values are organizer-reported aggregates, not our rerun. Exact expert/composite numeric scores are not supplied in the inspected final table. EcomMIR's two task values average to 0.8849, **not** the official 0.9070: do not replace the all-class weighting with an invented equal-task metric. The official 2025 online stage and final awards should not be merged with later model leaderboards.

### What each method actually contributes

| Method / attribution | Inspected technical idea | Evidence depth / limitation |
| --- | --- | --- |
| [IntentionGPT](https://doi.org/10.1145/3701716.3718370), Dynamic Challengers | Self-data augmentation, collaborative noise filtering, structure-aware domain retrieval and model soups. Organizer §3 supplies the team-level method summary. | Publisher [SIGWEB abstract](https://www.sigweb.sigweb.hosting.acm.org/toc/www25b.html) read; full paper and exact training/base/code artifacts not obtained. Abstract claims first place, consistent with the final gold table; no unrelated same-name chat app is used as code evidence. |
| [EcomMIR](https://doi.org/10.1145/3701716.3718371), 拥抱LLM / EmbraceLLM | CN-CLIP scene training/Greedy Soup; MiniCPM-V 2.6 intent LoRA; cleaning, hierarchical labels and high-confidence pseudo-label expansion. | [Author-hosted full paper](https://zhoushengisnoob.github.io/papers/WWWComp.pdf) reviewed. [E28](evidence.md#e28) preserves author Round2 task results, now separately corroborated by the official board. Many interventions are combined; no isolated LoRA effect. |
| [CuSMer](https://doi.org/10.1145/3701716.3718373), scale | Pseudo-label→fine-tune→merge and image-augmentation→fine-tune→merge pipelines; organizer §3 attributes diversity/confidence sampling and Breadcrumbs/TIES merging to scale. | Publisher abstract/organizer overview and [author identity page](https://binglin-wu.github.io/) reviewed; full method paper/code not verified. Abstract's online-final first and author's bronze are compatible because phase/rank differ. |

The organizer paper's Table1 establishes Dynamic Challengers / EmbraceLLM / scale prizes. Method-paper attribution uses the corresponding author reports and technical descriptions; CuSMer's author explicitly names scale@DLUT and bronze. Exact scored submission→paper checkpoint equivalence is still not pinned. Verified contestant implementation repositories were not found in this review; that is not a claim that none exist. The official MIRE baseline repository is not the released implementation of all three methods.

<a id="transfer-boundaries"></a>
## 7. What transfers to a new experiment

Useful hypotheses are evidence/label definition, context-aware retrieval, label-preserving augmentation, supervised adaptation and carefully audited merging. EcomMIR uses Round1 unlabeled inputs for training expansion: it is not an original-1000-label-only supervised experiment; this exposure alone neither establishes Round2 contamination nor proves a clean untouched split. Organizer reports of additional pseudo-labels or noise reduction are not treated as audited dataset counts or causal effects here.

The contest does not establish calibration, risk certificates, rare-class coverage, new-UI/time generalization, end-to-end p95 or superiority of D3/Intern/custom readouts. Use the existing [split protocol](multimodal-decision-finetuning.md#split-protocol), [minimal matrix](multimodal-decision-finetuning.md#experiment-matrix), [preflight](multimodal-decision-finetuning.md#preflight) and [result template](multimodal-decision-finetuning.md#result-template) before adapting another domain. Test one factor at a time with held-out grouped acceptance; stop or retain a stronger baseline when the preregistered risk/gain/cost conditions do not hold.

<a id="sources-and-gaps"></a>
## 8. Source register and remaining gaps

Primary links are attached above; immutable MIRE code pin is `d101287af90d114c5bf0cbfbd56fe9c52358e3bb`. The [source register](sources.md) records full-text versus abstract-only review and organizer-PDF content hash. [E28](evidence.md#e28) remains unchanged; [E33](evidence.md#e33) adds the official stage-specific comparison. Public rules/results, organizer full text, baseline code and public text demos were reviewed; the complete dataset/images, submission weights/raw predictions, exact team code, IntentionGPT/CuSMer full text and expert numeric scores remain unverified. No model, training, external evaluation script or dataset-download workflow was run.
