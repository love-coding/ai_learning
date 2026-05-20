# Git 工作流练习

> 在开始之前，先看看仓库当前状态：
> ```
> git status
> git log --oneline
> git branch
> ```

## 第1题：看懂当前状态

**目标**：理解 `git status` 输出的含义

先执行：
```bash
git status
```

你会看到文件分两区：
- **暂存区（Staged）** — 标记为绿色的文件（AM 状态），已经 add 过了
- **工作区（Working）** — 标记为红色的文件（?? 状态），还没被跟踪

**任务**：
1. 执行 `git status`，看看哪些文件已经暂存了
2. 哪些文件还没被跟踪

> 不用操作文件，看懂就行。

## 第2题：从 main 分支分出开发分支

**目标**：学会建分支、切换分支

目前所有人都在 main 上改，这是坏习惯。正确的做法：开发新功能时建一个新分支。

```bash
# 创建并切换到新分支（一步完成）
git checkout -b practice/git-workflow

# 或者分两步：
# git branch practice/git-workflow    # 创建分支
# git checkout practice/git-workflow  # 切换分支
```

**任务**：创建并切换到 `practice/git-workflow` 分支

做完后执行 `git branch` 确认当前在哪个分支。

## 第3题：暂存并提交

**目标**：学会 add + commit 的完整流程

目前工作区有很多未跟踪的文件（?? 状态）。挑几个提交。

```bash
# 查看有哪些未跟踪的文件
git status

# 暂存单个文件
git add phase1/week1/git_practice.md

# 暂存某个目录下的所有文件
git add phase1/week1/*.py

# 提交（写好说明）
git commit -m "提交说明"
```

**任务**：
1. `git add` 暂存你想保存的文件（至少 3 个）
2. `git commit -m "练习提交"`
3. 执行 `git status` 确认提交成功

> **提交说明规范**：简短的英文或中文说明，说清"做了什么"
>
> 示例：
> - `feat: 添加git练习文件`
> - `练习：完成git工作流练习`

## 第4题：推送远程

**目标**：学会把本地分支推送到 GitHub

```bash
# 第一次推送新分支，需要 -u（建立跟踪关系）
git push -u origin practice/git-workflow

# 之后推送，直接 git push 就行
```

**任务**：把 `practice/git-workflow` 分支推送到 GitHub

推送成功后，在浏览器打开 GitHub 仓库，应该能看到这个分支。

## 第5题：查看提交历史

**目标**：学会查看 git 提交历史

```bash
# 查看最近5条提交
git log --oneline -5

# 查看所有分支的提交历史
git log --oneline --graph --all

# 查看某个文件的修改历史
git log --oneline -- phase3/week1/git_practice.md
```

**任务**：
1. 用 `git log --oneline --graph --all` 查看所有分支的历史
2. 确认你的提交在历史中

## 第6题：合并分支

**目标**：学会把开发分支合并回 main

在 `practice/git-workflow` 分支上做完练习后，合并回 main。

```bash
# 先切回 main 分支
git checkout main

# 把 practice/git-workflow 的改动合并进来
git merge practice/git-workflow

# 推送到远程
git push
```

**任务**：
1. 切换回 main 分支
2. 合并 `practice/git-workflow` 到 main
3. 用 `git log --oneline -5` 确认合并成功

## 第7题（选做）：删除分支

**目标**：学会清理用完的分支

合并之后，开发分支就可以删了。

```bash
# 删除本地分支
git branch -d practice/git-workflow

# 删除远程分支
git push origin --delete practice/git-workflow
```

> `-d` 会检查分支是否已合并，没合并会拒绝删除。如果确定要强制删，用 `-D`。
