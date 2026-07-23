# 周四 GitHub 首次提交步骤卡（极简）

> 目标：把 `养老转行` 整个 vault 推到 GitHub 私有仓库，完成第一次备份。用 GitHub Desktop，不碰命令行。

## 状态（2026-07-23 更新）
- ✅ 本地提交已完成（WorkBuddy 代执行）：commit `e43aea1`，分支 `main`，29 个文件，工作区干净
- ⬜ 远端推送待你本人完成（需登录你的 GitHub 账号授权，AI 无法代操作）

## 准备（你已具备）
- 注册 / 登录 GitHub（github.com）
- 安装 GitHub Desktop（desktop.github.com）

## 步骤（GitHub Desktop，只差这最后一步）
1. 打开 GitHub Desktop → `File` → `Add local repository` → 选 `养老转行` 文件夹
   - 重要：文件夹已是 Git 仓库，**不要再点 Initialize**，否则会冲突
2. 右上角出现 `Publish repository` → 仓库名填 `elder-care-vault` → 勾选 `Private`（私有）→ `Publish`
   - 这一步首次即完成「建远程仓 + 推送」，可能需要输入一次 GitHub 密码/授权
3. 验证：网页打开 github.com 你的账号，能看到 `elder-care-vault` 且含全部文件即成功
4. 之后每天改动后：看 `Changes` → 底部 `Summary` 写一句 → `Commit to main` → `Push origin`

## 验收标准
- 远程仓库含 `养老转行` 全部文件
- 此后养成"每天一 commit 一 push"

## 辩证提醒
- Desktop 比命令行稳，别为学 Git 命令分心，那是另一条学习线
- 私有仓库免费，内容不外泄
- 版本回溯等真需要时再说，先用"每天一推"把习惯跑起来
- 关联：[[周一下午计划]]（首次提交原计划在周四）、[[2026-07-20]]（今日日记提及待提交）
