---
name: ui-design
description: "Design or visually improve websites and product interfaces using the existing brand, realistic content and rendered evidence. Use for visual direction or page design; frontend correctness reviews belong to frontend-check."
metadata:
  version: "0.1.0"
---

# 界面设计与探索


## 工作流程
识别交付类型：设计说明、静态原型、已有界面改版或可运行页面。先读取品牌、页面任务、真实内容和已有组件。遵守用户选定的风格与技术栈；截图还原以参考视口为基准，不发散新风格。

没有既定方向时，围绕产品内容提出可辨认的设计选择：信息结构、字体层级、视觉重心、色彩与材料。用户要求比较时做候选；已选定方向时直接深化，不强制停下来选方案。不要只给同一骨架换色。

写一份简短设计说明，记录主任务、主动作、内容优先级、关键状态与视口。先完成一个代表页面，再扩展。使用真实或明确标注的示例数据，不虚构客户、评价、收入或真实连接状态。

需要并排比较时读 [比较方法](references/comparison.md)。使用 `python3 scripts/compare.py --output <工作目录>/compare.html <候选HTML路径>...` 生成离线比较页。候选须在输出目录内或其子目录；页面不得自动运行陌生远程代码。

实现后在桌面与窄屏查看真实页面，检查长标题、中文换行、可读性、首屏主任务、图片裁切与主要操作。截图文件存在不代表视觉已检查。浏览器不可用时交付实现与未验证项，不给审美分数冒充实测。

## 交付与验收
交付页面、设计说明及实际查看过的截图；说明原型动作和已接入动作的区别。修改既有项目时保留业务逻辑，仅改变授权的界面范围。核心交互与状态问题按项目规范验证，不默认安装其他 Skills。
