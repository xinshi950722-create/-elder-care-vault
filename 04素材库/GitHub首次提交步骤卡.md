# 周四 GitHub 首次提交步骤卡（极简）

> 目标：把 `养老转行` 整个 vault 推到 GitHub 私有仓库，完成第一次备份。用 GitHub Desktop，不碰命令行。

## 准备（周三前）
- 注册 / 登录 GitHub（github.com）
- 安装 GitHub Desktop（desktop.github.com）
- 可选：网页建私有仓库 `elder-care-vault`（不建也行，Desktop 第 3 步能直接建）

## 步骤（GitHub Desktop）
1. 打开 GitHub Desktop → `File` → `Add local repository` → 选 `养老转行` 文件夹
2. 若提示不是 Git 仓库，点 `Initialize`（分支名用 `main`）
3. `Publish repository` → 勾选 `Private`（私有）→ `Publish`（首次即完成建远程仓 + 推送）
4. 之后每天改动后：看 `Changes` → 底部 `Summary` 写一句（如"周一 vault 搭建 + 适老化笔记"）→ `Commit to main` → `Push origin`
5. 验证：网页打开仓库能看到文件即成功

## 验收标准
- 远程仓库含 `养老转行` 全部文件
- 此后养成"每天一 commit 一 push"

## 辩证提醒
- Desktop 比命令行稳，别为学 Git 命令分心，那是另一条学习线
- 私有仓库免费，内容不外泄
- 版本回溯等真需要时再说，先用"每天一推"把习惯跑起来
- 关联：[[周一下午计划]]（首次提交原计划在周四）、[[2026-07-20]]（今日日记提及待提交）
