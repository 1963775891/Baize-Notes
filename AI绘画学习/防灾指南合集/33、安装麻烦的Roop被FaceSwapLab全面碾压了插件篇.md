![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At6tEFfQvRMheF9Hibu6iauRmU713sAeKTPu8pr4icrgg7ffmF3bDibtzu4vQWicicUN4AW8ylqLGFVydBTA/0?wx_fmt=jpeg)

#  安装麻烦的Roop，被FaceSwap Lab全面碾压了（插件篇）

原创  暴躁的卡爷  [ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

这两天有朋友参与了一个AI商业项目，给某品牌的代言人做AI形象。做的是非常好，一下子把群里几个热衷换脸的点燃了，烧起了鸡血。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6tEFfQvRMheF9Hibu6iauRmUvibO6a1BziaXh0eeYEBak0mHGLVLQLo3vhmAphmoVLCmRnfWrt3DkP9Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6tEFfQvRMheF9Hibu6iauRmUzZG9qP2LCwuLuviblxZRkNVsg3yjAGia9z0PibzS2vOAUY19vNO05sicoQ/640?wx_fmt=png)

于是...
有暴躁鱼干在线SD用户悄悄跟我说：他们这个炼lora，搞修图，巴拉巴拉一大堆，我找到一个神插件，比你之前推荐的roop强得多，你给爷装上，爷现在就去撸两个宇航员刘亦菲！

说完他就发了2张他自己换脸的图给我，我一看我去，还真行！很强。立马现学现卖了，啃了一下午官方文档。  

**网站上有一个很醒目的免责声明和许可，对阅读这篇文章的同样适用：**

  * 道德准则：  由于性能问题，NSFW 现在可以配置。请不要用它来恶意伤害他人，更不要做违法乱纪的事情。 

  * 许可证：  本软件根据 GNU Affero 通用公共许可证 （AGPL） 版本 3 或更高版本的条款分发。 

  * 模型许可证：  该软件使用InsightFace的预训练模型，这些模型仅用于非商业研究目的，如果看到有相机类应用使用，请狠狠举报吖的。 

  

这些很重要，一定一定要提前知道。之前roop的文章传送门：  

[ 违法乱纪的事，我劝你不要干！用ROOP（插件篇）
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247485189&idx=1&sn=d1e34db491dbb7b4a744868392f0b6ad&chksm=97a43134a0d3b822de767ee01d4fc498fef7fb3ede6e88f220aeae66ed9a7d0da4c7fc1f8db5&scene=21#wechat_redirect)
>>  

  

** **▍** ** FaceSwap Lab  ** ** ****

** **** ** ** ** ** ******** ** ** 下载和安装  ** ** ** ** ** ** ** ** ** ** ** **
**

1\. 其实所有能在扩展中搜到的插件安装起来都很简单。并且大部分优秀的插件都能通过  **
扩展——可下载——点击加载扩展列表——搜索关键词(如faceswap)  ——找到  ** 。

2\. 你也可以通过github的url, 从 从网址安装——粘贴url——安装  

https://github.com/glucauze/sd-webui-faceswaplab

3\. 最后如果你的网路环境真的太差了，还是老办法，你从文章末尾提供的下载方式中，把插件直接下载，并安装到SD目录中的extensions中。

  

** **** ** ** ** ** ******** ** ** 使用  ** ** ** ** ** ** ** ** ** ** ** ** **

插件还是十分复杂的。安装最好开科学的网络使用工具，首次使用会在好几个文件夹下载不同的模型，这也是我不直接提供模型的原因，会在sd的模型文件中生成一个目录并下载一个模型文件包并解压，还会在C盘的一个特殊目录下下载一个模型。总之，比roop的window环境安装起来还是容易太多。

安装好之后，会在生图设置页面下多一个设置项，对，和ControlNet在一块，且和CN一样会有好的把当前版本显示出来。（最近骚包选了个主题，别说不认识界面了
![](https://res.wx.qq.com/t/wx_fed/we-
emoji/res/v1.3.10/assets/Expression/Expression_42@2x.png) ）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6tEFfQvRMheF9Hibu6iauRmUdVttmQBuc3iczRIicG3c3WU02WKgnCoYRfEaKLG3kryu0AW1zVzPE7Qw/640?wx_fmt=png)

对这是局部，这个插件展开是这个样子的！而且，顶部tab上还有一个专属的页面，里面藏有更多的功能。 但别被吓到，
**我会略过这些麻烦的部分，直接讲最简单的如何进行脸部替换** 。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6tEFfQvRMheF9Hibu6iauRmUaKupfCjM4anL8B5wHEe56TibqNVsAzgEmYylNVOibRwDicfj8yjTzWKPw/640?wx_fmt=png)

###  **Face Unit 脸部单元**

与我们熟悉的CN的工作逻辑也是一样，每个替换脸部都有一个脸部单元，如果要使用，需要勾选启用。

  * Reference: 这是主要放入图片的地方，从图像中提取人脸并用于人脸替换。下面这个选择脸部模型可以不用管，那是快速炼人的进阶玩法。 

  * Batch Source Image: 除了单独传图外，还能用这个进行批量传所需替换的参考图， **这也是这个插件最牛B的地方，更多的参考意味着替换得更加自然** 。（但需要选中下面的“Blend faces混合面”，这些面将通过平均特征合并成一个面。如果没有选，将为每个面部创建一个新图像。） 

  * Blend Faces : 上面有说这个默认开启的勾选框会帮你将批量上传的参考图根据面部特征混合成为一个。 

你必须至少有一一个参考面部，或者脸的模型（今天不聊），如果都选择的话，会优先选择checkpoint的脸部模型  。

这就是今天重要的部分。很简单

  1. ** 不论是进行文生图，还是图生图，勾选启动脸部单元。   
**

  2. ** 往脸部单元里上传一张参考图（至少），也可以往右边的批量上传传更多的不同的参考图。   
**

  3. ** 点击生成。（图生图需要调整图片重绘幅度）   
**

  4. ** 完成！  **

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6tEFfQvRMheF9Hibu6iauRmUc4Hny1QVqD8cXfbo7yOqPe1Vnz3nlHBUIXZrWJuqH9RxViaXmKmwQcw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6tEFfQvRMheF9Hibu6iauRmUian7VfwnvbbBiaJF82pJFbZvVAoxlzU9je2dt1XHGK7UzcwdHFNiaBibKQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6tEFfQvRMheF9Hibu6iauRmUgDcogsDLuHJy9RmU3MhZxjyANEZxKDn7v7QB6RBHBcRsw8td7PAM4w/640?wx_fmt=png)

官方演示视频放入了一张爱因斯坦的照片，关键词输入portrait of a man，全局设置里保持面部修复算法为Codefomer
就能得到最后的带有爱因斯坦面部特征的一张人像了。

好了！补充一点其他吧。

** 高级设置  **  

如果你觉得脸部特征还不够明显的话，请跟着我操作一遍。

仍然是先启用插件，上传爱因斯坦（可以是多张）到参考图中。  

将启动下面的2个勾选框都选上。他们分别是相同的性别，按从大到小适配

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6tEFfQvRMheF9Hibu6iauRmUaaiamva1Rnw7hfic0wd6micRmZ8FEA8iagzE8ibKOGVHUTQRLAl7iaPxoHIA/640?wx_fmt=png)

在底部高级选项中，选择Post-
Processing和高级遮罩设置中选择面部修复。并选择放大算法。官方推荐003_realSR_BSRGAN_DFOWMFC_s64w8_SwinIR-
L_x4_GAN （我会在下载中提供，但我觉得常用的4x好像也ok）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6tEFfQvRMheF9Hibu6iauRmU7NrDe9VHRuuWsMZfmzKQAuUx36Lz7Vd4RPFftSxXGxmCcvVYgDs6kA/640?wx_fmt=png)

然后要把上面步骤教你的在脸部单元的  ，全局设置里保持面部修复算法为Codefomer关掉。再点击生成。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6tEFfQvRMheF9Hibu6iauRmUUugzqaoFad36eRM2rWP16aKd6Zmw36ibHasbrMTF3xlm77wqdAoT3Bw/640?wx_fmt=png)

我们会获得一个脸部特征的细节更丰富的脸。对比一下，右边是进阶的会更像，细节更多。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6tEFfQvRMheF9Hibu6iauRmUCziaHEKg0z33llrMKEtHjOibjjiaxHaE6kfSH5wgEtPhyjK43t2xmicueg/640?wx_fmt=png)
|
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6tEFfQvRMheF9Hibu6iauRmU7svZ3OnMD6ExMzD2jnYzlHRutp98jw3N9Y5rNtyaBEkkwla9ic3QumQ/640?wx_fmt=png)  
---|---  
  
以及还能通过inpaint的方式进行脸部替换；图生图的方式进行脸部重绘替换；多人多面部替换；等一系列功能。

感兴趣可以自己继续研究一下吧，篇幅有限，我就先介绍到这吧。

  

** 最后  **

感谢本期小伙伴的友情演出。

本期提到的插件  ** 在线  ** 云服务  ** aifish  .vip  ** 就有提供，登录  就可以使用  。

如果对SD防灾对策群感兴趣的也可以关注公众号给 **【小鱼干了】** ，通过公众号的自动回复 **加群** ， **加好友** ，获得
**在线SD云服务** 等操作。  ****

本期文章提到的插件，可以公众号回复【下载】获得资源。

  

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

