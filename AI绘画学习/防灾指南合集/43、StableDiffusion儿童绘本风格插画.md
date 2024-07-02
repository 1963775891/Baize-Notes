![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tyssYUEyRwyl8jQd1Vf21hUBwPSawSk0oPEbaFleGZYasHq3y3wniaibQ6g5dUj8NtNPia4qHkh2OianMNUhLUYBwA/0?wx_fmt=jpeg)

#  【Stable Diffusion】儿童绘本风格插画

[ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

编者荐语：

这是一篇好实战！~

以下文章来源于白马与少年  ，作者吴溪源

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7eibUJEMViclLvunqf0ykvDsVwB5l1CCp96dusJbO54pVA/0)
**白马与少年** .

分享学习心得——Blender，Stable Diffusion等

今天给大家推荐一个大模型和  lora的组合运用，可以生成一些儿童绘本  风格的插画。  起作用的主要是这个风  格lora——“  KIDS
ILLUSTRATION  ”，画风非常可爱治愈，可以搭配不同的大模型使用。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxVD9nMnyeI3gwxtx4ZbdTXHKoqroBFkB4ke8mYcchmds7Yo72OLnDGFwNYeNP8c2PruribHHkCLRw/640?wx_fmt=png)

官方案例使用的是超拟真大模型“  Realistic Vision  ”。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxVD9nMnyeI3gwxtx4ZbdTXzzQuRBKd7K8zj1Eu7lgQH4l96O5iaKYdovAfmYQZsicbQNGpt16eyZsA/640?wx_fmt=png)

我们来测试一下吧，既然是儿童绘本，我们就选择一个大家都熟悉的《小王子》的故事吧。  关键词描述：在一个荒凉的星球上，一个小男孩和一只狐狸，玫瑰花，星空。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxVD9nMnyeI3gwxtx4ZbdTXXdfAeNjQXRvYcnIf4Amyib7Cx9lPNJUEtJQ5ibCyUwlHytKmvF6JszvA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxVD9nMnyeI3gwxtx4ZbdTXUIRtibxpVSm8gicJOB1TTFmEd3TTnCRIs2q0165j9QPz08VOt44h8Q4A/640?wx_fmt=png)

使用latent couple插件（ [ 【Stable Diffusion】手涂蒙版定位插件Latent Couple
](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247486812&idx=1&sn=cbfff40072e25d54605f686c7733b8c0&chksm=9fbecda8a8c944be887648e28695df76810d7bf15a83588aa85ede35232c105c5d727c272ca6&scene=21#wechat_redirect)
）来确定小王子和狐狸的位置关系，并对小王子的服装做一个细致的描述——“黄头发，绿衣服，红围巾”。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxVD9nMnyeI3gwxtx4ZbdTXVFficbXpZGVia1p2BhgZQdqcTFWHcibAxUUEZOTGcmmevlk7ZboIibpQsQ/640?wx_fmt=png)

多刷一些图，最终筛选出来一张，动物的部分总是画得不太好，不过画风还是蛮喜欢的。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxVD9nMnyeI3gwxtx4ZbdTX8IynicPpZhvV6piabURozbpbtBXIicDic4QR6pHjiasrzRG7NF5p3JhjJsA/640?wx_fmt=png)

同样的参考词，我们再换几个大模型看看。  比如我们常用的2.5D模型“  ReV Animated  ”，直接生成。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxVD9nMnyeI3gwxtx4ZbdTXJRKouTZSBUtZgRXibZDzQL1wzvd4RSd0qPr5HlfondjHUsBULTbljOA/640?wx_fmt=png)

这个模型的人物效果会立体一些，而且小王子看起来很飒嘛，小狐狸还是一如既往的稳定……崩坏。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxVD9nMnyeI3gwxtx4ZbdTXXyhr66PXlUdYnzpFq6ZecFekpDxllQGcBEicJjsd6SI3PqZtcmk9pEA/640?wx_fmt=png)

#  还有一个“  Nigi3D”的模型，这个模型和lora的适配度也是比较高的。

#  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxVD9nMnyeI3gwxtx4ZbdTXmsiaVI7IPb3ZW85ic19eiaic6nS9lsibIEZ3mBz4jqGspVeezgNjwM9TrOQ/640?wx_fmt=png)
鉴于动物的输出不太稳定，我们暂时先只保留小王子的部分吧，修改一下提示词。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxVD9nMnyeI3gwxtx4ZbdTXLCAnPPZPE6BbZPsbyhnZMYh73hicyUokNJGT9I9evoKiaJwB3kY9JQHg/640?wx_fmt=png)

点击生成，这个画风是不是还挺讨人喜欢的呢。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxibKycBw7QWWvz7sk4Qb9B5zVictpoRuksaYame5Pnkia9cAfNqSjxvotzBQRaUhExIiayqKDJv9KQSA/640?wx_fmt=png)

以上，就是  关于儿童绘本风格的介绍，大家也可以试试其他二次元模型和这个lora配合，说不定也能形成其他有趣的插画风格  。  如果想要
这些模型和lora  的话，可以添加我的公众号【  **白马与少年** 】，回复【SD】即可。  
  
  

预览时标签不可点

微信扫一扫  
关注该公众号



轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6iciciaKY5WZ4ib8CVibVnVHRJwGj6ksg7fk0tzTMuLPsvptv6zswtKfCLNFwYr9aIBGkjiaYGBWtibwnOQ/0?wx_fmt=png)

小鱼干了







****



****



  收藏

