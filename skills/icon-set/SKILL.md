---
name: icon-set
description: "Create consistent icon sets as SVG or generated raster assets with semantic names and visual checks. Use for a matching collection of icons, not logos or a single unrelated illustration."
metadata:
  version: "0.1.0"
---

# 统一风格图标集


## 工作流程
列出语义名称和使用尺寸，确定风格规范：画布、留白、线宽、圆角、颜色、光线与细节密度。已有图标系统先延续，不为几个新增图标重造品牌。

功能符号优先SVG或已有授权图标集；立体、手绘等栅格风格使用宿主可用图片工具。使用生成服务前说明能力、素材上传和费用，沿用已授权供应商。没有生图能力可交SVG或提示词，不能声称已经生成PNG。

逐个选择易辨认的隐喻，并在目标尺寸比较，避免相似符号表达不同动作。SVG保持统一viewBox，移除脚本、外部引用和字体依赖。装饰图标在实际页面中隐藏于辅助技术；独立交互的按钮仍要文字标签。

生成宫格时读 [图标规范](references/icons.md)，记录行列与按行顺序。用 `python3 scripts/split_sheet.py <图片> <名称JSON> <输出目录> --rows N --cols N` 切图；图片尺寸必须整除网格，不猜测边界。脚本只切图，不自动移除背景。带色背景不得伪报透明。

在浅色、深色背景与实际尺寸逐一查看，检查边缘、留白、线宽和语义。透明度需检查真实alpha而非凭预览格子判断。

## 交付
交独立文件、名称清单、风格规范和实际检查记录。可参考 [三枚原创SVG](assets/icons.svg) 的一致性，但为用户任务设计新隐喻。
