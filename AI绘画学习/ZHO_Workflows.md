## 工作流合集

```markdown
文生图：Checkpoint → Lora  → CLIP  → ControlNet  → 采样器  → VAE解码  → 出图
                                                   ↑
图生图：                               加载图像 → vae编码      
```

## 1. 基础工作流

#### 1.1 文生图

![文生图](./../note_img/assets/1-1.jpg)

#### 1.2 图生图

![图生图](./../note_img/assets/1-2.jpg)

#### 1.3 节点束输入 输出 编辑

![节点束输入输出编辑](./../note_img/assets/1-3.jpg)

#### 1.4 通配符与风格提示词

![通配符与风格提示词](./../note_img/assets/1-4.jpg)

#### 1.5 ControlNet

![ControlNet](./../note_img/assets/1-5.jpg)

#### 1.6 细节修复

![细节修复](./../note_img/assets/1-6.jpg)

#### 1.7 XY对比

![XY对比](./../note_img/assets/1-7.jpg)

#### 1.8 单项对比
![单项对比](./../note_img/assets/1-8.jpg)

#### 1.9 图像反推提示词

![图像反推提示词](./../note_img/assets/1-9.jpg)

#### 1.10 背景去除

![背景去除](./../note_img/assets/1-10.jpg)

#### 1.11 重绘扩图

![重绘扩图](./../note_img/assets/1-11.jpg)

#### 1.12 噪声注入

![噪声注入](./../note_img/assets/1-12.jpg)

#### 1.13 稳定联接

![Cascade](./../note_img/assets/1-13.jpg)

#### 1.14 Stable Diffusion 3 API

![SD3API](./../note_img/assets/1-14.jpg)

#### 1.15 CosXL图像编辑

![CosXL图像编辑](./../note_img/assets/1-15.jpg)

## 2. 进阶工作流

#### 2.1 ipadapter

![ipadapter](./../note_img/assets/2-1.jpg)

#### 2.2 instantID

![instantID](./../note_img/assets/2-2.jpg)

#### 2.3 LayerDiffusion

![LayerDiffusion](./../note_img/assets/2-3.jpg)

#### 2.4 局部重绘进阶

![局部重绘进阶](./../note_img/assets/2-4.jpg)

#### 2.5 IC-Light

![IC-Light](./../note_img/assets/2-5.jpg)

## 3. 实用工作流

#### 3.1 角色一致性

#### 3.1.1 角色三视图与特写

![角色三视图与特写](./../note_img/assets/3-1-1.jpg)

#### 3.1.2 电商工作流

![](./../note_img/assets/3-2-1.jpg)

------

## 4. 稳定联接

![](./../note_img/ZHO_Workflows/Dingtalk_20240317192159.jpg)

------

#### 1 稳定联接 -标准

![](./../note_img/ZHO_Workflows/Dingtalk_20240317182319.jpg)


#### 2 硬边缘 Canny ControlNet

![](./../note_img/ZHO_Workflows/SCCN.jpg)

#### 3 重绘 Inpainting ControlNet

![](./../note_img/ZHO_Workflows/SCCN2.jpg)

#### 4.4 图生图

![](./../note_img/ZHO_Workflows/Dingtalk_20240308004442.jpg)

#### 5 稳定联接 ImagePrompt Standard

![](./../note_img/ZHO_Workflows/Dingtalk_20240326235311.jpg)

#### 6 稳定联接 ImagePrompt Mix

![](./../note_img/ZHO_Workflows/Dingtalk_20240327004040.jpg)

------

## 5. 3D

![](./../note_img/ZHO_Workflows/S232.jpg)


#### 5.1 CRM Comfy 3D

![](./../note_img/ZHO_Workflows/C3DCOLAB.jpg)

#### 5.2 草图 3D

![](./../note_img/ZHO_Workflows/Dingtalk_20240316231428.jpg)

   【Sketch to 3D】使用说明：

   - 使用模型：
      - [Playground v2.5.jpg)
      - [ControlNet.jpg)

   - 使用插件：
      - 草图画板：[AlekPet.jpg)
      - 背景去除：[BRIA_AI-RMBG.jpg)
      - TripoSR 3D生成：[TripoSR-ZHO.jpg)

#### 5.3 LayerDIffusion + TripoSR V1.0

![](./../note_img/ZHO_Workflows/Dingtalk_20240309193351.jpg)

   - 使用插件：
      - [LayerDIffusion.jpg)
      - [TripoSR-ZHO.jpg)




 ###3️⃣ LLM + SD

![](./../note_img/ZHO_Workflows/Dingtalk_20240130191521.jpg)

------

## 6. 重绘

#### 6. 1 简单 DD 重绘

![](./../note_img/ZHO_Workflows/Dingtalk_20240304191711.jpg)


#### 6.2 文生图 + DD 重绘 

![](./../note_img/ZHO_Workflows/Dingtalk_20240304195830.jpg)




 ###5️⃣ [YoloWorld-EfficientSAM

![](./../note_img/ZHO_Workflows/ywes_.jpg)





## 7. 分割

#### 7.1 图片检测+分割

![](./../note_img/ZHO_Workflows/Dingtalk_20240224154535.jpg)


#### 7.2 视频检测+分割

![](./../note_img/ZHO_Workflows/Dingtalk_20240317184123.jpg)

------

## 8. InstantID

#### 8.1  InstantID_pose_ref + ArtGallery

![](./../note_img/ZHO_Workflows/Dingtalk_20240124232833.jpg)


#### 8.2 InstantID_locally_pose_ref

![](./../note_img/ZHO_Workflows/Dingtalk_20240124230609.jpg)

------

9️⃣ [PhotoMaker-ZHO

![](./../note_img/ZHO_Workflows/Dingtalk_20240117201201.jpg)


## 9. Disney-风格+蒙版 

#### 9.1 lora + batch

![](./../note_img/ZHO_Workflows/Dingtalk_20240119202403.jpg)

#### 9.2  portraitmaster + styler + lora

![](./../note_img/ZHO_Workflows/Dingtalk_20240119201125.jpg)

------

#### 9.3 TravelSuite

![](./../note_img/ZHO_Workflows/Dingtalk_20240317191556.jpg)

------

#### 9.4 Latent_travel_workflow

![](./../note_img/ZHO_Workflows/9b2a5aa4875c678c95da6ffd80fb5512.jpg)

------

## 10. WordCloud

![](./../note_img/ZHO_Workflows/Dingtalk_20240317192659.jpg)

------

#### 10.1  WordCloud

![](./../note_img/ZHO_Workflows/Dingtalk_20240317192616.jpg)
