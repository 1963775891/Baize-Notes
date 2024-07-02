![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tyssYUEyRwwpS8rhVWtKWdr2fGlObzXnK3XRhz7AJzO398riaseiajLYBf6AOVVSeyico7cjnTvWS8iaVZYiaFV5Hgg/0?wx_fmt=jpeg)

#  【Stable Diffusion】Openpose再添新活，ControlNet里面直接编辑骨架图！

原创  吴溪源  [ 白马与少年 ](javascript:void\(0\);)

**白马与少年**

微信号  StreamWXY

功能介绍  Stable Diffusion、Blender等学习心得分享

__ __

__ _ _

我们在用参考图推理骨架的时候，会出现识别不准确，导致姿势不对的问题，但是要调整这个骨架又很麻烦。

最近的controlnet版本更新，当预览openpose骨架图的时候，右下角出现了一个编辑的按钮。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwwpS8rhVWtKWdr2fGlObzXnicmqpUI0RhoHyXIpGdVudicqjcxx4XdcA7DqibyJoEyfeSnIaV4goeenw/640?wx_fmt=png)

点击之后会弹出来这样一个页面，告诉我们缺少一个插件——  sd-webui-openpose-editor-main  ，再次点击这行白色的字。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwwpS8rhVWtKWdr2fGlObzXnXWLA9a53lrJTibDiacOF4D1nt55FpqETibRq2M8mZDmdvjtqdsMZYv0Vg/640?wx_fmt=png)

会跳转到这个插件的下载页面，可以直接下载，也可以复制这个网址去SD里面“从网址安装”。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwwpS8rhVWtKWdr2fGlObzXnPzzmeahUSDROPgT1uvia4v2ItBwjoicovDJKuXoT3SIK323b850eiaxyQ/640?wx_fmt=png)

安装完成之后，重启webUI，检查一下这个路径下“  stable-diffusion-webui\extensions\sd-webui-
openpose-edito  r  -m  ain  \di  st  ”是否存在dist文件且包含内容，中国大陆的一些用户报告了使用自动更新脚本下载
dist 时遇到的问题。如果没有的话，就直接去下载我云盘里的插件包。

然后使用openpose处理出骨骼图，再次点击“编辑”。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwwpS8rhVWtKWdr2fGlObzXngH2COCtJtYU3z20icXxd4v971QOIOagfeia9jiaarCTX095wpYRwpss8w/640?wx_fmt=png)

我们就可以进入到这个openpose的实时调整界面了。  

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwwpS8rhVWtKWdr2fGlObzXnxXn7BzM2qR26PvgS2ebdRdnj4j9Et7IoWV9KcgsmaZ5YZo5GiaB3MXA/640?wx_fmt=png)

我们可以通过实时调整给人物变换一个姿势。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwwpS8rhVWtKWdr2fGlObzXnF0XPOsdXHV8wweB8RMqDGN99lccpMrtAiaokH3nTNOvsVx5mNtNdMbQ/640?wx_fmt=png)

然后点击“发送到controlnet”。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwwpS8rhVWtKWdr2fGlObzXnJoPicuPQBseYd7JAfbyN2wN5ImacUZARGlC34HxfZ3ffZMT9icUgib7ew/640?wx_fmt=png)

关掉预处理器，直接将骨骼图作为结果输入。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwwpS8rhVWtKWdr2fGlObzXnibgkDib8AOfyAGLtJiawX88cxHhtSGcBoFo4zxYdPuZIBLxiclSSnP1iaHw/640?wx_fmt=png)

开启高清修复，这样我们的动作就改好了。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwwpS8rhVWtKWdr2fGlObzXnbiaCgDWTeuWa82kQCBXStWBLcL5a3o9xJDOsOoHs86zn4U7ogJHXfsA/640?wx_fmt=png)

效果很棒。

![](https://mmbiz.qpic.cn/mmbiz_png/tyssYUEyRwwpS8rhVWtKWdr2fGlObzXnStGJIVdIRHhtovicyhaLHPaibbLRlFegzy9zHoEVmg9M8MuWAM5oZHvg/640?wx_fmt=png)

这个插件可以用来帮助我们微调与参考图不匹配的骨架，也可以在原骨架上调整修改动作，总之能直接在controlnet里面改骨架还是非常方便的了。
大家想要这个插件的话，可以添加我的公众号【  **白马与少年** 】，回复【SD】即可。  
  
  

预览时标签不可点

微信扫一扫  
关注该公众号



轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rR335dShxibicFrWhQnGuwdp4icKgCxibWO94LTgVCdyGEa5tticq3VQ0wbSfnGkl6ficicgn1LmHvKohOIT76T3un55Q/0?wx_fmt=png)

白马与少年







****



****



  收藏

