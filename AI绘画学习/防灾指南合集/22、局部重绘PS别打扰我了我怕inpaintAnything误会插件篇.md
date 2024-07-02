![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At7qt5m6ePFqIs6ibrRZxj0t1juLQSibvYWJ3LicafTDxQ2Xjk1h8rz5PFAOiaSUKxFVI0Ldm8aHzvic3ibA/0?wx_fmt=jpeg)

#  “局部重绘”，PS别打扰我了，我怕inpaint Anything误会（插件篇）

原创  暴躁的卡爷  [ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

介绍segment anything不介绍inpaint anything肯定又会打喷嚏了！~

inpaint anything（以下简称IA）本身就是一个可以独立使用的工具，又有可以放进SD的插件，让局部重绘这件事变得更加容易学习和上手。

项目URL：

https://github.com/Uminosachi/inpaint-anything

  

** **▍** ** inpaint Anything  ** **

IA使用的核心依旧是Segment模型，上篇已经提及，你下载的sam模型仍然可以复制到这个插件中。还是一如既往的喂饭。  ****

[ SegmentAnything 能分离一切的插件
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247485292&idx=1&sn=9e387ec86ba6c182dc00dae6f159cd8a&chksm=97a4315da0d3b84bf179eb786c91cef7c76450ed4ec632cf4729afb65f319d072b58b386ef3f&scene=21#wechat_redirect)
>>

** **** ** ** ** ** ******** ** ** 下载和安装  ** ** ** ** ** ** ** ** ** ** ** **
**

1\. 其实所有能在扩展中搜到的插件安装起来都很简单。并且大部分优秀的插件都能通过  **
扩展——可下载——点击加载扩展列表——搜索关键词(如segment)  ——找到  ** 。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7fc52WpiaXRkMIUv9pQtPOxJp2PqWnZutRIDxZ0icqDwWy4tbI8zmpcib5fibcHRTWWYQsCKeicBATvhw/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

2\. 你也可以通过github的url, 从 从网址安装——粘贴url——安装  

https://github.com/Uminosachi/sd-webui-inpaint-anything

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7qt5m6ePFqIs6ibrRZxj0t1nicvt1y94xibxmMsxL57ZPdZz2jvKBTjeWYia6jEz1pM1LsQoAaKNxXow/640?wx_fmt=png)

3\. 最后如果你的网路环境真的太差了，还是老办法，你从文章末尾提供的下载方式中，把插件直接下载，并安装到SD目录中的extensions中。

（虽然但是，每次重复这一个环节挺啰嗦的，真心希望早日摆脱喂饭级别，让节奏快起来。）

** 下载模型  **  

IA插件同样需要下载模型，好在如果你有看上一篇也下好了sam模型，这一部分就可以跳过，另外。IA也很贴心的提供了下拉选项下载，点击下载也能，不过需要你的网络没问题（懂的都懂）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7qt5m6ePFqIs6ibrRZxj0t1chfCUpqXuDhTRBnFR5M0Eibs6wmsSicoBz30ov3ichUGYRPQ7gF4BdxgQ/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** 插件的用法  ** ** ** ** ** ** ** ** ** ** ** **
**

其实IA功能很多，但又比较简单。你可以把插件划分成三个区域。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7qt5m6ePFqIs6ibrRZxj0t1DH06uBoHe2kwbCqsRzDPaHksBPYWeiaR4MjGFw7QmVLu9kuB9HHGia4w/640?wx_fmt=png)

分别是：

  1. 分离目标以及调整区（左上） 

  2. 语义分割显示区&选择被分离的蒙版区（右） 

  3. 局部重绘区（左下） 

  

** 分离目标以及调整区  **

  * 将图像拖放到输入图像区域。（下载好模型后） 
  * 点  击按钮运行  **Segment Anything** ，模型会自动识别参考图  ，进行  元素分离。 
  * 如果图片识别难度高，可以勾选动漫模式，提高识别度，但也降低蒙版的分离质量。   

  * 填充选项勾选后，可以修改参考图的模式（通常默认就行）   

  

** 语  义分割  显示区  &选择  被分离  的蒙版区  **

  * 等待数秒钟，右边上面就会出现根据模型分离出来的不同区块。可以通过鼠标进行所需蒙版的选择，（因为已经分离好了，所以只用把需要重绘的区域点一个点就行）。 
  * 鼠标置于图片之上:按住  S  键进入全屏模式，  R  键重置缩放。（方便更精细的处理）。 
  * 选择好以后就可以点击创建遮罩了。   

  * 下面2个勾选好理解，一个反选，一个是否包含黑色区域（无法识别？） 
  * 下面就会出现遮罩高亮显示的蒙版。 
  * ** 展开蒙版区域  ** 按钮是用来扩充蒙版大小的，这个之前segment也有，帮助你向外扩展，可以一直点。 
  * 旁边的按钮就是选中的蒙版减去手动绘制的区域。 

  * 最后的按钮就将手动绘制的区域添加至蒙版中。都还比较好理解。 

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7qt5m6ePFqIs6ibrRZxj0t1Sq9HfoLhOoaCbuDhFloOe2liabNQdxezUB6svSfhzqyqPKlyOaMRt2A/640?wx_fmt=png)

  

** 局部重绘区  **

现在我们拿到了需要重绘的蒙版遮罩了。进入左下角的局部重绘区。  

这里提供了4种重绘和1种消除，本质都是inpaint（局部重绘）。我们一一介绍。

  

###  Inpainting Tab

这其实就是IA给大家提供的一个傻瓜式的局部重绘方案，主要是重绘模型，官方优选了6个比较常用的优秀ipaint模型（局部重绘是专门的模型），点击运行的时候会提供模型的下载（小心爆C盘）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7qt5m6ePFqIs6ibrRZxj0t1QBnH3D6EyC2zzicaESXlO8sibicic7JUH4Mfe7FiaX0pr8ISqsVCR3CBgibQ/640?wx_fmt=png)

优点就是模型不用管，成功率较大。自然可以调整的地方也不够多。就一笔带过了。（所有高级选项都是生图的基操，不多说）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7qt5m6ePFqIs6ibrRZxj0t1FPOYufHcFPw1veWI6Sk9SJiczd7SB1cwAOjUAwK6MlIhxaYn2pDALoA/640?wx_fmt=png)

###  Cleaner Tab

这个我的个人经验是，PS
beta的cleaner能力应该是最强，没有之一。这里IA提供了数种cleaner模型，在选中了一种清除模型后，可以一键擦除所需内容，（此擦除为清除元素，填充背景图）。亲测下来默认Lama就很好用，例如我们用它擦掉了少女的耳环。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7qt5m6ePFqIs6ibrRZxj0t1838ibeoo9LLBibRylhWKEqMtKT0PnicbJwaqJyexptWTVD4jbI7RtUuiag/640?wx_fmt=png)

###  Inpainting webui Tab

这部分就是当你有自己的局部重绘模型，可以选择，插件会自动从模型目录中读取。也很好理解，与第一个其实差不多。比如我这个就是dreamshaper8（效果一般）  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7qt5m6ePFqIs6ibrRZxj0t1XTv3uA4cF5Y5uYq1OOKUfbTM8yUQVib9rdGcNujkvZYicHbPVmHb13LA/640?wx_fmt=png)

###  Mask only Tab

这部分也很好理解，segment anything那一篇我们就介绍了将遮罩蒙版发送至图生图的蒙版绘制中，利用webui的蒙版局部重绘，这上一期我们也操作了。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7qt5m6ePFqIs6ibrRZxj0t1Yiaa3OJib2ibaO9d9WyNOEEtaEYnLVwcC8M6ZlGicAl3RFFFeoYQYVibFAQ/640?wx_fmt=png)

###  ControlNet Inpaint Tab

重点来了。这个CN的局部重绘可以说是IA重绘功能的精髓了。你可以在全局选择任何大模型作为底，然后插件为你提供CN的局部重绘参数，你可以很容易的利用CN的局部重绘进行inpaint。  

同时，它还提供了一个ControlNet选项。点开除了能调整CN的inpaint相关参数外还附赠了一个参考CN，相当于你在生图过程中开了2个CN单元，一个局部重绘，一个参考（reference），这就很有趣了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7qt5m6ePFqIs6ibrRZxj0t17YWUq50gDfznCxSXBptFt3ibbs4pomQ3IGLo18tKdJj6Wibo7AgBicjsg/640?wx_fmt=png)

对比一下有无参考的重绘结果：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7qt5m6ePFqIs6ibrRZxj0t1cg7kTUkzFUAaZI8tZqia1oKzQTj4wrXmwkicSELiaKpy5vicKKLCFLTZGA/640?wx_fmt=png)

|

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7qt5m6ePFqIs6ibrRZxj0t1zfORNZXANLAT2tB1z4f2mAcTpTlyxNPgB1fzDgQZNto9MMVn0VjpQw/640?wx_fmt=png)  
  
---|---  
  
  

总结，这是一个简单上手，可视化操作的局部重绘工具，对比与segment anything的优劣：

  1. segment anything 得益于GroundingDINO，可以只用文本分割。 

  2. inpaint anything可以直接将图片分离结果呈现。 

  3. inpaint anything可进行擦除，不跳转的细节重绘，体验更好。 

  4. inpaint anything的局部重绘对手应该是PS的SD插件（这个我们以后聊） 

  

好了，这一期inpaint anything内容就这么多

下期见~！~  

  

  

** 最后  **

如果对SD防灾对策群感兴趣的也可以关注公众号给 **【小鱼干了】** 私信微信号，我看到了会加你，拉你们进来一起开放，学习，共同进步。

文章中提到的LoRA资源，  公众号回复 **【下载】** 即可。

👇关注公众号，获得免费在线SD，下期见  ！  ~

  

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

