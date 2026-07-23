# GitHub 同步步骤卡（git push 版）

> 目标：让 `养老转行` vault 通过 git 与 GitHub 私有仓 `elder-care-vault` 持续同步。改自网页拖上传版，因用户需要"持续更新"。

## 状态（2026-07-23 更新）
- ✅ 本地 git 已接 `origin`：https://github.com/xinshi950722-create/elder-care-vault.git
- ✅ 今天新笔记/PPT 已提交本地（`20f0bb2`），工作区干净
- ⏳ 首次推送待你本机授权（沙箱无 GitHub 凭据，强推需你登录）
- 历史分裂：GitHub 上有一次网页上传的孤立提交，首次需 `--force-with-lease` 覆盖，内容不丢

## 首次推送（在你自己电脑的终端跑，非 WorkBuddy 对话框）
1. 打开 PowerShell / Git Bash / 终端（能访问你 GitHub 登录凭据的环境）
2. 进入 vault 目录：
   ```
   cd "D:\workbuddy work\2026-07-20-09-10-29\养老转行"
   ```
3. 首次强推（会弹 GitHub 登录，登录即成功）：
   ```
   git push -u origin main --force-with-lease
   ```
4. 验证：github.com 打开 `elder-care-vault`，能看到泰康/万科笔记、两份 PPT 即成功

## 日常同步（之后每次本地改完，一行命令）
```
git add -A && git commit -m "一句话说明本次更新" && git push
```
例：`git add -A && git commit -m "补充钱江运营岗调研" && git push`

## 注意事项
- 强推只首次需要；之后都是普通 `git push`
- 若弹出凭据失败：确认 GitHub Desktop 已登录，或在终端跑 `git config --global credential.helper manager`（Windows 凭据管理器）
- `.gitignore` 已排除：`.obsidian/workspace.json`、`graph.json`、Office 锁文件 `~$*`、`.trash/`，避免本地状态污染仓库
- CRLF 警告无害（Windows 行尾归一化）

## 辩证提醒
- 工具是杠杆不是目的。每天 `git push` 一行是习惯，别为"同步方式"反复横跳
- 关联：[[2026-07-23]]（今日切 git push）、[[养老管理岗位入门大纲]]
