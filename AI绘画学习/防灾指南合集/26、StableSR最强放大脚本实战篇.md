![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At4r2M1nnTf6XulOzZNib42e4k8O9l5lCd82UpmhMZrn788GWla1YnZRxZvhT5MwHomsLsVthiaRDw0g/0?wx_fmt=jpeg)

#  Stable SR最强放大脚本！（实战篇）

原创  暴躁的卡爷  [ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

连着弄了2篇如何使用SD对生图或者手上的成图进行放大。心想SD就这一手的王炸，牌桌上怎么都是吊锤所有市面放大免费&收费软件，别说妈妈不用担心，姥姥都再也不用担心遇到图片该怎么放大了。

直到，昨天群里一哥们一边看着公号的文章一边在群里求助：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4r2M1nnTf6XulOzZNib42e4bjUicIZrPtc5DelUNQGxSyjGLNSHzElsr1bOrZqicfuYERibRWtr6Fib2A/640?wx_fmt=png)

我猛灌了一口速效救心丸...暗暗嘀咕。

** 还TM的得继续磕高清放大！  **

之前一直在整合包里看到这个脚本，Stable SR，但一直不知道是干嘛的，直到最近边学变用一些高清放大方法才接触了这个脚本。

才发现这是个宝藏，感谢赛博菩萨们把这个脚本整合进懒人包。  ![](https://res.wx.qq.com/t/wx_fed/we-
emoji/res/v1.3.10/assets/newemoji/Worship.png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4r2M1nnTf6XulOzZNib42e4Ukju7UGUMVOtbfQ3CxyQVWYG4RRV9jvZZgLLGfOEPfp6M7mUqGoupg/640?wx_fmt=png)

** **▍** ** Stable SR 喂饭  ** ** ****

Stable SR 全称stable super resolution,由坡县的南洋理工大学s-lab发布的高分辨率解决方案（官方说是主要服务给真实世界
for Real-  World Image Super-Resolution），论文啥的我也不啃了，你们也没兴趣看，贴个链接给有心人。
https://github.com/IceClear/StableSR
先定义一下高清放大，上一篇文章我们介绍了如何把模糊的小破图进行放大重绘，注意关键词其实是 **重绘**
，利用AI模型将我们需要放大的图片再画一遍，所以对于改风格，换材质，添油加醋是一把好手。但是生活工作中我们会遇到很多图片场景，只想原汁原味的 **复原**
图片，哪怕是上一篇的红莲甲，也是努力去找到相似的模型画的像一点罢了。  （没看过前两篇的可以点下面链接）

[ 我生成的图为啥糊的一批？（插件篇）
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484870&idx=1&sn=13e7f0437b09c7dc5ad9ad7fabcf62de&chksm=97a433f7a0d3bae1d2867a5011fb2f952da46a6e60cd1863af0d41ac5551f1afdf0a04c956b4&scene=21#wechat_redirect)

[ 冥土追魂“马赛克”，SD高清（实战篇）
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484918&idx=1&sn=0c984e89cb2bfab5dfcd6ddffab1ffb0&chksm=97a433c7a0d3bad1eccbc3474820ee48b333bf6c02e9875020970fa0f5dc97d81a50a336e192&scene=21#wechat_redirect)  

而Stable SR + Tiled Diffusion，可以完美的把图片原汁原味的放大。4k也不在话下。废话不在多说了，先看效果，然后  直接  实操一遍
。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4r2M1nnTf6XulOzZNib42e49C9W4aKcwljBo29dB3qZpzicrTxD2e06Iibukb5kEfZxtRjibSJGMb86Q/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** 需要准备  ** ** ** ** ** ** ** ** ** ** ** **
**

使用插件前有些东西需要准备。如果你没有，我会在文末提供。

  * StableSR插件下载。由于主流懒人包都自带。拓展里也能搜到。 

  * 插件中有一个起作用的小模型(约400MB) ->放 **插件自己** 的模型目录中。   

  * 官方SD2.1模型，Stable Diffusion V2.1 512 EMA 模型 (约 5.21GB) ->放 **基础模型** 目录中。 

  * 官方模型伴有一个官方VAE（VQGAN VAE 约750MB) ->放 **VAE模型** 目录（非必要） 

  * Tiled Diffusion & VAE 扩展插件这个之前介绍放大插件篇就提到过的魔王插件，这里主要用来解决超大分辨率显存不足的问题配合使用（非必要）。 

  
** **** ** ** ** ** ******** ** ** 开始放大  ** ** ** ** ** ** ** ** ** ** ** **
** 先随便找一张图，它不是真实世界的，用它也是为了证明放大这种也可以，这张图分辨率是600x410，能看，但不够精细。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4r2M1nnTf6XulOzZNib42e4760ia0rwas1MhFnv4PaNNvy6RdBVY6PDEqTeAphnHEcN5MP8LC9M5BA/640?wx_fmt=png)

使用起来十分简单，  主要步骤：

  1. 基础模型选择刚才下载的  v2-1 512-em  a-pruned  模型，如果下了VEA也可以挂上。 

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4r2M1nnTf6XulOzZNib42e42HICekMuEuvCVlEO1u7D3akRNQL99ldQicC4J0sJfm1GHZD1Njpg15g/640?wx_fmt=png)

  2. 切换到图生图（img2img）标签。  在参数设置底部找  到“脚本”下拉列表，选择 stableSR 脚本，SR Model选择...只有一个选（没有的去下一下） 

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4r2M1nnTf6XulOzZNib42e4EQ4HhgvQaGH0CS1Oq5jEuK9Tcrh9NphibCXdta6aia9VFIiasP67Wsyag/640?wx_fmt=png)

    1. 放大倍率：根据图片原始大小选择。这里我选了8倍，目标4K。 
    2. Color Fix：是图片色彩修复，有2个选择，色泽浓郁选AdalN，清单一点选Wavlet。   

    3. Save Original:字面意思，保存原始，不用勾。 
    4. Pure Noise: 勾选后无视去噪强度，怎加图片细节，一般建议勾。 

  3. 开启TiledDiffusion&VAE，这里主要用降低显存门槛，毕竟放大8倍。另外实测Tiled的设置对结果有很大影响，包括倍率。照做就行，重点划线。 

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4r2M1nnTf6XulOzZNib42e4B8zKDIBw0RT6qUHDHUEaQbKEkhG851gewsSZGmDPjwMicibdIibylrPDw/640?wx_fmt=png)

稍微等一小会儿，就能出图了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4r2M1nnTf6XulOzZNib42e4NU5ibPyuIkOARhxLTiam7FRHqF0uRSPSciaDGsZ8Tfbib8GRPEoZYNDSNA/640?wx_fmt=png)

SR会贴心的出2张，一张压缩后的jpg，一张原始的png。一张4k原图得16M一张，还是很贴心的。

对比一下，操作简单，关键词和设置都不用，最强放大坐实。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4r2M1nnTf6XulOzZNib42e4l6Udbq9Rwj3OBabED8Ry2gsYX3OGNbJwaIqA74XJomFryxyxib2eGDg/640?wx_fmt=png)

  

最后贴一下这三期讲的主流放大方法的优缺点：  

  * Tiled Diffusion + StableSR: 出图清晰度最高,细节最丰富,但速度慢,需要下载大型模型。 
  * Tiled Diffusion + ControlNet Tile: 速度最快,但出图有轻微模糊感,细节令人眼花缭乱。 
  * Ultimate SD Upscaler + ControlNet Tile: 速度中等,效果与前者类似,但在纯色背景下易产生缝隙。 
  * Tiled Diffusion + Noise Inversion + ControlNet Tile: 出图整洁,但速度慢。   

  
如果只用  Tiled Diffusion放大8倍，会得到这样的图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4r2M1nnTf6XulOzZNib42e4JlGP2YLwrjrjy5CyrxuBL9F8v5mdut22L2ibA2NkuO1d3LkH75ict9JQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At4r2M1nnTf6XulOzZNib42e4Jo6nWGvvt4ZgFOw7m7jwHGBfyFX3iaffJjZVI7SII8xzpVILSIiclqGw/640?wx_fmt=jpeg)

OK，绷不住了... 下期见...  

如果对SD防灾对策群感兴趣的也可以关注公众号给 **【小鱼干了】** 私信微信号，我看到了会加你，拉你们进来一起开放，学习，共同进步。

文章中提到的插件和模型资源，  公众号回复 **【下载】** 即可。👇关注公众号，获得免费在线SD。

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

