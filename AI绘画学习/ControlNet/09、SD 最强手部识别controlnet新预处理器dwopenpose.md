![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tyssYUEyRwwGRJiau6YhN9aWbwxDYFVibb5qictUdmHfVqA0RJ2RxzokkCGRKworCLFsRNwciaQ8rOMqI9pG0j602A/0?wx_fmt=jpeg)

#  【Stable Diffusion】最强手部识别，controlnet新预处理器dw openpose

原创  吴溪源  [ 白马与少年 ](javascript:void\(0\);)

**白马与少年**

微信号  StreamWXY

功能介绍  Stable Diffusion、Blender等学习心得分享

__ __

__ _ _

在我们的controlnet中，手部识别一直使用的是openpose预处理器，但是有些情况下，复杂的手势是无法识别的。

比如，川建国同志的这张图。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwwGRJiau6YhN9aWbwxDYFVibb0amL01QexVZyATicNbdJzgdibwGZ3fYRu1iaDvlnkLWQPovicczVdB7MyQ/640?wx_fmt=png)

我们使用openpose-hand预处理器，检测出来的却没有手部。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwwGRJiau6YhN9aWbwxDYFVibbKumocUohQn5Oicic7lbaibsGpMNv0BJiaAYc63JhgqdAw9ybFicodIDLfYw/640?wx_fmt=png)

今天给大家推荐一款controlnet最新的预处理器，它能完美解决AI对于手部的识别问题，它就是——dw openpose

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwwGRJiau6YhN9aWbwxDYFVibbI2YrDaH0zuJoGgN1FsJ0OOtY3KsIjrDeAdc3ZT8Q8t0GZRib80A4w2w/640?wx_fmt=png)

大家从我的云盘中下载这个文件，将它放入到SD的这个目录下：extensions\sd-webui-
controlnet\annotator\downloads\openpose

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwwGRJiau6YhN9aWbwxDYFVibbyWNnUy9uyCtktCxV3RUg5XHXXwpdRzR7Tw1yDQNyUAfMibjbIMu3LGg/640?wx_fmt=png)

我们刷新一下，就可以看到这个预处理器了，中文叫二阶蒸馏-全身姿态估计。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwwGRJiau6YhN9aWbwxDYFVibbFMrCEJz6BIoyicIeAFQ0jhclb6LqMw3TK1ntVLNM7iawSJE7E70nwTzw/640?wx_fmt=png)

可以看到手部被完美的识别了出来。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwwGRJiau6YhN9aWbwxDYFVibbXjWXncuqH8Lic1vKF6kho5icXVBxVEib7Frr7VGbaK0Pbt13c8c6EWDcA/640?wx_fmt=png)

我们再试试，使用战狼的经典形象，原先的预处理器无法识别。好像这种带透视的，手臂不完整的，都比较难以识别。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwwGRJiau6YhN9aWbwxDYFVibbbA2zVBIn5UAaoIICT9hCeaiaqF1J3zWVCoia6m5puGSGE8tR1DHRufQA/640?wx_fmt=png)

换上我们的  dw openpose，完美识别。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwwGRJiau6YhN9aWbwxDYFVibb0s9YnicaYiakv6DezVnGpOyo9U1JlF6S2TXOQK87T4znaqmnlQiav9SlA/640?wx_fmt=png)

出一张图试试看，可以看出，图中基本上复现了战狼这个手部的动作，但是感觉又挺奇怪的。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwwGRJiau6YhN9aWbwxDYFVibbD47zqWO8pjVkMKVtSwIDlveicnUXkS1XSFBGcn5P5mbYKGzWEm9P9LQ/640?wx_fmt=png)
需要说明一下的是，目前这个DW
Pose只是更精确的openpose预处理器，并没有对ControlNet的openpose模型做任何改动，所以只能说AI的理解能力更强了，但是动手能力还有待提高。控制力度更强的ControlNet
openpose模型需要我们等待后续的更新了。

接下来，我们找一张难度没有那么大的图片试一试吧。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwwGRJiau6YhN9aWbwxDYFVibbC7Uia0urRrsJSfUk1IMu8vuxsrKMKRcDmxQVG0g9NAyvuwe7yQx4Rhg/640?wx_fmt=png)

我们使用之前的预处理发现，这种手臂不完整的图片还是没办法很好地识别出手部的。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwwGRJiau6YhN9aWbwxDYFVibbLooKhEN3cqbTiaQudd06yBWy8ur2QdYuOKfFrBavmJI0ibd7f0tpEcGg/640?wx_fmt=png)

接下来，运用我们的dw-pose预处理，一键搞定！  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwwGRJiau6YhN9aWbwxDYFVibbK5rvGk1uDPQhdyIjVVN61vBquT3cEafqwXrfozygtfJdBzkFzTA4ng/640?wx_fmt=png)

接下来，我们进入openpose的编辑面板，对不相符的骨骼进行调整。不知道这个插件的，大家可以看我的这篇文章—— [ 【Stable
Diffusion】Openpose再添新活，ControlNet里面直接编辑骨架图！
](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487238&idx=1&sn=5811609c88ef76639c85709a96671ab3&chksm=9fbecff2a8c946e4355c09751c4ac021dc72f8a53d3bc9be643861daf220474d847eaf1e3213&scene=21#wechat_redirect)
[
](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247486812&idx=1&sn=cbfff40072e25d54605f686c7733b8c0&chksm=9fbecda8a8c944be887648e28695df76810d7bf15a83588aa85ede35232c105c5d727c272ca6&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwwGRJiau6YhN9aWbwxDYFVibbrs73E0Q3Dk3kYfWvpxXZGcRPzKI3k6mtcRjaWtn9XYmf9eNsQ4QsdA/640?wx_fmt=png)

调整好之后，我们将骨骼图发送回controlnet。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwwGRJiau6YhN9aWbwxDYFVibb2icHuoHQwOkT1icTy8MWjFShLRsDcTWqu9VxSkgqicLwH1T2lb0fe9Z0w/640?wx_fmt=png)

接下来，设置模型和提示词。  大模型：ghostmix_v20Bakedvae  正向提示词：1girl,solo,long hair,looking at
viewer,jewelry,earrings,indoors,bangs,dress,blush,plant,multicolored
hair,upper body,shelf,pink eyes,window,potted plant,flower,closed mouth,from
side,wavy hair,bare shoulders,sleeveless,pink hair,kitchen,breasts,blue
dress,white hair, <lora:Colorful portraits_20230715165729-000018:1>  
负向提示词：EasyNegative, badhandsv5-neg,Subtitles,word

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwwGRJiau6YhN9aWbwxDYFVibbjNyMRZ0T2Y0cVOJ3ouoCPIibyq5McXqDPk5icNakP3nGuWR6UtzExFXQ/640?wx_fmt=png)

一口气生成了八张图，选择一张合适的，然后使用差异随机种子进行一个细节微调。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwwGRJiau6YhN9aWbwxDYFVibbnMSsFHRJojKezIGgzKTVBL7nduBAkakC6hN99pOpEPCHUbX7k6d75g/640?wx_fmt=png)

选择一张满意的发送到图生图。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwwGRJiau6YhN9aWbwxDYFVibbjQ5JpdFHw5Hzu4WnG7syicsVToyaJpCGwuSYRVwDf1vCEKBCfiblxkEQ/640?wx_fmt=png)

使用tile和脚本放大。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwwGRJiau6YhN9aWbwxDYFVibbaausAiaP2C3kMkyFKbopl53qMwUpWLMx4mk6Eof6SmnHgy4eMTAicN4Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwwGRJiau6YhN9aWbwxDYFVibbtbBOXSPITFOL4AUYdbPfM4r0iaWEC2KFGnbJYIcAFuFLOwRnbUsKJcQ/640?wx_fmt=png)

好了，我们的图片就生成完毕了。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwwGRJiau6YhN9aWbwxDYFVibb6QiaMyPuYPFBxBKpx6ImiaUmEZcCXyOkSlEXRP5nsuymnKQHgHVcIOcA/640?wx_fmt=png)

以上，就是关于  controlnet新预处理器dw openpose  的讲解，它可以识别出以往我们无法预览的骨骼图。想要的话，  可以添加我的公众号【
**白马与少年** 】，回复【SD】即可。  ** -END-  ** **  
**  
  

* * *

往期精选>>  

  * [ 【PS】无需魔法！Photoshop beta 25.0一键安装， 中文提示词+神经网络滤镜  ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487520&idx=1&sn=7be16204847c820313d9909eee490508&chksm=9fbed0d4a8c959c2cf440e90b584aef5b55f8bec25071fe6980002ee090bfdad39cd91261b4d&scene=21#wechat_redirect)
  * [ 告别提示词颜色污染！Cutoff插件  ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487640&idx=1&sn=250144a861cb4ac36f93be6408c85fb8&chksm=9fbed06ca8c9597a48f177fd8af9a5e10fd9e78f176613b05eac7d3ca8c68e01dceee947e159&scene=21#wechat_redirect)   

  * [ 超大尺寸绘制、分区控制，详解Tiled Diffusion & VAE插件功能  ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487605&idx=1&sn=e484f52f33a815fdcb12049742d46692&chksm=9fbed081a8c959977fac918147429f0f625eb1c2547fdf128196f97ac35c999b807ad9ddb083&scene=21#wechat_redirect)   

  * [ AI造字，把你的名字写在季节里  ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487476&idx=1&sn=074940028b8a295b22806ffad9181386&chksm=9fbecf00a8c94616f43d0b60fd06fbd201617f27725c4d7514c34fafe66f57dc40224ecb93b6&scene=21#wechat_redirect)
  * [ 隐藏在光里的秘密，AI造字光与影的艺术~ ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487455&idx=1&sn=362d5a02e23dfe19e1f3f0749ee1224c&chksm=9fbecf2ba8c9463df50a45ae0b25e35c510b01a166608205f78956a14a24cc571c66f6503a30&scene=21#wechat_redirect)
  * [ 来点夏天的感觉，AI造字浪里个浪~ ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487439&idx=1&sn=4ffba393c0ba29e78cd5a87c03895440&chksm=9fbecf3ba8c9462d04569f9f469268be00d01a92806115b51c4244af4cbc1c5151b238f5c659&scene=21#wechat_redirect)
  * [ 隐藏定位点！融合度更高的二维码生成 ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487390&idx=1&sn=fe28a857f50661807e449f1c04400096&chksm=9fbecf6aa8c9467cdfde4c9b37eff054f279ff230524399b11702a4442db514bcb27009d24e7&scene=21#wechat_redirect)
  * [ 图片高清化+面部修复+一键抠图，一些你不知道的事儿 ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487327&idx=1&sn=aad22a60028778b97bf00262f3a67883&chksm=9fbecfaba8c946bd29853ea9c15d90c03e2ac09ee4d22c27956bbcbcab3fa6c4551b5f599d03&scene=21#wechat_redirect)   

  * [ 无需Lora，一键换脸插件Roop ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487143&idx=1&sn=f564fb2e97142443fd706a15a3801ce3&chksm=9fbece53a8c9474550a6bdc7b15a8bd1961c0a5f48b8c736a18cbd1fb5906e5008b544383af4&scene=21#wechat_redirect)

  * [ 超清无损放大器StableSR ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247486854&idx=1&sn=e52870038dafc7518219660c90b1718b&chksm=9fbecd72a8c944647bb21f5e4546589295e5696a1f62601931080ccd4d29a1ec1230f73feb64&scene=21#wechat_redirect)

  * [ 如何画出商用级别的高清大图 ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247486230&idx=1&sn=dde16ebbd5078661c21835c94db554dc&chksm=9fbecbe2a8c942f48cfe40eaea15ff963db9b4fe1c9a8aed330ee718bcf6720e491fc9237a7e&scene=21#wechat_redirect)

预览时标签不可点

微信扫一扫  
关注该公众号



轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicFrWhQnGuwdp4icKgCxibWO94LTgVCdyGEa5tticq3VQ0wbSfnGkl6ficicgn1LmHvKohOIT76T3un55Q/0?wx_fmt=png)

白马与少年







****



****



  收藏

