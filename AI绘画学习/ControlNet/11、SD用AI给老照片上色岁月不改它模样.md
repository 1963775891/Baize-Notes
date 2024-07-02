![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rR335dShxibicImXIszOSsKGeGJreYlCvlic3iaqVE4smcd48HYnxUnB90xrlmVTrPFCUcaleUeXzFFQOjmiak9v9ZQ/0?wx_fmt=jpeg)

#  【Stable Diffusion】用AI给老照片上色，岁月不改它模样

原创  吴溪源  [ 白马与少年 ](javascript:void\(0\);)

**白马与少年**

微信号  StreamWXY

功能介绍  Stable Diffusion、Blender等学习心得分享

__ __

__ _ _

在最近新上线的controlnet模型中，除了我们之前测试过的一众适配sdxl的模型以外，还增加了一款名为  **Recolor**
的新模型，它的作用是可以将黑白的图片进行重新上色。  
看到这个功能，我首先想到的就是可以用它来修复那些已经年代久远的老照片。毕竟在以前那个年代，没有现在这种可以永远保存的数码拍照技术，很多洗出来的照片也都随着岁月的流逝而褪去了色彩。如果能用AI技术恢复这些往日的时光，也许能唤醒我们心底的一些温暖。

于是，我联系爸妈帮我找来了一些他们珍存的照片。他们也很热心于这件事情，立马给我发来了一大堆照片，其中有很多我也没见过的他们年轻的时候的样子，还包括我爷爷奶奶外公外婆那一辈的回忆。虽然很多照片都是黑白的，但是仍然能感受到那个时候的阳光和清风。

这是我的奶奶，她离开已经有十几年了，年轻时候留下的照片不多，这一张算是保存得很好的了，那个年代的人物照片总能让人感受到一种独特的气质。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicImXIszOSsKGeGJreYlCvlib1GA81LhfIicibialmVToHOCicicvrSSP9mQgVGKTfBcJrlLV6hUdp7iaXMA/640?wx_fmt=png)

既然是人物照片的还原，我这里就选择了realisian的写实大模型。提示词直接描述颜色和对应的内容。比如黑色的头发、黄色的皮肤、深蓝色的衣服、浅蓝色的背景。因为黑白照片，颜色无从判断，所以有些只能靠猜测了。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicImXIszOSsKGeGJreYlCvlNdiamehOTTqvks7at7Cibkc3bjglpteXGSXM2HNIXrtgmp4lNeHickbtA/640?wx_fmt=png)

ControlNet这里选择Recolor，预处理器有两个，经过我的测试，选择“recolor_luminance”的效果会更好一些。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicImXIszOSsKGeGJreYlCvld2Hr7yy4qgpfMOg6gESMHRibiadDbe6oNzjNtGzVwh9dImORmIfFqgsg/640?wx_fmt=png)

但是仅仅这样是不够的，从渲染的结果上我发现，颜色并不是精准地出现在我们想要的位置上的，提示词之间会出现相互的污染。而且由于照片上斑驳的痕迹，即使是背景也不能够做到完全统一，看来事情并没有我想象的那么简单。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicImXIszOSsKGeGJreYlCvloKldvxJYQSG5iaUfP8AgMicXW9AvIMvDFCHicwEH8xs2eHhQr85ad1gicA/640?wx_fmt=png)

为了做到颜色与内容的统一，我启用了之前讲到过的一款cutoff插件来进行控制，依次按顺序设置好颜色提示词，不了解这款插件的朋友可以参照我这篇文章—— [
【Stable Diffusion】告别提示词颜色污染！Cutoff插件
](http://mp.weixin.qq.com/s?__biz=MzkzMzIwMDgxMQ==&mid=2247487436&idx=1&sn=dba5cf7a170223deda6a706fa2e14f6b&chksm=c2515908f526d01eae402083a7f93e4c5c7dca057693a25847bb8e97929c875617777cbb9721&scene=21#wechat_redirect)
。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicImXIszOSsKGeGJreYlCvlxcKTts7zgoTFA91bh3pOiboGiadPIIxKwNmg9cSp16iazbkpWJVawj0Bw/640?wx_fmt=png)

终于得到了一张配色正确的照片，但是还没有完，由于以前的照片像素比较低，接下来我准备将它变得更高清一点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicImXIszOSsKGeGJreYlCvlKk5PgePDwZmtZO3loibfvVnSEtJzye3MQIGCGSqjJ0UvP02jadiaoPGg/640?wx_fmt=png)

将照片放入到后期处理中，使用GFPGAN算法将人脸变清晰，不知道这个功能的可以参考我这篇文章—— [ 【Stable
Diffusion】图片高清化+面部修复+一键抠图，一些你不知道的事儿
](http://mp.weixin.qq.com/s?__biz=MzkzMzIwMDgxMQ==&mid=2247487422&idx=1&sn=9cdf7ef37c2acb3c0fc3328d0ba8af74&chksm=c251597af526d06c921ea6728cb2a32bdf1d5f699e19d6ba13b849994e4d01af8a5144132aad&scene=21#wechat_redirect)
。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicImXIszOSsKGeGJreYlCvlhpTZ47VQ5h5g0LK12MLyskqHcRQ7bChVDksf29Us8J6k65GFqNc5GA/640?wx_fmt=png)

这个步骤，可以将我们的五官进行重绘，但是却没有办法将照片中的头发、衣服等其他元素变清晰。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicImXIszOSsKGeGJreYlCvlghvD5fIZofbic2UwabPk5LSGtPIka9WIayRgecy5eLRPRjKicCtdiaPJw/640?wx_fmt=png)

所以，接下来我将图片再发送到图生图当中，打开stableSR脚本，放大两倍。这个放大插件是所有插件中对原图还原最精准的，也是重绘效果最好的，不知道的朋友可以参考我的这篇文章——
[ 【Stable Diffusion】超清无损放大器StableSR
](http://mp.weixin.qq.com/s?__biz=MzkzMzIwMDgxMQ==&mid=2247487403&idx=1&sn=cbb96534fa6f58c37cf9fc64bc7ade0c&chksm=c251596ff526d0792b4bba0e21b69427b23e780824bdc75b22f1073e8bad6f61f30199fc8344&scene=21#wechat_redirect)
。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicImXIszOSsKGeGJreYlCvlBTFwUpzMibUDHTZah3ydkBzGaicpRBz0B3V3fkUTnZMGaDraXvbr4iceQ/640?wx_fmt=png)

切换到sd2.1的模型进行修复，vae选择vqgan，提示词可以什么都不写，以免对原图产生干扰。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicImXIszOSsKGeGJreYlCvlegxsT7qSuxFc45UlgcQzZV29mGM5QE9xPplYpL8cl87RibNksd7kkpA/640?wx_fmt=png)

启用MutiDiffusion插件，不开放大倍数，仅使用分块渲染的功能，能帮助我们在显存不够的情况下，将图片放大到足够的倍数。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicImXIszOSsKGeGJreYlCvlnmw5P7ESopGNYkMVNNia05SibXpgUsrKaF7r25SeRRWFTtvibbyibckRCg/640?wx_fmt=png)

好了，经过一顿操作，我们就将这张图片处理完成了。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicImXIszOSsKGeGJreYlCvlB0YmibNtylSCPnlogzicn0x9vVnhoHoQia2gw0iaHnlHT6iblNFQTicGU9UQ/640?wx_fmt=png)

对比一下看看，之前的黑白照片和经过上色高清化完成之后效果。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicImXIszOSsKGeGJreYlCvlibIDVSwVpvhVnricmKYibCNWfMUQ2RLpwsbnqcgXO1ynYFAuqGu57HltQ/640?wx_fmt=png)

同样的步骤，又还原了一张我妈妈的照片。在问到她当时穿的什么颜色衣服的时候，她记得可清楚了，想都没想就告诉我说是绿色的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicImXIszOSsKGeGJreYlCvlItRN5eeVPyFfC8Cf4zx7WiaUgVkiafwFsZgTKHywYK5NYAf6f00I7U8w/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicImXIszOSsKGeGJreYlCvlvkYLGejALGWLx4IBrP4wFSOeH53NrFwqFPqa7CIgeNMkicWKzZ0d8cQ/640?wx_fmt=png)

这两张还算容易的，接下来就遇到比较棘手的照片了。  
比如这一张，是我外公外婆带着我妈和我舅舅。外公走得更早，我甚至都没见过一面，只有这些照片还记录着他存在的痕迹。而
这张照片也有些年头了，一直被外婆好好保存着。人物多、场景复杂，像素非常的低，使得这张照片处理起来难度很大。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicImXIszOSsKGeGJreYlCvl5UnyFt4icxAPcJDGgcxMiaDzomV0EdLJbds0kTzLHd8TTfRIlMCVRQbg/640?wx_fmt=png)

我首先在ps里面进行了一下角度的调整和照片的裁切，然后使用刚才的步骤进行上色，但是直接上色的结果有点像是加了一层黄色滤镜，有颜色但是年代感还是太强了。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicImXIszOSsKGeGJreYlCvledySxl2v2LD0cR2QgDic8pwANuOCYQibZrg8ZTkHgDXBoyBaBbsKiaiakw/640?wx_fmt=png)

而太具体的颜色指定，又容易让画面污染严重，因为内容实在太多了，光是指定衣服就得十来个颜色提示词，AI能分辨得清才怪。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicImXIszOSsKGeGJreYlCvljbmuFFhO5xpaCXGH6ib4rIFDUbA0hRQIP7j42xibc6jqJMibT7c0GZlGQ/640?wx_fmt=png)

所以我决定放弃人物服装的颜色指定，只给一个场景方向，剩下的交给AI去自行决定。于是，我从网上找到了一张仙人洞的照片，让AI去帮我匹配色调。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicImXIszOSsKGeGJreYlCvlygb0iaGB50AUL76VPs6RNGA1wcGCIPsktNxjKjZ7GsdECmeSW99YgYQ/640?wx_fmt=png)

加入第二个controlnet来控制颜色，使用的是t2ia_color的模型。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicImXIszOSsKGeGJreYlCvls7GY17jsic0caFKkJ9zQ4Ws7QCeIbundTLx3190uSH3NIvyIvhDRBHQ/640?wx_fmt=png)

关键词只给了：蓝天、绿树、灰石砖这么简单的几个词。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicImXIszOSsKGeGJreYlCvlbeFYDfvaPmv090HgOercZjkf6ttG6kUYUNIxryLz0GzE2ciclzYtIyw/640?wx_fmt=png)

颜色终于正常了，最后经过脸部的修复和放大，得到了最终的效果。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicImXIszOSsKGeGJreYlCvlTj7V3BkA3Oyjexovm3KwEGnOo7DiaueRpUcd5VUOo2494KqJBAKA9Ug/640?wx_fmt=png)

对比一下前后的效果，那个流逝的时光仿佛又回来了，外婆看到后也非常高兴，在微信上连连夸赞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicImXIszOSsKGeGJreYlCvlZiazYfEuGEZzzfPKxTjqXZLPOqsUBibOI9dKV6tibWUXFBzbS1p6icrRlw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicImXIszOSsKGeGJreYlCvlXxVDPoVpD9RmccRHJKVAQ3kaAJKuMZyegHaqn0aPLmnrhHCdlFUocQ/640?wx_fmt=png)

同样难度的还有这张照片，是外婆带着我妈和舅舅拍的合影，应该是在影棚里拍的，背景是张画。这张照片的难点主要还是内容太多了，无法一一指定颜色，所以我只能逐个上色，再用ps进行融合。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicImXIszOSsKGeGJreYlCvl1GNd3HlpTSJxficiceC1YJppydy91YQNV68EpnLqRJ89co84v5ntqjtg/640?wx_fmt=png)

过程太繁琐我就不写了，直接上图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicImXIszOSsKGeGJreYlCvlG393lmh6MmlLa8iaS21LDSh4KEuw7TXxoApzbDYNne3qPvzXRIzTibwQ/640?wx_fmt=png)

看着这些老照片一张一张的翻新，思绪也会沉浸在某段时光里。也许不曾去过，但又总觉得似曾相识；也许相隔遥远，但又觉得触手可及。

_ 小镇的深处一条长长的街巷  _

_ 高高的红砖房，旧旧的玻璃窗  _

_ 蜿蜒的藤蔓带着淡淡泥土香  _

_ 缠绕这慢慢的时光  _

_ 日落前，挥挥手  _

_ 说他没有等太久  _

_ 夜如水，月如钩  _

_ 总有人等在回家的路口  _

_ 熟悉的地方  _

_ 依然安详  _

_ 岁月不改它模样  _

_ 风吹过树梢，沙沙地响  _

_ 把故事慢慢讲  _

  
** -END-  **

* * *

  

我的最新课程《Stable Diffusion零基础入门宝典》已经上架CCtalk，正在预售中， ** 前100名报名立减100  ** ，想了解的朋友
长按下方图片识别二维码，可以进入购买链接>>>

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rR335dShxibicWmbe9oYaryEicR9BouhhB701eVnt7WG0l9SzmNLOBxyicqGS4XNzUh7qbdKZZq1stDrOv1bAJYPRg/640?wx_fmt=jpeg)

  
  
**** 往期精彩内容回顾  ** **

  

  * [ 【课程】爆肝制作！Stable Diffusion零基础入门宝典  ](http://mp.weixin.qq.com/s?__biz=MzkzMzIwMDgxMQ==&mid=2247487870&idx=1&sn=7a425e50ccdfdc040b7fa285aad369c7&chksm=c25147baf526ceaca4de604a50d8b59d09920c7e4fe94223c3daa06ec337d18fc7ffb8e97e83&scene=21#wechat_redirect)

  * [ 【ComfyUI】Blender+Stable Diffusion！少年啊，这盛世如你所愿！（附中文汉化插件）  ](http://mp.weixin.qq.com/s?__biz=MzkzMzIwMDgxMQ==&mid=2247487928&idx=1&sn=90bb8f134e4c5e0a634d8acccf6f473c&chksm=c251477cf526ce6adfa92eadbcadc75d1f276a90fb56a8bc65b6bf72295973a9d9afdfeb4549&scene=21#wechat_redirect)

  * [ 【ComfyUI】本地部署ComfyUI上手指南，我就喜欢连连看  ](http://mp.weixin.qq.com/s?__biz=MzkzMzIwMDgxMQ==&mid=2247487895&idx=1&sn=aa21eede16dfe4bde7e0e93e353f7357&chksm=c2514753f526ce451175f654a93f48b526fc6de3e3b1564b218db41f7e3f99df5a84bb887043&scene=21#wechat_redirect)   

  * [ 向未来而生，关于SDXL你要知道事儿  ](http://mp.weixin.qq.com/s?__biz=MzkzMzIwMDgxMQ==&mid=2247487710&idx=1&sn=7f2b024f8377aff1c1b1822d155555f5&chksm=c251461af526cf0c74568effaefc6b285384ebadcb87e655fbfb41cb2ccad52e5d5f9193a687&scene=21#wechat_redirect)   

  * [ 想磕的CP随便磕，多角色Lora同时出现的方法  ](http://mp.weixin.qq.com/s?__biz=MzkzMzIwMDgxMQ==&mid=2247487442&idx=1&sn=9716b6af338e4ab7c944d5a37ec3e4da&chksm=c2515916f526d000fe74344b48afcddbd757788f76588f12b69db3f6f4643fd8aa29e68474ff&scene=21#wechat_redirect)

  * [ Roop换脸插件，全网最简单傻瓜式安装教程  ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487776&idx=1&sn=836fdeb74a045f86a81c47056ef7adec&chksm=9fbed1d4a8c958c2565166dce7a521871c9a5ebfa141132a0eb3f53a65816bbc3c16b1a4e368&scene=21#wechat_redirect)   

  * [ 【Lora炼丹术】从零开始，炼制你的第一个LoRA（1）  ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487751&idx=1&sn=dbc26500f9bda94fc09e1208864bb320&chksm=9fbed1f3a8c958e5b3853430fe79f9099d6962a4fd480fd6fff9f7fae3cd0ef933adf8637ac6&scene=21#wechat_redirect)   

  * [ 【PS】无需魔法！Photoshop beta 25.0一键安装， 中文提示词+神经网络滤镜  ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487520&idx=1&sn=7be16204847c820313d9909eee490508&chksm=9fbed0d4a8c959c2cf440e90b584aef5b55f8bec25071fe6980002ee090bfdad39cd91261b4d&scene=21#wechat_redirect)   

  * [ 最强手部识别，controlnet新预处理器dw openpose  ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487676&idx=1&sn=43988fe6f8e6172707d62feb70412540&chksm=9fbed048a8c9595e745ed69acb2b699b802ac93f6e64c3270f6f1523eb214ed3edc156a891cf&scene=21#wechat_redirect)   

  * [ 超大尺寸绘制、分区控制，详解Tiled Diffusion & VAE插件功能  ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487605&idx=1&sn=e484f52f33a815fdcb12049742d46692&chksm=9fbed081a8c959977fac918147429f0f625eb1c2547fdf128196f97ac35c999b807ad9ddb083&scene=21#wechat_redirect)   

  * [ AI造字，把你的名字写在季节里  ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487476&idx=1&sn=074940028b8a295b22806ffad9181386&chksm=9fbecf00a8c94616f43d0b60fd06fbd201617f27725c4d7514c34fafe66f57dc40224ecb93b6&scene=21#wechat_redirect)
  * [ 隐藏在光里的秘密，AI造字光与影的艺术~  ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487455&idx=1&sn=362d5a02e23dfe19e1f3f0749ee1224c&chksm=9fbecf2ba8c9463df50a45ae0b25e35c510b01a166608205f78956a14a24cc571c66f6503a30&scene=21#wechat_redirect)
  * [ 隐藏定位点！融合度更高的二维码生成  ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487390&idx=1&sn=fe28a857f50661807e449f1c04400096&chksm=9fbecf6aa8c9467cdfde4c9b37eff054f279ff230524399b11702a4442db514bcb27009d24e7&scene=21#wechat_redirect)
  * [ 图片高清化+面部修复+一键抠图，一些你不知道的事儿  ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487327&idx=1&sn=aad22a60028778b97bf00262f3a67883&chksm=9fbecfaba8c946bd29853ea9c15d90c03e2ac09ee4d22c27956bbcbcab3fa6c4551b5f599d03&scene=21#wechat_redirect)

  * [ 如何画出商用级别的高清大图  ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247486230&idx=1&sn=dde16ebbd5078661c21835c94db554dc&chksm=9fbecbe2a8c942f48cfe40eaea15ff963db9b4fe1c9a8aed330ee718bcf6720e491fc9237a7e&scene=21#wechat_redirect)

###

预览时标签不可点

微信扫一扫  
关注该公众号



轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicFrWhQnGuwdp4icKgCxibWO94LTgVCdyGEa5tticq3VQ0wbSfnGkl6ficicgn1LmHvKohOIT76T3un55Q/0?wx_fmt=png)

白马与少年







****



****



  收藏

