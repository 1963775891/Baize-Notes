![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At4ZicUdFGicslK0jWibrMVLDf7uiaNlzMXr5iaZoKlLnicQhccYtMicPYMibLK8Hky3Cj1fp9icQnQQCQLSleA/0?wx_fmt=jpeg)

#  Dynamic Prompts插件，魔法提示词由魔法帮你补全（插件篇）

原创  暴躁的卡爷  [ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

没那么多段子可写了，但文末有新东西。

** **▍** ** Dynamic Prompts  ** ** ****

这个插件也是一个老牌插件了，很早就成了必装插件之一了。只是生态发展太快，prompt这块又被all in one一家独大了，动态提示词（Dynamic
Prompts）过去很多优势功能已经被蚕食，这也是有人问我这个插件怎么没看我聊过。但它有着不可替代的部分，一直保留在我的webui中。

** **** ** ** ** ** ******** ** ** 下载和安装  ** ** ** ** ** ** ** ** ** ** ** **
**

1\. 其实所有能在扩展中搜到的插件安装起来都很简单。并且大部分优秀的插件都能通过  **
扩展——可下载——点击加载扩展列表——搜索关键词(如dynamic)  ——找到  ** 。

2\. 你也可以通过github的url, 从 从网址安装——粘贴url——安装  

https://github.com/adieyal/sd-dynamic-prompts

3\. 最后如果你的网路环境真的太差了，还是老办法，你从文章末尾提供的下载方式中，把插件直接下载，并安装到SD目录中的extensions中。

（先把图去了，慢慢少点啰嗦。）

** 怎么操作  **

这个插件功能很多，基础功能不需要单独或者后台下载模型，装好就能用；  我们需要的魔法功能在后面，  我们逐一介绍下去，着急的可以跳过。装好长这样。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4ZicUdFGicslK0jWibrMVLDf7wic8DoDfxHVXtrlZWrXwlMfmpfEJaZBl5KVc75oVTghqnEv3eXGg7Sg/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** 启动动态提示词  ** ** ** ** ** ** ** ** ** ** **
** **

还记得我们在《 [ 嘛呢吽-咒语范式（关键词篇）
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484604&idx=1&sn=8a6f04ee9e3969de14b2e5e78b27472d&chksm=97a4328da0d3bb9b3812cc4524f9742ef04019564605222251132bca75f41505e3df4479f842&scene=21#wechat_redirect)
》中提到过webui的一种语法，通过“|”让生成的图中出现进行组合排列吗？矩阵是一个脚本插件，需要在设置参数中每次使用都需要开启。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4ZicUdFGicslK0jWibrMVLDf7kxGoystIfeSrxX6ASfvdB31KAiaMmT0ox4th0ybGNnjXsskJicA1dRpg/640?wx_fmt=png)

而动态提示词可以简单理解是提示词矩阵的高级版。开启后，通过  {关键词1|  关键词2  |  关键词3  }
语法分别生成不同的图片。例如：{cat|run|sky},

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4ZicUdFGicslK0jWibrMVLDf7XZANyPZxHgRAmY8pXMgRyDbRDXmbzcPWDXbiaxZOibtagicKxRIia0UAmQ/640?wx_fmt=png)

动态提示词可以简单的将我们希望赋予不同图片尝试对比的词在一次生成中完成。与矩阵不同，他们是分离的，不是组合的。
另外如果与别的插件在语法上冲突，在设置里支持变更语法通配符的  。

** **** ** ** ** ** ******** ** ** Need help?  ** ** ** ** ** ** ** ** ** **
** ** **

忘了，应该先讲这个，插件很贴心的用了一个单独栏提供了帮助，还是中文的，虽然也有点晦涩，但还是把功能讲的很明白了。看图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4ZicUdFGicslK0jWibrMVLDf78c76OsJ5ZsFTcDmAdb3umswUlgrbbKiasHTBVk8HoFqiaOEJ7T4icosAQ/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** 组合生成  ** ** ** ** ** ** ** ** ** ** ** **
**

动态提示词能分离，自然也能组合。只是这里的语法是  {2$$艺术家1|艺术家2|艺术家3}  语你也  可以理解，输入了2份，才能进行组合。还是看例子：

{cat|run|sky  },不输入$$ 默认为1.  {2$$cat|run|sky}, 效果为  {cat|run|sky},
{cat|run|sky}。  换言之，我们也可以使用两个{A组合}{B组合}进行更多的组合可能性。这里是工程问题，就不多赘述  。

** 打开组合生产开关  ** 。  

最大生成数为0就好，需要限制自己设。组合批次就是遍历一遍所有的组合。2次就x2。也很好理解。这里有2个 **重要信息** ，需要注意：

  * 打开组合开关后，组合数会覆盖上面生成数和生成批次。 
  * {cat|run|sky},  {cat|run|sky}是会出现cat,cat的词，而  {2$$cat|run|sky} 是去重的  。 

看看组合效果吧。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4ZicUdFGicslK0jWibrMVLDf7yurwAzSA8eicFhK21TavAbrhzuzBtaVKloDPMrccN0RkaSGHkmQsnrA/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** 魔法关键词  ** ** ** ** ** ** ** ** ** ** ** **
**

如果说前面分离生成，组合生成可以手动操作，不算特别常用的话，这部分就是本篇的重点了。因为被称为魔法的关键词也能用别的魔法自动生成补充了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4ZicUdFGicslK0jWibrMVLDf7j965hwHNc5xrf2FPwagRzz7iaW77IIu2DSoRlgXvfXnMYQm2TeiaSspQ/640?wx_fmt=png)

勾选上魔法提示词，加到多少个词自己设。创意度可以理解就是与原提示词的贴切程度，进行过图生图的也好理解。

前面说的下模型在这里就需要选择提示词的模型了，一般选中后都会后台下载，每个大概800m，因为安装了路径很蛋疼，这里我就不提供手动下载的方式了。可以通过上面的url去详细了解其他的prompt模型。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4ZicUdFGicslK0jWibrMVLDf7zPgdNrSia2qYFDbfayJa8yFGojxnd4xcwrWiaykuZI9q2uzGG4CfwWEQ/640?wx_fmt=png)

以MagicPrompt模型为例（官方说这个模型Lexica.art那训练8000个关键词。举例  "dogs playing football"：

> dogs playing football, in the streets of a japanese town at night, with
> people watching in wonder, in the style of studio ghibli and makoto shinkai,
> highly detailed digital art, trending on artstation

> dogs playing football, in the background is a nuclear explosion.
> photorealism. hq. hyper. realistic. 4 k. award winning.

> dogs playing football, in the background is a nuclear explosion.
> photorealistic. realism. 4 k wideshot. cinematic. unreal engine. artgerm.
> marc simonetti. jc leyendecker

其他设置，包括不希望出现的prompt，赋予prompt权重也都很好理解。需要注意的是如果你只是在找寻灵感，目标不明确，可以勾选“手气不错”（  I'm
feeling lucky）  会得到一些让人意外的图片。

那么，我们实际跑一下看？

** 关键词  **

1girl,school uniform,white shirt with blue collars,blue shorts,dynamic
posture,  
  
---  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4ZicUdFGicslK0jWibrMVLDf7NtJGYs1icGabp8hU6ibp1497y7pZ9Q6Fz2SmytnicNkFQVux0jcWlAiaicA/640?wx_fmt=png)

通过动态提示词，我们得到了若干组魔法补充后的提示词，如果勾选“手气不错”还有更多意想不到的结果哟。  

** 关键词  **

1girl,school uniform,white shirt with blue collars,blue shorts,dynamic
posture,, 4k, deviantart, FAN ART, beautiful, symmetrical, highly detailed,8k,
vibrant, Beautiful, artstation, trending on artstation, intricate details,
alluring  
  
---  
** 关键词  **

1girl,school uniform,white shirt with blue collars,blue shorts,dynamic
posture,muted colors:2.0, octane render,4k, neon:3.5, avant-garde,
hyperrealism,4k, deviantart, artstation, professional photography, concept art  
  
---  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4ZicUdFGicslK0jWibrMVLDf7NiauMtQsdm33ywEd9efgrCnGbuq7AdV4k7nTic1N0KFgCB93n96VGbxQ/640?wx_fmt=png)

** 这就是魔法，用魔法生出更多的魔法咒语  ** 。

我们，下期见~  

  

** **▍** ** 重要通知  ** **

** 开新群啦~  **

感谢那个每天999+的防灾小伙伴们，不到一个月，群就满了。所以我们开新群啦！~ 欢迎更多学习交流的“话痨”和“热心肠”加入。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4ZicUdFGicslK0jWibrMVLDf7Jf0K8LF7jT4bB6k16vATgA9Mjz8XwQkibVHCGuUchObAXIrrGN8wu5A/640?wx_fmt=png)

  

**在线SD上线啦~**

暴躁鱼干来啦！经过技术大佬的帮助，专门开发上线了一个超级廉价的服务小白用户学习SD的在线服务。

  * 有浏览器（手机都行）就能生图，  即开即用。 
  * 不需要复杂的部署和安装； 
  * 不需要自己下载模型，安装插件； 
  * 不需要科学冲浪，魔法楼梯；   

可以随时  看教程的同时，自己也上手体验一把，这期的插件也有哟。  苦恼只有mac生产工具的朋友可以体验一下。  **购买前务必先阅读购买须知** 。

除了是防灾群福利外，也是<小鱼干了>福利！  ** 关注公众号--> **** 获得在线SD & **免费** 体验激活码  **

  

** ** 最后.  ** **

本期没有群里的小伙伴友情出演。  

二维码失效or群满之后，  也可以关注公众号给 **【小鱼干了】** ，加群主微信好友，拉你们进来一起开放，学习，共同进步。

文章中提到的插件资源，公众号回复 **【下载】** 即可。

8~

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

