![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At5DkDSGichOiaXRtl8m0Odbwgn7iac2PZdaugDfcwemW2e2WcKARP6aDdqfnFrBO1BWIcn7pbFcxHQeg/0?wx_fmt=jpeg)

#  品牌LOGO风格化，SD独领风骚（实战篇）

原创  暴躁的卡爷  [ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

最近有些膨胀了，越是不缺啥越来啥！本来就不缺钱，有些“爸爸”非要上着杆子送钱来，拦也拦不住。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4ZctYj7sMGajiao2kIEtDcibZwIyia0KHJmAwUFcu5nysZ7nRafRgX5CWd2THSIr1ghOjfjrCQqPqKw/640?wx_fmt=png)

看好了，Daddy，你得曝光已经在上面图里了。钱我不退的。 ![](https://res.wx.qq.com/t/wx_fed/we-
emoji/res/v1.3.10/assets/Expression/Expression_52@2x.png)  

** **** ** ** ** ** ******** ** ** 五斗米的小鱼干了  ** ** ** ** ** ** ** ** ** ** **
** **

事情是这样，之前我用SD  做了一组 **小鱼干了** ™的LOGO风格化，
上面这位Daddy看了后大为震惊，说回去就要把市场部门的品牌视觉设计师都开了，非要求着让我给ta安排一次单独授课...
我听完直摆手，这怎么行，我这风骨能在这里轻易弯折？ ![](https://res.wx.qq.com/t/wx_fed/we-
emoji/res/v1.3.10/assets/newemoji/2_06.png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4ZctYj7sMGajiao2kIEtDcibr5t30xksXqjATJXq7iacDdwFtsKTkhteRE8ZIxPFhOdh8DAscW3Nxhg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4ZctYj7sMGajiao2kIEtDcibfOdlHo8ibibEpujZz2kXzfvn8vKTKKYQeS6rORC3wiaHf9TDCkzia3ibeRg/640?wx_fmt=png)

我跟ta说，你想学啊，我教你啊！ 就是最近一直很忙，得等等。（  忙着在群里吹牛打屁，一刻不停。）

然后就出现了文章开始的那段聊天记录。这...
一下就给我干不好意思了。知识肯定免费的一口一口喂，铁律不变，谁交钱谁傻X！但你是老板，你要赞助，投资，给群友发福利，那我只能说，来！来者不拒！往我嘴里炫！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4ZctYj7sMGajiao2kIEtDcibohZicTnNCyicC4QaTPbTTgmrLib7bH2jwzDqZFCUoVxUYzrvramg7UFMg/640?wx_fmt=png)

  

** **▍** ** 品牌LOGO风格化  ** ** ****

好，闲话不多说了，我们应约，直接开始用Stable
Diffusion开始做品牌LOGO的风格化。由于内容基础知识和使用到的插件等在之前的文章都有提及，如果没看懂，或者新上手的小伙伴请参考之前的文章。

[ ** 我生成的图为啥糊的一批？（插件篇）  **
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484870&idx=1&sn=13e7f0437b09c7dc5ad9ad7fabcf62de&chksm=97a433f7a0d3bae1d2867a5011fb2f952da46a6e60cd1863af0d41ac5551f1afdf0a04c956b4&scene=21#wechat_redirect)
[ ** >> **
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484870&idx=1&sn=13e7f0437b09c7dc5ad9ad7fabcf62de&chksm=97a433f7a0d3bae1d2867a5011fb2f952da46a6e60cd1863af0d41ac5551f1afdf0a04c956b4&scene=21#wechat_redirect)

[ ** SD的优势区间，ControlNet做字体！(实战篇）  **
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484749&idx=1&sn=69e4460b7df1dde9e3e3bc1e2771bac7&chksm=97a4337ca0d3ba6a5a01bed6dd16915de6704f23f13d06f72ae4463338ddfbf099f734c31e8c&scene=21#wechat_redirect)
** >> **

  

** **** ** ** ** ** ******** ** ** 需要准备  ** ** ** ** ** ** ** ** ** ** ** **
**

  * 大概只需要准备一个品牌LOGO，最好是黑白稿，（你可以用小鱼干了的LOGO练习）  ，  这里我选了一个字形更粗壮规整的品牌LOGO做示例。 

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4jj29NyvPIZhADVsQjup7libhMcYY8CPcS0GWKpkGp3hZvmZ1hAQFBj3MLzMBrjh8rwUZvsV6T6uw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4jj29NyvPIZhADVsQjup7licyPnlxp4zdlfspKOYWt15mdUJDzpesJYW6BuicRJHYmfCQ204Uop1jA/640?wx_fmt=png)

  * 然后需要准备好ControlNet插件，这个插件我们已经讲了很多回了，它可以运用的场景很多，这次我们还是主要使用它的几个子模型来进行品牌标识的风格化。如果这部分没有准备好，文末会提供下载，但你可能需要看一下上面两篇文章提前了解一下功能特性了。 

  * 最后就是挑选几个你喜欢的大模型，和一些LoRA配合“食”用，风味更佳，但不是必须。比如：同样会把我用的LoRA在文末提供。 

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4jj29NyvPIZhADVsQjup7louGosdPrnpr4nBiaRMjqv03jlpsX9uL10p8XIdpHDRY8km7ib5FGp3Rw/640?wx_fmt=png)

  

** **** ** ** ** ** ******** ** ** ** **** ** ** ** ** ******** ** ** 开始生图  **
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

先选择几个常用的大模型按照心中设想的场景随便来几张，比如这里我选的是dreamshaper模型，想象的是一个废土场景，破败锈迹的风格化。

** 关键词  ** (masterpiece, best quality),aesthetic illustration,stylized digital
art,abstract and colorful paint style,(style-rustmagic:1) portrait,detailed
background,detailed face,( scifi, radiation, transparent, nuclear, see-
through, uraniumtech theme:1.1),rusted iron,(rusty:1.05),red
rust,weathered,corroded,grungy,worn-out,dented,dirt,made of rust,abandoned
rust in background,low light,shadows,dark clouds,cinematic
atmosphere,<lora:3DMM_V7:1>,  
Negative prompt: human,cluttered,twisted,interlaced,disorderly  
---  
** 设置  ** Steps: 20, Sampler: Euler a, CFG scale: 7, Size: 512x512, Model:
dreamshaper_631BakedVae, Clip skip: 2,  
---  
  
会等到一组这样的图，测试关键词部分不需要图片有多大的分辨率，快速抽几张卡看看效果即可，如果你有熟悉的词也可以直接略过这部分。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4jj29NyvPIZhADVsQjup7lUQicwpiccYtvShBTibNYp1Z7nEib1bAFS6mcrf1efEyUD1eibjhKOfLeVfQ/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** ** **** ** ** ** ** ******** ** **
开启ControlNet  ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
** ** ** ** **

材质和光影都符合预期了，就可以开启ControlNet。品牌标识的风格化原理其实与之前我们做字体风格化十分相似，不一样的地方是LOGO视觉是有一定的规范，会比字的识别更要求主体部分的清晰。

** Invert+Depth  **

可以使用之前锁字体的方式使用Invert（白底黑线反色）预处理器，配合Depth深度的Control模型，这个组合比较适合将 **前后景分割清晰**
，前景主体光影效果佳。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4jj29NyvPIZhADVsQjup7lO2icQ4Wd7T2BHuUNl9zsDWul5GxOrn3JWe5QEibK90DkxWzQb71Mo6yQ/640?wx_fmt=png)

** Canny  **

也可以直接使用Canny（硬边缘），控制类型里选中后什么都不用调整。利用预处理器的边缘识别，把主体部分从背景中分离出来。尤其是边缘部分会让 **轮廓清晰**
。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4jj29NyvPIZhADVsQjup7ldlMNpox1wjmNgIgUcIIrnUicY3F0sEofgySUQw1ibQKO4NQWfkj8148g/640?wx_fmt=png)

所以我们就能轻易得到效果不错的废土风格LOGO。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4jj29NyvPIZhADVsQjup7lVoM8rBHrFMgeeOysafeuQRicM5ZxxHdJKibv2m7xKLEu46McGb1QVgeg/640?wx_fmt=png)

左：Depth 右：Canny

因为这个LOGO本身十分规则，所以一个ControlNet的单元就能控制得很好，如果遇到一些复杂图形，我们还需要通过多个Control单元分别控制，比如之前小鱼干的LOGO，有线性的轮廓，又有线框住的内部填充，就需要把上面进行融合。

这样我们就能得到更清晰的图案。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4jj29NyvPIZhADVsQjup7lEpCmJBlNhWQzxPKgYhEqmy7arHrQkaicgtf7Klyh2NYqS0cJX6aArUw/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** ** **** ** ** ** ** ******** ** ** 换换其他风格
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

我们可以尝试切换一下模型，改改关键词，生一个更有幻想感觉的风格。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4jj29NyvPIZhADVsQjup7lEicZW9MEFD7nB1zvL03zluzpA8GWyHnE64egSRt6S3jNrIwT6DIHbeA/640?wx_fmt=png)
模型：  majicmixSombre 关键词：幻想，未来科技，干净
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4jj29NyvPIZhADVsQjup7l2wibNyrr4FSguJIc5QXYKxgibt7Iz32I3jx26CeMtic4TchYvGGss8Rqw/640?wx_fmt=png)

模型：  majicmixSombre 关键词：魔幻，蘑菇，晚上

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4jj29NyvPIZhADVsQjup7lk8icTFN95RzhPDjIb71WhCFxptV6iaiawyD7SNib3yIV9j1RlibqALdBNIA/640?wx_fmt=png)

模型：  revAnimated 关键词：宁静，未来主义，透明皮肤

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4jj29NyvPIZhADVsQjup7lmKeLqfr09G5FuJ6EC9Ktia6bicLUjKJmxqzOF5JicWtGx5Do6SpMFgYuA/640?wx_fmt=png)

模型：  majicmixSombre 关键词：魔幻，3D质感

** **** ** ** ** ** ******** ** ** ** **** ** ** ** ** ******** ** ** 再上工作流
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

本来也算含含糊糊结束了，最后还是要绕回这个，因为在抽卡的过程中我们仍然会遇到很多“瑕疵品”，他们有的艺术性足够，只是缺陷明显。  

这个时候我们只需要再次祭出神器PS beta版。（这是当前扩图和局部擦除最强工具），随手框一下，关键词都不用填。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4jj29NyvPIZhADVsQjup7ldwhvplVib4dNDclOredMrewL9JGXTiaT5qb78lZjQPPibMx9rRUv8ibicUQ/640?wx_fmt=png)

将将！

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At4jj29NyvPIZhADVsQjup7lkfUAuEG8Ln47Eicjq6KNrOR1gJj2tFDaiaTZmNljZD9AkHYx4WcplgpA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5DkDSGichOiaXRtl8m0Odbwg3xiarUMbuN2JNcvjFF9WTIWb14aCJqvxPicTGDF7Ywt3WXSQEQZab7icQ/640?wx_fmt=png)

** 最后  **

部分杜撰场景如有巧合纯属巧合。  感谢群里的小伙伴  友情出演与投喂赞助。  

如果对SD防灾对策群感兴趣的也可以关注公众号给 **【小鱼干了】** 私信微信号，我看到了会加你，拉你们进来一起开放，学习，共同进步。

文章中提到的LoRA资源，  公众号回复 **【下载】** 即可。

下期见  ！  ~

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

