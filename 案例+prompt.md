

## 一、Checkpoint

#### **1. 奇幻骇客_白棱XL**

![](./note_img/Reference/20240901_170936.jpg)

```markdown
•本模型是一个基于sd xl1.0的2.5d偏写实风格类模型
•推荐尺寸：768*1344，1024*1024，1024*1280等
•推荐步数：30起
•推荐采样：【Euler a】【DPM++ 3M SDE Exponential】【Restart】
•反词推荐：没有反词的图就是【无】(malformed hands, poorly drawn hands, mutated fingers:1.4),
•cfg scale：3.5起步
•放大推荐：使用图生图进行放大处理，采样和出图时一致，步数是出图的1.5-2倍，重绘幅度0.1-0.2
•注意：全身开ad修脸 推荐：【face_yolov8n_v2.pt】，大批量跑图建议开启ad，我的高清图基本都是Ultimate SD upscale放大处理，放大算法 4x-UltraSharp，4x_NMKD-Siax_200k
随便介绍下 2条路线：
栩栩真境XL偏真实类
奇幻骇客XL偏特效类
```
#### **2. UNIT3XL-基础单元-工作流兼容版-AiARTiST**

![](./note_img/Reference/20240901_171823.jpg)

```markdown
常用配置：
Clip Skip 1 / CFG 1.5 / Steps 10 / 采样方法 (Sampler) Euler a / VAE 自动
默认：640 x 1280 ，高清放大 1.5倍，高清重绘幅度0.5，重绘方式 Latent

无HYPER加速推荐配置：
Clip Skip 2 / CFG 7 / Steps 30 / 采样方法 DPM++ 2M Karras / VAE 自动
默认：640 x 1280 ，高清放大 1.5倍，高清重绘幅度0.5，重绘方式 Latent

如果图片尺寸用于出版，可发送到「Tiled Diffusion」或「后期处理」扩大
图片后期处理高清化设置： 8x_NMKD-Superscale_150000_G 可叠加0.5的
4x-UltraSharp 或 R-ESRGAN 4x+ Anime6B
其他出图分辨率：：
Size: 1280x720 / 1536x768 / 960x1920 / 1920x960 / 2048x1024 / 1024x2048

LoRA用法 <lora:Hyper-SDXL-8steps-UNIT:1> 
LoRA权重可以适当微调，在0.5~1均可生效，权重降低后CFG可以适当开大
在LoRA权重为1的时候，CFG Scale 建议为1，权重为0.8时，CFG 1.5 类推
```
#### **3. AiARTiST 专用ACG Playground SDXL**

![](./note_img/Reference/20240901_172405.jpg)

```markdown
常用配置：
Clip Skip 1 / CFG 1 / Steps 10 /Euler a / VAE 自动
默认：640 x 1280 ，高清放大 1.5倍，高清重绘幅度0.5，重绘方式 Latent
其他出图分辨率：：
Size: 1280x720 / 1536x768 / 960x1920 / 1920x960 / 2048x1024 / 1024x2048
推荐Prompts tag清单（加强元素风格描述）：
CinematicVJ,C4D,Surrealist,trend art,realistic,
CG animations,A human head,figure, sculpture,mannequin,fashion art,digital artwork,QRcode，a burst of vibrant colors,paint splashes,transparent bubbles,neon signs,astronaut,cyberpunk style,DJ mixer,space Explosion,robotic Buddha,monks,silver color,depth of field,gauze fluttering,reature limbs and trunk,many holes and patterns on body,starry sky,Science fiction movies,cityscape at night,huge billboard,traffic lights,bustling and lively,surrounded by water,vibrant, colorful grid-like structure,flowing wave, growing light,creating a gradient effect, digital abstract,Particle light,neon colors,abstract shapes,stacked together,three-dimensional geometric structure,deep purple color,geometric,DNA molecule,double helix structure,alternating wavy pattern,connected together等等
电影VJ，C4D，超现实主义，潮流艺术，写实，CG动画、人头、人物、雕塑、人体模型、时尚艺术、数字艺术品、QRcode，一阵鲜艳的色彩，油漆飞溅，透明气泡，霓虹灯，宇航员，赛博朋克风格、DJ混音器、太空爆炸、机器佛、僧侣、银色、景深、纱布飘动，肢体和躯干栩栩如生，身上有很多洞和图案，星空，科幻电影，夜晚的城市景观，巨大的广告牌，红绿灯，繁华热闹，被水包围，充满活力，多彩的网格状结构，流动的波浪，生长的光线，创建渐变效果，数字抽象，粒子光，霓虹灯颜色，抽象形状，堆叠在一起，三维几何结构，深紫色，几何，DNA分子，双螺旋结构，交替波浪图案，连接在一起
```
#### **4. Dream Tech XL | 筑梦工业XL-与光同尘**

![](./note_img/Reference/20240901_173337.jpg)

```markdown
DPM++ 2M Karras,Steps:30,CFG:6
画风推荐提示词：
写实风格/摄影风格：Photography, realistic, portrait
2D动漫/动画风格：anime/cartoon
3D卡通风格：3D cartoon/3D render
虚幻引擎5风格：Unreal Engine 5 render
```
#### **5. DreamShaper XL**

![](./note_img/Reference/20240901_181650.jpg)

```markdown
Turbo 版本CFG：2 ，Step：4-8； DPM++ SDE Karras （不是 2M）
```
#### **6. LEOSAM HelloWorld 新世界 | SDXL大模型**

![](./note_img/Reference/20240901_181922.jpg)

```markdown
负面提示词
“bad hand,bad anatomy,worst quality,ai generated images,low quality,average quality”

832, 1248；896, 1152；1248, 832；1024, 1024；1360, 768；1152, 896；768, 1360；960, 1088；992, 1056；1088, 960；704, 1472；1056, 992；1472, 704；1632, 640；640, 1632；
美学质量描述词五个等级
worst quality \ low quality \ average quality \ best quality \ masterpiece
```
#### **7. helloFlatArt扁平画风**

![](./note_img/Reference/20240901_180915.jpg)

```markdown
推荐设置
采样方法：Euler a, DPM++ 2M Karras, DPM++ 2M alt Karras;
采样步数：28;剪辑跳过：2放大算法：R-ESRGAN 4x+/R-ESRGAN 4x+ Anime6B;
重绘幅度：0.3-0.5;CFG比例：7;VAE ：vae-ft-mse-840000-ema-pruned.safetensors
```
#### **8. **

![]()

```markdown

```
#### **9. **

![]()

```markdown

```
#### **10. **

![]()

```markdown

```
#### **11. **

![]()

```markdown

```

## 二、Lora

#### **1. LYS 透明t&线框_XL**

![](./note_img/Reference/20240901_171322.jpg)

```markdown
基本适用各种物体的设计及展示，人物也可以。使用时，提示词可使用
((transparent, light-painted, wireframe, contour light))
（（透明、光绘、线框、轮廓光））
```
#### **2. 白棱XL_冰和水-控制**

![](./note_img/Reference/20240901_174120.jpg)

```markdown
简介：可动漫人物，可真人模型,可物品
加强冰和水的出现形态，冰和水可以切换按照权重控制
推荐权重：0.7-1
推荐尺寸：如1024*1024，888*1280等
推荐步数：20-50
推荐词：ice and water, ice, water等等
```
#### **3. 商业kvv1**

![](./note_img/Reference/20240901_174418.jpg)

```markdown
应用领域：
游戏与娱乐产业、品牌形象设计、电商产品、运营活动
触发词：shangyekv\(style\)，权重0.6-0.7较为合适，结合controlnet可玩性更高
```
#### **4. 小猪佩奇｜夏日3D电商场景**

![](./note_img/Reference/20240901_175731.jpg)

```markdown
版本触发关键词：
beach,3D rendering, isometric, blender, clean background, Redshift rendering, c4d, 8k,
出图推荐设置：
采样方法：Euler / Euler a;迭代步数：32+;尺寸默认：512x768;高清修复：R-ESRGAN_4x+;高清倍数：x2;高清采样：25+;重绘幅度：0.5+;最终尺寸：1024x1536;LORA权重：0.4～0.7

CN 的 CANY 权重适当加到1.2-1.4，可以先用 1.5 去试验一下，看是否有产出形状，在适当的往下调，可以在加一个 depth，如果 depth 出不来，用lineart 去辅助搭配
```
#### **5. 美妆分子气泡场景lora**

![](./note_img/Reference/20240901_180326.jpg)

```markdown
单元0 SoftEdge (软边缘)或者Canny (硬边缘)（彩色图标）控制权重：0.8-1.1
单元1 Segmentation (语义分割)（黑白图标）控制权重：0.5-0.8
单元2 Tile (分块)（彩色图标） 控制权重：0.6-0.8  引导介入时机：0.1 引导终止时机：0.6
推荐参数：
底模：anything-v5-PrtRE.safetensors
触发词：bubble
DPM++ 2M Karras;Steps：20;
推荐lora权重：0.65-0.85 低于0.65 IP权重丢失，高于0.85容易污染场景;
重绘幅度：0.3~0.5;放大倍数：1.5-2;
图片后期处理高清化设置： 4x-UltraSharp 或 R-ESRGAN 4x+ Anime6B
```

#### **6. 光泽玻璃材质**

![](./note_img/Reference/20240901_182630.jpg)

```markdown
大模型：revAnimated_v122；权重：0.9；建议的步骤数：20至40
高清修复模型推荐：R-ESRGAN 4x+；重绘幅度：0.5(单独主体图标)-0.7(场景)
```
#### **7. **MIRACLE-造梦空间 大师胶片电影风格模拟

![](./note_img/Reference/20240901_182934.jpg)

```markdown
触发词：INJECTION (可不填写)
推荐lora权重：0.3~0.7，权重不同电影风格强弱变化，增加大师元素0.6就够了，0.5为中值，可以根据需要自行调节lora权重。（权重0.3只增加电影感,常用0.5）
采样步数：30~50；CFG:7~8；写实模型：DPM++ 2M Karras ，绘图模型：Euler a
推荐分辨率：640x1280；重绘幅度0.4-0.6
高清化：8x_NMKD-Superscale_150000_G 自带胶片底噪
大模型： LEOSAM HelloWorld 新世界,SDS_FILM/胶片摄影
叠加使用Lora:SDS_Film Grain_XL_SLIDER 还原底噪
```
#### **8. mw_bpch_扁平风格插画**

![](./note_img/Reference/20240901_183225.jpg)

```markdown
触发词：bp_ch
lora权重：0.7~0.8，采样方法：Euler a，dpm++ 2m karras ，
高清修复：R-esrgan 4x+ 重绘幅度0.5左右
大模型：mw_Anime Painting
正向提示词示例：bp_ch, 1girl, solo, black hair, closed eyes, plant, shirt, computer, long hair, blush, laptop, earrings, jewelry, upper body, white shirt, leaf, profile, short sleeves, hand up, sitting, white background
负向提示词示例：easynegative,dark,bad hands,bad feet,worst quality,low quality,normal quality,bad artist,bad anatomy,
```
#### **9. 简白_夏日海滩电商场景**

![](./note_img/Reference/20240901_183500.jpg)

```markdown
触发关键词：
jianbai E-commerce,jianbai summer beach,
大模型：电商场景MIX；放大算法：R-ESRGAN 4x+ 或者 ESRGAN_4x
DPM++ SDE Karra ；权重 0.8
正向：
jianbai E-commerce,jianbai summer beach,3D cartoon, colorful beach scene with lounge chair and swimming ring on the sand, in the style of Pixar, cute and playful character designs, side view, background is a blue sky and white clouds, rocks in the water, palm trees, colorful beach toys, bright color palette with high resolution and high details.
简白电子商务，简白夏季海滩，3D卡通，沙滩上躺椅和游泳圈的彩色海滩场景，皮克斯风格，可爱俏皮的人物设计，侧视图，背景是蓝天白云，岩石水中的棕榈树、色彩缤纷的沙滩玩具、高分辨率和高细节的明亮调色板。
```

#### **10. 电商模型-直出电器化妆品类海报场景kv-静物摄影**

![](./note_img/Reference/20240901_184238.jpg)

```markdown
推荐麦橘V7，极氪白V6，烟上月，DgirlV5，
步数推荐30，512*768；高清修复10-20 步数 R-ESRGAN/4x；DPM++ 2M Karras；权重:0.6-0.8
提示词自己更改优化-可以出空白场景，也可以直接输入具体产品自动出产品海报
化妆品提示词：dianshang,no humans,curtains,<lora:dianshang2-000014:0.6>,cosmetics,white desktop,bottle,close-up,
风扇提示词推荐：dianshang,no humans,curtains,<lora:dianshang2-000014:0.6>,white desktop,close-up,bladeless fan,
加湿器提示词：dianshang,no humans,curtains,<lora:dianshang2-000014:0.6>,plant light and shadow,humidifier,mist,cosmetics,white desktop,
空白场景提示词：dianshang,no humans,indoors,curtains,<lora:dianshang2-000014:0.6>,white countertop,plant light and shadow,plant,
电饭煲提示词：dianshang,no humans,<lora:dianshang2-000014:0.6>,rice cooker,solid wood table,

```
#### **11. Sim简约插画-XL-lora**

![](./note_img/Reference/20240901_184537.jpg)
![](./note_img/Reference/20240901_184606.jpg)

```markdown
Steps: 20, Sampler: DPM++ 2M, CFG scale: 5-7
分辨率：832*1248（主要）、896*1152（其次）、768*1360（其次）
lora权重：测试下来0.2-1
```
#### **12.绿意盎然春色茶饮**

![](./note_img/Reference/20240901_185741.jpg)

```markdown
推荐权重:0.5~0.8。
推荐模型：ReVAnimated_v122
可选关键词:A cup surrounded by greenery 一个绿色植物环绕的杯子, Moss Micro Landscape 苔藓微景观, greener 绿色
触发词：green；CFG Scale:7；DPM++ 3M SDE Karras；放大算法： 4x-UltraSharp
```
#### **13.粘土世界—风景版**

![](./note_img/Reference/20240901_190033.jpg)

```markdown
权重推荐0.6-1
大模型推荐  ReVAnimated_v122；放大算法：4x-UltraSharp；迭代步数：30左右；DPM++ SDE Karras
VAE：840000-ema-pruned.safetensors；CN：tile
反向
ng_deepnegative_v1_75t,badhandv4 (worst quality:2),(low quality:2),(normal quality:2),lowres,bad anatomy,bad hands,normal quality,((monochrome)),((grayscale)),
```
#### **14. **Alice_v1 爱丽丝

![](./note_img/Reference/20240901_191136.jpg)

```markdown
-创意概述：提示词可以用各种颜色的花，如：黄色的花，橙色的花，白色的花，蓝色的花，还有鸟、建筑、帽子花等
-生成建议：真实底模权重:0.5或以下；二次元底模使用full body生成全身图。
重绘幅度建议0.4-0.45
```
#### **15.**MW_button card drawer

![](./note_img/Reference/20240901_191545.jpg)

```markdown
触发词：mw_an, button；权重：0.7~0.9，
步数：20 建议采样方法：Euler a
高清修复：r-esrgan 4x+ 重绘：0.5
推荐模型： MW_Anime Painting 2D
```
#### **16. 踏山听海**

![](./note_img/Reference/20240901_191940.jpg)

```markdown
Clip 1；权重：0.8左右，0.6以下，可以展现全景微观世界
正面：masterpiece, best quality, ultra high res, mini_world, the mini world composed of ancient architecture and a mountain & river and bridge, vivid color, <lora: Mountain Listening to Sea[min world]: 0.8>, c4d, potted plant_style,
杰作，精品，超高解析，迷你世界，古建筑与山水桥组成的迷你世界，色彩鲜艳，lora: Mountain Listening to Sea[min world]：0.8>，c4d，盆栽_风格 ,
负面：(worst quality, low quality, NSFW:2), ng_deepnegative_v1_75t, EasyNegative,
（最差质量、低质量、NSFW:2）、ng_deepnegative_v1_75t、EasyNegative、
```
#### **17. **国风山水

![](./note_img/Reference/20240901_192412.jpg)

```markdown
权重: 0.7~0.8；触发词: jijian；CFG Scale: 7；DPM++ 3M SDE Karras；放大算法: 4x-UltraSharp
正向
Lushan, (Masterpiece, High Quality, Superior Quality, Beauty and Aesthetics): 1.2), Lushan Waterfall, Embroidery, Golden Water Flow + Ink Blue Mountains, Minimalist Mountain Shape Combines of Minimalist Lines, next to colorful floral designs, delicate watercolor, animated gifs, organic and flowing forms, french countryside, joyful figurative art, light emerald and amber, mountain, green plants, milky transparent water, product poster, moss micro-landscape, green, simple, clean light color background, ray tracing, foreground occlusion, natural light, jungle, lushan Optional keywords: jijian, blue sky, close-up, cloud, cloudy sky, day, foot fog, mountain , mountainous, horizon onsen outdoors, sky snow, solo steam water Optional keywords: jijian bird building city cloud cloudy sky fog horizon & nbsp; mountain mountainous horizon no humans outdoors scenery sky sunset tree very long hair water 
庐山，（杰作，高品质，精品，美感和美学）：1.2），庐山瀑布，刺绣，金水流+水墨蓝山，极简线条的极简山形组合，旁边色彩缤纷的花卉图案，细腻的水彩，动画gif，有机和流动的形式，法国乡村，欢乐的形象艺术，浅翡翠和琥珀，山，绿色植物，乳白色透明水，产品海报，苔藓微景观，绿色，简单，干净的浅色背景，光线追踪，前景遮挡、自然光、丛林、庐山可选关键词：极间、蓝天、特写、云彩、阴天、白天、脚雾、山地、山区、地平线温泉户外、天空雪、独奏蒸汽水可选关键词：极间鸟楼城云 阴天 雾 地平线山山地平线无人户外风景天空日落树很长的头发水
反向
text, 
```
#### **18. **

![]()

```markdown

```
#### **19. **

![]()

```markdown

```
#### **20. **

![]()

```markdown

```
#### **21. **

![]()

```markdown

```
#### **22. **

![]()

```markdown

```
#### **23. **

![]()

```markdown

```

## 三、案例

#### **1. 抖音(透明玻璃花升级版)**

![](./note_img/Reference/20240831_162757.jpg)

```
prompt:
masterpiece, best quality, glass texture, flowers, plant, many flowers, surrounded by growing plants, (transparent), best quality, (Pixar-style:1.4), (At Night:0.8), Ultra-detailed aesthetic, beautiful composition, rich bright colors, volumetric soft light, reflection in the water, water ripple. Inspired by Alice in Wonderland, unreal Engine, octane render, 3D rendering,
杰作，最佳品质，玻璃质感，花卉，植物，许多花朵，周围环绕着生长的植物，（透明），最佳品质，（皮克斯风格：1.4），（夜间：0.8），超细致的美感，美丽的构图，色彩丰富鲜艳，体积柔和的光线，水中倒影，水波纹。灵感来自爱丽丝梦游仙境，虚幻引擎，辛烷渲染，3D渲染

negative_prompt:
((spots), (low quality, worst quality:1.4), EasyNegative, EasyNegativeV2, nsfw,

Sampler: Euler a
Base Model: ReVAnimated_v1.22
ControlNet: lineart
LoRA1: Messy glass tentacle_1.0, Weight 0.8
LoRA2: 3D rendering style_3DMM_V11, Weight: 0.4
LoRA3: glasssculpture, Weight: 0.3 (Download v2.0)
```

#### **2. 抖音-二次元**

![](./note_img/Reference/20240831_162807.jpg)

```
正向关键词
(masterpiece:1.2), best quality, (the blue sky surrounded by clouds:1.3), small flower, Forest, floral, sunny, plant, stream, illustration, lake, day, Children's illustrations, scenery, watercolor painting, outdoors, plant, highres, extremely detailed wallpaper, 8k, insane details, intricate details, hyperdetailed, hyper quality, high detail, ultra detailed, look up, look from the bottom up, graffiti,
（杰作：1.2），极品，（白云环绕的蓝天：1.3），小花，森林，花卉，阳光，植物，溪流，插画，湖泊，白天，儿童插画，风景，水彩画，户外，植物, 高分辨率, 极其详细的壁纸, 8k, 疯狂的细节, 复杂的细节, 超详细, 超品质, 高细节, 超详细, 向上看, 从下往上看, 涂鸦,

反向关键词
((simple background)), lowres, bad anatomy, bad hands, text, error, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry BadDream UnrealisticDream,

采样：DPM++2 M SDE Karras
Base Model: 安妮ani~二次元私模_v1.0
ControlNet Weight: 1,
LoRA: CJ Cartoon|儿童绘本卡通插画_v2.0
```

#### **3. 快手-幻彩世界**

![](./note_img/Reference/20240831_162815.jpg)

```
正向关键词
(the blue sky surrounded by clouds:1.3), Illustrative style, an image of a bioluminescent celestial mushroom paradise forest, flowers, fantasy, illustration, animation, stylized, (fractal art:1.3), colorful, thistles and thorns, masterpiece, highest quality, cloud, in spring, on the ground, vegetation, road, miniature photography, warm tone, mushroom house group, car, highway, house, aurora,
（被云包围的蓝天：1.3），插画风格，生物发光天蘑菇天堂森林的图像，花朵，幻想，插图，动画，风格化，（分形艺术：1.3），色彩缤纷，蓟和荆棘，杰作，最高质量、云、春天、地面、植被、道路、微型摄影、暖色调、蘑菇屋群、汽车、高速公路、房子、极光、

反向关键词：
Realistic, EasyNegative, (worst quality, low quality:1.4), (depth of field, blur:1.2), (greyscale, monochrome:1.1), 3D face, cropped, lowres, text, (nsfw:1.3), (worst quality:2), (low quality:2), (normal quality:2), lowres, normal quality, (grayscale), skin spots, acnes, skin blemishes, age spot, (ugly:1.331), (duplicate:1.331), (morbid:1.21), (mutilated:1.21), (tranny:1.331), mutated hands, (poor draw hands:1.5), blur, (bad anatomy:1.21), (bad proportions:1.331), bs, extra disfigured (1.331), (missing arms:1.331), (extra legs:1.331), (fused fingers:1.61051), (too many fingers:1.61051), (unclear eyes:1.331), lowers, bad hands, missing fingers, extra digit, bad hands, missing fingers, ((extra arms and legs))), freckles, (white border:2), nsfw,

采样：DPM++2 M karras
Base Model: AWPainting_v1.3
ControlNet: Same as above invert+grcode monster		Weight: 1.2-1.4
LoRA: Iridescentpainting I幻彩插画_v1.0	Weight 0.6
LoRA2: CJ Cartoon|儿童绘本卡通插画v2.0	Weight 0.2
```

#### **4. 抖音-造梦无界**

![](./note_img/Reference/20240831_162826.jpg)

```
正向关键词
(masterpiece:1.2), best quality, sunny, (the blue sky surrounded by clouds:1.3), (building:1.3), Science and technology, modern city, city of the future, day, scenery, outdoors, plant, highres, original, extremely detailed wallpaper, 8k, insane details, intricate details, hyperdetailed, hyper quality, high detail, ultra detailed, look up, look from the bottom up, Cities of the future, skyscrapers,
（杰作：1.2）、最佳品质、阳光明媚、（白云环绕的蓝天：1.3）、（建筑：1.3）、科技、现代城市、未来城市、白天、风景、户外、植物、高清、原创，极其详细的壁纸，8k，疯狂的细节，复杂的细节，超详细，超质量，高细节，超详细，抬头，从下往上看，未来的城市，摩天大楼，

反向关键词：
(worst quality:2), (low quality:2), (normal quality:2), lowres, bad anatomy, bad hands, normal quality, (monochrome), (grayscale),

采样：DPM++2 M SDE Karra
Model: chilloutmix_NiPrunedFp32Fix
ControlNet invert Model: control_v1p_sd15_grcode_monster 1.6,
LoRA1: Future City v1 Weight 0.8 
LoRA2: Iit Weight 0.35 (Brighten the picture lora, download from the cloud)
LoRA3: New Sci-Fi Neo Sci-Fi_v1.0 Weight 0.5
```

#### **5. 快手-夏日气球**

![](./note_img/Reference/20240831_162836.jpg)

```
正向：
(top view:1.2), (inflatable balloon material:1.2), transparent plastic, outdoors, day, water, tree, blue sky, no humans, ocean, beach, sand, palm tree, swimming pool, beachball, masterpiece, best quality, studio lighting, Realistic rendering details, c4d, blender, octane render, 8k, no one,
（顶视图：1.2），（充气气球材料：1.2），透明塑料，户外，白天，水，树，蓝天，没有人类，海洋，海滩，沙滩，棕榈树，游泳池，沙滩球，杰作，最佳品质、工作室灯光、真实渲染细节、c4d、搅拌机、辛烷渲染、8k、没有人、

反向：
((nsfw)), sketches, (worst quality:2), (low quality:2), (normal quality:2), lowers, facing away, looking away, text, error, extra digit, fewer digits, cropped, jpeg artifacts, signature, watermark, username, blurry, skin spots, acnes, skin blemishes, bad anatomy, fat, bad feet, cropped, (poorly drawn hands:1.3), (poorly drawn face:1.3), mutation, deformed, tilted head, bad anatomy, bad hands, extra fingers, fewer digits, extra limbs, extra arms, extra legs, malformed limbs, fused fingers, too many fingers, long neck, cross-eyed, mutated hands, bad body, bad proportions, gross proportions, text, error, missing fingers, missing arms, missing legs, extra digit, extra arms, extra leg, extra foot, missing fingers, (nipple:1.3), perspective outfit, complex background, (people:1.3), (girl:1.2), (man:1.2), (woman:1.2),

采样：DPM++2 M Karras
Base Model: ReVAnimated_v1.22,
controlnet: lineart Weight: 1
IP-adapter (Because the padding image has characters, the output image may have characters that need to be filled in with PS style painting and retouching)
LoRA1: Creative | Inflate effect Weight 0.6
LoRA 2: shangyekvv Weight 0.6
```

#### **6. 超级符号机甲风**

![](./note_img/Reference/20240831_162851.jpg)

```
正向：
(gray background:1.4), machinery, extreme detail, future, science and technology, concept artist, fantasy art, miniature, (best quality), (masterpiece),
（灰色背景：1.4）、机械、极致细节、未来、科技、概念艺术家、奇幻艺术、微型、（最佳品质）、（杰作）、

反向：
nsfw, (worst quality, bad quality:1.3),

采样：DPM++2 M SDE Karras,
Base Model：ReVAnimated_v1.22
LoRA: 光环风格机甲, 权重:0.4
LoRA2: NijiMecha-机甲风, 权重:0.7
```

#### **7. 夏日图标**

![](./note_img/Reference/20240831_162945.jpg)

```
正向：
Masterpiece, top view, (conceptual art formed by colored liquid splashing in huge transparent bubbles, plump, round edges, smooth texture, water droplets, 3D art:1.4), solo, (placed on pure white background:1.3), pure color, light and shadow, natural light, high quality, high detail, Sony FE GM, UltraHD,
杰作，顶视图，（彩色液体溅在巨大透明气泡中形成的概念艺术，丰满，圆边，光滑纹理，水滴，3D艺术：1.4），独奏，（放置在纯白色背景上：1.3），纯色，光影、自然光、高画质、高细节、Sony FE GM、UltraHD、

反向：
nsfw, (worst quality, bad quality:1.3),

采样：DPM++2 M SDE Karras
Base Model：XXMix9 realistic_v4.0_v4.0,
ControlNet（图标最好处理成黑白的）: invert + control_v11f1p_sd15_depth, 权重：1-1.2
ControlNet1（彩色图标）: t2 iadapter, 权重1
ControlNet2（彩色图标）: tile, 权重0.8
LoRA: 各种飞溅水果系列_v1.0, 权重0.8
LoRA2: 美妆分子气泡场景lora, 权重0.8
LoRA3: 上古神话_水神共工氏, 权重0.4
```

#### **8. 机甲图标**

![](./note_img/Reference/20240831_162952.jpg)

```
正向：
yellow (change to your color keyword), hjymechatype, mecha, no humans, science fiction, vehicle focus, shadow, wheel, spacecraft, gradient background, gradient, machinery, robot, white background, ground vehicle, thrusters, blue led lighting, shining, metal, pip wire on surface, line shape led lighting, chrome,
黄色（更改为您的颜色关键字）、hjymechatype、mecha、没有人类、科幻小说、车辆焦点、阴影、轮、航天器、渐变背景、渐变、机械、机器人、白色背景、地面车辆、推进器、蓝色 LED 照明、闪亮，金属，表面点线，线形LED照明，镀铬，

反向：
ng_deepnegative_v1_75t, easynegative, nsfw

步数：30,
采样方法：Euler a,
Base Model：麒麟-revAnimated v122
LoRA1: 好机友科技机械文字, 权重：0.5,
LoRA2: 好机友科技机甲风格文字, 权重：0.5
Controlnet canny weight：1.35
Controlnet：t2iadapter_color, weight:1.0
Controlnet 2：lineart, weight:1.0
```

![](./note_img/Reference/20240831_162857.jpg)

```
正向提示词：
(white_background:1.2),mecha,machine,miniature,(metal:1.1),(The color palette includes shades of Red,silver gray and yellow:1.1),(concept machinery artist:1.1),(simple background:1.1),(solid background:1.1),((best quality)),((masterpiece)),8k,no humans,[lora:Mechanicaldog:0.75](lora:Mechanicaldog:0.75)
 
Model: ReVAnimated_v122_V122
Lora: Mechanicaldog.safetensors
 
✨ControlNet参数(根据不同图标微调参数)：
Model:control_v11p_sd15_canny [d14c016b]
Weight:1.2
Guidance Start:0
Guidance End:0.94

```

#### **9. SDXL抖音夏日**

![](./note_img/Reference/20240831_163158.jpg)

```
正向：
Transparent, glass, Summer, petals, big trees, lake, (Morandi color extension object in transparent container:1.3), clear frosted glass outside, (3D render of abstract shapes and objects floating in the air:1.1), semitransparent, soft pastel colors, (highly detailed:1.2), hyperrealistic, an octane render, the unreal engine, (high resolution:1.2), excellent composition, cinematic atmosphere, dynamic dramatic colorful light, precise coherent, aesthetic, very inspirational, stunning, highly detail, intricate, beautiful, surreal summer, Super scene, an artwork scene of mountains, trees, buildings, and grass, in the style of luminous 3d objects, cartoon-characters, selective focus, vivid birdlife, realistic lighting, modeling plants, materpiece, best quality,
透明，玻璃，夏天，花瓣，大树，湖泊，（透明容器中的莫兰迪颜色扩展对象：1.3），外部透明磨砂玻璃，（抽象形状和漂浮在空中的物体的3D渲染：1.1），半透明，柔和的粉彩颜色，（高度详细：1.2），超现实，辛烷渲染，虚幻引擎，（高分辨率：1.2），出色的构图，电影氛围，动态戏剧性彩色光，精确连贯，美观，非常鼓舞人心，令人惊叹，高度细节，错综复杂，美丽，超现实的夏天，超级场景，山，树，建筑物和草的艺术场景，采用发光3D对象的风格，卡通人物，选择性焦点，生动的鸟类，逼真的灯光，植物建模，作品，最佳质量

反向：
nsfw, (worst quality, bad quality:1.3), nsfw

步数：40，
采样：DPM++3M SDE Karras
Model: LEOSAM HelloWorld新世界ISDXL大模型v6.0.safetensors
LoRA1: 小猪佩奇I3D夏日风景XL, 权重0.6
LoRA2: 电商-超现实主义v2, 权重0.6
Controlnet: invert（白底黑线反色）, model:sai_xl_depth_256lora, weight:1.3
放大算法R-ESRGAN4x+	重回幅度0.4
```

#### **10. 游戏头像框**

![](./note_img/Reference/20240901_181216.jpg)


```markdown
正向提示词
masterpiece,genshin impact,best quality,(touxiangkuang:1.5),(8k, Premium, Premium:1.2),perfect flower,clear outline,delicate,(Avatar frame:1.3),a drawing of a wreath with flowers and butterflies on it,blue and pink color scheme,(rose:1.5),trans rights,ribbon,rose crown,pink and blue colors,flower frame,purple ribbons,pastel simple art,star guardian inspired,pink and blue colour,satin ribbons,stylized flowers,ribbons,blue and pink colors,flower tiara,soft cute colors,pink and blue,round design,sticker design,sticker concept design,blue and pink,flat pastel colors,rpg game item,magic spell icon,wide ribbons,pink and blue palette,rosette,unused design,soft aesthetic,a purple and white circular with a star in the middle,fantasy game spell icon,fantasy game spell symbol,world of warcraft spell icon,epic legends game icon,diablo 4 queen,symmetrical portrait rpg avatar,plain purple background,fantasy shield,centered elven,stylized border,ornate borders + concept art,better known as amouranth,white border frame,fantasy gauntlet of warrior,lightning mage spell icon,twitch emote,quest marker,clean borders , photorealistic,night time raid,skill ability art,kingdom of elves,discord profile picture,star guardian inspired,omega,guildwar artwork,3 d icon for mobile game,league of legends champion,emote,xenon,mmorpg,arc,character icon,
杰作，原神，最佳品质，（头象狂：1.5），（8k，高级，高级：1.2），完美花朵，轮廓清晰，精致，（头像框：1.3），画有花朵和蝴蝶的花环，蓝色和粉色配色方案，（玫瑰：1.5），反式权利，丝带，玫瑰王冠，粉色和蓝色，花框，紫色丝带，柔和的简单艺术，星之守护者的灵感，粉色和蓝色，缎带，风格化花朵，丝带，蓝色和粉红色的颜色，花头饰，柔和可爱的颜色，粉红色和蓝色，圆形设计，贴纸设计，贴纸概念设计，蓝色和粉红色，平面柔和的颜色，rpg 游戏项目，魔法咒语图标，宽丝带，粉红色和蓝色调色板,玫瑰花结,未使用的设计,柔和的美感,紫色和白色的圆形,中间有一颗星星,幻想游戏咒语图标,幻想游戏咒语符号,魔兽世界咒语图标,史诗传奇游戏图标,暗黑破坏神 4 女王,对称肖像rpg 头像，纯紫色背景，幻想盾牌，中心精灵，风格化边框，华丽边框 + 概念艺术，更广为人知的 amoranth，白色边框框架，幻想战士的手套，闪电法师法术图标，抽搐表情，任务标记，干净的边框，逼真，夜间突袭，技能能力艺术，精灵王国，不和谐个人资料图片，星之守护者启发，欧米茄，公会战争艺术品，手机游戏的3D图标，英雄联盟冠军，表情，氙气，MMORPG，弧线，角色图标，

负向提示词
paintings,sketches,nsfw,(worst quality:2),(low quality:2),(normal quality:2),lowres,normal quality,((monochrome)),((grayscale)),skin spots,acnes,skin blemishes,age spot,manboobs,backlight,glasses,panty,anime,cartoon,drawing,illustration,boring,long neck,out of frame,extra fingers,mutated hands,monochrome,((poorly drawn hands)),((poorly drawn face)),(((mutation))),(((deformed))),((ugly)),blurry,((bad anatomy)),(((bad proportions))),((extra limbs)),cloned face,glitchy,bokeh,(((long neck))),((flat chested)),red eyes,extra heads,close up,text,watermarks,logo,Six fingers,fingers.,nsfw,

采样方法Sampler：DPM++ 2M
迭代步数Steps：30
提示词引导系数CFG：7
模型Model：游戏头像框，游戏ICON, helloWonderland儿童插画
随机种子Seed：2059388304
```

![](./note_img/Reference/20240901_181248.jpg)


```markdown
正向提示词Prompt
masterpiece,best quality,((Circle: 1.2)), (Official Art, Aesthetics: 1.2), (8kPremium: 1.2),(gold: 1.2),tk,oc render,3D render,(love herat),(flash), Color scheme purple,Round metal frame,bright, crown,(wing), purple wings, wide wings, gemstone, pattern, graphic texture, thick style, quality, masterpiece style, metallic, absolute symmetry,glint,sparkle,pendant, crown, sparkling, crystal, black background,

负向提示词Negative prompt
EasyNegativeV2,nsfw

采样方法Sampler：Euler a
迭代步数Steps：24
提示词引导系数CFG：7
模型Model：游戏头像框，游戏ICON, AWPainting
随机种子Seed：3284450114
```

#### 11. 春季踏青主题海报

![]()


```markdown
Prompt 1:
(outdoor sunny spring day), (lush green meadow with colorful flowers), (cherry blossom trees in full bloom), (soft sunlight filtering through the trees), (gentle breeze causing leaves and flowers to sway), (bright blue sky with fluffy white clouds), (a charming little picnic setup with a checkered blanket and basket), (vivid pastel color palette), (bokeh effect in the background), (vibrant, joyful atmosphere), (smooth, detailed textures), (cinematic wide-angle shot), (soft, diffused lighting), (3D chibi style), (dreamy and whimsical aesthetic), (perfectly balanced composition)
（室外阳光明媚的春日）、（郁郁葱葱的草地，开满五颜六色的花朵）、（盛开的樱花树）、（柔和的阳光透过树丛）、（微风吹动树叶和花朵摇曳）、（明亮的蓝天蓬松的白云）、（带有方格毯子和篮子的迷人小野餐布置）、（生动柔和的调色板）、（背景中的散景效果）、（充满活力、欢乐的气氛）、（平滑、细致的纹理）、（电影效果）广角镜头）、（柔和的漫射照明）、（3D赤壁风格）、（梦幻而异想天开的美感）、（完美平衡的构图）

Prompt 1:
A perfectly balanced, dreamy springtime scene with a cinematic wide-angle shot, capturing a lush green meadow filled with vibrant flowers and cherry blossom trees in full bloom. Soft sunlight filters through the leaves, casting a gentle glow on the scene. A slight breeze makes the flowers and leaves sway, creating a whimsical atmosphere. A charming picnic setup with a checkered blanket and basket sits in the foreground, all in a vivid pastel color palette. The background features a bright blue sky with fluffy white clouds and a subtle bokeh effect, with smooth, detailed textures and a joyful, vibrant aesthetic.
电影般的广角镜头完美平衡、梦幻般的春天场景，捕捉到了郁郁葱葱的绿色草地上开满了生机勃勃的鲜花和盛开的樱花树。柔和的阳光透过树叶的缝隙，在景色上投射出柔和的光芒。微风徐徐，花叶摇曳，营造出一种异想天开的氛围。前景是一个迷人的野餐设施，配有格子毯子和篮子，全部采用生动柔和的调色板。背景以明亮的蓝天、蓬松的白云和微妙的散景效果为特色，具有平滑、细致的纹理和愉悦、充满活力的美感。

prompt 2:
Chibi anime girl, pink hair, round glasses, t-shirt, skirt, barefoot, spring meadow, cherry blossoms, sunlight, lens flare, bokeh, pastel colors, soft focus, dreamy atmosphere, poster composition, hyperdetailed, soft lighting, vibrant, joyful, serene, artistic masterpiece
赤壁动漫女孩，粉红色的头发，圆眼镜，T恤，裙子，赤脚，春天的草地，樱花，阳光，镜头光晕，散景，柔和的色彩，软焦点，梦幻般的气氛，海报构图，超详细，柔和的灯光，充满活力，欢乐、宁静、艺术杰作

prompt 2:
spring scene featuring the chibi anime girl with pink hair and round glasses. She's walking barefoot through a lush meadow dotted with cherry blossoms. The atmosphere is dreamy and joyful, with soft sunlight filtering through the trees. Use pastel colors and soft focus to enhance the peaceful mood. Include bokeh effects and lens flares for a magical touch. Style the image as a highly detailed, vibrant poster composition capturing the essence of a perfect spring day and creating an artistic masterpiece.
春天的场景，以粉红色头发和圆眼镜的赤壁动漫女孩为特色。她赤脚走在开满樱花的郁郁葱葱的草地上。柔和的阳光透过树林洒落，气氛梦幻而欢乐。使用柔和的色彩和柔和的焦点来增强平静的情绪。包括散景效果和镜头光晕，带来神奇的触感。将图像设计为高度详细、充满活力的海报构图，捕捉完美春日的精髓，创造出艺术杰作。


负面Prompt:
(low resolution), (blurry details), (oversaturated colors), (harsh lighting), (poor composition), (monochrome palette), (dull, lifeless atmosphere), (grainy textures), (distorted proportions), (unbalanced scene), (unrealistic shadows), (pixelation), (washed-out colors), (dark and gloomy tones), (noisy background), (flat and uninteresting lighting), (lack of depth), (motion blur), (poorly defined edges), (unappealing aesthetic)
```

#### **12. IP**

![]()


```markdown
chibi,Pixar\(style\),Cartoon\(style\),simple background,C4D, octane rendering, blind_box, studio lighting,kawaii cartoon style, exaggerated proportions, vibrant colors,highly glossy 3D rendering, smooth texture, high detail
chibi、皮克斯\(风格\)、卡通\(风格\)、简单背景、C4D、辛烷渲染、blind_box、工作室灯光、卡哇伊卡通风格，夸张的比例，鲜艳的色彩、高光泽 3D 渲染、平滑纹理、高细节

little_girl,solo,loli,full_shot,cute,looking at viewer,appearance soft, round, and very shiny, high detail  textures,smooth_hair,parted bangs, small tuft tied on top,round face,
小女孩，独奏，萝莉，全景，可爱，看着观众，外观柔软，圆润，非常有光泽，高细节纹理，光滑的头发，分开的刘海，小簇扎在上面，圆脸，

short light brown-pink hair, large purple eyes, large round pink glasses, gradient pink-to-white short-sleeve shirt, yellow shorts, white stripes,
浅棕色粉色短发，紫色的大眼睛，粉红色的大圆眼镜、 粉白渐变色短袖衬衫，黄色短裤，白色条纹、

one arm raised, fist clenched, other arm bent at chest, one leg lifted, jumping pose,
full of curiosity,big smile, eyes closed in a crescent shape, happy and excited expression,soft smile, innocent expression,smiling,
一只手举起，握紧拳头，另一只手弯曲放在胸前，一条腿抬起，摆出跳跃的姿势、
充满好奇、灿烂的笑容，眼睛闭成月牙形，开心兴奋的表情，柔和的笑容，天真的表情、

one arm raised, the other arm relaxed, one leg extended forward, tiptoe pose, presenting a light and lively dance pose.
一只手臂抬起，另一只手臂放松，一条腿向前伸直，踮起脚尖的姿势,呈现出轻盈活泼的舞蹈姿势。

surprised expression, big round eyes, slightly open mouth
惊讶的表情，圆圆的大眼睛，微张的嘴

standing on a circular stage, surrounded by floating bubbles, sparkling lights,magical and dreamlike atmosphere.
站在圆形舞台上，周围环绕着漂浮的气泡，灯光闪烁,梦幻般的神奇氛围。

metallic silver or black stage, deep blue or purple gradient background with glowing effects,bubbles, sparkles, spotlight effects,complete with glowing effects.
金属银或黑色舞台，带有发光效果的深蓝或紫色渐变背景,气泡、火花、聚光灯,发光效果
```

#### **13. 星空海**

![](./note_img/Reference/20240831_161612.jpg)

```markdown
正向关键词：
a boat floating in the ocean,Night,Sparkling on the sea xbeautiful,fantasy scene,top view,Ultra Wide Angle,Panorama,
漂浮在海洋中的小船,夜晚,波光粼粼的海面,美丽,奇幻场景,顶视图,超广角,全景,

大模型: 万享XL进阶版V80
Lora 1: Muertu XL丨增强黑夜晚上星空场景效果,
Controlnet : invert +control_v1p_sdxl_qrcode_monster
```

#### **14. 瑞幸logo 水晶效果**

![](./note_img/Reference/20240831_162038.jpg)

```markdown
提示词：
Crystal texture,(blue frosted glass material:1.4),(Snowflakes are flying:1.4),(Snow:1.2),blue crystal,water flow,blue frosted glass material,crystal butterfly,blue sky,grass,river,water surface,scene 3d,color streamers,color transparent streamers,(pink flowers:0.1),fantasy,3D art,3D scenes,font art,enhanced contrast between text and background,C4D,OC rendering exquisite pictures,masterpieces,high-definition details,dreamy pictures,medium shots,simple pictures,large color blocks,HD,4K,high saturation,high purity,
水晶质感，（蓝色磨砂玻璃材质：1.4），（雪花飞舞：1.4），（雪花：1.2），蓝色水晶，水流，蓝色磨砂玻璃材质，水晶蝴蝶，蓝天，草地，河流，水面，场景3D,彩色飘带,彩色透明飘带,(粉色花朵:0.1),奇幻,3D美术,3D场景,字体艺术,文字与背景增强对比度,C4D,OC渲染精美图片,杰作,高清细节,梦幻图片,中景,简约图片,大色块,高清,4K,高饱和度,高纯度,
大模型：ReVAnimated_v122
Lora1：3D电商模型；Lora2：梦中花境；Lora3：梦幻3D场景；Lora4：电商场景MAX；Lora5：李魚丸的水晶闪闪
```

#### **15.**玻璃质感

![](./note_img/Reference/20240831_162922.jpg)

```markdown
正向
(colored transparent glass:1.2),rich colors,summer colors,color conflicts,distant view,lake,watersurface,reflection,masterpiece,highest quality,commercial photography,8k,flower,cloud,fantasy,bokeh,
（彩色透明玻璃：1.2），色彩丰富，夏日色彩，色彩冲突，远景，湖泊，水面，倒影，杰作，最高品质，商业摄影，8k，花卉，云彩，幻想，背景虚化，

反向：nfsw,(worst quality,bad quality:1.3),采样：DPM  2 M Karras
大模型：realisticVisionV50
ControlNet 1:ip-adapter_sd15_plus 权重:1
ControlNet 2:lineart_standard 权重:1.3
ControlNet 3:depth_midas 权重:1
LoRA,1:glasssculpture 权重0.8
LoRA,2:明胶GelatinTech-20 权重0.6
```

#### **16.白露插画**

![](./note_img/Reference/20240831_163713.jpg)

```markdown
正向：
Illustration style,garden,yard full of flowers,water,dew,leaves,(drops hanging on leaves :1.4),(dew :1.2),two young people,sitting on the grass,drinking hot drinks,steaming cups,in the distance there are many hills,surrounded by bamboo forests,super detail,bright colors,
插画风格，花园，开满鲜花的院子，水，露水，树叶，（树叶上挂着的水滴：1.4），（露水：1.2），两个年轻人，坐在草地上，喝着热饮，热气腾腾的杯子，在远处有很多山丘，周围都是竹林，超级细节，鲜艳的色彩

大模型：动漫插画children_v2.0.safetensors
Lora：白泽MARS-治愈 0.80
Lora：光影艺术插画 权重：0.30
Lora：万物调节 | 细节权重：0.25
Lora：小清新治愈画 权重：0.30
```

#### **17.**涂鸦Icon

![](./note_img/Reference/20240831_164238.jpg)

```markdown
(glass:1.1),glass texture,Unique graffiti style letters and words,full of personality graffiti,(creative design:1.3),vivid colors,detailed patterns,3D icon,best quality,masterpiece,(white background:1.1),
（玻璃：1.1），玻璃质感，独特的涂鸦风格字母和文字，充满个性的涂鸦，（创意设计：1.3），鲜艳的色彩，细致的图案，3D图标，最佳品质，杰作，（白底：1.1），
```

#### **18.**SD XL大模型 | 梦幻海底

![](./note_img/Reference/20240831_164359.jpg)

```markdown
大模型：Dream Anime XL | 筑梦动漫XL
lora:Sim简约插画-XL-lora
((underwater world)),(beautiful detailed water),((coral)),dynamic angle,floating,(detailed light),no humans,flower,(underwater forest),(bloom)coral,scenery,air bubble,submerged,schools of fish,colorful corals,swaying sea grass,deep blue sea,mysterious atmosphere,soft lighting,realistic details,best quality,masterpiece,
((海底世界)),(美丽细致的水),((珊瑚)),动态角度,漂浮,(细致的光),没有人类,花朵,(水下森林),(绽放)珊瑚,风景,气泡,淹没，鱼群，七彩珊瑚，摇曳的海草，深蓝色的大海，神秘的气氛，柔和的灯光，逼真的细节，最好的品质，杰作，
```

#### **19.**封神

![](./note_img/Reference/20240831_164621.jpg)

```markdown
Gold, bronze ware,dragon_print,dragon scale,atmosphere,ultra-highdefinition,ultra-detailed, Chinese historical relics, cgrendering.ocrendering,strongtexure, ultra high definition, masterpiece,IvoryGoldAI
黄金,青铜器,龙纹,龙鳞,大气,超高清,超细致,中国历史文物,cgrendering.ocrendering,strongtexture,超高清,杰作,IvoryGoldAI

大模型：Realistic Vision V4.
Lora：科技感IvoryGoldAI, 
DPM++ SDE Karras
迭代步数Steps：44
```

#### **20.**窗外的赛博麻雀

![](./note_img/Reference/20240831_165022.jpg)

```markdown
正向：
Envision a palm-sized robotic sparrow mascot designed for companionship,(intricate details),hdr,(intricate details, hyperdetailed:1.2),ice, water, ice and water, 
fluorescence transparent metal armor.bright light, clay material, precision mechanical parts.holographic,translucent,
设想一个手掌大小的机器人麻雀吉祥物，专为陪伴而设计，（复杂的细节），hdr，（复杂的细节，超详细：1.2），冰，水，冰和水，
荧光透明金属装甲。强光，粘土材料，精密机械零件。全息，半透明，

反向：
marker_(medium),faux_traditional_media,traditional_media,millipen_(medium),nib_pen_(medium),ballpoint_pen_(medium),(long neck:2),(sagging breasts:1.2),lowres,nsfw,nsfw

Model：PAseer-SDXL-RealisticFairyland (3D/2.5D),
Lora：SDXL Detail 细节调节器,  niji-3d icon 炫彩风SDXL
迭代步数Steps：45；  CFG：9.5
```

#### **21.**夏至

![](./note_img/Reference/20240831_165111.jpg)

```markdown
正向
Outdoor,blue sky,white clouds,(transparent glass material:1.4),(no one),roads,rivers,(lotus leaves:1.2),pink lotus flowers,strong contrast,depth of field,masterpieces,high-definition details,wallpaper,3D art,C4D,OC rendering,surrealism,
户外，蓝天，白云，（透明玻璃材质：1.4），（无人），道路，河流，（荷叶：1.2），粉红荷花，强烈反差，景深，杰作，高清细节，壁纸，3D艺术，C4D，OC渲染，超现实主义

反向
(worst quality:2),(no people),(low quality:2),(normal quality:2),lowres,bad anatomy,bad hands,text,error,missing fingers,extra digit,finder digits,cropped,jpeg artifacts,signature,watermark,username,blur,nsfw,nsfw,

模型Model：ReVAnimated_v122, 
lora：3D电商模型, 【LIB首发】透明机械体, 梦中花境：0.2, 创意｜透明五彩花卉：0.3
Steps：30
```

#### **22.**夏日清凉季

![](./note_img/Reference/20240831_165316.jpg)

```markdown
Transparent, glass，Summer, swimming pool, petals, big trees，(white_background),a pattern of english letters,(Morandi color extension object in transparent container:1.3),clear frosted glass outside,((isolated on a white background with no shadows or reflections)),(3D render of abstract shapes and objects floating in the air:1.1),semitransparent,soft pastel colors,(highly detailed:1.2),hyperrealistic,an octane render,the unreal engine,(high resolution:1.2), excellent composition, cinematic atmosp
透明，玻璃，夏天，游泳池，花瓣，大树，（白色_背景），英文字母图案，（透明容器中的莫兰迪色延伸物体：1.3），外面透明磨砂玻璃，（（隔离在白色背景上，没有阴影或反射）），（抽象形状和漂浮在空中的物体的 3D 渲染：1.1），半透明，柔和的色彩，（高度详细：1.2），超现实，辛烷渲染，虚幻引擎，（高分辨率：1.2） ），优秀的构图，电影氛围

大模型：SDXL 1.0.safetensors
lora：sdxl海报
```

#### **23.**贵族

![](./note_img/Reference/20240831_184842.jpg)

```markdown
正向
Exquisite jewelry design, complex pattern texture, diamonds, gemstones, rose gold, studded with blue gemstones and red crystals, sparkling, background with flowers and gemstones, (rose flower: 1.3), green leaves, exquisite vintage pattern , retro texture details, (vines: 1.4), (bright flowers), font surrounded by flowers, diamonds, crystals, sunlit, outdoor, water surface, reflection, gemstone fragments, ray tracing, blue sky, dreamy scene, light Colorful background, surrealism, masterpiece, high-definition picture, ultra-detail,
精致的珠宝设计，复杂的图案纹理，钻石，宝石，玫瑰金，镶满蓝色宝石和红色水晶，闪闪发光，背景有鲜花和宝石，（玫瑰花：1.3），绿叶，精致的复古图案，复古纹理细节，（藤蔓：1.4），（鲜艳的花朵），字体包围花朵，钻石，水晶，阳光照射，户外，水面，倒影，宝石碎片，光线追踪，蓝天，梦幻场景，光彩色背景，超现实主义，杰作，高高清图片，超细节，
反向
blouse,frame, grid, (worst quality, low quality:2), monochrome, zombie,overexposure, watermark,text,infant,bad anatomy,bad hand,extra hands,extra fingers,too many fingers,fused fingers,loli,bad arm,distorted arm,extra arms,fused arms,extra legs,missing leg,disembodied leg,extra nipples, detached arm, liquid hand,inverted hand,disembodied limb, loli, oversized head,extra body,completely nude, extra navel,easynegative,(hair between eyes),sketch, duplicate, ugly, huge eyes, text, logo, worst face, (bad and mutated hands:1.3), (blurry:2.0), horror, geometry, bad_prompt, (bad hands), (missing fingers), multiple limbs, bad anatomy, (interlocked fingers:1.2), Ugly Fingers, (extra digit and hands and fingers and legs and arms:1.4), ((2girl)), (deformed fingers:1.2), (long fingers:1.2),(bad-artist-anime), bad-artist, bad hand, extra legs ,(ng_deepnegative_v1_75t),nsfw

模型：麦橘；lora：Alice_v1 爱丽丝；Steps：30；DPM++ 2M SDE Karras
```
#### **24.**梦幻透明超级符号

![](./note_img/Reference/20240831_193749.jpg)

```markdown
(transparent qlassmaterial:1.3),flower,grass,outdoor,floral,green,bluesky,(cherry blossom:1.2),white clouds,runningwater,spring weather,aesthetic,3D art,C4D.OC rendering,masterpiece,high definition detail, (masterpiece:1.2),exquisite,high resolution,perfectilumination,(Extreme detail CG:1.2).best quality.32K,
（透明玻璃材质：1.3）、花、草、户外、花卉、绿色、蓝天、（樱花：1.2）、白云、流水、春天的天气、唯美、3D艺术、C4D.OC渲染、杰作、高清细节、 (杰作:1.2),精致,高分辨率,完美照明,(极致细节CG:1.2).最佳品质.32K,
```

#### **25.**机械表

![](./note_img/Reference/20240901_171524.jpg)

```markdown
正向
((transparent, light-painted, wireframe, contour light)),3D, mechanical watch, complex gear structure, simple background, showcase
反向
(worst quality:2),(low quality:2),(normal quality:2),lowres,normal quality,((monochrome)),((grayscale)),skin spots,acnes,skin blemishes,age spot,(ugly:1.331),(duplicate:1.331),(morbid:1.21),(mutilated:1.21),(tranny:1.331),mutated hands,(poorly drawn hands:1.5),blurry,(bad anatomy:1.21),(bad proportions:1.331),extra limbs,(disfigured:1.331),(missing arms:1.331),(extra legs:1.331),(fused fingers:1.61051),(too many fingers:1.61051),(unclear eyes:1.331),lowers,bad hands,missing fingers,extra digit,bad hands,missing fingers,(((extra arms and legs))),verybadimagenegative_v1.3,badhandv4,EasyNegative,nsfw,nsfw
（（透明，光绘，线框，轮廓光）），3D，机械表，复杂的齿轮结构，简单的背景，展示

Model：奇幻骇客_白棱XL;LYS_transparent&wireframe_XL;DPM++ SDE Karras
```
#### **26.**LIBLIB梦幻海报

![](./note_img/Reference/20240901_173420.jpg)

```markdown
正向
Dream, glowing neon word "LIBLIB" is clearly labelled in the image, surrounded by red roses in a pond inside a dark forest, highly detailed, ultra-high resolutions, 32K UHD, best quality, masterpiece, <lora:Dream XL:1>
梦想，发光的霓虹灯字“LIBLIB”在图像中清晰地标记，周围是黑暗森林内池塘中的红玫瑰，高度详细，超高分辨率，32K UHD，最佳质量，杰作，<lora:Dream XL:1 >
反向
Bad quality, worst quality, normal quality, low-res, sketch, poor design, deformed, disfigured, soft, bad composition, simple design, boring, watermark, error, cropped, blurry

模型Model：Dream Tech XL | 筑梦工业XL；DPM++ 2M Karras；CFG：6；Steps：30
```
#### **27.**华为科技风满满

![](./note_img/Reference/20240901_173613.jpg)

```markdown
正向
A spaceship,NCK manufacturer,a DT touring class spaceship with glowing LED lights on it. landing on an island,rendered in the style of a 3D rendering with a white background,photographed professionally with professional lighting and color grading to appear hyper realistic,cinematic shots,blue and white,Water surface reflection,In the distance is the deep starry sky. Astronaut,
一艘宇宙飞船，NCK 制造商，一艘 DT 旅行级宇宙飞船，上面有发光的 LED 灯。登陆岛屿，白色背景3D渲染风格，专业拍摄，专业灯光和调色，显得超写实，电影镜头，蓝白色，水面倒影，远处是深邃的星空。宇航员，
反向
deformed ship,deformed aircraft,asymmetric ship,bad quality,normal quality,worst quality,anime,boring,bad composition,drawing,cartoon,simple composition,poor composition,poor design,soft,disconnected parts,bad ship,asymmetrical wings,asymmetrical ship,no wings,missing wings,out of frame,two ships,ships duo,ships fleet,,nsfw

模型Model：Dream Tech XL | 筑梦工业XL； 筑梦工业 | 环宿星港-飞船XL； 3D全息艺术_SDXL(载具篇)；Steps：35；CFG：6.5
```
#### **28.**金典字体

![](./note_img/Reference/20240901_174636.jpg)

```markdown
正向
cows,(masterpiece:1.2), best quality, masterpiece, highres, original, extremely detailed wallpaper, perfect lighting,(extremely detailed CG:1.2), drawing, paintbrush,, masterpiece, best quality, 8k, insane details, intricate details, hyperdetailed, hyper quality, high detail, ultra detailed, <lora:shangyekvv1-000012:0.6>
 牛，（杰作：1.2），最佳质量，杰作，高分辨率，原创，极其详细的壁纸，完美的照明，（极其详细的CG：1.2），绘画，画笔，杰作，最佳质量，8k，疯狂的细节，复杂的细节，超详细、超品质、高细节、超详细、<劳拉：shangyekvv1-000012：0.6>
 反向
 (((simple background))),lowres,bad anatomy,bad hands,text,error,extra digit,fewer digits,cropped,worst quality,low quality,normal quality,jpeg artifacts,signature,watermark,username,blurry BadDream UnrealisticDream, realisticvision-negative-embedding
 
Model：revAnimated_v122, 商业kvv1；Steps：30；DPM++ 2M SDE Karras
```
#### **29.小米logo**

![](./note_img/Reference/20240901_174850.jpg)

![](./note_img/Reference/20240901_175156.jpg)

![](./note_img/Reference/20240901_175139.jpg)

```markdown
正向
masterpiece,best quality,outdoor,landscape,building,tree,flower,water,mountain,plant,grass,boli,DDicon,shangyekv\(style\),huwai,
杰作，最佳品质，户外，景观，建筑，树，花卉，水，山，植物，草，波里，DDicon，shangyekv \（风格\），huwai，
反向
nsfw

Model：revAnimated_v122,；科技感DDicon_lora：0.4, 商业kvv1：0.4, 电商|微观与产品：0.5, 创意|透明五彩花卉：0.4, 简白_春意盎然，满屏都是花花（电商风格）：0.6, 光泽玻璃材质：0.6

语义分割图具体步骤（在PS里新建一个画板，尺寸跟生图的时候尺寸一样，用颜色定义画面材质，我的主体定义为建筑，先在PS里生成3D形状，填色，每个颜色新建一个图层，用白色描边）

```
#### **30.SD超级符号海报**

![](./note_img/Reference/20240901_180045.jpg)

```markdown
正向
(Masterpiece:1.2),(View from above:1.4),(Grass:1.3),(Sea: 1.3) (Swimming Pool:1.2),waves,beach,blue sea,water surface,(Flowers:1.2),small flowers,Swimming pool,green plants,flowers,green theme,C4D,OC rendering,3D art,high-definition details,spring atmosphere,
（杰作：1.2）、（俯视：1.4）、（草：1.3）、（海：1.3）（游泳池：1.2）、海浪、沙滩、碧海、水面、（花朵：1.2）、小花,游泳池,绿植,花卉,绿色主题,C4D,OC渲染,3D艺术,高清细节,春天气息,
反向
lowres,bad anatomy,bad hands,text,error,missing fingers,extra digit,fewer digits,cropped,worst quality,low quality,normal quality,jpeg artifacts,signature,watermark,username,blurry,nsfw,,nsfw
Model：ReVAnimated_v122, 3D电商模型, 【梦幻】3D电商草地, 小猪佩奇｜夏日3D电商场景
CFG：7.5；steps：30；DPM++ 2M SDE Karras
```
#### **31.气泡Icon**

![](./note_img/Reference/20240901_180642.jpg)

```markdown
正向
of glass,crystal clear,(pure white background:1.2),boli,Blisters,ice,Transparent water droplets,no human,best quality,UHD,8K,Composed of transparent water drops,gestural movement,surrealist fantasy style,organic fluid,light painting,nature theme,studio lighting,perfect lighting,outdoors,nature,golden ratio composition,realistic masterpiece,award winning photography,8k.,
玻璃，晶莹剔透，（纯白色背景：1.2），波利，水泡，冰，透明水滴，没有人类，最佳品质，UHD，8K，由透明水滴组成，手势运动，超现实主义幻想风格，有机流体，光画,自然主题,工作室照明,完美照明,户外,自然,黄金比例构图,写实杰作,获奖摄影,8k。,
反向
(nsfw)EasyNegative,draw by bad-artist,sketch by bad-artist-anime,(bad_prompt:0.8),(artist name,signature,watermark:1.4),(ugly:1.2),(worst quality,poor details:1.4),bad-hands-5,badhandv4,blur,nsfw,nsfw,

Model：ReVAnimated_v122, Gelatin Tech – World Morph, 美妆分子气泡场景lora, abel万物冻结（冰）
```
#### **32.**谷雨字研

![](./note_img/Reference/20240901_184941.jpg)

```markdown
正向
Outdoor,(blue sky surrounded by white clouds:1.3),(white clouds),depth of field,cherry blossoms scattered all over the mountains,small wildflowers,pink flowers,yellow flowers,grasslands,distant mountains,waterfalls,(cherry blossom trees),cherry blossoms falling,grasslands,roads,small grass,many cherry blossoms,rapeseed flowers,masterpieces,high-definition details,spring atmosphere,green plants,flowers,light and shadow,ultra wide angle lens,
室外，（蓝天白云：1.3），（白云），景深，漫山遍野的樱花，小野花，粉红花，黄花，草原，远山，瀑布，（樱花树） ）,樱花飘落,草原,道路,小草,很多樱花,油菜花,杰作,高清细节,春天气息,绿植,花卉,光影,超广角镜头,

反向
NSFW,nude,naked,porn,(worst quality, low quality:1.4),deformed iris,deformed pupils,(deformed,distorteddisfigured:1.3)cropped,out of frame,
poorlydrawn,badanatomy,wronganatomy,extralimb,missinglimb,floatinglimbs,disgusting.amputation,blurry,jpegartifacts,watermark,watermarked,text,Signature,EasyNegative,BadArtist,BadPrompt,BadImages,poor anatomical structure,low quality,text errors,extra numbers,fewer numbers,jpeg artifacts,signatures,watermarks,username,blurring,cropped,nsfw,

模型Model：revAnimated_v122；
lora：科技感IvoryGoldAI,3D电商模型；绿意盎然春色茶饮；【新中式】山水1.0；踏青｜春季清新自然环境背景；花之恋-汉服写真 十二花神系列-樱花
Steps：30；CFG：7
```
#### **33.**谷雨 2

![](./note_img/Reference/20240901_185458.jpg)

```markdown
正向
bird, scenery, tree, outdoors, mountain, no humans, building, water,<lora:spring:0.8>, (((masterpiece))),(((best quality))),((ultra-detailed)),
鸟、风景、树、户外、山、无人、建筑、水、<lora:spring:0.8>, (((杰作))),(((最佳质量))),((超详细)),

反向
Lotus,people,person,cat,NSFW,nude,naked,porn,(worst quality, low quality:1.4),deformed iris,deformed pupils,(deformed,distorteddisfigured:1.3)cropped,out of frame,
poorlydrawn,badanatomy,wronganatomy,extralimb,missinglimb,floatinglimbs,disgusting.amputation,blurry,jpegartifacts,watermark,watermarked,text,Signature,EasyNegative,BadArtist,BadPrompt,BadImages,poor anatomical structure,low quality,text errors,extra numbers,fewer numbers,jpeg artifacts,signatures,watermarks,username,blurring,cropped,nsfw,

Model：revAnimated_v122；科技感IvoryGoldAI, Mid - Biochemical, 3D电商模型, 绿意盎然春色茶饮, 创意｜透明五彩花卉
```
#### **34.24节气惊蛰**

![](./note_img/Reference/20240901_190639.jpg)

```markdown
正向
The Chinese solar term startles insects, and in the busy spring of farming, all things in the world revive and thrive. In the sky, there is a beautiful rainbow, wood, green rice fields, many small animals, (water droplets: 1.2), green grasslands, ponds, on the ground, butterflies, ladybugs, plants, water, flowers, leaves, lakes, no one, the background is the earth, masterpiece, the best quality, wide-angle lens
节气惊虫，春耕农忙，万物复苏，欣欣向荣。天空中，有美丽的彩虹，树林，绿色的稻田，很多小动物，（水滴：1.2），绿色的草原，池塘，地上，蝴蝶，瓢虫，植物，水，花，树叶，湖泊，没有人，背景是地球，杰作，最佳画质，广角镜头
反向
extra fingers,fewer fingers,lowres,bad anatomy,bad hands,text,error,missing fingers,extra digit,fewer digits,cropped,worst quality,low quality,normal quality,jpeg artifacts,signature,watermark,username,blurry,wrong legs,nsfw,Hide arms,wrong Human body structure,Extra breasts,(((Hide hands))),(((extra legs))),(((wrong legs))),Finger connection,pointy ears,lowres,bad anatomy,bad hands,text,error,missing fingers,extra digit,fewer digits,cropped,worst quality,low quality,normal quality,jpeg artifacts,signature,watermark,username,blurry,lowres,bad anatomy,bad hands,text,error,missing fingers,extra digit,fewer digits,cropped,worst quality,low quality,normal quality,jpeg artifacts,signature,watermark,username,blurry,nsfw,

Model：全网首发｜儿童插画绘本, 儿童插画绘本Minimalism, 小清新治愈画风插画
```
#### **35.**

![](./note_img/Reference/20240901_192527.jpg)

```markdown
正向
A book with glowing characters floating in space, two people reading the words from behind, in the style of fantasy, simple background, book cover design, the book title is written on top of the cover, in the style of illustration, art station trend, bright colors, red and gold tones, orange glow, golden light effect, starry sky background, book illustration, in the style of a movie poster, book shape, book texture.
一本书，发光的人物漂浮在太空中，两个人从后面读字，幻想风格，简单的背景，书籍封面设计，书名写在封面上，插画风格，艺术站潮流，明亮的色彩，红色和金色色调，橙色发光，金色光效，星空背景，书籍插图，电影海报风格，书籍形状，书籍纹理。
反向
Blur, low quality, noise, text, disordered book,nsfw

Euler a
```

#### **36.**

![]()

```markdown

```
#### **37.**

![]()

```markdown

```
#### **38.**

![]()

```markdown

```
#### **39.**

![]()

```markdown

```
#### **40.**

![]()

```markdown

```
#### **41.**

![]()

```markdown

```
#### **42.**

![]()

```markdown

```
#### **43.**

![]()

```markdown

```
#### **44.**

![]()

```markdown

```
#### **45.**

![]()

```markdown

```

