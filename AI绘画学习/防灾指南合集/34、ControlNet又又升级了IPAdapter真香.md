![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At7e1xe7TRU1hRsrnT8HndcIDv31dONPuMQEBXJJVntfqibUsuCXE9SXtHbNHAKgGKSoYnAatylwLqw/0?wx_fmt=jpeg)

#  ControlNet又又升级了，IP-Adapter真香

原创  暴躁的卡爷  [ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

我好像不是一个追新的人...ControlNet都已经更新了好几个版本，我才敢小心翼翼的点下更新按钮，下载新的模型，下载新的预处理器...
是的，CN足以让人杯弓蛇影。  毕竟CN1.1大版本当时与segment不兼容卡住了我很长时间。

等到大家已经验证好了，CN的几个新增功能真香，我才敢在电脑上点下那个更新按钮。（生产力插件真的需要谨慎更新）

好！今天主要给家介绍这个e4fbb1b版本上增加的模型，IP-Adpter！

  

** **▍** ** IP-Adpter  ** ** ****

这是一个来自腾讯AI研究院的项目IP-Adapter: Text Compatible Image Prompt Adapter for Text-to-
Image Diffusion Models。

文档就不严谨的啃了，大概就是 **图片转化为提示词** 与文本兼容完成文生图。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7e1xe7TRU1hRsrnT8HndcIFfOKAhia4dOL0tnH7naeQBtLfF5pIvbaziaInmZNTFNDSG2P7kGibia7DQ/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

主要官方很重要的更新都是围绕SDXL_1.0来的。这是否在暗示我们，别再折腾你那破了webui1.5了，和过去趁早说再见，和前任不再有瓜葛。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7e1xe7TRU1hRsrnT8HndcIEkEPibaFd1USnicTvTIz8ckpRGQHiaaNAlEJCdZvoLqQ66EAooN3evtwQ/640?wx_fmt=png)

可惜，我偏不！！！我就只用1.5，有本事你们都别向下兼容了。不还得乖乖发1.5的CN模型嘛。新提供的预处理器模型兼容SD1.5和XL，同样ControlNet模型也包含
SD1  .5和XL。因为没有升级webui1.6 所以，我也就放弃了XL部分。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7e1xe7TRU1hRsrnT8HndcIiaByLK0VpvqG4YibTsPuPSykHv78nSzIAWCfCPKRLhIhrFEeroCb9lEg/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** 下载和安装  ** ** ** ** ** ** ** ** ** ** ** **
**

先把模型下载方式放出来 WebUI 》》》

https://huggingface.co/lllyasviel/sd_control_collection/tree/main

另外官方很贴心的为ComfyUI玩家也准备了可以使用的插件》》》

https://github.com/laksjdjf/IPAdapter-ComfyUI

通过上面huggingface的链接，可以找到CN更新的众多模型。文件名带有XL的就是专门为XL提供的，有大有小，与我无关。我们只要载明找到ip-
adapter的这两个文件就行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7e1xe7TRU1hRsrnT8HndcIXSYOpoIM8VgUKCtZgePzBFXq4w3Ke6lzBXRSk8mC5Y0bPsuFbkcNZg/640?wx_fmt=png)

考虑到plus版也没多大，所以就只需要下载这个plus（更精细），并放入你的SD文件夹下\models\ControlNet中。  

然后记得更新你的CN到  1.1.400版以上。就能在预处理器里找到
IPAdapter的选项了。不要急，预处理器里没有模型也会报错的，你可以在文末下载中获得2个预处理器模型。（很大，一个3G+一个2G+
要有心理准备和硬盘准备）  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7e1xe7TRU1hRsrnT8HndcI7Ozy3BLgGQOwWWOoUZLtaxZbcicueGMFl5b0DZlLqQficWQMON6gqkpA/640?wx_fmt=png)

把他们放进下面目录中，安装下载部分就完成了。  sd根目录\extensions\sd-webui-
controlnet\annotator\downloads\clip_vision

  

** **** ** ** ** ** ******** ** ** 如何使用  ** ** ** ** ** ** ** ** ** ** ** **
**

其实看到我上面高度提炼的解释很快就知道这个“真香”的CN模型怎么使用，就和CN官方的那些模型一样，可以单独，也可以混入工作流中与更多CN单元组合创造很多好作品。

最直观的使用方法就是不再需要反推插件了。tagger哭了，我还没来得及介绍这个必装插件，它就没有必要存在了。甚至对很多人来说prompt输入框也没用了。
![](https://res.wx.qq.com/t/wx_fed/we-
emoji/res/v1.3.10/assets/newemoji/2_05.png)

来看官方演示：  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7e1xe7TRU1hRsrnT8HndcIvq3eTB0He9o5KnGOrIyIske7XCQicFoGSX88ZNxACiaR8lEg5NCbZdvg/640?wx_fmt=png)

  1. 一张图，在不同模型下的不同效果，完全替代文字prompt   

  2. 图生图，输入image prompt 进行了有如藏图一般的CN效果。 

  3. 局部重回输入image prompt 后配合遮罩完成换脸。 

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7e1xe7TRU1hRsrnT8HndcIp8eDWAe9BPvYkHDMsOs7W4NicLPwfG1FsABbL72aTYXdawYiauexGbbQ/640?wx_fmt=png)

配合depth的CN 单元，大卫也能变成戴珍珠的石膏大卫，和🍓形状的海岛。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7e1xe7TRU1hRsrnT8HndcIo3CicypQY7Y2aLlFX5TKQ4xICkFozNpDvtEGyztsYQS0eEN9wmjibncg/640?wx_fmt=png)

image promp  t 配合文本框输入的prompt，还能实现给图片增加细节元素的功能，这个真是太赞了！
![](https://res.wx.qq.com/t/wx_fed/we-
emoji/res/v1.3.10/assets/Expression/Expression_53@2x.png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7e1xe7TRU1hRsrnT8HndcIVw5qWk6lw9NiapicuyViaeGun76puiaHvYvCBIX6ickzSY78MEKEhuK5hTw/640?wx_fmt=png)

这个就更绝了，上一期我们还介绍了替掉roop的同门师兄插件FaceSwap Lab（需要的请传送门：  [ 安装麻烦的Roop，被FaceSwap
Lab全面碾压了（插件篇）
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247485721&idx=1&sn=f4470a2684c7cae1aecccde36bfa5a8f&chksm=97a43f28a0d3b63e56a197933247481a4213fc09fcf9aae528893b6d8dad852ae1e44659f90c&scene=21#wechat_redirect)
>> ）结果人家这也是一张脸，配合以前生图该怎么填怎么填，该怎么设置怎么设置，就能通过真实、二次元模型进行面部固定的生图骚操作了。

当然，官方肯定不忘推销一下他们XL有多厉害，与我无关 ![](https://res.wx.qq.com/t/wx_fed/we-
emoji/res/v1.3.10/assets/Expression/Expression_23@2x.png) 。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7e1xe7TRU1hRsrnT8HndcIEEKcwpMp7ibdenUFWs7WicCNEasDpN1kYglsldcG0zMXwnDNuic72JYTg/640?wx_fmt=png)

也补充了一下，新版本的Clip-Vit-H模型（这个是我们需要下载的）比老的bigG（也有提供）更好，体积更小，但效果不打折。

** **** ** ** ** ** ******** ** ** 最佳实践  ** ** ** ** ** ** ** ** ** ** ** **
**

如果你只使用图像提示，你可以设置  _ scale=1.0  _ 和  _ text_prompt=""  _ (或者一些通用的文本提示，例如:“
best quality
”，你也可以使用任何否定的文本提示)。如果降低CN的权重比例，可以生成更多样化的图像，你可以通过这个来调整与原图相似程度。（我认为这个操作性要远强于CFG强度调整对图片

对于多模式提示，您可以调整刻度以获得最佳结果。大多数情况下，设置scale=0.5可以得到很好的效果。对于SD
1.5版本，我们建议使用社区模型（finetune的各路大神的模型）来生成好的图像。

  

好了，别光说不练，光看不赞，随便上个过去的图试试吧。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7e1xe7TRU1hRsrnT8HndcI2y5wvulsJhaGu4YoQLHZOgdFY05alvGITbkrEiaYLgDbicMLnMm9ApPw/640?wx_fmt=png)

上图是我的image prompt，（感兴趣也可以反推一下），下面是我希望做的改变，和替换成二次元风格的模型。

** 关键词  ** (best quality),  mixed c  olorful hair,<lora:beautiful-detailed-
eyes:0.8>  
---  
** ** ** 设置  ** Steps: 30, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed:
497551718, Size: 512x696, Model hash: da86cc9d88, Model:
mixProV4MIXProV45Fp16_40, Denoising strength: 0.7, Clip skip: 2, Token merging
ratio hr: 0.2, ControlNet 0: "Module: ip-adapter_clip_sd15, Model: ip-
adapter_sd15_plus [32cd8f7f], Weight: 1.15, Resize Mode: Crop and Resize, Low
Vram: False, Processor Res: 512, Guidance Start: 0, Guidance End: 1, Pixel
Perfect: False, Control Mode: Balanced", Hires upscale: 1.55, Hires upscaler:
R-ESRGAN 4x+ Anime6B, TI hashes: "badimage: d70463f87042", Version: v1.5.2  
---  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7e1xe7TRU1hRsrnT8HndcI4jicrjmZCaUUcJQMmuyEBjY1bcHX9jBuRFDr89jGkcRY3qgsWjRuaBw/640?wx_fmt=png)

好了，这期就说到这。

  

  

** 最后  **

本期没有小伙伴友情演出。

如果对SD防灾对策群感兴趣的也可以关注公众号给 **【小鱼干了】** ，通过公众号的自动回复 **加群** ， **加好友** ，获得
**在线SD云服务** 等操作。  ****

本期文章提到的模型lora，可以公众号回复【下载】获得资源。

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

