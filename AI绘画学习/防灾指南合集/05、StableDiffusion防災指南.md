![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At5wtvRxKRkN4GWicE93NRia42jCup56RuHz4MR5ibYDfBTHPyk3fSEvSrEzs2ts4Cx5scbNaLbyKUVXw/0?wx_fmt=jpeg)

#  Stable Diffusion 防災指南

原创  暴躁的卡爷  [ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4ZTg0vEv5ZcSylfXhflSCnFhavdOV1eMuoByBBiah2XwFfxSNOzPcM4ibWtwSNmx9VSQNibYAR2mW9w/640?wx_fmt=png)

随着大语言模型的阶段性爆发以及图片生成的扩散模型惊艳表现，裹挟而来了一阵巨大的，史无前例的AIGC狂风骤雨，并随之而来的产业变革，职业焦虑，专业普及等等一系列的“灾难性”变化，处在风暴外的人很难独善其身，处在风暴中心的设计师们又该如何应对呢？

这篇SD防灾指南将尝试从图片生成模型stable
diffusion和ta的生态切入，系统的指引我们从零到一的了解AIGC，熟悉ta，并驾驭ta，成为一个优秀的“災害對策精英”。

  

** 怎么开始？？  **

防災指南会根据一个图片生产者从“小白”到成为“對策精英”的学习周期来分步讲述如何生图，并针对不同角色不同阶段单独有针对性更细致的文章攻略。所以指南更像是一个目录，wiki，和指南本身。但文章仍然有些长有点干，需要点耐心。

  

** 开始之前  **

所有文章都会尽量避免晦涩难懂，但因为行业起源，以及更有利于彼此交流和深入学习，大家还是需要对一些基本知识有一点了解，包括后续会出现的一些专业名词，就不再一一解释。可以先通过下面这两篇做一个了解，包括扩散模型的工作原理，决定了我们后续理解我们的图是怎么变出来的。

[ ** AIGC常见名词解释（字典篇）  **
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484472&idx=1&sn=b277914771d3a54a76cc2f3bbaeaa867&chksm=97a43209a0d3bb1fd4f4895e653d9a5425cdf9914e06c0058e67c04e7e24a973b64fac5f5276&scene=21#wechat_redirect)

[ ** Stable Diffusion的工作原理（理论篇）  **
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484513&idx=1&sn=ff202f639dab537dedb3542fea9580e7&chksm=97a43250a0d3bb460e3f21df12c178865f9c293b7604328239bf5fc2a18f5b2590fbc6538f32&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4ZTg0vEv5ZcSylfXhflSCnp6cUj120Du3JRibjHNaFAsHj9b03jg0X992WTRKzzII2hX0wArnOPCA/640?wx_fmt=png)

  

** 为什么是从SD开始？  **

当前主流的图片  AIGC
就是SD和Midjourney之争了，甚至在某些维度上让我想到iOS和Android。MJ做得很好，但我仍然希望你的入门和进阶都从SD入手。

  * 可控性。AI出图最大的阻力就是可控性，包括图片质量的可控和图片内容的可控。图片生成得完整，好看是MJ的强项，普通人大概只需要这个需求发发朋友圈吹牛打屁，换换头像。而真正要做到心有所想，生而所得，MJ和它的用户都在努力，但把这一部分只交给关键词来控制很难。这里有更多控制变量的SD有巨大的优势。 

  * 开源性，战未来。并不是说闭源不好，提供良好的使用体验，黑盒去噪，是MJ努力降低图片  AIGC  的门槛的产品思路，但拥有越来越成熟丰富的开源生态的SD，也意味着会有越来越多的神级插件，越来越厉害的技术融合，进一步提高美术生产效率和精度。 

  * 灵活私密性，SD可以像MJ一样云端部署，随时随地可以访问。也可以本地部署，调用本地的算力，灵活的调整配置所需的生产环境。隐私性也是很多像游戏、影视等商业项目只考虑SD本地部署的重要原因。 

  * MJ很贵。呸，MJ很简单没挑战。呸，  SD的知识体系很碎片，更需要一个开始。 

有个不恰当的比如：MJ是自动挡的车，而SD就像手动挡的车。掌握后者大概率能轻松驾驭前者。也更容易二者兼修打组合拳。

  

** 准备工作  **

在决定使用SD来解决我们所需的生图需求后，也初步了解了AI和扩散模型的工作原理后我们需要开始准备第一部分了。  

这里有三个比较重要的部分需要提前准备，并且这三部分决定了后面我们在生图能达到的质量高度和效率高度，他们分别是 **算力** ， **工具** 和
**模型** 。

  

** 硬件  **

**
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5OKCwshyLbLgyYkUliahWcfsssn607xUVUTqO2tIbTC3GCMAR1FtWTg1iaeAsR4vrZN94XuicngwUxA/640?wx_fmt=png)
**

算力这个词听起来就很厌烦的，又是什么互联网黑话生造出来的破烂词，当然它和AI本就密不可分，我们的生产又本身离不开计算机，索性将这部分叫硬件部分。

也就是你需要准备一台电脑，这台电脑最好有一个独立的英伟达的显卡，显存最好是12G以上的。操作系统最好是windows的。

如果很遗憾，上面这些词语参数听起来像天书一样，你可能需要先看看这篇文章了解一下算力和显卡以及你当下手上的设备可不可以加入“防灾”。

** 你看我这算力如何（硬件篇）链接漏了，看公号历史查询。  **

如果，你对计算机的基础常识都不能理解，你只会用开关机，那我大概率还得出一篇：

攒一台AI跑图打游戏两不误的小钢炮（硬件篇）（挖坑1）

  

** 工具  **

准备好了硬件就要准备软件工具，与很多只能在云服务上使用的工具不同，SD借助开源工具，可以云端部署，也可以本地部署，使用上面提到的本地硬件来运行，这样更“私有”，也更灵活可控。

当然，你可能也需要忍受他们糟糕的用户体验和凌乱的界面。大概长这样。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5YiaH0ja7cDkQgUJt0TvhU4SFUdyUbtOyEHWnyDW4Qzqrx1ia9r3hKeCeFoFObHZ1mUW7Nz3OFxWAA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5OKCwshyLbLgyYkUliahWcf7RzOzicib1kxuGafIjgMgn16PEjgvlCFFuMCz1ic0bGd3tt9Jtth22tdw/640?wx_fmt=png)  

目前主流的开源工具主要有２个。

  * ** Web UI  ** Stable Diffusion WebUi 一个基于 Gradio 库的开源工具，由个人大神automatic1111开发，并在全球开发者贡献下，成为一个强大的最主流的生产工具。（上图1） 

  * ** ComfyUI  ** 流程图/模块化设计的 Stable Diffusion GUI，采用连线式交互，更接近现有游戏、影视的生产流程和交互方式，门槛更高，天花板也更高。（上图2） 

  

我们主要使用WebUI这个工具，因为前者的生态更加完善，学习门槛相对更低。（后者因为解决了一些当前工作流的硬伤，可能在未来某个时间点爆发式的增长）。

目前，解压就可用的懒人包实在太方便了，是最推荐的方式。你也可以自己搭建环境，一步步部署，如果你是MAC系统的话。具体如何安装WebUI可以参考这两篇：

[ ** 安装WebUI（工具篇）  **
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484586&idx=1&sn=d48a436c86f8b0788469996cff622ddc&chksm=97a4329ba0d3bb8dbba4aa3352a8c025431c7e81292342d66b15c7b48342b23373fb496c5fe0&scene=21#wechat_redirect)
** **

[ ** WebUI常见问题（工具篇）  **
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484517&idx=1&sn=298f5c67b48fed275b5104f99d9ee3b7&chksm=97a43254a0d3bb4227e06b13975f9dfda7d1e59a27dbcfdb8085f2274f0964f22c90cf9271a6&scene=21#wechat_redirect)
** **

  

** 模型  **

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5OKCwshyLbLgyYkUliahWcfut9OgMrcCWMzrYtAGBUdvqY9Ksib1eDn4n3P8TV55fbSXibdHS60tZ9g/640?wx_fmt=png)

模型是aigc的灵魂，所有的生态都是围绕模型展开的，模型在某些维度上决定了出图的风格，内容和质量。

Tips：  因为先有的是扩散模  型，再有的现在大热的图像生产，再才诞生了WebUI这些围绕模型服务的工具，  模式等（过去的模型并没达到这个高度，
限定不追溯AI发展史防杠）

模型的获取主要源自：自己 **训练** ，和 **下载** 。

因为SD的开源性，我们可以自己通过训练集finetune（微调）或者Mix（融合）SD的大模型来得到一个特定风格化的模型，然后分享出来提供他人下载使用。从而得到越来越多丰富多彩的模型去解决我们的生产需求。  

上面提到的懒人包中通常有一个模型提供，如果没有可以自行从下面2个网站下载，  别问我图里为啥这么多马赛克

  * ** civitai  ** https://civitai.com/ 

  * ** huggingface  ** https://huggingface.co/ 

  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5wtvRxKRkN4GWicE93NRia422eSDxa0kke4YFBJG9qicqaAjphNuNWTfuKXCyaYlTKjB1Fxa0m2Cpbw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At7iaoFZian8hx8Z34NCgaTlicL5gXCjILlBXmCibkFBC8xicibbnlIlDnFy5Tlsx7uPD3YEXk4SCo7cUb5w/640?wx_fmt=jpeg)

  

关于模型的更多格式版本补充可以看这篇：  

[ ** 关于model你需要知道的二三事（模型篇）  **
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484587&idx=1&sn=3d55afd18f973250455f31700185b0a5&chksm=97a4329aa0d3bb8ce0a2dfe50367fa90c721668d02b1da9ed3241c6501d6bfb9eb8533d9568b&scene=21#wechat_redirect)

我也会定期推荐优秀的模型给大家  （挖坑2）.

  

** 准备完毕，尝试生第一张图  **

你可以啥也不想，啥也不看，轻轻的用你的鼠标点击一下屏幕上那颗大大的，方方的，  橘黄的生成按钮
，在终端中会显示进度，右下角的区域就出现了一张图，它可能长这么个模样。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5wtvRxKRkN4GWicE93NRia42BgNib1qRc3ydKURTvmQB1EAYibRcJ16ktg1hicL5vcqb8kEoic5MwuGzUw/640?wx_fmt=png)

没有输入任何文字，调整任何参数，这个抽象的图好像还不赖~（你们选择的大模型如果比较写实，那这张图可能更抽象）好像是个不错的开始。

  

** Step1. 先认参数  **

把大象装冰箱，得先把冰箱门打开。同样，想自己生图就需要先认识一下一张图片是由哪些参数得出的。上面我们点了生成按钮，在电脑右下角收获了一张图片，这张图片的下发有一堆参数（每一次生成都有一组参数在这个地方显示）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7iaoFZian8hx8Z34NCgaTlicLTFSf2FYAia49VSbhEShXibLfqrf71F6lnb7FOPZOdeRDYIrVwCjInkTA/640?wx_fmt=png)

Steps:  20,  Sampler:  Euler a,  CFGscale:  7,  Seed:  2607380765,  Size:
512x512,  Modelhash:  b6928134bb,  Model:  25D_mixProV3_v3,  Clipskip:  2,
ENSD:  31337,  Version:  v1.3.2  
  
---  
  
  

** 简单解释这些参数：  **

Steps：  迭代次数，取值与采样方法有关。
代表迭代（渲染）步数。根据图片质量和内容复杂程度，取15-30之间，太高影响较小，也加大运算时间。回报递减，取决于采样器。

Sampler：  采样方法（不同的采样方法有不同的效果和速度），Euler a就很好用，速度也很快。其他采样器也各有特点，需要我们在生产的过程中耐心去试。

CFGscale：
图像与你的提示的匹配程度。增加这个值将导致图像更接近你的提示（根据模型），但它也在一定程度上降低了图像质量。可以用更多的采样步骤来抵消。默认为7，更小ai更具创造力，太高则容易过饱和和混乱，一般少调整。

Seed：  保持这个值不变，可以多次生成相同（或相似）的图像。种子是决定生图结果的随机数。遇到随到不错的种子可以记住这个值下次还找你。通常-1随机。

Size：  就是图片的尺寸。默认都是512x512。更大的图片也意味着需要更多的显存和更长的时间来生成。

Model：  这是我们选择的模型。Modelhash：这是模型的身份证。

ENSD：  对图像质量无任何提升, 只为ancestral采样方法产生不同的结果，无视。

Version：  这是你的sd版本，不用关心。

Clip skip：  这个参数的原理是十分复杂的，而且设置它很频繁，简单理解就是写实图设置1，二次元一些就设置2。有些制作精良的模型介绍也会给出clip
skip值的影响。  ` `

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At5o0HTbIK7RfJ1moIjmIF91ibvIib3B7t1fIbibVnu1BPXVJTH8c5ibwTWuBlSMPjo7gmCUicUFInjib5ibA/640?wx_fmt=jpeg)

  

** Step2. 再次认识WebUI  **  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7iaoFZian8hx8Z34NCgaTlicL1ib16DY2UfjfoKRhYsQDsjAl3N4ibzhk4UzFRCwaQ0uaLiby2apU7ibxEA/640?wx_fmt=png)

我把webUI的界面分成了几个区域，他们按照一定的逻辑归类。

** TAB功能模块：  ** 每个标签在WebUI都是一个独立的功能，如文生图，图生图，训练，设置，以及很多独立的，功能强大的插件。  

** 关键词模块：  ** 这里有2个面积巨大的输入框，分别是正向关键词和反向关键词。这里就是我们用文本控制出什么图的操作台了。  

** 设置模块：  **
有没有很熟悉，这里很多参数都是我们在生成一张图后，显示出来的参数，上面已经有一一介绍，这里通过uikit调整这些参数来控制最终生成的图片是什么样子的。（MJ策略性的隐藏了这部分）

** 生成结果模块：  **
这里预留了一些空间，来实时预览我们的生图过程和展现生图结果，如果有多张图片也会罗列，有一些快捷功能可以操作图片。还有底部有图片参数详细信息和生图过程中的错误反馈。  

** 插件脚本模块：  ** 最后就是插件脚本模块，在生图的前中后周期中都有不同的插件服务，这里会是主要的陈放之所。

  

** Step3. 关键词和基础设置  **

我们在TAB功能模块区找到PNG图像信息（PNG info），切换过去然后将一张AI生成的PNG图片导入进去。我们也会得到这样的一组参数：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5o0HTbIK7RfJ1moIjmIF91w2TP7pcrbfZzNibMOpX5JxcyZMSOLzm3MKlI9EOOQwz1zmkSkSq7x9g/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At7iaoFZian8hx8Z34NCgaTlicLTFSf2FYAia49VSbhEShXibLfqrf71F6lnb7FOPZOdeRDYIrVwCjInkTA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

** 关键词  ** shose, sleek glass thickness,transparent, holographic,smooth color
background,cinematic lighting,4k, Negative prompt(low quality), (worst
quality:1.4)  
---  
** 设置  ** **** Steps:  20, Sampler: Euler a, CFG scale: 7, Seed: 3793992816,
Size: 512x512, Model hash: 9aba26abdf, Model: deliberate_v2, Clip skip: 2,
ENSD: 31337, Version: v1.3.2  
---  
  
  

复习一下上面的知识点。  

这只鞋子的参数是：采样步数20（默认），采样器Eular
a（默认），CFG7（默认），种子balabala，尺寸512（默认），Clip跳过2（默认），模型deliberate_v2。

除了模型和第一次的生成不同外，其他参数都一样的，起到生出这双科技质感的鞋子关键作用的是 ** 关键词+模型  ** 了。

** 关键词：  **

  * Prompt：  对你想要生成的东西进行文字描述。正向关键词可以使用英文的自然语言描述，可以用单词，词组，颜文字，emoji...通过逗号，空格来分割。词汇的 **顺序，重复，权重** ，在模型中语义的 **自带权重** 等都会影响生图结果。 

  

  * Negative prompt：  用文字描述你不希望在图像中出现的东西。反向关键词与上面相同的格式语法，且2者互相 影响。如果填写了仍然出现可以适当的增加权重。格式为(),(()),(xxx:1.6),降权同理[],[[]].[xxx:1.4]。 

  

这里只简单提及关键的影响和基础使用方法。关键词的语法格式，基础范式等更详细的介绍可以看这篇：

[ ** 嘛呢吽-咒语范式（关键词篇）  **
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484592&idx=1&sn=b51c015c17cbcdca1512f7eb6965004b&chksm=97a43281a0d3bb973d651c2b29390dfdf7dc47afa6c88fe443afb7379c7abb7c3b59f126b25c&scene=21#wechat_redirect)
** **

  

** 模型：  **

模型前面已经提及，在生图过程过，WebUI的工作都需要基于某一个大模型，所以在用户界面上，选模型是放在最靠前的位置。
这也是WebUI当下面临的一个问题，随着模型越来越多成为条件因素而不是唯一基础，越来越多需要模型串并联的工作流成为主要的需求解法。

与模型相关联的还有一个参数是VAE。

VAE：
是一种用于学习潜在表示的深度学习技术。它们也被用来绘制图像，在半监督学习中取得最先进的成果，以及在句子之间进行插值。对于小白用户，你可以简单理解它会影响你出图的色彩（其实是有误的，模型篇里有说）。

  

** 基础设置：  **

那是不是前面讲的一大堆参数就都默认不管就行了？

如果在对策入门早期，没有精力理解确实可以不用掌握，都默认即可。但不代表这部分是没用的，看我调整了 **采样器** 和 **采样步数**
后（仍然随机种子），又会得到下面这张图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5wtvRxKRkN4GWicE93NRia429l6tBJqnNSMJHO2TibLicHSrRkibibGZqtC3TmFicgmGrG3OTC5dpCx9aIQ/640?wx_fmt=png)

Steps:  40,  Sampler:  DDIM,  CFGscale:  7,  Seed:  1196435060,  Size:
512x512,  Modelhash:  9aba26abdf,  Model:  deliberate_v2,  Clipskip:  2,
ENSD:  31337,  Version:  v1.3.2  
  
---  
这些参数都会影响到我们的生图结果，受篇幅影响，具体每个参数会产生什么样的影响，可以参见这篇：

#  [ ** 它们都有啥作用（参数设置篇）  **
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484591&idx=1&sn=bca140576f4522ad61708a16e91ba1e8&chksm=97a4329ea0d3bb88fdafa3be709c1899b187d2fc047c761cd7ae5c588a612ccb46c3581baa38&scene=21#wechat_redirect)
** **

#  [ ** 生图和训练当中的辞海（其他参数篇）  **
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247484590&idx=1&sn=153be0769419645814e8b8bb15248458&chksm=97a4329fa0d3bb89dcc04c11076550125fbe4fb09392d5969e8c1beba6753fbd8b107581c021&scene=21#wechat_redirect)

  
** 最后再补充一个经常使用的设置参数：  ** Batch count/Batch size：
决定生成的图片数量。可以简单理解前者生几批图，后者每批生几张图。如果显存足够，则可以增加 Batch Size；否则，只能增加 Batch
Count，得到的图片数量是两者之积（对于显存较小的情况，建议只修改 Batch Count）。

  

** 进阶部分  **

至此，恭喜你，你已经成功把大象装进了冰箱~
至于想再装狮子老虎，就是进阶部分了。主要也就4个部分。分别是图生图（包括局部重绘），WebUI插件，小模型（LoRA、Embedding、Hypernetwork等），以及大小模型的训练finetune（俗称炼丹）。

** 图生图（img2img）&局部重绘（inpaint）  **

图生图其实本质仍然是文生图（txt2img），只是把上传的参考图转出成为了关键词信息，其他参数都与上面提到的文生图参数一致，当你把文生图熟练掌握后，图生图就显得十分简单了。

只多了1个与图片相关的设置：Denoise strength，而inpaint则是在图生图的基础上多了一组蒙版设置。

局部重绘在很多时候能在工作流程上提供很好的解决办法，将生成图片导入局部重绘中，对问题部分进行多次局部重绘，且可进行多次图生图。这里如果使用一些第三方插件如ps插件会更加自如，最新的ps官方也是使用相似的工作原理。

利用好图生图和局部重绘在复杂的工作流中将是一个很重要的技能。后续实战篇会有更多的提及。  （挖坑2）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5o0HTbIK7RfJ1moIjmIF91Ej3CSSdRy5QZaiczttv4ThAic4mlnIGykrH4PSiaNeu5DrtNCA1GNCSwg/640?wx_fmt=png)

  

** 插件  **

得益于良好的开源生态，我们能在webui上使用很多拓展工具，这些插件有的能改变工作体验，有些能实现某些革命性的解决问题的办法。受篇幅影响，我不在这里一一列举，只先管中窥豹一下它们的强大。

值得庆幸的是，很多整合包就整合了很多好用的插件（这也是懒人包的亮点之一，佬与佬的品味差距）比如：

** controlnet：  ** 能用专门的轮廓识别、动作识别、景深识别等预处理模型让需要的对应图片牢牢的control住的神级插件！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5wtvRxKRkN4GWicE93NRia42N4ThuqnK9T2JMX6dkbxicBnibqqxTUWwnjlLO5Gwv93QVibnNLJJ7hNhg/640?wx_fmt=png)

** tagger：  ** 可以通过图像识别，反推关键词的插件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5o0HTbIK7RfJ1moIjmIF91NBtM2PouCX97D1CHvL9mlmgIfPdIYRxiaSRHZgLwmXZTb2bnHXicoUJw/640?wx_fmt=png)

还有dreambooth训练插件，图片浏览插件，动画脚本等等，都是在已经很牛*的工具基础上又提高了生产上限。webui本身就提供了拓展功能，能在拓展页面自己选择需要的插件工具：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5wtvRxKRkN4GWicE93NRia42BjhpGE6jgflxhJiajIl1zNQU2y4wk12GtmIgBicVYBfjmFdr7wA75yVA/640?wx_fmt=png)

更多插件的介绍和使用，会有专门的篇幅介绍，可以关注后续的更新。  （挖坑3）

  

** LoRA、Embedding、Hypernetwork  **

这部分要解释起来还很麻烦，但这些又是进阶的很重要的一部分，大概是很多人使用SD而不用MJ的最核心部分吧。

简单的说，他们就是一个个的微型模型。他们可以在一个模型上串联另一个模型的一部分特征，并且可以修改权重。  

  * ** LoRA：  ** 与下面二者不同，LoRA更接近完整的大模型，这个是出现最晚，但最强的概念。通过少量图片就能很好的微调大模型得到一个文件大小相对很小的模型文件。（大小几兆-两三百兆的.safetensors格式）   

  * ** Embedding：  ** 是Textual Inversion的结果，教 AI 用模型中的标签组成一个 人或者物品。更接近从模型中“找”。是去年还比较流行的炼丹方式，文件很小是优点（大小2kb的.pt格式）。   

  * ** Hypernetwork：  ** 中文叫超网，也是很成熟的一种技术，就像一层层盖棉被一样去改变模型的细节。通过调节权重来改变生成结果，适合调整风格。（大小100-300兆的.pt格式，根据层数决定） 

通过将一个个的大模型与小模型的组合，就能得到很多不同的风格和创意结果。甚至我们很多人都猜测MidJourney的工作原理也是模型的串并联，能让结果的质量控制得很优秀。

同大模型一样，LoRA、Embedding、Hypernetwork文件也能去上面提到的C站，黄脸上下载，更多介绍，大小模型的搭配
更多同样会有专门的篇幅介绍，  可  以关注后续的  更新（挖坑4）。

  

** 炼丹  **

至于如何生产大小模型，想到过年那会儿我没日没夜，废寝忘食的炼丹，炸炉，炼丹...睁眼炼丹，闭眼睡觉的场景就不寒而栗...

其实当下我认为炼丹是一个投入产出比不高的行为。对硬件要求高，对训练集的版权许可又有法律和道德的约束。

所以这个坑也先挖了，以后填  （挖坑5）  。

  

** Hello，New World  **  

与很多代码学习的书籍会用写一个“hello
world”的程序来开始一样，写到最后我会提供一套参数，你可以根据上面学到的知识，把他们对应安放到你的工具当中，快去看看会得到什么样的图吧。

** 关键词  ** ((best quality ,masterpiece, highres)),Illustration,  
Defined ‘real’ light source,detailed light,beautiful detailed glow,  
1girl,10-year-old,solo,long sleeves,railing,brown eyes,brown hair,Blue jean
jacket,White T-shirt,smile,long hair,city,Turn and look back,Look at view  **
** 关键词  ** ** (low quality, worst quality:1.4),(bad-artist:0.7),(bad
hand:1.4),lowres,  
cropped,blurred,mutated,error,deformed  
---  
** 设置  **

Steps: 30, Sampler: DDIM, CFG scale: 10, Seed: 1039378680, Size: 300x400,
Model hash: 89d59c3dde, Model: final-pruned, Clip skip: 2

Hires upscale: 2, Hires upscaler: Latent Denoising strength: 0.7  
  
---  
  
  

模型你可以换成任意模型，感受一下不同模型提供的魔法效果吧。  

记得把高分辨率修复勾选上！~

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At5wtvRxKRkN4GWicE93NRia42wvfJc8N8XSg3K8RPmV4q2BMmxibokVwU1WUaG7Dsht9kxCtEeEegVmA/640?wx_fmt=png)

我们，新世界再见！~災害對策精英们！~

  

** 参考  ** ****

* * *

  

稳定扩撒  

|

https://huggingface.co/blog/stable_diffusion  
  
---|---  
sdbook 术语  
|  https://stable-diffusion-book.vercel.app/GettingStarted/term/#_8  
  
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

