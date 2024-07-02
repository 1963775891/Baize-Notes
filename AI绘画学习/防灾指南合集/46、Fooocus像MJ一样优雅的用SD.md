![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At4LgLibrkWZEiceWbLJa4ZMb4jRDypaabyNAt2oUJUYkpkFcpdbUclG5yfLp9g5rHATiaw3299EH3R1w/0?wx_fmt=jpeg)

#  Fooocus：像MJ一样优雅的用SD

原创  暴躁的卡爷  [ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4LgLibrkWZEiceWbLJa4ZMb47ubBhQicicfZ8dRjTcZe3RfeCOoVmCwDhS7LSHGDgVKqKMJz95lE4XJA/640?wx_fmt=png)

最近防灾群里流行三种病，一种叫“口癖”是“出教程”。第二种叫表情是“喂我”，第三种是:“义父在上”。而且这三种病以迅雷不及掩耳盗铃儿响叮当之势迅速的蔓延开来。先放一张图，文末我再补充一个彩蛋。  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At61wL1mROM4TKJzwrJHvicbGywZL8RVawdsHVB52icSdkurYBtoE8KvVZEOh7bklkvRHnWQzGvPuYLw/640?wx_fmt=jpeg)

不过，大家聊到了fooocus，看到这个名字奇怪的东西出的图又十分惊艳。所以今天我们就来盘一盘这款工具，虽然它出来了有一段时间了。

  

** **▍** ** Fooocus  ** ** ****

Fooocus
的出现还得说SD－XL，因为XL的模型相比sd1.5来说太大了，对硬件（显存）要求又高了一个档次！8G显存的电脑发出了不争气的哭泣声。于是我们的Controlnet
的作者 lllyasviel 发布的一款全新的开源 AI 绘画工具 Fooocus。

作者在GitHub文档里说：Fooocus是对稳定扩散和Midjourney设计的重新思考：

  * 从稳定扩散中学习，该软件是离线的、开源的和免费的。 

  * 从中途学到，不需要手动调整，用户只需要专注于提示和图像。 

  

与WebUI相似，都是使用了Gradio组件开发而来，而与WebUI不用的是，它的界面长这样。对，只有一个输入框+一个生成按钮，如果你没有看到那个
Advanced的话。也恰好印证了作者希望将SD结合MJ降低AIGC门槛的思想，只需要输入几个关键词就行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At61wL1mROM4TKJzwrJHvicbGicw4EZBpNX55Xo4vtiaiaOxYK5A4Ow4TKwkbCx6DcjFhZIAFIFbNaR9Yw/640?wx_fmt=png)

那我输入下面的关键词，随便跑一张，效果果然还是很不错的。主要利用到了SD-XL的特性，不再需要输入质量词起手。

白猫，一只带头盔的猫，赤壁，超级可爱，俏皮，海军蓝的背景，开心的表情，宇航员头盔

** 关键词  ** white cat,a cat with a helmet,chibi,Super cute,playful,navy
background,happy facial expression,astronaut helmet  
  
---  
  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At61wL1mROM4TKJzwrJHvicbGDxhNb5WPicwEdricY3FAiaU2eA8jQGDicuCXuFibzNpU6bYoQDTeQpc8vxQ/640?wx_fmt=png)

** **▍** ** 高级选项  ** **

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At61wL1mROM4TKJzwrJHvicbGibcibtXCXwkQO3njdglSUdGGRExYMSZnxUDiclu02ZJJge3xsShU4y2Gg/640?wx_fmt=png)
|
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At61wL1mROM4TKJzwrJHvicbGbSsbtIOGLdc8VrWwshObM27wib1BqdpmflSwLiaWPhjlzXFOsxbVUUBQ/640?wx_fmt=png)
|
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At61wL1mROM4TKJzwrJHvicbGBwGQ4ib50C9WE8sQXB05hd50xpcmd1iaEnKJIes6dQGFnmBTiaDEDcyAQ/640?wx_fmt=png)  
---|---|---  
  
当我们勾选高级设置之后，会在图片生成区域旁多出一个功能设置区域。有三个tab，分别是设置，风格，高级。

** ** **** ** ** ** ** ******** ** ** 设置  ** ** ** ** ** ** ** ** ** ** ** **
** **

这里可以  选择生成的图片的质量高低（质量，速度）。以及一大堆生图的尺寸，是的，你没听错，只能选择，不能自定义。（很烦），还能补充反向关键词，  ，出图数量
和种子数。（好评）。

** ** **** ** ** ** ** ******** ** ** 高级  ** ** ** ** ** ** ** ** ** ** ** **
** **  

先说高级是因为我要把style风格留在最后。 ![](https://res.wx.qq.com/t/wx_fed/we-
emoji/res/v1.3.10/assets/Expression/Expression_29@2x.png)
高级设置给了fooocus战未来的可能性。因为这里可以切换模型，以及补充lora。熟悉webui的同学对这个肯定不陌生，finetune的模型和lora才是sd强大之处。至于还有一个采样清晰度，我也没严谨的测过，就不提了。

** ** **** ** ** ** ** ******** ** ** 风格  ** ** ** ** ** ** ** ** ** ** ** **
** **

重头戏来了。相信没有了解过XL的同学，对着几十种风格一下子“哇”了起来。事实上，每一个风格还真的都能对应生成相关的图片，突然一下子有比MJ更酷嗖了！要知道简单通过关键词+风格选择就能锁定想要结果听起来就很美妙。

这里我也亲自测了一下，  数量太多，就挑重点了  。  

还是上面太空小猫的关键词。

** artstyle-hyperrealism(艺术超现实主义）  **

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At61wL1mROM4TKJzwrJHvicbGdpwiaLUjRgsp692B3DyicxLoVHCICo7zOnkPpWWppCs46gZN9Yu645yg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At61wL1mROM4TKJzwrJHvicbG5PXVmdLPic82jzEfrmOLDXwHcpicI4lHKes7MUYLVDKAAslUI3Kuv1Bg/640?wx_fmt=png)
****

  

** sai-analog film模拟胶片  **

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At61wL1mROM4TKJzwrJHvicbGUInCJHU7n8dFAV2USJ4HhIJICSqIPyfEhkZuaAhwB4XaR7A5uqiczWQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At61wL1mROM4TKJzwrJHvicbGFia1xXa3m1PxiaNClGeCwVqAoBLcjWdHlyibLTKjmfqkCibFylJiby0haMg/640?wx_fmt=png)

  

** sai-cinematic电影  **

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At61wL1mROM4TKJzwrJHvicbGc7hvrq5AHcf7WDCNWRp12rSG2gwqPZALicPMyQalqspahOApQMm9PbA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At61wL1mROM4TKJzwrJHvicbGSCI1lSyshV30T5oiaZBg0ialibUoUWInkJUPpSmFRooY7QdrYxaYwu7PQ/640?wx_fmt=png)

  

** Adorable 3D Character可爱的3D角色  **

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At61wL1mROM4TKJzwrJHvicbGvJ9CX4ZuromxicgsWEjWtu0MwcgKRKN8QTNcpDmMMOHxag2lPkOPoHg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At61wL1mROM4TKJzwrJHvicbGNWyWTzhVn52A3ZVwf39xAoo5GXrMmDpBibZN8xjIX9cLlUED8sXKKuA/640?wx_fmt=png)

  

** artstyle-psychedelic  ** ** 迷幻  **

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At61wL1mROM4TKJzwrJHvicbGib5NWbzYvMnEwgpMHYibSiaXeawXXub6kNdx1MIAIW5uv4qAePJ1uEHfQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At61wL1mROM4TKJzwrJHvicbGqCFH4k4TsKIBYT5rQwMwyUX1cf9FGFXus5LgSOL8ORcKUJ2PmojGEA/640?wx_fmt=png)

  

** artstyle-steampunk蒸汽朋克  **

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At61wL1mROM4TKJzwrJHvicbGSqQlJhlFWqiaaJuzU48f4mZCW4uE7hSALDOvhXic1SfNqjX1KQPEQOlg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At61wL1mROM4TKJzwrJHvicbGeicGgVLhhtia6whsjecg8NSQxuM49GSlVzOhSR9wH3IiazV38iaHkEia0sQ/640?wx_fmt=png)

  

  

** artstyle-surrealist超现实主义  **

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At61wL1mROM4TKJzwrJHvicbGqicDIwJqTIUhx1l6g5lpgyzdJue5DrmVlSanJqKCSQJJyGKY4KiacDTg/640?wx_fmt=png)  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At61wL1mROM4TKJzwrJHvicbGZk1XQLLxAVaX62HIru0ibMdSA3hbJOCXfdLllAA68YDrMsSibxgyF1ng/640?wx_fmt=png)

  

** artstyle-art nouveau新艺术风格  **

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At61wL1mROM4TKJzwrJHvicbGXpwY9CXVVOFLekhFWia27oQyBQBC1Lqcc5GByqxn2KaeuITRh88QcYg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At61wL1mROM4TKJzwrJHvicbGNtfbzjzZMReVicXTbFjOUjX9icax7h9Oc9fose0icnjGTXbiaNX2IUtopw/640?wx_fmt=png)

  

** artstyle-graffiti涂鸦  **

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At61wL1mROM4TKJzwrJHvicbGnQF25zrKGiaKqF7P2VrLu5nxvJloBFcv84kBmt65Ml9TSbaYcibL6FJQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At61wL1mROM4TKJzwrJHvicbGNvNKmO9SnpccXIncbB101QUmE4h6FKO8yVZZ7hRqFBic0Nic5e4AhEpw/640?wx_fmt=png)

  

** misc-horror恐怖（这哪里恐怖了，可爱！）  **

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At61wL1mROM4TKJzwrJHvicbGdrjndG1eG8oLguPzuA4jBE69I1ZG45KMlYP7upAJOqiaqWXrdG1Mhicw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At61wL1mROM4TKJzwrJHvicbGEqJNVfDEiceQ7HwQ4dq06siaibgvwjL5rM2HnCKVemw4GXzQyRC6KpQvQ/640?wx_fmt=png)

  

** sai-fantasyart幻想艺术  **

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At61wL1mROM4TKJzwrJHvicbGS8a0om2PZJg46Q7eAGFz8K3b8NyU1o1HtH3Kggjj1ibz8REURvXMqqQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At61wL1mROM4TKJzwrJHvicbGaFA9AicmyOaM24N1EpweKt90nTaWLJeJh5Bfc63RiaJiaCmvDO7HsF3cA/640?wx_fmt=png)

  

** futuristic-biomechanicalcyberpunk未来主义生物力学赛博朋克  **

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At61wL1mROM4TKJzwrJHvicbGeYbTks7unKZYonYBdiaqUnHYrYqkt5LD40PyKxNicNicicQZNXu6mqaB4w/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At61wL1mROM4TKJzwrJHvicbG3XKuefRXwjNshItOhGCM31KGpWWOy8MYpzUIGO91ff2ic7phEJHfFkg/640?wx_fmt=png)

太多了，好看又可爱的都还没发完，篇幅有限。就先这些吧。其实原理就是关键词，是XL特有的关键词引导独特的风格（有学MJ的嫌疑），所以更加期待在XL模型基础上炼丹师们微调的专业模型了！！

** **** ** ** ** ** ******** ** ** 安装  ** ** ** ** ** ** ** ** ** ** ** ** **

最后补充一下fooocus的安装和使用方法。

  1. 先说本地的，你需要从ControlNet作者的Github上将工具文件下载到本地。 

https://github.com/lllyasviel/Fooocus  （放心，老规矩，文末有下载）  然后  与webui一样  ，这只是工具，
也没有  懒人包  （因为足够懒了）  还需要下载对应的模型。  你也可以自己去  C站上自己下载  很多  NB的  微调过的  XL模型。
但这里我们介绍fooocus  ,  还是  原汁  原味的体验一下  XL的2个基础模型和一个基础LoRA，  下载
地址如下（自行复制，或者老规矩见文末  ）  ：  https://huggingface.co/stabilityai/stable-diffusion-
xl-base-1.0/resolve/main/sd_xl_base_1.0_0.9vae.safetensors
https://huggingface.co/stabilityai/stable-diffusion-xl-
refiner-1.0/resolve/main/sd_xl_refiner_1.0_0.9vae.safetensors
https://huggingface.co/stabilityai/stable-diffusion-xl-
base-1.0/resolve/main/sd_xl_offset_example-lora_1.0.safetensors  2\.
另一种就是云端体验，登录 **AIfish暴躁鱼干在线SD云服务**
，除了可以使用小鱼干了亲自调教的webui外，还临时上线了fooocus服务在线体验，早用早享受，先到先体验！  https://aifish.vip

  

** ** **** ** ** ** ** ******** ** ** 最后  ** ** ** ** ** ** ** ** ** ** ** **
** **

** ** **** ** ** ** ** ******** ** **
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At61wL1mROM4TKJzwrJHvicbGiaZ1Q1k4YK0VM7s2VribLerqMqqC7TXj5icrLdrA0pKq8WlBuDaN9UUIA/640?wx_fmt=png)
** ** ** ** ** ** ** ** ** ** ** ** ** **

部分杜撰场景如有巧合纯属巧合。  感谢群里的小伙伴友情出演。

如果对SD防灾对策群感兴趣的也可以关注公众号给 **【小鱼干了】** ，通过公众号的自动回复 **加群** ， **加好友** ，获得
**在线SD云服务** 等操作。  ****

本期文章提到的工具和模型，可以公众号回复  **【下载】** 获得资源。

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

