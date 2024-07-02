![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At70hicCwGDKPXXyet43lAwQSc2q2sbMfqTUnQfRE7aMkibLc4Jga7jR0tOHY6JTTAkRvic8m7nOibjoHw/0?wx_fmt=jpeg)

#  SD的优势区间，ControlNet做字体！(实战篇）

原创  暴躁的卡爷  [ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

一直在想该如何为一些web UI的神级插件起个头，虽然说起来都是三言两语，简简单单，但好像受制于很多因素，大概还是只能在实战和逗逼中体验学习到。

巧了，前几天SD防灾群里就有小伙伴询问下面这种特效怎么做的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSKBbL6aFiaxmhichFiah2KibIMiaPcXfBfGSehPvy6XU2m7fibLtx571WnS9g/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSFuVJ6uSehtU76g370BRociaib0pWVl9BHh45ib1XSbF5wVeBxiadVF3ZMw/640?wx_fmt=png)

然后群里小伙伴就热烈的讨论起来，还有人提供了自己设计的字体供大家尝试和小范围“比拼”“斗图”。这种开放精神和进步态度，让人感动。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQS52Vfr0q859eGDr4M410YfVo6wd0RnTzRU1abzwlcRE3N6mmQBHtsZQ/640?wx_fmt=png)

所以我也跟着一起从头试了一遍，捋了一下方法，核心还是使用 **Stable Diffusion** 和它的插件 **C** **ontrolNet**
，找合适的模型生成而来。过程不难，一两个演示就可以轻松学会了，案例很简单，但我的重点还是通过实战让大家了解插件的用法，这也是 **C**
**ontrolNet** 的简单入门。

如果你还不了解SD，那你可能需要先去过往文章了解一下：  [ ** Stable Diffusion 防災指南 ** ＞  ** ＞  ** ** **
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484593&idx=1&sn=28186490d02d1f6376e10d549c8f480d&chksm=97a43280a0d3bb968a1988fb3ad41c30b3698dd9d9316a3b38bc32d41838f1988f4400de24ee&scene=21#wechat_redirect)
**** 这里我就直接开始。

  

** **▍** ** 大象装冰箱  ** **

虽然不讲SD的基础，但插件基础还是需要简单说一下的，controlnet是当前SD领先MJ的核心插件之一，所有所谓的控制力皆源自这个插件，而这个插件需要准备官方提供的14个CN模型，基本能涵盖当前所需的大部分生图的控制需求。我们要完成上面这种艺术字体也是。

同以前一样，实战篇不过多赘述理论，ControlNet的理论和各个模型控制哪部分可以参考这篇文章，后面提到的“术语”都默认你读过这篇了。  

[ ** 初认Controlnet插件（插件篇）  **
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484743&idx=1&sn=6af762a7ff8938d57c506f30a426856b&chksm=97a43376a0d3ba6089c57b2c29c698e72c52ec39ca48b948634037d261d1e08d6cabab262a9d&scene=21#wechat_redirect)
** **

**  
**

** **** ** ** ** ** ******** ** ** 准备字体  ** ** ** ** ** ** ** ** ** ** ** **
**

其实这种字体美化字体肯定是主体，只是学习阶段可以不用太专注字体选择甚至字体设计，只是提醒一句不要买椟还珠了。
选好字体注意需要使用黑白的图，或者对比度极高的图，需要保证字的边界是清晰的。下图是我们的练习素材：  

  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At70hicCwGDKPXXyet43lAwQSYHmMiaMeEal0vKJu0kiaGHxW2l3LFFdMglIgneKEeO4aNMp87Ef3lRPA/640?wx_fmt=jpeg)

  

感谢群友  @末末  提供的  自己设计的字给大家练习。需要的也可以自取，已经授权。

  

** **** ** ** ** ** ******** ** ** 选择ControlNet模型  ** ** ** ** ** ** ** ** **
** ** ** **

这里不是绝对唯一答案，因为很多CN模型能实现相似效果，或者更有故事性的效果的。以比较容易出效果为例：

将字体参考图放进ControlNet中，预处理器选择invert（from white bg&black
line)，注意控制类型就不要选择预设的了，因为很有可能处理模型不是一一对应的。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSVztTmOjw7gL0eL5UKOdRvT7X1d3UHmLdjHTFCAY7zfrjK0BGAhGibyw/640?wx_fmt=png)

invert比较适合完全还原字体的细节。当然如果字形本身识别度很高的话，也可以使用Canny等模型。选好预处理可以点击  💥  按钮预览一下。

然后选择Control模型，可以选择 **Depth** 景深模型，也可以选择 **Scribble** 涂鸦模型，使用Canny描边的预处理这里也可以用
**Canny** 的模型，但控制力稍差。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSbcl2bIbvTJhicNg76NZoyS1TGgVACdvNXiaic1Zkzm6DicKWs08tGVHu9w/640?wx_fmt=png)

选择好之后，记得点击 **启用** ，开启ControlNet。

** **** ** ** ** ** ******** ** ** 选择生图大模型  ** ** ** ** ** ** ** ** ** ** **
** **

插件暂时简单的设置完毕，要选择生图模型了，大模型决定了我们的最终的风格，是真实系，是动画二次元，还是什么，这决定你对模型熟悉程度。  

生成一个真实场景下的字体，文章开始图片相似的风格，是我的目标，以此为例：

经过一些尝试，我选了真人效果卓绝的大模型 **lofi.v2** ，（还有一些其他比较真实的模型都可以备选，只是会有一些参数变化需要注意）

不同的大模型，会对CN模型的控制力有不同的适应度，所以需要微调参数。

** **** ** ** ** ** ******** ** ** 关键词和参数  ** ** ** ** ** ** ** ** ** ** ** **
**

最后输入关键词，生成一个怎样的场景和材质，就由这些关键词和设置来控制了，也可以简单写一两个关键词，但这样你就将控制参数赌在随机种子上了，我们的目标还是自己控制生图结果，魔法词部分不会的可以看历史文章。  

以下是我的关键词示例：

** 关键词  **

(masterpiece, highres,high quality, high resolution),8k,

High detail,(detailed light:0.8),rainwater,Ambient light,3d
rendering,realistic,8k,cinema light,  
(Osmanthus fragrans:1.4),Osmanthus fragrans,Water drop,(rain:1.2),(Fuzzy
background:1.2),Above water,Plant in soil,pond,45° overlooking Angle,outdoor,

Negative prompt:badimage  
---  
** 设置  ** Steps: 20, Sampler: Euler a, CFG scale: 7, Seed: 4162507521, Size:
512x512, Model: lofi_V2pre ,Clip skip: 2, Hires upscale: 2  
---  
** CN设置  ** ControlNet 1: "preprocessor: invert (from white bg & black line),
model: control_v11f1p_sd15_depth [cfd03158], weight: 1.15, starting/ending:
(0, 1), resize mode: Crop and Resize, pixel perfect: False, control mode: My
prompt is more important  
---  
  
  

** **** ** ** ** ** ******** ** ** 出图  ** ** ** ** ** ** ** ** ** ** ** ** **

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQS5oGibhqW1fSbgtYEtgxty2J2p6cI1Qic28rIESMOQQBhd0JQoHcG7AMg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSPP17kCH0IVrhL0jEjrVLRJicY8VZ8DBh5lLlt0dLE2vbYcxucE4llSQ/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

这是群友最早尝试夏天荷叶构成字形的思路（与字本身稍微没有关联很紧）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQS90AibHpMFkAwkzfDHeSBIKfEZfJ2Uv4QIAONvms4P05QleM72udzaqA/640?wx_fmt=png)

如果觉得字体图结合的还不够，可以更加放飞一些，以图像效果为主导。这些就比较随意，按需自己调整。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQStQA027BhgRvlK1tfsvBTnmyMSklEGNPHCyNNCrmK7M0yRibEVegNTvw/640?wx_fmt=png)

  

** 注意：  **

  * 上面我使用的是invert+Depth 达到的效果，我调高了control的权重，并且还设置了控制模式为 更偏向提示词。这不是唯一解。后面问题部分会细说。 

  * 不熟悉关键词，和模型的，可以  按照我的顺序反向操作，先填写关键词，然后挑选合适的模型先出普通的图片，最后再使用ControlNet锁住字形。 

  

** **▍** ** 出现的问题  ** **

实际在一下午的练习过程，不同的基础会发生很多匪夷的问题，相信这些问题我遇到了，你们也可能会遇到。

** 1.字形一坨死黑  **

这种情况时常发生，大概率是因为Control的控制力太强，可以适当降低CN的权重，或者像我上面提到的，将控制模式改成更偏向提示词。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSWAwgZmfESrYUs0rW8ObFB4dBXssVePbjeFdXF1CKPabmgrD8aYLf0A/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSmhgPibIQRTCsRdFkIDicWeLUK84oFIjALg7IsGIfq5cVjIx272dhdaDA/640?wx_fmt=png)

** 2  .  字没有啥样式  **

** **** ** ** ** ** ******** ** **
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At70hicCwGDKPXXyet43lAwQS0lPHXx5CdiacPwSxt6sw7JiauJ9Oz2QSmJC2mgJicRrsEaLNWZMlhaTlA/640?wx_fmt=jpeg)
** ** ** ** ** ** ** ** ** ** ** ** **

这种多半是因为关键词太少了+控制力过了。先尝试生出一张漂亮的场景图。或者参考我的历史文章生图实战篇。

** 3.字呢？  **

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSODiagLzXoZjHicIC5HTKPC9QqD6meRiaUow1qhh59meLpEicW2XsLZGrwg/640?wx_fmt=png)

这个也很好理解，控制力不够，提高CN的权重。或者使用更随机的涂鸦模型，就需要将控制模式改成均衡或者更偏控制。还可以使用多个CN
单元，补充控制边缘或者景深等方式。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSWZaXKOqDSTE8TAxkvKJM76Vq8dBbPhib35tZ1DdiaTGZTwY0vMBnia1WA/640?wx_fmt=png)

** 4\.  ** ** 字是不是只能用粗的？  **  

理论上更粗的字更容易成为画面主体，但因为CN的精准度很高，所以画面只要好看，字体的字重不是关键因素，字的笔画间隔，识别度更重要。比如这位群友的打榜后的freestyle,就很好。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSOb3h5MhdbrksJFecflelbThZ694aX30jl9Ve9ibLUibwORRNfX3LcicZQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSsanHdOn07buCMnK1ILWalg2WvHlxGnfwYkq80NxV3icznuiaFvRZicjJw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSZtprbZnKpictUjo5M9zrI3eRsNvQ3p4MvUSmNyyFOqLiciaM4H4q9TR1g/640?wx_fmt=png)

  

** 5\.  ** ** 我没有你这个预处理器！  **  

有人因为安装的WebUI版本较早，ControlNet 也不是1.1的，更早的版本可能有一些模型和预处理器的缺失。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSf24ZHR6wodp6bDEfMUQ8yFZ0uibXVLldpODWqIic7lhlTuSQWkutsk7w/640?wx_fmt=png)

还有因为版本老旧，去和IT打辩论的群友。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At70hicCwGDKPXXyet43lAwQSVzpNCoHGSWlXSpptgpMIGjUsjmclKiaj4QjEaIVFylryDfWWYBqklsA/640?wx_fmt=png)

我大概只能说2点。  （先  笑一会儿  ）

  1. Invent不是必须的，可以有很多替代方案，上面也有提到一些。 

  2. CN的版本当然是越新越强，但也会出现不兼容的问题， **总之，IT说的挺好的，还有和IT搞好关系** 肯定没错，明天可能就给你更新了。 

  

好吧，以上。你学会了吗？  

  

** 最后  **

感谢群里的小伙伴出品与授权&友情出演，网名就不贴出来了，需要可以加。  

如果对SD防灾对策群感兴趣的也可以关注公众号给“小鱼干了”私信微信号，我看到了会加你，拉你们进来一起开放，学习，共同进步。

👇关注公众号，获得免费在线SD，下期见。

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

