#### **1. 抖音(透明玻璃花升级版)**

![](./note_img/Reference/20240831_162757.jpg)

```
prompt:
masterpiece, best quality, glass texture, flowers, plant, many flowers, surrounded by growing plants, (transparent), best quality, (Pixar-style:1.4), (At Night:0.8), Ultra-detailed aesthetic, beautiful composition, rich bright colors, volumetric soft light, reflection in the water, water ripple. Inspired by Alice in Wonderland, unreal Engine, octane render, 3D rendering,

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

![]()


```markdown
正向提示词
masterpiece,genshin impact,best quality,(touxiangkuang:1.5),(8k, Premium, Premium:1.2),perfect flower,clear outline,delicate,(Avatar frame:1.3),a drawing of a wreath with flowers and butterflies on it,blue and pink color scheme,(rose:1.5),trans rights,ribbon,rose crown,pink and blue colors,flower frame,purple ribbons,pastel simple art,star guardian inspired,pink and blue colour,satin ribbons,stylized flowers,ribbons,blue and pink colors,flower tiara,soft cute colors,pink and blue,round design,sticker design,sticker concept design,blue and pink,flat pastel colors,rpg game item,magic spell icon,wide ribbons,pink and blue palette,rosette,unused design,soft aesthetic,a purple and white circular with a star in the middle,fantasy game spell icon,fantasy game spell symbol,world of warcraft spell icon,epic legends game icon,diablo 4 queen,symmetrical portrait rpg avatar,plain purple background,fantasy shield,centered elven,stylized border,ornate borders + concept art,better known as amouranth,white border frame,fantasy gauntlet of warrior,lightning mage spell icon,twitch emote,quest marker,clean borders , photorealistic,night time raid,skill ability art,kingdom of elves,discord profile picture,star guardian inspired,omega,guildwar artwork,3 d icon for mobile game,league of legends champion,emote,xenon,mmorpg,arc,character icon,

负向提示词
paintings,sketches,nsfw,(worst quality:2),(low quality:2),(normal quality:2),lowres,normal quality,((monochrome)),((grayscale)),skin spots,acnes,skin blemishes,age spot,manboobs,backlight,glasses,panty,anime,cartoon,drawing,illustration,boring,long neck,out of frame,extra fingers,mutated hands,monochrome,((poorly drawn hands)),((poorly drawn face)),(((mutation))),(((deformed))),((ugly)),blurry,((bad anatomy)),(((bad proportions))),((extra limbs)),cloned face,glitchy,bokeh,(((long neck))),((flat chested)),red eyes,extra heads,close up,text,watermarks,logo,Six fingers,fingers.,nsfw,

采样方法Sampler：DPM++ 2M
迭代步数Steps：30
提示词引导系数CFG：7
模型Model：游戏头像框，游戏ICON, helloWonderland儿童插画
随机种子Seed：2059388304
```

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

Prompt 1:
A perfectly balanced, dreamy springtime scene with a cinematic wide-angle shot, capturing a lush green meadow filled with vibrant flowers and cherry blossom trees in full bloom. Soft sunlight filters through the leaves, casting a gentle glow on the scene. A slight breeze makes the flowers and leaves sway, creating a whimsical atmosphere. A charming picnic setup with a checkered blanket and basket sits in the foreground, all in a vivid pastel color palette. The background features a bright blue sky with fluffy white clouds and a subtle bokeh effect, with smooth, detailed textures and a joyful, vibrant aesthetic.

prompt 2:
Chibi anime girl, pink hair, round glasses, t-shirt, skirt, barefoot, spring meadow, cherry blossoms, sunlight, lens flare, bokeh, pastel colors, soft focus, dreamy atmosphere, poster composition, hyperdetailed, soft lighting, vibrant, joyful, serene, artistic masterpiece

prompt 2:
spring scene featuring the chibi anime girl with pink hair and round glasses. She's walking barefoot through a lush meadow dotted with cherry blossoms. The atmosphere is dreamy and joyful, with soft sunlight filtering through the trees. Use pastel colors and soft focus to enhance the peaceful mood. Include bokeh effects and lens flares for a magical touch. Style the image as a highly detailed, vibrant poster composition capturing the essence of a perfect spring day and creating an artistic masterpiece.


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
大模型: 万享XL进阶版V80
Lora 1: Muertu XL丨增强黑夜晚上星空场景效果,
Controlnet : invert +control_v1p_sdxl_qrcode_monster
```

#### **14. 瑞幸logo 水晶效果**

![](./note_img/Reference/20240831_162038.jpg)

```markdown
提示词：
Crystal texture,(blue frosted glass material:1.4),(Snowflakes are flying:1.4),(Snow:1.2),blue crystal,water flow,blue frosted glass material,crystal butterfly,blue sky,grass,river,water surface,scene 3d,color streamers,color transparent streamers,(pink flowers:0.1),fantasy,3D art,3D scenes,font art,enhanced contrast between text and background,C4D,OC rendering exquisite pictures,masterpieces,high-definition details,dreamy pictures,medium shots,simple pictures,large color blocks,HD,4K,high saturation,high purity,
大模型：ReVAnimated_v122
Lora1：3D电商模型
Lora2：梦中花境
Lora3：梦幻3D场景
Lora4：电商场景MAX
Lora5：李魚丸的水晶闪闪
```

#### **15.**玻璃质感

![](./note_img/Reference/20240831_162922.jpg)

```markdown
正向
(colored transparent glass:1.2),rich colors,summer colors,color conflicts,distant view,lake,watersurface,reflection,masterpiece,highest quality,commercial photography,8k,flower,cloud,fantasy,bokeh,反向：nfsw,(worst quality,bad quality:1.3),采样：DPM  2 M Karras
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
```

#### **18.**SD XL大模型 | 梦幻海底

![](./note_img/Reference/20240831_164359.jpg)

```markdown
大模型：Dream Anime XL | 筑梦动漫XL
lora:Sim简约插画-XL-lora
咒语：((underwater world)),(beautiful detailed water),((coral)),dynamic angle,floating,(detailed light),no humans,flower,(underwater forest),(bloom)coral,scenery,air bubble,submerged,schools of fish,colorful corals,swaying sea grass,deep blue sea,mysterious atmosphere,soft lighting,realistic details,best quality,masterpiece,
```

#### **19.**封神

![](./note_img/Reference/20240831_164621.jpg)

```markdown
Gold, bronze ware,dragon_print,dragon scale,atmosphere,ultra-highdefinition,ultra-detailed, Chinese historical relics, cgrendering.ocrendering,strongtexure, ultra high definition, masterpiece,IvoryGoldAI

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

大模型：SDXL 1.0.safetensors
lora：sdxl海报
```

#### **23.**贵族

![](./note_img/Reference/20240831_184842.jpg)

```markdown
正向
Exquisite jewelry design, complex pattern texture, diamonds, gemstones, rose gold, studded with blue gemstones and red crystals, sparkling, background with flowers and gemstones, (rose flower: 1.3), green leaves, exquisite vintage pattern , retro texture details, (vines: 1.4), (bright flowers), font surrounded by flowers, diamonds, crystals, sunlit, outdoor, water surface, reflection, gemstone fragments, ray tracing, blue sky, dreamy scene, light Colorful background, surrealism, masterpiece, high-definition picture, ultra-detail,
反向
blouse,frame, grid, (worst quality, low quality:2), monochrome, zombie,overexposure, watermark,text,infant,bad anatomy,bad hand,extra hands,extra fingers,too many fingers,fused fingers,loli,bad arm,distorted arm,extra arms,fused arms,extra legs,missing leg,disembodied leg,extra nipples, detached arm, liquid hand,inverted hand,disembodied limb, loli, oversized head,extra body,completely nude, extra navel,easynegative,(hair between eyes),sketch, duplicate, ugly, huge eyes, text, logo, worst face, (bad and mutated hands:1.3), (blurry:2.0), horror, geometry, bad_prompt, (bad hands), (missing fingers), multiple limbs, bad anatomy, (interlocked fingers:1.2), Ugly Fingers, (extra digit and hands and fingers and legs and arms:1.4), ((2girl)), (deformed fingers:1.2), (long fingers:1.2),(bad-artist-anime), bad-artist, bad hand, extra legs ,(ng_deepnegative_v1_75t),nsfw

模型：麦橘；lora：Alice_v1 爱丽丝；Steps：30；DPM++ 2M SDE Karras
```
#### **24.**梦幻透明超级符号

![](./note_img/Reference/20240831_193749.jpg)

```markdown
(transparent qlassmaterial:1.3),flower,grass,outdoor,floral,green,bluesky,(cherry blossom:1.2),white clouds,runningwater,spring weather,aesthetic,3D art,C4D.OC rendering,masterpiece,high definition detail, (masterpiece:1.2),exquisite,high resolution,perfectilumination,(Extreme detail CG:1.2).best quality.32K,
```

#### **25.**

![]()

```markdown
![]()
```
#### **26.**

![]()

```markdown
![]()
```
#### **27.**

![]()

```markdown
![]()
```
#### **28.**

![]()

```markdown
![]()
```

