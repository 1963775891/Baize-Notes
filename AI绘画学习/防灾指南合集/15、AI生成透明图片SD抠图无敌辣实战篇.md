![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At4H4icNTKuBBRobO3PqqCBp8079Wkjox9t5yKBibuewndKWWfuuIBUlY1MgPFg5XbbGnDw5hHxZnnDQ/0?wx_fmt=jpeg)

#  AI生成透明图片？SD“抠图”无敌辣！（实战篇）

原创  暴躁的卡爷  [ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

最近几天沉迷于Darkest Dungron ii 无法自拔，荒了课业。  晚上2点突然猛地从床上绷了起来，带着好久没更新文章的愧疚之心伏案奋笔写到天亮。

前几天，群友又对SD能做啥不能做啥展开的一  顿  猛烈又细腻的讨论。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7b72JvlpL2nJgVj70G3ynNzy8Nia6gRH1VEicQCyQCPFkAvXpice0pezaddJqsyGUxZbcT9QJ3TfmNQ/640?wx_fmt=png)

所以，今天我们就来聊聊在工作流设计中必不可少的一个环节——拼合。

噢，不对，是拼合前的抠图。

** **** **** ** ** ** ** ******** ** ** 拼合是结果，抠图是过程？  ** ** ** ** ** ** ** **
** ** ** ** ** ** ** ** **

对于传统设计师来说，抠图和拼合本身就是一种快速提升工作效率的手段，但是很多时候我们在遇到棘手的素材时，抠图变成了最耗时的那部分工作，而且效果不佳。

如今对于本身就是效率代名词的AI绘画来说，拼合是一个常用，甚至是必用的一个工作流程。强大的  为SD的生态又为我们提供了很多优秀的抠图插件。
这让过去还在为美图秀秀充值，为Remove bg低分辨率苦恼的设计师打开了一扇窗  。

按照惯例，如果你连SD是什么都还不清楚，你可以参考下面这篇先入门：  

[
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484593&idx=1&sn=28186490d02d1f6376e10d549c8f480d&chksm=97a43280a0d3bb968a1988fb3ad41c30b3698dd9d9316a3b38bc32d41838f1988f4400de24ee&scene=21#wechat_redirect)
[ ** Stable Diffusion 防災指南 ** ＞  ** ＞  ** ** **
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484593&idx=1&sn=28186490d02d1f6376e10d549c8f480d&chksm=97a43280a0d3bb968a1988fb3ad41c30b3698dd9d9316a3b38bc32d41838f1988f4400de24ee&scene=21#wechat_redirect)  

  

** **▍** **SD直接生成透明图片** ** ** **** **

如何提高拼合效率呢？这里我抛砖引玉提供2个关键信息。

  * 通过提示词以及对提示词敏感的模型可以获得干净的背景。 

  * 通过ABG Remover 脚本直接获得透明的结果图片。   

** **** ** ** ** ** ******** ** ** 提示词&模型  ** ** ** ** ** ** ** ** ** ** ** **
**

通常我们需要添加  _ simple background，  transparent background，clean background  _
以及颜色背景，来让生成的图片成为一个独立的物品，你还可以添加  _ isolated，solo  _
等词语将生成元素单独分离出来。但需要注意的是不同的模型会对关键词的敏感程度不同，一些擅长画复杂场景，复杂结构的模型很难绘制单独元素，故而魔法词也不会生效。

我们直接使用下面的参数来实际感受一下：

** 关键词  **

1 toy tree,simple shape,surrealism,  (extra cute:1.2),minimalism,soft and rou
nded,mellow,ar  tistry,c4d,(simple background:1.2),(whi  te
background:1.2),minimalist style,(45° isometric viewing angle:1.2),isometric,

<lora:3DMM_V7:1>,<lora:DDicon:0.2>

Negative prompt: (worst quality, low quality:1.3),plural
items,human,projection,shadow  
  
---  
** 设置  ** Steps: 35, Sampler: Euler a, CFG scale: 8, Seed: 460508448, Size:
512x512, Model: primemix_v21, Clip skip: 2,  
---  
我们会得到一组纯色背景的元素，是的你没看错，投影都没有的。在这个模型中，背景关键词作用不大，起作用的是isometric（等距视角），
minimalism（极简风格）以及一些3d相关的词。当然，2个3d的lora也能单独影响。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7b72JvlpL2nJgVj70G3ynNib95Ee9gmGibVWvJLTmPMNCFcRJWBcICWDGDnl9Bh5lAYdAnjw52eB3w/640?wx_fmt=png)

而我们把相同的参数提供给其他模型，他们会对不同的关键词给出不同的敏感程度，而有的即使你加了所有 _ simple background，
transparent background，clean background  _
之类的背景词，它仍然倔强的提供着复杂光影的背景，比如我们之前常用到的majicmixFantasy这个模型。 ** 所以  模型和关键词是  同时  生效的
** 。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7b72JvlpL2nJgVj70G3ynNwZ6MbohXKCxxhact0Z4bIicsvQ213iasqxqeppb8CJIQZQr9Gfhm30Uw/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** ABG Remover插件  ** ** ** ** ** ** ** ** **
** ** ** **

其实这个插件很强，不一定需要  背景  洁白无瑕就能把背景抠掉，但因为这个插件很强，又很傻瓜，所以上面是一个前置知识点，有备无患。

先介绍一下这个插件，顾名思义，就是帮我们去除背景的。ta可以在扩展里搜索到，也可以在文末里下载到。作为WebUI元老级的插件，我很早就了解并使用过它，但一直没有合适的场景真正运用到它，甚至它的GitHub介绍也寥寥几笔，略显冷门。

直到我深刻的认识工作流对ai绘画的意义之后，这个插件成为我推荐的必装插件之一。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4H4icNTKuBBRobO3PqqCBp8qYMzwjhK745bltok7FONZudVvK8CFcVvW1FXR7AKbFDr5XxT7oaBCQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7b72JvlpL2nJgVj70G3ynN8EXzDjiafBrZFVo48c42350icVvyqINib10BcdbHibMwVHak6Ir2cpQN6g/640?wx_fmt=png)

使用方法也很简单：

  * 文生图时，在底部脚本里选择ABG Remover，选择项里勾选第一个或者第二个，开始生图就行。   

  * 图生图就是单纯的抠其他图时，同上操作，重点是 **重绘幅度调成0.01** .然后生图。 

然后我们就会得到抠好背景的图片以及一个蒙版。像这样：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7b72JvlpL2nJgVj70G3ynNiaKQsrzgQHZdzHHQTI9QIUDTgFt0lictGC1Use1ibu4icibtibzTAoF0yAlw/640?wx_fmt=png)

Oh，Amazing！~ So easy!~

我们还可以通过调整关键词和模型，去生成其他风格种类的透明背景元素，比如这样。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7b72JvlpL2nJgVj70G3ynNcB6I0yOibyuPn6FSS1ywtc0Y8wZTet7rohjjmoVic4u50pmqlsLGoBTA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7b72JvlpL2nJgVj70G3ynNzSmkJ55PibjasYxiaIoTppC8zAGsVpF9j8As6SDaY4ibPwvIZLiaTutPww/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** 回来拼积木  ** ** ** ** ** ** ** ** ** ** ** **
**

当你能轻易的通过关键词、模型以及ABG Remover插件获得单独的，抠好的元素后，最后回到你熟悉的合成工具（PS，figma等），拼积木就好。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7b72JvlpL2nJgVj70G3ynNbXLlMeqIiblCvBDN01M7Nu9KibHIwDoiaW1px7hoR18vFPVbaTlF9BZbQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4H4icNTKuBBRobO3PqqCBp8hNYBBXfNspoSCu1Oc1y899TEclIcdOzE1x4z8icIsOLWPYdfy6ZlGrQ/640?wx_fmt=png)

  

** 最后  **

感谢群里的小伙伴  友情出演。  

如果对SD防灾对策群感兴趣的也可以关注公众号给 **【小鱼干了】** 私信微信号，我看到了会加你，拉你们进来一起开放，学习，共同进步。

文章中提到的插件和LoRA资源，  公众号回复 **【下载】** 即可。

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

