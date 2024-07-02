![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At7fc52WpiaXRkMIUv9pQtPOxAay6gtzf6PZl1bY8DENx6RuLVQZS6xmR4XYlxrXEwpKv4rh95QHTibA/0?wx_fmt=jpeg)

#  SegmentAnything 能分离一切的插件

原创  暴躁的卡爷  [ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

为什么？为什么七夕这天我还在电脑前写文章？而群里的那份热闹劲已经...

并未随着爱意浓郁的节日而消失，还在。  ![](https://res.wx.qq.com/t/wx_fed/we-
emoji/res/v1.3.10/assets/Expression/Expression_42@2x.png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5lwAciazc3UoveHURw964wjrliaOWEAgatVWjAfsRb1ESibm1wTBS7LE82UBj7OCgPc64abK9MxWIUg/640?wx_fmt=png)

那好吧，那我还是继续写文章吧，我得装一装。继续伏案...  

  

** **▍** ** SegmentAnything  ** ** ****

这个插件很早就挖了坑，也提及了很多次，也在很多其他插件遇到过很多次。因为下限和上限都很高，所以它不是一个单纯的抠图工具，但在抠图上，它很强！~

因为功能很全，描述又很晦涩，我们就不按照老套路跟官方文档走一遍，我用自己的理解，简单粗暴的解释一下插件功能。  

如果只需要了解抠图知识，可以传送门看看之前提供的“抠图”插件和优劣结论：  

[ SD“抠图”插件们哪家强（实战篇）
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247485131&idx=1&sn=7c5ca99af2d1af168f43092f6de468d2&chksm=97a430faa0d3b9ec6e525eabb9b371c7b835053127fd84634ba7730ab2097951248972f29d30&scene=21#wechat_redirect)
>>  

[ SD的这些“抠图”插件们（插件篇）
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247485093&idx=1&sn=995dccb0d74ef32c2014b2826665a293&chksm=97a43094a0d3b982169df3c581a1ac36af7f0955d8a42d93e2c89448fbfca21e3d42b2f1906c&scene=21#wechat_redirect)
>>

** **** ** ** ** ** ******** ** ** 下载和安装  ** ** ** ** ** ** ** ** ** ** ** **
**

1\. 其实所有能在扩展中搜到的插件安装起来都很简单。并且大部分优秀的插件都能通过  **
扩展——可下载——点击加载扩展列表——搜索关键词(如segment)  ——找到  ** 。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7fc52WpiaXRkMIUv9pQtPOxJp2PqWnZutRIDxZ0icqDwWy4tbI8zmpcib5fibcHRTWWYQsCKeicBATvhw/640?wx_fmt=png)

2\. 你也可以通过github的url, 从 从网址安装——粘贴url——安装  

https://github.com/continue-revolution/sd-webui-segment-anything

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7fc52WpiaXRkMIUv9pQtPOxQ5EyfhRPyXcypSYE4caXcVzjAX7IhgwKviaNjIVPASmhyqUia7YASzOg/640?wx_fmt=png)

3\. 最后如果你的网路环境真的太差了，还是老办法，你从文章末尾提供的下载方式中，把插件直接下载，并安装到SD目录中的extensions中。

（虽然但是，每次重复这一个环节挺啰嗦的，真心希望早日摆脱喂饭级别，让节奏快起来。）

** 下载模型  **  

插件装好后，会在生图设置里找到。插件分成2部分，Seg和GroundingDINO,我们会分开来讲，  还有一步需要操作。下载SAM模型。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7fc52WpiaXRkMIUv9pQtPOxruTmbCAIBC5rNLSibuqyBEVoI9l53j1DmUUMqIA3T8rzY2NHLVPNFXw/640?wx_fmt=png)

SAM模型有很多技术团队在研发和优化，官网有介绍。因为涉及到啃书，这里我就无脑建议大家选择Facebook团队中号模型： **sam_vit_l**
.(功能依赖强烈的可以选h，也意味着需要更大的显存）

文末下载中，插件也会有提供模型的下载。记住别改名字，模型可以用在很多地方。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7fc52WpiaXRkMIUv9pQtPOx5F4JmEmj4YmWyhQ8wEOWNgC6PAQxv9biaRianR1wezXmE6yF69Yck7Kg/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** Seg（语义分离）  ** ** ** ** ** ** ** ** ** ** **
** **

操作其实很简单，文生图和图生图都适用的。选择好sam模型后，可以在图片上传处上传你想分离的图片，在图上左键点上你想保留的部分（黑点），右键点击你想去掉的部分（红点）。然后点击下面按钮，
**预览分离结果** 。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7fc52WpiaXRkMIUv9pQtPOxPTeM3u0tnnXxgDwV1cxRKW5xh2ma3gPWWDyXSbcEYsCzq5bcaYhmLw/640?wx_fmt=png)

就能获得三个有一定差异的分离结果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7fc52WpiaXRkMIUv9pQtPOxtibWNsoicaZdeF76TtTYKvSSdlMcwjWL6eJKdFnlqwsvzH0y6eDzkKIw/640?wx_fmt=png)

|

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7fc52WpiaXRkMIUv9pQtPOx9s3nCJQUSpY95Lzx7AI1cYhPb03h0xkbVxKic0LzSbKf2e0WASsneNw/640?wx_fmt=png)

|

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7fc52WpiaXRkMIUv9pQtPOxdQzWqJicQTibzl6Kr1CpdiaVAFFkcqulINgXt6rjgg71HJb1rWQDhzKgQ/640?wx_fmt=png)  
  
---|---|---  
  
根据需要和自己点的误差进行调整和选择。（其实按照之前我们学习的抠图，这一步就已经完成，拿走你需要的带透明背景图的分离元素就行。)

如果需要进行后续工作流操作，比如将元素分离，进行局部重绘，就可以在三个蒙版里选择一个所需蒙版（0，1，2对应123排序），并勾选复制到局部重绘....这个我们一会再细说。

** **** ** ** ** ** ******** ** ** GroundingDINO  ** ** ** ** ** ** ** ** **
** ** ** **

如把GroundingDINO拆开是因为我们大部分时候也用不着它。但需要的时候又是“真香”，与需要下sam模型不同，勾选GroundingDINO，后会自动下载2个对应的模型，选择第一个就行。然后我们可以在检测提示词输入框中输入希望提取的部分。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7fc52WpiaXRkMIUv9pQtPOxFKNz49Jpzqc5OdboxPdNHVV6a7sT2WqjTFHy66NqfHuABeJZsViaRbg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7fc52WpiaXRkMIUv9pQtPOxr9Royia2nclmRTkyVMfLa2zH48zN3II73ibMb9ia8l6ubNfn5t84uUjWg/640?wx_fmt=png)

例如：输入手和脸，就能把2个部分都分离出来，如果有些分界不清的地方不满意，可以调整box 阈值获得更好的分离效果。

** **** ** ** ** ** ******** ** ** 蒙版  ** ** ** ** ** ** ** ** ** ** ** ** **
** **** ** ** ** ** ******** ** ** 局部重绘+CN局部重绘  ** ** ** ** ** ** ** ** ** **
** ** **

最后实际演示一下，语义分离后的局部重绘有多强大。以上面分离出来的手为例。

手，对大家来说还是常见又极具挑战性的事情。所以我们需要多给它一点空间。我们选择需要的蒙版对应编号后，可以勾选展开蒙版设置。给蒙版外扩一些像素。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7fc52WpiaXRkMIUv9pQtPOxgw32SEcxTkiaba0ibuyMzPyPIXUmXsbhWUxrdsDd4ef7Dw6NHbV8eJ2Q/640?wx_fmt=png)

再发送重绘蒙版，或者手动复制原始图片&蒙版图片到图生图的重绘蒙版中，  点了发送可以不用管是不是没有内容，有的，只是没显示  。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7fc52WpiaXRkMIUv9pQtPOxtEYYsJNDYL0VpNibfnJJEcWTfoKvPv8fSicp0EmjWUweozEQl41pFtGQ/640?wx_fmt=png)

注意，上传蒙版到ControlNet需要对应到CN的单元，如果传到0，那就需要在单元0上设置启用，选中局部重绘，或者手动选预处理器和模型（这部分属于之前CN教程部分了，没更上节奏的翻历史吧，或者看下面传送门）
[ 初认Controlnet插件（插件篇）
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484743&idx=1&sn=6af762a7ff8938d57c506f30a426856b&chksm=97a43376a0d3ba6089c57b2c29c698e72c52ec39ca48b948634037d261d1e08d6cabab262a9d&scene=21#wechat_redirect)
>>

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7fc52WpiaXRkMIUv9pQtPOx5g16COD8kF28iajibrhu9jY6cR4ibRfiasozNsaFVPbLH7BKxqXa4icMmMg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7fc52WpiaXRkMIUv9pQtPOx4plsfJjS0paSBHSEaYUhURapBLP5zz7lNrvfwDdECCSal5BldvLAqQ/640?wx_fmt=png)

最后，就是图生图的基础工作了，设置好关键词，简单调整一下尺寸，参数设置，重绘幅度可以更具情况来。因为我是需要将手套换成光手带绳子，与原图差别很大，所以幅度开到0.6-0.8。剩下的就是大量抽卡了。  

** 关键词  ** masterpiece,smooth hands,a red rope on the wrist,slender red rope,  
---  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7fc52WpiaXRkMIUv9pQtPOxYHUuwpWGicTrUiaj7v478IJ3Syy7tRfiaKvI6icKicRicDE1PVuc38yoP0Pg/640?wx_fmt=png)

|

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7fc52WpiaXRkMIUv9pQtPOxlw347zEuKSC1vpeApErrianrxFgel5VqKNJknEf9ZlA4mia2rRGbzrWQ/640?wx_fmt=png)  
  
---|---  
  
将将将... 手套已脱，手部inpaint完毕。  抽卡费时费电... 就这样吧。

官方文档里有一个B站视频，可以更直观的学习这个插件：  

https://www.bilibili.com/video/BV1Hh411j7b2/?vd_source=bf2fb1228409a6646717f9ce78c7d8ca

**
但我有个疑问，ControlNet1.1之后的局部重绘是不是可以脱离图生图单独运行，也就是CN的inpaint和图生图遮罩重绘可以二选一？期待这个问题有人解答一下。
**

Segment作为语义分离在很多插件里都有运用，但原理是相似的。另外不同的色块会区分不同的语义，这个涉及到啃文档, 肯定很多人不愿意看，不重要，下期见。

**  
**

** 最后  **

部分杜撰场景如有巧合纯属巧合。  感谢群里的小伙伴友情出演。  

如果对SD防灾对策群感兴趣的也可以关注公众号给 **【小鱼干了】** 私信微信号，我看到了会加你，拉你们进来一起开放，学习，共同进步。

文章中提到的LoRA资源，公众号回复 **【下载】** 即可。

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

