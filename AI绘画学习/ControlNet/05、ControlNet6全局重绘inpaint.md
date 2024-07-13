![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tyssYUEyRwyy12uiaSWO1yvkFhHXwa1d9h0fjNib0MxxRiakDWLYGKib5g75mXcjHGJuxG4NicicOeyT3Tfd1E3F4myA/0?wx_fmt=jpeg)

#  【Stable Diffusion】最强控制插件ControlNet（6）全局重绘inpaint

原创  吴溪源  [ 白马与少年 ](javascript:void\(0\);)

**白马与少年**

微信号  StreamWXY

功能介绍  Stable Diffusion、Blender等学习心得分享

__ __

__ _ _

在Stable
Diffusion中，如果我们想对已经画好的图像进行修复，可以使用之前介绍过“图生图”当中的“局部重绘”功能。但是“局部重绘”也有自己的局限性，并不是所有的情况下都表现得很好。

在ControlNet中，同样有一个inpaint功能，可以使用于绘图的修改调整，我们今天就来对比一下  inpaint模型和“局部重绘”的效果有什么不同。

**# ControlNet VS 局部重绘  **
首先我们使用真实系模型“deliberate_v2”，在文生图中生成一张人物图，填写一段提示词，描述的是一个穿黑衣服的光头男人。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyy12uiaSWO1yvkFhHXwa1d9QQNoiaUCtUeWpQPnRnLDqeOwnmibWEf7vRFhhE2JHDjekwfuCsUq1lbQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyy12uiaSWO1yvkFhHXwa1d9EFxiaaC7rDsmDDjvE6TX4oNBT1B6YwxNTR6Na00QKQInTHpibH7fEYEA/640?wx_fmt=png)

接下来，我想通过局部调整的方式给人物加上帽子。  首先我们要在正向提示词中加入“Wear a
hat”，来告诉AI需要给人物加上一顶帽子。然后我们打开ControlNet，将图片拖入其中，使用画笔涂抹人物的头部，涂抹的蒙版范围决定了重绘区域，所以想要多大的帽子就涂抹多大的范围。
预处理器选择“  inpaint_glob  al_harmonious 重绘-全局融合算法  ”，模型也要选择“  inpaint
”，从名字可以看出它的原理是原图重画，然后只取蒙版部分填补进来。这种算法的好处就是重绘部分和整体的融合程度最高，缺点是耗时较长。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyy12uiaSWO1yvkFhHXwa1d9iaaUYZSuicmbQgAeemk6f22ymFLHZJhxmZhsUlRkD98z0KnmpUrUBicbw/640?wx_fmt=png)

点击生成，可以看到帽子已经完美地出现在了人物的头顶。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyy12uiaSWO1yvkFhHXwa1d9p6sLbFaGAwiaF2ncbsnRTLo3hgBAIfT5FPicF1tubZahuibnRJPicBu4Yw/640?wx_fmt=png)

接下来，我们测试一下“图生图”中的“局部重绘”。  将原图发送到“图生图”中，使用局部重绘涂上帽子的区域，添加关键词，重绘幅度拉到0.8。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyy12uiaSWO1yvkFhHXwa1d9hThR5wPANIMiarhbx4EQUuygb6s8da42Yw7lMwKibq4skX41h0dG8wmQ/640?wx_fmt=png)

效果也有，但是感觉哪里有点怪怪的。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyy12uiaSWO1yvkFhHXwa1d9ZuJhQjLGTK4PM4pGlUFjQf3gYooITyibszBZCplylfszlQfrfVZzz1w/640?wx_fmt=png)

调整参数，再画一张看看。融合的部分，还是稍微有点不太自然。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyy12uiaSWO1yvkFhHXwa1d9nWKibO6bUJdP8Pm0Kp04A53jyMbdLLzrmLPhPHRCmMy6g2TpJafvVqg/640?wx_fmt=png)

我们再做一个对比测试。  先绘制一张女孩在海上坐帆船的自拍照风格的图片。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyy12uiaSWO1yvkFhHXwa1d9A87z6f8shBiaovIn0DibPkfyiayibprr1kUocsabAvkC8jqWUicJqFj0vDQ/640?wx_fmt=png)

使用  C  ontrolNet  中的inpaint模型，涂抹人物的衣服部分，添加关键词“夏威夷风格衬衫”。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyy12uiaSWO1yvkFhHXwa1d9YG6dpxNxxa3GXYQmgRwiba2CSJHuLs5XcI4SNibBB1icK0rSGF66ibZZ0g/640?wx_fmt=png)

点击生成，修改得非常贴合，几乎看不出痕迹。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyy12uiaSWO1yvkFhHXwa1d91HmrnTgnr6I4PJpA8iaqTQfCy9j20WegqFrUJl7Ciclda0j7gl5Inxfg/640?wx_fmt=png)

同样的参数，给到“局部重绘”当中。
![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyy12uiaSWO1yvkFhHXwa1d9eg2cedUSkfZGdRSDRQQCcWSR0pFPxwR63BpviaWuaRNg18Rpuhv5uWg/640?wx_fmt=png)  

“重绘幅度”设置为最大的1，相比于  C  ontrolNet，产生的变化就相对小了一些。实际操作中具体该如何应用，大家可以根据需要选择。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyy12uiaSWO1yvkFhHXwa1d9VdFI2FXWEB56yHo9emuAbfjBdSvEGDu1N1TibjzGV5qicViaff8Qicq0ug/640?wx_fmt=png)

**# 去除图像人物**

有时候，我们需要去掉画面中的主体形象，填补上相对复杂的背景，这个需求可以使用  inpaint重绘功能来实现。  

****

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyy12uiaSWO1yvkFhHXwa1d9CKFd7UBtCesM6RBOwtuvAqeop9FIqDiaaTwfKFMickgXnRaSBaO1EG5w/640?wx_fmt=png)

我们首先将这张图放入WD 1.4 标签器（Tagger）中，对图像进行裁剪，只保留背景的部分，然后进行反推提示词。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyy12uiaSWO1yvkFhHXwa1d9tmu4YI6LibJLJfHb2YpTvBSc2rh2sgXaiaPzDPA4RUThUNuklcZwSQ1Q/640?wx_fmt=png)

这张图片的反推提示词如下：outdoors, no humans, tree, scenery, grass, sky, cloud, day, blue
sky, mountain, road, house, path, building, nature, cloudy sky。  
检查一下，如果问题不大就可以发送到文生图中。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyy12uiaSWO1yvkFhHXwa1d9NW1cAz6gD3kDpVR2pXTsPUbQkvTXbeo5tHOlWZh4XyEVJwEPP8HoDA/640?wx_fmt=png)

开启  C  ontrolNet，使用  inpaint模型，涂抹人物的部分，点击生成。  
![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyy12uiaSWO1yvkFhHXwa1d9saAeb8lGR7NWt5Gc0kibc3cVIVgN6Ouq3SibSV9ia4wznRNhVzKvic4woA/640?wx_fmt=png)
修补完之后，人物的部分确实已经去掉了，草地、桥梁、山也填补得比较完美，但是画面风格好像有点不太一样。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyy12uiaSWO1yvkFhHXwa1d9xkV5tI4kyxvhIDribsmNqrqShWogibibKmLJclG33q72IbPPEWNpC6qKw/640?wx_fmt=png)

我尝试将控制权重提高到2，来尽可能保留原图的风格，控制模式改为更注重提示词。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyy12uiaSWO1yvkFhHXwa1d9bB8bPgTWHwv6zFc9tgibP3Ykv0xibuCqIqaTIPsgccNjaBcKGibL1FDkw/640?wx_fmt=png)

这样，除了颜色饱和度比较明亮以外，整体修补得还是不错的，颜色方面可以通过后期的PS去调整。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyy12uiaSWO1yvkFhHXwa1d9clfibic5T6NYiagPU9vibs5Eq3byq8sJxRMkR1njDicvgYniaEpUfES8VUkQ/640?wx_fmt=png)

我们再试试图生图中的“局部重绘”功能，同样的方法，涂抹掉人物的部分。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyy12uiaSWO1yvkFhHXwa1d9A89UUfq7bicC5MNnZu3aszoib2TcQiaMhno8yZKGz3iaQ6jeuzrUlBBjuw/640?wx_fmt=png)

可以看到，虽然风格保持了一致，但是填补得并不好看，在原本人物的部位，生成了一些奇怪的东西。
![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyy12uiaSWO1yvkFhHXwa1d92eMtrYKcQ72qz05eB2AOWednDoohcsDYcau6bGqAPnwdhjGDet5ibfQ/640?wx_fmt=png)

**# 总结**

在图像的修复和调整方面，inpaint模型是要强于“局部重绘”的。因为  inpain
t模型实际上是对全图进行绘制，所以重绘区域和整体的融合度会更高，而“局部重绘”很难从全局出发来构思这张图。  

如果你先要保证整张图不变，只修改局部的话，就要使用“局部重绘”，因为  inpain  t无论如何都会对蒙版以外的区域做调整，和之前会有区别。  

当然，如果你本来就是对AI出图做调整的话，因为有原先的关键词，参数，种子作为固定，所以哪怕是  inpain
t，也能基本保证其他区域不变，就像我们一开始做的那两个案例一样。  以上就是ControlNet插件当中  inpaint重绘  功能
的介绍，和与“图生图”中“局部重绘”的对比，更多的使用方法大家可以继续发掘。  如果想要  ControlNet中  模型的话，可以添加我的公众号【
**白马与少年** 】，回复【SD】即可。  
  
  
  

预览时标签不可点

微信扫一扫  
关注该公众号



轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicFrWhQnGuwdp4icKgCxibWO94LTgVCdyGEa5tticq3VQ0wbSfnGkl6ficicgn1LmHvKohOIT76T3un55Q/0?wx_fmt=png)

白马与少年







****



****



  收藏

