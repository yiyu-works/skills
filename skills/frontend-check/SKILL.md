---
name: frontend-check
description: "Review or fix frontend interactions, responsive behavior and data states using observable evidence. Use for forms, lists, dialogs and UI state bugs, not aesthetic redesign or backend-only reviews."
metadata:
  version: "0.1.0"
---

# 前端状态与交互检查


## 工作流程
先确认是只读评审还是修复，定义一个可复现用户任务及预期结果。查相关组件、数据来源与调用位置，不先通读整个代码库。证据分成源码推断、实际复现与待确认三类。

为受影响操作建立状态表：初始、加载、成功、空结果、失败、重试；编辑涉及未保存数据、重复提交与读回。不要强行测试与改动无关的全部状态。

列表检查对象 ID、筛选分页、排序和选择范围；异步请求检查过期响应是否覆盖新查询。表单检查标签、校验、提交中禁用与失败后保留输入。弹窗检查焦点、关闭、滚动和键盘路径。详细案例见 [状态矩阵](references/state-matrix.md)。

实际操作从入口走到结果。保存后刷新或重新读取；点击按钮、请求发送或提示成功不能证明数据已保存。只能模拟接口时明确标注，不向真实账户创建测试数据。无授权的删除、购买与发送止于可安全验证的边界。

修复针对根因，复用已有组件和测试基础，不顺便重设计或升级依赖。添加测试应针对错误行为，避免只断言实现细节。按改动运行相关检查；存在构建或类型门禁时执行。

## 报告
使用 [评审模板](assets/review.md)。每项包含位置、复现步骤、预期/实际、影响、证据和最小建议；按用户影响排序。无法运行时交付源码评审，不标为交互通过。
