---
name: video-to-article
description: "Turn supplied video plus time-aligned subtitles or transcript into a sourced Markdown article with verified frame references. Use for video-to-article conversion, not transcription, editing or publishing."
metadata:
  version: "0.1.0"
---

# 视频转图文文章


## 工作流程
输入应有视频和SRT/VTT字幕，或带来源的逐字稿。缺少文字内容时先说明需要转录能力，使用已授权工具获得字幕；不要仅凭画面编出视频观点。只给字幕可做文字稿，但配图未验证须明确。

用 `python3 scripts/parse_subtitles.py <字幕> --output <输出.json>` 整理时间与文本。通读内容，再按读者问题重组文章，不直接拼接字幕。名词、数字、命令等不确定处与字幕、画面及原始资料对照。

读 [来源与时间轴](references/article.md)。字幕与视频可能来自不同剪辑版本，核对前、中、后位置；有剪辑映射才转换工程时间轴。首版只截导出视频，不声称支持Screen Studio工程解析。

按内容选稳定结果帧，通过 `python3 scripts/extract_frame.py <视频> <秒数> <输出.png>` 截图，并逐张查看。图只用来解释实际步骤或证明结果，不用泛用配图替换证据。敏感字段打码后才放入公开稿，原帧保留在私有工作目录。

文章使用自然段连接问题、过程和结果；操作步骤用有序列表。命令与配置从真实材料获取，截图模糊处不猜补。引用、作者观点与编辑补充区分。每个关键事实在工作记录关联时间点或外部来源。

## 交付
交文章Markdown、相对路径images目录与sources.md。原文语言沿用或按用户指定转换。不自动发布，不虚构文章配图已核验；缺字幕、图像查看或FFmpeg时写清完成范围。
