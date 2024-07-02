![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At6fodnL41dBuHG30GArFa8FK2CYVmM07Laxe2snWFmiarYRtZtEQVJiavJwIrZLSaytTN6RvE52jvxg/0?wx_fmt=jpeg)

#  违法乱纪的事，我劝你不要干！用ROOP（插件篇）

原创  暴躁的卡爷  [ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

最近去“博德之门”出差太久了，贻误了更新... 挂了几天的空挡，又在一个失眠的晚上被无形的力量拉起来伏案。

上个星期防灾群进了一个新朋友，上来就“帮他朋友问一下”有没有一键换脸的AI，他想做恶作剧。结果一不小心就把事情聊严重了...造成了一堆人的社交圈信任危机。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6fodnL41dBuHG30GArFa8F4sMIB5kyhNLBypOvoIKPkZiay14iauGOGWLpLsaWy8icxvG1kiaKqkGGqg/640?wx_fmt=png)

当事人要求重码出镜。聊天中的关注信息涉及到比较严重的歧视问题，也码上了，勿问。

段子归段子，玩笑归玩笑，最近SD还真有一个插件贼火，可以不用炼人物LoRA就能实现换脸。前段时间火了个App叫啥啥相机的，有好事者推测Maybe用的这个插件。  

所以今夜我们来介绍这个火了又没完全火的SD插件。

** **▍** ** ROOP插件  ** **

先看看插件效果，比较可惜插件目前仅仅支持图片，至于视频换脸其实也是一个很早的技术了，只是因为涉及到太多相关法规，不多聊。  

Target Video  |  Output Video  
---|---  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/fY8ibThH1At6fodnL41dBuHG30GArFa8FseeL1qctJwkEy0HGBbFMxbib0ibknvdqia9e8x1NjIpRLMbXludledQsA/640?wx_fmt=gif)
|
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/fY8ibThH1At6fodnL41dBuHG30GArFa8FzloaSESAU6VoIsXbc36kKb7r8viaGicGdajS9gnOEia4T7FcxpZ5PQaoA/640?wx_fmt=gif)  
  
素材来自插件基于的roop技术 https://github.com/s0md3v/roop

老规矩是先看下载安装，再看如何使用。但因为这个插件有些不一样。我们就反过来，先跟着GitHub的文档看如何使用。

** **** ** ** ** ** ******** ** ** 使用  ** ** ** ** ** ** ** ** ** ** ** ** **

  1. 从插件菜单中找到roop（大概跟controlnet 放在一块。如果没找到的不要急，往后看） 

  2. 在“roop”下拉菜单下，导入包含人脸的图像。 

  3. 打开“启用”复选框 

  4. 就是这样，现在生成的结果将具有您选择的脸，是不是超简单，一键换脸？ 

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6fodnL41dBuHG30GArFa8Fhqq8xbzcJC1A9D0gwEUnoVwpVicGcSzuOMibkncexCGicia68M5bHqyia9A/640?wx_fmt=png)

  

** 官方还给了一些使用技巧  **

  * 首先，确保启用“恢复面部”（推荐选择GFPGAN）选项。您也可以尝试“  Upscaler  ”选项，或者为了进行更精细的控制，请使用“附加”选项卡中的放大。这个过去我们专门花了好几篇来讲，如果对放大还不了解的请进传送门。  [ 我生成的图为啥糊的一批？（插件篇） ](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484870&idx=1&sn=13e7f0437b09c7dc5ad9ad7fabcf62de&chksm=97a433f7a0d3bae1d2867a5011fb2f952da46a6e60cd1863af0d41ac5551f1afdf0a04c956b4&scene=21#wechat_redirect) >>
  * 为了获得更好的质量，请使用 img2img 并设置去噪并逐渐增加它，直到您获得质量和相似性的平衡。0.1 
  * 如果图像中有多个人脸，请使用“逗号分隔的人脸编号”选项选择要交换的人脸编号 
  * （ **注意这一条很重要** ）如果你启用了插件，也没有报错，但还是不显示替换成功的图片，则表示检测到您的图像是 NSFW（限制级的） 或根本无法检测到人脸。 

  

  * **补充一个官方免责感受一下严肃性**   

该软件的开发人员意识到其可能存在的不道德应用程序，并致力于采取预防措施。它具有内置检查功能，可防止程序在不适当的媒体上运行。我们将继续朝着积极的方向发展这个项目，同时遵守法律和道德。如果法律要求，此项目可能会关闭或在输出中包含水印。（👍）

  

** **** ** ** ** ** ******** ** ** 安装  ** ** ** ** ** ** ** ** ** ** ** ** **

老你可以通过在扩展中心加载扩展列表后搜索roop，点击安装。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6fodnL41dBuHG30GArFa8FRoaK6wNyR0kdxGxYX9BNc4JrzSVDk26Uhj9uQ6h04wGaDeicwLRkT0Q/640?wx_fmt=png)

也可以直接从网址进行github url安装。

安装地址：https://github.com/s0md3v/sd-webui-roop  还可以通过文末提供的下载方式手动安装。  

** 但是与以往的插件不同，这个插件安装是需要Windows环境的。  
**

  

> 在 Windows 上，下载并安装 **** ** Visual Studio  ** 。在安装过程中，请确保包含 **Python** 和
> **C++** 包。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6fodnL41dBuHG30GArFa8FSOibcBtzUy1ITr3TamXZJnIkzXfrpUheHicupjC6F01S6HcG2uQiagbHw/640?wx_fmt=png)

就是这个东西，可以在官网下载：

https://visualstudio.microsoft.com/downloads/ （文末下载也会提供）  

安装好所需环境后还需要

  * 运  行以下命令：  pip install insightface==0.7.3 

  * 关闭 webui 并再次运行它 

  * 如果遇到错误，请下载  inswapper_128.onnx  模型并将其放入目录中。'NoneType' object has no attribute 'get'<webui_dir>/models/roop/ 

对于其余错误，官方说：请使用谷歌。祝你好运。 ![](https://res.wx.qq.com/t/wx_fed/we-
emoji/res/v1.3.10/assets/Expression/Expression_2@2x.png) （这也太调皮了）

  

而我，很遗憾。我倒在了安装环境第一步：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6fodnL41dBuHG30GArFa8FFuwjSia6zFrdGCeqGETHxfC4V1RKygE6dLlO1VEOE4pPLr5mXuFTJDA/640?wx_fmt=png)

** 是的，这一期插件我没有安装上，也没有使用的需求。  **

** 还是想通过这一篇文章告诉大家，换脸有法律风险，请大家不要侵犯他人肖像，隐私。更不要做  违法乱纪的事情。  **

** 如果使用真人的脸，建议用户征得相关人员的同意，并在网上发布内容时明确提及这是 deepfake。  **

  

也确实在很多地方看到大量的安装失败的案例，我没法解答，尤其是安装VS环境上，不亲测总有洗稿嫌疑。这里我推荐白马的两篇文章详细讲解：

[ 【Stable Diffusion】无需Lora，一键换脸插件Roop
](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487143&idx=1&sn=f564fb2e97142443fd706a15a3801ce3&chksm=9fbece53a8c9474550a6bdc7b15a8bd1961c0a5f48b8c736a18cbd1fb5906e5008b544383af4&scene=21#wechat_redirect)  

[ 【Stable Diffusion】多人物脸部替换，一键换脸插件Roop（2）
](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487296&idx=1&sn=0359f42088aaf09f80141c43f88fa78b&chksm=9fbecfb4a8c946a2446ff15137cc8dcfb437401e1ad58b3a4c84b1b1dd3af9622faea80ce5db&scene=21#wechat_redirect)  

  

  

** 最后  **

部分杜撰场景如有巧合纯属巧合。  感谢群里的小伙伴  友情出演与素材授权。  

如果对SD防灾对策群感兴趣的也可以关注公众号给 **【小鱼干了】** 私信微信号，我看到了会加你，拉你们进来一起开放，学习，共同进步。

文章中提到的插件和微软安装环境资源，  公众号回复 **【下载】** 即可。

下期见  ！  ~

  

**参考** ****

* * *

  

roop  |  https://github.com/s0md3v/roop  
---|---  
sd-roop  
|  https://github.com/s0md3v/sd-webui-roop  
  
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

