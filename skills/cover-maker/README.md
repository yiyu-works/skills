# 真实内容封面

cover-maker · 免费实验版 0.1.0

## 使用

```text
使用 $cover-maker：根据这段产品演示和字幕，制作16:9与3:4封面，保留真实界面和可编辑标题。
```

## 安装

```bash
npx skills add yiyu-works/skills --skill cover-maker
```

也可将本文件夹完整复制到宿主的 skills 目录。见 [安装说明](../../docs/installation.md)。

## 依赖与范围

HTML/SVG封面不需生成API；视频选帧需FFmpeg；栅格导出需浏览器或图片工具。工作流程见 [SKILL.md](SKILL.md)。外部模型及付费服务的费用不包含在技能中。

## 示例与验证

- [示例任务](../../examples/cover-maker/README.md)
- [验收任务](../../evaluations/cover-maker/cases.md)
- [首版验证记录](../../evaluations/RESULTS.md)

本版不宣称已完成多模型效果评测。
