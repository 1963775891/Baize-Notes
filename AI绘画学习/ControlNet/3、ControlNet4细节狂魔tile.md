![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tyssYUEyRwzZzSUpoqogaj0SgAOOdM2fH33XmIFJexjyl96lQIHez8Nlt2ZbVnaxsgvDZBWktR4n4KPpeibVb0w/0?wx_fmt=jpeg)

#  【Stable Diffusion】最强控制插件ControlNet（4）细节狂魔tile

原创  吴溪源  [ 白马与少年 ](javascript:void\(0\);)

**白马与少年**

微信号  StreamWXY

功能介绍  Stable Diffusion、Blender等学习心得分享

__ __

__ _ _

随着ControlNet1.1的更新，tile模型横空出世，其强大的功能让之前的一些模型变得有点黯然失色。
今天我们就来盘点一下，这个神奇的Tile模型都有哪些用法。

  * **高清修复小图**

在我们做设计的时候，经常会遇到一些分辨率不高的素材图片，我们需要将它进行高清化处理。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzZzSUpoqogaj0SgAOOdM2fiag8xcXGQUXn6KOia3zf5oW3drfHSSbW6LQgHSe9wk4GfBMFN2VG3TiaQ/640?wx_fmt=png)

比如这张食物的图片，先把它拖进“  W  D 1.4 标签器  ”，可以进行反推关键词，然后发送到图生图。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzZzSUpoqogaj0SgAOOdM2fE7fpldnckZu1nZ0cPQuyibmc0MP7xnBkDd9tvEMssx91JVCkKFC3YhA/640?wx_fmt=png)

我们可以通过翻译软件检查一下提示词有没有问题，这边通过反推得到的提示词是——“没有人，食物，食物焦点，现实，水果，静物，草莓，模糊，蛋糕，糕点，景深，甜点，模糊背景，奶油”。基本上与原图相符，可以先不调整。  
接下来，我们使用大模型“dreamshaper”。调整参数尺寸，放大为2K，提示词引导系数 (CFG Scale)官方推荐在15以上，重绘幅度在0.5以上。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzZzSUpoqogaj0SgAOOdM2foKK2xjTTk8GGGgYARniaBfuSNV42784Fic5e7vt3pB5aF0THcC7WiaN2g/640?wx_fmt=png)

打开ControlNet，导入图片。tile的预处理器是用来降低原图的分辨率的，为的是给新图有足够的空间来添加像素和细节。如果你的图片本身像素就很低，可以不使用预处理器，直接使用tile模型。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzZzSUpoqogaj0SgAOOdM2fs4QQgPs2MkmlWx3udicnnMESrU3jcSjC8lUd2goWoabteVuic11bkzcA/640?wx_fmt=png)

可以看到放大后的图片，清晰度和细节都有了很好的提升。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzZzSUpoqogaj0SgAOOdM2fW99x9dBGe2jD8fuVUPN69lyIsRfNjFiae4iahWgGHzBHO0DpK8DOPw4w/640?wx_fmt=png)

对比一下使用tile模型处理前后的区别。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzZzSUpoqogaj0SgAOOdM2fRVW6rEUXWnqfYOmU1icHguTExCa5Ukic7emRWHA1CqKGVRrTtu9GR9cQ/640?wx_fmt=png)

  

  * **修复和增加细节**

我们先随便绘制一张小屋的图，可以看出，这张图中的细节不足，而且有些地方的结构也是错误的。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzZzSUpoqogaj0SgAOOdM2fSHzP1DQY5fTCmLz4G4q89ybicA3GMKUPnqLqfcv10FpRlPAEj9uBzOw/640?wx_fmt=png)

由于这张图是采用高分辨率文生图绘制的，分辨率是1800x1200，所以我们在
ControlNet中启用了tile预处理器，让图片先缩小，给AI足够的空间去绘制细节。  ****

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzZzSUpoqogaj0SgAOOdM2fXZ86IQ3xniaYtKq1WSmgbMicP53WCg0Q0X2gk5pGEXP5CTHr2PotpwBg/640?wx_fmt=png)

修复图中，增加了很多的细节。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzZzSUpoqogaj0SgAOOdM2fxkvxtxUSeZjVpSozcFmBicuf8icNROYDDlgXib6FVpbfia5cTt0bug8Tgg/640?wx_fmt=png)

我们在提示词中增加“秋天”这个关键词，就得到了秋天的景色。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzZzSUpoqogaj0SgAOOdM2fQq29ADNJ9b1GfvTULT6Q4ClN1IibenQf0tsmwk1HojoS1EAaU5icYngg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzZzSUpoqogaj0SgAOOdM2feCV1vs6Yt2t8vGSfbrDcx2EaFzt8plibYBuUict1MYs0op3D8JXxxlwg/640?wx_fmt=png)

再试试，冬天的效果，选择更注重提示词的模式。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzZzSUpoqogaj0SgAOOdM2fxicxlmZym1CI2ue32nibe5Xic2Uj0js0VDDiawwpiaMCZo2CBjQgNtR0PuA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzZzSUpoqogaj0SgAOOdM2fCUkrmicXWCpU0ial0M4R52qxulc9t6dlqekiaVgSER6MqrL0zOeDhRx6Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzZzSUpoqogaj0SgAOOdM2fP94E5icGU921IxYnsDbibxeoHTbvAWUkajjebaLnibE2rF16ib5FC7Iy9Q/640?wx_fmt=png)

  

  * **修改添加细节** ****

这里我们先绘制一个女孩的图片，使用的“meinapastel_V4”大模型。关键词信息：(杰作，最好的质量，高分辨率:1.4)，1女孩，女人，星蝴蝶，绿色鱿鱼装，角发带，微笑，看着观众。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzZzSUpoqogaj0SgAOOdM2fUQNGAFU84ovJUpgiaqYX6dNcRXPyicxVt0naVvicic47CgsMpOQtbzXwbQ/640?wx_fmt=png)

使用tile模型，添加新的提示词：红眼睛、蓝头带。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzZzSUpoqogaj0SgAOOdM2f4BiasWjsl98Y9QDNZdHjS4TX2cgE4uQaLUR4GTdk4nvQlFYFMuDibsgw/640?wx_fmt=png)

得到结果，成功调整了图片的细节。但是tile模型的原理实际上是对图像进行重绘，并不是像ps那样可以只改局部，所以整个图像上还是会有些微的变化。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzZzSUpoqogaj0SgAOOdM2f1LC7IBSy3SlEAMw1gOFwSibMPicxqXgcVuN9K0ibGMMnHdhVKTNLlc53g/640?wx_fmt=png)

  

  * **分区放大** ****

我们之前曾经讲到过如何生成商业级高清图片—— [ 【Stable Diffusion】如何画出商用级别的高清大图
](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247486230&idx=1&sn=dde16ebbd5078661c21835c94db554dc&chksm=9fbecbe2a8c942f48cfe40eaea15ff963db9b4fe1c9a8aed330ee718bcf6720e491fc9237a7e&scene=21#wechat_redirect)
。比如我使用大模型“colorBoxModel”绘制的下面这张图，如果还希望它能更清晰一点，就可以使用SD放大。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzZzSUpoqogaj0SgAOOdM2fTJX36OMHaDLwDX0NI5icNQb39xaibPXGfYCgicWUCRhic7d397uPQBs7TA/640?wx_fmt=png)

SD放大的原理就是利用  分区的方式  将  图片切成  多块  ，然后每一块分开渲染  ，最终合并成一张图
。但是这样渲染有一个缺点，就是重绘幅度不能开得太大，开得太大的后果就是每一块分区里面都有可能生成新的人物。
当我将重绘幅度调到1，放大刚才那张图片，结果就变成了这样，每一个分区之中都产生了新的绘画。通常情况下，使用SD放大，重绘幅度都设置在0.3以下。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzZzSUpoqogaj0SgAOOdM2f31VI3WVCOqzfF6hCib0Bl1gnYhq24mJqU3UxClJ0SDvhMic9JJQlTJww/640?wx_fmt=png)

这时，我们使用tile模型，还是保持重绘幅度为1，放大1.5倍，进行绘图。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzZzSUpoqogaj0SgAOOdM2fFkkgDTMIfiatK4AnaicmLAjXbQibCDAb85LkWRSR8mFpOCAIiahgzbJ4nA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzZzSUpoqogaj0SgAOOdM2fxDtATX9nEC1l7icD0kpZgjn6uW1TEA40qEQNXQPl1gY57c32ibHDRVLg/640?wx_fmt=png)

由于重绘幅度的提高，画面的细节得到了非常大的加强，但是可以看到，在tile模型的加持下，如此高的重绘幅度并没有导致画面崩坏。当然在一般情况下，也不需要将重绘幅度刻意调这么高，因为太多的细节也会影响图片的观感。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzZzSUpoqogaj0SgAOOdM2fDnx2amaAr63kkwlQsJVScJpiaR8hR6GLQIUr7jB7QkHkibSibyLicalAyg/640?wx_fmt=png)

放大之后，拿来做手机壁纸也非常漂亮了。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyvZKqib0EdWpvJsDnib7qQyAjufarcQWWKXDzLciakZZMf1bCNg1bPRicKicoVENictXjwKphvmk50IMicg/640?wx_fmt=png)

  

  * **补齐草稿** ****

当我们有一张这样的草图的时候，我们可以利用Tile模型对它进一步细化。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyvZKqib0EdWpvJsDnib7qQyAmibeFmjZXEPoZvCm1b24vcTD9JDxZoIbAz0Esa5lvkaO2MDXdI73YRA/640?wx_fmt=png)

将图片导入到  ControlNet中，提示词为“一间木屋，两棵树”。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyvZKqib0EdWpvJsDnib7qQyAMTmKjdGDhIuNFEC2AHb170J0q9Jhw7YDia0YtNHy6l7H8a6wWodiaz3w/640?wx_fmt=png)

这是细化之后的结果，tile的这个功能可以帮助我们对简单的色块草稿做细化，提供一些设计灵感。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyvZKqib0EdWpvJsDnib7qQyANyuWO1jaw7u5OmFVRTBPCvcTibtPSI8LcibL6aHiauI6MuTctw4MFs21Q/640?wx_fmt=png)

我们再增加一点关键词——“一间长满鲜花的木屋”，并将下面的控制模式改为“更注重提示词”。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyvZKqib0EdWpvJsDnib7qQyAicbRhhkF9iasQdRmLA63GeAu2ia0ic1g7ErfMGHFdYMiaUm9rLD2FrkDx2Q/640?wx_fmt=png)

生成一下，是不是更惊艳了，这个用法就是我们最后要讲的一个tile的功能，也是它的最强功能——随机提示词转换。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyvZKqib0EdWpvJsDnib7qQyAMgZA3tIhkoTHAOP9yFnXu1tDCqOicDotNktAsjqLMUiaN9e8ZvV09rhg/640?wx_fmt=png)

  

  * **随机提示词转换** ****

这个用法的主要效果，就是可以用提示词对我们的参考图做出调整。  比如我这里找到一张钢铁侠的图片，我想要用这个动作来绘制一个美国队长的形象。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyvZKqib0EdWpvJsDnib7qQyAlK8dsFF3vm1iaVBMPUZI9FnqhI5RhcHDbMmZRS40HsXJkibAy5lZ3m9Q/640?wx_fmt=png)

在此之前我们可能需要使用  openpose  来识别这个  骨架  ，或者  用canny来识别轮廓等等  。  但有时  你会  发现，
openpose  对于一些  动漫形象  ，或者是非人类的  形象  ，它无法识别出骨架  。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyvZKqib0EdWpvJsDnib7qQyAK2hdctHEHnmuia6bfUqdjX7vqtCbX2JVIvV7Hr2prAbVQibvKQzFXuKw/640?wx_fmt=png)

但是，强大的tile模型可以做到这一点，从某些方面来说，甚至比它们更好用。  我们输入提示词信息：美国队长，手拿盾牌，背对观众，美丽，杰作，最好的质量。
控制模型选择“更注重提示词”。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyvZKqib0EdWpvJsDnib7qQyAtu9gB5VtBnfrANPWunc3An3KuGpyDeHAHRXX19ezc3I6VO93P8tScQ/640?wx_fmt=png)

点击生成，可以看到效果是非常不错的，tile模型做到了openpose做不了的事情。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyvZKqib0EdWpvJsDnib7qQyAJicGicmOHbD7Hp8F3Og1aoIPbQWJptXEE0RGQibHO0T28rjG7soBRmncw/640?wx_fmt=png)

好了，以上就是ControlNet插件当中tile模型的用法，高清重绘、抠细节、局部调整、色块联想、姿态绘制，几乎无所不能。
这个强大的tile模型我已经给大家整理好了，  有需要的可以添加我的公众号【  **白马与少年** 】，回复【SD】即可。

  

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

