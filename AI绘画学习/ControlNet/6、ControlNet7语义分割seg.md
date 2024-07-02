![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tyssYUEyRwyclu9q0t5G5Dcgkgyu5ehc9vT3D3fzm6bsK6VEwAIBfoNJGuZgGWWc02yojMlROQjicroKl1zvwPA/0?wx_fmt=jpeg)

#  【Stable Diffusion】最强控制插件ControlNet（7）语义分割seg

原创  吴溪源  [ 白马与少年 ](javascript:void\(0\);)

**白马与少年**

微信号  StreamWXY

功能介绍  Stable Diffusion、Blender等学习心得分享

__ __

__ _ _

在画面创作中，构图是至关重要的。而在大部分的AI绘图中，人物往往都是处在画面中心，或者是随机生成，看天吃饭。

在ControlNet中，有一个语义分割的预处理器和模型，就能解决我们构图的问题。

**# 简单理解seg** seg的主要作用就是把图像中的元素分类到对应的类别当中，并按色块区分出来。  为了方便理解，我们从网上找一张上海的街景图做演示。
![](https://mmbiz.qpic.cn/mmbiz_jpg/tyssYUEyRwxalq1p2mKfdTYgCDC5ju4KX0Pia6VsbrxYgibDZyOv5r3iaVcAMTT5tNMuFVYVtu5JytKOuudtELicGA/640?wx_fmt=webp)

  

将图片拖入到  ControlNet中，使用一个seg预处理器，进行预览。

  
![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxalq1p2mKfdTYgCDC5ju4KDNxO0Hwa2iaUxI7N41mGTE2oYwt6OYdE5lGVx2BSJuq7NEgAtulRpFg/640?wx_fmt=png)  

可以看到，照片被处理成了很多的色块。天空、大楼、汽车、路灯、马路等等，每一种都被赋予了一个独特的颜色。

  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxalq1p2mKfdTYgCDC5ju4KRHmQqLlcsq8ZD4YDXyxb1o1L6CPRRGl3yibTReQYl3CFicdIEUxUJicnw/640?wx_fmt=png)

在最新的  ControlNet版本中，seg预处理器有三个，它们对物体的区分会有区别。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxalq1p2mKfdTYgCDC5ju4KO5PotnIpibpcM9zUobkqOm01F0OsHGh8rjiaruM0XOE9kiaq3e8q12sqw/640?wx_fmt=png)

我们用这三种算法分别做了一次预处理，第一张和第三张都是基于ADE20K协议，所以它们的颜色对应是一样的。而第二张是基于COCO协议，它的每个颜色所对应的含义不同。至于具体应该使用哪一种预处理器，主要还是看你需要的元素能否被准确地识别出来。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxalq1p2mKfdTYgCDC5ju4KSHEEYdBdQb62enC2ZSib9eeia6ySCVwdyxsfTCKiaMjYLq1yuJkTW8CRg/640?wx_fmt=png)

这两种协议中，每个颜色所代表的含义已经被整理成了两张表格，分别是由b站Up主“大江户战士”和“智能野人”整理完成。这两张完整的表格我也会放到百度云盘，有需要的朋友可以在我的公众号回复“sd”自行领取。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxalq1p2mKfdTYgCDC5ju4KuuJXmtOXUHIia1PZeO2Xyodfy7UeSwSIHH2chtJBM3uicTUrm9AkcSHQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxalq1p2mKfdTYgCDC5ju4K98tmfDAChUkp6rYWWnuRmZSSYwnvLfFTXOXXN4XBAP1xfQtOcGZEiag/640?wx_fmt=png)

**# 实例运用**

那当我们通过seg做好语义分割之后，这张图到底有什么作用呢？  我们添加正向提示词：城市，街道，夜晚，霓虹灯，广告灯箱，多彩，繁华，赛博朋克。
使用“neverendingDreamNED”大模型，添加好seg模型，点击生成。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxalq1p2mKfdTYgCDC5ju4K5miaQBsJW59tjx97IXdgic0yDibgFAX4aeCQzMWkIrO7SZvss6S4vaMAw/640?wx_fmt=png)

我们就得到了一张和原图构图一样，元素位置一样的图片。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxalq1p2mKfdTYgCDC5ju4KvDdVzEvSrU4euJUporDVLrvMYC8A4Cof1YkSyBia5NhciaTVa3UgvgbQ/640?wx_fmt=png)

接下来，我们将seg图导入到ps里面，来做一下调整。  按照  ADE  20K  协议的  颜色对照表，找到树、水、船的色值。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxalq1p2mKfdTYgCDC5ju4KOj8KUktI61vWOibDt2rLDVMLibqONmENBwQoa6AC0kEITiaVFNALe0xkg/640?wx_fmt=png)

用魔棒工具选择大楼的色块，填充为树的颜色。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxalq1p2mKfdTYgCDC5ju4KOlczURXDdEESjy3PwH9TVOOHFpDWWmibX9dbHOvoduTcMR1Y3E6ScQw/640?wx_fmt=png)

以此类推，将马路换成了水面，汽车换成了船。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxalq1p2mKfdTYgCDC5ju4KWr3RvZicrdaLZ9QVnP7X0Z7ydyejYMZzFXToPsL01SIiaWMe8KBt3PEQ/640?wx_fmt=png)

将文生图的关键词修改为：  森林，河流，船。
在ControlNet中导入我们修改好的seg图，因为不需要预处理，所以预处理器中填入none。选好模型，点击生成。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxalq1p2mKfdTYgCDC5ju4KZicgM0wZ6zcfjV4NA7XGNMT4CtCwuRQm0YFLBFCWdricUkuAia40Vc4sw/640?wx_fmt=png)

一张符合原构图的森林风景画就诞生了。理论上，我们可以在色块图上做任意的调整，比如增删某个色块的面积，添加其他物体元素的色块，来达到随意布局的效果。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxalq1p2mKfdTYgCDC5ju4KeNjficQ6r3wJwICHrCvCc8C8UFuV68NZPCAyQY66YqDOr5Fzh1eunlw/640?wx_fmt=png)

**# 人与景的融合**

我们使用大模型“CounterfeitV30”先绘制一张公园的风景图，提示词为：((masterpiece,best quality)),no
humans, grass, outdoors, Stone bench,on ground, sunlight, dappled sunlight,
day, depth of field。

****

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxalq1p2mKfdTYgCDC5ju4KiatvqQrWajOGQAEM3XV6gkghuaApPgIj1TKgyNpRqrTZkA54Wx9lJ9Q/640?wx_fmt=png)

这次我们使用coco协议的seg进行语义分割，生成预处理器。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxalq1p2mKfdTYgCDC5ju4KicdBCicjf6CyOMeFHCD3xnSwBjhdA1yO0uhNXDngEgvHvvsBCR9LribZA/640?wx_fmt=png)

通过查表找到人物的颜色色值。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxalq1p2mKfdTYgCDC5ju4K0FlBAlIQiaFD4AicbtnoXFqGM8Gf1dVAeVeLNKssYBwUCPNMiaIy5qe0g/640?wx_fmt=png)

通过ps抠一张坐着的女孩的图片，按照色值填充成剪影，放入到图中，保存成一张新的seg图。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxalq1p2mKfdTYgCDC5ju4KHPhicUt3H0BtAmuCtTl75Fj6TaNicjh00KLicuXuVd3PMicmCb9pS24iagg/640?wx_fmt=png)

添加女孩的文字描述词：白色短发，白色裙子，坐着。  
点击生成，因为添加的人物只是剪影，AI很难识别出真正的动作，所以很有可能会出现姿态错误。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwyclu9q0t5G5Dcgkgyu5ehciarHwvO4Fl6WGqiaQHGVfpwiciaZ4rhAnZ5yqtxIulB7nOeUEaDGib3PUwA/640?wx_fmt=png)

此时，我们可以进入  之前讲过的  “  3  D  openpose  ”  插件（  [ 【Stable
Diffusion】最强控制插件ControlNet（2）姿态约束
](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247486330&idx=1&sn=b60f9e57b6260894e14cae7b1dc7e68e&chksm=9fbecb8ea8c94298eb4ca3ef8a3dae90d468610ff84eb10c0b6203b747fddda89605c3003f65&scene=21#wechat_redirect)
）来  增加一个  人物的骨架约束  。  打开  “  3  D  openpose  ”插件，
首先要设置好背景图片，这样就能对应着调整骨架。将刚才生成的图片放进来，然后点击“从图片中检测”，就可以得到大致的骨架，然后自定义调整一下，摆出自己想要的姿势。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxalq1p2mKfdTYgCDC5ju4K1GficqXn2kNkuDRJeTKTdzU13nU7JhYs11U3bsNC6zNG3w0KBc7v5ZA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxalq1p2mKfdTYgCDC5ju4KUFcuE76ibXCymPwGo6wvd0JQoqUOFTorZFkTDaYuawLibdejkmO0wbqg/640?wx_fmt=png)

生成的骨架图发送到  ControlNet  中。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxalq1p2mKfdTYgCDC5ju4KnoasUgegcickiajhetN47g5eR0Gn6dbTDjw9fdFticoEO4z7x4Sz9aFow/640?wx_fmt=png)

此时的  ControlNet由三个通道组成，一个seg通道做构图、一个renference定义风格、还有一个openpose骨架定义人物姿态。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxalq1p2mKfdTYgCDC5ju4KqAemX4y84mcW69H9wKujdjicFibEj9fll0FbvxXNT3JBibMiatmpic7iaYMw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxalq1p2mKfdTYgCDC5ju4KbQN1d0f4HVt37cG8ZBDgW3fa4PicprkPsyUwed4GUF7VCbrwibibEEkicg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxalq1p2mKfdTYgCDC5ju4Kkz1mA36MicVFJYeGWmUH1587pzXO192dHWOmBtCRiceAGsIbcBeOXhtA/640?wx_fmt=png)

再次生成，人物的姿态就比较正确了。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxalq1p2mKfdTYgCDC5ju4KdkjVkCAf0Dz1IibSr12MNAAfAaTkYhhZLHiaK5a4suPiar7QDJZjejL1Q/640?wx_fmt=png)

接着发送图生图，启用  ControlNet  中的tile模型，拉高重绘幅度到0.85，做进一步的细化。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxalq1p2mKfdTYgCDC5ju4KbAcasNibXUibbC4pvYz6BCfE9SwpbvdvXwBPGT0IZhAwZF5vlaWIMYzQ/640?wx_fmt=png)

完工，画面整体还是不错的，可惜手部还是出现了一些问题，有的时候确实单靠AI很难调整过来，所以当AI完成百分之九十工作之后，剩下百分之十的细节调整还是需要靠后期PS来完成。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwxalq1p2mKfdTYgCDC5ju4KgNbSXO7pLe4eVJPhiclmmyJKvsV7gY6mJ1ibs4gxNn4YnskEtia2CNLMw/640?wx_fmt=png)

好了，以上就是ControlNet插件当中语义分割seg  的用法介绍  ，可以通过这个功能，完成我们自定义构图的梦想。
一个色块就是一个元素，我们离神笔马良又进了一步。  
如果想要  语义分割的色彩对照表格  的话，可以添加我的公众号【  **白马与少年** 】，回复【SD】即可。  
喜  欢的话  ，可以  点  赞  支持一下哦~  

预览时标签不可点

微信扫一扫  
关注该公众号



轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicFrWhQnGuwdp4icKgCxibWO94LTgVCdyGEa5tticq3VQ0wbSfnGkl6ficicgn1LmHvKohOIT76T3un55Q/0?wx_fmt=png)

白马与少年







****



****



  收藏

