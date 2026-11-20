# 2026-11-19：客服分流案例的源码与保留复核

[实现审查](https://github.com/leoncuhk/awesome-decision-models/blob/bfe34486a0537cca5eda963315ae612a6184ca8d/docs/customer-service-implementation-review.zh-CN.md) · [领域主问题](https://github.com/leoncuhk/awesome-decision-models/blob/bfe34486a0537cca5eda963315ae612a6184ca8d/docs/domain-path-applicability-research.zh-CN.md)

## 保留决定

- Parlant：保留为routing类源码参考，固定`07b2bcb4bebfeda7c53f1e2bbf2c68415f389e83`；上游独立checkout位于工作区`refs/repos/parlant`。共享状态批量Proposition、声明关系解析及工具后更新有实际代码。
- Modem：保留为routing类产品案例，未定位核心服务端源码；新文档明确只有事件自身可判的条件能前置筛选，依赖外部资料时仍启动Agent。
- Entagl：保留为evaluation类历史回放报告；未定位公开harness、完整标签与逐条输出，业务API不代替评测代码。

## 本次做了什么

新增三项双语canonical资源和相应一手来源，生成首页/来源页；把详细代码定位、失败处理和保留依据集中到实现审查，并接入现有研究入口。保留旧源码pin与历史应用表，不用最新代码静默重写旧证据。

Parlant审查覆盖引擎调用、effort策略、Jev适配器、声明关系、工具执行与测试源码；执行12项隔离纯协议观察，结果随文保存。局部解码的数值/候选/类型校验缺口是复用边界，不宣称真实API已返回非法值。未修改上游、安装依赖、运行pytest或付费模型，不新增`reproduced_here`或性能数值账本。

## 验证边界

本次已运行`python3 scripts/render.py`，`python3 scripts/validate.py`与`git diff --check`均通过；另检查协议JSON、源码pin和本地clone清洁状态。按数据/模板变更范围不重跑程序单元测试。仓库结构验证、局部协议观察、完整模型效果与生产业务收益分别报告；本次只覆盖前两项。

## English summary

Retain a pinned Parlant source-code reference, a bounded Modem event-gating case and an Entagl replay report. Only the first supplied inspectable core routing code. Preserve historical versions and distinguish local protocol observations from model, engine and production validation. Update canonical bilingual resources and active research navigation without vendoring upstream projects or creating a new runtime.
