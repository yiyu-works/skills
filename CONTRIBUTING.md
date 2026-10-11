# 贡献

Issue请包含：Skill名称/版本、宿主、最小输入、预期结果、实际结果、证据与复现步骤。不要上传隐私和凭据。

新增技能须有明确触发边界、可重复验收任务、相关依赖说明和来源许可。修复应针对真实行为，不为增加数量创建空目录。

运行 `python3 scripts/validate_repo.py` 与 `python3 -m unittest discover -s tests -v`。修改HTML运行浏览器检查并记录范围；修改媒体脚本实际检查输出。
