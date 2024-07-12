### Stable Diffusion 提示词

#### **1、起手式**

**基础起手式：**

```
Best Prompt：
masterpiece, best quality,

negative_prompt：
((NSFW)),lowres,bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, JPEG artifacts, signature, watermark, iceman, blurry,
```
**二次元通用：**

```sh
Best Prompt：
SFW, (masterpiece:1,2), best quality, masterpiece, highres, original, extremely detailed wallpaper, perfect lighting,(extremely detailed CG:1.2),

negative_prompt：
((NSFW)), (worst quality:2), (low quality:2), (normal quality:2), lowres, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, age spot, (ugly:1.331), (duplicate:1.331), (morbid:1.21), (mutilated:1.21), (tranny:1.331), mutated hands, (poorly drawn hands:1.5), blurry, (bad anatomy:1.21), (bad proportions:1.331), extra limbs, (disfigured:1.331), (missing arms:1.331), (extra legs:1.331), (fused fingers:1.61051), (too many fingers:1.61051), (unclear eyes:1.331), lowers, bad hands, missing fingers, extra digit,bad hands, missing fingers, (((extra arms and legs))),
```

**NAiDefault**

```sh
prompt：
masterpiece, best quality

negative_prompt：
((NSFW)),text, lowres, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, bad anatomy, bad hands, error, missing fingers, extra digit, fewer digits, missing arms, long neck, Humpbacked
```

**负面起手式：**

```
negative_prompt：
((NSFW)),bad face,bad anatomy,bad proportions,bad perspective,mutated hands and fingers,more than five fingers,lowres,bad hands,text,error,missing fingers,extra digit,fewer digits,cropped,worst quality,low quality,normal quality,jpeg artifacts,signature,watermark,username,low quality lowres disfigured,low quality lowres malformed,low quality lowres mutated,low quality lowres anatomical nonsense,low quality lowres text font ui,low quality lowres error,low quality lowres malformed hands,low quality lowres long neck,low quality lowres blurred,low quality lowres lowers,low quality lowres low res,low quality lowres bad proportions,extra fingers,fewer fingers,strange fingers,bad hand,(EasyNegative:1.2),text,username,extra fingers,fewer fingers,long body
```

**橘子模型专用**

```sh
prompt：
t-shirt, long t-shirt, narrow waist t-shirt, t-shirt over hips, short dress

negative_prompt：
((NSFW)),bare, nafw, sagging breast, crop top
```

**国风模型**

```sh
prompt：
masterpiece, best quality

negative_prompt：
((NSFW)),(worst quality, low quality:1.4)
```

**平涂风**

```sh
prompt：
ligne claire,lineart,monochrome
```

**新海诚**

```sh
prompt：
masterpiece, best quality,

negative_prompt：
EasyNegative, illustration, 3d, sepia, painting, cartoons, sketch, (worst quality:2), (low quality:2), (normal quality:2), lowres, bad anatomy, normal quality, ((monochrome)), ((grayscale))
```
**AI推文**

```sh
prompt：
((masterpiece),(Highest picture quality),(Master's work),(8K wallpaper),(ray tracing),Depth of field,finely detail,best quality, high resolution illustration,Cinematic Lighting),

negative_prompt：
EasyNegative, ng_deepnegative, (low_quality:1.4), (worst_quality:1.4), (badhand:1.1),collage, artist_name, signature, artist_logo, watermark,NSFW,(worst quality:2),(low quality:2),(normal quality:2),lowres,normal quality,((monochrome)),((grayscale)),skin spots,acnes,skin blemishes,age spot,(ugly:1.331),(duplicate:1.331),(morbid:1.21),(tranny:1.331),mutated hands,(poorly drawn hands:1.5),blurry,(bad anatomy:1.21),(bad proportions:1.331),extra limbs,(disfigured:1.331),(missing arms:1.331),(extra legs:1.331),(fused fingers:1.61051),(too many fingers:1.61051),(unclear eyes:1.331),lowers,bad hands,missing fingers,extra digit,bad  hands,missing fingers,(((extra arms and legs))),(EasyNegative:0.8),(badhand:0.8),nfsw,sketches, (worst quality:2), (low quality:2),lowres, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, bad anatomy,(long hair:1.4),DeepNegative,(fat:1.2),facing away, looking away,tilted head, lowres,bad anatomy,bad hands, text, error, missing fingers,extra digit, fewer digits, cropped, worstquality, low quality, ,jpegartifacts,signature, watermark, username,blurry,bad feet,cropped,poorly drawn hands,poorly drawn face,mutation,deformed,worst quality,low quality,normal quality,jpeg artifacts,signature,watermark,extra fingers,fewer digits,extra limbs,extra arms,extra legs,malformed limbs,fused fingers,too many fingers,long neck,cross-eyed,mutated hands,polar lowres,bad body,bad proportions,gross proportions,text,error,missing fingers,missing arms,missing legs,extra digit, extra arms, extra leg, extra foot,, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry,
```

------

#### **2、正面提示词**

**高质壁纸**

```sh
prompt：
masterpiece, best quality
```

**镜头虚化**

```sh
prompt：
depth of field, blurry background, blurry foreground, 
```

**画面增强**

```sh
prompt：
high resolution illustration, colorful, 8k wallpaper, highres
```

**光线增强**

```sh
prompt：
Cinematic light, ray tracing
```

**细节增强**

```sh
prompt：
hyper detailed,ultra-detailed
```
**超高细节**

```sh
prompt：
8k wallpaper,(best quality:1.12),(detailed:1.12),(intricate:1.12),(ultra-detailed:1.12),(highres:1.12)
```

------


#### **3、负面提示词**

**负面扩展**

```sh
((NSFW)),artist name, twisted torso, (((fusion), extra, bad, fewer, missing), fist,clenched hand)
```
**人物负面 1**

```sh
((NSFW)),extra fingers,fewer fingers,(low quality, worst quality:1.4), (bad anatomy), (inaccurate limb:1.2),bad composition, inaccurate eyes, extra digit,fewer digits,(extra arms:1.2),
```

**人物负面 2**

```sh
((NSFW)),(EasyNegative:1.1),ng_deepnegative_v1_75t,bad-hands-5,lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry
```
**人物负面 3**

```sh
((NSFW)),paintings, sketches, (worst quality:2), (low quality:2), (normal quality:2), lowres, normal quality, ((monochrome)), ((grayscale)), skin blemishes, age spot, glans, extra fingers, fewer fingers, multiple hands, multiple heads, Multiple arms, disabled body, illustration, 3d, sepia, painting, cartoons, sketch, bad anatomy, bad hands, collapsed eyeshadow, multiple eyebrows, pink hair, holes on breasts, stretched nipples, analog, analogphoto, signature, logo, facing away, looking away,(fat:1.2), glans,((watermark:2)),((white letters:1)), age spot, multiple eyebrows, fleckles, stretched nipples, nipples on buttocks, analog, analog photo, 2 faces, hat, bad composition, error hands, error fingers, dark, (thick eyebrows:1.2), 2girls, (((duplicate))), mutated hands,(((((fused fingers))))), (((((too many fingers))))),signature, watermark, username, blurry, artist name, text, chromatic aberration, flat color, flat shading, retro style,, low res, bad face, missing fingers, extra digit, fewer digits, multiple legs, malformation 
```
**人物负面 4**

```sh
((NSFW)),EasyNegative,paintings,sketches,(worst quality:2),(low qualaity:2),(normal quality:2),((monochrome)),((grayscale)),skin spots,acnes,skin blemishes,age spot,glans,fewer fingers,((watermark:2)),((multi nipples),bad anatomy,bad hands,text,error,missing fingers,extra digit,fewer digits,cropped,jpeg artifacts,signature,username,bad feet,{Multiple people},bad anatomy,bad hands,cropped,blurry,poorly drawn hands,poorly drawn face,mutation,deformed,extra fingers,extra limbs,extra arms,extra legs,malformed limbs,fused fingers,too many fingers,long neck,cross-eyed,mutated hands,bad body,bad proportions,gross proportions,missing fingers,missing arms,missing legs,
```
**负面**

```sh
((NSFW)),bondary,thick line,lines,lineart,ng_deepnegative_v1_75t,(badhandv4:1.2),EasyNegative,(worst quality:2),easynegative,drawing,painting,crayon,sketch,graphite,impressionist,noisy,blurry,soft,deformed,ugly,(deformed iris,deformed pupils,semi-realistic,cgi,3d,render,sketch,cartoon,drawing,anime:1.4),text,close up,cropped,out of frame,worst quality,low quality jpeg artifacts,ugly,duplicate,morbid,mutilated,extra fingers,mutatedhands,poorly drawn hands,poorly drawn face,mutation,deformed,blurry,dehydrated,bad anatomy,bad proportions,extra limbs,cloned face,disfigured,gross proportions,malformed limbs,missing arms,missing legs,extra arms,extra legs,fused fingers,too many fingers,long neck,sketches,tattoo,(beard:1.3),(EasyNegative:1.3),badhandv4,(worst quality:2),(low quality:2),(normal quality:2),lowers,normal quality,facing away,looking away,text,error,extra digit,fewer digits,cropped,jpeg artifacts,signature,watermark,username,blurry,skin spots,acnes,skin blemishes,bad anatomy,fat,bad feet,cropped,poorly drawn hands,poorly drawn face,mutation,deformed,tilted head.bad anatomy.bad hands,extra fingers,fewer digits,extra limbs.extra arms,extra legs,malformed limbs.fused fingers,too many fingers,long neck,cross-eyed,mutated hands,bad body,bad proportions,gross proportions,text,error,missing fingers,missing arms,missing legs,extra digit,extra arms,extra leg,extra foot,missing fingers,(Worst quality,low quality,lowres:1.2),error,cropped jpeg artifacts,out of frame,watermark,signature,
```

**人物负面**

```sh
negative_prompt：
((NSFW)),Photo_Comparison, 1girl, breast, standing, white shirt, phone, cellphone, smartphone, holding, sex, vaginal, picture
```

**更强的负面tag**

```sh
negative_prompt：
((NSFW)),EasyNegative, bad-artist-anime, bad-artist, bad-hands-5, bad-image-v2-39000, bad_prompt_version2
```

------


#### **4、人物提示词**

**美女起手式：**

```
Best Prompt：
Best quality, masterpiece, (photorealistic: 1.4), raw photo, (Authentic skin texture_1.3), 1 girl, solo, bangs, long hair, white dress, half body, 

negative_prompt：
(Worst quality, low quality,NSFW:2),EasyNegative,ng_deepnegative_v1_75t,
```
**精美模特prompt：**

```sh
Best Prompt：
standing, (RAW photo, best quality),(realistic,photo-realistic:1.3),masterpiece,an extremely delicate and beautiful, extremely detailed, CG, unity, 2k wallpaper, Amazing, finely detail, light smile, extremely detailed CG unity 8k wallpaper, huge file size, ultra-detailed, high res, absurdres, soft light, ((medium hair: 1.3), short bang, pink hair, floating hair novafrogsty), beautiful detailed girl, detailed fingers, extremely detailed eyes and face, beautiful detailed nose, beautiful detailed eyes, long eyelashes, light on face, looking at viewer, (closed mouth: 1.2), thigh highs, miniskirt, black underwear, unbuttoned shirt,

negative_prompt：
((NSFW)),paintings, sketches, (worst quality:2), (low quality:2), (normal quality:2), lowres,((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, age spot, glans, extra fingers, fewer fingers, ((watermark: 2)), (white letters: 1), (multi nipples), bad anatomy, bad hands, text, error, missing fingers, missing arms, missing legs, extra digit, fewer digits, cropped, worst quality, jpeg artifacts, signature, watermark, username, bad feet, {Multiple people}, blurry, poorly drawn hands, poorly drawn face, mutation, deformed, extra limbs, extra arms, extra legs, malformed limbs, fused fingers, too many fingers, long neck, cross-eyed, mutated hands, polar lowres, bad body, bad proportions, gross proportions, wrong feet bottom render, abdominal stretch, briefs, knickers, kecks, thong, {fused fingers] l, {bad bodyj]), bad-picture-chill-75v,ng_deepnegative_v1_75t,EasyNegative, bad proportion body to legs, wrong toes, extra toes, missing toes, weird toes, 2 bodies, 2 pussy, 2 upper, 2 lower,2 heads, 3 hands, 3 feet, extra long leg, super long leg, mirrored image, mirrored noise, (bad_prompt_version2: 0.8), aged up, old
```

**精致女孩**

```sh
prompt：
an extremely delicate and beautiful girl
```

**脸部增强**

```sh
prompt：
1girl face ,Curly blue hair，Delicate and perfect face, beautiful face,Happy smile,side face,Lateral face,(best aesthetic, best quality, masterpiece, extremely detailed:1.2,extremely detailed CG unity 8k wallpaper)
```

**真人照片**

```sh
prompt：
(8k, RAW photo, best quality, masterpiece, ultra highres, ultra detailed:1.2), (realistic, photo-realistic:)
```

**隐藏手掌**

```sh
negative_prompt：
lower arms,hands,palms
```

**崩坏修正**

```sh
negative_prompt：
easynegative, bad-hands-5
```

**修手**

```sh
prompt：
good hands,

negative_prompt：
bad-hands-5,bad hands, fewer digits, extra digit
```

**抽卡**

```sh
prompt：
1girl, food, candy, solo, lollipop, animal ears, black hair, controller, sleeves past wrists, can, hair ornament, game controller, horns, ahoge, streaked hair, long sleeves, blue eyes, multicolored hair, stuffed toy, swirl lollipop, white hair, animal ear fluff, long hair, fang, :d, bangs, thighhighs, twintails, socks, stuffed animal, smile, holding, wooden floor, virtual youtuber, bandaid, looking at viewer, off shoulder, monster energy, knees up, blush, asymmetrical legwear, puffy long sleeves, open mouth, shirt, candy wrapper, low twintails, cat ears, feet out of frame, hairclip, energy drink, object hug, choker, mouse (computer), bandaid on face
```

------

### Stable Diffusion 笔记

#### **1. 动漫转真人的方式**

- 文生图+controlnet_tile：
- 文生图+controlnet_canny：
- 文生图+controlnet_refer：
- 图生图+controlnet_：
  
  **对比差别：**
  
  

------

#### **2. 局部重绘的方式**

- 图生图+controlnet_inpoint：
- 局部重绘+controlnet_canny：

  **文生图_重绘幅度：就是将文生图发到图生图进行重绘**

------

#### **3. 视频转动画(Deforum)**

  **Max frames(最大帧数)**

  **Strength schedule(帧时间变化):**
  0:(0.65) → → → 第0帧开始每一帧和上一帧相似度0.65
  50:(0.5) → → → 第50帧开始每一帧和上一帧相似度0.65

  **Noise schedule(噪点时间变化):**
$$
0:(-0.06*(cos(3.141*t/15)**100)+0.06)	//缓入缓出
$$

  15：每秒帧数

  **Depth Warping & FOV(视野范围)**
  FOV schedule(视野时间变化)







------

### 实操案例

1. #### **扩图**

**文生图** + ControlNet_inpaint（局部重绘）；**only+lama**；更偏向ControlNet；缩放后填充空白；提示词可不写

> 注意：图生图不适合扩图，因为没有随机种子，人物脸部也会容易改变，重绘幅度也难把控；需要加入controlnet控制，比较麻烦。

------

2. #### **模特换装**



------

3. #### **超级符号**



------

4. **电商融图**



------

5. #### **线稿上色+转3D+三视图**



------

6. #### **模特写真照**



------

7. #### **电商打光**



------

8. #### **室内渲染**



------

9. #### **AI造字**



------

10. #### **转矢量**



------

11. #### **A1 放大**



------

