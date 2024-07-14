![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rR335dShxibibA3ibdbFtbNCO28ib12oCibOI8JZRzEdmOliam2BkZf6bLyVXNibuo5UHAeXibdktquKXW0ZrC9sQEbFKA/0?wx_fmt=jpeg)

#  【Stable Diffusion】来了来了！属于SDXL的ControlNet模型它终于来了！（测评）


Face的网址：https://huggingface.co/lllyasviel/sd_control_collection/tree/main。可以看到这里有相当多的模型，当然，我们不需要全部都下载下来，因为它们之间有很多功能是重复的，是不同的作者做出来的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOInu8XpSpqSIK8eMnDRPIGwUPfptahFRD7iccys60glVsHxObeZaiaBh8g/640?wx_fmt=png)

但是呢，  为了帮你们提前踩雷，  我把他们全部都下载了，而且逐个做了测试，看到我这么辛苦的份上，你们一定会要给我一个“点赞”和“在看”的吧。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOI9LDiaWsksVib9fw2iaK9ARolrfzEWVor3h4aZByZbVzKakiboymA7MG7Jw/640?wx_fmt=png)

接下来，让我们来分类看一下吧。

** #Canny硬边缘  **

首先是canny，它有几个不同的型号，体积越大，速度越慢。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOIKh3Huz9J1rfXib1gWtaiaTvWdoib4AQapmsjk5UkiaxI0k0WLrFicziaz9ibQ/640?wx_fmt=png)

我使用的是4080ti的笔记本进行的测试，12G显存。

  * 模型sdxl base+refiner 
  * 提示词：masterpiece,best quality,1girl 
  * 采样方法：euler a 
  * 尺寸1024*1024    

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOIUm7PL6cCX0lS2BJWJqwDTE4oQlFqUl4cU9fwLKh2SHhHbGsX91Ec1g/640?wx_fmt=png)
使用diffusers的2.5Gfull模型绘制的图片，一张图花了2分57秒，从这个效率上来看，这个大尺寸基本可以弃了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOI1bVJib6b2xBTCf550U8zZA3WZ4wGBoFmia1Gzjldj2E2WwuF8iavql2gA/640?wx_fmt=png)

使用  diffusers的  320Mb的small模型，用时34s，质量上差距不大，主要是时间优势很明显。  

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOI4oOjrzkHnnDf9awWzLhHVVtH9uuZyYKGK08vibYfFBibTPeyb7FNLjyQ/640?wx_fmt=png)

我们可以再看看其他作者的，这张是kohya的，用时33秒，更接近真实质感。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOIxebcRS5iakybBPrXbvxCdib600L2qsAOc6FwMrq4tpJV1b2DZRTye2MQ/640?wx_fmt=png)

sai的canny分为128lora和256lora，分别用时39秒和1分08秒，这个模型比较偏绘画的感觉。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOIpLuRAWTEyRwLvXHTdC7TcdhchwSZ2j4Q4iaWqeBW1IK08usF3l3uTXw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOIlE8xwWb8r3jwC07ZSZkmOJDEczmSoicBAQajbaUyicyExyu87vnmb6lQ/640?wx_fmt=png)

最后还有一个t2i的canny模型，用时34s，也是偏插画一点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOIOsmG68mSSD9TNJ1oSJyosKZ6ldd1B0NSznEquc8FfnZTSSUwUMnC3A/640?wx_fmt=png)

你们觉得哪个效果更好呢？时间上基本都在30秒以上，如果关掉refiner的话，能节省一半左右的时间，平均在17秒左右。  
** #Depth深度  ** 接下来测试一些depth模型，图形尺寸664*1024。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOIJR6r5D0QFEic4Bo7XCT1VMmjvCjkIstL1tMSRWibw3y6UzafUQDcwHBQ/640?wx_fmt=png)

使用  diffusers的full  模型  ，用时  2分48秒，sdxl给我随机到了一个拼贴画的风格。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOIMQkDCg3S7Quib91xhCdxic5UPH3ssQkCW925E1Y2icausKjEMHP9clI1g/640?wx_fmt=png)

使用  diffusers的  small  模型  ，用时  23s。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOI66plicoic1WCmDRAToNYHB6pcc6kuASgibRzRoJpPy1iaRrsh1TAm6HLQA/640?wx_fmt=png)

使用  kohya  模型  ，用时  42秒。这……好像和我的图片没什么关系。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOI58LpExHFm6VDicwVGYGicYMV3HEYInbU9CtUbRueTJ7icelPLnsiajJG0A/640?wx_fmt=png)

使用  sai  模型  ，用时1分1  2秒，画质还可以，稍微有点慢。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOIS2WcSbRbaOhFUibKpWLibUtdfuelwWNSMiaw4gicwbOzjRKEMkDpXia79Tw/640?wx_fmt=png)

使用  sargezt  模型  ，奇奇怪怪，没什么关系，用时1分52  秒。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOIRBcUhrJ8XeJ8BCqibfsv0xlictuAA51uUAib9UUE2S4ZviatabvzIVMJ6A/640?wx_fmt=png)

** # Sketch草图  ** 接下来测试一下sketch模型，画一只可爱的小猫，图形尺寸1024*624。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOITDyBcBHYqwsPJ7OTMrQN79jc2AJJLrnbibtjGac81HFUPeENGxoMlxw/640?wx_fmt=png)

使用  kohya  模型  ，用时  30秒，这是个啥？？？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOIADcrwyIticfcxfoxOHVIpo0IibJiaXPjNxCnyl6JsZ33Lw6hxmUwzfugw/640?wx_fmt=png)

使用  sai  模型  ，没找到小猫具体的位置，用时  32秒，画质还可以。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOIxV3JQENgOPQO60ShlufFia7T2BH41SzcEETuCGLo552umVhRUzVUetQ/640?wx_fmt=png)

使用  t2i  模型  ，用时  28秒，唯一一个准的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOI8aZU0W3eX9cOhVLpIH7ZnicnZP505Ac0pJAeF2icV50AZraerftFvkZA/640?wx_fmt=png)

** # Openpose骨架  ** 最后测试一下openpose模型，图形尺寸1024*624。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOISSOWwKLeo94U4PibicRJuYfFt1oIylkJfEoH8LXb5lgDsf5C9hR7wP5w/640?wx_fmt=png)

使用  kohya  模型  ，画很好看，但姿势不对，用时  40秒。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOIvILOzlBte2r9bByUszcLiajLb1q0jB5xWHQsupKTOqkc1Wbtn0Z8auw/640?wx_fmt=png)

使用  thibaud  模型  ，动作有那么点意思了，但是时间太慢了，用时  2分12秒。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibibA3ibdbFtbNCO28ib12oCibOICBZibjStDfsia3ic1c3om6wg0gN39JuHAFsWT21VmGqFy446zlkv3BRdw/640?wx_fmt=png)

** # 总结  ** 最后说下结论吧，没有权威性，全凭主观感受。  在canny模型中，我推荐使用  ** “
diffusers_xl_canny_small  ”  ** ，  出图快，效果也还不错；depth模型中，我推荐使用  **
“diffusers_xl_depth_small”  ** ，理
由同上，其实“sai_xl_depth_128lora”效果也不错，但是渲染时间太长了，当然这个不是模型的问题，是我的问题，因为我买不起那么好的电脑；Sketch模型中，我推荐使用
** “t2i-adapter_xl_sketch”  ** ，这是腾讯家出品的，起码还挺还原的；openpose模型中，推荐  **
“thibaud_xl_openpose_256lora”  ** ，虽然它画的不太准，但是它时间短啊，唉。。。
以上就是对sdxl的controlnet在webUI中表现的测评。  虽然  我的测评并没有很严谨（  客  观原因还是sdxl对机能的要求太高了  ）
，  但是  总体的成功率感觉还是太低了
。而且因为sdxl模型支持多种画风，所以在我的提示词中并没有给出具体要求的情况下，controlnet的结果是千变万化的。  
