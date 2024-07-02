![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tyssYUEyRwzibHMPpVIGwr2VGM18OBhEphOwLEwK5ytMsECvQPM3icTKENbqLMyqViaaSshicAYn6yN4PH2gGhKicXw/0?wx_fmt=jpeg)

#  【Stable Diffusion】最强控制插件ControlNet（2）姿态约束

原创  吴溪源  [ 白马与少年 ](javascript:void\(0\);)

**白马与少年**

微信号  StreamWXY

功能介绍  Stable Diffusion、Blender等学习心得分享

__ __

__ _ _

上一次，我们讲解了ControlNet里面关于线条约束类预处理器和模型的运用，今天我们来了解一下姿态约束类的模型。
**姿态约束类：它可以通过生成的骨架来规定绘图中人物的动作和表情。**

  * **openpose：可以直接解析出人物的动作骨架。**   

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibHMPpVIGwr2VGM18OBhEp06ne8s7vLR3skskzMCczHVibO4u1pyZbTicLg6vibvKzdLH6OIt90c75w/640?wx_fmt=png)

之前给大家演示过了一个模仿库里打球的女孩绘图，就是使用的  ControlNet的openpose预处理器。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibHMPpVIGwr2VGM18OBhEpIr1ibrxqSLJjR4KFd9lDPbb1gC36qJqzPe5LJPNVvdjlX2CST4CUxBQ/640?wx_fmt=png)

而最新的  ControlNet1.1版本，除了身体姿态以外还增加了更详细的脸部和手部的预处理器。
**![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxibuSoLUE4yOibOmMibQ6YOZOy2SrxtV4AXlQzGR21cFFtrBSTYiam9gSzwBq9PBey5f758iaKnpKBI6A/640?wx_fmt=png)
** 当然，这些所有的预处理器对应的模型都是openpose。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibHMPpVIGwr2VGM18OBhEpSL2L3RTmuPu3iaXEnvkfgBVCFibeFmj3hhJUyDjXXoV2t4F48FS1qePQ/640?wx_fmt=png)

  * ** ** **openpose_face：解析姿态和脸部**

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibHMPpVIGwr2VGM18OBhEpYDOZYEhKiaxickt8boDJib1IvTmiaZgtD7Jnn0icmDgHnzSurSDZc08Y4pg/640?wx_fmt=png)

使用的AbyssOrangeMix2模型做演示，风格不一样，但是还原了人物的表情和动作。  
****

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibHMPpVIGwr2VGM18OBhEpISy85sibsW0F2tYlibBkvAsAKRPn4iaRrHhKH2FR6xDibeXSOTM50Aib4ew/640?wx_fmt=png)

  * **openpose_faceonly：仅解析脸部**

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibHMPpVIGwr2VGM18OBhEpfUfO9L6Pft0q82S7unIOiaf6ItwvNOS4FJfvTlChxaJcoyokib5N1JIA/640?wx_fmt=png)

测试了一下，这个面部识别只对真人和2.5D的形象可以识别，卡通二次元角色不起作用。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibHMPpVIGwr2VGM18OBhEpYztzATVt1gkAWRicV2f5gACQ1ic42VTyI3ZpGacN8kVuYnEISbLTiaXRA/640?wx_fmt=png)

  

  * **openpose_hand：解析姿态和手部**

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibHMPpVIGwr2VGM18OBhEpBzDnQcNTmqW5OdfuXmVO3TxXszrPFsYcbmnxf1ESUE80tfQD1yqzqw/640?wx_fmt=png)

有了手部的骨架控制，可以一定程度上解决AI一直以来不会画手的问题，但是当手部骨架与身体骨架重合的时候，还是会产生一些问题，要通过多刷图来筛选。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibHMPpVIGwr2VGM18OBhEpFxwL0Hkbef73JGmoeOCib9zwnibrIGshIKiaJwCr9J5iaXxJQXaKlz2Hibw/640?wx_fmt=png)

  * **openpose_full：解析姿态、手部及脸部**

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibHMPpVIGwr2VGM18OBhEp0AUwFFwcfnDuc0ymlz2PRaJsH1fGOhrPy0dKVbYmRtfRh3NEgxeLicw/640?wx_fmt=png)

包含了所有人物信息的预处理器，我们再次请出库里当一下模特，模型使用的国风3，这个动作的模仿也是让人不得不佩服AI的脑洞了。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibHMPpVIGwr2VGM18OBhEpibPxjCzQiabQA0iard3shqialZlV4YSIYvicHI12gYSOLPTAaSqCgr3ziaNg/640?wx_fmt=png)

这张图蛮好看的，我决定来把她细化一下。  首先，我们使用之前讲过的扩展图片的方法，将这张图发送到图生图，通过“缩放后留白”
和提高重绘幅度，将这张图片的背景变宽。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibHMPpVIGwr2VGM18OBhEpFLcLOrj59lVfOicCrHYTzlz3JAoPRBiaW7FVuMLG9Db5ETHwvMyx4BuA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibHMPpVIGwr2VGM18OBhEpqjPA8Iia6Lg4p4LUkOwNjOyGvwWD7Aqgjaibias6Idrhickua6mB98XjSw/640?wx_fmt=png)

再次发送到图生图，使用  ControlNet中tile模型（这又是一个神器，后面细讲）进行细化。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibHMPpVIGwr2VGM18OBhEpkSg9vXlHp1EhJ7Mr72icqBe7k3UkXxQhr0Xq0tq1YXVuVpNzr2hlJWg/640?wx_fmt=png)

这时，图片拥有了更精致的细节，最后再使用一次SD放大插件。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibHMPpVIGwr2VGM18OBhEpKibmjMjfJCULQickORJftIdL5eXjcZodVypudpJOaKgHEgJrBFbrRhGg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibHMPpVIGwr2VGM18OBhEpWFCg0egqkibH9h9I2iaoQeCvN1ULsvtqARWrJEqwAzlGn2icPrcPwr0Kw/640?wx_fmt=png)

完美。  
![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibHMPpVIGwr2VGM18OBhEpR6Dg2BHnYmVkkiam6604YmDujgEkos9iawEPzg48UyD02vmoxVqlhuSA/640?wx_fmt=png)
以上，就是关于  ControlNet中姿态约束类预处理器的介绍，但是很多时候，我们并不能恰好找到满足我们需求的动作图片拿来给
ControlNet解析，那我们可不可以自定义动作骨架呢？
答案当然是可以的，作为一个开源软件，各种各样的插件帮手自然是必须有的，这也是我们这么喜欢blender的原因。
我们可以在【扩展】-【加载扩展列表】中搜索【posex】，就可以找到这个插件。
![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxibuSoLUE4yOibOmMibQ6YOZOaETffkZR1JBZSXNhibklv21IPcol6nCaiatqEgP533JTGY0kF1P813mA/640?wx_fmt=png)  
如果安装不了，可以直接将我分享的这个插件文件夹拷贝至这个目录下...\sd-webui-aki-v4\extensions，确保软件是最新版本，然后重启。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibHMPpVIGwr2VGM18OBhEpQ8qTAhQRt1wqwVm1PMROEM7HWLXAIRhKxGp8Vib9UgK1dIOMkGDEMyQ/640?wx_fmt=png)

我们重启软件后来到首页，点击“将图片发送至ControlNet”，就可以得到如下界面。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibHMPpVIGwr2VGM18OBhEphaqTicSxodBibT2UXNh6skvs8y2DCjtb9A6x3uCPNwNSJDcglia1ay3dA/640?wx_fmt=png)

拖动鼠标左键可以旋转视角。  

![](https://mmbiz.qpic.cn/mmbiz_gif/tyssYUEyRwzibHMPpVIGwr2VGM18OBhEpfgA6Hl43jHFViaDP7CeJGOTFG1iaemRgFz1ACLUg3L12eoWvbkkMJic8w/640?wx_fmt=gif)

拖动鼠标中键可以  缩放视角  。

![](https://mmbiz.qpic.cn/mmbiz_gif/tyssYUEyRwzibHMPpVIGwr2VGM18OBhEppMOUicvyF8Tb7STnnl4XkGXAhibCf1HQJLSfc5vE5L2icOBqicG1AYZvcg/640?wx_fmt=gif)

拖动鼠标右键可以拖动视角。  

![](https://mmbiz.qpic.cn/mmbiz_gif/tyssYUEyRwzibHMPpVIGwr2VGM18OBhEpibkQOwmbzToCKJzcFYnEESrY9NArJgBfOLQh5t04lI0NSkCPNaib3osg/640?wx_fmt=gif)

如果玩坏了，可以点击这里重置镜头和动作。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibHMPpVIGwr2VGM18OBhEpjCc4EoF0mxTNciaebNk14EUTUyaWAxZv8sBqxQzwUMUuibJFkjITSmww/640?wx_fmt=png)

我们调一个玛丽琳梦露的经典动作来试一试，右边可以调整出图的尺寸。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibHMPpVIGwr2VGM18OBhEpx1DXxywDAp7MMoHeFSNIn6nsib5eZoWU9DicxSiacRcF80Iqkn281QrmA/640?wx_fmt=png)

接下来启用  ControlNet，因为骨架图是从posex链接过来的，所以这里不需要再添加图片，也不需要预处理器，直接加载openpose的模型就可以了。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibHMPpVIGwr2VGM18OBhEpsu8iaF2t8UiclU3WXmOTWwpS3ry1DO2GEDXONia7FkNT6zmNJkzZsOiaicg/640?wx_fmt=png)

依旧是国风3模型，点击生成，这个姿势就绘制出来了。当然，AI的识别不会这么准确，经常会出现骨骼错位的崩坏图，所以需要你耐心的去刷图和调整参数。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibHMPpVIGwr2VGM18OBhEprepcnWOePeOwu3LxqfkibFXia6Y8zHkAjMHlRZz1vYAWNdamveRjlmcg/640?wx_fmt=png)

好了，今天我们介绍了  ControlNet中  关于姿态约束类的预处理器和模型。
另外，我这边还收集了一些不同的pose的骨架图，可以在人物动作上做一些参考，  有需要的可以添加我的公众号【  **白马与少年** 】，回复【SD】即可。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibHMPpVIGwr2VGM18OBhEp91IPehBGzYhuHUfMYGRSARJarV09u6B5aIhLdQGdpUplAu7ic6R391w/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibHMPpVIGwr2VGM18OBhEpbXv42HoY4udAObntFtaxUMKBMkuslVP32y2OZRvsiayHPbicJ8Soa2sA/640?wx_fmt=png)

  

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

