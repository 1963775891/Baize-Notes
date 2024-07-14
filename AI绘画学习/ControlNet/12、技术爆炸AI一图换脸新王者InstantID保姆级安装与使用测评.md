#  AI一图换脸新王者，Instant ID保姆级使用测评
__ _ _

接下来说正题。  
在SD中有很多人物换脸的新技术，比如像之前的Roop还有ReActor，它们都可以实现仅凭一张图进行人物换脸，后来又出现了EasyPhoto，可以通过快速炼制的小模型来对人物进行模仿。而最近，controlnet中又加入了一个新成员——Instant
ID。  它可以仅通过一张图片进行完美换脸，可能是目前最强的脸部迁移模型。  **_ _ **

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxib9dvIZBULKTzhrf91eeknaZWrxbfUG1XNMQkTx3QgGrwsnicvGXxibHXA63lWg1RRN6dQwwIPmajc1Q/640?wx_fmt=png&from=appmsg)

与现有的免调谐先进技术进行比较。InstantID 实现了更好的保真度，并保留了良好的文本可编辑性（面孔和样式融合得更好）。  ** _ _ **

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxib9dvIZBULKTzhrf91eeknaZm79Z5tzCibRpEDbsZ6nS6osia1zGzmq29k12MibxAxGJiadffpabMwibYcg/640?wx_fmt=png&from=appmsg)

可以用于特定人物生成广告大片和艺术照，或者是进行视频中的人物换脸。 

**01 **
首先将controlnet升级到最新的版本，目前我的是V1.1.440，可以看到在控制选项中多了一个Instant_ID，这就是我们今天的主角了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxib84rV6h9jTLKxNEdoCQypwQiaWkvt7ch5xjFfdicmz01ibluATkXsBgPlmtoK1Dic5bp477LNtrTRZ6hw/640?wx_fmt=png&from=appmsg)
点开预处理器选项，可以看到有两个新的选项——  **instant_id_face_embedding** **** 和
**instant_id_face_keypoints** **。**
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxib84rV6h9jTLKxNEdoCQypwQI2ClODpgGGCRqZCCKN4InB1lNAYatcujiaLc5lKYWbaKx2WTjPSmqQQ/640?wx_fmt=png&from=appmsg)
与此配套的，我们还需要下载一下最新的controlnet模型。这里我已经给大家整理好了，只需要到我的云盘里就可以直接下载了，然后
将下载好的模型放入到以下路径中——  **E:\sd-webui-aki-v4.4\extensions\sd-webui-
controlnet\models**
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxib84rV6h9jTLKxNEdoCQypwQUDeCNtXCtdVMv4fQHFiadNSZKbAMpZicLhjG230ibbaibLfGTYAWr8ORXg/640?wx_fmt=png&from=appmsg)
除此之外，我们还需要下载5个  insightface的模型，我也在云盘里给大家准备好了。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxib84rV6h9jTLKxNEdoCQypwQcYzUJsmKicvdEPj1NsBWABpNwJSgGYAibcbs7W3FWadf3Nicuic7LoZCzw/640?wx_fmt=png&from=appmsg)  
将模型放到如下的路径当中，如果没有此文件夹可以新建一下——  **E:\sd-webui-aki-v4.4\extensions\sd-webui-
controlnet\annotator\downloads\insightface\models\antelopev2** 重启软件，这样，我们的
Instant_ID就安装好了。  

**_#_**_02_ 使用方法** 

Instant ID 使用 ControlNet 和 IP-Adapter 的组合来控制扩散过程中的面部特征。  

要使用Instant_ID，我们需要开启两个controlnet进行控制。  

在第一个单元中，我们主要进行的是人脸的参考，放入一张人物的正脸照片，因为 ControlNet 模型从 ipadapter 模型获取输出。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxib9dvIZBULKTzhrf91eeknaZsCLUEqibEOtlicpNSL5TonicibKGYtlupZ6kz5c7EebSvicgtrH1ibmRG5Dg/640?wx_fmt=png&from=appmsg)
预处理器选择 **instant_id_face_embedding** ，模型选择 **ip-adapter_instant_id_sdxl** 。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxib84rV6h9jTLKxNEdoCQypwQI9jLib2XVlFPfqbfRUbEGGkicG4nYSORoH8NQHg3O9wU601OasHy2Nibg/640?wx_fmt=png&from=appmsg)
第二个单元是进行人物面部朝向的参考，可以放入一张动作的照片，这个模块参考的主要是头的朝向，脸部是谁并不重要，至于人物的姿态动作会随机生成。  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxib9dvIZBULKTzhrf91eeknaZe9siaZIIA6rzSG1tHw1892UIVIU79aRI06YFMYKgib7H4L92G8ooVc8A/640?wx_fmt=png&from=appmsg)
预处理器选择  **instant_id_face_keypoints** ，模型选择  **control_instant_id_sdxl** 。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxib84rV6h9jTLKxNEdoCQypwQK1dbnfGbIoZyCa8C90OW8RUfkONswdvFxEzA2YuPr6n5yIrrVCQiadg/640?wx_fmt=png&from=appmsg)  

**_#_**_03_ **

** 生图测试**

目前Instant_ID只适用于sdxl大模型，经过我的测试，并不所有的sdxl模型都能产生很好的效果，这里我先选择一个turboDiffusion大模型，并将vae切换为自动。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxib9dvIZBULKTzhrf91eeknaZrPjR87HCwibps1icmtBc5gEDUHtiapicqyO4Tvaj794lI4qyoic9nAiaXlSw/640?wx_fmt=png&from=appmsg)
我输入一段油画风格的提示词内容。  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxib9dvIZBULKTzhrf91eeknaZjBeGEAmeWbM8nRuYbcIh3zF3snwZOIDBKo69Ma3TBf7MjTIic4Q9BfQ/640?wx_fmt=png&from=appmsg)
提示词引导系数这里不能设置为太高，一般在2-4之间效果会比较好。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxib9dvIZBULKTzhrf91eeknaZKx0LM67sPiaPDGjFB6LY0jnS7xfd63WpJKiaruu42b2J9ibI59jHicIMlw/640?wx_fmt=png&from=appmsg)
看一下出图效果，还是挺不错的，脸部也很像。  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxib9dvIZBULKTzhrf91eeknaZ6iavaoQAQGuutiaoySfeDEn2OW7KYia5WFSDHJOK88SCGNm9iaP9ibUMcow/640?wx_fmt=png&from=appmsg)
由于sdxl拥有很多种不同的风格，我们可以试试其他的提示词控制和参考图片，以下是我的一些测试。  
赛博朋克风格。  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibuFercwGmHPy4v4KAhWPKVdlPiaBKYG442waicq1o37apB2TDcuUCMxk9UYsD8dCuxsLlcTBeA5CCg/640?wx_fmt=png&from=appmsg)
日常生活照。  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibuFercwGmHPy4v4KAhWPKVA6l86lQ5qqCfXicSAnlfj7ahA6EKZAaHM62fiaCuRmHeUbs20icQRuwaw/640?wx_fmt=png&from=appmsg)
影楼写真照。  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibuFercwGmHPy4v4KAhWPKVMSnibic48oJib3XIRoqfQTJLN7t0nbpjcMNrib1fdmMCb8LA2bqqC74hwg/640?wx_fmt=png&from=appmsg)
素描绘画风格。  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibuFercwGmHPy4v4KAhWPKVKsbj56ST6U4VmloicyQqGt5Y3nDs73wLa0A0BILXQumoW8UcK0n0fHA/640?wx_fmt=png&from=appmsg)
古装造型。简直太像了！她果然还是非常适合这个造型。  
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibuFercwGmHPy4v4KAhWPKVW5gWacmIK3HZyANGxrqkRCqSqdnw6XibtRC4BhaFgQaC0DmKXDFtmkg/640?wx_fmt=png&from=appmsg)  

关于Instant
ID模型的使用方法就介绍到这里，总体测试下来感觉，人物的相似度还是非常高的，比起之前的一图换脸插件roop的效果提升了不止一点点，甚至可以与lora模型不相上下。不过缺点是，需要使用sdxl模型，对电脑配置有一定的要求，并且大模型的选择和图片选择也会对图片质量产生很大的影响，所以要出好图还是需要多多地尝试。