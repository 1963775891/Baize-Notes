![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At4Tiaice0E5sMKQnCCmq1rZfqrXLu0lWtkarJ2ibiaBv5YE7Vkyy1tybbLe0l3bfxDbCEUTpwr51xQ4OA/0?wx_fmt=jpeg)

#  AIGC常见名词解释（字典篇）

暴躁的卡爷  [ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

** 先热个身  **  
** chatGPT  ：  ** 是由致力于AGI的公司OpenAI研发的一款AI技术驱动的NLP聊天工具，于2022年11月30日发布
，目前使用的是GPT-4的LLM。  
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At4ZTg0vEv5ZcSylfXhflSCnAtCBjjKoR17Y7ico8rh60cs8PRZuoBribjxq3Xhr6lHiaWCJK2ibV7xgBg/640?wx_fmt=jpeg)
额！~ chatGPT我听过，也知道是啥，但你这个解释我直接给我干懵了，套娃呢，解释藏我不认识的单词是不！~  
** AI：  ** 人工智能（Artificial Intelligence）  ** AGI：  ** 通用人工智能 （Artificial
General Intelligence）能够像人类一样思考、学习和执行多种任务的人工智能系统  ** NLP：  ** 自然语言处理（Natural
Language Processing），就是说人话  ** LLM：  ** 大型语言模型（Large Language
Model），数据规模很大，没钱你搞不出来的，大烧钱模型。
这段解释chatGPT的释义，一句话就把关于AIGC的几个常见名词都涵盖了，不愧是去年火到我卖地瓜的二姨都知道的“鸡屁屉”。一个字！绝！  
** AIGC是什么？  ** ** AIGC：  ** AI generated
content，又称为生成式AI，意为人工智能生成内容。例如AI文本续写，文字转图像的AI图、AI主持人等，都属于AIGC的应用。类似的名词缩写还有UGC（普通用户生产），PGC（专业用户生产）等。  
能进行AIGC的产品项目也很多，能进行AIGC的媒介也很多包括且不限于  
** 语言文字类：  ** OpenAI的GPT，Google的Bard，百度的文心一言，还有一种国内大佬下场要做的的LLM都是语言类的。  **
语音声音类：  ** Google的WaveNet，微软的Deep Nerual
Network，百度的DeepSpeech等，还有合成AI孙燕姿大火的开源模型Sovits。  ** 图片美术类：  **
早期有GEN等图片识别/生成技术，去年大热的扩散模型又带火了我们比较熟悉的、生成质量无敌的Midjourney，先驱者谷歌的Disco
Diffusion，一直在排队测试的OpenAI的Dalle·2，以及stability ai和runaway共同推出的Stable
Diffusion...  
** ** ** SD是什么？  ** SD是Stable
Diffusion的简称。是它是由初创公司StabilityAI、CompVis与Runway合作开发，2022年发布的深度学习文本到图像生成模型。它主要用于根据文本的描述产生详细图像。Stable
Diffusion是一种扩散模型（diffusion model）的变体，叫做“潜在扩散模型”（latent diffusion model; LDM）。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4ZTg0vEv5ZcSylfXhflSCnHtCdVPIHVkibs7IKXA2qYSR4atzKYrQFETt7icVJxUmXPlbs8eKEXyug/640?wx_fmt=png)
SD的代码模型权重已公开发布，可以在大多数配备有适度GPU的电脑硬件上运行。当前版本为2.1稳定版（2022.12.7）。

源代码库：github  .com  /Stability-AI  /stablediffusion  
  
---  
我们可以通过一系列的工具搭建准备，使用SD进行想要的图片aigc（心想事成的魔法施与）。

###  

** MJ是什么？  **
MJ是midjourney的简称。Midjourney是一个由同名研究实验室开发的人工智能程序，可根据文本生成图像，于2022年7月12日进入公开测试阶段，用户可透过Discord的机器人指令进行操作创作图像作品。
通过Discord的社区属性，更轻量的产品形态，更简单的生图，且图片质量很高。MJ具备更简单的交互，更直观的生成、放大、保留、分享功能，如果愿意购买更高级的服务，甚至可以享受更快速，更强大的增值服务。
缩写/写作术语表  |  解释  
---|---  
oneshot  |  一张图  
LAION  |  一个图像数据集库，https://laion.ai  
aug  |  augmentaion, 通过裁切，翻转获取更多数据集的方式  
ucg  |  unconditional guidance  
ML  |  机器学习  
LatentSpace  |  潜在空间  
LDM  |  Latent Diffusion Model 潜在扩散模型  
Stable Diffusion  |  稳定扩散  
超分  |  一般指使用 Ai 技术提升图片分辨率，提高清晰度  
黑话  |  解释  
---|---  
NAI  |  (Novel AI，一般特指 Leak)  
咒语  |  prompts，关键词  
施法/吟唱/t2i  |  Text2Image  
魔杖  |  t2i/i2i 参数  
i2i  |  Image2Image, 一般特指全部图片生成  
inpaint  |  i2i 一种 maskredraw，可以局部重绘  
ti/emb/炼丹  |  Train 中的文本反转，一般特指 Embedding 插件  
hn/hyper/冶金  |  hypernetwork，超网络  
炸炉  |  指训练过程中过度拟合，但炸炉前的日志插件可以提取二次训练  
废丹  |  指完全没有训练成功  
美学/ext  |  aesthetic_embeddings, emb 一种，特性是训练飞快，但在生产图片时实时计算。  
db/梦展  |  DreamBooth，目前一种性价比高（可以在极少步数内完成训练）的微调方式，但要求过高  
ds  |  DeepSpeed，微软开发的训练方式，移动不需要的组件到内存来降低显存占用，可使 db 的 vram 需求降到 8g 以下。开发时未考虑
win, 目前在 win 有兼容性问题故不可用  
8bit/bsb  |  一般指 Bitsandbyte，一种 8 比特算法，能极大降低 vram 占用，使 16g 可用于训练
db。由于链接库问题，目前/预计未来在 win 不可用  
  
后面这些难啃一些，随便看看吧  ** 机器学习是什么？  ** ** **
机器学习是人工智能的一个分支。人工智能的研究历史有着一条从以“推理”为重点，到以“知识”为重点，再到以“学习”为重点的自然、清晰的脉络。显然，机器学习是实现人工智能的一个途径之一，即以机器学习为手段，解决人工智能中的部分问题。机器学习在近30多年已发展为一门多领域科际集成，涉及概率论、统计学、逼近论、凸分析、计算复杂性理论等多门学科。  
** 自然语言是什么？  **
自然语言（NLP）认知和理解是让电脑把输入的语言变成有意思的符号和关系，然后根据目的再处理。自然语言生成系统则是把计算机数据转化为自然语言。
是人工智能和语言学领域的分支学科。此领域探讨如何处理及运用自然语言；自然语言处理包括多方面和步骤，基本有认知、理解、生成等部分。  
** AI的推理是什么？  **
推理是指利用训练好的模型，使用新数据推理出各种结论。借助神经网络模型进行运算，利用输入的新数据来一次性获得正确结论的过程。这也有叫做预测或推断。  
** AI的训练是什么？  **
训练是指通过大数据训练出一个复杂的神经网络模型，通过大量标记过的数据来训练相应的系统，使其能够适应特定的功能。训练需要较高的计算性能、能够处理海量的数据、具有一定的通用性，以便完成各种各样的学习任务。  
** 神经网络是什么？  ** 人工神经网络（英语：Artificial Neural Network，ANN），简称神经网络（Neural
Network，NN）或类神经网络，在机器学习和认知科学领域，是一种模仿生物神经网络（动物的中枢神经系统，特别是大脑）的结构和功能的数学模型或计算模型，用于对函数进行估计或近似。神经网络由大量的人工神经元联结进行计算。大多数情况下人工神经网络能在外界信息的基础上改变内部结构，是一种自适应系统，通俗地讲就是具备学习功能。现代神经网络是一种非线性统计性数据建模工具，神经网络通常是通过一个基于数学统计学类型的学习方法（Learning
Method）得以优化，所以也是数学统计学方法的一种实际应用，通过统计学的标准数学方法我们能够得到大量的可以用函数来表达的局部结构空间，另一方面在人工智能学的人工感知领域，我们通过数学统计学的应用可以来做人工感知方面的决定问题（也就是说通过统计学的方法，人工神经网络能够类似人一样具有简单的决定能力和简单的判断能力），这种方法比起正式的逻辑学推理演算更具有优势。

** 参考  **

* * *

  

AI 维基百科

|

https://zh.wikipedia.org/wiki/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD  
  
---|---  
sd  book 术  语  
|  https://stable-diffusion-book.vercel.app/GettingStarted/term/#_8  
人工智能科普  
|  https://zhuanlan.zhihu.com/p/521942102  
  
  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At4Tiaice0E5sMKQnCCmq1rZfqyWfDWNCmkWEjEOGZFq5Q83d8vqaDHTXnENC1BJ7qeEXiaM9V0jHwehg/640?wx_fmt=png)

预览时标签不可点

微信扫一扫  
关注该公众号



轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6iciciaKY5WZ4ib8CVibVnVHRJwGj6ksg7fk0tzTMuLPsvptv6zswtKfCLNFwYr9aIBGkjiaYGBWtibwnOQ/0?wx_fmt=png)

小鱼干了







****



****



  收藏

