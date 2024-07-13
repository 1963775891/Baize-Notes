![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At5wtvRxKRkN4GWicE93NRia42x3bYvWNTFFCdkFu3ia1cJOVjrrYj83TUCRZyYmNtp7KIHicug55znVsQ/0?wx_fmt=jpeg)

#  安装WebUI（工具篇）

原创  暴躁的卡爷  [ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

**
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5OKCwshyLbLgyYkUliahWcfiayuQnO6usT77dpMwZec8IKzOCWgaQ5XIRBLxIicMpgf0aBozWZs9s9Q/640?wx_fmt=png)
**

** WebUI  **

Stable Diffusion WebUi 一个基于 Gradio
库的开源工具，由个人大神automatic1111开发，并在全球开发者贡献下，成为一个强大的最主流的生产工具。在当下就是我们的主力工具了，我们争取把ta玩的比PS还6...

** 懒人包一键搞定  **

在不论是本地部署还是云端部署都已经很成熟简单了，不再像以前还需要一点程序基础自己一点点部署了。 **懒人包主要适用windows平台，其他平台往后看** 。

###  https://www.bilibili.com/video/BV1iM4y1y7oA/

这里我们主要使用B站赛博菩萨 大佬@秋葉aaaki提供的  **懒人整合包**
，里面整合了一些环境和一款人人都爱的启动器。具体的安装方法可以看链接视频，很简单，下载点点点。我们只需要记住下面几个关键词。

**懒人包** \--  包含  \-- **模型、插件** \-  & \- **启动器**

通常下载下来是个压缩文件，大概10来个G，长这样子  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5YiaH0ja7cDkQgUJt0TvhU4s1JgL9TicAFaZC6mbKlbibBqbSnnXd0xUbKGAGrwgiaXGkICDMF4QKphA/640?wx_fmt=png)

解压之后有一大堆文件夹，你不认识ta，ta也不是认识，没关系。你只需要在一堆英文文件名中找到一个中文名为： ** 启动器  **
的exe文件。双击点开得到：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5YiaH0ja7cDkQgUJt0TvhU4iaFfuhtXaMkCdjRTeUbUib32wZBWib6BdSwaSW9JIPAlTaJbDQOlbGS1Q/640?wx_fmt=png)

你暂时也不用关心这款强大的、可以自动自我更新，可以手动更新一系列webui、模型和插件的无敌好用启动器怎么用，点击那个蓝色按钮，开启你的AI世界。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5YiaH0ja7cDkQgUJt0TvhU4SvSUEia0QZwOw1yznpaINf5G9h5PIrC9MUecpnZaZb6rxSBozPbIia3w/640?wx_fmt=png)

等系统弹出一个黑色的控制台，里面开始刷刷的跑代码后，可以起身上个厕所（1-2分钟加载）后你的浏览器会自动弹起，打开一个http://127.0.0.1:7860/的标签。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5o0HTbIK7RfJ1moIjmIF91WnsRiaL7adfsXyguCCnNXbTJUIhxQB7ibSOtezXFKOAEfKwAa1UhwECg/640?wx_fmt=png)

整合包可能长这样：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5YiaH0ja7cDkQgUJt0TvhU4SFUdyUbtOyEHWnyDW4Qzqrx1ia9r3hKeCeFoFObHZ1mUW7Nz3OFxWAA/640?wx_fmt=png)

喔！~你的工具已经Ready了！~

  

###  ** WebUI 原生安装  （Windows平台）  **

请做好 C 盘暴涨 15GB 的准备。因为懒人包太好用了，原生安装和Linux平台同理，有需求的人可能不打需要被指南，我就简单搬运一下stable-
diffusion-book的内容。

首先，您需要下载安装 Python-3.10.6，使用管理员身份安装，安装务必勾选 Add Python to PATH 。然后安装 git 下载
stable-diffusion-webui 仓库，例如运行 git  clone  https:
//github.com/AUTOMATIC1111/stable-diffusion-webui.git  在 Windows
资源管理器中以普通用户（非管理员）身份运行  webui-user  .bat  然后，您需要进入这个文件夹，并运行 webui-
user.bat这个过程可能需要一些时间，请耐心等待。

  

** WebUI 原生安装  （Mac 平台）  ** ****

如果你是 Mac 系统，请查看此教程进行安装，文末有github原始文档链接。

原生安装都需要注意网络是否能稳定访问Github等国际网站，以下安装都是默认打开  终端ap  p的。

大概安装步骤是：  

  1. 如果未安装 Homebrew，请按照 https://brew.sh 中的说明进行安装  。在终端窗口输  入  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/  install  /  HEAD  /install.sh)  " 

  2. Homebrew安装完毕后，打  开一个新的终端窗口并运行brew install cmake protobuf rust python@3.10 git wget 

  3. 通过运行克隆 Web UI 存储库git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui 

  4. 将要使用的稳定扩散模型/检查点放入中。关于模型部分，可以参考 合集中的模型篇部分，后面也提供了2个模型，可以任选一个下载放入路径stable-diffusion-webui/models/Stable-diffusion 

  5. cd stable-diffusion-webui然后运行 Web UI。将使用 venv 创建和激活 Python 虚拟环境，任何剩余的缺失依赖项将自动下载并安装。./webui.sh 

  6. 若要稍后重新启动 Web UI 进程，请再次运行。请注意，它不会自动更新 Web UI;要更新，请在运行 之前运行。./webui.shgit pull./webui.sh 

NovelAI: https://huggingface.co/a1079602570/animefull-final-
pruned/blob/main/novelailatest-pruned.ckpt

SD1.5: https://huggingface.co/runwayml/stable-
diffusion-v1-5/blob/main/v1-5-pruned.ckpt

  

##  ** 了解WebUI目录  **

📁 .

    
    
    ├── 📄 config.json  
    ├── 📄 environment-wsl2.yaml # Windows Subsystem for Linux 的环境配置  
    ├── 📁 embeddings # 存储embedding模型的目录  
    │   ├── 📄 place textual inversion embeddings here.txt  
    ├── 📁 extensions  # 插件目录│   ├── 📄 put extensions here.txt  
    │   └── 📁 stable-diffusion-webui-localization-zh_CN  
    ├── 📄 launch.py  
    ├── 📄 LICENSE.txt  
    ├── 📁 models # 存储各类模型的目录  
    │   ├── 📁 aesthetic_embeddings # 美学嵌入模型  
    │   ├── 📁 Codeformer  
    │   ├── 📁 deepbooru # 深度图库标签分类模型  
    │   ├── 📁 ESRGAN # 增强超分辨率生成对抗网络模型  
    │   ├── 📁 GFPGAN # 基于 GAN 的人脸修复模型  
    │   ├── 📁 hypernetworks # 超网络模型  
    │   ├── 📁 LDSR # 轻量残差网络模型  
    │   ├── 📁 Lora # Lora 模型  
    │   ├── 📁 ScuNET  
    │   ├── 📁 Stable-diffusion # 稳定扩散模型  
    │   ├── 📁 SwinIR # 轻量级基于 Swin Transformer 的增强超分辨率模型  
    │   ├── 📁 VAE # 变分自编码器模型  
    │   └── 📁 VAE-approx # 变分自编码器的近似计算模型  
    ├── 📁 outputs # 存储各类输出结果的目录  
    │   ├── 📁 img2img-grids # 由图生图模型生成的网格图（2x2）  
    │   ├── 📁 img2img-images # 由图生图模型生成的图像  
    │   ├── 📁 extras-images # 额外的生成图像  
    │   ├── 📁 txt2img-grids # 由文本生图模型生成的网格图（2x2）  
    │   ├── 📁 txt2img-images # 由文本生图模型生成的图像  
    │   └── ... # 其他目录  
    ├── 📁 repositories # 目录缓存  
    ├── 📄 requirements.txt # pip项目依赖  
    ├── 📄 style.css    
    ├── 📄 styles.csv  
    ├── 📄 styles.csv.bak  
    ├── 📄 ui-config.json  
    ├── 📄 webui.bat # Win 运行脚本  
    ├── 📄 webui-macos-env.sh # macOS 默认环境配置  
    ├── 📄 webui-user.bat # Windows 启动用户脚本配置  
    ├── 📄 webui-user.sh # Linux & Mac 启动用户脚本配置  
    ├── 📄 webui.py   
    └── 📄 webui.sh # Linux & Mac 运行脚本  
    

对于 Windows 用户，要启动项目，只需要执行 **webui.bat** 。若需要配置环境变量或追加启动参数，则可编辑 **webui-
user.bat** 。

对于 Mac 或 Linux 用户，启动项目的方法是执行 **webui.sh** 。同样地，若需要配置环境变量或追加启动参数，则可编辑 **webui-
user.sh** 。

目录中需要认识几个文件夹已标分别标记为橙色和红色，这里不要求记住，在后续的内容可能会慢慢提到，他们对应的是 ** 插件、模型、生的图  **
存放的位置，并且懒人包中的启动器也把重要的文件夹放在了启动页面的文件夹类下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5YiaH0ja7cDkQgUJt0TvhU4iaFfuhtXaMkCdjRTeUbUib32wZBWib6BdSwaSW9JIPAlTaJbDQOlbGS1Q/640?wx_fmt=png)

  

##  ** 手动启动 WebUi  **

如果你不使用一键启动运行。那么你可以使用以下命令启动 Webui

python3 launch.py --autolaunch

如果你的显卡显存小于 8GB ，那么请附加 --lowvram 参数。

经过稍微的等待后，会输出如下类似的界面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4ZTg0vEv5ZcSylfXhflSCnibaFjKtxpoBIfkicfuJtkRI2oBM8S028ZeU5ib66xssvxWYD5xDLz1CBA/640?wx_fmt=png)

其中，http://127.0.0.1:7860 就是本地机器的链接（运行在本地机器上面），剩下的信息是大模型和嵌入模型的加载情况。

打开此地址，你会看到下面的界面：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4ZTg0vEv5ZcSylfXhflSCnxiave8Ag0GUrHvJ1hCpsrZgyia3WUp5TOlYDkIMMndJrVwGYNIMZrduw/640?wx_fmt=png)

在这个界面中，打开 extensions 选项卡。点击Avaliable二级选项卡点击
LoadFrom，然后在扩展列表中找到中文扩展并安装即可汉化界面。如果你是一键包版本，那么应该会自带中文扩展。

##  

** 安装错误处理  **  

参考合集中这篇文  章

WebUI常见问题（工具篇）

  

  

文章专业内容部分参考：

stable diffusion book  ‍  |  https://stable-diffusion-book.vercel.app/install  
---|---  
mac安装教程  
|  https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Installation-
on-Apple-Silicon  
  
声明，文档使用 GFDL 许可。  详细声明请点链接查看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4U0j2osXIvO9RdUCbNiav0ebib3KSaHPucaTwJVzcia9klFJXgEcibUSEGeb6vMjX9cibjUNo9NxQVwpg/640?wx_fmt=png)

预览时标签不可点

微信扫一扫  
关注该公众号



轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6iciciaKY5WZ4ib8CVibVnVHRJwGj6ksg7fk0tzTMuLPsvptv6zswtKfCLNFwYr9aIBGkjiaYGBWtibwnOQ/0?wx_fmt=png)

小鱼干了







****



****



  收藏

