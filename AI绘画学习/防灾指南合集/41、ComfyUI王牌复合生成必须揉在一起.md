![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At49jSInH38NQthkcE8eFWicXs6C0FDlVpQVshB6DsIziayGx4Mo0d8WHbgw599HPe1mtn70OpiaOeTzw/0?wx_fmt=jpeg)

#  ComfyUI王牌！复合生成！必须揉在一起

原创  暴躁的卡爷  [ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

上期我们讲了利用基于语言到图像的生成网络的GLIGEN模型可以做到指哪打哪的生成。  就又有猴急的comfy先驱栋梁说，这算个鸟！  
Comfy的工作流牛，就牛在可以直接串烧生成。把想要生成的前景A+前景B和背景A一起，一次性生出来。  
不演了，摊牌了，这就是对webui工作流的降维打击。王炸。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At49jSInH38NQthkcE8eFWicXHq2Zf2HBTicIFcMaGgIRibgICz2NibLicOIibyf9g68G2j4mJQKDn4z83tA/640?wx_fmt=png)

比如我也整一个沈腾老师的操场场景，人物换成妹子。且每个人都可以独立调整，就可以用这么一套工作流程串联起来。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At49jSInH38NQthkcE8eFWicXiaEWrJ1urggrInf7IMqZsDANibzyPJicLHwHmjt0f61PI5soVzSFxndZw/640?wx_fmt=png)

好像有点意思，这还只是今天主要内容-复合生成，并没有结合更多的，之前讲的CN，高清啥的再进行一次串联。潜力巨大！

  

还是老样子，AB航线提供选择。

  1. ** 🤔A航线  ** 有webui的底子，想了解生图过程，能 **举一反三，进阶学习** 的。 

  2. ** 🤓B航线  ** 喂饭都不想吃，我只想 **无脑使用** ，出图效果好的。 

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5WWPHUPkYwQ2s3ThTehqVEjPBZD7RlzPPeMwI7icf8QRpveXQA1Zu5Uk2H8icGuVjVPwIusFrKvMZA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

  

** **▍ ** **** **** **复合生成** ** ** ** ** （ ** ** ** ** ** A航线 ** **** 🤔）  **
** ** ** ** ** **

生成上没有什么需要特殊下载的插件，（如果有也是之前必备插件里包含了的）这次主要就是正儿八经的利用流的串并联完成一个完整工作流。

官方示例里称之为Noisy Latent Composition- 噪声潜空间合成。

其中关键要点：

  * Latent复合，坐标的放置。（这个上一期已经铺垫） 
  * 多次生成，每添加一个元素，增加一次生成。   

  * 串联生成需要用到K采样器（高级）。 

** **** ** ** ** ** ******** ** ** Noisy Latent Composition  ** ** ** ** ** **
** ** ** ** ** ** **

** **** ** ** ** ** ******** ** **
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At49jSInH38NQthkcE8eFWicXUV3AZCq6YDNdE0xO70aCInaR2zC2o8ICN9vbpRWy2ABQnHicoZJMGGw/640?wx_fmt=png)
** ** ** ** ** ** ** ** ** ** ** ** **

噪声潜在合成是指在图像完全去噪之前，潜伏合成在一起，同时仍然有噪声。由于在最初的采样步骤中对姿势和主体等一般形状进行了去噪，因此，例如，我们可以将具有特定姿势的主体定位在图像上的任何位置，同时保持高度的一致性。

下面是一个示例。此示例包含 4 张合成在一起的图像。1 张背景图片和 3 个主题。总步骤为 16 个。潜空间被采样 4 次，每个步骤都有不同的提示。背景为
1280x704，主体尺寸为 256x512。完成这 4
个步骤后，图像仍然非常嘈杂。然后将主体合成（粘贴）到背景上，并应用一些羽化。然后，在此合成图像上运行其余的采样步骤。

最后再进行一次图生图的放大操作，进一步避免复合生成的违和感，也获得更大的图片尺寸。

还是老规矩，跟着重新连接一遍就能轻松掌握。不过我要先讲一下这个高级采样器，这是复合生成的关键。

** **** ** ** ** ** ******** ** ** K采样器（高级）  ** ** ** ** ** ** ** ** ** ** **
** **

我们没有讲过SDXL在comfy里怎么连接的，这个很多教程已经提到过。之前转载白马的文章也有写： [
【ComfyUI】使用ComfyUI玩SDXL的正确打开方式
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247485991&idx=1&sn=4e51fe0545fb44ed9fa09f2d13493000&chksm=97a43c16a0d3b500c65ed585290c1f592399f9024c2edf1a3c8804ce72342b5c44f0bccc7502&scene=21#wechat_redirect)
>>

这里再强调一次， **SDXL官方模型的工作流程其实就是XL1.0的底模与refiner模型的串联生成完成** 。

而我们这次潜空间复合生成也同样需要，如果是串联生成就要用到高级K采样器，先看看2个采样器有什么不同。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At49jSInH38NQthkcE8eFWicXGOaSMDdmBURChWTTebzev1O7GtsWt061TjLibzJHw0zldF9wRDCxC3Q/640?wx_fmt=png)

可以很清楚的看到高级采样器可以控制降噪的开始结束步数。这就意味着两次或者多次采样可以连成一起。  

而普通采样器有一个降噪（denosie），也就是我们常翻译的重绘幅度。这个在进行图生图重绘，放大里是不可替换的。也就是说这里的高级采样器并不是真的高级了，只是单独提供给潜空间生成串联的一种特殊采样器。  

消化一下。我们开始，先创建2次生成，第一次用来生成最底层的背景，第二次用来生成前景，注意选择高级采样器。

开始步数肯定是0了，结束步数这里官方设定的是4，我自己研究了一下，因为是在潜空间生成一个大概，不能过于清晰细致，所以步数需要很少就行。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At49jSInH38NQthkcE8eFWicXktatz5ricpYoaS5OQBj2xczG3uUF8JpGzQgQFpC472iacTbyWqSNChkA/640?wx_fmt=png)

接下来这个节点就如同上一期提到的区域混合一样，它是将关键词这一层进行混合，而我们需要将图片在潜空间进行混合。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At49jSInH38NQthkcE8eFWicXHSZ5Ztxj9X6tc9mkMLtSlNhdsLPJaw2TgKhvGg92e2K1Vhg98y5Z7Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At49jSInH38NQthkcE8eFWicXiaibr6Xb9kgoGlOiahAwZI7dlUzgNibTRGLhPPZmicw0E4ojud8SBK6NI5w/640?wx_fmt=png)
|

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At49jSInH38NQthkcE8eFWicXw09gNKwnW6tTrWLSXNZt4Wc3Cpe1FsvWs6efxMQSsBs27QPmcbqzwA/640?wx_fmt=png)  
  
---|---  
  
在latent选项里找到这个latent复合节点。这个小小节点就是合成的关键。注意，目标是画布，源是主体。也就是背景连上面，前景连下面。你没汉化就看这个图to是目标，from是源。然后坐标和羽化就随意，视情况调整。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At49jSInH38NQthkcE8eFWicXlBqKVKyZqnq26ZKR9vsNHiauAog3u546CnMG3plrmGAHxa0Od5ecRyg/640?wx_fmt=png)

你也可以再添加数个前景主体。再进行一次生成完成合成。latent输出给采样器的latent输入（当然少不了模型、关键词文本编码器、解码、存图）  

注意：
**这里的采样器（高级）就要把剩下的采样步数给补上了，也就是开始降噪的步数与前面对上，结束步数如果没有后续串联的话可以设置一个无限大就行。因为总步数会限制住的**
。  

![](https://mmbiz.qpic.cn/mmbiz_png/fY8ibThH1At49jSInH38NQthkcE8eFWicXOxw7rVlNSKAqocRw13q5PBFdbpFbfvq9LzArDqnmLrtfAibEtO8qQww/640?wx_fmt=png)

最后补一个高清放大，放大获得更高质量的图是原因之一，另一个原因是再进行一次图生图可以进一步融合，提高画面整体性，减少突兀感。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At49jSInH38NQthkcE8eFWicX5QTgAqyBUOjOgULFxu2QvqnyhM0Qo8yicY5TK0vNg7hbFlwrbXMZXYg/640?wx_fmt=png)

注意这里的采样器使用是普通不带高级字样的k采样器。因为我们需要里面的重绘幅度。设置为0.4-0.6之间就好。

是不是也超级简单，（虽然我认为这已经是ComfyUI的真正进阶工作流了）拆解一下还是很简单的，也没有装插件报错的麻烦，也不用下模型被网络环境折腾疯掉，还不来试试？

** **** ** ** ** ** ******** ** ** **▍ ** **** **** **复合生成** ** ** ** ** （ **
** ** ** ** B航线 ** **** 🤔）  ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

** **** ** ** ** ** ******** ** ** 导入工作流or图片  ** ** ** ** ** ** ** ** ** ** **
** **

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At49jSInH38NQthkcE8eFWicX56CzFcVpfSWwrGZw7upqOSYBrQNmrzmglug77iclTPCK5aPgvfvZhaw/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At49jSInH38NQthkcE8eFWicXknXafPMnaLS2mf9VmdudNI9xsjNFT22d4gxCQoUIL82gMf6V8znv0Q/640?wx_fmt=png)

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

