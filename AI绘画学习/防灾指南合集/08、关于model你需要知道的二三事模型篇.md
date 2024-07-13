![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At5wtvRxKRkN4GWicE93NRia42FCjzjMdc00VUlTicDbevm6NZPz0q7QgyfGE00hSQc31FGkyTwicFbwcQ/0?wx_fmt=jpeg)

#  关于model你需要知道的二三事（模型篇）

[ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

  

** Model是什么  **

这里的Model 特指：Stable Diffusion，是2022年发布的深度学习文本到图像生成的潜在扩散模型”（latent diffusion
model; LDM），以及用这个方法训练得到的其他模型。

  

** 先说SD系列  **

比  如sd-v1-4、sd-v1-5、sd-v2（简写成SD1.5、SD2.0）之类的大模型，这些都是Stable-
Diffusion官方出的大模型，分别是1.4、1.5、2.0和2.1版本。  

**![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5OKCwshyLbLgyYkUliahWcfDEDkvSf98icnQmfco4qePLRgwhOjduZDrg3ibncdgopqZNWRryP5PGPg/640?wx_fmt=png)
**

SDv2更新了CLIP模型到OpenAI公司开源的更大的、参数更多的OpenCLIP模型，可以更好地理解人类语言，所以效果比SDv1好。而且SDv2移除了NSFW检测器，数据集更多，效果也更好一点，但是相对的可以生成NSFW内容，请各位不要用来生成违法内容！还去除了一些艺术家风格的关键词，可能需要规避一些版权问题。  

SD官方模型十分庞大，什么风格都有，属于样样通，样样不精那种，但正因为其庞大驳杂的特点，让SD比较适合作为底模进行再训练和finetune微调。由于一些反向操作，SD1.5是目前训练最好用的底模，而不是更新后的SD2.1。

** 模型的格式  **

.ckpt 和 .safetensors 后缀名的文件都是用来保存模型的权重和参数的，但是有以下区别：

.ckpt 文件是用 pickle 序列化的，这意味着它们可能包含恶意代码，如果你不信任模型来源，加载 .ckpt 文件可能会危及你的安全。

.safetensors 文件是用 numpy 保存的，这意味着它们只包含张量数据，没有任何代码，加载 .safetensors 文件更安全和快速。

为了将 .ckpt 文件转换为 .safetensors 文件，你需要先加载 .ckpt 文件中的数据，然后用 numpy 保存为 .safetensors
文件。这个过程需要一些额外的步骤和工具。

** 模型的命名规则  **  

  * v1-5-pruned-emaonly.ckpt  \- 4.27GB, ema-only weight. uses less VRAM - suitable for inference 

  * v1-5-pruned.ckpt  \- 7.7GB, ema+non-ema weights. uses more VRAM - suitable for fine-tuning 

我们在下载模型的时候会看到pruned、emaonly（ema）之类的后缀，可以看看他们分别表示什么意思。

  * ** F  p32  ** ：意味着模型使用32位浮点数(float point)储存值，是模型的原始保存值 
  * ** Fp16  ** ：意味模型用16位浮点数存，相对于Fp32更小更快，但是无法用于CPU，因为有的半浮点精度运算在CPU上不支持。通常为了更快的运算，在GPU上我们也会将Fp32转换成Fp16，这个可以在设置里配置。 
  * ** pruned  ** ：意味对模型参数进行了修剪，以达到更快的运行速度（也就是丢了一些参数） 
  * ** ema  ** ：ema(Exponential Moving Average指数移动均值)是一个技术用来抵抗波动以得到更好的结果，比如小明多次最后一次考试考砸了，这不能反映他的水平，取多次平均才能更好地表达他水平。    

###

###  ** final-prune系列  **

这个经常出现在很多懒人包里的模型是 **NovelAI** 出的大模型，final-prune是剪枝版，animefull-
latest是完整版，根据上面的知识点可知不自己练模型的话，没有太大差别。

NovelAI又简称为NAI，NAI 系列模型基于Stable Diffusion Model在使用  Danbooru
图片社区的训练集训练而来的，比SD官方模型，更适合出二次元的图片，不过对于当下的环境，也有一些陈旧了，在二次元风格上属于大而全，不够精细垂直。脱胎于SD官模，又沦为和官模相似的底模定位。

  

##  ** Stable Diffusion 和 NAI 关系？  **

因为泄漏事件，NAI 使用数千万 Danbooru（图站）图片训练的模型被泄漏了两次。这也是我们能下载到以final-
prune命名的模型的原因，所以NAI和SD的关系已经被广泛的认知  （不知道MJ和SD的关系是不是也是类似，虽然官方都强调过并不是）  ~

  

  

##  ** 模型三大件:clip、unet、VAE  **

通过 ** [
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484513&idx=1&sn=ff202f639dab537dedb3542fea9580e7&chksm=97a43250a0d3bb460e3f21df12c178865f9c293b7604328239bf5fc2a18f5b2590fbc6538f32&scene=21#wechat_redirect)
[
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484477&idx=1&sn=09c98f54489fcba0269684699a7c7d76&chksm=97a4320ca0d3bb1af65d22ea271fd5dbacbf66a0ab7bd07deebc806f4a652ec41673f2d6c65f&scene=21#wechat_redirect)
[ Stable Diffusion的工作原理（理论篇
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484513&idx=1&sn=ff202f639dab537dedb3542fea9580e7&chksm=97a43250a0d3bb460e3f21df12c178865f9c293b7604328239bf5fc2a18f5b2590fbc6538f32&scene=21#wechat_redirect)
** 了  解到扩散模型的工作原理，也知道模型中  clip、unet、VAE  的重要。

  * TextEncoder（Clip）：会把tag转化成U-net网络能理解embedding形式 

简  单的说就是将“人话”转换成AI能够理解的语言

  * U-net：对随机种子生成的噪声图进行引导，来指导去噪的方向，找出需要改变的地方并给出改变的数据 

简单的说就是死盯着乱码图片，看他像什么

  * VAE：AI原本的生成图不是人能看的正常图片，VAE的作用就是把AI的这部分输出转化为人能够看的图片。 

简单的说就是把AI输出翻译成人能看到的图片

  

** 模型一般大小  **

一般模型大小为1.98Gb和3.97Gb有的为7.17G，除非模型各部分精度不同造成的其他模型大小之外，一般而言奇怪大小的模型都会或多或少的存在junk
data。

noVAE模型的大小为1.8G左右，noVAE&clip的模型为1.6G

默认情况下，webui 会将所有加载的模型转换为FP16使用。

  

** VAE是什么  **

.vae.pt 后缀名文件是用来保存变分自编码器（VAE）的权重和参数的，VAE 是一种生成模型，可以用来对图像进行编码和解码。VAE 的作用是：

为 Stable-diffusion 的模型提供:

低维的隐空间，可以在这个空间中控制图像的风格和特征。

初始化的图像，可以在这个图像的基础上进行细化和改进。

颜色校正的功能，可以让生成的图像更加鲜艳或者柔和。

  

###

###  ** VA  ** ** E问题的原因  **

###

模型输出图发灰说明这个模型的VAE出现问题了，常见于融合模型中。不同VAE之间的任何Merge都会导致VAE中的某些东西被破坏。并且很多融合的模型再拿去融合，那么VAE就会跟着破坏。这就是为什么很多模型输出图是灰色的，以及人们热衷于单独使用加外置VAE的原因。

遇到这种情况，一般而言需要修复VAE才能使得模型正常使用。不过web
UI提供了外置VAE的选项，可以在生成时忽略模型的VAE而使用外置VAE替代。所以造成我们很多时候会误以为VAE就是纠正色调或者是“模型滤镜”，新入门可以这么粗暴的去理解，这只是一个原本错误的学习方式。

  

  

** 附加点：大模型外的小模型  **

** **
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5wtvRxKRkN4GWicE93NRia42G1mUf3UMBEGGZoib8I21ErXmrRXGWGBI8ZDMr2TMX35ISRL78Mo9icgA/640?wx_fmt=png)
** **  

###  ** Textual Inversion (TI)  **

从一些具有共同语义 [v] 的图片中，提取 [v] 的一个方法。提取出的 [v] 张量称之为 "Embedding"。将 Embedding
保存为文件，之后生成图片时就可以在 prompt 中以文件名引用。

####  特征训练产物大小较小，webui 自带训练支持。

可以解决新出的角色画不出的问题，或者模仿特定的可以用语言精确描述的艺术风格。

因为 TI 是在 Text Encoder 的输出做处理，所以并不能让模型学习到它不知道的概念。不同模型的 embeddings 不通用。

** hypernet  w  orks  **

hypernetworks .pt
文件是用来保存超网络（hypernetworks）的权重和参数的，超网络是一种可以生成其他网络权重的网络。超网络的特点是：

可以用来对 Stable-diffusion 的模型进行文本反演（textual
inversion），即根据自己的图片训练一个小部分的神经网络，然后用这个结果来生成新的图片。

可以用来对 Stable-diffusion 的模型进行风格迁移（style
transfer），即根据自己的图片或者其他模型生成一个新的权重，然后用这个权重来改变生成图片的风格。

可以用 NovelAI 的 hypernetwork 自训练工具来创建自己的 .pt 文件，然后把它复制到 Stable-diffusion 的
models/hypernetworks 文件夹中。

** Lo  RA  **

Lora 模型是一种轻量级的微调方法，可以通过少量的图片训练出一个小模型，然后和大模型结合使用，干涉大模型产生的结果。

Lora 模型可以在 t2i 和 i2i 模式下使用，可以和任何主模型一起使用。  ** **

LoRA是一种用于大语言模型的低秩逼近（Low-Rank Approximation）技术，可以减少参数量和计算量，提高训练效率和生成质量。

LoRA也可以用于Stable-diffusion中的交叉关注层（cross-attention layers），从而改善用文字生成图片的效果。

LoRA模型的个头都比较小，常见的都是144MB左右，使用的时候要与精简版（prund）的Stable Diffusion1.5模型配合使用。

LoRA模型训练时占用的显存非常小，一般在7GB左右，适合低配电脑使用。

  

  

文章参考：

stable diffusion book  |  https://stable-diffusion-book.vercel.app/install  
---|---  
  
AI绘图红宝书

|  https://z28pynubvc.feishu.cn/wiki/wikcnYiF2qaBWVtvVmjq7GjPXpc  
  
#  Stable-diffusion 各模型区别笔记

|  https://zhuanlan.zhihu.com/p/611248399  
  
模型理论科普V2.0.0627

|

https://docs.qq.com/doc/DQ1Vzd3VCTllFaXBv?ADPUBNO=27314&ADSESSION=1688098098&ADTAG=CLIENT.QQ.5983_.0&ADUIN=76145389&nojump=1&tdsourcetag=s_pcqq_send_grpfile  
  
声明，文档使用 GFDL 许可。  详细声明请点链接查看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5wtvRxKRkN4GWicE93NRia42mINp8NB5HRDKfsnj48CgOiaReyfq5NjYNzTyq80PiczoianApmUnpTsNA/640?wx_fmt=png)

预览时标签不可点

微信扫一扫  
关注该公众号



轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6iciciaKY5WZ4ib8CVibVnVHRJwGj6ksg7fk0tzTMuLPsvptv6zswtKfCLNFwYr9aIBGkjiaYGBWtibwnOQ/0?wx_fmt=png)

小鱼干了







****



****



  收藏

