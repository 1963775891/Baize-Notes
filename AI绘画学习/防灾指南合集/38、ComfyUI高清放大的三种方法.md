![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At6GxIZ1buriceLPN8AZWQLgcAH0WNia4H4kGNPFAcYREsfwibT2YjIPoYibd08xCbp6Pqic2NIH3PuXB5g/0?wx_fmt=jpeg)

#  ComfyUI-高清放大的三种方法※

原创  暴躁的卡爷  [ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

基础的文生图和图生图已经完毕，应该很多人都已经开始爱上这个SD工具的生图方式了。也有不少人迫不及待的自己去搜寻进阶玩法了。那今天就要讲一个重要部分了。（敲黑板，划重点了）  

** 高清放大  **

高清放大可以说是进行AI绘画的一个灵魂工序了。尤其是在过去sd1.5训练集还是512x512的时候，想要出一张1024甚至2k的图片一定少不了放大这一步。如果webui上的高清放大你还不了解，就先传送下面看看：  

[ 冥土追魂“马赛克”，SD高清（实战篇）
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484918&idx=1&sn=0c984e89cb2bfab5dfcd6ddffab1ffb0&chksm=97a433c7a0d3bad1eccbc3474820ee48b333bf6c02e9875020970fa0f5dc97d81a50a336e192&scene=21#wechat_redirect)
>>

XL？XL太无脑了，直接1024直出就行。如果是半路出家，也可以先从ComfyUI的第一篇开始了解，连上你的第一个生图节点。

[ ComfyUI，你开启XL钥匙打开了新世界
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247485938&idx=1&sn=4786693cccbcd59f84dbaf261258dc52&chksm=97a43fc3a0d3b6d54735e790318ee8b81f2361c7872dd9eeae17b5e92c1f1218ab9c6a7fb401&scene=21#wechat_redirect)
>>>

  

还是老样子，AB航线提供选择。

  1. ** 🤔A航线  ** 有webui的底子，想了解生图过程，能 **举一反三，进阶学习** 的。 

  2. ** 🤓B航线  ** 喂饭都不想吃，我只想 **无脑使用** ，出图效果好的。    

如果跟随  《  [ Stable Diffusion 防災指南
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484593&idx=1&sn=28186490d02d1f6376e10d549c8f480d&chksm=97a43280a0d3bb968a1988fb3ad41c30b3698dd9d9316a3b38bc32d41838f1988f4400de24ee&scene=21#wechat_redirect)
》  一路学习过来的朋友可以选择 **A航线**
继续跟随卡爷的节奏进入ComfyUI新世界，而对ComfyUI本身兴趣不大，但对比WebUI还简单无脑的生图很需要，直接跳过下面A部分，滑到后面的
**B航线** 就行，按需食用即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5WWPHUPkYwQ2s3ThTehqVEjPBZD7RlzPPeMwI7icf8QRpveXQA1Zu5Uk2H8icGuVjVPwIusFrKvMZA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

  

** **▍ ** **** **** **高清放大** ** ** ** ** （ ** ** ** ** ** A航线 ** **** 🤔）  **
** ** ** **

主要介绍3个主流的放大方式，还有一个使用ControlNet的Tile放大我们在介绍ComfyUI的CN使用的时候会再细说。这两个方法是：

  * 潜空间放大Latent Upscale（文生图）   

  * 图生图重绘放大 
  * 图生图USDU(Ultimate SD Upscale)放大（图生图）   

** **** ** ** ** ** ******** ** ** 潜空间放大  ** ** ** ** ** ** ** ** ** ** ** **
**

WebUI中我们有一个熟悉的文生图放大功能：Hires.fix，这个的原始原理就是潜空间放大，就在图片被VAE解码前再回到潜空间中使用算法再进行分块重新绘制，再生产而出。这个原理很重要，会直接影响我们后面几乎所有放大方式。

所以我们还是手动连接一遍。先把常规的生图连接好。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6GxIZ1buriceLPN8AZWQLgcncr9f36WeAlrT7wic9cLdwqPfjlv9MTJjgIkdEtxAzdEBYQPJdsm8zw/640?wx_fmt=png)

先注意潜空间Latent这个粉色节点，在上一期基础图生图中我们就简单介绍了一下它和蓝色图片的关系，我们可能模模糊糊的感觉到蓝色的图片经过VAE编码变成粉色从采样器的左边进，右边出，经过VAE解。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6GxIZ1buriceLPN8AZWQLgcib94ZH6xjwd0nawpIic6icWtx01jtF955A3BDzqLqicEdRBQsNXygicibJfQ/640?wx_fmt=png)

而潜空间则是在出结果前不需要经过VAE编解码，不经过蓝色节点。所以相对而言速度会稍微快一丢丢，但由于潜空间进度的尺寸原因，显存占用并没有更少，这个在webui放大的时候就已经介绍过。

我们可以使用ComfyUI提供的快捷方式，也可以自己连。右键K采样器。就能看到添加Hi-resFix。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6GxIZ1buriceLPN8AZWQLgcT6MTLic4Wzf0BFRicSicnHGN1Vngfh2iaLnJMFbhoBBs4GBLV6blYLDJKw/640?wx_fmt=png)

点击后，其实潜空间的高清放大就连接好了。这里提供的是固定尺寸的缩放，你也可以手动拖动采样器右边的latent输出粉点点，选择Latent按系数
缩放（这个更适合，毕竟直接填写倍数就够了，前面比例已经设置好了，也不需要再设置图片裁剪还是伸缩）  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6GxIZ1buriceLPN8AZWQLgcIJoN4GWicok0Ciard8Qt66AMsJqWKNstJocNlosD7xkVoVGf6hI0w76A/640?wx_fmt=png)

最后就从第二个K采样器进行图片输出即可。

注意VAE的连接，XL模型直连模型即可。老模型缺少VAE需要单独加载一个节点。 **还有就是注意降噪（重绘幅度）记得改小。1就和原图关联不大了** 。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6GxIZ1buriceLPN8AZWQLgcXt3pXSOj0V1ibx03mqeoqn61kE9WGuSW5QdJ8q4FJWavVlSvT5iapFdw/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** 图生图重绘放大  ** ** ** ** ** ** ** ** ** ** **
** **

其实大部分人在掌握潜空间hiresFix就足够用了。但因为过去使用webui几乎不用latent算法，习惯使用4xUltraSharp放大算法的人来说总觉得毛毛虫虫爬爬爬。于是我求遍了各个群，最终Fok大佬给我简单普及了一下潜空间放大的原理后，我终于明白了Hires.Fix的工作原理，以及为啥WebUI的Hires.fix还能选择放大模型。（但我还有一个疑问，这种放大感觉就是SD放大，与潜空间已经没关系了，这真的是webui的hires.fix原理吗？希望有人能留言解答一下）  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6GxIZ1buriceLPN8AZWQLgcN2Df8QE6TEibOXUdrs6dNHdibAuvNyu1fgS6YNJr0enBmRNYQGNsF8nA/640?wx_fmt=png)

本质就是上面说的进行了一次图生图重绘。这也是为什么第二期我要和大家介绍图生图和基本的放大原理。

我们只需要将VAE解码的图片连接一个通过模型放大的节点。这个节点在图片合集中。然后模型就可以选择我们之前熟悉的各种4x 8x了。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6GxIZ1buriceLPN8AZWQLgcfHH0CLErVVnOz785VvMQePThRvGueUD8EXRABUML09JNUsKHgyMdAQ/640?wx_fmt=png)

然后就是上一期讲的简单的缩放，比如按倍数放大后再进入K采样器进行重绘。

这里有一个不知道是不是错误的方式，至少肉眼看不到效果。是直接图片——图片放大模型——放大产出。这种放大类似webui的后期处理，效果不明显，但胜在速度快，所以用在采样重绘前效果显著得多。

注意： **按照倍率缩放，需要注意与你的放大模型一起是乘算的，也就是放大到2倍，你选的是4x放大模型，则需要把倍率设置成0.5** 。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6GxIZ1buriceLPN8AZWQLgcQIDyOoWOeDV6lB0zlp5QNxnOnQuf6G7srY1UtCFFdQAvWNZDCAp8SQ/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** SD放大（USDU)  ** ** ** ** ** ** ** ** ** **
** ** **

最后，我们介绍另一个图生图放大的放大，就是我们在WebUI里经常用到的，经过大量抽卡，拿到n张结构，美学都还不错的图，可以进行图生图的高清放大。
其实上面的放大方式在我的理解就是普通的SD放大，USDU会增加更多参数调整，包括tile的大小等。

只是用到USDU需要先安装对应插件，也比较好找。在Manager里安装节点里搜  Ultimate SD
Upscale，也可以在a1111替换中更容易的检索到。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6GxIZ1buriceLPN8AZWQLgcVphOQ3zyPsWqtsScZoYAz62SDoxqs0ib6ujTEpbEiaUicibcNxW4CQVs2Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6GxIZ1buriceLPN8AZWQLgcm6RzVl7JFicnBdp95EH30PyheFjggo8YeTbbp4xH4utQrR3eWCeR24g/640?wx_fmt=png)

安装好插件后，就能在图像-放大-USDU。有2个节点，分别是带放大模型和不带模型的选择。按需使用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6GxIZ1buriceLPN8AZWQLgcm7PHj408LKn4YvwicvNccRicVricyjUCe6KAia9JbkCf4VycnNv8D4mGsA/640?wx_fmt=png)

好了，这样，你就掌握了t2i，i2i的常用三种高清放大方法，并且在comfy的网络加持下，组合出更多的玩法了。  

** **** ** ** ** ** ******** ** ** **▍ ** **高清放大** （ ** ** ** ** ** B航线 **
**** 🤔）  ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

** **** ** ** ** ** ******** ** ** 导入工作流or图片  ** ** ** ** ** ** ** ** ** ** **
** **

上面提到的3个工作流和图片已经放入下载中，也可以进最近成立的ComfyUI学习交流群向群主索取。导入后只需要传图和填基本参数就能用， **超级简单** ！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6GxIZ1buriceLPN8AZWQLgcXt3pXSOj0V1ibx03mqeoqn61kE9WGuSW5QdJ8q4FJWavVlSvT5iapFdw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6GxIZ1buriceLPN8AZWQLgcQIDyOoWOeDV6lB0zlp5QNxnOnQuf6G7srY1UtCFFdQAvWNZDCAp8SQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6GxIZ1buriceLPN8AZWQLgcm7PHj408LKn4YvwicvNccRicVricyjUCe6KAia9JbkCf4VycnNv8D4mGsA/640?wx_fmt=png)

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6GxIZ1buriceLPN8AZWQLgc02zDIFNYShXzrVIHttR2jFtvia6EUj1ymvicDDFH3e3hFnLRzWhxIlHA/640?wx_fmt=png)

  

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6GxIZ1buriceLPN8AZWQLgck9MnLTvrLAiaIswicmgnxexJu6cUXiahXREfeKCO5ZoKLZa0mMO3xux3w/640?wx_fmt=png)

  

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6GxIZ1buriceLPN8AZWQLgc8mJfBEx4l6CKTibYiaY7osSxh4gTdwXqxWruEg1mFjzwCxkYNowicnosA/640?wx_fmt=png)

  

图片或者workflow的json文件，取走任意一种导入就能使用啦，B航线简直不要太简单！~

  

  

  

** 最后  **

如果对SD防灾对策群感兴趣的也可以关注公众号给 **【小鱼干了】** ，通过公众号的自动回复 **加群** ， **加好友** ，获得
**最新AI绘图信息** 等操作。  ****

本期文章提到的PNG信息图片和工作流，可以公众号回复【下载】获得资源。

  

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

