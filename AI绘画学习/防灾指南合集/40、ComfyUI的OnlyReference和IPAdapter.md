![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At49jSInH38NQthkcE8eFWicX6brGtgIq2nNkpia6b4XYItjebj8gjrUWQGu69386761WVwN5icuC6qbQ/0?wx_fmt=jpeg)

#  ComfyUI的Only Reference和IP-Adapter

原创  暴躁的卡爷  [ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

首先你得知道什么是IP-Adapter和Only Reference。如果不知道，那你一定要知道...
因为这是2个很夸张，使用率很高的功能，在webui中都是加持CN上王座的大杀器。

Only Reference  则  是CN在1  .1  的时候  加入的图片参  考功能，  那是卡爷拿来斗图必备的，这比传统的图生图要香多了，  比如
：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At49jSInH38NQthkcE8eFWicXh7picZqicXIss15ltQjocB3HdqfiaG1VBuetGIbjZVZBwaRurYz9MqSCg/640?wx_fmt=png)

而IP-Adapter我们之前也介绍过，先丢传送门，是一个能Image Prompt的强大CN模型+预处理器组合。

[ ControlNet又又升级了，IP-Adapter真香
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247485760&idx=1&sn=134ea1bc8e2a51d945be5571a5f54fe9&chksm=97a43f71a0d3b667425418bf06468b70b0dcddf000631f1d081cbc5dde4493f4122a9dad1381&scene=21#wechat_redirect)
>>  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At49jSInH38NQthkcE8eFWicXm1q9RUbw7rq0SqAECjhDs9T3iaaT6jc6ojBp3vibIRSz19q4mhVTKeKg/640?wx_fmt=png)

可是我们现在不是灭门换comfy了吗？为了怕comfyui误会，webui已经不熟了呀，这两个CN的左右护法还没怎么能不一起带过来呢！~

  

还是老样子，AB航线提供选择。

  1. ** 🤔A航线  ** 有webui的底子，想了解生图过程，能 **举一反三，进阶学习** 的。 

  2. ** 🤓B航线  ** 喂饭都不想吃，我只想 **无脑使用** ，出图效果好的。 

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5WWPHUPkYwQ2s3ThTehqVEjPBZD7RlzPPeMwI7icf8QRpveXQA1Zu5Uk2H8icGuVjVPwIusFrKvMZA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

  

** **▍ ** **** **** **Only Reference和IP-Adapter** ** ** ** ** （ ** ** ** ** **
A航线 ** **** 🤔）  ** ** ** ** **

这两个为啥要一起说，实际使用中，他们无论是操作还是流程都是相似的，只有结果上有一些区别，甚至包括图生图的大概区别是啥：

  * 图生图你可以理解为告诉AI，给咱来一个隔壁一样的菜。（重绘幅度和模型决定了有什么不一样。）   

  * Only Reference则是告诉AI，按照隔壁冒肥牛的风格给我们再冒个毛肚啥的。（模型风格决定了可以加些什么辅料） 
  * 而IP-A则是告诉AI，看这个图，你懂吧！~ 不懂我可以给你打点prompt。    

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At49jSInH38NQthkcE8eFWicX5QA73Ox9A57Qia7DrjxlNIucoBF1HjthGI8UibFHL3wNHJ4ibaVvbVpbw/640?wx_fmt=png)
浅显易懂了吧！~

** **** ** ** ** ** ******** ** ** Only Reference  ** ** ** ** ** ** ** ** **
** ** ** **

先来讲Only 参考，这是CN1.1加入的特色功能。对于很多时候我们并不希望垫图去模仿（chaoxi）而是真的只是参考就很舒服，趁手。

但因为CN的Only
Reference好像并没有开源，所以Comfy的作者自己写了一个相似的功能。我自己也使用了相同参数在webui和comfyui里试了一下。嗯，确实可以——以假乱真。  

使用也很容易。

右键新建——实验节点——简易仅参考（easy only reference）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At49jSInH38NQthkcE8eFWicXoVRp20WOib6qzkdNYkuzwUbLfxTDqLs3R4Q8LweJodzbBQAzOzImYuw/640?wx_fmt=png)

参考latent可以连接图片转编码进来，也可以从别的工作流潜空间直接过来。反正记住输入端是粉色的潜空间，不是蓝色的图片哟。  

模型连你正常的生图流进入和出去。  

latent输出进入采样器，所以这个参考的图片尺寸与导出是锁死的，注意。（可以修改，但肯定走的是裁切或者拉伸，这也侧面说明了只是参考在构图上是有局限性的）

完毕，就这么简单。

** **** ** ** ** ** ******** ** ** IP-Adapter  ** ** ** ** ** ** ** ** ** **
** ** **

IP-Adapter则比较麻烦，但ta的收益也是与麻烦成正比的。如果想完全脱离webui，还是建议在你的comfy小家里添置一下IP-Adapter。

** 1\. 安装插件  
**

首先需要安装插件，还是采用最简单的通过管理器安装，点击管理器——点第一个安装节点——搜索IPadapter（不要“-”），这两个都可以，plus安装完毕后会有一个单独的子菜单，我的右键已经有点拥挤了，所以我只安装了下面这个153的插件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At49jSInH38NQthkcE8eFWicXg9QnfkwOAG9IGPGTyTzfTOrQoRahjQKe3Er2XhauCD730AiaH1q1HIA/640?wx_fmt=png)
** **

** 2.下载模型  **

插件安装好后，还需要提供对应的模型  ，同上还是  采用最简单的  通过管理器安装  ，点击管理器  ——点第三个安装模型  ——  搜索
IPadapter（不要“  -”  ）  。  

这里有sd1.5和sdXL的两种模型，我建议都要。

这里备注一个B站up视频里提及下载模型的错误，他让下载的vit-h的模型是无法在IP-A的流里使用的。  

我们只需要下载111和112模型就可以了。但我建议1.5下载114 plus版会更好。就是稍微大了一点。记得开好网络环境，多等待一会。（切记）  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At49jSInH38NQthkcE8eFWicXiafCuzpmu6pkCriczTibFUicpM65M2Cf6MSiamvibynfrDgIW9RibXLhq7qMQ/640?wx_fmt=png)

还没完，再在搜索框中输入clip。因为我们还需要clip模型支持，这个之前webui也提及过。  

下载括号里有IP-A的2个模型就行。这两个模型很大，时间会有亿点点长。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At49jSInH38NQthkcE8eFWicX56XkcMOoy21vHB30IDIA7LRcyvKIDOV8A8ScDNsEfWia2UiaLTesdp9A/640?wx_fmt=png)

可以看看控制台，是否在下载中。现在完毕会出现在comfy-model-clip_vision的路径中。2个文件夹。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At49jSInH38NQthkcE8eFWicXibhRbNeibXdZRfrXu9Y9ibrYWAkhxPx9jiav3HhOX9Mrw0maic1KA3YibrEA/640?wx_fmt=png)

还要去插件目录下查看模型是否准备ok，记得把三个模型都收拾好放入：ComfyUI\custom_nodes\IPAdapter-ComfyUI\models  

然后重启comfy，右键加载器——IP适配加载器就是我们这一part的主角了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At49jSInH38NQthkcE8eFWicXw29HltvxAkZTneAia1etxLyuqoiaJ3CibNvxwticq9Diau0MDkjEY6ECficw/640?wx_fmt=png)

与Only Reference一样，CN加入常规生成的工作流，在model和clip中间。新建一个IP适配加载器。

模型接入模型加载器或者lora，接出K采样器。图像接入图像加载器就行。

至于遮罩和视觉输出空着不用管。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At49jSInH38NQthkcE8eFWicX1ZVNzuOZ2GsMUKlkAtqubxjq8gkuFpy6o4WEurFCgK44XEhfqyQu8w/640?wx_fmt=png)

加个帽子啥的细节跑一下。如果可以，你也可以加入之前提过的高清放大和面部修复。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At49jSInH38NQthkcE8eFWicXQN1Fo10o2jMs5LQ50yurKib1q6zLU3YcPLd61B6mabIzKJSBUQQyHnw/640?wx_fmt=png)

是不是很简单？  

  

** **** ** ** ** ** ******** ** ** **▍ ** **** **** **Only Reference和IP-
Adapter** ** ** ** ** （ ** ** ** ** ** B航线 ** **** 🤔）  ** ** ** ** ** ** ** **
** ** ** ** ** ** ** ** **

** **** ** ** ** ** ******** ** ** 导入工作流or图片  ** ** ** ** ** ** ** ** ** ** **
** **

我已经把工作量都拆解成接线盒，你可以选择单独接还是无脑直接用，就随意了！我把2个工作流合在一起，需要哪个连哪个。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At49jSInH38NQthkcE8eFWicXVCpTpeYCRekhHXeCT0XJn6Rgm0GSHv32CXRG4JYKLy7ZSbC0IicNCoA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At49jSInH38NQthkcE8eFWicXhEL5jIjzLJDESqLyZj6Q7znY0IyRoYmGdjbRSNXtrp0FfDBqcFbLibA/640?wx_fmt=png&from=appmsg)

高清放大一下，嗯，加了帽子，加了微笑，很好！~  

图片或者workflow的json文件，取走任意一种导入就能使用啦，B航线简直不要太简单！~

  

** 最后  **

如果对SD防灾对策群感兴趣的也可以关注公众号 **【小鱼干了】** ，通过公众号的自动回复 **加群** ， **加好友** ，获得
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

