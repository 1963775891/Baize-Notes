![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tyssYUEyRwzibeehwRxP8YUOVdZiaXkzZBgb6VmmaDtp8TbFFEhDN5jkAejqd7VnWKCGfic0rnlKYR8ssj8PMplCg/0?wx_fmt=jpeg)

#  【Stable Diffusion】简笔水彩风格插画

吴溪源  [ 小鱼干了 ](javascript:void\(0\);)

**小鱼干了**

微信号  ifishhh

功能介绍  不定期推送AIGC指南，设计干货，行业内幕，观点吐槽... ... 这里有好玩的地方，美味的食物，优秀的设计，实惠的旅程，以及不正经的观点...

__ __

__ _ _

今天给大家推荐一个大模型和  lora的组合运用，可以生成一些类似简笔  水彩风格的插画。  首先是这个大模型“  Flat-2D Animerge
”，适合生成一些卡通动漫的图片。官方建议CFG值在5或6比较好。（如果使用动态阈值修复的话，可以拉到11）

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibeehwRxP8YUOVdZiaXkzZBglBL3e7J48ElOxBQMCkTLFsHbxlnEMuQCDpYM0ylcXjzhGQh2CzOPw/640?wx_fmt=png)

还有两个lora，一个是“  Chinese painting style  ”，这个可以增加一些中国画水彩风格的效果。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibeehwRxP8YUOVdZiaXkzZBCYOjWOR5sTq8o9CCLraicLop3l3RJ2C3yu5icJ6HgBUkGlKUszLD3Eaw/640?wx_fmt=png)

还有一个lora是“  Crayon drawing  ”，它可以给画面添加一些简单的线条和小孩子的笔触。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibeehwRxP8YUOVdZiaXkzZBsw7Fcefe1cOrKDAr8Q5Pxle8XyicsialxymjeMFfENgJR3jPaL07QZzg/640?wx_fmt=png)

接下来，我们使用这三者的组合，将下面这张图片转换为简笔水彩风格吧。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibeehwRxP8YUOVdZiaXkzZBu2pTDBfMfQeyibo3Pxe4D50jk78CIUgTjlciaHoxibSp9HSQTQ8kch2QQ/640?wx_fmt=png)

将图片丢到标签器中，反推出关键词，然后发送到“文生图”。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibeehwRxP8YUOVdZiaXkzZBgwC9fhsW5T39FibKWEHv3BZ55rQIicyXcQrV7dS3ibFjE7DMMfcET5aYg/640?wx_fmt=png)

在正向提示词的末尾，添加上这两个lora,  “  Chinese painting style  ”权重设置为0.4，  “  Crayon
drawing  ”权重设置为0.8。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibeehwRxP8YUOVdZiaXkzZBibHpUpOJ4Ticy9pOkLzr09LpaY3mciaKfrgwtB8Nc8P1pJR3s2Y1ZffSg/640?wx_fmt=png)

尺寸按照参考图设置好，重绘幅度开0.5可以让AI更自由发挥一点，如果想和原图更接近，可以降低数值。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibeehwRxP8YUOVdZiaXkzZBgficWTA7YtTwIr1WKhkqeFIg0iadWjuyf4KX3icicJobXkxdNibTn39a4zg/640?wx_fmt=png)

将图放入controlnet中，选择tile模型，权重为0.5，控制模式选择“更注重提示词”。这里的权重主要会影响画面的复杂度，数值越高，细节越多，数值太低的话，会和图像差得比较远。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibeehwRxP8YUOVdZiaXkzZB3HCbJxt03b899D6ibq7ml6swdpiauHLd82VCBqxwZoaBI4iccCaXMLRyg/640?wx_fmt=png)

点击生成，这样一幅简笔水彩风格的插画就完成了，是不是很治愈呢？

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibeehwRxP8YUOVdZiaXkzZBaia1N0f5HUgCryJKo0icYfhmrsib598x0vTaLicyHaSAAVictMVShzlCfFQ/640?wx_fmt=png)

当然，这是在有参考图的情况下，我们对原图进行的风格化转变。如果你想要画出原创的卡通插画，就可以不使用controlnet。  
我们还是使用这个大模型和lora搭配，只不过调整一下提示词，这里我将提示词调整为“一个女孩坐在沙发上，吃西瓜，看电视，夏天”。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibeehwRxP8YUOVdZiaXkzZBu6sFRicJ6fRicqCj0ssicxYLbujIkOweyfJttl9MPc2ppGWHoMhWc5kXQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibeehwRxP8YUOVdZiaXkzZBicepwoWDTTUG7sG3IT8bsvR0k2pT8pvPI2cFRGjpnghmIs7jYDpIzlg/640?wx_fmt=png)

完成后有些小瑕疵，比如手里西瓜的部分，还有脚的部分。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibeehwRxP8YUOVdZiaXkzZBYj3ACH2jq83iah74CwHmoVN5JC8ib2nG55pYx1ljhlZ0C5Ctriad7aGjA/640?wx_fmt=png)

送到ps里后期修复一下，西瓜的部分可以使用“创成式填充”，让AI帮你画好。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibeehwRxP8YUOVdZiaXkzZBIEwFbibUgqEWln1vV36v4a8OBFI1mic9beMToZBbRibL1kOqjfFGnvhHA/640?wx_fmt=png)

脚的部分有点难，AI搞不清楚结构，那就用画笔修一下好了，毕竟是简笔画，对细节要求不是很高。这样 ，一幅还蛮有意思的小插画就做好啦。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwzibeehwRxP8YUOVdZiaXkzZBdBNG0MMCUnqWcKSiaWiafia9SFFZWH3weia3vYxUxmI0ibGGeMNhDe01g2A/640?wx_fmt=png)

以上，就是  关于简笔水彩风格绘画的介绍，你学会了吗  。  如果想要  这些模型和lora  的话，可以添加我的公众号【  **白马与少年**
】，回复【SD】即可。  
  
  

预览时标签不可点

微信扫一扫  
关注该公众号



轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/fY8ibThH1At6iciciaKY5WZ4ib8CVibVnVHRJwGj6ksg7fk0tzTMuLPsvptv6zswtKfCLNFwYr9aIBGkjiaYGBWtibwnOQ/0?wx_fmt=png)

小鱼干了







****



****



  收藏

