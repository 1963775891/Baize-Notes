![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At4Ar9MO2OUTOkyiaeFTRbIk3kVcgiaOuosJcdY2rvQy2ancVLH01nDq0028GYpxC9lWNpTlsxrAlfkw/0?wx_fmt=jpeg)

#  ComfyUI-ControlNet不能漏啊！~

原创  暴躁的卡爷  [ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

之前讲comfy放大的时候就留了使用CN的tile放大的扣子，今天群里就给我上了一课。  布佬一本正经的告诉我，她有物理放大的法宝...
非要让我推荐给你们。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4Ar9MO2OUTOkyiaeFTRbIk3P4X8xN5Ge20hcVPuwOyyQZqPQ8c5saXlLq3AibF8uPX2YEU5atKTngw/640?wx_fmt=png)

推荐的很好，以后不要推荐了。能物理放大我这里还有更高明的办法，连眼镜放大镜显微镜都不需要。你把 **脸凑近点** 就能30焦段转50焦段了。
![](https://res.wx.qq.com/t/wx_fed/we-
emoji/res/v1.3.10/assets/Expression/Expression_41@2x.png)

好了，不扯闲皮，今天把ControlNet安排了，Comfy就算进阶完毕了。不过ControlNet因为预处理模型众多，所以B航线会有些为难。所以还是会以当前最常用的tile
放大控制画面，tile细节添加来实现高清放大的方式为例子。

算是补充了之前挖坑的其他放大方法吧，这个方式webui同样适用（之前一直忘了提）。

  

还是老样子，AB航线提供选择。

  1. ** 🤔A航线  ** 有webui的底子，想了解生图过程，能 **举一反三，进阶学习** 的。 

  2. ** 🤓B航线  ** 喂饭都不想吃，我只想 **无脑使用** ，出图效果好的。 

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5WWPHUPkYwQ2s3ThTehqVEjPBZD7RlzPPeMwI7icf8QRpveXQA1Zu5Uk2H8icGuVjVPwIusFrKvMZA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

  

** **▍ ** **** **** **ControlNet** ** ** ** ** （ ** ** ** ** ** A航线 ** **** 🤔）
** ** ** ** **

** **** ** ** ** ** ******** ** ** 基础CN应用  ** ** ** ** ** ** ** ** ** ** ** **
**

我们还是老规矩，手动连接一遍。  先把常规的生图连接好。  稍微不一样的是controlnet是在  clip时
生效的。所以我们把生成过程可以分成两部分。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4Ar9MO2OUTOkyiaeFTRbIk3UtQj5lrap9NbAMDjCyzpRy9hqcI84NM1NNGSDthfz7CaOtibx1Ye7yA/640?wx_fmt=png)

  
我们可以通过右键新建一个controlnet应用。新建-条件-controlnet应用，它长这个模样。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4Ar9MO2OUTOkyiaeFTRbIk3chib5e715r1ktroNA269N7Gicl9SC1SgBx46n7Vd7Hib6pprxHDa1X8oQ/640?wx_fmt=png)

  * 橘色点点分别从关键词进，经过cn离开连接到采样器中。   

  * 青色点点是连接cn模型的，拖拽点点一拉就知道。   

  * 蓝色点点就是需要上传的图像的，且需要连接cn的预处理器。（这里是重点和难点） 

所以CN连接进comfy的流程大框架上很简单。因为CN基本上是针对正向关键词的，条件部分只需要正向关键词连接，如果你对CN的进出时间有要求，可以采用高级CN应用。如下图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4Ar9MO2OUTOkyiaeFTRbIk3y8XWhvzkchjsoU1jpC8qVuSXRkiaibU3DWkVxcDhl1OTDpu9yrMxODLw/640?wx_fmt=png)

剩下的就是连预处理器部分了。这里需要安装预处理模型插件。我在模型插件篇就已经提前提及comfy的CN预处理模型如何安装，且大概有些什么功能。可以传送门了解一下：  

[ ComfyUI进阶前必备插件们续
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247486056&idx=1&sn=52cdd5e70195642855a0a4bbb17c8b60&chksm=97a43c59a0d3b54fb8fc0f0be338dd114578ee827ac5de09a3379f37b70c0a128599eb64a1a4&scene=21#wechat_redirect)
>>>

请安装 **aux** 不要装错插件了，  不要下载ControlNet Preprocessors，  安装好之后，右键新建里面就会出现CN的预处理器：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4Ar9MO2OUTOkyiaeFTRbIk3nxIQlMQYwtnFgjR3hOicL3xX5flfHtuwOa24ticnoBGtmpEk04uJ4m6Q/640?wx_fmt=png)

这里面有当下CN版本最新最主流的预处理，包括DW面部手部姿态，上色等。直到写文章的今天我才发现有一个AIO Aux 预处理器。这个AIO就是all in
one。 所以无脑选这个预处理器就行了。

再给预处理连接一个上传图片节点，（如果需要可以增加一个缩放）和一个预处理器的预览节点。这样，整个CN我们就连接完毕了。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4Ar9MO2OUTOkyiaeFTRbIk3YSskpNmcnDNTyGPicGiaomosoDKUZANG14yh7STXQj5iboGsNcrfIf7Dg/640?wx_fmt=png)

是不是很简单！~  

最后别忘了，如果是图生图的CN，需要将上传的图片再经过一次VAE编码连进K采样器的Latent中，以获取图片尺寸。

**CN的组合**  

这个官方的连线应该一下就能看明白，甚至不用纠结webui是否开启多个CN单元。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4Ar9MO2OUTOkyiaeFTRbIk302DlSPEeicRrZAohcNMuHSVp4yf7hfIEvF5moRK6GQmpv6jmzMuYDaw/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** Tile放大（进阶组合）  ** ** ** ** ** ** ** ** ** **
** ** **

这大概是我们首次进行复杂的任务串联工作流了。我们先拆解一下需求，我们要通过普通文生图产生一个觉得不错的图片然后将这个图片进行放大，使用的是CN的tile锁住结构，然后补充细节。

所以整个步骤是先连接一次普通生成。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4Ar9MO2OUTOkyiaeFTRbIk3uCmnFTUKgIKEqdnnbH9Vml4oBgePMibNeBYIYeRPHdn8LezFjJtPnYw/640?wx_fmt=png)

然后再基于这次生成的图片进行一次图生图的CN生成。

需要注意的是图片进入CN预处理前需要进行放大操作，这里放大2倍。预处理选tile，模型选tile模型。 同样别忘了将图片连上vae编码连进latent。

** **** ** ** ** ** ******** ** **
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4Ar9MO2OUTOkyiaeFTRbIk3EZRwcXOueG72xS1OcgKX60M1PqQnuUT4Cdjg9DjjB0yPGKfnicCo6dg/640?wx_fmt=png)
** ** ** ** ** ** ** ** ** ** ** ** **

但因为我们只是单纯的放大，增加细节，所以关键词和模型以及VAE都直接复用第一次生成的就行了，所以上面蓝色部分保留，紫色部分连接上上上一张图的紫色部分。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4Ar9MO2OUTOkyiaeFTRbIk3LRclP0GctVILmD7EMtPqyAOD54MCEu489KnJPuialkCv3ibJvzC32Wzg/640?wx_fmt=png)

跑一次看看。

哇奥！~ 大功告成！~  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4Ar9MO2OUTOkyiaeFTRbIk3hTicuF0icUCHFa0xYK7a7EtXX72H2F8MDE8NmD5JibjRTSGzDMZJnhAYw/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** **  
** ** ** ** ** ** ** ** ** ** ** ** ** **

** **** ** ** ** ** ******** ** ** **▍ ** **高清放大** （ ** ** ** ** ** B航线 **
**** 🤔）  ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

** **** ** ** ** ** ******** ** ** 导入工作流or图片  ** ** ** ** ** ** ** ** ** ** **
** **

CN的基础工作流：（以深度预处理器为例）最后图片没有进行放大，细节少了点，可以自行复习放大操作。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4Ar9MO2OUTOkyiaeFTRbIk3EZRwcXOueG72xS1OcgKX60M1PqQnuUT4Cdjg9DjjB0yPGKfnicCo6dg/640?wx_fmt=png)

CN的复杂多任务串联工  作流：（tile放大）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4Ar9MO2OUTOkyiaeFTRbIk3LRclP0GctVILmD7EMtPqyAOD54MCEu489KnJPuialkCv3ibJvzC32Wzg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4Ar9MO2OUTOkyiaeFTRbIk3VXAQtib0Z9G8Oz8zkzMZfOF4Vz9AB2wibncDIKaY6wIxqvyW60thWQNA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4Ar9MO2OUTOkyiaeFTRbIk3nzEH8Fib8lJia6yNyAxbddibUjDGUwfQqHObPAWx1D3v7drDm3RyzN4GQ/640?wx_fmt=png)

图片或者workflow的json文件，取走任意一种导入就能使用啦，B航线简直不要太简单！~

  

** 最后  **

如果对SD防灾对策群感兴趣的也可以关注公众号 **【小鱼干了】** ，通过公众号的自动回复 **加群** ， **加好友** ，获得
**最新AI绘图信息** 等操作。  ****

本期文章提到的PNG信息图片和工作流，可以公众号回复【下载】获得资源。

  

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

