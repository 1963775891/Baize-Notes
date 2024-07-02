![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At5VzM106XKPibmQic8s6nMP60555udrSoOFtAqvsprsM682YgLHF2Ormw8zCEEGS2SlI0QtWJVvzGYg/0?wx_fmt=jpeg)

#  是PS的SD插件，不是SD的PS插件！

原创  暴躁的卡爷  [ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

上周通宵给群友写了如何用ps beta修手（阅读量好低啊，不是你们吵着要的吗？ ![](https://res.wx.qq.com/t/wx_fed/we-
emoji/res/v1.3.10/assets/Expression/Expression_55@2x.png) ）修手修到都我看手就想吐了...
以为手这玩意儿已经不是问题了... 谁知道...

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5VzM106XKPibmQic8s6nMP60rIEmx14wSick3icCWPuBuyJea5DFX2IzNZibrf36HSpSIicpmumic5qZ3ibg/640?wx_fmt=png)

整这一出是吧？我吃这一套？我吃。求得很好，我求你下次别求了。 ![](https://res.wx.qq.com/t/wx_fed/we-
emoji/res/v1.3.10/assets/newemoji/Worship.png)

** **** ** ** ** ** ******** ** ** 说两句  ** ** ** ** ** ** ** ** ** ** ** ** **

还是有话像说在前头，其实上半年GitHub上有很多ps的sd插件，但确实很少在网上看到相关的教程，甚至看到很多付费（或者潜在付费）的psAI插件，我当时就在想，大概这些开源插件比较适合改成商业产品，自然也就没多少人愿意分享了。我也很怂，怕人揍我，也一直不敢吭声。直到Adobe
出了PS beta。

无敌一般的PS beta很快就成为最好用，“最便宜”的局部重绘工具了，能解决80%的局部重绘问题，也杀死了很多人的创业梦。

但不得不说，本地部署的SD配合上PS的SD插件，熟练以后，剩下那20%的风格，场景也能被你牢牢掌控。
**这期是“商业机密”，我求你一个人悄悄看，不要扩散** 。

  

** **▍** ** Stable Art  ** **

Stable.art 是 Photoshop （v23.3.0+） 的开源插件，能让你在ps中随便框框就能轻松局部重绘，无缝衔接。这在PS
beta出来之前简直就是黑科技。

至于如何安装，我会在文末提供，stable art至今都是0.01版，简单又强大。  

下图右侧是stable art的界面。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4ZicUdFGicslK0jWibrMVLDf7IsXV1zuY0DfyHAfGNSkAWSEhe6XtLFkGyfLw8iaAfHFdJia1ECrJIIMQ/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** 走两步  ** ** ** ** ** ** ** ** ** ** ** ** **

  1. 接下来我简单演示一下这款PS的插件如何操作。 
  2. 打开目标图标。(ps部分不用我来教吧，不会的话可以关掉手机出门左转了)，这张昨天讲dynamic prompt做的图，有点“违规”了，我们就用插件给她局部重绘。 
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

以为完事了吗？不，我怕有群友又说我骗ta，不重绘个手能叫重绘？安排！

下图左为一个坏手，为了提高抽卡效率，用画笔给小拇指补一下（这个之前就有介绍）。需要的传送门:  [ AI:你都不会画手，为何骂我？（实战篇）
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247485357&idx=1&sn=adb3c961e17ffda4ebc6c2fa4e3305f3&chksm=97a4319ca0d3b88a53465d6486863d7a448b35e38ee7e3fc9b4daa970516095b73403ef1bbd3&scene=21#wechat_redirect)
>>  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5VzM106XKPibmQic8s6nMP60bzg7Z4Ed3Uiadjnu1MQALQTgfbenT55a78AfbI4KCXbr5NZ33rLpF5g/640?wx_fmt=png)

选对模型，（关键词都可以不要）相比较PS beta那惨不忍睹的抽卡，插件的好手率要高很多。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5VzM106XKPibmQic8s6nMP60tun7UCxoQNa7J8pWGAaMFBljlfk2NibQQ3iaPl42O0r8Qogd2SKzD6Yg/640?wx_fmt=png)

最后随便选一张，起锅！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4ZicUdFGicslK0jWibrMVLDf7dj6UKzM2FpqicCiafGic0edYxt6AuxO1E3sBtglyicwlrdJajLNcZMbQAw/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** 我不会的是"二次元"！  ** ** ** ** ** ** ** ** ** **
** ** **

有人就说了，我ps beta贼听话，真人重绘贼6，但只会出真人，二次元整不了。

没完没了了是吧，首先ps beta还是很全能的，这个要先澄清。然后，插件整二次元，就是 **换个模型** 的事。就不浪费篇幅写案例了。太长了没人看。

  

** **** ** ** ** ** ******** ** ** 安装  ** ** ** ** ** ** ** ** ** ** ** ** **

安装ps插件有两种方式。但要求ps的版本需要是高于  v23.3.0的（因为ps 23之后才支持插件拓展的），beta版也能装。

  * 确保你安装了Adobe Creative Cloud客户端，双击下载的 CCX file，会提示安装成功后，在ps的插件->stable art就能启用。 

  * 如果没有装ACC的用户，可以直接通过压缩包，解压到ps的安装目录下，Adobe\Adobe Photoshop (Beta)\Plug-ins 里放好就行。 

文件下载见文末，当然GitHub上还有带contorlnet的ps-
sd插件，还汉化了，也一直在迭代。名为：Auto.Photoshop.SD。我也一并提供下载，怎么操作就自己摸索吧，stable art够我用了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5VzM106XKPibmQic8s6nMP601iabZ3H65mhO1EAqlnUiaGYCKVOPRx8uyc7ZGWgwbMEToySdr0J6Mzzg/640?wx_fmt=png)

那这篇就这样。

  

** **▍** ** 最后  ** **

** 开新群啦~  **

感谢那个每天999+的防灾小伙伴们，不到一个月，群就满了。所以我们开新群啦！~ 欢迎更多学习交流的“话痨”和“热心肠”加入。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4ZicUdFGicslK0jWibrMVLDf7Jf0K8LF7jT4bB6k16vATgA9Mjz8XwQkibVHCGuUchObAXIrrGN8wu5A/640?wx_fmt=png)

**在线SD**

关  注公  众号获取在线SD链接  。

  * 打开浏览器就能生图，即开即用； 
  * 不需要复杂的部署和安装； 
  * 不需要自己下载模型，安装插件； 
  * 不需要科学冲浪，魔法楼梯； 

AIfish暴躁鱼  干  ！  一个  服务  用户  学习SD的在线服务。  欢迎使用，也欢迎奔走  相告。

** **  
** **

** ** 最后.  ** **

感谢群里的小伙伴友情出演，如有巧合纯巧合。  

文章中提到的PS插件资源，关注公众号回复  **【商业机密】** 即可。

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

