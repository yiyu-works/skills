---
name: web-slides
description: "Create or edit keyboard-navigable HTML slide decks with presenter notes and printable pages. Use for browser presentations; native editable PPTX export is outside this skill."
metadata:
  version: "0.1.0"
---

# 可编辑网页演示


## 工作流程
确认听众、讲述时间、画幅和交付形式。先写故事线，每页承担一个论点，证据来自资料；不把长文章按段落直接铺满幻灯片。

使用 [演示模板](assets/deck.html)，保留语义标题、方向键、Home/End 导航、页码、演讲者备注和打印样式。按内容调整页数与排版，不让每页都成为相同的卡片网格。默认16:9，用户指定比例时同步调整。

图表标明单位、来源和时间；缺失数据不造数。真实素材与生成素材在交付说明区别。图片与字体默认本地或系统资源，使演示可离线打开。

读 [演示验收](references/slides.md) 检查缩放、长中文和宽表。浏览器实际走完所有页面；打印预览验证一页一张与备注隐藏。保存HTML成功不证明页内不溢出。

备注可通过“N”切换用于演讲，不得把机密写入要公开分享的HTML：隐藏备注仍在源文件中。键盘事件遇到输入框或可编辑元素时不要抢占。

## 交付
交可编辑HTML及相关资源、实际验证记录。可用浏览器打印导出PDF，但只有实际导出并检查后才声称PDF可用。HTML不是原生PPTX，本技能不承诺可编辑PPTX转换。
