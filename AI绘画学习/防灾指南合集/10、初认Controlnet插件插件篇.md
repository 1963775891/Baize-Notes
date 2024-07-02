![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At70hicCwGDKPXXyet43lAwQSVZ4DdibNYfag8hyCnfICqKTtElKODsNhquWlgibKlBNDBMq8jxv9QZyQ/0?wx_fmt=jpeg)

#  初认Controlnet插件（插件篇）

原创  暴躁的卡爷  [ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

** **▍** ** 认识插件ControlNet  ** **

ControlNet算是当前SD领先MJ的基于WebUI的核心插件之一，所有所谓的控制力皆源自这个插件。如果SD和WebUI基础还不清楚的可以点击链接从零开始学。

[ ** Stable Diffusion 防災指南 ** ＞  ** ＞  ** ** **
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484593&idx=1&sn=28186490d02d1f6376e10d549c8f480d&chksm=97a43280a0d3bb968a1988fb3ad41c30b3698dd9d9316a3b38bc32d41838f1988f4400de24ee&scene=21#wechat_redirect)

大部分整合包都整合了整合时能整合到的最新版本co  ntrolnet插件，安装即  食  。
但由于插件更新速度太快，day级别，所以也有可能你在用的时候已经更新了更多control模型和使用体验。你可以从GitHub上手动下载插件到本地，也可以在WebUI的扩展中心，粘贴下面地址，下载，等一小会儿插件就装好了。

https://github.com/Mikubill/sd-webui-controlnet

在你的WebUI中，它大概长样。在生图参数下面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSh1BZrSlduvM6qf8c6Xf4aM602L99L3ibWDYojnx3XAD58HVX3az6gJw/640?wx_fmt=png)

  

** **** ** ** ** ** ******** ** ** 下载模型  ** ** ** ** ** ** ** ** ** ** ** **
**

插件下好之后是需要下载ControlNet专属模型的，这个一般整合包里是不带的，需要你网络“很好”的情况下，首次使用ControlNet就会自动下载（大部分人可能都会下载失败），如果失败就手动
从 ControlNet 1.1 下载模型，地址：
https://huggingface.co/lllyasviel/ControlNet-v1-1/tree/main
您需要下载以“.pth”结尾的模型文件。  将模型放入

“stable-diffusion-webui\extensions\sd-webui-
controlnet\models”中。现在1.14版本已经包含了所有“yaml”文件。您只需要下载“pth”文件。大概就这么些，每个1.3G左右。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSTic4tFKBppP0ia7PRKGzppSdHaGk81aa3bh1PqcnlxJA8I8l4VicPjbgw/640?wx_fmt=png)

  

** **** ** ** ** ** ******** ** ** ControlNet 1.1 新功能  ** ** ** ** ** ** ** **
** ** ** ** **

  * ###  **完美兼容适配 ControlNet 1.0/1.1 和 T2I Adapter 的模型**

欢呼...

  * ###  **完美支持 Web UI的 High-Res. Fix**

欢呼  ...

  * ###  ** ‍  完美支持所有 WebUI的 Img2Img 或 Inpaint 设置以及所有蒙版类型 **

欢呼...

  * ** 新的“像素完美”模式  **

如果您打开像素完美模式，则无需手动设置预处理器（注释器）分辨率。ControlNet
将自动为您计算最佳注释器分辨率，以便每个像素与稳定扩散完美匹配。欢呼...

  * ###  **用户友好的 GUI 和预处理器预览**

重新组织了一些以前令人困惑的 UI，例如“新画布的画布宽度/高度”，  现在，预览 GUI 由“允许预览”选项和触发按钮控制  💥
.预览图像大小比以前更好了。

  * ‍ 

###  **支持几乎所有放大脚本**

现在ControlNet 1.1可以支持几乎所有的  Upscaling/Tile  方法。欢呼...

  * ###  **更多控制模式（以前称为猜测模式）**

这个新功能很好用，我们将在实战篇里看到它的运用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSyA0niatMdWfPCf7RfErPCvD2S3SrD6wh6oB5A73Sk0N1jT19K9rrvgQ/640?wx_fmt=png)

  

具体三种模式分别有什么作用，如果不想啃官方枯燥的说明就看官方这张图，一眼懂。更接近control的图还是prompt的control力更强的区别。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSt25YgPM0tANicvHdibyQMbprEFp6vz0ibXqzp34ibB4NslGOFhibQq63pTA/640?wx_fmt=png)

  * ###  **Reference-Only Control**

###  现在有一个不需要任何控制模型的预处理器。它可以直接使用图像作为参考来引导扩散，看介绍感觉神了，图生图已经没意义了...虽然我还没试。

  

** **** ** ** ** ** ******** ** ** 多控制网和开启关闭  ** ** ** ** ** ** ** ** ** ** **
** **

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSj7yKSIe79arPeZ9d1zmSzUkQVPlutEibtiaA0awxkzBoEPRYlBd4BcmA/640?wx_fmt=png)

controlnet支持多个单元输入，共同生效。与关键词，LoRA一样，每个control单元都有权重（control weight）可以来控制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSxfJ5JP9LW6HlwL2d991ywX43n96jOQmWe6L53yw2ZWJNYrnAaLEIibA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSOBwDH2bicYvibrAMiciaGkxuH7AVNEZMquFSr6HOXGJPfTokpPCVqvVNkg/640?wx_fmt=png)

如果界面上4个单元都不够用，可以在设置里controlnet目录下，调整ControlNet Unit最大数量，重启WebUI才生效。

每个单元的开启很容易，把 **启用** 勾选上就立刻生效。生图可见。  

** 低显存模式  ** 针对8G及以下的显卡，可以勾上。  

画面精度高可以勾上 **完美像素模式** 。  

** 允许预览  ** 是比较老的功能了，字面意思。

  

** **▍** ** 认识Controlnet模型  ** **

** ** ** **** ** ** ** ** ******** ** ** 模型命名规则  ** ** ** ** ** ** ** ** ** **
** ** ** ** **

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSibQ8StPpDKgJcVhnXjB3ZFbLrojs0z5KtCsrumib6WkNsLQ2ibv6FdQHA/640?wx_fmt=png)

** ** ControlNet 1.1 include 14 models  ** **

ControlNet真正厉害的还是这些预处理器和模型的搭配使用，给SD的控制力提供了无限可能。那在这里先认识一下这14个官方模型，有些我用的不多，主观直白的解释不精准，以你为准，以官方文档为准。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSbxXGsYK5wl80e1NyYKXevoAUaPFiaficOkW6HeqYjBDObfdicCwPGcu6g/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** 1.Normal法线  ** ** ** ** ** ** ** ** ** **
** ** **

说实话，用的不多，主要3D很常见的法线提取，把参考图的起伏质感强化。可能是1.0效果不好，1.1应该对  normal-from-midas
有很大的改善。找不到法线，应该翻译成常规了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSgNU9ia7wjmsqWp4w6kEmWYx19MPBaib55UM2kicU2Hog7xJ7xCXeG7E2A/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** 2.Canny硬边缘  ** ** ** ** ** ** ** ** ** **
** ** **

canny用的很频繁，就是锁住描边轮廓
。需要提一下预处理器中的invert（白底黑线反色）这个预处理器同样适用在Lineart（线稿）中，老版本的CN有可能没有这个预处理器，需要去单独下载，注意。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSLC4K8MBibjhCH3DX66GmdDgwM4BAaALcOtkdtf9FU27mdpibzibiccAMuw/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** 3.MLSD直线  ** ** ** ** ** ** ** ** ** ** **
** **

MLSD用的也不多，但看官方文档，感觉好像很适合装修建筑设计等行业，能把规则的参考图提取其中的直线部分。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSYBxRl4Hebiahvic9oy7OCN2FNgduibiaia74uKPcyC1vn5ia8Qy9GffGfCeQ/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** 4.Scribble涂鸦  ** ** ** ** ** ** ** ** ** **
** ** **

顾名思义，会对参考图进行不规则的描绘，适合只需要控制大概的方式。还可以给手绘稿，场景铺调子等地方使用，很万金油。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSyib9wvDkqDjAdBbfgjQuLkLKx7XeeH6mR88jRPbuQG8GMO38b5FfjDA/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** 5.Soft Edge软边缘  ** ** ** ** ** ** ** ** **
** ** ** **

与硬边缘相似，但又不同的是更适合边缘线不清晰，材质柔和，倒角平滑的轮廓。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSlLib5iaddI98upKcwhdUKic4NWOdl8xkGPSMkATGzQhKHfQLFKvbAe1xw/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** 6.Segmentation语意分割  ** ** ** ** ** ** ** **
** ** ** ** **

使用segment的语意识别模型，能将参考图中的不同元素区分开，有助于AI理解，避免重叠交叉部分出现鬼图。但这部分的预处理模型选择比较多，表意自然也都不一样。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSQYZl9DO66A7PmDIuib0EENCKw9faoaxnLOG9zP62Ulic2zdyTyaKMCng/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** 7.Openpose姿态  ** ** ** ** ** ** ** ** ** **
** ** **

到了最常用的openpose了，二次元福音，鬼手拯救者，群people战神。能提取参考图的骨骼，最新1.1预处理器还能识别面部特征和手部骨骼。6到起飞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSfnowp8GZYfgyQdwrjnjmVbQzdMWSiasl1ycYSiaiaHCUg6JvffRIriarNQ/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** 8&9.Lineart线稿  ** ** ** ** ** ** ** ** **
** ** ** **

Lineart和canny是一对正反操作，前者对有分割，线条敏感，后者在意的是光影下的边缘。所以线稿很适合对原始线稿进行上色，很多场景下他们是相似的。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSRD8oqWicErCKEaxQuNxmhcnyEibggZ6b0K5CcBqdzwBjWXsVHrTCqsFQ/640?wx_fmt=png)

为此，专门有一个模型针对二次元处理线稿上色。Anime Lineart。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSNLGD6yjjaMqhx8rM54skloZk9s1zMNHibbFkCiculsjf6SnI7Cs0jQfg/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** 10.Shuffle随机洗牌  ** ** ** ** ** ** ** ** **
** ** ** **

感觉更像是将元素特征从参考图中提取出来，然后赋予给生成的图。预处理和模型也都就一个。随机变化性很大。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSkhLAm1sqZNPsmjDfaeiampJw4ibkVqbgFxzTesFUgNyS5HqBQC6lkEhQ/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** 11.Instruct Pix2Pix  ** ** ** ** ** ** **
** ** ** ** ** **

这个好像连翻译都翻译不出来，☞定像素to像素？看文档，使用逻辑还很复杂，我也没有尝试过，不敢乱描述，感觉像能保留参考图的一部分像素，另一种局部重绘？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSPaTo4xO4DgCuYwDFtzXKmIrUDKqcqQMB0x0ndb4egGMjwASWMETicVg/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** 12.Inpaint局部重绘  ** ** ** ** ** ** ** ** **
** ** ** **

和图生图的局部重绘撞车了！这个就比较好理解了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSuCJJqQ3yBGXQGqicwFaUuCcZiaibZibFa1ryZicDuptia8Hzfic4CtsFLQytQ/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** 13.Tile分块  ** ** ** ** ** ** ** ** ** ** **
** **

这个模型可以用在很多方面。总体而言，该模型有两种行为:

  * 忽略图像中的细节并生成新的细节。 
  * 如果局部tile语义和提示不匹配，则忽略全局提示，并使用局部上下文引导扩散。 

由于该模型可以生成新的细节而忽略现有的图像细节，因此我们可以使用该模型去除不良细节并添加精细细节。例如，消除因图像大小调整而引起的模糊。
MJ的无限放大猜测用的就是这个模型的原理。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSEZB3ibwF0k2NrqdYBOLFC3OQYTtF8zbSJ0OJjKBnbbOD2yI6EH8BluA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSNcF9BZGTQg7xTqnc5YuzR40rcJAAZribiaGaEYxBPc6VNlibVYr1ZmQJg/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** 13.Reference-Only Control  ** ** ** ** **
** ** ** ** ** ** ** **

这个是1.1的新功能，很强，能做到control又不control真的是参考的意义。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSGbF06GyQwSzg1sn6VFHE2rJ2r5PcyUajEPAuU8zJZSIvpDZTgfHpxg/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** 14.T2I-Adapter自适应  ** ** ** ** ** ** ** **
** ** ** ** **

通过预处理器，我们可以得到色块处理结果，类似涂鸦的手绘处理结果，（风格会报错，大概还没准备好）整体上感觉仍然有点像图生图找风格的场景使用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQS9FdwoJv8z32icF4bOJS6ia3iabiaKmctJrORpt5CDd1hAOufBicoFh8jCdw/640?wx_fmt=png)

自此，14个官方可下载到的ControlNet模型就都介绍完毕了，还有一些其他Con模型我们留给以后慢慢介绍吧，这些就够消化好久了。

如果篇幅太长啃不动，请持续关注我，我们实战篇见。

  

**参考** ****

* * *

  

ControlNet  |  https://github.co  m/lllyasviel/ControlNet-v1-1-nightly#model-
specification  
---|---  
  
声明，文档使用 GFDL 许可。  [ 详细声明请点链接查看
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484392&idx=1&sn=d4541799ffade58ee09370b9c1239a37&chksm=97a435d9a0d3bccf4ab397577108d2d92092259b4cf3ca877a891173f1e965c69ca52f7e7eb6&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5wtvRxKRkN4GWicE93NRia42mINp8NB5HRDKfsnj48CgOiaReyfq5NjYNzTyq80PiczoianApmUnpTsNA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

** **** ** ** ** ** ******** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

预览时标签不可点

微信扫一扫  
关注该公众号



轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6iciciaKY5WZ4ib8CVibVnVHRJwGj6ksg7fk0tzTMuLPsvptv6zswtKfCLNFwYr9aIBGkjiaYGBWtibwnOQ/0?wx_fmt=png)

小鱼干了







****



****



  收藏

