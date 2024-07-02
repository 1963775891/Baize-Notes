![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tyssYUEyRwzJ23hFIVYiaaEoTrLEVIX0EDMTxHatQ1dvMMwnibsmSSdqO3yerxM83wNtyJwGFsm3ibmMia5wmQju5w/0?wx_fmt=jpeg)

#  【Stable Diffusion】最强控制插件ControlNet（8）创成式填充

原创  吴溪源  [ 白马与少年 ](javascript:void\(0\);)

**白马与少年**

微信号  StreamWXY

功能介绍  Stable Diffusion、Blender等学习心得分享

__ __

__ _ _

最近PS2023beta的出现给我带来了不小的惊喜，最主要的就是它的“创成式填充”，通过现有图片可以进行扩展和延展，其强大的契合度合理性目前无人能及。还不了解的朋友可以看我的这一篇公众号——
[ 【PS】Ai绘图哪家强？Photoshop 2023 Beta爱国版降临！
](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247486687&idx=1&sn=bc00c7e4ae00e2858c61e9b973747534&chksm=9fbecc2ba8c9453d8b9c3252ea1c81be41a94e9d21b66962b0ebf27e4a06d7daf9d3c1938707&scene=21#wechat_redirect)  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzJ23hFIVYiaaEoTrLEVIX0EIBicl9SiaU05d6dkQiawbsQhw7K2Y0kJDs0vJZhYxecSPJgtVNFO2s0Tw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzJ23hFIVYiaaEoTrLEVIX0EXhGicT9rmTzR4Ho9Tm05RI6tNwuiaoV3YRVkxTJZjxvnJpdOZiaicw8M1g/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzJ23hFIVYiaaEoTrLEVIX0EXQeHcMES0BcZS2hSmbwhFDbf4deJMKph7ZTz4LChraMgKicicz5ribrOQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzJ23hFIVYiaaEoTrLEVIX0ExND97vpj7c4F2Hyf0T88ZIIwPUwjS1AO2aSYpibcs9f8peez3sA4Ivg/640?wx_fmt=png)

不得不说，ps的大模型是真的强，涵盖范围包罗万象，什么风格的图都能进行扩展填充。但是，最近很多小伙伴反映说PS的这个功能出了问题，经常出现错误或者是网络忙碌之类的提示。这个问题呢，主要还是与我们的网络有关，需要一些魔法梯子作为辅助，其实还是可以正常使用的。  

那没有这些条件的朋友会说，既然ps玩不了，有没有别的方法可以替代呢？享受过了这个功能，突然就不能用了，感觉浑身难受怎么办？

其实，我们的Stable Diffusion也是能实现这些功能的。今天我们就来一起看看Stable Diffusion中的“创成式填充”该怎么玩？  

**# 图片扩展  ** 我们用这张图作为例子来讲解一下，首先将它导入到图生图界面。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzJ23hFIVYiaaEoTrLEVIX0EJJ7x9OzZiaKDeJict4b1ibl4Ofwt6ZLMdHSdnnLQWYBgiakvY7TxhT8UIQ/640?wx_fmt=png)

根据情况选择大模型，一般卡通类的选择“revAnimated”，真实类的选择“  Realistic Vision
”，但是也不一定，如果效果不好，可以尝试一下其他的模型。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzJ23hFIVYiaaEoTrLEVIX0E1bCIibH2GcGtVA3Gg4W136mPwdBad9S7ibqHV1jGFUn2380erA1NQneQ/640?wx_fmt=png)

图生图中比较重要的参数，一个是“缩放模式
”，选择“缩放后填充空白”；然后是尺寸，如果是横向扩充就增加宽度，如果是纵向扩充就增加高度；单批数量可以根据需求填写，增加抽卡概率；最后尽量将“重绘幅度”加大到“0.8”以上，让AI充分发挥想象。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzJ23hFIVYiaaEoTrLEVIX0EH2icIx1wtZJk62ZgBofibuNRDDcCq7N5hERarbxfkEuoc2fB1UEllQ8g/640?wx_fmt=png)

接下来是controlnet的设置，升级到最新的controlnet版本，将图片导入进来。
启用插件，“控制类型”选择“局部重绘”，也就是我们之前讲到过的inpaint预处理器，然后在预处理器的下拉菜单中选择“inpaint_only+lama”，这是一个新增的预处理器，专门用于扩图。另外，控制模式选择“更倾向Controlnet”，缩放模式选择“缩放后填充空白”。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzJ23hFIVYiaaEoTrLEVIX0EntsAkYZLa5D0tc8Pf0iaPzXRroicVeW8EMAaK01iaypriczTxvHm5u8wDQ/640?wx_fmt=png)

为了让出图更加统一，甚至还可以再增加一个reference  
_only的通道，来进一步巩固扩图的风格。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzJ23hFIVYiaaEoTrLEVIX0EdKeOqRRI2nt6q41Q4vYPRMF4zZGfjFFXKE5fia7an5ETocEgOcXHzmA/640?wx_fmt=png)

设置好之后，点击生成，等待结果，选择一张满意的即可。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzJ23hFIVYiaaEoTrLEVIX0E0yVEY7ge92ic0vv4DDxe3rI6FfuEfMB9jmVPRTR60JEmQg4YnA3W5Gg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzJ23hFIVYiaaEoTrLEVIX0E7cAyPXHBtgCkN16soV6GezQsTsr8G8D1dwxiaLnu7ASbqzcqBFiaQibMg/640?wx_fmt=png)

我们再试验一张图，将这张图放进图生图中。
![](https://mmbiz.qpic.cn/mmbiz_jpg/tyssYUEyRwzJ23hFIVYiaaEoTrLEVIX0EmYPeX596mFXYwzxpBBdRFMkTQKibAsTYNllqQBJ2JvCVeOiaiaZnmib8YQ/640?wx_fmt=jpeg)
有时为了更好地控制出图，我们还可以通过反推提示词的方式，增加一些文本进行控制。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzJ23hFIVYiaaEoTrLEVIX0E1ZY6TWJHL9yoID2pFElGnlmNV73GukKic1qg0ia53j8p3s5tic1xqtnjg/640?wx_fmt=png)

这样生成的图也会受到提示词的影响，可以看出图形部分的衔接还是很自然的，但是不是每一次效果都能非常好，新生成的部分和原图可能会存在色差，需要通过调整各项参数来修正。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzJ23hFIVYiaaEoTrLEVIX0EPdicyq1DicoSllVq0jmNvsMaUWOVu3yWNnOsdXqz4oZSibIavmJI8XBgQ/640?wx_fmt=png)

从网上找一张建筑图，使用真实系模型来扩展一下，  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzJ23hFIVYiaaEoTrLEVIX0EXSPbO26tjBgGIqfoqtkVZibZdFC928XfuS5G5CAjmsGwQzb8x32Jtibg/640?wx_fmt=png)

其他参数不变，仅需要调整尺寸，并将图片分别放入“图生图”和“controlnet”中。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzJ23hFIVYiaaEoTrLEVIX0EicWrJjtGc6krWYljSvLVjDHZsuMhEebEibeday2U8s7QEeZ9adIAIa8w/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzJ23hFIVYiaaEoTrLEVIX0ES7HVYz7CMrHmr5MqQtw3VPd0cq3zuvvWs0NY7sAeapoOv9KS8EXTYw/640?wx_fmt=png)

点击生成图片就扩展好了，只要记住这个工作流，扩图还是很快的，只要替换图片改尺寸就可以了。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzJ23hFIVYiaaEoTrLEVIX0EhWSaK3pA8qibRzB5M4qd7R5A1hiaicfraSWKxLCjsRibzOVVrlcX6r62vw/640?wx_fmt=png)

**# 去除图像人物**

将画面中不需要的元素去掉，也是新PS的“创成式生成”中非常有用的一个功能，这个功能的实现不需要用到controlnet，直接使用“图生图”中的局部重绘就可以了。

我们以这张图片为例子，看看怎么快速去掉图中的人物。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzJ23hFIVYiaaEoTrLEVIX0EmkkrzL73h2Y3lkhXpiccNX1aIUvDbPpicuE6SjJegjvbdQG3IGTc0ulA/640?wx_fmt=png)

在使用“局部重绘”时，有一个步骤很关键，就是选择我们的大模型。

我们打开C站，可以看到下载页面有一个版本选择的地方，有的版本号的后面跟了一个inpainting，说明这个模型是专门用于重绘的，所以要下载和使用这个模型。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzJ23hFIVYiaaEoTrLEVIX0EZMD33VdYgYhsJv74VDics49jjiaa6fltrEsSTa92QaxE6ibj5eVS8Y07Q/640?wx_fmt=png)

不用填写任何提示词，只需要将图片放入“局部重绘”中，涂抹掉人物的部分，蒙版可以比人物更大一点，保证能全部包裹住。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzJ23hFIVYiaaEoTrLEVIX0EHFWQ3HqX4fR3mCrzibwfq4LZa30rEE9AXapiabJxiaPauskoH4U6raBFQ/640?wx_fmt=png)

蒙版区域内容处理选择“填充”，“重绘幅度”为1。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzJ23hFIVYiaaEoTrLEVIX0EwRx9HbnSOBfZBtRa8WCnZUtukibERabEnibeGufAGWyAufjibKucJF25A/640?wx_fmt=png)

这样，我们就很快地将人物去掉了。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzJ23hFIVYiaaEoTrLEVIX0Ekkv7IHL0iag6gxTV9kqG8NmZzRH32xkgUT7vfmDdX4BMQj7TzibzoDHw/640?wx_fmt=png)

**# 总结**

创成式填充在工作中的作用还是很大，特别是在我们的素材图不完整的情况下，这个功能就显得尤为重要。在这方面PS的强大不言而喻，无论是出图的质量还是操作的方便程度上，都是最好的。

在这方面，SD就相对复杂一些，想要达到很好的效果，需要多一些的调试，但是也是很厉害的。如果你的电脑用不了最新的ps，不妨看看在SD里面怎么使用“创成式填充”吧。

  
  
  

预览时标签不可点

微信扫一扫  
关注该公众号



轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicFrWhQnGuwdp4icKgCxibWO94LTgVCdyGEa5tticq3VQ0wbSfnGkl6ficicgn1LmHvKohOIT76T3un55Q/0?wx_fmt=png)

白马与少年







****



****



  收藏

