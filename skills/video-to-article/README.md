# 视频转图文文章

video-to-article · 免费实验版 0.1.0

## 使用

```text
使用 $video-to-article：把视频和 SRT 转成教程文章，提取真实配图，并记录关键结论对应的时间点。
```

## 安装

```bash
npx skills add yiyu-works/skills --skill video-to-article
```

也可将本文件夹完整复制到宿主的 skills 目录。见 [安装说明](../../docs/installation.md)。

## 依赖与范围

字幕解析需Python 3.9+；截图需FFmpeg；需图片查看能力。工作流程见 [SKILL.md](SKILL.md)。外部模型及付费服务的费用不包含在技能中。

## 示例与验证

- [示例任务](../../examples/video-to-article/README.md)
- [验收任务](../../evaluations/video-to-article/cases.md)
- [首版验证记录](../../evaluations/RESULTS.md)

本版不宣称已完成多模型效果评测。
