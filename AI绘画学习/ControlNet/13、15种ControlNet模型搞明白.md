## 「ControlNet的终极攻略」

**一、ControlNet究竟能干什么？**

**1.**

**控制人物姿势**能控制生成的人物的姿势、表情，甚至是每一根手指的骨骼

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100700471001.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100700187002.png)

**2.**

**线稿上色**

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100700367003.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100701849004.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100701719005.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100701122006.png)

**3.**

**恢复画质**

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100701725007.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100702734008.png)

**4.**

**动漫变真人**

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100702754009.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100702503010.png)


controlnet还有非常多的功能用法，具体用法会在后面的文章里面详细去讲**二、ControlNet是什么**

**AI**

**绘画最终要实现的目标——让出的图与我们脑海里想象的画面一致**

但目前现状是：随机性太强

很多时候能不能出来一个好看的画面，只能通过大量的「抽卡」实现，以数量去对冲概率

这种情况下，如果能用好控制出图的三个最关键因素，能让「出图与我们想象的画面一致」概率更高

**1.提示词**

**2.Lora**

**3.ControlNet**

提示词的作用是奠定整个图的大致画面  
Lora的作用是让图片主体符合我们的需求  
ControNet的作用是精细化控制整体图片的元素——主体、背景、风格、形式等

提示词的用法我在SD的教程里讲过，这个更多的是需要平时的积累，用AB测试去知道每个词对图片产生的影响，从而养成提示词思维  
Lora模型的训练教程我也写了

而我们这篇文章主要讲的是ControlNet的用法  
把15种模型都给你演示一遍，让你知道每一种模型有什么用，应该怎么用，从而真正掌握ControlNet

**ControlNet**就是你提供一张图片，然后选择一种采集方式，去生成一张新的图片**

比如你提供一个图片  
可以选择采集图片中人物的骨架，从而在新的图片中生成出一样姿势的人  
可以选择采集图片中画面的线稿，从而在新的图片中生成一样线稿的画面  
可以选择采集图片中已有的风格，从而在新的图片中生成一样风格的画面  
用的时候不必拘束于哪一种模型更好，更重要的是你脑海里想要什么样的画面  
多去尝试，也可以结合其他模型一起用，最终把图片变成你想要的画面就可以了


**详细的讲解Controlnet的具体操作步骤：**


现在我们需要让黑色衣服的小姐姐摆出白色衣服小姐姐的动作,得到最右边的照片

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100703422016.png)

**1.基础设置**

首先我们先正常的生成出来一张满意的照片  
这里的基础设置就是：选大模型、写关键词、用Lora、参数设置等等  
这一步的内容在Stable Diffusion的教程里面都有详细讲到，这里就不再具体去拆解了如果忘记了或者有不懂的可以回去翻SD的教程

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100704510017.png)


这时候直接点击生成就得到了一张比较满意的照片

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100704896018.png)


为了等一下加上controlnet控制姿势也能生成出来一样的照片  
我们要固定照片的随机数种子

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100704131019.png)


接下来我们就在controlnet里面控制小姐姐的姿势

**2.controlnet**

**的使用**

controlnet

的使用方法就只有两步

·上传图片

·选模型


滑到SD最下面打开controlnet的面板

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100704870020.png)


上传一张人物姿势的照片  
下面的“启用”按钮一定要打开，其他按钮可以按照我的选电脑显存比较低还可以打开“低显存模式”，但是照片生成速度会比较慢

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100704404021.png)


看到控制类型有很多个选项，这个其实就是快捷键  
选中“OpenPose”  
就会自动帮我们加载预处理器和模型

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100705737022.png)


点开 预处理器 的选项卡，里面的所有预处理器都是去识别照片姿势的的，只是识别的东西有多有少  
我们这里就用最普通的“openpose”其他的会在后面细讲

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100705564023.png)


点击爆炸按钮 “ ” 就可以在图片右边看到预处理之后的人物姿势线条

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100705335024.png)


最后点击生成，小姐姐就摆出我们指定的姿势了

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100704896018.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100705657025.png)


controlnet的不同功能的实现其实就是上传不一样的照片，然后选用不一样的预处理器和模型  
**一般情况下，预处理器和模型名字一样，是配套使用的**

controlnet是辅助我们生成想要的照片的一个工具  
我们的大模型和关键词也非常关键  
要换照片风格一定要记得换大模型

二次元图片用anything  
真实照片可以用chilloutmix

接下来我们就看一下每一种预处理器和模型都有什么用**五、姿势约束**这一节讲的是openpose模型，主要控制生成照片人物的姿势  
这里的姿势有身体姿势、表情、手指形态三个  
可以只控制某一个或者两个，也可以三个一起控制

身体姿势  
身体姿势+脸部表情  
只有脸部表情  
身体姿势+手指+表情  
身体姿势+手指

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100705329026.jpg)

**1.**

**控制身体姿势**  
一般情况下，在SD里面生成一张照片，照片人物的动作都是随机的  
但controlnet可以让生成出来的人物摆出任何你想要的姿势

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100706927027.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100706756028.png)


首先我们正常设置大模型和关键词  
然后打开controlnet，上传自己想要生成的姿势照片  
controlnet的模型选择：**预处理器：openpose**模型：openpose**

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100706936029.png)


点击预处理的爆炸按钮就可以看到，模特的姿势被提取成了一个火柴人  
里面的小圆点就是人体的重要关节节点

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100706481030.png)


看看生成出来的照片，模特的姿势就几乎完全复刻出来了

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100706483031.png)

**2.**

**控制人物姿势和手指**除了识别人物整体的姿势以外，还可以识别手指的骨骼  
这样在一定程度下就可以避免生成多手指或者缺少手指的照片

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100707527032.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100707692033.png)


具体的操作跟前面是一样的  
只是预处理器的选择不同  
controlnet的模型选择：**预处理器：openpose\_hand**模型：openpose**

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100707917034.png)


看看SD预处理之后的火柴人，在人体整体姿势的基础上，还多了线条和节点表示手指

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100707238035.png)

**3.**

**控制人物表情**

openpose

除了控制人物的姿势，还可以控制人物的表情但是用controlnet复刻人物表情比较适合放特写的大头照  
这样识别出来的五官才会更加精确  
相对应的也只能生成出来大头照

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100707590036.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100708654037.png)


这里我们又换了一个预处理器  
controlnet的模型选择：**预处理器：openpose\_faceonly**模型：openpose**

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100708404038.png)


预处理之后就是把模特的脸型五官用点描出来

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100708327039.png)


看看生成出来的照片，脸型和五官在一定程度上都还原了

但是，如果你生成的照片用了Lora

再用controlnet控制表情可能会导致生成出来的照片跟Lora的人不太像  
因为生成出来的照片的人物五官和脸型都被controlnet影响了

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100708654037.png)

**4.**

**全方面控制人物姿势**这里我们是把人物的整体姿势、手指、表情都复刻了

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100708518040.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100709232041.png)


controlnet的模型选择：**预处理器：openpose\_full**模型：openpose**

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100709268042.png)


看看处理后的照片就会有我们上面说到的所有东西

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100709872043.png)

**5.**

**自由编辑火柴人**有时候预处理器处理出来的火柴人可能会不太准确  
又或者我们需要更加细致的去调节  
这时候我们可以再安装一个插件，这样我们就可以自己去调节预处理之后的火柴人

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100709599044.png)

**01.**

**安装插件的方法：** ①在“扩展”里点击“可下载”页面

②点击“加载扩展列表”

③在搜索框里输入“openpose”

④安装“sd-webui-openpose-editor”

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100709944045.png)


⑤点击“已安装”页面⑥点击“应用更改并重载前端”按钮

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100710856046.png)


这样插件就安装好啦！

**02.**

**插件的使用方法**接着我们回到controlnet里面  
点击预处理后的图像旁边的“编辑”按钮，就可以自行去编辑火柴人的节点

如果打开编辑按钮是空白的，那就先点击一下预处理之后的图片，再去编辑

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100710727047.png)


把鼠标放到圆形节点上面，就可以调整位置  
调整好了之后，点击左上角的“发送姿势到controlnet”就可以啦

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100710799048.png)


这样通过自己的调节，把腿的节点拉长，就可以生成一个大长腿美女了

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100710628049.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100711566050.png)

**6.**

**小结**识别人体姿势有五个预处理器，在这里有一些我自己选预处理器的小技巧  
在日常使用中，如果原图的手指骨骼比较清晰，可以用识别到手指的预处理器  
如果识别出来的手指线条比较乱，自己调整也没调整好，那就只识别身体姿势  
不然生成出来的照片手指反而更乱了  
控制表情的最好用在生成近景特写图片，这样识别出来的才比较准确

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100711645051.png)

**六、线条约束**这一节会讲到lineart、canny、softedge、scribble、mlsd五种模型它们都是用来提取画面的线稿，再用线稿生成新的照片

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100711392052.png)

**1.lineart**

lineart

是一个专门提取线稿的模型，可以针对不同类型的图片进行不同的处理  
点击选择“Lineart”，预处理器和模型就会自动切换

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100711711053.png)


点开预处理器  
里面的各种模型可以识别不同图片的线稿

动漫：lineart\_anime 或 lineart\_anime\_denoise素描:lineart\_coarse  
写实：lineart\_realistic  
黑白线稿：lineart\_standard

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100711986054.png)

**01.**

**动漫照片**提取动漫的线稿，再重新上色

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100712989055.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100712514056.png)


首先处理动漫照片记得要换二次元的大模型  
然后关键词可以写一些质量词，然后描述一下照片里面有什么东西  
另外需要注意的是，图片的分辨率大小要设置的和原先的比例一样不然照片会自动裁剪放大

controlnet的模型选择：

**预处理器：lineart\_anime**或**lineart\_anime\_denoise**模型：lineart**

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100712913057.png)


可以看一下两个预处理器出来的效果，选一个自己比较喜欢的就可以


lineart\_anime

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100712899058.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100713806059.png)

lineart\_anime\_denoise

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100713650060.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100713164061.png)

**02.**

**素描照片**

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100713407062.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100701849004.png)


controlnet的模型选择：

**预处理器：lineart\_coarse**模型：lineart**

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100714673063.png)

**03.**

**写实照片**可以上传自己的照片，提取出线稿，然后生成自己的二次元头像

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100714983064.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100714638065.png)


要生成二次元照片，一定要先换成合适的大模型

controlnet的模型选择：

**预处理器：lineart\_realistic**模型：lineart**

因为真人照片换成二次元在五官比例上会不太匹配，这时候我们就要适当把controlnet的权重降低

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100714335066.png)


还可以将真实的照片转换成真实的照片，生成一个长的很像的人

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100714485067.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100715468068.png)

**04.**

**黑白线稿**

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100715386069.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100715265070.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100715240071.png)

controlnet

的模型选择：

**预处理器：lineart\_standard**模型：lineart**

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100716715072.png)

**2.canny**

canny

可以识别到画面的最多的线条，这样就可以最大程度的还原照片  
但是比较适合二次元照片

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100716342073.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100716690074.png)


controlnet的模型选择：

**预处理器：canny**模型：canny**

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100716805075.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100716781076.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100717197077.png)

**3.softedge**

softedge

只能识别图片大概的轮廓细节，线条比较柔和，这样给SD发挥的空间就比较大

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100717430078.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100717572079.png)


controlnet的模型选择：

**预处理器：softedge\_pidient**模型：softedge**

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100717343080.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100718182081.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100718475082.png)

**4.mlsd**

这个模型只能识别直线，所以只适合拿来做房子的设计

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100718517083.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100718702084.png)


controlnet的模型选择：

**预处理器：mlsd**模型：mlsd**

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100718575085.png)


看看预处理出来的图，都只有直线  
绿色植物和瓶子这些有弧度的线条都会被忽略掉

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100719667086.png)

**5.scribble**

这一个功能和图生图的涂鸦功能一样  
可以将自己随便画的东西放进去，通过输入关键词得到有着一样线条的照片

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100719500087.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100719157088.png)


controlnet的模型选择：

**预处理器：invert**模型：scribble**

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100719753089.png)

**6.**

**小结**识别线稿的模型有很多，如果你不知道什么情况下用哪个好，可以参考一下我的选择  
1.想最大程度还原照片：canny  
2.只想控制构图，给SD更多可以变化的地方：softedge  
3.真人、素描等照片：lineart  
4.建筑物装修：mlsd**七、空间深度约束——depth**能够很好的复刻房子线条，而且物品的距离镜头的前后顺序比较清晰

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100719101090.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100720907091.png)


controlnet的模型选择：

**预处理器：depth\_leres++**模型：depth**

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100720222092.png)

**八、物品种类约束——seg**识别图片不一样的东西，就用不同的颜色表示

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100720403093.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100720773094.png)


controlnet的模型选择：

**预处理器：seg\_ofade20k**模型：seg**

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100720427095.png)


可以把seg色块图下载下来，自己到ps或者其他修图软件改照片物体的颜色  
这样SD就会根据颜色生成出来特定的某样东西网盘链接里有一份文档，可以看到不同的颜色代表什么物品

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100721838096.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100721629097.png)

**小结**看到这里建筑物装修已经有三种模型可以处理了  
1.只还原整体的结构：mlsd  
2.还原物品的先后关系：depth  
3.比较好的还原原图有的物品，想自己后期编辑色块，改变室内装修结构：seg

depth和seg除了用在建筑上，还可以用在人物照片**九、风格约束**这一节会讲到shuffle、reference、normal、t2ia四个模型

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100721788098.png)

**1.shuffle**

将其他图片的画风转移到自己的照片上  
下面第一张是原图，其他三张分别是由水墨画、油画、赛博朋克风格的图片转移过来的画风

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100721886099.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100721971100.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100722597101.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100722864102.png)


首先先用大模型和关键词生成一张自己喜欢的图片  
固定随机数种子  
然后打开controlnet将别的照片画风转移到自己的照片

controlnet的模型选择：

**预处理器：shuffle**模型：shuffle**

用shuffle可能会影响自己原图的形状，可以稍微调整一下“引导介入时机”的参数  
设置在0.2~0.3之间就差不多  
先生成出来大体的形状再去改变画风  
或者用两个controlnet：一个固定线稿，一个影响画风

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100722398103.png)

**2.reference**

可以很好的还原原图的角色

**01.**

**让照片动起来**让坐着的小狗跑起来

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100722912104.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100722534105.png)


选择写实的大模型  
然后在关键词里面输入：一只狗在草地上快乐地奔跑

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100723594106.png)


controlnet的模型选择：

**预处理器：reference**不用模型**

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100723345107.png)

**02.**

**还原角色**给SD一张人物角色图，它会根据人物的五官、发型还原这个人物

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100723961108.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100723789109.png)


具体操作方法和上面是一样的  
关键词还可以加上情绪的描述，或者不一样的服装发型

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100723817110.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100724709111.png)

**3.Normal**

这个模型可以参考原图的明暗关系，并且还原原图的姿势

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100724327112.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100724586113.png)


controlnet的模型选择：

**预处理器：normal\_bae**模型：normalbae**

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100724921114.png)

**4.t2ia**

t2ia

这个模型比较特殊，不同的预处理器要用到不同的模型

它的主要功能有3个：  
1.将原图的颜色模糊成马赛克再重新生成图片  
2.提取素描的线稿，生成真人照片（这个不好用，直接用lineart就行）  
3.参考原图风格，生成相似风格的照片

参考原图的颜色，将原图模糊成马赛克，再生成图片

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100724263115.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100725833116.png)


controlnet的模型选择：

**预处理器：t2ia\_color\_grid**模型：t2iadapter\_color**

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100725583117.png)

**十、重绘——inpaint**和图生图里的局部重绘差不多，但是inpaint可以将重绘的地方跟原图融合的更好一点

**1.消除图片信息**

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100725300118.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100725917119.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100726688120.png)


关键词填写照片背景的描述词

controlnet的模型选择：

**预处理器：inpaint\_global\_harmonious**模型：inpaint**

inpaint\_global\_harmonious预处理器是整张图进行重绘  
重绘之后整体融合比较好，但是重绘之后的图片色调会改变  
inpaint\_only只重绘涂黑的地方  
为了重绘之后的图片更像原图，可以把控制权重拉满

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100726258121.png)


可以看看在图生图局部重绘出来的效果，是不如inpaint的

这张图是我跑了十几张图之后选的比较好的一张

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100726354122.png)

**2.**

**给人物换衣服**

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100726927123.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100726946124.png)


操作方法和上面一样，只是关键词的描述不一样**十一、特效——ip2p**给照片加特效  
这个功能目前来说没有太多的实际用处，只能拿来玩一下  
比如让房子变成冬天、让房子着火

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100726871125.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100727872126.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100727524127.png)


这里需要输入的关键词比较特殊  
需要在关键词里面输入：make it.... （让它变成...）  
比如让它变成冬天，就输入：make it winter

controlnet的模型选择：

**预处理器：无**

**模型：ip2p**

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100727297128.png)

**十二、加照片细节——tile**

tile

模型的玩法有很多


**1.**恢复画质**

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100701725007.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100728388129.png)


controlnet的模型选择：

**预处理器：tile\_resample**

**模型：tile**

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100728657130.png)


但是这个恢复画质的方法可能不太适合真人  
因为tile模型的工作原理是先忽略掉照片的一些细节，再加上一些细节  
这些SD自己加上去的细节可能会导致生成出来的照片不像原图

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100728108131.png)

![](https://www.wehelpwin.com/Editor/ewebeditor/uploadfile/20230906100728540132.png)

