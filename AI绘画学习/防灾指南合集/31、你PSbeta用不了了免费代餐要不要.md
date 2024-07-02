![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At5z5Qs12weF01BLHibHmOG50QEp7co37o3TAEYOkibFS7Bgb4oaI2YQw4CQEwJy0gZ2muCS71AZzU3Q/0?wx_fmt=jpeg)

#  你PS beta用不了了？免费代餐要不要？

原创  暴躁的卡爷  [ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5z5Qs12weF01BLHibHmOG50wI0klFDFRQn4oNLIL9iaMzakSQXDo7SPnT0tt9LZRmrWS7phAbibz4kA/640?wx_fmt=png)

最近你是不是发现你的ps beta创成式创不了了？是不是跑到各个群里去问了一大圈，得到的结论是，买正版吧！

是的，Adobe开始收网了，就在他们精简计算了算力成本和让你的依赖程度后，这么多破了的用户“baipao”他们的服务器，退出大陆区的Adobe显然不傻，收网！  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At5z5Qs12weF01BLHibHmOG50q3XYuplAX4HXNskV3QUQYresKE6MJqaKrLsCSNticgfWnBTKgfl7uRg/640?wx_fmt=jpeg)

其实之前就有提到目前还没有任何一家商业公司会免费的提供“算力”这个东西，因为成本真的很大，即使是微软这样的巨头也要使用阉割后的GPT给bing搜索。所以一直对中国区睁一只眼闭一只眼的Adobe一定不会让‘免费用算力’这件事持续发生。  

所以，PS beta一个之前SD局部重绘的代餐，马上就成了被过去被代餐的代餐而代餐了。

之前是“商业机密”的商业机密插件又重新成为商业机密了。

  

** **** ** ** ** ** ******** ** ** 还是要说两句  ** ** ** ** ** ** ** ** ** ** ** **
**

所以再次把之前的PS上的本地SD插件拿出来，再说一遍  。  ** 除了需要本地算力，和不是“那么”傻瓜外，插件比创成只强不弱  ** 。

而失去免费的AI生成的PS，又变成那个笨重，落后，大而全，全而不精的老工具产品了。

  

** **▍** ** Stable Art  ** **

之前有提到过，所有的封面都是用ps 局部重绘而来的，很效率，恰好最近beta用不了，失去拓展封面的傻瓜工具了，我也再次使用stable art进行局部重绘-
扩图了。效果果然杠杠，依然效率。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5z5Qs12weF01BLHibHmOG50Wyn7iaX1ABOiaxR8stWUek8mdptc2or91jHz1lMqGdDjMtpa2tnA9qqw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5z5Qs12weF01BLHibHmOG504d6Oq4khNd8FmUrpjicFFurtgBLn3eGiaN0pdGa80oiaqiaBYJanZWlfzA/640?wx_fmt=png)

Stable.art 是 Photoshop （v23.3.0+） 的开源插件，能让你在ps中随便框框就能轻松局部重绘，无缝衔接。这在PS
beta出来之前简直就是黑科技。

如何安装，在文末提供，stable art至今都是0.01版，简单又强大。  

下图右侧是stable art的界面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4ZicUdFGicslK0jWibrMVLDf7IsXV1zuY0DfyHAfGNSkAWSEhe6XtLFkGyfLw8iaAfHFdJia1ECrJIIMQ/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** 走两步  ** ** ** ** ** ** ** ** ** ** ** ** **

  1. 接下来我简单演示一下这款PS的插件如何操作。 
  2. 打开目标图。(ps部分不用我来教吧，不会的话可以关掉手机出门左转了)，这张昨天讲dynamic prompt做的图，有点“违规”了，我们就用插件给她局部重绘。 
  3. 打开ps，同时也要打开本地的sd（一定要运行中哟） 
  4. 先检查插件是否工作，点击endpoint. 默认就是http://127.0.0.1:7860 如果连上了字体会从灰色亮起来。   

  5. 然后就可以选择所需模型了（这里比PS的创成强的地方就是你本地那几百G的模型都能用上，再也不用担心风格问题了） 
  6. 使用选择工具，对目标区域进行框选。 
  7. 填写基本设置（正反关键词，种子，采样器，采样步数，CFG等） 
  8. 单独说一下模式选择inpait，只有inpaint才会阅读整张图的信息，进行局部重绘。 
  9. 局部重绘的本质就是图生图，所以denoising（重绘幅度）和图生图一样，这里建议调低一些，小于0.5，因为我们要稳定不要创意。 
  10. 点击大大的按钮生成。（高级设置里可以改生成张数，resize放大还是缩小） 

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4ZicUdFGicslK0jWibrMVLDf7Zxup5vgUEslIkuHPFUej7QsfFqiab4awCu166nssbAriaNFibypf2WS2g/640?wx_fmt=png)

因为局部重绘的图片尺寸其实很小，对显存和GPU挑战都不大，所以生成速度很快，默认4张会显示在按钮下方，也会有一个智能图层的建立。也可以继续Generate
More... 与beta不同，你可以选择都要！！把需要的勾选上就会显示出来。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At5VzM106XKPibmQic8s6nMP60PmepicytPky2E0iam8sSFv7pT1p6ibkHMLcIqEX7SY8QaR5h4acwCEo0w/640?wx_fmt=jpeg)

  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At5VzM106XKPibmQic8s6nMP60FxjCUmRKK3IUD4QSiaaIfzd6lKSC4Xnqtdlibg0Aich5TibOB6lJ4yib0Hw/640?wx_fmt=jpeg)

利用，工作流还可以多次多步生成，一步一步缩小不满意的区域。（看我走了6步）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5VzM106XKPibmQic8s6nMP60ouwmYib3cbwITJGib6xVYE49pAVPGghYbGONEARkoO691VBB3Fsmm8Kg/640?wx_fmt=png)

最后收获一个你自己满意的图片。完事！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4ZicUdFGicslK0jWibrMVLDf7p0XYYq8ebWewmXjOBm1O3BQkBxTNiaDPZK0TjvTLGBLUgVRL5kG0Xwg/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** 我不会的是"手"！  ** ** ** ** ** ** ** ** ** ** **
** **

下图左为一个坏手，为了提高抽卡效率，用画笔给小拇指补一下（这个之前就有介绍）。需要的传送门:

[ AI:你都不会画手，为何骂我？（实战篇）
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247485357&idx=1&sn=adb3c961e17ffda4ebc6c2fa4e3305f3&chksm=97a4319ca0d3b88a53465d6486863d7a448b35e38ee7e3fc9b4daa970516095b73403ef1bbd3&scene=21#wechat_redirect)
>>  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5VzM106XKPibmQic8s6nMP60bzg7Z4Ed3Uiadjnu1MQALQTgfbenT55a78AfbI4KCXbr5NZ33rLpF5g/640?wx_fmt=png)

选对模型，（关键词都可以不要）相比较PS beta那惨不忍睹的抽卡，插件的好手率要高很多。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5VzM106XKPibmQic8s6nMP60tun7UCxoQNa7J8pWGAaMFBljlfk2NibQQ3iaPl42O0r8Qogd2SKzD6Yg/640?wx_fmt=png)

最后随便选一张，起锅！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4ZicUdFGicslK0jWibrMVLDf7dj6UKzM2FpqicCiafGic0edYxt6AuxO1E3sBtglyicwlrdJajLNcZMbQAw/640?wx_fmt=png)

  

** **** ** ** ** ** ******** ** ** 安装  ** ** ** ** ** ** ** ** ** ** ** ** **

安装ps插件有两种方式。但要求ps的版本需要是高于v23.3.0的（因为ps 23之后才支持插件拓展的），beta版也能装。

  * 确保你安装了Adobe Creative Cloud客户端，双击下载的 CCX file，会提示安装成功后，在ps的插件->stable art就能启用。 

  * 如果没有装ACC的用户，可以直接通过压缩包，解压到ps的安装目录下，Adobe\Adobe Photoshop (Beta)\Plug-ins 里放好就行。 

文件下载见文末，当然GitHub上还有带contorlnet的ps-
sd插件，还汉化了，也一直在迭代。名为：Auto.Photoshop.SD。我也一并提供下载，怎么操作就自己摸索吧，stable art够我用了。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5VzM106XKPibmQic8s6nMP601iabZ3H65mhO1EAqlnUiaGYCKVOPRx8uyc7ZGWgwbMEToySdr0J6Mzzg/640?wx_fmt=png)

通过群友验证，补充比较重要安装问题：1. 如果你用不了beta的创成生成，那你可以卸载beta了，因为beta会影响你使用stable
art插件。请安装ps
2023。另外如果你使用acc安装，请通过acc的增强工具安装ccx版的插件。否则也可能会出现插件链接失败。如果别的pojie方法，方可以使用解压到文件夹的方式。Auto.Photoshop.SD
测试不受影响，两个方式都能正常使用。

那这篇就这样。

  

** **▍** ** 最后  ** **

** 还有一件事，想简单提一下  ** ，事情起因是上一篇讲stable
art插件，有个人就遇到上面红字的情况，公众号后台私信我，询问方法。我没有即时回复到后被骂街了，嘴和菊长反了。  

我写公号是为了帮助到真正需要帮助的，没有必要更没义务一定要真的喂饭从嘴喂到大肠，管你拉shi撒niao。21世纪了，不用人教你怎么网上冲浪吧。  

**  
**

这期没有群友的参加，还是例行感谢一下。

如果对SD防灾对策群感兴趣的也可以关注公众号给 **【小鱼干了】** ，通过公众号的自动回复 **加群** ， **加好友** ，获得
**在线SD云服务** 等操作。  ****

本期文章提到的PS插件工具，可以公众号回复  **【商业机密】** 获得资源。

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

