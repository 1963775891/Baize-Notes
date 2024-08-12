## **1 配置ComfyUI运行环境**

1. Nvidia显卡驱动下载地址

https://www.nvidia.cn/geforce/drivers/

2. 安装Git，非常强大的软件版本管理工具，下载和更新开源项目都靠它

https://git-scm.com/download/win

3. 安装Python，它其实是Python语言的运行环境，版本不要太新，有些软件包不能兼容Python的新版本，安装的时候选中“将Python添加到系统变量”，系统变量需要重启才能生效，后面我们安装CUDA再重启

https://www.python.org/downloads/release/python-3119/

4. 安装CUDA 12.2，AI领域非常重要的通用计算软件包，Nvidia的市值全靠它，安装后重启Windows

[https://developer.nvidia.com/cuda-12-2-0-download-archive?target\_os=Windows&target\_arch=x86\_64&target\_version=11&target\_type=exe\_local](https://developer.nvidia.com/cuda-12-2-0-download-archive?target_os=Windows&target_arch=x86_64&target_version=11&target_type=exe_local)

5. 安装 [cuDNN v8.9.2 (June 1st, 2023), for CUDA 12.x](https://developer.nvidia.com/rdp/cudnn-archive#a-collapse892-120)，可以把它看成CUDA的扩展包，有些软件包要用到它，有备无患，编辑一下系统环境变量

[https://developer.nvidia.com/rdp/cudnn-archive#a-collapse892-120](https://developer.nvidia.com/rdp/cudnn-archive#a-collapse892-120)

![](https://cdn.openart.ai/wangeditor_uploads/i0Fw5vnAPfyXOXA92IIF/compressed/image_KeDAyS6F_1715605995277_512.webp)

![](https://cdn.openart.ai/wangeditor_uploads/i0Fw5vnAPfyXOXA92IIF/compressed/image_Msk7g3zi_1715606074829_512.webp)

这样就满足了onnxruntime-gpu 1.17的环境要求，InstantlD Face Analysis如果要以CUDA方式运行，就需要这样的环境。

![](https://cdn.openart.ai/wangeditor_uploads/i0Fw5vnAPfyXOXA92IIF/compressed/image_2Y3N5V_o_1715606349508_512.webp)

![](https://cdn.openart.ai/wangeditor_uploads/i0Fw5vnAPfyXOXA92IIF/compressed/image_y1oj9183_1715606161629_512.webp)

## **2 安装ComfyUI本体**

1. 通过git下载ComfyUI

https://github.com/comfyanonymous/ComfyUI

打开官网阅读安装说明，找到想要安装的位置，打开命令提示符cmd，家里网不好的话开一下加速（如果你的加速端口不是7890，自己修改一下端口）

```markdown
set http\_proxy=http://127.0.0.1:7890 & set https\_proxy=http://127.0.0.1:7890
git clone https://github.com/comfyanonymous/ComfyUI.git
```

2. 给ComfyUI创建一个它自己专属的虚拟环境，如果以后还要安装其他Python项目，不同项目需要的软件包都不一样，共用一个环境的话就会相互打架，虚拟环境可以避免发生冲突

```markdown
cd ComfyUI
python -m venv .venv
```

3. 要对虚拟环境进行操作，就要先激活虚拟环境，否则就是在操作非虚拟的系统环境

```markdown
cd .venv
cd Scripts
activate.bat
```

激活成功后命令提示符的最前面会显示(.venv)

4. 更新一下Python的软件包管理工具pip，下载和更新软件包都靠它

```markdown
python.exe -m pip install --upgrade pip
```

5. 安装Torch，打开PyTorch官网复制安装命令，这个安装命令经常会更新，推荐安装2.3.0，这个版本可以兼容xformers	https://pytorch.org/

```markdown
pip install torch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 --index-url https://download.pytorch.org/whl/cu121
```

可以顺便安装一下xformers

```markdown
pip install xformers==0.0.26.post1

和flash attention

pip install https://github.com/bdashore3/flash-attention/releases/download/v2.5.8/flash\_attn-2.5.8+cu122torch2.3.0cxx11abiFALSE-cp311-cp311-win\_amd64.whl
```

6. 安装ComfyUI所需要的软件包，安装之前我们先检查一下requirements.txt的内容，很多软件包都是通过Torch来调用CUDA，它非常基础，有CPU版本和GPU版本，我们需要安装GPU版本，所以我们先删掉**torch和torchvision**，避免它用CPU版本覆盖我们刚才安装的GPU版本

```markdown
cd ..
pip install -r requirements.txt
```

7. 创建启动文件，打开记事本，复制下面的内容（7890端口号可能要自己修改，家里网好的话删掉这一句），将文件保存为start-comfyui.cmd文件，保存类型“所有文件”，存到ComfyUI目录下

```markdown
set http\_proxy=http://127.0.0.1:7890
set https\_proxy=http://127.0.0.1:7890
echo "Start VENV"
call .venv\\Scripts\\activate.bat
echo "Start ComfyUI"
python -s main.py --auto-launch --listen --use-pytorch-cross-attention
pause
```

8. 双击运行start-comfyui.cmd，启动ComfyUI

9. 打开OpenArt，下载工作流，拖进ComfyUI界面中（ComfyUI生成出来的图片默认带有工作流信息，也是可以拖进界面里载入工作流的）

https://openart.ai/workflows/datou/manga-cosplay/SgsFFSuOeFe7Qzs3eHij

理论上会出现一片红，工作流无法运行，这是因为缺失了很多自定义节点（ComfyUI自带的节点叫官方节点，其他开发者开发的节点叫自定义节点），不用紧张，安装了工作流需要的自定义节点后就不红了

## **3 安装ComfyUI自定义节点**

1. 先安装一个自定义节点管理工具ComfyUI Manager，养成一个习惯，安装前先仔细阅读安装说明

https://github.com/ltdrdata/ComfyUI-Manager

2.  回到之前安装ComfyUI的命令提示符窗口

```markdown
cd custom\_nodes
git clone https://github.com/ltdrdata/ComfyUI-Manager.git
```

3. 养成另一个习惯，先检查requirements.txt，确认一下有没有torch、torchvision，有的话删除掉

```markdown
cd ComfyUI-Manager
pip install -r requirements.txt
```

4. 重新运行start-comfyui.cmd，启动ComfyUI，打开Manager，点击Install Missing Custom Nodes，挨个安装缺失的节点（不要安装Comfy\_KepListStuff节点），安装完成后重启

（更安全的方法是挨个git clone安装自定义节点，挨个检查requirements.txt，确认一下有没有torch、torchvision，一发现就删除，挨个pip install -r requirements.txt，然后重启ComfyUI）

5. 如果一切正常的话，ComfyUI启动后会提示三个InstantID相关的节点缺失，从命令提示符窗口可以看到造成这个问题的原因是insightface软件包安装失败，安装它需要用到Visual Studio的编译工具，下载安装VS，选中Python开发和C++开发，点击安装，安装后不用重启Windows

https://visualstudio.microsoft.com/zh-hans/free-developer-offers/

6. 回到之前安装ComfyUI的命令提示符窗口，安装insightface

pip install insightface

7. 再运行start-comfyui.cmd，启动ComfyUI，所有节点都正常了

8. 安装Ollama

https://ollama.com/

9. 安装Ollama模型，新开一个命令提示符窗口，家里网不好还是先加速一下

```markdown
set http\_proxy=http://127.0.0.1:7890 & set https\_proxy=http://127.0.0.1:7890
ollama run llava-phi3:3.8b-mini-fp16
ollama run llama3:8b-instruct-q6\_K
```

![](https://cdn.openart.ai/wangeditor_uploads/i0Fw5vnAPfyXOXA92IIF/compressed/image_o8MuS8RE_1715481462456_512.webp)

[https://x.com/xulzy\_6/status/1787684486815396073](https://x.com/xulzy_6/status/1787684486815396073)

## **4 安装工作流需要的其他模型文件，工作流里都有写**



## **5 运行工作流**

> 如果安装了正确版本的CUDA和cuDNN后InstantlD Face Analysis还是无法调用CUDA，可以试试激活虚拟环境后，运行
>

```markdown
pip uninstall onnxruntime onnxruntime-gpu
pip install onnxruntime-gpu --extra-index-url https://aiinfra.pkgs.visualstudio.com/PublicPackages/\_packaging/onnxruntime-cuda-12/pypi/simple/
```

然后重启ComfyUI