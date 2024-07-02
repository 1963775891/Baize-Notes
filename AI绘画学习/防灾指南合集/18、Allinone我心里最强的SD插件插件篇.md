![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At4q8tQS93j6Xg5icMOF50Hq119zStubLaor0vm8VvDJ9ePicuMmJCnjfD05GHtJ35amg6gw5Oum3K0w/0?wx_fmt=jpeg)

#  All in one，我心里最强的SD插件（插件篇）

原创  暴躁的卡爷  [ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

还记得刚接触AI绘画那会儿，就和一个朋友聊天，他问我英语几级？我说五级，他说扯犊子,  你这一看就是3级都没过的艺术Boy  ，
英语没五级，不然他也不会去考十级。然后就一脸遗憾的告诉我，AI绘画这事，我没戏。

我当时很气愤，回家就把Disco Diffusion从Google云盘上下载下来了。第二天，我就下单了本英语字典，放在桌上。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4q8tQS93j6Xg5icMOF50Hq1GOem3PGgzBD6eYpY2hibewD6TmtOPxibmib6A1rM16RfRiapuQh1G0UGlA/640?wx_fmt=png)

后来，真的开始用Stable Diffusion生图了，每次打开SD启动器前，我都会开一堆软件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4q8tQS93j6Xg5icMOF50Hq10KLE457vns5vkd0zmRqbNyXWR2cRV1XeFQDFQxvyqYJeVZRFGKy58A/640?wx_fmt=png)

这样就会出现  以  下三种常见的工作路径是：

  1. 我看到别人写的不错的prompt  ——  微信截图翻译成中文  ——  不错啊！ ![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/Expression/Expression_52@2x.png) ——  复制  ——  粘贴到我SD的关键词输入框中。 
  2. 我自己想一个场景  ——  在翻译软件中写一串  ——  翻译成英文  ——  粘贴到我SD的关键词输入框中  ——  粘错了  ![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/Expression/Expression_18@2x.png) ——  去Ditto里再选一次  ——  再次粘贴。 
  3. 从Ditto或者别的云文档中，把我传家宝关键词复制出来  ![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/v1.3.10/assets/Expression/Expression_30@2x.png) ——  粘贴到我SD的关键词输入框中  ——  修改  ——  生图。 

是不是很蛋疼，就和坐在电脑前的你，一毛一样？  直到ta的出现！~

** **▍** ** All in one插件简介  ** ** ****

其实SD的翻译插件有很多，之前有试过很多，包括prompt_translator，Stable-Diffusion-Webui-Prompt-
Translator，是都不太好用。或者说都有这样或那样的体验问题，比如翻译等待时间太长，网络环境导致翻译失效，付费api绑定失效等。

后来all-in-one出现了，之前所有的翻译问题都迎刃而解了，还整合了诸如收藏，历史等十分关键、便利的prompt功能。

所以我一直都和群友说，all in one在我心中是 **最佳** ，力压controlnet一筹，因为
**写关键词的门槛降低了之后，AI生图才变成你能参与的快乐了** ，不再只是一个搬运工。

我就带着大家从安装到使用来了解一下这个No.1。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4q8tQS93j6Xg5icMOF50Hq1g2Ct24UI3kTTISWdQo3icJAoLmibcHakK9dXemMDYLYyoV9CO6o3vJ4Q/640?wx_fmt=png)

  

** **** ** ** ** ** ******** ** ** 安装  ** ** ** ** ** ** ** ** ** ** ** ** **

1\. 其实所有能在扩展中搜到的插件安装起来都很简单。并且大部分优秀的插件都能通过  ** 扩展——可下载——点击加载扩展列表——搜索关键词(如all-
in-one)  ——找到  ** 。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4q8tQS93j6Xg5icMOF50Hq1ic1TS0TMu3FBPIW7dkzovr2gJTALF8mZ09a4JrGicqIPKGLBFkMlAiaDw/640?wx_fmt=png)

图片示例搜索的是tanslat,没打完是为了模糊到translation和translate，出现的插件包括上面我提到的以前用过的一些翻译插件。

2\.  你也可以通过github的url, 从 从网址安装——粘贴url——安装  

https://github.com/butaixianran/Stable-Diffusion-Webui-Prompt-Translator

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4q8tQS93j6Xg5icMOF50Hq1KV192LDaLhPqeh6MTTxt8MBqs8vO92OvjHo09gIRSvRzNIpPtNBszQ/640?wx_fmt=png)

3\. 最后如果你的网路环境真的太差了，还是老办法，你从文章末尾提供的下载方式中，把插件直接下载，并安装到SD目录中的extensions中。

（虽然但是，每次重复这一个环节挺啰嗦的，真心希望早日摆脱喂饭级别，让节奏快起来。）

** **▍** ** All in one插件使用  ** **

其实很早就想把神级插件拿出来的，但因为他的厉害之处很难用静态图文描述清楚，偶然看到官方文档居然是带动图的，那就再好不过了，功能介绍我就使用官方文档的动图做演示。
文档贴心的有中文，感谢大佬的辛苦付出。除了上面贴的giturl有一个简版文档外，  ta还有一个官方文档，包括完整的使用方式。

https://aiodoc.physton.com/zh-CN/Installation.html

** **** ** ** ** ** ******** ** ** 基本翻译功能  ** ** ** ** ** ** ** ** ** ** ** **
**

** 自动翻译  **

作为核心功能，翻译，我们只需要设置好需要翻译的语言，选择接口后，在白色输入框中输入中文，就可以立马在原始prompt输入框中显示并自动翻译成英文了。（同时，提示词也会出现一个带翻译的标签）

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/fY8ibThH1At4q8tQS93j6Xg5icMOF50Hq1lhpyo0fl6icXexlk2ngrwzCeQKRtKMWEKVve4k8UMOoYhH7CKVx6ISg/640?wx_fmt=gif)

** 在WebUI的输入框中编写并一键翻译  **
你可以把你复制来的，或者自己之前手动收藏的prompt，或者纯手打入WebUI关键词输入框，点击面板任意位置，这些prompt就会被分割成一个个的独立标签（标签方便调整见后）。
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/fY8ibThH1At4q8tQS93j6Xg5icMOF50Hq1UtznxInyOLiaNib1iajRafq5x1DdAOe5EB9cPicfPg58icmQNSkLCbJqSmQ/640?wx_fmt=gif)
然后可以点击“A|B”图标，把英文标签一键翻译成中文。（前提是你已经调整好翻译api设置）

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/fY8ibThH1At4q8tQS93j6Xg5icMOF50Hq1W7BuFTYFics576TYKBUwhKibxNnwehEQpTPXl5bEgyFNty5LbfU3bObg/640?wx_fmt=gif)

** 快速调整  **  

上面括号里所说的标签意义很大，我们可以通过拖拽标签来调整关键词的顺序，可批量操作，还能直接在标签上进行加减权重，复制，收藏等操作，
**这很方便，所以重要** 。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/fY8ibThH1At4q8tQS93j6Xg5icMOF50Hq1JwicRxoq4SQuzHnVAiaKLrr2YAAia4c98ic02fxribhiaMP8ciadsUyS0XGbg/640?wx_fmt=gif)

** 翻译api设置  **

点击第二个齿轮按钮⚙，再点api，我们就能在界面中设置翻译的接口。作者十分贴心的提供了测试用例，我们结合自己的网络情况可以进行测试  。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/fY8ibThH1At4q8tQS93j6Xg5icMOF50Hq1oZ0ZepuLuicX848qJPIqL37WCYYjKHjHPbBoHU3y4a4ppm8UW9YGttg/640?wx_fmt=gif)

这里注意看我的结论，付费api效果会好很多。但免费的也不是不能用，作者也强调了免费接口是不稳定的，这里我自己测试了一下翻译结果。 **比较推荐使用**
【MyMemory】,中文词汇准确，就是是繁体的哟。其次是【腾讯交互翻译】，网络不稳定可以使用【Bing】，其他的都还行，就凑合。官方也提供了翻译对比，包含付费的，在文档里可以查到。

  

** **** ** ** ** ** ******** ** ** 强大的历史 ** **** ** ** ** ** ******** ** ** **
**** ** ** ** ** ******** ** ** 和 ** **** ** ** ** ** ******** ** ** 收  ** **
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
** ** ** ** ** ** ** ** ** ** ** ** **** ** ** ** ** ******** ** ** 藏  ** **
** ** ** ** ** ** ** ** ** ** ** 功能  ** ** ** ** ** ** ** ** ** ** ** ** **

点击历史记录图标，你就能看到你每次针对prompt做出的修改，都会在记录中被保存（最多100条，超过被删除）。当然你也可以手动删除，不赘述。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4q8tQS93j6Xg5icMOF50Hq1Y2LFice6sH9ic6pHyl8TZE8VECJQRM7z8qjC4vffcmYU0v9OMkfoJvdA/640?wx_fmt=png)

你可以直接复制历史记录的关键词，同时还可以通过点击收藏图标，把历史中需要保存的关键放入收藏栏中。  

然后下一次（不管哪一次），启动都可以从历史或者收藏中把关键词导入prompt的输入框中进行生图，Amazing！~

词条多了，记得手动给收藏添加一个备注名称哟。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/fY8ibThH1At4q8tQS93j6Xg5icMOF50Hq1zk3k1pKL2mY7PNO7I1Xm1sntiaNn3dPDHGhrgBdXjBaibZ2fXSCd0QQg/640?wx_fmt=gif)
** **** ** ** ** ** ******** ** **  
** ** ** ** ** ** ** ** ** ** ** ** **

** **** ** ** ** ** ******** ** ** 其他体验痛点  ** ** ** ** ** ** ** ** ** ** ** **
**

** 使用ChatGPT生成Prompt  ** ** **** ** ** ** ** ******** ** ** ** **** ** ** **
** ******** ** ** ** **** ** ** ** ** ******** ** ** ** **** ** ** ** **
******** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
** ** ** ** ** 如果你有OpenAI账号，插件也为你提供了chatGPT接口，这部分我没测试过，但感觉会调教语言模型的大佬应该会香疯了。

**![](https://mmbiz.qpic.cn/sz_mmbiz_gif/fY8ibThH1At4q8tQS93j6Xg5icMOF50Hq1nAZfbibZSdhXrxRQFKRMmicyWW90b4AQSqChp9DBRfGfpZdQicyQ7Hovg/640?wx_fmt=gif)
**  

** UI设置  ** 如果习惯使用插件后，可以在界面上把原生WebUI输入框可以隐藏起来。也可以把标签隐藏；甚至还可以改变插件样式。总之自由度很高。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/fY8ibThH1At4q8tQS93j6Xg5icMOF50Hq1PdDqjeqZFcajoUmo21gsf4dia464n9935DYI5xJOy4u4iatly93zuQkg/640?wx_fmt=gif)

** 支持tag补齐，  ** ** Lora、LyCORIS、Textual Inversion 高亮和检测  **

** **
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/fY8ibThH1At4q8tQS93j6Xg5icMOF50Hq1XwBKent1D1rLgJ67nlQNYCoWYRJmTugWZlFX7FWTA4KL9YEINgwUiaQ/640?wx_fmt=gif)

**************************************************************![](https://mmbiz.qpic.cn/sz_mmbiz_gif/fY8ibThH1At4q8tQS93j6Xg5icMOF50Hq1wELWN5SOPgRXLK9ydqku3ppgiaArcDcjgIsmscXibXy21L9D58J13vdQ/640?wx_fmt=gif)
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
** ** ** ** **  

重要的我就先介绍到这，更多其他功能可以自行查阅官方文档。

  

** 最后  **

感谢群里的小伙伴  友情出演。  

如果对SD防灾对策群感兴趣的也可以关注公众号给 **【小鱼干了】** 私信微信号，我看到了会加你，拉你们进来一起开放，学习，共同进步。

文章中提到的插件资源，  公众号回复 **【下载】** 即可。

下期见  ！  ~

  

**参考** ****

* * *

  

All-in-one 官方文档  |  https://aiodoc.physton.com/zh-CN/Installation.html  
---|---  
  
声明，文档使用 GFDL 许可。  [ 详细声明请点链接查看
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484392&idx=1&sn=d4541799ffade58ee09370b9c1239a37&chksm=97a435d9a0d3bccf4ab397577108d2d92092259b4cf3ca877a891173f1e965c69ca52f7e7eb6&scene=21#wechat_redirect)

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

