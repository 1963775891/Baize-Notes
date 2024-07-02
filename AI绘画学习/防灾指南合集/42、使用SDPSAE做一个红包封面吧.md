![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At5D7sbQjuJm8yHte3N7qjyWYWtxZ5Fp44iaUiaG7L3UoYE4SNyt0Uehib4bdLjicyVHSEJL6pJTuctjRQ/0?wx_fmt=jpeg)

#  使用SD+PS+AE做一个红包封面吧

原创  暴躁的卡爷  [ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

最近，有一点忙碌，也有一些  困惑。  大概每个时间段都会遇到（给自己的倦怠戴上一顶冠冕堂皇的帽子）。  

好在AI的天也在这个时间变化得没那么快，就好像刻意的在等一些有心人，给大家一些些放下浮躁的情绪，好好沉淀下来的时间。
![](https://res.wx.qq.com/t/wx_fed/we-
emoji/res/v1.3.10/assets/Expression/Expression_21@2x.png)
要硬说有什么错过了没给大家讲的，大概也就只有一个SVD了。这是啥？stable video diffusion， 一个由SD的创造公司stabilityAI
去年11月的时候发布的可以直接将图片变成视频的扩散模型。img2vid。  
![](https://mmbiz.qpic.cn/sz_mmbiz_gif/fY8ibThH1At5D7sbQjuJm8yHte3N7qjyWl2I8IvC47dZic6wUeErScRzF1mzKPiaXLH2hvqnUTdh20LbBFd6MRKQA/640?wx_fmt=gif&from=appmsg)  
好巧不巧，在疯狂使用comfyui进行img2vid测试的时候，微信红包封面的一些“商业化”行为疯狂地在防灾群里弥漫开来。
后来演变成一个活动，且参与到人很多，就是... 单纯的想靠变卖红包设计发家的想法充斥着大家的话语之间
![](https://res.wx.qq.com/t/wx_fed/we-
emoji/res/v1.3.10/assets/Expression/Expression_42@2x.png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5D7sbQjuJm8yHte3N7qjyWwxd1tM2Zdib40WVb9REjmwjQzcU9NrcAlkSdQDcOfzRGvibSAicODs00g/640?wx_fmt=png&from=appmsg)
于是我想要不试着用AI做一个小视频，然后去买点红包封面给大家用，过节热闹热闹。
在尝试了让显卡“疯狂锻炼”了2天后，我对animatediff和svd打鼻孔里喷了一股气，俩废物！~  还得传统工作流，打组合拳。  
  
** 如果你只是这几天被封面吸引，可以直接滑到文末领取即可。  **  
** 先看效果：  **

  

** **▍** ** AI部分-SD  ** **

与以往专门针对SD去介绍工具不同，红包封面做成什么样由你自己决定的。工具也是，你可以用webui，comfyui，当然也可以用更简单的Midjourney去做一个带有可爱的中国龙的作品。

这里我就以上面为例， 我心里想要做一个有一些“禅意”的女神，带着金银珠宝来为你祝福，祝福语我也提前想好了，早早的就写在了我的草稿本上。  

找风格阶段就因人而异了，本身就是一个经验累计的结果，比如这次我更希望是一个主流审美能接受的，且又是我个人很喜欢的厚涂画法。所以我选了一款XL模型—NJ-
Niji风格sdvn7（这个在C站很好找，就是MJ的数据集帮你做出接近Niji风格的作品）

** 关键词  ** 1girl, cinematic lighti  ng,(shadow:1.2),light,red background,

(fasion),inkling,clean background,piles of jewelry all over your
body,((coins)),bust,chest,gold and jade in glorious splendor,(((gems))),water
vapor,obscure,divine,zen,bodhisattva,monk robe,  
  
---  
  
如果你用的sd1.5的模型，记得加上质量词。

为了接近我的想要的美术风格，我们还需要加入一个lora，这在过去讲过的教程中，已经属于基操了，就不细说。

我用的还是1.9版，可可爱爱一些。权重0.5-0.6，丰俭由人。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5D7sbQjuJm8yHte3N7qjyWmrHmGdSC5Og38Iy31v45teXu1RHvD7RZIJGibBOSC0374wKq1icoo9dw/640?wx_fmt=png&from=appmsg)

大概就这么随便一连吧。（XL尺寸记得要设在1024左右，更大的需要连入放大工作流）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5D7sbQjuJm8yHte3N7qjyWdL96D6NulO3yg1XCicE2VhnaRqock6ncbvfdJMxN96hwCMzOB5wE0Hg/640?wx_fmt=png&from=appmsg)

她们当中就出现了很多我很喜欢的目标结果。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5D7sbQjuJm8yHte3N7qjyWt9UaBH3SuOYJ7oRCKHIEBroB274gkn1oI2TIoMEViauug9oKVsdib7Ew/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5D7sbQjuJm8yHte3N7qjyWZ7NbhZicPMss9HILU8PmooCzrDriaa06zcOxU7iaOAuFGwW3UHcslRpGw/640?wx_fmt=png&from=appmsg)

什么？手？我们已经教了太多次如何修手了，所以这些错误在心里已经都被她的美完全盖住了。这大概也是我们使用AI落地生产的最重要的，要找优点，而不是找缺点，指望一抽必中完美是最不现实的。

选择一个最接近心中构图和画面感的，进入下一步  。

  

** **▍** ** PS部分  ** **

这大概是整个工作流里最关键的一部分吧，也是我长久以来反复念道的隐形能力决定了你的AI是否真的听你的话。
因为我做的是社群小伙伴专属红包，所以祝福语是一定需要放进来的，这里不可能通过ai直接生成。且我还要把小鱼干了那可爱的猫头也放进去。视差动画成了我的首选目标。需要让logo和主体融合，祝福语则以元素的形式悬浮在画面之上。来，先领教一下灵魂草图。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5D7sbQjuJm8yHte3N7qjyWPbKVQ97xiakZOnElmgYwHK3QcWUicWRC82t7ClKvyGgsA8DyyAs1Uhrg/640?wx_fmt=png&from=appmsg)

** 1\.  ** 先修手。PS的创成是最简单的。
将简单重复的地方框选，不需要任何关键词进行创成就可以做到很快的修补。如果多次都很难出现满意的手，我更倾向，自己手画一下。可以先把坏手擦掉（这个更容易实现）然后随便添置一下手的大致轮廓（甚至不需要你有多深的功底）。这个之前也有讲过方法，不记得的看下面传送门。
[ AI:你都不会画手，为何骂我？（实战篇）
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247485357&idx=1&sn=adb3c961e17ffda4ebc6c2fa4e3305f3&chksm=97a4319ca0d3b88a53465d6486863d7a448b35e38ee7e3fc9b4daa970516095b73403ef1bbd3&scene=21#wechat_redirect)
>>>
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5D7sbQjuJm8yHte3N7qjyWtgicRUS9o7EY2sftpBtjGp5qt6rxUSsdOoibfyG2FyrqXyR4ayEmSJng/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5D7sbQjuJm8yHte3N7qjyWa4H6xE2QnBqzBO7tW5GRb1iaGx2xfMXNx1zk2SYialchGa9qqh4XpSBg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5D7sbQjuJm8yHte3N7qjyW1D2haWGkduz6icXY8XD8w39lM9PUqWPppjSprAn2TCqoVeVKFmO96fQ/640?wx_fmt=png&from=appmsg)

很快，你就能收获“意外之喜”。  
** 2\.  ** 再把我可爱的logo，猫猫头塞进手中。做个简单的遮罩，加点光影，让两种画风融合得不要太突兀就行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5D7sbQjuJm8yHte3N7qjyWCZqZiaCPE4WBYYaCXxHnqkDgVBluJicfYFqQDDfpC9NQ7Pj3KH8tWGLQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5D7sbQjuJm8yHte3N7qjyWLiaVXicuHjgb5eZayibSKaSUmwm3rrnOrVGGTuuagV2hbfREpibA1JsG0A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5D7sbQjuJm8yHte3N7qjyWT1Zjme2cehGa9LibyuF9hnXnWBlESfbZhzlNMzXHCmBURueyHHMWutA/640?wx_fmt=png&from=appmsg)

**3.**
然后就需要为视频做准备了，主要包括尺寸调整，需要继续使用PS的创成进行扩图，使用PS的对象选择工具进行快速的抠图。为了视差的元素，需要把宝石和金币都扣出来。成为独立元素。（记得分好图层）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5D7sbQjuJm8yHte3N7qjyWZam8dgYCWELO6ysatFHhaDQqxW72MVPicmnT0uUvHclnlBOYpA4zS3w/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5D7sbQjuJm8yHte3N7qjyWP1a66V9JtgPgR7Fy0wnb9w3wHLgkRrjzJibKxhicLN6o9IkkBUgsRb8w/640?wx_fmt=png&from=appmsg)

注意，扣掉的，独立的元素还需要使用创成进行原始底图的补充，不然视差动画就“露馅”了。最后对比一下这里处理的前后差别。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5D7sbQjuJm8yHte3N7qjyW27SZuIQ2DYiagw0gJvZduYyLVibXRIpG34SoQPicm3rWsgUmb0xicdys9w/640?wx_fmt=png&from=appmsg)

**4.** 然后就是另一个重头戏了，注入灵魂！专属祝福语的字体设计。因为需要字像悬空的符文，所以字形需要更接近图形的表达，也就是装饰元素>
识别度。不然会和主体内容抢注意力。  所以，我在iPad上手写了一些“鬼画符”。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5D7sbQjuJm8yHte3N7qjyWvfibc86bcyqCxtlwRt8udBC18tkJYmeiaV1bgLs5xuvFQdsCvmAdz4GA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5D7sbQjuJm8yHte3N7qjyWn8CRXRbn2Xwic9icFHKcHIUfawNYEL7O7QMDPfUwcEbBgfTCnrJOwmiaA/640?wx_fmt=png&from=appmsg)

**5.**  
最后将上面的这些“元素”拽进画面中，进行组合排列。想象他们悬浮往外扩散的效果。
因为最终是视频，所以所有元素都堆进来的效果只要不太差，就符合任务目标。他们同框的时间很短，“出勤”是有时差的。
分好图层，做最后的位置调整，给一些前景元素景深效果(模糊)。保存psd了。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5D7sbQjuJm8yHte3N7qjyW2lMYY8Dib9Diclg8n9K1wBlBaTvFNjtMIichl20udm6vSiaZojZicnrZzbw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5D7sbQjuJm8yHte3N7qjyWdq7mN0QYUWbjibibSqzwrTp2EicqrwGu8EE2Krdl1zZrV5icBIGLX14V3w/640?wx_fmt=png&from=appmsg)

  
** **▍** **AE部分** **
其实AE部分没什么值得特殊讲解的，主要用了2个插件，且2个插件其实也都可有可无。我主打的就是一个“体力活”。无非就是4层元素的进入和消失，和摄像机的推入推出...  
咳咳.. 其实主要是因为我太久没用ae，悲催的使用习惯让我一直做完都没有保存过一次。直到第三次渲染，到处3s 视频的时候，文件崩溃了...
![](https://res.wx.qq.com/t/wx_fed/we-
emoji/res/v1.3.10/assets/Expression/Expression_11@2x.png)
对，一次都没存过，连工程目录都没有，就自然连自动保存文件也不存在。  好在...
东西大致上做完了。（这也是为什么有人说主体人物不居中，我也发现了，但我没法改...或者说懒得重做了）  算了，不重要，我可以简单的重新过一遍。  **
**** ** ** ** ** ******** ** ** Pt_Multiplane  ** ** ** ** ** ** ** ** ** **
** ** ** 先是视差动画插件，Pt_Multiplane。其实我后来发现它只是一个效率插件，因为我压根就没用...纯手动拖的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5D7sbQjuJm8yHte3N7qjyWHsmeRiaoJprLOuNvPMCWwNyZESFCuDycrscg8nNmPgIWQbrNog7W9Cw/640?wx_fmt=png&from=appmsg)

插件会新建一个镜头（摄像机）。镜头就是你的主合成结果了。你需要把视图切换成顶视图，然后将元素按照希望的景深位置放置好。

比如我会按照背景-人物-人物遮挡-字符元素-宝石金币的顺序去布置。然后动画打上镜头推移关键帧就行了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5D7sbQjuJm8yHte3N7qjyWNkwDDf9L6icQAfxYicMUv1Ppgu0VuD8arLfPvzr6tD5hfW2UmErHRGjA/640?wx_fmt=png&from=appmsg)

** **** ** ** ** ** ******** ** ** Loopflow  ** ** ** ** ** ** ** ** ** ** **
** **

Loopflow名声在外，其实没有啥需要特别介绍的。这套视觉其实也不需要它，只是因为最早的起念，是想用ai生视频，而技术和loopflow相似同源，我就顺手安排了。让背景层滚动一下也挺不错。（其实个人觉得反而比svd直接抽卡要效率得多得多，也许还是我不够强
![](https://res.wx.qq.com/t/wx_fed/we-
emoji/res/v1.3.10/assets/Expression/Expression_41@2x.png) ）

** **** ** ** ** ** ******** ** ** 微信红包封面开放平台  ** ** ** ** ** ** ** ** ** **
** ** **

这里不得不提一嘴，目标是做微信红包封面，平台规范还是需要掌握的。尤其是视频的尺寸，码率，时长。  

**
视频封面视频格式：MP4；视频宽高比建议3:4；分辨率低于4k；时长1s至3s；文件不超过20MB；帧率30fps以内；码率不高于3000kbit/s；视频编码H.264/AVC；yuv格式420。
**

还有就是活用官方提供的模板。下为figma版。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5D7sbQjuJm8yHte3N7qjyWojlviaeH0jjBfzlOvdBUGGQbNsLicy1skoiaY0fqlH7ZPs5ic53uDhjzsQ/640?wx_fmt=png&from=appmsg)

** Tips:  **

  1. 动动脑子加上封面挂件和气泡挂件会让你的红包生动不少。 
  2. 视频  在封面  上传处会  提供3s裁切，以及尺寸的裁切的，注意  制作的时候  考虑  尺寸和时长。 
  3. 但封面故事的视频可以15s，尺寸也可以更长。（这是为啥我要扩图获得更多内容的原因），还可以添加音频。  注意码率也更低  。 
  4. 注意有些文案，以及logo会被要求提供证明材料，建议巧妙的隐藏成为图形元素。 

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5D7sbQjuJm8yHte3N7qjyWbu6BiaHQ5p8neqFMgJdkMPcwba1hQ2Wl1gNsejP9iaUeW0cXKInVSNaw/640?wx_fmt=png&from=appmsg)

最后，就是等待审核通过了，就去购买红包，并兑换发放了。  

你学会了吗？

  

** **** ** ** ** ** ******** ** ** **▍ ** **** **** **红包领取** ** ** ** ** ** **
** ** ** ** ** ** ** ** ** ** ** ** **

  

这大概是这个红包封面的最后一波领取了，1500个，应该也不会再购买补充了。  不  过，  应该可能或许还会有别的更好看的样式  在设计  的路上。

  

回见！~

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

