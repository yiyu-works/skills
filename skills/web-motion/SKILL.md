---
name: web-motion
description: "Implement purposeful CSS, SVG or JavaScript web animation with reduced-motion and failure fallbacks. Use for scroll reveals, progress and interactive transitions, not AI video generation or standalone video editing."
metadata:
  version: "0.1.0"
---

# 网页交互动效


## 工作流程
将动效写成可验证的关系：触发输入、变化对象、初末状态、播放/随动方式与静态替代。明确是解释信息还是反馈操作，不为所有元素添加动画。

优先项目已有动画能力；简单显隐用CSS，滚动驱动使用可观察进度，复杂时间轴才增加依赖。默认以transform和opacity为主，避免每帧读取布局后再修改布局。用户内容与导航不依赖动画才能访问。

读 [动效约定](references/motion.md)。可参考 [离线动效样例](assets/motion.html)，其中进度和出场是两种不同机制，不将示例配色视为品牌要求。

检测 `prefers-reduced-motion`，并响应设置变更；减少动效时内容直接显示。无JS、资源失败、页面后台、卸载和尺寸变化都有可用结果。涉及React等组件时清理监听、观察器和动画句柄。

实际验证正向、反向、快速输入与触摸；检查滚动是否被劫持、键盘是否受阻。使用开发工具观察关键性能，不能凭“用了GPU属性”声称性能通过。

## 交付
交代码、动作说明和实际检查记录。已有视频可作为素材但不生成AI视频或绑定付费供应商；用户要视频驱动复杂动画时说明超出首版范围。
