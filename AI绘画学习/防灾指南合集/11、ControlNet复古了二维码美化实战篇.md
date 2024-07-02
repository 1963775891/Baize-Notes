![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At70hicCwGDKPXXyet43lAwQSsYib6HoEW9EuBVsiaGgAKjs09JibDiasrxlRRh9dqebblXL6M1MToGRiaVQ/0?wx_fmt=jpeg)

#  ControlNet复古了二维码美化（实战篇）

原创  暴躁的卡爷  [ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

  

友情提示：本文内容图片特殊，在深色模式下阅读，体验更佳。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7JC99dYaRM9ibEYkKRusaV9WcbvZNI3IhlP8nKe4ymzklk8DXyzjUyp0lAMiaeqylchUxMRR1dp7FQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At6paJtAG9aZmVW9uq1r4ibXU3ibBkfon7x4VLdxwIvCVepPiaplUAWib3VNmYnXBAojClWthBrWu1Mn6g/640?wx_fmt=jpeg)

就是最近有个二维码很火，你们见过吗？这个二维码最近到处都能看到，我们SD防灾群里也小声议论（八卦）了三五回了，你们见过吗？大概长这个样子。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7JC99dYaRM9ibEYkKRusaV9Nn62y1sE1kZibGmZibPRG5IN6Mkr4Ku6JjlkESUPj0QMofibIDxpPqlYQ/640?wx_fmt=png)

对，这是个二维码，真的可以扫，扫了以后是一个叫小杨的男人的微信。但为了防止你们总打扰小杨，我很善意的给他的女人打了码。

所以因为他和他的女人，突然就掀起了一阵强大的二维码美化风。上一次这么关注二维码美化的时候还是...移动互联网刚兴起的时候。果然是  天道好轮回，
世事难料啊。

为此，SD防灾群又展开了一次“  巨型  演习”，非要把这美工title给自己安排得明明白白。没办法，这就是大家的拼劲...  另  外
二维码美化有没有需求，  很多人都有聊，但聊  这个本身就  很  没意义。

** **** ** ** ** ** ******** ** ** 很遗憾，这又是SD的专属快乐  ** ** ** ** ** ** ** ** **
** ** ** **

与之前做字体一样。核心还是使用 **Stable Diffusion** 和它的插件 **C** **ontrolNet**
，找合适的模型生成而来。ControlNet大概就是老天用来拯救在MJ淫威下强大但复杂不易学的SD吧。过程也不难，甚至可以说无脑，但却有着很多隐形知识在其中，且听我慢慢道来。

如果你还不了解SD，那你可能需要先去过往文章了解一下：  [ ** Stable Diffusion 防災指南 ** ＞  ** ＞  ** ** **
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484593&idx=1&sn=28186490d02d1f6376e10d549c8f480d&chksm=97a43280a0d3bb968a1988fb3ad41c30b3698dd9d9316a3b38bc32d41838f1988f4400de24ee&scene=21#wechat_redirect)
****  
** **▍** ** 大象装冰箱  ** **

** **** ** ** ** ** ******** ** ** 下载二维码ControlNet模型  ** ** ** ** ** ** ** **
** ** ** ** **

首先，需要去下载一个用来控制二维码的  ControlNet  模型，目前主要有2个都还不错的ControlNet模型。

1\. **Controlnet QR Pattern**

在C站搜 **QR Codes** , 就是下面这个，注意左上角的模型类型是controlent，这个类型C站全站也没几个，挺好找的。（黄脸上也有）

写文章的时候这个Control模型还没有更新到v2.0，所以文章素材绝大多数都是v1.0生成的。2.0还是要强一丢丢。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6paJtAG9aZmVW9uq1r4ibXUxbyBEqq42bj657ib2ibicJKF0iaQwR0NJoqb8HTfgia1RlP8CkXXW89Nmug/640?wx_fmt=png)

我们可以通过C站模型详情介绍中的链接 https://antfu.me/posts/ai-qrcode 官方给出了很详细的教程。  

看教程，好了本篇完毕。

2\.  ** Controlnet QR Code Monster  **

这个模型C站没有，只能在黄脸上下，搜索关键词 **monster-labs** ，这个模型使用感受也挺好的，好像更适合做不规则线条（
没有严谨对比测试，并不负责）  。

接下来就是要把control模型放进模型目录下：  
“stable-diffusion-webui\  models  \controlnet\”

在WebUI的CN插件中，刷新并重启服务就能看到和使用。

** **** ** ** ** ** ******** ** ** 跟着官方教程来一遍  ** ** ** ** ** ** ** ** ** ** **
** **
官方教程其实讲的很清楚，我们简单挑重点过一遍，而且主要使用的是工作流的方式。ControlNet是重要的一步，但不是全部。这也是使用SD的主要注意事项。

** **  
** **

** ** 1.设置环境  ** **

看防灾指南，不多说

**  
**

** 2.创建二维码  **

网上有数百个QR码生成器，你爱用啥用啥，有会员，有钱也随意炫，我这里推荐上面的官方又提供了一个免费开源的工具，主要是他有WebUI的插件形态，不用来回切换浏览器很开心。https://qrcode.antfu.me/
，插件就自己搜吧。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6paJtAG9aZmVW9uq1r4ibXUDiaOuJ5VibmgEvukickROeH4uLibp9dS560xgnb2Ep1VXXibt29OgY9n2pA/640?wx_fmt=png)

这个二维码生成器界面美观易用，功能齐整。也拥有很多样式可以选择，比如这样：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6paJtAG9aZmVW9uq1r4ibXUgAMZsXh57efX2DYweoyKT8GicNJPicVmQ9PRYg2zlNgNR55lJGmzNicxw/640?wx_fmt=png)
|
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6paJtAG9aZmVW9uq1r4ibXUsCk9xpbVX2TAmVcPJYgc1WrtXlx1yqHKV9R0vBiayYXZSHO6OPv18Eg/640?wx_fmt=png)
|
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6paJtAG9aZmVW9uq1r4ibXUE1GKAhlWGblokpCFkddlTDFjkwJa5o7j2o8xSNzdHBglko7XmBDohA/640?wx_fmt=png)  
---|---|---  
  
稍微注意，二维码的复杂程度取决于内容字段长度，比如带https:// 就要长好多，但如果没有https://
扫码是不会做跳转的，这些大家自己尝试和取舍，但也不要为了追求超短链接去网上找短链生成器，微信封的很严。  

至于图形样式，我比较推荐上面第三种，色块区分比较容易给AI发挥空间。(个人)

**  
**

** 3\. Txt2Img生图  **

该试试生图了，官方也希望你在跑二维码之前先试着生出质量不错的图，那我们就偷个懒，拿上一期做字体的关键词和设置复用好了。

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
** 启动ControlNet  **

把第二步做好的二维码发送至ControlNet或者复制过来。预处理器选无，  或者像字体设计一样选择Invert好像也行
，模型选择一开始你下载的2个ControlNet模型，任选一个就行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7JC99dYaRM9ibEYkKRusaV9WB0Jxia0q6k9EZoiaMl9HDRyI1Cl3HFstAU2eOXVglDXvnQtFiauVtsJg/640?wx_fmt=png)
(这是官方图素材）

** 4.抽卡和金色传说  **

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7JC99dYaRM9ibEYkKRusaV9yGZEswKCO6aPBloUiarYC7NEicNRwhDffKyMKQ0tSGtreFdd4upH4WSQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7JC99dYaRM9ibEYkKRusaV9yGZEswKCO6aPBloUiarYC7NEicNRwhDffKyMKQ0tSGtreFdd4upH4WSQ/640?wx_fmt=png)

官方太凶残，在找到一组很满意的参数之后，就把批次增加到了100左右，也就是来一个100连抽，然后他说他就去睡觉了，跑通宵？what？  

这种电费和电脑都很残暴的土豪不值得我们学习，我们就跑个4x2就行，通常好的关键词一组就能看出效果。  

当然你需要检查  生成的图像是否可以扫，  这是一个平衡，  在风格化和识别度上  ，  官方提供的调整是  控制  开始  步骤和结束
步骤。我自己用Control的权重来控制。  

看到上面2组图，第一组意境更好，因为有前中后三层景物，而且前景还比较清晰明确，但很遗憾，他们勉强能用个别手机扫出来，并不能直接被微信识别。而后面一组用了更强的控制力，可以直出就能用。

当然，如果我们本身追求的是艺术性，风格化，也可以保持你最喜欢的画面，不用在意识别度，我们跟着官方往后走。

  

** 5.掏出传家宝PS精修  **

如  从模型生成的图像并非在每个细节上都完美无缺。我们可以使用 inpaint
功能告诉模型重绘图像的某些部分（最好保留与原始生成相同或相似的提示）。这里官方直接祭出了传家宝PS，
**好家伙，原来神奇的二维码不是一步到位的，还是P的啊** 。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At7JC99dYaRM9ibEYkKRusaV9dnKDicljXJU4o3OGaOU6G4ziam2Uo9xH5HHxiaNrct5Gd4spkgh3Xv1Vg/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7JC99dYaRM9ibEYkKRusaV9WrblNkfZnEV1PLW9AuXkVHKpvfWa1jBeqUcLYtDwgwSWicqcEOqkHWQ/640?wx_fmt=png)
(这是官方图素材）

他们还提供了一套很厉害的工具，就是上面提供二维码的网站切换tab能看到，它能将你的图片不容易识别的地方都挑选出来。然后根据需求调整，说实话，完了半天我没玩明白这工具咋用，最后很笨拙的下载一个透明的遮盖层，将这一层导入ps中。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7JC99dYaRM9ibEYkKRusaV91iafxrMiays5apw9ibG4qYcXo2JaqibIzy70rOtSribeKqsAJ1ThjpiaOHFQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7JC99dYaRM9ibEYkKRusaV9YnfJv5Sqpl2vGCL1Zoibr1j3y1kX5ARYDQNLPgUMeSIdLGpyx5FMXQw/640?wx_fmt=png)

(这是官方图  素材）

在ps中结合图片进行局部重绘，或者手动调整。还没完。

** 6.高清放大  **

官方建议的生成大小为 920x920
像素。但是图片质量还是不尽人意，人物是缺少手部脸部细节的，所以需要进行图片的高清放大，这也是很多群里的小伙伴总是嚷嚷为啥我得图片这么糊。是的，你需要高清放大。

高清放大的方式有很多，以后会专门开一期单独讲。  （我挖了太多的坑了）

这里就照搬官方给的SD放大脚本，（  SD放大是图生图专属放大脚本，现在并不是很受欢迎，因为有更多更好用的出现了）  ，脚本在图生图的最下面。点开后：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7JC99dYaRM9ibEYkKRusaV92ZcHpg4H9VyskhR58QSshMFeyjcU7yvSDEJOJJfmqLFJakh3p6v2iaw/640?wx_fmt=png)

(这是官方图素材）

把参数调好，放大2倍，太多会爆显存。等一会就好了。

  

** 7.最后的处理  **

其实我也没想过他们还要再p一次图... 使用Photoshop和Lightroom进行微妙的调色和后期处理... 完成。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At7JC99dYaRM9ibEYkKRusaV9Tq410WP8TsgDx8qlxD15ZBGZibwnaQj2CZibt5v8fwYEWpQJPvq9BsyQ/640?wx_fmt=jpeg)

  

** **** ** ** ** ** ******** ** ** 工作流的重要性  ** ** ** ** ** ** ** ** ** ** **
** **  

其实细心一点发现在第四步，我就已经完成了一个简单的二维码美化了，刨去第一步的环境，第二步下模型，第三步复制以前的参数，只有 **一步就完成了。很简单** 。

而  带  着大家完全一步步按照官方教程走一遍其实还是想通过这个实战例子告诉大家工作流才是现在你们  看  到的那么
多美丽漂亮的AI绘画出图背后的真实做法。  流程很长，但熟练的人也可以很快完成。  为什么是熟练人可以很快？  因为以前做过，可以举一反三  。

你会发现  AI  的瓶颈好像不是技术，关键词，参数，又回到了  一开始提到的  审美，  创意、意识形态  、经验判断这些  **隐形知识** 上。

这就引申出当下AI绘画的核心。  以前的经验仍然宝贵，  工作流还是工作流，只是串联的工作流内容不一样罢了。

  

** **▍** ** 通往罗马的路  ** **

** **** ** ** ** ** ******** ** ** ** **** ** ** ** ** ******** ** ** 图生图更容易
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

我自己在实际测试中发现，直接用文生图的二维码还是比较容易出废图，主要问题还是识别率上，虽然很多时候画面和风格让人眼前一亮。

** 但可以用图生图解决。  
**

在上面 **步骤3** **停下来** ，直接找到一张生成的觉得很喜欢的图片，导入图生图（带关键词&参数信息）。

接下来就是在图生图里启用 **C** **ontrolNet** 。  使用monster模型时需要稍微开高一些控制权重（1.5左右）  。然后光速抽卡！~

来看一下效果：  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7JC99dYaRM9ibEYkKRusaV9xtib3tjqBiafGAsibkH9DvPJ8ah8mCRdeTZ4Xicpkicic2hgE8CbpxX6ca0Q/640?wx_fmt=png)
|
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7JC99dYaRM9ibEYkKRusaV9Xw9eRibtRTmsBNZwuAAnYoyUmmdFGwVq1BVr2Omibho5cchKsYsgvrQQ/640?wx_fmt=png)  
---|---  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7JC99dYaRM9ibEYkKRusaV9ia0Gehtiaahw3hGsThjvNSGqD83kaM4GpvqKWnAVo9mv8YxXmibKz93uQ/640?wx_fmt=png)
** **** ** ** ** ** ******** ** ** ** **** ** ** ** ** ******** ** ** ** ** **
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

还可以把二维码反相，会得到不同的视觉感受哟！  ~是不是更简单，更酷~

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7JC99dYaRM9ibEYkKRusaV9WWVbu2iaWEpzqW5ia9IYu0jH08G3dMy6v7xC2v7YFYdROo1qMtPWFVIA/640?wx_fmt=png)

  

** **** ** ** ** ** ******** ** ** P图谁不会？不满意叠图层  ** ** ** ** ** ** ** ** ** **
** ** **

在用controlnet生图完毕效果不太理想的，识别率不高的情况，你还可以把喜欢的图片（无法识别）也丢进PS中，然后把二维码也丢进PS中...
嗯，剩下的其实不用我教你，你一定是设计师，也一定懂...  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7JC99dYaRM9ibEYkKRusaV9ibpfvicyj9d4a0JCY7k8LHicibGzH07ibJ1z9TTEeYDQA7qaDbsUvsfkM0w/640?wx_fmt=png)

虽然也是用ps，但这比上面官方提供的方式要粗暴得多，当然也快的多，而且识别度也高， **就是** ...  

神马？你连PS都不会，调光，图层特效都不懂？

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At7JC99dYaRM9ibEYkKRusaV95g5vLBpUzTLpkSHR19icSf4jsALFz3KdAYRxjRhia6Hu5yaG6UJpBYPA/640?wx_fmt=jpeg)

那就直接二维码糊上了，调透明度就行了，这不也能出效果嘛！  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7JC99dYaRM9ibEYkKRusaV9URFoApRnbBCbAwPc0niaMwJDhzcxJGoynUBfo9tX8QF15vn4ibNribLtQ/640?wx_fmt=png)

  

** **▍** ** 其他风格的QR  ** **

好了，自此你应该也基本掌握了使用第三方的ControlNet模型，和更多的工作流方式去完成一个需求任务。  

剩下的就欣赏一下不同风格，不同模型的QR码吧。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7JC99dYaRM9ibEYkKRusaV9o9OGXEiaAAqPibnyu5LE3svl6gQvpp2nXvnxMknicibV3LDiaFfXluzd58Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7JC99dYaRM9ibEYkKRusaV9IgdZIOVtkJTLjziaTSyyLIUPVGHp3icMx4prLcJicfTayhjPt3gIYVs4w/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7JC99dYaRM9ibEYkKRusaV9t5BskVZcmk3HMicEkAmfGKduiakNj9M9CicicAspEvqSHIwrJZHQfPQNzw/640?wx_fmt=png)

这组我很喜欢，相比较很多硬凹出来的，我挺喜欢这些视差的二维码，文章开头的那一组窗外也是相似的，很妙！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7JC99dYaRM9ibEYkKRusaV9uAGuryegzpBdjkwL01gDI66icG0kcKXmwM3EeZ5Yw9vj9lwiaMp6oV2Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7JC99dYaRM9ibEYkKRusaV9oTXqXHHSH3gu3sYapmLfoZsAEGEpU4eK0HzyfjyicP1JeYMxLOqHHnA/640?wx_fmt=png)

上面我喜欢的巧妙构图类型群里有人不喜欢，说没妹子... 没灵魂。其实吧，url简短才容易给你注入灵魂，不然妹子都花吧拉叽的，看啥看...

你说是吧~ 看啥看， 还不去试试？  

  

** 最后  **

感谢群里的小伙伴出品与授权与  友情出演。  

如果对SD防灾对策群感兴趣的也可以关注公众号给“小鱼干了”私信微信号，我看到了会加你，拉你们进来一起开放，学习，共同进步。

👇关注公众号，获得免费在线SD，下期见。

**  
**

**参考** ****

* * *

  

Stylistic QR官方文档  |  https://antfu.me/posts/ai-qrcode  
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

