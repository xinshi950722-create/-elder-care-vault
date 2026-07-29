---
tags: [素材, 工具, Git]
---

# GitHub 同步步骤卡（git push 版）

> 让 `养老转行` vault 通过 git 与 GitHub 仓 `-elder-care-vault` 持续同步。改自网页拖上传版，因你需要"持续更新"。

## 状态（2026-07-23 已跑通）
- ✅ origin 已接：`https://github.com/xinshi950722-create/-elder-care-vault.git`
- ✅ 首次强推完成（本地 `abd95d8` 覆盖远端），`main` 已跟踪 `origin/main`
- ✅ 之后日常普通 `git push` 即可，无需再强推
- ⚠️ 仓库名带前导横杠 `-elder-care-vault`（建仓时多打了一个 `-`），暂不改

## 日常备份（每天在 Obsidian 写完笔记后）
打开 PowerShell，先 `cd` 进 vault 目录，然后**一行一行**敲下面三行。
注意：用回车分行执行，不要用 `&&` 串起来，PowerShell 5.1 不支持 `&&`。

**第 1 步 · 暂存所有改动**
```
git add -A
```

**第 2 步 · 提交并写摘要**（把引号里换成当天日期 + 你做了啥）
```
git commit -m "2026-07-23 补充日常备份步骤卡"
```

**第 3 步 · 推送到 GitHub**
```
git push
```

**验证成功**：看到 `main -> main` 这类提示、且没有 `error` / `fatal` 字样，即同步成功。去 github.com 刷新仓库能看到刚加的文件。

## 首次推送（已完成，留作备查）
1. 进 vault 目录：`cd "D:\workbuddy work\2026-07-20-09-10-29\养老转行"`
2. 首次强推：`git push -u origin main --force-with-lease`（弹浏览器登录，登录即过）
3. 成功输出示例：`+ ff9c3f6...abd95d8 main -> main (forced update)`

## 踩过的坑（速查，避免重蹈）
- **连不上 / Connection reset**：别手动给 git 加 `127.0.0.1` 代理，Astrill 是全隧道模式，直连即可。
- **要密码却失败**：GitHub 早不支持账号密码，HTTPS 推送必须用 Personal Access Token（PAT，形如 `ghp_xxxx`）。
- **Repository not found**：仓库真名是 `-elder-care-vault`（带前导横杠），`origin` 写错成 `elder-care-vault` 就会找不到。
- **`&&` 不是有效语句分隔符**：PowerShell 5.1 不支持 `&&`，命令必须分行跑。

## 注意事项
- `.gitignore` 已排除：`.obsidian/workspace.json`、`graph.json`、Office 锁文件 `~$*`、`.trash/`，避免本地状态污染仓库。
- CRLF 行尾警告无害（Windows 行尾归一化）。
- 工具是杠杆不是目的，每天三行是习惯，别为"同步方式"反复横跳。

## 关联
- [[索引]]
[[2026-07-23]] [[养老管理岗位入门大纲]] [[WorkBuddy四段式提问法]]
