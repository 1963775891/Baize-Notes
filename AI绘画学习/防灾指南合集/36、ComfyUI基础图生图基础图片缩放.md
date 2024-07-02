![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7ib4tdvJxapk6m7h3uxKhl6ydCLjMpMYJzicPq4ZdlibyDLXpusC7iaYlfLA/0?wx_fmt=jpeg)

#  ComfyUI-基础图生图&基础图片缩放

原创  暴躁的卡爷  [ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

书接上文，上一期我们介绍了ComfyUI的最最基础的一次生成过程，打铁趁热，我们接下来讲讲图生图，以及和图生图紧密相关的基础图片缩放功能。

上一期很重要，就像《防灾指南》进行SD生图入门一样。传送门：

[ ComfyUI，你开启XL钥匙打开了新世界
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247485938&idx=1&sn=4786693cccbcd59f84dbaf261258dc52&chksm=97a43fc3a0d3b6d54735e790318ee8b81f2361c7872dd9eeae17b5e92c1f1218ab9c6a7fb401&scene=21#wechat_redirect)
>>>

  

还是老样子，AB航线提供选择。

  1. ** 🤔A航线  ** 有webui的底子，想了解生图过程，能 **举一反三，进阶学习** 的。 

  2. ** 🤓B航线  ** 喂饭都不想吃，我只想 **无脑使用** ，出图效果好的。    

如果跟随  《  [ Stable Diffusion 防災指南
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484593&idx=1&sn=28186490d02d1f6376e10d549c8f480d&chksm=97a43280a0d3bb968a1988fb3ad41c30b3698dd9d9316a3b38bc32d41838f1988f4400de24ee&scene=21#wechat_redirect)
》  一路学习过来的朋友可以选择 **A航线**
继续跟随卡爷的节奏进入ComfyUI新世界，而对ComfyUI本身兴趣不大，但对比WebUI还简单无脑的生图很需要，直接跳过下面A部分，滑到后面的
**B航线** 就行，按需食用即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5WWPHUPkYwQ2s3ThTehqVEjPBZD7RlzPPeMwI7icf8QRpveXQA1Zu5Uk2H8icGuVjVPwIusFrKvMZA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

  

** **▍ ** **** **** **基础** ** ** ** 图生图 ** （ ** ** ** ** ** A航线 ** **** 🤔）  **
** ** ** **

webUI将文生图和图生图拆分成2个工作page其实是有逻辑分类误导的。因为本质上文本和图片都需要经过各自的编码器进行编码翻译。看下面这张图就很直观的了解了文生图和图生图的区别。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7iboKibrXOLnaLRud4OWdaBDjEV7GRrHxEWo3A5YSLzLunDicVrgGSwZhcw/640?wx_fmt=png)

图生图需要将加载图片通过图片编码器翻译，再进入潜空间进行重新排列组合。而文生图的整套逻辑是不受影响的。  

所以我们可以自己手动连接一个基础图生图的工作流出来。

Img2Img在ComfyUI中工作原理也是完全相同的，加载一个图像，用VAE图像编码器将其转换为潜在空间，然后用低于1.0的噪点对其进行采样。降噪控制添加到图像中的噪声的数量。降噪越低，添加的噪声就越少，图像的变化就越小。这就是我们熟悉的
**图片重回幅度（denoise）** 。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7ibsEhnw1zd4Qsjg9G2gMRDwBctCnC9BYibgAP9SQN7rJZcTMPZA8iaJibiaw/640?wx_fmt=png)

因为有图片作为目标了，之前建立的空latent就可以删掉，替换成一个VAE编码器，然后将VAE连接到模型的VAE中，如果有自己倾向的也可以单独连线一个VAE加载器。这就是一个基本的图生图所需的latent连线部分。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7ibo3K6hEIbWtGs1dqyR642eU6Y5lXF0GN1nWGZjdPcWk7SicWSjNab9SQ/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** 基础放大  ** ** ** ** ** ** ** ** ** ** ** **
**

图生图的节点连接还是很容易的。但因为我自己在学习comfy的过程中，对于图片放大，潜空间放大，使用放大模型放大，和直接图片尺寸改大的认知上欠了债，导致后续自己连接hires.fix
的高清放大的”卡关“了很久。  

为了避免相似的惨案发生，我们就先只在基础图生图部分进行概念的划分。

先了解什么场景下我们需要放大或者缩小。  

在加载图片后，我们因为目标需求尺寸和原始图片尺寸不相配，所以需要调整图片尺寸，而文生图在空latent里设置尺寸的节点又不生效，所以只能调整图片输入的尺寸，这个时候就需要进行图片的缩放。  

右键新建节点——图像——放大，这里面有所有的基础放大操作。（忽略最下面的2个，那是传说中的USDU插件，以后进阶图生图我们会再单独介绍）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7ibvibzIJJIb6MviaFrrtnUwk4q4EIKIXv621N34TGsQm5hRtBbEW32Oiaog/640?wx_fmt=png)

我把这四个缩放节点都掏出来，就很容易理解了。

他们前三者分别用不同的方式进行图片的缩放，如果输入分辨率则有一个是否中心裁切的选项，不然默认都是拉伸的。缩放方法有一些常用的缩放算法，这里展开就很复杂了，默认最近邻插值（nearest-
exact）就行，因为对于我们希望的放大，这种放大都是暴力不可用的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7ibweOf2JK50MmJ33eaJibKULJvIJ4CRxWwCUg2nwvya2Ck0P7COuYjCZw/640?wx_fmt=png)

至于使用放大模型，这里就相当于webui中的附加功能的放大方式。就像之前介绍webui所有主流放大方法中说的，如果只是追求速度，可以使用通过模型放大的节点，且可以多次串联，效果聊胜于无。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7iblwaadKsEdRKnym5g6GRUfX3voKRWAZpP4P1WXjg3YIGwufYBQic9MEg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7ibFZEWlAiamkNSrCPWhpath8oJmF2icoeZvFm8gm9ZqzLRFLomNJa7sTDA/640?wx_fmt=png)  

那什么样才能做到我们理想的高清放大，或者webui的那些放大放大如何在comfyui中实现？别着急，之后会有单独一篇来讲。  

这次我们只需要对一些webui中我们都被安排得明明白白，在comfyui里完全得自己来的概念先种个种子。

还有就是这个蓝色的 图像-图像的连接线。是以后各种工作流串并联的重要部分。  

  

  

** **** ** ** ** ** ******** ** ** **▍ ** **第一次生成** （ ** ** ** ** ** B航线 **
**** 🤔）  ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

** **** ** ** ** ** ******** ** ** 导入工作流or图片  ** ** ** ** ** ** ** ** ** ** **
** **

下图工作流已经放入下载中，也可以进最近成立的ComfyUI学习交流群向群主索取。导入后只需要传图和填基本参数就能用， **超级简单** ！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7ibHgmiatbB1yAZfoWjia4HnyAxVAt9DvYfSUjd0MDiaYDJ38fo2167Q3d6w/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7ibnZAKxvTYDFZibBAZLmpb4gB6rXpfmGkwW7yNiaygmoIEX3hLwcYovN7g/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** 傻瓜式操作  ** ** ** ** ** ** ** ** ** ** ** **
**

将上面工作流or图片导入后，看下图，你只需要操作：

  * 选择模型。（可默认）   

  * 填写关键词（负面关键词可以默认） 
  * 导入图片，设置图片尺寸。（默认1倍，原始图片尺寸为1024x800)   

  * 设置图片参数（基本都默认即可） 
  * ** 重绘幅度需要调整0.3-0.5与原图接近，0.5-0.7有很大的变化，大于0.7放飞  **   

  * 点击最右边的第一个按钮，就可以目送你的图片从左到右的进行生成工作了。   

** 全程甚至只需要填写正向关键词这一步操作就行  ** ，和webui一样，比webui还流畅，还直观，甚至更简单的生成动作。

  

** **** ** ** ** ** ******** ** ** 中文设置  ** ** ** ** ** ** ** ** ** ** ** **
**

使用 **暴躁鱼干在线云** 学习使用ComfyUI的只需要在生图控制台右上角点击设置⚙图标，然后在设置菜单中找到语言设置，切换成中文就行。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6THAskDAAulLI2yYgxiaJjk4fIyb6ydiadNicG32Gjnk0UxX5vKZLXct12diaRHIficrqZkyOriaMn47tg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)  

没用使用 **暴躁鱼干在线云** 的暂时不要着急我们后续插件篇会提到如何安装UI汉化插件的。

  

  

如果你都已经开始着急更多WebUI上熟悉的功能了，那么恭喜你，你上道启航了，好的开始，我们下一篇见！~

  

  

** 最后  **

**在线** 云服务地址:  **aifish.vip** 。

如果对SD防灾对策群感兴趣的也可以关注公众号给 **【小鱼干了】** ，通过公众号的自动回复 **加群** ， **加好友** ，获得
**在线SD云服务** 等操作。  ****

本期文章提到的PNG信息图片和工作流，可以公众号回复【下载】获得资源。

  

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

