![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rR335dShxibibA3ibdbFtbNCO28ib12oCibOI8JZRzEdmOliam2BkZf6bLyVXNibuo5UHAeXibdktquKXW0ZrC9sQEbFKA/0?wx_fmt=jpeg)

#  【Stable Diffusion】来了来了！属于SDXL的ControlNet模型它终于来了！（测评）

原创  吴溪源  [ 白马与少年 ](javascript:void\(0\);)

**白马与少年**

微信号  StreamWXY

功能介绍  Stable Diffusion、Blender等学习心得分享

__ __

__ _ _

千呼万唤始出来！就在昨天，  WebUI
的ControlNet1.1.4版本终于更新，这次的更新支持了SDXL1.0的模型。我怀着兴奋的心情，打开了网站开始下载模型。这次总共出了四种控制类型，分别是Canny、Depth、Sketch和Openpose。

来到Hugging
Face的网址：https://huggingface.co/lllyasviel/sd_control_collection/tree/main。可以看到这里有相当多的模型，当然，我们不需要全部都下载下来，因为它们之间有很多功能是重复的，是不同的作者做出来的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOInu8XpSpqSIK8eMnDRPIGwUPfptahFRD7iccys60glVsHxObeZaiaBh8g/640?wx_fmt=png)

但是呢，  为了帮你们提前踩雷，  我把他们全部都下载了，而且逐个做了测试，看到我这么辛苦的份上，你们一定会要给我一个“点赞”和“在看”的吧。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOI9LDiaWsksVib9fw2iaK9ARolrfzEWVor3h4aZByZbVzKakiboymA7MG7Jw/640?wx_fmt=png)

接下来，让我们来分类看一下吧。

** #Canny硬边缘  **

首先是canny，它有几个不同的型号，体积越大，速度越慢。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOIKh3Huz9J1rfXib1gWtaiaTvWdoib4AQapmsjk5UkiaxI0k0WLrFicziaz9ibQ/640?wx_fmt=png)

我使用的是4080ti的笔记本进行的测试，12G显存。

  * 模型sdxl base+refiner 
  * 提示词：masterpiece,best quality,1girl 
  * 采样方法：euler a 
  * 尺寸1024*1024    

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOIUm7PL6cCX0lS2BJWJqwDTE4oQlFqUl4cU9fwLKh2SHhHbGsX91Ec1g/640?wx_fmt=png)
使用diffusers的2.5Gfull模型绘制的图片，一张图花了2分57秒，从这个效率上来看，这个大尺寸基本可以弃了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOI1bVJib6b2xBTCf550U8zZA3WZ4wGBoFmia1Gzjldj2E2WwuF8iavql2gA/640?wx_fmt=png)

使用  diffusers的  320Mb的small模型，用时34s，质量上差距不大，主要是时间优势很明显。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOI4oOjrzkHnnDf9awWzLhHVVtH9uuZyYKGK08vibYfFBibTPeyb7FNLjyQ/640?wx_fmt=png)

我们可以再看看其他作者的，这张是kohya的，用时33秒，更接近真实质感。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOIxebcRS5iakybBPrXbvxCdib600L2qsAOc6FwMrq4tpJV1b2DZRTye2MQ/640?wx_fmt=png)

sai的canny分为128lora和256lora，分别用时39秒和1分08秒，这个模型比较偏绘画的感觉。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOIpLuRAWTEyRwLvXHTdC7TcdhchwSZ2j4Q4iaWqeBW1IK08usF3l3uTXw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOIlE8xwWb8r3jwC07ZSZkmOJDEczmSoicBAQajbaUyicyExyu87vnmb6lQ/640?wx_fmt=png)

最后还有一个t2i的canny模型，用时34s，也是偏插画一点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOIOsmG68mSSD9TNJ1oSJyosKZ6ldd1B0NSznEquc8FfnZTSSUwUMnC3A/640?wx_fmt=png)

你们觉得哪个效果更好呢？时间上基本都在30秒以上，如果关掉refiner的话，能节省一半左右的时间，平均在17秒左右。  
** #Depth深度  ** 接下来测试一些depth模型，图形尺寸664*1024。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOIJR6r5D0QFEic4Bo7XCT1VMmjvCjkIstL1tMSRWibw3y6UzafUQDcwHBQ/640?wx_fmt=png)

使用  diffusers的full  模型  ，用时  2分48秒，sdxl给我随机到了一个拼贴画的风格。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOIMQkDCg3S7Quib91xhCdxic5UPH3ssQkCW925E1Y2icausKjEMHP9clI1g/640?wx_fmt=png)

使用  diffusers的  small  模型  ，用时  23s。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOI66plicoic1WCmDRAToNYHB6pcc6kuASgibRzRoJpPy1iaRrsh1TAm6HLQA/640?wx_fmt=png)

使用  kohya  模型  ，用时  42秒。这……好像和我的图片没什么关系。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOI58LpExHFm6VDicwVGYGicYMV3HEYInbU9CtUbRueTJ7icelPLnsiajJG0A/640?wx_fmt=png)

使用  sai  模型  ，用时1分1  2秒，画质还可以，稍微有点慢。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOIS2WcSbRbaOhFUibKpWLibUtdfuelwWNSMiaw4gicwbOzjRKEMkDpXia79Tw/640?wx_fmt=png)

使用  sargezt  模型  ，奇奇怪怪，没什么关系，用时1分52  秒。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOIRBcUhrJ8XeJ8BCqibfsv0xlictuAA51uUAib9UUE2S4ZviatabvzIVMJ6A/640?wx_fmt=png)

** # Sketch草图  ** 接下来测试一下sketch模型，画一只可爱的小猫，图形尺寸1024*624。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOITDyBcBHYqwsPJ7OTMrQN79jc2AJJLrnbibtjGac81HFUPeENGxoMlxw/640?wx_fmt=png)

使用  kohya  模型  ，用时  30秒，这是个啥？？？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOIADcrwyIticfcxfoxOHVIpo0IibJiaXPjNxCnyl6JsZ33Lw6hxmUwzfugw/640?wx_fmt=png)

使用  sai  模型  ，没找到小猫具体的位置，用时  32秒，画质还可以。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOIxV3JQENgOPQO60ShlufFia7T2BH41SzcEETuCGLo552umVhRUzVUetQ/640?wx_fmt=png)

使用  t2i  模型  ，用时  28秒，唯一一个准的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOI8aZU0W3eX9cOhVLpIH7ZnicnZP505Ac0pJAeF2icV50AZraerftFvkZA/640?wx_fmt=png)

** # Openpose骨架  ** 最后测试一下openpose模型，图形尺寸1024*624。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOISSOWwKLeo94U4PibicRJuYfFt1oIylkJfEoH8LXb5lgDsf5C9hR7wP5w/640?wx_fmt=png)

使用  kohya  模型  ，画很好看，但姿势不对，用时  40秒。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOIvILOzlBte2r9bByUszcLiajLb1q0jB5xWHQsupKTOqkc1Wbtn0Z8auw/640?wx_fmt=png)

使用  thibaud  模型  ，动作有那么点意思了，但是时间太慢了，用时  2分12秒。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOICBZibjStDfsia3ic1c3om6wg0gN39JuHAFsWT21VmGqFy446zlkv3BRdw/640?wx_fmt=png)

** # 总结  ** 最后说下结论吧，没有权威性，全凭主观感受。  在canny模型中，我推荐使用  ** “
diffusers_xl_canny_small  ”  ** ，  出图快，效果也还不错；depth模型中，我推荐使用  **
“diffusers_xl_depth_small”  ** ，理
由同上，其实“sai_xl_depth_128lora”效果也不错，但是渲染时间太长了，当然这个不是模型的问题，是我的问题，因为我买不起那么好的电脑；Sketch模型中，我推荐使用
** “t2i-adapter_xl_sketch”  ** ，这是腾讯家出品的，起码还挺还原的；openpose模型中，推荐  **
“thibaud_xl_openpose_256lora”  ** ，虽然它画的不太准，但是它时间短啊，唉。。。
以上就是对sdxl的controlnet在webUI中表现的测评。  虽然  我的测评并没有很严谨（  客  观原因还是sdxl对机能的要求太高了  ）
，  但是  总体的成功率感觉还是太低了
。而且因为sdxl模型支持多种画风，所以在我的提示词中并没有给出具体要求的情况下，controlnet的结果是千变万化的。  
对于这次controlnet在sdxl上的表现你觉得怎么样呢？把你的感想写在下面留言区吧。  
我会把我觉得比较好的几个放在网盘里面，没必要都用了，占地方。想要完整测试其他的模型的朋友可以去官网下载一下，  关注我的公众号【白马与少年】，发送【
SDXL  】即可获取链接。  ** -END-  ** **  
** ** **

  

我的最新课程《Stable Diffusion零基础入门宝典》已经上架CCtalk，正在预售中， ** 前100名报名立减100  ** ，想了解的朋友
长按下方图片识别二维码，可以进入购买链接>>>

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rR335dShxibicWmbe9oYaryEicR9BouhhB701eVnt7WG0l9SzmNLOBxyicqGS4XNzUh7qbdKZZq1stDrOv1bAJYPRg/640?wx_fmt=jpeg)

* * *

  
往期精选>>  

  * [ 【课程】爆肝制作！Stable Diffusion零基础入门宝典  ](http://mp.weixin.qq.com/s?__biz=MzkzMzIwMDgxMQ==&mid=2247487870&idx=1&sn=7a425e50ccdfdc040b7fa285aad369c7&chksm=c25147baf526ceaca4de604a50d8b59d09920c7e4fe94223c3daa06ec337d18fc7ffb8e97e83&scene=21#wechat_redirect)

  * [ 【ComfyUI】本地部署ComfyUI上手指南，我就喜欢连连看  ](http://mp.weixin.qq.com/s?__biz=MzkzMzIwMDgxMQ==&mid=2247487895&idx=1&sn=aa21eede16dfe4bde7e0e93e353f7357&chksm=c2514753f526ce451175f654a93f48b526fc6de3e3b1564b218db41f7e3f99df5a84bb887043&scene=21#wechat_redirect)   

  * [ 一键切换不同画风，SDXL Styles汉化版插件 ](http://mp.weixin.qq.com/s?__biz=MzkzMzIwMDgxMQ==&mid=2247487817&idx=1&sn=cf8ccec5f2b974744b01d57cdb1e4d92&chksm=c251478df526ce9b16eb1a64dec74931ac17dd6e68ce9086102b9c33c8fd7dc6375795a0e8ac&scene=21#wechat_redirect)   

  * [ 向未来而生，关于SDXL你要知道事儿 ](http://mp.weixin.qq.com/s?__biz=MzkzMzIwMDgxMQ==&mid=2247487710&idx=1&sn=7f2b024f8377aff1c1b1822d155555f5&chksm=c251461af526cf0c74568effaefc6b285384ebadcb87e655fbfb41cb2ccad52e5d5f9193a687&scene=21#wechat_redirect)

  * [ Roop换脸插件，全网最简单傻瓜式安装教程 ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487776&idx=1&sn=836fdeb74a045f86a81c47056ef7adec&chksm=9fbed1d4a8c958c2565166dce7a521871c9a5ebfa141132a0eb3f53a65816bbc3c16b1a4e368&scene=21#wechat_redirect)   

  * [ 【Lora炼丹术】从零开始，炼制你的第一个LoRA（1） ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487751&idx=1&sn=dbc26500f9bda94fc09e1208864bb320&chksm=9fbed1f3a8c958e5b3853430fe79f9099d6962a4fd480fd6fff9f7fae3cd0ef933adf8637ac6&scene=21#wechat_redirect)   

  * [ 【PS】无需魔法！Photoshop beta 25.0一键安装， 中文提示词+神经网络滤镜 ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487520&idx=1&sn=7be16204847c820313d9909eee490508&chksm=9fbed0d4a8c959c2cf440e90b584aef5b55f8bec25071fe6980002ee090bfdad39cd91261b4d&scene=21#wechat_redirect)   

  * [ 最强手部识别，controlnet新预处理器dw openpose ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487676&idx=1&sn=43988fe6f8e6172707d62feb70412540&chksm=9fbed048a8c9595e745ed69acb2b699b802ac93f6e64c3270f6f1523eb214ed3edc156a891cf&scene=21#wechat_redirect)   

  * [ 超大尺寸绘制、分区控制，详解Tiled Diffusion & VAE插件功能 ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487605&idx=1&sn=e484f52f33a815fdcb12049742d46692&chksm=9fbed081a8c959977fac918147429f0f625eb1c2547fdf128196f97ac35c999b807ad9ddb083&scene=21#wechat_redirect)   

  * [ AI造字，把你的名字写在季节里  ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487476&idx=1&sn=074940028b8a295b22806ffad9181386&chksm=9fbecf00a8c94616f43d0b60fd06fbd201617f27725c4d7514c34fafe66f57dc40224ecb93b6&scene=21#wechat_redirect)
  * [ 隐藏在光里的秘密，AI造字光与影的艺术~ ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487455&idx=1&sn=362d5a02e23dfe19e1f3f0749ee1224c&chksm=9fbecf2ba8c9463df50a45ae0b25e35c510b01a166608205f78956a14a24cc571c66f6503a30&scene=21#wechat_redirect)
  * [ 隐藏定位点！融合度更高的二维码生成 ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487390&idx=1&sn=fe28a857f50661807e449f1c04400096&chksm=9fbecf6aa8c9467cdfde4c9b37eff054f279ff230524399b11702a4442db514bcb27009d24e7&scene=21#wechat_redirect)
  * [ 图片高清化+面部修复+一键抠图，一些你不知道的事儿 ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247487327&idx=1&sn=aad22a60028778b97bf00262f3a67883&chksm=9fbecfaba8c946bd29853ea9c15d90c03e2ac09ee4d22c27956bbcbcab3fa6c4551b5f599d03&scene=21#wechat_redirect)

  * [ 超清无损放大器StableSR ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247486854&idx=1&sn=e52870038dafc7518219660c90b1718b&chksm=9fbecd72a8c944647bb21f5e4546589295e5696a1f62601931080ccd4d29a1ec1230f73feb64&scene=21#wechat_redirect)

  * [ 如何画出商用级别的高清大图  ](http://mp.weixin.qq.com/s?__biz=MzA3ODY0OTc1NQ==&mid=2247486230&idx=1&sn=dde16ebbd5078661c21835c94db554dc&chksm=9fbecbe2a8c942f48cfe40eaea15ff963db9b4fe1c9a8aed330ee718bcf6720e491fc9237a7e&scene=21#wechat_redirect)

预览时标签不可点

微信扫一扫  
关注该公众号



轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicFrWhQnGuwdp4icKgCxibWO94LTgVCdyGEa5tticq3VQ0wbSfnGkl6ficicgn1LmHvKohOIT76T3un55Q/0?wx_fmt=png)

白马与少年







****



****



  收藏

