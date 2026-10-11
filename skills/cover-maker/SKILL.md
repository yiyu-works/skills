---
name: cover-maker
description: "Design multi-aspect covers from supplied screenshots, video frames and verified titles. Use for tutorial or product-demo covers; does not transcribe video or publish content."
metadata:
  version: "0.1.0"
---

# 真实内容封面


## 工作流程
确认主题、受众、指定画幅与真实素材。只有视频时先从用户提供的字幕/说明理解内容，再选帧；视频不能被截图内容完整推断。源视频和屏幕可能包含敏感字段，先检查再决定是否上传外部工具。

候选帧用 `python3 scripts/extract_frame.py <视频> <秒数> <输出.png>` 截取（需要FFmpeg）。看过实际画面后选择稳定、清晰、对应标题的帧，保留时间与来源。字幕时间不一定是最终编辑视频时间，先核对对应关系。

标题只表达视频或用户材料支持的主张，不夸大收益和结果。先确定主信息、真实画面和层级，再安排装饰。已有品牌优先，产品Logo使用提供或授权资产，不凭记忆重画成官方标识。

读 [多画幅设计](references/covers.md)，按用途分别排版而非机械裁切。可从 [封面模板](assets/cover.html) 制作16:9，并按需求适配其他比例。标题用真实文本叠排，避免依赖生成模型拼字。

缩小到列表缩略图检查文字与主体，在实际尺寸检查裁切、隐私和对比。使用生图只能辅助背景或风格，不篡改真实截图中的产品证据。无生图能力仍可用HTML/SVG交付。

## 交付
交每个请求画幅的封面、可编辑源文件和素材/时间点记录。HTML模板不等于PNG；需实际截图或导出并查看后才报告PNG完成。自动发布不在范围内。
