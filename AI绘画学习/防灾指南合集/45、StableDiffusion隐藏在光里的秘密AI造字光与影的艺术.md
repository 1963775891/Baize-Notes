![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tyssYUEyRwx8sFGj4G5dprAgUl5ewXBKU1PBsDwTwbgicyMicTcomicnHGJXnwyicybGEFiaIeRqc9SRTrvpGhnb2cw/0?wx_fmt=jpeg)

#  【Stable Diffusion】隐藏在光里的秘密，AI造字光与影的艺术~

[ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

以下文章来源于白马与少年  ，作者吴溪源

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7eibUJEMViclLvunqf0ykvDsVwB5l1CCp96dusJbO54pVA/0)
**白马与少年** .

分享学习心得——Blender，Stable Diffusion等

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwx8sFGj4G5dprAgUl5ewXBK3rfwX2k1mUzNd3oUIAMibsM7jibKufKKHHsrnfb6H0vHkC3hAechqYJg/640?wx_fmt=png)

一张图，正常看是非常美的画面，缩小了看，就能看到画面中隐隐约约透出的几个文字，虽然经不起细细地推敲，但这恰恰就是AI绘画所独有的浪漫。

今天我们就来了解一下，这种隐藏在画里的“藏头诗”该怎么做。

先在ps中做一张任意文字的图片，黑底白字，文字可做任意变形处理，完成之后适当虚化，让边缘不至于很生硬。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwx8sFGj4G5dprAgUl5ewXBKFeGuN0dza3KVrPF9cYtuMjhwt5hT5uvgZTOjkJhpECJX2zvHvribRqw/640?wx_fmt=png)

将图片放入controlnet中，预处理器选择  inpaint_global_harmonious全局重绘  ，模型选择
lightingBasedPicture  。

控制权重我设置为0.7，介入时机为0.2，终止时机为0.6。这些参数主要控制的是文字在画面中的显眼程度，要让文字可以被识别，但是又不能太明显，融合的还要自然，这就需要反复去调试了。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwx8sFGj4G5dprAgUl5ewXBKCzDzRv77ZsGeymibUysPGSsA6mIP6tLfKficDvSWCujjrBj4bh2s2rfg/640?wx_fmt=png)
这里用到的一个controlnet的新模型  lightingBasedPicture
，是一个可以控制画面当中光影关系的模型，使用它你可以按照自己的想法控制画面当中光源的位置和形状。
![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwx8sFGj4G5dprAgUl5ewXBKILV4yqrLSVVVQJ65J6WfzjpCibiaHAlDsDNyia1ErHUrtf1GXYdBGIiawA/640?wx_fmt=png)

大模型使用majicmixRealistic，提示词为——1girl,sitting by the window,meditation,soft
light,light and shadow,close-up,portrait,

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwx8sFGj4G5dprAgUl5ewXBKTrWtnoVVIseHKeXN2jJ6udcvKRY2nhicIHbqfgRasmXdNmqiauLfvFUg/640?wx_fmt=png)

设定好尺寸就可以开始刷图了。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwx8sFGj4G5dprAgUl5ewXBK4VYZQC9Q1Ns3IOdXibMu6DibicJdgbBFbCh0xibGDzGY0kOQr56wJP5syQ/640?wx_fmt=png)

给大家看一些测试过程中的图片，比如这张我调高了controlnet的权重为0.8，这个时候文字就不是光了，而变成了人物服装的一部分。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwx8sFGj4G5dprAgUl5ewXBKavR5ZOXbTzn2JsXsUQz4jCzqqbBPJhI3n7q2Cb8lXwwcy2bFQIxZVQ/640?wx_fmt=png)

再看这张，画面的感觉挺好的，但是文字的光感不强，比较难以识别。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwx8sFGj4G5dprAgUl5ewXBKDbKicich3eoyIf8mZciboyTJ85WezOwKU7zWdypdopkem0IPx08WP33icw/640?wx_fmt=png)

所以我锁定随机种子之后，将lightingBasedPicture模型的终止时机由0.6提高到了0.7，这样文字就比较好识别的，当然再提高的话呢，字又会显得太突兀，我们要把握好一个平衡。  

[
![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwx8sFGj4G5dprAgUl5ewXBKk45jtm8ddjib9sTiccVRVIB5jUgYFzb4ns6JeCPHQHcq0PibRqoLcytdA/640?wx_fmt=png)
](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487439&idx=1&sn=4ffba393c0ba29e78cd5a87c03895440&chksm=9fbecf3ba8c9462d04569f9f469268be00d01a92806115b51c4244af4cbc1c5151b238f5c659&scene=21#wechat_redirect)

好了，光影字体就讲到这里。  如果想要最新的controlnet模型的话，可以添加我的公众号【白马与少年】，回复【SD】即可。

  

** -END-  **  
**  
**  

* * *

往期精选>>  

  * [ 来点夏天的感觉，AI造字浪里个浪~  ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487439&idx=1&sn=4ffba393c0ba29e78cd5a87c03895440&chksm=9fbecf3ba8c9462d04569f9f469268be00d01a92806115b51c4244af4cbc1c5151b238f5c659&scene=21#wechat_redirect)   

  * [ 隐藏定位点！融合度更高的二维码生成  ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487390&idx=1&sn=fe28a857f50661807e449f1c04400096&chksm=9fbecf6aa8c9467cdfde4c9b37eff054f279ff230524399b11702a4442db514bcb27009d24e7&scene=21#wechat_redirect)
  * [ 图片高清化+面部修复+一键抠图，一些你不知道的  事儿  ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487327&idx=1&sn=aad22a60028778b97bf00262f3a67883&chksm=9fbecfaba8c946bd29853ea9c15d90c03e2ac09ee4d22c27956bbcbcab3fa6c4551b5f599d03&scene=21#wechat_redirect)   

  * [ 无需Lora，一键换脸插件Roop  ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487143&idx=1&sn=f564fb2e97142443fd706a15a3801ce3&chksm=9fbece53a8c9474550a6bdc7b15a8bd1961c0a5f48b8c736a18cbd1fb5906e5008b544383af4&scene=21#wechat_redirect)   

  * [ 提示词标签选择器Easy Prompt Selector  ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487103&idx=1&sn=dff3272fa8c3b99b2265aa8dfee6ca2c&chksm=9fbece8ba8c9479d9ac6bfb710314793bdc526b2ac58d9f263f41323a1a1ed15f8cedf27667e&scene=21#wechat_redirect)   

  * [ SD梦幻联动PS插件Photopea  ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247486998&idx=1&sn=3946968e6476c6aaacf2282a0459eda0&chksm=9fbecee2a8c947f4852619b326447156f8a4af5de9ed5d31bdccf7aab3f8219b4214e488e8f4&scene=21#wechat_redirect)   

  * [ 超清无损放大器StableSR  ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247486854&idx=1&sn=e52870038dafc7518219660c90b1718b&chksm=9fbecd72a8c944647bb21f5e4546589295e5696a1f62601931080ccd4d29a1ec1230f73feb64&scene=21#wechat_redirect)

  * [ 如何画出商用级别的高清大图  ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247486230&idx=1&sn=dde16ebbd5078661c21835c94db554dc&chksm=9fbecbe2a8c942f48cfe40eaea15ff963db9b4fe1c9a8aed330ee718bcf6720e491fc9237a7e&scene=21#wechat_redirect)   

  * [ 【PS】Ai绘图哪家强？Photoshop 2023 Beta爱国版降临！  ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247486687&idx=1&sn=bc00c7e4ae00e2858c61e9b973747534&chksm=9fbecc2ba8c9453d8b9c3252ea1c81be41a94e9d21b66962b0ebf27e4a06d7daf9d3c1938707&scene=21#wechat_redirect)

预览时标签不可点

微信扫一扫  
关注该公众号



轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6iciciaKY5WZ4ib8CVibVnVHRJwGj6ksg7fk0tzTMuLPsvptv6zswtKfCLNFwYr9aIBGkjiaYGBWtibwnOQ/0?wx_fmt=png)

小鱼干了







****



****



  收藏

