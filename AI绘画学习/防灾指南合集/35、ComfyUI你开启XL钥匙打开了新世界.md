![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At5WWPHUPkYwQ2s3ThTehqVEkUEHyLX1JpstVVr1MSqe7r79gG3Gzv9f009dK8RFBbqicg1KcyR9STw/0?wx_fmt=jpeg)

#  ComfyUI，你开启XL钥匙打开了新世界

原创  暴躁的卡爷  [ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5WWPHUPkYwQ2s3ThTehqVEcarf6f4U2TojVEh3XwtMXAnYOAHoHU7HVHZfv3BfCibFoIjtCS6abUg/640?wx_fmt=png)

今天要开一个深坑了，最早在三四月份做相关产品的时候，就有大佬跟我说，节点式生成的 **ComfyUI** 解决了很多 **webUI**
蛋疼的一些交互和逻辑，未来可期，让我留意，当时很是认可，但也一直没空研究。

直到SD发布了XL1.0后，ComfyUI再次用它优秀的底层逻辑率先打击了臃肿不稳定的WebUI1.6，成为更适合“体验”XL的SD生图工具。如果要给这个“体验”定义更严格生产一些的话，那可以说是最佳工具，没有之一。

但在与大家一起努力学习，了解了ComfyUI后，我有点难以抑制的激动，我觉得之前称呼这个“开启XL大门的钥匙”有些欠妥，它应该是开启AIGC新世界大门的钥匙！
![](https://res.wx.qq.com/t/wx_fed/we-
emoji/res/v1.3.10/assets/newemoji/Fireworks.png)
![](https://res.wx.qq.com/t/wx_fed/we-
emoji/res/v1.3.10/assets/newemoji/Fireworks.png)
![](https://res.wx.qq.com/t/wx_fed/we-
emoji/res/v1.3.10/assets/newemoji/Fireworks.png)

** 所以决定，这个坑要挖了，且毅然决然的往里跳了  ** 。在过去的一周中，我已经用ComfyUI平替掉了大部分WebUI的生图工作。
还卖掉了12G显存的3060，只留了一台8G的3070，使用ComfyUI+云端SD完全够了
。还新获得了很多有如魔法一般的工作流（指的是ComfyUI's workflow)，这让我对扩散模型进行aigc有了新的认知。所以以后应该也会是
**ComfyUI作为创造主力C，WebUI打野辅助** ，  MJ中单负责GANK  ，我给他们包鸡包眼，端茶送水付电费就好。
![](https://res.wx.qq.com/t/wx_fed/we-
emoji/res/v1.3.10/assets/Expression/Expression_93@2x.png)
![](https://res.wx.qq.com/t/wx_fed/we-
emoji/res/v1.3.10/assets/Expression/Expression_58@2x.png)

我已经迫不及待的想把它安排(li)给你们了。

##  ** **** ** ** ** ** ******** ** ** 可以选择的新世界  ** ** ** ** ** ** ** ** ** **
** ** **

至于很多人跟我一样，觉得密密麻麻有如电路板一样的操作界面太劝退了，我这两天在学习的过程中思考了一下，我准备之后的文章都会提供2套思路，分别是：

  1. ** 🤔A航线  ** 有webui的底子，想了解生图过程，能 **举一反三，进阶学习** 的。 

  2. ** 🤓B航线  ** 喂饭都不想吃，我只想 **无脑使用** ，出图效果好的。    

如果跟随  《  [ Stable Diffusion 防災指南
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484593&idx=1&sn=28186490d02d1f6376e10d549c8f480d&chksm=97a43280a0d3bb968a1988fb3ad41c30b3698dd9d9316a3b38bc32d41838f1988f4400de24ee&scene=21#wechat_redirect)
》  一路学习过来的朋友可以选择 **A航线**
继续跟随卡爷的节奏进入ComfyUI新世界，而对ComfyUI本身兴趣不大，但对比WebUI还简单无脑的生图很需要，直接跳过下面A部分，滑到后面的
**B航线** 就行，按需食用即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5WWPHUPkYwQ2s3ThTehqVEjPBZD7RlzPPeMwI7icf8QRpveXQA1Zu5Uk2H8icGuVjVPwIusFrKvMZA/640?wx_fmt=png)

  

** **▍ ** **第一次生成** （ ** ** ** ** ** A航线 ** **** 🤔）  ** ** ** ** **

在进行ComfyUI的第一次生成前还是有很多准备工作的，考虑走A航线的大家已经是AI栋梁了，就不再像以前一样喂饭了，不过我们还是需要先基本了解一下:

  * ComfyUI是什么 
  * 如何在本地安装ComfyUI 
  * 一次基本生成（txt2img）的工作原理（ **尤为重要** ） 
  * 进行一次基本生成 

##  ** **** ** ** ** ** ******** ** ** 1\. ComfyUI  ** ** ** ** ** ** ** ** **
** ** ** **

A powerful and modular stable diffusion GUI and backend（一个强大的、模块化的Stable
Diffusion GUI和后端）作者是这么开场白的。

ComfyUI主要使用基于图形/节点/流程图的界面来设计和执行进阶的SD管线。所以我们可以简单的理解过去我们在webui中一个按钮和几个设置操作的工作部分，需要在ComfyUI中进行workflow的连接。而SD在整个扩散生成的过程，每一个工作环节都将颗粒度变小，最小单位是一个或者多个参数组成一个节点块。多个节点块构成一个生成步骤。多个生成步骤拼起来是一次任务，而若干个任务就能解决无穷无尽的需求了。

就好像从蛋白质形成细胞，到器官，到人体，人体组成家庭，家庭构建社会...一样可以进行更多的组合，这里就充满了创造和想象，这也是ComfyUI领先于WebUI的逻辑所在。一会在工作原理上会再详细介绍。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5WWPHUPkYwQ2s3ThTehqVEtquOfIjYic7h3AO9fXeicPwvHJwBgsVV0Oiac3hbXKeGZp5cAzIpjX2jg/640?wx_fmt=png)

这样你大概率可以完成这样你在webui想都不敢想的操作：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5WWPHUPkYwQ2s3ThTehqVES6CUcfkNk3nzh3wQEHwibqVkx98CwQzgY1j7KbyDtbPRFVXsctCt91A/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5WWPHUPkYwQ2s3ThTehqVEnPX4oI8xaxLvHWNf44PdfEAwnMib046rgprl7ibgyGD7IbUSqFsx7Q0A/640?wx_fmt=png)

官方的特征介绍（我把主要的列出来）：

  * 节点/图形/流程图界面，用于实验和创建复杂的稳定扩散工作流程，而无需编写任何代码。 

  * 完全支持 SD1.x、SD2.x 和 SDXL 

  * 异步队列系统 

  * 仅重新执行在执行之间更改的工作流部分（节省计算资源） 

  * 甚至可以使用cpu进行生图（很慢），可以在小于3G显存的GPU上运行 ` `

  * 可以加载 ckpt、安全张量和扩散器模型/检查点。独立的VAE和CLIP型号。 

  * 嵌入/文本反转 

  * 从生成的 PNG 文件加载完整的工作流（带有种子）。 

  * 将工作流保存/加载为 JSON 文件。 

  * 启动速度非常快。 

  * 完全离线工作：永远不会下载任何内容。 

  * 设置模型搜索路径，可以复用设备上的其他路径里的模型文件。 

  

##  ** **** ** ** ** ** ******** ** ** 2\. 安装  ** ** ** ** ** ** ** ** ** **
** ** **  

** 直接下载  ** 官方提供了一个window版的解压即用，（像不像懒人包？就是），复制下面链接即可下载，大小1.35G（不含模型），版本121.  
https://github.com/comfyanonymous/ComfyUI/releases/download/latest/ComfyUI_windows_portable_nvidia_cu121_or_cpu.7z
** 手动部署  ** 需要先确认 **python** 安装（有webui这里应该都有装好）， **pytorch** （  注意：pytorch
尚不支持 python 3.12，因此请确保您的 python 版本为 3.11 或更早版本）  
git 克隆comfyui到本地。打开windows的cmd，然后输入下面：

  * 

    
    
    git clone https://github.com/comfyanonymous/ComfyUI.git

至于如何安装pytorch，以及Linux，Mac OS如何安装，受限篇幅，我就不多废话，上面clone的地址上有详细说。  
所以综合来看，ComfyUI在部署上其实比WebUI反而更容易。  **修改** ** 配置-使用WebUI的模型共享  **
上面特性有介绍设置模型搜索路径，可以复用设备上的其他路径里的模型文件。你只需要部署好ComfyUI后进入文件夹中找到下面这个文件。（记事本打开，也可以把.example删掉再打开）

ComfyUI/extra_model_paths.yaml.example

把base_path: 后面改成你webui的根目录就行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6THAskDAAulLI2yYgxiaJjk12iaLO1wcyukuVSczjzficanFGibJuibM83iagAxbM0Ra4fTpZDp7mwhpGg/640?wx_fmt=png)

  
** **** ** ** ** ** ******** ** ** 3\. 一次T2I的工作原理  ** ** ** ** ** ** ** ** **
** ** ** ** ** **** ** ** ** ** ******** ** ** *  ** ** ** ** ** ** ** ** **
** ** ** **  

这部分很重要，这部分是使用好ComfyUI的核心，可以说是基本功，只要了解了扩散模型的工作原理，你才能自己拼装出来能应付所有需求的工作流。

先倒退回最早学习SD扩散模型的理论知识（现在回想起来，当初可能真的是学了个寂寞啊，文章也是囫囵吞枣，重点还是看引用链接吧）传送门：  

[ Stable Diffusion的工作原理（理论篇）
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484513&idx=1&sn=ff202f639dab537dedb3542fea9580e7&chksm=97a43250a0d3bb460e3f21df12c178865f9c293b7604328239bf5fc2a18f5b2590fbc6538f32&scene=21#wechat_redirect)  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5WWPHUPkYwQ2s3ThTehqVEd62vkKEReNjEuibwbbgbVd2ichbrWJkOze0Ls4CJKmZvuGaCvicprQKlQ/640?wx_fmt=png)

我基于自己的理解重新做了一张更好消化的原理流程图。里面红色部分也是ComfyUI的节点重要组成部分，就像乐高的基础模块了。

** 编码器  ** （Encoder）：文本也好，图片也好都需要经过一个编码器才能变成机器认识的语言。尤其是图片，与文本的编码不一样，这个我们图生图再说。

** 采样器  **
：这里名词不是很严谨，但为了方便你学习ComfyUI，你就把带有算法，在潜空间一顿操作的玩意儿叫采样器，图片尺寸，采样步数，采样算法，潜空间种子等一系列的设置也都在这部分完成。

** 解码器  ** ：经过潜空间操作之后变成噪点的这一堆玩意儿，还需要一个解码器才能重新变成图片。

** 加载器  **
：这是为了工具而设立出来的一个东西，因为模型我们需要有个盘子装起来，所以需要加载checkpoints，lora，controlnet模型，甚至图片，在comfyui里都统称加载器。

  

整个原理有个不恰当的比喻就是：  

** 就像你虚着眼睛看一张图，这个图在潜空间里重新一顿洗牌，码牌，等你把眼镜一带，哇，图生出来了  ** ！

  

  

** **** ** ** ** ** ******** ** ** 4\. 进行一次基本生成  ** ** ** ** ** ** ** ** ** **
** ** **

好了，4个器皿你都get到了。这个时候我们再打开ComfyUI，这下默认的这个组合你就很容易认识了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5WWPHUPkYwQ2s3ThTehqVEVb8M9a2YI5ugGMicHkWqZaNxLp8zP1CuwqEDoLwUGrvl3RRpLonrNew/640?wx_fmt=png)

如果没有默认工作流，可以从B航线窃取，ComfyUI官方特性就提到了最好用的“拿来主义”，也是 **B航线能成立的原因** 。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5WWPHUPkYwQ2s3ThTehqVEa8WZoALXAWQ0iaibc8R94pKiaUFmJicTu2G1icm4dJrtfGQD0yicoZLOpKng/640?wx_fmt=png)

如果你对于不是中文有些苦恼，也没关系，先认识这几个单词也没坏处，之后会在插件那期专门提供汉化插件的安装。

最后，就只需要选择需要的模型，随便设置一下熟悉的参数，在正向关键词里填入你想要描述的英文prompt。点击默认在右边dock住的菜单栏上的queue
prompt按钮。（快捷键Ctrl+Enter）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5WWPHUPkYwQ2s3ThTehqVEFhUpCUjjmUvJ9ywd3zY63Rq67Pdk353Ay63VhholvblPqDPL1YpKBA/640?wx_fmt=png)

你会目送，程序从加载器开始加载模型，快速的clip编码进入采样器开始跑进度条，最后从解码器解码出来放入保存的图片容器中。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5WWPHUPkYwQ2s3ThTehqVEgSMa79xhEw764fW3fAVPRScorOxic8ldZADwN8qo226ugsNDY9oiaKjA/640?wx_fmt=png)

你ComfyUI的Hello world 就！！了。

  

  

** **** ** ** ** ** ******** ** ** **▍ ** **第一次生成** （ ** ** ** ** ** B航线 **
**** 🤔）  ** ** ** ** ** **** **  
** ** ** ** ** ** ** ** ** ** ** ** **

  

B航线就不用动脑子了，也不用管ComfyUI怎么工作的，最多先进行一次安装，如果安装都不想做，你可以更我一样选择在线云，打开浏览器就能使用comfy。

** **** ** ** ** ** ******** ** ** 安装  ** ** ** ** ** ** ** ** ** ** ** ** **

复制下面链接，你就获得一个纯净的官方comfyUI。老样子，我也会在文末提供网盘下载。至于手动部署就算了，太复杂。

https://github.com/comfyanonymous/ComfyUI/releases/download/latest/ComfyUI_windows_portable_nvidia_cu121_or_cpu.7z

** **** ** ** ** ** ******** ** ** 导入工作流or图片  ** ** ** ** ** ** ** ** ** ** **
** **

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6THAskDAAulLI2yYgxiaJjkia3oeNUqy3Pia0CQIZoIKK5aTbEXBq5H0sIXtpQRE8m41hZD4QiaPdOicg/640?wx_fmt=png)

第一次进入你大概看到这样一次生成，如果不是也没关系，不用自己重新连接一遍。只需要把我下面这张图片拖拽进入ComfyUI中，你就会获得这个图片生成的完成工作流（包含使用模型，prompt，参数，种子，甚至节点布局都是像素级的还原。）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6THAskDAAulLI2yYgxiaJjkwUVLMAaricb5B21cyMaFUk8K1SoFzFGPPCiazYUDRwPaly8Uzhgfp5YA/640?wx_fmt=png)

微信压缩了图，你大概率要从下载中获得原始图片和工作流的json文件。

** **** ** ** ** ** ******** ** ** 傻瓜式操作  ** ** ** ** ** ** ** ** ** ** ** **
**

将工作流or图片导入后，看下图，你只需要操作：

  * 选择模型。（可默认）   

  * 填写关键词（负面关键词可以默认） 
  * 设置图片尺寸。（默认512x512)   

  * 设置图片参数（捷克默认）   

  * 点击最右边的第一个按钮，就可以目送你的图片从左到右的进行生成工作了。   

** 全程甚至只需要填写正向关键词这一步操作就行  ** ，和webui一样，比webui还流畅，还直观，甚至更简单的生成动作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6THAskDAAulLI2yYgxiaJjkC8Wknvu1HCGic3q8vg2X6fiaPRcBGAyGDqrF3nYXn2oCw6UyJe1icImgg/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** 中文设置  ** ** ** ** ** ** ** ** ** ** ** **
**

使用 **暴躁鱼干在线云** 学习使用ComfyUI的只需要在生图控制台右上角点击设置⚙图标，然后在设置菜单中找到语言设置，切换成中文就行。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6THAskDAAulLI2yYgxiaJjk4fIyb6ydiadNicG32Gjnk0UxX5vKZLXct12diaRHIficrqZkyOriaMn47tg/640?wx_fmt=png)  

没用使用 **暴躁鱼干在线云** 的暂时不要着急我们后续插件篇会提到如何安装UI汉化插件的。

  

好了，AB航线都启航了，万事开头难，ComfyUI这个头还是比使用14篇基础知识堆砌而出来的WebUI开端-防灾指南要容易得多了。

如果你都已经开始着急更多WebUI上熟悉的功能了，那么恭喜你，你上道启航了，好的开始，我们下一篇见！~

  

  

** 最后  **

** 在线  ** 云服务地址:  ** aifish.vip  ** 。

如果对SD防灾对策群感兴趣的也可以关注公众号给 **【小鱼干了】** ，通过公众号的自动回复 **加群** ， **加好友** ，获得
**在线SD云服务** 等操作。  ****

本期文章提到的ComfyUI安装包、PNG信息图片和工作流，可以公众号回复【下载】获得资源。

  

下期见！~

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5wtvRxKRkN4GWicE93NRia42mINp8NB5HRDKfsnj48CgOiaReyfq5NjYNzTyq80PiczoianApmUnpTsNA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

微信扫一扫  
关注该公众号



轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6iciciaKY5WZ4ib8CVibVnVHRJwGj6ksg7fk0tzTMuLPsvptv6zswtKfCLNFwYr9aIBGkjiaYGBWtibwnOQ/0?wx_fmt=png)

小鱼干了







****



****



  收藏

