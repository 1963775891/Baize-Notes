![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tyssYUEyRwyQfCQCa50bTAiaScjRwz58llI1ChWtFCpOEF3cutibc6fLwYwTdyKXolzaw1MyxQwahaQ5a0TYRtzA/0?wx_fmt=jpeg)

#  【Stable Diffusion】最强控制插件ControlNet（3）深度约束

原创  吴溪源  [ 白马与少年 ](javascript:void\(0\);)

**白马与少年**

微信号  StreamWXY

功能介绍  Stable Diffusion、Blender等学习心得分享

__ __

__ _ _

在之前讲到的关于ControlNet的线条约束和姿态约束中，我们可以看到它预处理出来的图片都是平面的。
![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzfp6gdlVQlnJKKbT6qVrFJCbVv7dLg7icTicYJZVSpu6IKl4Sgic7T6gVVayKnyAic9p4iaFktnStFib9A/640?wx_fmt=png)
对于简单的结构还好，但是对于透视感比较强的图，AI可能就不能很准确地显示出来。
比如这张俯拍图，从骨架图中可以看到，人物从平面上来看似乎被识别成了一个短腿的形象。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzfp6gdlVQlnJKKbT6qVrFJSQec3wSicQRYWAYlfqzPJTTEgwAnpenWwaQDtTEticRBrnv92zPMibzpw/640?wx_fmt=png)

我们用这个姿态跑了几张图出来试试，选了一张最接近的，可以看出，openpose也并不是完全无法识别透视角度，但是要达到一模一样的透视单靠openpose是很难的。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzfp6gdlVQlnJKKbT6qVrFJWn2Ow8Icd6lxZYorXXC8PzhKly1FCXr9GDJym1QyZtSYSKLVPaibDjQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzfp6gdlVQlnJKKbT6qVrFJCI2pXZy4uSxUy8uTrQ4Uib5ba86EH6sD2iatmribKV6VicsqwOOohFTADQ/640?wx_fmt=png)

怎么样能达到完全一致的透视关系的识别呢？这个时候就要引入一个新的概念：深度约束。
****深度约束类：它可以通过黑白灰的颜色信息来记录场景中物体的远近关系，并且也能一定程度上还原外部的轮廓和线条。** **
我们使用depth预处理器来处理一下这张照片。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzfp6gdlVQlnJKKbT6qVrFJH0qiaiaErVL4M15UujjoeHOSH2SQGzgFiawXwmZnbF4vSTpgJxOgiclfzg/640?wx_fmt=png)

最新版的  ControlNet有四种深度图估算的预处理器，我们使用XYZ插件来看一下这四种预处理的区别，使用的时候可以根据渲染情况选择合适的预处理器。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzfp6gdlVQlnJKKbT6qVrFJcZZia6t0NkowKsvq43wXMT1MVCeG8Qmqicibo0Zf50Vg2BiaOGrQ0UaOfQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzfp6gdlVQlnJKKbT6qVrFJXHibyZcQ9P45BDiaLt30UZMQ7eNL2Hor69L9YwZMZwjGiaiaHE7lNvt6nA/640?wx_fmt=png)

但是，因为这个深度图也是有轮廓边界的，所以除了姿态以外，人物的整体形象也会固定下来。

比如这张样图，我们找的是一个男生，如果用这张深度图去生成一个女生会怎么样？  

我们随便生成一张，可以看到脸虽然是女生，但是因为身体轮廓是比较宽的肩膀，所以看起来十分的违和。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzfp6gdlVQlnJKKbT6qVrFJH6hlBQjWW9Vr01z8FHbiazHdqlP4go0CWQmZxsjYZNaFPLbX4V70lLQ/640?wx_fmt=png)

那有什么办法可以让图片既保持这种深度关系，但又不要完全按照这个轮廓来呢？这里，我们就要引入一个  ControlNet的多重控制的概念。  

我们来到【设置】面板，找到【ControlNet】，调整【ControlNet Unit 的最大数量】，这里我设置的是4。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzfp6gdlVQlnJKKbT6qVrFJIicYBSVrddwKyA5vsCtyCTh7KLkpfkO7neakI8MjU8s9hHK2XqleCUQ/640?wx_fmt=png)

这里就会出现四个面板，每个面板都可以使用一种预处理器对出图进行控制。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzfp6gdlVQlnJKKbT6qVrFJnETRNp9EX66BbicLtTJca0cllQmT02s5ywcsoogAwC7t7GqzQr3qGfQ/640?wx_fmt=png)

这里，我们首先使用的是openpose来控制人物的基本骨架，虽然它不一定那么准确，但是也是有几率能表达出一定的透视关系的。
![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzfp6gdlVQlnJKKbT6qVrFJHgA5oibbpkQhjkhLrMdBb4gGQmSVPBLfVYibysUqR8KzU9icv0n2biaEuQ/640?wx_fmt=png)
第二个控制模块，我们采用深度预处理器，但是权重缩小到0.25，因为不希望它太强的框定人物的轮廓。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzfp6gdlVQlnJKKbT6qVrFJHaSKvIxOerQ4HbbMqUTlibs8iaJ4y9eckeVL6DuJYh6UvHdK9ibq0FrcA/640?wx_fmt=png)

键入关键词：全身，1个女孩，白发，紫眼睛，学生，马尾，校服，墙纸，校园，操场。  点击生成，这样我们就得到了和原图透视一样的绘图。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzfp6gdlVQlnJKKbT6qVrFJtsqHDfCXAPw9dEEqo6fDGAu05sEBbEMUBJoBltTnhOEzv2BRcBfpaA/640?wx_fmt=png)

  
我们再来看一个  插件，叫做“sd-webui-3d-open-pose-editor”，可以在扩展中下载并安装。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyQfCQCa50bTAiaScjRwz58lbfvicLMRBcUq3ARgRiapbvoTFiaZ73CkHqEYuZiaoXU5ibS343jrpG6qsQQ/640?wx_fmt=png)

它的界面非常像一个三维软件，而且功能比我们上次讲的posex还要全面。
![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyQfCQCa50bTAiaScjRwz58lhGG2XSicOFnZyo9J1vbcYl43uzLUweP8xAwny8L9OehFAibiabDRLkzcQ/640?wx_fmt=png)
这个骨架包含了完整的手和脚的结构，右边的控制面板可以对每一个关节进行调整，摆出自己想要的姿势，身体的各个部分也可以细化调节。
同时还可以控制相机的尺寸，焦距，可以把人物摆在画面中的任何位置方便构图，右下角可以看见目前整幅画面的预览效果。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyQfCQCa50bTAiaScjRwz58lryWyHXhibJSExjAhsXDCaxhKmVwrpL2IGNpEEsEWmddtP8Q8ib2sZU0g/640?wx_fmt=png)

我们确定好动作和构图之后，点击生成，可以得到这样四张图，分别代表了：骨架、深度、法线、线条。后面三张图，主要针对的就是手部的绘制。一般情况下，我们使用骨架和深度就够了。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyQfCQCa50bTAiaScjRwz58lHQwqcMQ6IOnZsqeCckVZ6nvH1Ssv8bYFgVLmZNb3icJTABJsFokL8Kg/640?wx_fmt=png)

这里对应着发送到  ControlNet的哪一个区块，不需要的图直接点右上角的叉就可以关掉了。确定好之后，点击【发送到文生图】。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyQfCQCa50bTAiaScjRwz58lAPGDWmT7xSMTHwGF3D3poepFzQdngDtSYheq71xnwxTBHjp1KKwMew/640?wx_fmt=png)

来到首页，就看到图片已经被发送到
ControlNet了，两个面板都要点击【启用】和对应的模型。因为已经是AI可识别的骨架图和深度图了，所以不用再添加预处理器。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyQfCQCa50bTAiaScjRwz58llut5swc6VlXTdsjHshgMm1gSQpR7DwMhLdplMUZmUFby54ViccFsRRA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyQfCQCa50bTAiaScjRwz58loLUKtPdmVKeGTaia4VhVNicsruOq1ouzt84bpib4iaorWqgJFTfSJaAOJw/640?wx_fmt=png)

我们设计的是一个拿枪的姿势，因为在插件中手部的姿势未必能很精确地匹配枪，所以我们降低一点深度图的权重，让AI可以自由发挥一下。  然后输入关键
词：上半身，1个女孩，白发，紫色的眼睛，(警察)，双手握枪，手枪，壁纸，蓝天，城市
点击生成，开始刷图。对于目前的AI来说，画手还是一个难题，所以要通过不断地调试筛选，来选择一张比较满意的构图，让手部和枪能匹配上。  

![](https://mmbiz.qpic.cn/mmbiz_jpg/tyssYUEyRwyQfCQCa50bTAiaScjRwz58lfAJBG9QQkziaPTf4Mhe7SOKlLMnzrJq7OwCqXdicfzichicsCtfDqFcw6Q/640?wx_fmt=jpeg)

最后，使用SD放大，完成。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyQfCQCa50bTAiaScjRwz58l0tSx6po5wLpj3HvdicgD5lbRrBib8Ol84ysSxibre2lCnic63kC54ic1tOw/640?wx_fmt=png)

以上，就是关于ControlNet中深度约  束预处理器的介绍。

  

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

