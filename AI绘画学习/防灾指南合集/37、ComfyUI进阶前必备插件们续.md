![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7ibmdywvp7lFHRJeu4UHmPqb5STzuxVwfdmZjY6lt2pbGu3lkyPYf9k3Q/0?wx_fmt=jpeg)

#  ComfyUI进阶前必备插件们续

原创  暴躁的卡爷  [ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7ib5CUyiaicoiackuSfS6dt97fYhJYKDzFe3yh6YqYfloHETGfyQYySEWbZw/640?wx_fmt=png)

就像WebUI一样，一款工具之所以被大家喜爱，能持续成为生产力，必然和他的生态有着密不可分的关系。（小声BB，fooocus，你看看你）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7ibRBxibh95nWkmpGyo5oKawsEPX9HceVYIBbh33Miac2hZEeRrueIc2U0w/640?wx_fmt=png)

WebUI我们花了大篇幅的去介绍了各种插件，他们分布在一次生成的生命周期前中后，想要提升效率，就不然少不了他们。那ComfyUI也必然有一波让你爱的要死的插件们。

并且只有当你感受到裸感的comfy，你才迫切的需要给ta武装起来。这也是我们学习一个工具需要的节奏，前面3篇已经带了大家进入了新世界，那就由这些🐂🍺的插件让我们畅游爽玩新世界。

先推荐一个Github page，它就帮我们收录了很多好用的插件：

https://github.com/WASasquatch/comfyui-plugins

  

  * 插件安装管理器：https://github.com/ltdrdata/ComfyUI-Manager 
  * SDXL风格样式：https://github.com/twri/sdxl_prompt_styler 
  * ComfyUI界面汉化：https://github.com/AIGODLIKE/AIGODLIKE-COMFYUI-TRANSLATION 
  * 中文提示词输入：https://github.com/AlekPet/ComfyUI_Custom_Nodes_AlekPet 
  * 蟒蛇八卦工具箱：https://github.com/pythongosssss/ComfyUI-Custom-Scripts 
  * #  提示词权重调节器：https://github.com/BlenderNeko/ComfyUI_ADV_CLIP_emb 

  

  

** **▍ ** **必备插件** （ ** ** ** ** ** A航线 ** **** 🤔）  ** ** ** ** **

  

这6款白马已经介绍过了，我就不多废话了，下面给传送门。我推荐的安装顺序是：

[ 爽玩必备！6大插件汇总推荐
](https://mp.weixin.qq.com/s?__biz=MzkzMzIwMDgxMQ==&mid=2247488103&idx=1&sn=2a36742e726d78f5cd2631fdde339602&scene=21#wechat_redirect)
>>>

  

1\. ComfyUI界面汉化 （消除语言障碍先，不行咱还能来回切换）

2\. 插件安装管理器 （这就是所有插件的基地了，强大不言而喻）

3\. 权重调节器 （能用webui的语法进行括号文学，就是👍）  

4\. 蟒蛇工具箱 （可以预览模型效果，webui的模型库分类没白做，还有很多实用工具）

5\. 中文提示词输入 (如果你有稳定的出入网络，那这个插件可以往上提升2个位置，但如果没有，这就用不了。）  

但prompt的填写，因为没有webui上all in one，会让生成工作写词的效率折半，这也是为什么我一直认为all in
one是最强sd插件的原因，至今不变。

6\. SDXL 风格样式 （这个我觉得可以不太需要）  

  

** 但除了以上6个外还有5个必装插件。一定要装好，跑通了，ComfyUI才是生产力！~  **

** 1\. ** comfyui_controlnet_aux  ** **

** ** 2.ComfyUI-Impact-Pack  ** **

** ** 3.ComfyUI_UltimateSDUpscale  ** **

**4.abg-comfyui** **5.comfyui-dynamicprompts**

  

##  ** **** ** ** ** ** ******** ** ** ControlNet 预处理器  ** ** ** ** ** ** **
** ** ** ** ** **

相信CN对于当下的SD生图来说有多重要已经不言而喻了。而CN又分成模型部分和预处理器部分。模型部分我们之前就讲过可以与webui共用。而预处理器部分则需要单独下载和安装。

** comfyui_controlnet_aux  ** ：

https://github.com/Fannovel16/comfyui_controlnet_aux

注意：这里官方提到与老的预处理器是冲突的。

不要下载ControlNet Preprocessors !

不要下载ControlNet Preprocessors !

不要下载ControlNet Preprocessors !

安装就不喂了，所有插件都一律git，  或者下载插件解压  （但建议git安装环境）

  * 

    
    
    git clone https://github.com/Fannovel16/comfyui_controlnet_aux.git

##  

安装好之后，就能在右键新建里找到专属的一个分类节点。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7ibmAg8lxHicvDF1BsWoTT5z3J5mickQT5z6wXoBFVYPUH2vY1CCr22IiaYA/640?wx_fmt=png)

至于如何连接ControlNet和预处理器，我们以后单独说，这里只介绍插件。

** Example 效果：  **  

##  Canny Edge

硬边缘预处理器，熟悉的味道  

###
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7ibxCUQMqRyPT4biavHplSNJH5J4F7Qfp2p9auH97GOSlUZiaibECfyUJngg/640?wx_fmt=png)

###  HED Lines

软边缘预处理

###
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7ibo419klxgD8m56BxFLBrIQwtiaCbR1J3vUxsc0nibvlqGiatl2yTmK8x1A/640?wx_fmt=png)

###  Realistic Lineart

线稿  预处理

###
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7ibVWzoeEpoPiapI2MRibZp6UfEbF6uYcCwqiaiaiaBvAoOfCjYmibXH9c9K8Sw/640?wx_fmt=png)

##  Scribble/Fake Scribble

涂鸦预处理

###
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7ibZPMqxQoPdoVXCQ6VS6t9AniblicibFxeo5EYicfNvuBeWcZbNrRUiaH646Q/640?wx_fmt=png)

##  Normal and Depth Map

常用的2种深度 预处理 Depth (idk the preprocessor they use)

##
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7ibRMIibzfcpCUuM6dUmibr799R1JdElRvmDu0kPPqXyvj23iac7aFwZ8Jpw/640?wx_fmt=png)

##  Zoe - Depth Map

##
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7ibYDryWWX2n6g7q7LjOnYcDCEpoBH1pjpF9WqxibzCEQzulZic978PWX4w/640?wx_fmt=png)

##  BAE - Normal Map

法线预处理。

##
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7ibrmvN47lKo7w0B64D2jXnFzicFcGz1HaagS69eI5PIuY2Hic37WpRxQ5A/640?wx_fmt=png)

##  Faces and Poses

比较牛的是，预处理器里整合了DW pose，直接可以识别手和脸了！  ~  

###
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7ib1lvcX1IlQK0GGicorZ4ZQiaqmB0AUcQAX0yHTQnhXd588O7hYcMH7mrA/640?wx_fmt=png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7ibIgqr24oXREQHPcvTqRhhopgrIgr6gThA71YdicSSACcibt6OR6Kl3mJg/640?wx_fmt=png)

##  Semantic Segmantation

##  我们熟悉的seg，元素分离预处理器。

###
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7ibolWZToo7K3m060ru4QU0b5Xr7sn0n3rQMfbR7OcEdibermFz1Gz3QAQ/640?wx_fmt=png)

##  T2IAdapter-only

##  我不常用的T2I，还有最近更新的上色 Color Pallete for T2I-Adapter
![](https://res.wx.qq.com/t/wx_fed/we-
emoji/res/v1.3.10/assets/Expression/Expression_21@2x.png)

###
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7ibZKtA8E3msG4JxGl6dbMXHicTVjmX0EkPyX07d2LWOIr9nHtnBjuE1CA/640?wx_fmt=png)

  

最后，提供一个测试的工作流，看看你的插件是否work  

https://github.com/Fannovel16/comfyui_controlnet_aux/blob/master/tests/test_cn_aux_full.json

  

##  ** **** ** ** ** ** ******** ** ** ComfyUI-Impact-Pack  ** ** ** ** ** **
** ** ** ** ** ** **

这个就是个重量级的插件了，包含了很多的功能，其中最让人念念不忘，强烈推荐的是它的  DDetailer功能。

安装我就一带而过了，因为之后讲进阶的修脸时候会再次详细介绍如何具体的使用DDetailer。  

  * 

    
    
    git clone https://github.com/ltdrdata/ComfyUI-Impact-Pack.git

##  还可以通过最上面介绍的manager管理插件进行这个插件的安装。  

  

这里面包含了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7ibKObV9viaLMxW40hKYU8etCEQCwp9HYbLZJtlLdC92oukXsYaK6ibIFKA/640?wx_fmt=png)

####  DDetailer基本的自动人脸检测和细化。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7ibdZicrr3JU5OsCqWZ944q5fU68E2vGiau4dicUibVYCbQhyFcHOjetSw62w/640?wx_fmt=png)

  * 由于低分辨率而损坏的面部通过生成和合成以高分辨率恢复，以恢复细节。 

  * “面部细节分析”节点是用于人脸检测的“检测器”节点和用于图像增强的“细节分析”节点的组合。 

  * 将MMDetLoader的bbox模型和SAMLoader加载的检测模型传递给FaceDetailer。由于它执行KSampler的图像增强功能，因此它与KSampler的选项重叠。 

  * 面部细节分析器的 MASK 输出提供了检测到和增强区域所在位置的可视化。 

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7ibcuIibPky4LDicw3CEIg9JSUmvUTwVhpqDWwKHbtEKsbhnJh9MMMPANtQ/640?wx_fmt=png)

这里篇幅受限就先抛砖。一定要装这个插件啊~

  

##  ** **** ** ** ** ** ******** ** ** ComfyUI_UltimateSDUpscale  ** ** ** **
** ** ** ** ** ** ** ** **

接下来的三个都是WebUI中的必备插件，首先是USDU，作为图生图的王牌放大插件，直接就有ComfyUI版的了。

可通过git安装，或者管理器里检索到直接安装。

  * 

    
    
    git clone https://github.com/ssitu/ComfyUI_UltimateSDUpscale --recursive

主要提供了SD放大的参数设置节点，可以直接进行SD放大。这里之后也会细聊。

** **** ** ** ** ** ******** ** **
![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7ibx8AMxbTthuqUaTiaQFFQ3hjlibBGSzPGFyIfNrZic9xmPFBQpQV4AWdKQ/640?wx_fmt=png)
** ** ** ** ** ** ** ** ** ** ** ** **

  

** **** ** ** ** ** ******** ** ** abg-comfyui  ** ** ** ** ** ** ** ** ** **
** ** **

ABG在WebUI就已经介绍过了，属于体量又小，效果又赞的好插件。Webui的介绍看这里：

[ AI生成透明图片？SD“抠图”无敌辣！（实战篇）
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247485066&idx=1&sn=a711105ff5b79ef3311960ee46144b50&chksm=97a430bba0d3b9ad57bf0740d686386be7b6c22de0479dd6386254e27aab181d52980d335550&scene=21#wechat_redirect)
>>>

安装方式这里就建议从Manager管理，Automatic1111替代 里直接找到并安装。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7ib0xT0JAuMMMJgria7PIGhQ3XaWwvF0xjap0zjyC688udFibf2GUiazdPFw/640?wx_fmt=png)

也可以通过，但我好像报过错，所以建议上面的方法。

  * 

    
    
    git clone https://github.com/kwaroran/abg-comfyui git

安装好后有点不好找，在图像分类中。简单抠图还是效果嘎嘎的。  
  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7ibIECfibNyV4FwxMPAiavoyCbTLAazM4Scngs3Rbia6ZZLTibW8OTXUicibq9A/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7iba3sTiaz83h3BJ8RmQyOMhtw4aeUNQscU3QicrxDG0hQAwuST5icgO3HTg/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** comfyui-dynamicprompts  ** ** ** ** ** **
** ** ** ** ** ** **

动态提示词也专门有一期介绍了webui上的魔法词有多香。传送门：

[ Dynamic Prompts插件，魔法提示词由魔法帮你补全（插件篇）
](http://mp.weixin.qq.com/s?__biz=MzIxNDU3MzkxOA==&mid=2247485411&idx=1&sn=da9a1c60fc4eca035dbbe6460e136e7c&chksm=97a431d2a0d3b8c41aa22df5c7596fa16e0b480af581cbf4c9c3e2b0b508dc5cc4f44edf53fd&scene=21#wechat_redirect)
>>>

也一样从Manager安装就行了。

  * 

    
    
    git clone https://github.com/adieyal/comfyui-dynamicprompts git

安装好也会有单独一个分类，具体使用方式其实和webui一样，就不多啰嗦了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7iboqeibknJkhA0CrAJVzEDMeUliceyIUXN389R5iaPOJwZEcI7yFALBJqkQ/640?wx_fmt=png)

还有很多实用的插件、节点、工具。你可以自行在Manager里检索，安装体验。

又遇到特别神的，强烈安利，必装的插件，也欢迎评论留言。  

  

****

** **** ** ** ** ** ******** ** ** **▍ ** **必备插件** （ ** ** ** ** ** B航线 **
**** 🤔）  ** ** ** ** ** **** **  
** ** ** ** ** ** ** ** ** ** ** ** **

  

** B航线... 装插件完全没你啥事... 上云用就完事了....  **

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6So8x4iavkvv7dXBFCPMG7ibDTAW5ibhibpgtCBoPoTJmEbA08o5P3P6TOdEOYNlnINOazNfiaE2k3A3g/640?wx_fmt=png)

** **** ** ** ** ** ******** ** ** 安装  ** **** ** ** ** ** ** ** ** ** ** **
** **

如果实在想体验，那就从下载里一股脑把插件打包，解压到你的ComfyUI文件夹中，路径：ComfyUI_windows_portable\ComfyUI\custom_nodes

完事。

如果报错，就再回到A航线吧，主打就是一个傻瓜不动脑！少动手~  

  

  

  

好了，你已经完成了初见，武装齐全两个部分了，接下来就要开始进阶了，我们会重走一遍webui的生产大道，进行放大，修脸，重绘等一系列进阶操作。

我们下一篇见！~

  

  

** 最后  **

如果对SD防灾对策群感兴趣的也可以关注公众号给 **【小鱼干了】** ，通过公众号的自动回复 **加群** ， **加好友** 等操作。  ****

本期文章提到的ComfyUI安装包、PNG信息图片和工作流，可以公众号回复【下载】获得资源。

  

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

