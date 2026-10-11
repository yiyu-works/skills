# 安装

## 选择安装

在具备Node.js/npm的环境运行：

```bash
npx skills add yiyu-works/skills --skill readme-polish
```

安装器按当前版本提示选择宿主。安装后通过宿主技能清单确认；名称与本库目录相同。此命令由第三方 skills CLI 提供，不是本库自建脚本。

## 手动安装

下载仓库后，将 `skills/<名称>/` 整个文件夹复制到宿主文档规定的位置。Codex用户级目录通常为 `~/.codex/skills/`，Claude Code通常为 `~/.claude/skills/`；其他宿主按官方说明，不假定所有工具读取同一位置。

不要把整个仓库当成单个Skill，也不要只复制SKILL.md而漏掉资源。修改已安装版本前保留本地改动。产物保存到用户任务目录，不写回技能目录。

## 脚本

SKILL.md里的 `scripts/` 和 `assets/` 均相对当前技能根目录。可用绝对路径调用；Python辅助工具默认3.9+。有Pillow要求的工具仅在栅格切图时需要它；使用虚拟环境安装。FFmpeg使用已有安装，不自动修改系统。

外部服务不由本库提供，不把API Key发到Issue或写进提示词。没有需要的能力时说明未完成部分。
