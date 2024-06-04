## 同步Typora文件到GitHub

```sh
1.复制仓库地址：
https://github.com/yourusername/typora-notes.git

2.导航到存储笔记的目录：
cd ~/Documents_Path

3.克隆远程仓库到本地：
git clone https://github.com/yourusername/typora-notes.git`

4.进入克隆的仓库目录：
cd ~/Documents_Path/typora-notes

```

**使用命令行同步文件到GitHub**

```sh
// 打开命令提示符或终端
git status	// 查看文件状态
git add .	// 添加更改到暂存区
git commit -m "Update notes"	// 提交更改
git push origin main	// 推送更改到GitHub
```

**生成Personal Access Token**

 ```
  - Settings > Developer settings > Personal access tokens > Tokens (classic) > Generate new token
  - 设置Token名称，选择合适的过期时间（如60天）。
  - 选择需要的权限，通常需要 `repo` 权限来访问你的仓库。
  - 点击 `Generate token` 按钮。
  - 生成后，立即复制Token。因为离开页面后无法再查看这个Token
 ```

**配置Git使用Personal Access Token**

```
// 设置你的Git用户名和邮箱
git config --global user.name "yourusername"
git config --global user.email "youremail@example.com"

// 在推送代码到GitHub时，使用Personal Access Token代替密码：
// 当你运行 git push 命令时，会提示你输入GitHub用户名和密码。在这里，你需要：
- 输入你的GitHub用户名。
- 输入你的Personal Access Token作为密码。
```

**将操作简化到脚本中**

创建一个名为 `sync.bat` 的文件，内容如下：

```batch
@echo off
cd /d "C:\Users\YourName\Documents\typora-notes"
git add .
git commit -m "Auto commit"
git push https://yourusername:yourtoken@github.com/yourusername/typora-notes.git
```

确保将 `yourusername` 和 `yourtoken` 替换为你的GitHub用户名和Personal Access Token。

