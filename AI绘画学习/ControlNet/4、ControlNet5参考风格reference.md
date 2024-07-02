![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tyssYUEyRwz5Tgf7ASQqica3Es7WbXUPv4VYurqMgAMCgWxhQJarO7sqYJ9OgBqOqiawbvSQQicPbzkBwG3C0uUGA/0?wx_fmt=jpeg)

#  【Stable Diffusion】最强控制插件ControlNet（5）参考风格reference

原创  吴溪源  [ 白马与少年 ](javascript:void\(0\);)

**白马与少年**

微信号  StreamWXY

功能介绍  Stable Diffusion、Blender等学习心得分享

__ __

__ _ _

因为AI生成人物往往是带有随机性的，每次生成都会有一些不可控的区别，所以一直以来，设计师们都想解决生成人物能保持统一这个问题。

自从ControlNet1.1.17的版本升级之后，作者更新了一个新的预处理器——  refer
ence。这个预处理器最大的作用，就是通过一张给定的参考图可以延续出一系列相似的图
，这样就为我们给同一个角色生成系列图提供了可能，接下来让我们一起来看看它是怎么使用的。

**# 使用方法** 首先我们进入文生图，填写一段提示词。如下：(杰作，最好的质量)，一头白发的女孩坐在绿植和鲜花的田野里，温暖的灯光，模糊的前景。
设置一下常规参数，先生成一张图。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwz5Tgf7ASQqica3Es7WbXUPvIfpLFKWTKJhzFEvusPic2ic43WiaYl8sNW3CSnLMCoeYib6UvibglNnubeQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwz5Tgf7ASQqica3Es7WbXUPvnujkNbial6QwGvx3BZDibcFENlnzu25ICyNATeds3Mu2jggrj8meJJxA/640?wx_fmt=png)

接下来，我们想用这个人物作为主角生成一系列其他的图。将图片拖入到  ControlNet中，预处理器选择  refer  ence
only，控制模型一定要选择“均衡”。保真度数值越高，对图片的参考就越强，我们先设置为1看看。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwz5Tgf7ASQqica3Es7WbXUPv4MDP5G4710TvtNlxJ1BsgB1bJPr67tiaBb7tmsYHQiamJIl1icGKLj1aQ/640?wx_fmt=png)

可以看到，在没有明确指向性提示词的情况下，人物形象保持了一致，但是她的表情、动作、服装产生了随机的不同程度的变化。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwz5Tgf7ASQqica3Es7WbXUPvNVHszNLXzrcauJNibN6eq3DAoEPeDWE4XZe0HLlsVCdW6R22MWSTJdA/640?wx_fmt=png)

我们可以试着通过添加关键词的方式来给人物换装，比如添加“红裙子”。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwz5Tgf7ASQqica3Es7WbXUPv2BmmXtyqabtia1XUc4JwPk9MxtKr3TOYvicza1F3CSnpWFJD5NHZ1W2w/640?wx_fmt=png)

同时更改服装和表情，比如添加“黑色校服、哭泣”。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwz5Tgf7ASQqica3Es7WbXUPv8tTj5FTvQ0YJnN3G7D89ic1ZuW0dcca2N8MQvE9ENB5W0Mo8SKsexUw/640?wx_fmt=png)

同时更改动作和表情，比如添加“抱手、生气”。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwz5Tgf7ASQqica3Es7WbXUPvl8Yr83iaBtsA1mtaEicgYa1ep9icwWbOibpVUlfAOiaX3rCS6OPNlibGxDiaQ/640?wx_fmt=png)

同时更改姿态，环境  和表情，比如添加“  在花丛中奔跑  、开心  ”。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzGGG1VtPVPTibKMOU1p8mSgUxiacSWfKj2A06HTZbmzkogbFkp15Qicu6uOCu7p6aQqfPPGGXStfgOA/640?wx_fmt=png)

添加“红色棒球帽，时尚卫衣，在商场逛街”。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwz5Tgf7ASQqica3Es7WbXUPvwIUo4gwtjgawoGa74ibTDvibcxb8rdk3IlTTF0RcHlGpQ11UpWK3UP4Q/640?wx_fmt=png)

通过一系列测试，可以发现这个功能可以让我们在绘制系列插画、漫画、小说插图等等工作时，能保持主角形象的统一，也能根据情况做实时的调整，如果后期再配合lora，潜力可以想象是非常大的。  

**# 其他应用**

我们还可以测试一些有趣的东西，比如拿一些完全不相干的图片来做参考，看看会发生什么。

还是使用刚才女孩坐在草地上的提示词不变，但是参考图片换成一筐草莓。  

****

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwz5Tgf7ASQqica3Es7WbXUPvxmrYkIIqdibUrrHQXJ61lHQPWovFYzKt5xWDg8Bnpicp1LWsvbygpvkQ/640?wx_fmt=png)

得到了和刚才那张图比较接近的色调，说明这个风格参考也可以作为一种滤镜功能使用。找到喜欢的图片色调，就能直接参考出来。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwz5Tgf7ASQqica3Es7WbXUPvtKfFcdZEBEtCU9faN1yABaOEhS8iaa9q9hmPOjX7YkibYr9jfUWQMU0w/640?wx_fmt=png)

如果使用蒙娜丽莎作为参考，会得到什么效果呢？  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwz5Tgf7ASQqica3Es7WbXUPvZ0eEUp8Opqljg2O6pUibVr9HEaXFfCeZ9hcFYSd7MYIf2Humt8mZa9Q/640?wx_fmt=png)

世界名画诞生了，而且似乎是连画风也进行了参考，甚至脸庞也有点像了，可能是我把参考值拉满了的原因。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwz5Tgf7ASQqica3Es7WbXUPvSCY0A0gg9fRAQUgwLa1fLpU2HcK4e6XkSOSsicuwDzHea4Kaxvwb0Iw/640?wx_fmt=png)

再尝试参考一下梵高的星空，很好奇这种特别强烈的绘画风格参考出来是什么样的。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwz5Tgf7ASQqica3Es7WbXUPva7icO1hlImOABo2iaChRvvcV27lqRbPmDx1mUBFnUic8eBlotRJam8cfw/640?wx_fmt=png)

当当，图像生成！  色调、笔触还挺有那个味道的，而且像素越低，感觉越像是什么回事。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwz5Tgf7ASQqica3Es7WbXUPvz0HOJxf0JC15Ctibx1PVB0GWzKHibfBHFE6wpVYONh5yvZCVnb7NGeXA/640?wx_fmt=png)

最后，我们再使用  refer  ence进行一下扩图。将上面这张图发送到图生图，调整尺寸，用较小的重绘幅度，得到下面这张图片。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwz5Tgf7ASQqica3Es7WbXUPvOp6iaykeKxj3G6ZKSQas0O6ibC90Ee77TFvzKxUjAFBrpYAwg36ZpHCw/640?wx_fmt=png)

进行局部重绘，将两边区域图上蒙版。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwz5Tgf7ASQqica3Es7WbXUPvHa496pibSDC4me0iaerUVffk1TO2tfqia1zavsUpzooB7MKBibo44Amsqg/640?wx_fmt=png)

正向提示词改为“长满鲜花和植物的田野”，来描述背景的内容。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwz5Tgf7ASQqica3Es7WbXUPvKeR0loC2y2ga8EHK8QlVicemMjO1iaj3FRoK90Lo0IfAPD16NYVDQEOw/640?wx_fmt=png)

ControlNet继续使用星空来控制参考风格。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwz5Tgf7ASQqica3Es7WbXUPvNZiaAHQdTGlVJNVHY1ibeWVaicB2puP8Cmia2qwiaY5PVZ4V6AMvBKoicPQg/640?wx_fmt=png)

这样背景就扩充好了，效果还是不错的。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwz5Tgf7ASQqica3Es7WbXUPvt8e2lzw3V7Jykt6ibjyRm1GLXyoFTZHLRFGOPMibgSJq0cF0OljYN5Eg/640?wx_fmt=png)

借用这个思路，我们还可以尝试通过多个  ControlNet通道的结合，来实现绘图的风格控制。  比如，我们接下来要给这张线稿上色。
![](https://mmbiz.qpic.cn/mmbiz_jpg/tyssYUEyRwzGGG1VtPVPTibKMOU1p8mSgAxLJzxpzDvtFOsJGbbwgGY35Qyo5A3roqz7LSaSibTZV2WnsuoDCzrA/640?wx_fmt=jpeg)

  

然后风格参考这张水彩的插画。

  

![](https://mmbiz.qpic.cn/mmbiz_jpg/tyssYUEyRwzGGG1VtPVPTibKMOU1p8mSgSCThl0LSo1zPPAEsIj67tur0D91c3TrNianPZyrpQA28EWBWbjU87JQ/640?wx_fmt=jpeg)  

两个通道分别如下设置：一个采用lineart_anime做预处理器；另一个用reference_only做参考风格。提示词为：一个女孩，头像，水彩。  

  
![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzGGG1VtPVPTibKMOU1p8mSg6xFXtrEgxiaLl4lRORF9qBeQU1ricFKT92KxEqh2Ip0vuFszrmY2QdQw/640?wx_fmt=png)  
![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzGGG1VtPVPTibKMOU1p8mSgvf2vfdY31XiaP1vLo6Tq3LWtUBiafvdMcDibOpGQ4WjJpxlYGDUwWqUiag/640?wx_fmt=png)  

点击生成，我们就通过参考风格绘制好了这张线稿上色。这张的模型使用的是有名的二次元  模型“AnythingV5V3_v5PrtRE”。

  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzGGG1VtPVPTibKMOU1p8mSg0NriblrPpJmibFYJdxZV0Kiapyscickrp70ialm1FHTM2tWAeSBNTAQBW0Q/640?wx_fmt=png)  

使用不同的模型和参数设置也会产生不用的效果，比如这张更换了大模型“colorBoxModel_colorBOX”，色彩更鲜明一些。

  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzGGG1VtPVPTibKMOU1p8mSgXk5ba9nw6xI4pd7s1qe5kCa9jCSGI0TKKqtxwWkzJDiaja9cgicJdsTQ/640?wx_fmt=png)  

这张还是使用的“AnythingV5V3_v5PrtRE”模型，并额外添加了“Moxin”Lora，水墨风格化更明显了。

  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzGGG1VtPVPTibKMOU1p8mSgpZHy6iba0IwxUlFSsFBELQ4SlIo3WgfL0m2S1kA0RghJTF44RlCqZYA/640?wx_fmt=png)
好了，以上就是ControlNet插件当中  refer  ence参考预处理器  的介绍，更多的用法大家可以自己去发掘，玩得开心。  
![](https://mmbiz.qpic.cn/mmbiz_png/7QRTvkK2qC5Q3Q2JPcAgQibyJut3L80CAK1LpzPEewG6jC5ZIx1A91KV1uibXnuSldvicmibw1Cykpul8XsKzanOag/640?wx_fmt=png)
END
![](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC7iacMXKXoMLGhrILmzV69icN12icicVxBjAwDzhoxvibibtC2Ya931h4INzthwBaJaiaxHoBib4G8NSCd0sw/640?wx_fmt=gif)
我是一个IP设计师
![](https://mmbiz.qpic.cn/mmbiz_jpg/tyssYUEyRwzZXZia7R6Qa6ceAbTPzMBaTDlDs76q5fX7zt4Bl9eSTysEvHubMRLD73M7d6GxY6rBOlu6fS6n2Eg/640?wx_fmt=jpeg)
长按二维码识别

喜欢的话，可以点  赞  支持一下哦~

预览时标签不可点

微信扫一扫  
关注该公众号



轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicFrWhQnGuwdp4icKgCxibWO94LTgVCdyGEa5tticq3VQ0wbSfnGkl6ficicgn1LmHvKohOIT76T3un55Q/0?wx_fmt=png)

白马与少年







****



****



  收藏

