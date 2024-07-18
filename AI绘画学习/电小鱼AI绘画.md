## 1、文生图-txt2img

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/txt2img00_03-scaled.jpg)

### **CLIP skip**

先看名稱有CLIP(Contrastive Language-Image Pre-Training)，我們就可以知道，這裡在圖片生成過程中主要是介入到 “Prompt轉換給Stable Diffusion理解/參照”這段。一般使用時，都是默認的預設數值就好，如遇到模型在使用說明中有特別提到使用指定的clip skip數值會產出較理想結果時，再來使用即可。

從網上相關的原理說明來看(想深入了解原文解釋的可參考網址中Clip Skip這段說明→https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Features#clip-skip)。我的理解就是，文字資訊Prompt的內容是會被分層分類，一層層推進過濾，愈分愈細，最終Stable Diffusion就會以讀取到的分層分類後的資訊進行繪圖。(ex. 人類分成男性、女性→女性又再分成女孩、女人→女人又再細分下去，可能是依人種、髮色、穿著、動作…等不同特徵來分類。)

而Clip skip的數值範圍從1~12(層)，如果我需要完整保留prompt所有細節描述精準的產出，那就不要跳過任何一層分類(這裡是數值1)，如果我想讓Stable Diffusion在不同程度/內容細節上可以更自由發揮創意，那就把數值逐漸拉高(跳過更多分類層)測試看看。skip數值愈大，所生成的圖像也愈偏離提示詞內容，但同時Stable Diffusion也能較不受提示詞限制，在更廣的分類層下有更多的素材內容可以取用作圖。

下面測試了2個案例

案例一、提示詞是”a girl, black long hair, wearing sunglasses”。

Clip skip1~3之間，所有提示詞的內容都有呈現符合，一個女孩、黑色長髮，戴著太陽眼鏡。  
Clip skip4~6之間，髮色開始跑掉不是指定的黑色。  
Clip skip7之後太陽眼鏡都不見了，且有的髮色不是黑色，有的變成短髮。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/txt2img05_02.png)

案例二，提示詞只有”a cat”，當Clip skip的數值愈高，就開始愈來愈不像貓，神態長得開始往狗/或其它動物的方向去。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/txt2img06.png)

### 正、反向提示詞輸入

正向提示詞(Prompt)就是我們需要畫面中出現的內容，但有時生成的圖片雖然都符合了我們所描述的同時，畫面中也可能會多出一些其他我們不想要的內容，這時就需要利用反向提示詞(Negative Prompt)去告訴Stable Diffusion，我不要什麼。

下面是提示詞的一些基本格式寫法和原則。

- 提示詞可以是單字、單詞或是短句。  
  “1girl, beautiful, sitting, sofa”  
  “a beautiful girl, sitting on the sofa”  
  “a beautiful girl is sitting on the sofa”
- 不同關鍵詞間以英文逗號分開，逗號前後有無空格不影響生成內容。
- 放在愈前面的提示詞，權重愈高。
- **增強/減弱**提示詞權重的寫法 :  
  – **(提示詞:權重數值)**, 權重數值一般默認為1，低於1減弱、大於1加權，0.1~2之間較不會讓畫面崩壞。 ex. (one girl:1.2)，(red hair:0.8)  
  – **(提示詞)** = 增強1.1倍權重，((提示詞)) = 增強1.1\*1.1倍權重。ex. (one girl) = (one girl:1.1)  
  – **\[提示詞\]** = 減弱1.1倍權重，\[\[提示詞\]\] = 減弱1.1\*1.1倍權重。
- **混合** : 利用”**AND**“進行多種元素強制融合。 ex. 1cat AND 1dog = 產生出來的圖像會同時具備貓和狗的特徵。  
  變化方式可以利用” :數字”來加權重。ex. 1cat AND 1dog:1.6 = 產生出來的圖像會同時具備貓和狗的特徵，但會更偏向狗的特徵。
- **交替換算** : **\[提示詞1|提示詞2\]** = 提示詞1、2交替演算(一步畫提示詞1、一步畫提示詞2，反覆交替)，成像會更偏向前面的提示詞，功能類似AND。ex. \[1cat|1dog\]
- **漸變** :  
  – **\[提示詞1:提示詞2:數字\] = \[from:to:when\] :** 數字大於1時，理解為第x步以前生成提示詞1，第x步開始生成提示詞2。ez. \[1cat:1dog:20\]=1~19步生成貓、20~生成狗。數字小於1時，理解為百分比%。  
  – **\[提示詞:數字\] = \[to:when\] :** \[flower:20\] = 從第20步開始生成花，\[flower:0.5\]=總步數的50%開始生成花。  
  – **\[提示詞::數字\]** = **\[from:when\] =** \[flower::20\] = 到第20步停止生成花，\[flower:0.5\]=到總步數的50%停止生成花。

來測試一個漸變的案例 :  
提示詞是 : \[1cat:1dog:20\]，總步數(Steps)為40。很明顯20以前都是在生成貓，20以後開始加入/生成狗的外貌特徵。
![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/xyz_grid-0008-3654281751-scaled-e1691582092133.jpg)
透過案例來比對一下套用embedding、Lora以及LyCORIS模型的出圖效果。

案例一、”a girl in leather jacket”
![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/txt2img16.png)
當其它所有參數設定都不變動，只套上Emma Watson的embedding(Textual Inversion)。按下小紅書叫出模型選單，點選要使用的Embedding, 讓這個embedding的”觸發詞(Trigger Words)”顯示在Prmopt欄裡。最後生成出來穿皮衣的Emma Watson。
![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/txt2img17.png)

案例二、”a girl sitting on a chair”
![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/txt2img18.png)
一樣所有參數設定都不變動，再添加讓人物穿上特定風格服飾的Lora。<lora:lo\_dress\_classic\_style3\_v1**:1**\>，套用上的Lora，在冒號後面的數字代表權重，預設是1，可自行調整影響的權重。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/txt2img19.png)

案例三、和案例一同樣”a girl in leather jacket”的設定，改套用Emma Watson的LyCORIS模型。  
(PS. 自WebUi 1.5.0以後的版本，LyCORIS模型不需要再另外下載外掛就能直接使用，所有LyCORIS模型放置的位置和使用方法都和Lora一樣。)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/txt2img17_02.png)

### 出圖參數設置

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/txt2img24_02.jpg)

- **Sampling method(採樣方法)** : 根據不同的Checkpoint模型，都會有個別更適合使用的採樣方法。通常我都是直接設定使用Civitai模型資訊說明裡推薦的採樣方法。而每個採樣方法的出圖效率速度都不一樣，實際測試實驗對比可參考下列說明文章，有詳細說明。[→ AI繪圖-實測：比較目前20種採樣方式的速度與圖片生成結果(stable diffusion webui)
- ![](https://vocus.cc/article/6423ef9ffd897800011688b1.jpg)
- **Sampling Steps(採樣/迭代步數)** : 這裡是控制圖片去噪的步數，一般來說，步數愈高畫得愈細緻，但同時也更費時。根據使用的採樣方法不同，也都會有個別適合的步數範圍。一般我都是設在20~40之間。如果是動物有毛皮紋理特別需要細節呈現的圖像，就盡量拉高一些試看看(40左右)。

------

- **Restore faces (面部修復)** : 生成人像圖如果出現”臉崩/面部畸形”的情況時可開啟使用。但這比較適合在畫三次元真人人像時使用，二次元的圖不適合(反而成像效果更差)。

- **Tiling (平舖)** : 生成可平舖的圖(Seamless Pattern)

- **Hires. fix (高清修復)** : 假設畫一張512\*512全身人像時，由於臉部在畫面中所佔的比例很小，所被分配到的像素/噪點不夠多，生成的人臉就很容易崩壞。如果此時開啟高清修複功能(假設放大2倍)，原本512\*512的圖變成1024\*1024，臉部也因此按比例多增加更多的像素/噪點可用(SD有更大的空間去針對臉部作畫/畫更細緻)，就可修復原本崩壞的人臉。  
  勾選Hires. fix後另展開的設定選項如下圖 :  
  ![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/txt2img25.png)

  – _**Upscaler (放大演算法)**_ : 在預設的放大演算法清單中，建議使用**R-ESRGAN4x+(畫真人/三次元)、R-ESRGAN4x+Anime6B(畫動漫二次元)**。  
  – _**Hires steps (高清修復採樣步數)**_ : 設置為0時代表與原始圖像生成的採樣步數一樣。  
  – **Denoising strength (重繪幅度)** : 數字越低，對原圖產生的變化越少，但同時對臉部的修復效果也較不明顯。一般通常設置在0.4~0.7間平衡修復和維持原圖關係的效果較剛好。

- 高清修復和面部修復最好不要同時開啟使用。

------

- **圖片寬高設定** :  
  – Stable Diffusion1.5版本是用512\*512的圖去訓練出來的模型。如果寬高設定超過這範圍，整個畫面的構圖容易會出現奇怪的重複(ex. 人物有2顆頭、連體嬰….)，因此寬高設定盡量至少其中有一邊設在512-768之間。  
  – 想要生成大圖時，可先生成512或768的小圖，再勾選啟用高清修復重繪放大。這樣構圖內容就不會出問題的同時也能生成高清的大圖。又或者在文生圖裡先生成小圖，之後再把小圖丟到圖生圖(img2img)裡重繪放大。在這裡大家應該了解到，其實在文生圖裡的高清修復(Hires. fix)，就等於是先把圖生圖裡重繪放大的功能提取出來併到文生圖的介面裡同時一次出圖使用。
- **生成圖片數量** : Batch size拉高容易爆顯存，如果想一鍵同時生成多張圖又不想爆顯存的話，調高Batch count數量較適合。
- **CFG Scale – Classifier Free Guidance Scale (提示詞相關性)** : 官方定義是指用來調節提示詞對擴散過程的引導程度。數值越高越偏向提示詞內容生成，數字越低，Stable Diffusion就越自由發揮，忽略提示詞內容。  
  數值設定建議 :  
  0-1時 : 圖像崩壞  
  2-6時 : 生成圖像比較有想像力(漸偏離文本內容)  
  7-12時 : 普遍效果較好，既有創意也能遵循文字的提示詞  
  10-15時 : 提示詞影響生成圖像更多，另畫面的對比飽和度也會上升  
  18-30時 : 畫面逐漸崩壞，但另再拉高採樣步數可以降低崩壞程度

------

- **Seed (隨機種子)** :  
  – 數值為 -1 時，每次隨機產生不同的噪聲圖。如果是指定的種子數值就會產生同樣的噪聲圖。  
  – 在種子數值和其它所有參數設定都一模一樣的條件下所生成的圖會近99%相似，但仍不會100%一樣(神經網絡工作的原理不會產生100%一模一樣的圖)。

勾選Extra，會展開另一個隨機種子選項。(這個Extra的Seed平時不太會用到)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/txt2img26.png)

- **Variation seed (差異隨機種子)** : 生成圖像時，同時產生另一張噪聲圖，調整差異強度去控制生成的圖像。  
  – 強度設定0時，用Seed的噪聲圖去生成的圖像  
  – 強度設定1時，用Variation seed的噪聲圖去生成的圖像  
  – 強度設定0.5時，用2張種子的噪聲圖按比率去生成的圖像

------

**Script(腳本)**

- **X/Y/Z plot** : 方便用來一次生成多張圖對照、測試各參數、模型對出圖成像的影響。  
  如下圖所示，我想知道Euler a 和 DPM++ 2M Karras兩種採樣器，在不同採樣步數時的成像效果。可以這樣設定 :  
  ![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2-2023-08-10-200726.png)
  ![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/xyz_grid-0005-720844771-1-scaled.jpg)

  在此Steps 採樣步數的寫法可以是 :  
  (1) 步數每次加1 : 1-5 = 1,2,3,4,5  
  (2) 不同步長 : 1-20(+2) = 1,3,5,7,9,11,13,15,17,19  
  (3) 規定範圍內出多少個圖 : 1-10\[5\] = 1,3,5,7,10

- **Prompt Matrix (提示詞矩陣)**腳本選擇提示詞矩陣後，在Pompt欄裡輸入 :  
  正常提示詞 | 測試改變提示詞1 | 測試改變提示詞2 | 測試改變提示詞3…..  
  ex. a girl|hat|sunglasses|mask  
  ![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/prompt_matrix-0012-661202695.jpg)    

------

## 2、图生图-txt2img

圖生圖的介面和文生圖大致上都很相似，大部分的參數功能設定也都和文生圖一樣，先簡化來看就只是在文生圖的基礎上多加了一個可以放進一張圖片的窗口，讓Stable Diffusion除了讀取你給的文字描述、參數值資訊外，另外多了參考圖片可做為出圖的生成依據。
![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/img2img01_03.png)

### CLIP反推提示詞  & DeepBooru反推提示詞

- CLIP反推提示詞 : 對圖生圖窗口裡的圖像進行”完整句型”的描述。ex. a girl sitting on a chair
- DeepBooru反推提示詞 : 對圖生圖窗口裡的圖像進行”單詞型”的描述。ex. a girl, sitting, chair
- CLIP反推提示詞能比較清楚描述畫面中物件與物件間的關係，較實用。
- DeepBooru反推提示詞能產出的單詞量相對貧乏不夠仔細，如果想反推出單詞的話推薦改用”Tagger”這個外掛來取代會比較精準一些。
- 第一次使用CLIP和DeepBooru反推提示詞功能時，程式會需要先下載相關模型資料，通常要等待比較久的時間是正常的。這次下載完成，之後再使用時就不用等這麼久了。  
  (PS. 如果運行下載模型過程中不小心中斷/下載失敗，可以直接從網上下載後，放進下圖執行視窗所提示的路徑裡。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/img2img02-e1692169176130.png)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/img2img03-e1692169124725.png)

### 縮放模式(Resize mode)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/img2img04-e1692170858132.png)

- **Just resize (拉伸)**

512\*768的原圖，圖生圖重繪生成768\*768

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/img2img05_02-e1692177589549.png)

- **Crop and resize (裁剪)**

512\*768的原圖，圖生圖重繪生成512\*512

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/img2img06-e1692177625620.png)

- **Resize and fill (填充)** : 適合用在對圖像背景畫面延伸重繪生成，需搭配高一點重繪幅度(Denoising strength)值使用，如果重繪幅度為0或過低時只會對邊緣像素作拉伸。

512\*768的原圖，圖生圖重繪生成768\*768

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/xyz_grid-0001-607774214-scaled.jpg)

- **Just resize(Laten upscale) 直接縮放(放大潛變量)** : 在0或低重繪幅度時和Just resize(拉伸)很像，只是生成的畫面會變模糊。 需要搭配高一點重繪幅度值來使用，它會對拉伸後的圖片內人物/背景所佔的區域，重新添加細節生成新圖。  
  如下圖所示，Denoising為0時僅畫面拉伸+變糊，接著往上提高Denoising，開始針對拉伸後的區域比例重新生成繪制人物和背景。Denoising到了約0.5時畫面變清晰，0.7以上畫面清晰以外，人物和背景的比例又開始恢復成原圖該有的樣子，最終和Resize and fill 在高重繪幅度時一樣，能擴展生成新的背景。

512\*768的原圖，圖生圖重繪生成768\*768

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/xyz_grid-0011-2589505107-scaled.jpg)

### 圖生圖全圖重繪(img2img)

這裡的參數值設定和文生圖裡幾乎一樣，就不再重複介紹，下面我們直接用實際狀況案例來看我們能利用這一區的功能做些什麼。

案例一、這張512\*512女孩人像圖，我想在這張基礎上多變化出差不多主題內容/構圖比例的圖來參考/使用。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/img2img07_02.png)

只設定一個Denoising來看不同變化。(還可再搭配參數裡其它設定/換不同的模型來交錯生成更多不同的新圖出來)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/xyz_grid-0010-1498247453-scaled.jpg)



prompt裡的”a girl”，改成”a man”

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/xyz_grid-0012-476795773-scaled.jpg)



(PS. 這裡生成圖像的尺寸如果按比例設定放大，就等於是之前我們在文生圖裡所使用的Hires.fix(高清修復)是一樣的作用。放大畫面尺寸，多增加更多的像素/噪點，讓SD有更大的空間作畫，也就能把原圖畫面中的每個細節畫得更細緻。)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/img2img08-e1692191583151.png)

------

案例二、同樣是案例一的原圖，我想把這張三次元的真人女孩轉畫成二次元動畫風格的圖。這裡只把checkpoint換成專畫動畫風格的模型。再來看不同重繪幅度下的變化。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/xyz_grid-0006-661202695-scaled.jpg)

在Denoising0.8以上才比較達到我心目中要轉換的風格程度(2D 卡通的畫風)，但是過高的Denoising數值，又會讓新圖整個失去了原圖人物的特徵/穿著不一樣。我如果想要保有原圖人物主要的輪廓特徵(不要這麼卡通圓臉)/衣服穿著不改變，就需要搭配外掛擴充來達到目的。ex. ControlNet的Canny，在SD成像過程中去限制輪廓線範圍…等，又或是找到有訓練這類轉換畫風的Lora輔助模型等….方式。

------

## 3、局部重繪(Inpaint)

  在圖生圖底下的提示詞欄位是要描寫你想要SD生成新圖的內容，而不是描寫原圖。但如果只是要進行重繪放大/高清修復，只用低重繪幅度去稍微增加畫面細節/精緻度，並不想有太大的內容元素/構圖改變時，Prompt欄放原圖的描寫或是全空白皆可。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/img2img10.png)

接著來看一下局部重繪裡一些前面沒有出現過的參數項目:

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/img2img11.png)

- **Mask blur :** 跟Photoshop裡”羽化邊緣”一樣的意思，數值愈大，Mask與原圖交界處羽化範圍愈大。當發現重繪內容與原圖間的過渡不自然時，試著拉大Mask blur數值，但數值過高時也會造成Mask裡可重繪圖的區堆範圍變小(可再把Mask的範圍往外塗抹擴大調整)。
- **Mask mode :**是要重繪Mask區域還是Mask以外的區域。
- **Masked content :** 這裡是要告訴Stable Diffusion，這個塗黑的Mask區域，一開始要根據什麼來逐步去噪重繪生成圖像。是原圖、Mask區域裡像素的顏色混合、還是亂數噪點…？如下圖所示:  
  (PS. 大多時後都是用original或fill為主就行。)  
  (PS. 這裡當我們把Denoising拉到很低近0時，我們就可以很清楚的看到，最初一開始SD在Mask裡加了什麼東西上去，以及後續Denoising拉高過程中它是如何去噪演變畫出圖像來的。)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/img2img12.png)

fill:  
![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/xyz_grid-0033-2283476247-scaled.jpg)

original:

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/xyz_grid-0019-2338501450-scaled.jpg)

laten noise:

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/xyz_grid-0035-1999603094-scaled.jpg)

laten nothing:

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/xyz_grid-0034-3775166615-scaled.jpg)

從上面的比較圖可看出，不管是選擇哪一種的Mask content，Denoising數值過低(還來不及去噪完成)，或是過高(畫面崩壞走鐘)都不適合，實際哪一個數值最剛好，就依照所選的Mask content去決定。選擇一般最常用的original時，Denoising一開始先設0.4~0.6之間大致上相對保險能產出正常的結果來。

- **Inpaint area :** Whole picture(全圖)，是指底下設置圖像長寬尺寸的像素按區域範圍比例分配給Mask區域。如果是Only masked，則是指所有像素集中給Mask區域(分到更密集/更多的噪點，相對可畫出更多細節/畫面更細緻)。但這裡也不是愈密集的噪點就愈好，還是要看整體畫面的協調/自然度，或是你對畫面重點主題的安排。又或者有時密度太過高時，反而會出現奇怪的幻覺/崎形圖，ex. 出現臉中臉….Mask區域不是單加上太陽眼鏡，而是把戴著太陽眼鏡的全臉都給塞進來了。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/img2img13_02.png)

這裡大家再重複加強回憶一下之前文生圖裡提到的Hires. fix. ，當生成512\*512的圖出現人臉崩壞時，勾選打開高清修復放大倍數(假設512\*512→1024\*1024)就能把崩壞的人臉修復成美美的臉，是因為放大解析度同時也按比例增加臉部區域裡的像素密度，SD就有更大的作畫空間去把臉仔細畫好。

不過文生圖裡高清修復放大倍數只能Whole picture 512\*512→Whole picture 1024\*1024去分配這裡的像素密集度，但局部重繪介面下則能有更多的選擇方式(Only masked)搭配操控指定區域的像素密度。

而比起Whole picture, 使用Only masked的另一個好處就是較不易爆顯存，即便最後只是生成一張512\*512的圖，不需去放大整張的解析度，同樣也能增加要修復區域的像素密度達到修復的效果。所以平時在文生圖階段時我很少去用高清修復，文生圖處只需快速算出大量小圖符合構圖主題就行，部分區域崩壞的修正或增添細節精緻度的作業放到圖生圖/局部重繪再進行，能掌握得更精準有效率。
_PS._  
_不同Inapint area的選擇對出圖尺寸大小的影響(當原圖是512\*512):_  
_Whole picture : 新生成圖的長寬會和設定值一樣。ex. 長寬設定512\*256會壓縮變型，設定1024\*1024會產出1024\*1024的大圖。_  
_Only masked : 新生成圖的長寬永遠與原圖尺寸一樣。ex. 長寬設定512\*256不會縮小壓縮變型，設定1024\*1024也不會產出1024\*1024的大圖。 _

- **Only masked padding, pixels :** 這個參數的設定是用來搭配Inpaint area裡的”Only masked”，以進一步調整Mask區域裡的像素密度。數值越高，Masked區裡的像素密度就會變越低。直接看下圖對比就清楚它的作用了 :

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/img2img14.png)

------

## 4、塗鴉(Sketch)

這區的功能就是幫助不會畫圖的手殘黨重新找回自信心的地方(這裡的所有參數項目和img2img完全一樣，就不重複說明了)。直接來看下圖範例 :

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/img2img15.png)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/xyz_grid-0040-1403360187-scaled.jpg)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/img2img16.png)

有空可以把家裡小孩的塗鴉畫丟進來玩玩，見證化腐朽為神奇的過程。

------

## 5、局部重繪塗鴉(Inpaint Sketch)

單看名稱就知道，這裡就是”局部重繪”+”塗鴉”的綜合功能。所參數值的項目和局部重繪都一樣，只是多增加了一個”Mask transparency”，用來控制Mask的透明度，數值愈高Mask愈透明。但注意這個數值不能拉到100，拉到100就代表這個局部重繪的Mask是全透明，SD會顯示錯誤(SD看不到塗抹Mask的地方，它會不知道你要重畫哪裡？)

如下圖，我想在小女孩的衣服上左右各別添加紅色及紫色的蝴蝶結。如果是在局部重繪區，只塗上黑色Mask，其它蝴蝶結顏色以及分別哪個要在右、哪個要在左的設定，單靠Prmopt裡進行文字描述，生成的結果通常不會這麼精準理想，可能一下出現顏色混合(同一個蝴蝶結上有紫色也有紅色)、一下又是各顏色所在位置不是你想要的。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/img2img17.png)

不同Mask transparency數值，最終所產生出的局部重繪效果。拉到90時(Mask快接近全透明)，SD差不多就是直接忽略這裡的Mask區域，同樣的Denoising重繪幅度下，也不會對畫面產生重繪效果。[ 

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/img2img18.png)

------

## 6、局部重繪蒙版上傳(Inpaint Upload)

當在使用Inpaint裡的筆刷+滑鼠來塗畫Mask區的時後通常不是這麼好用/好畫，很常會畫歪或是塗抹的Mask區不夠精確。這時就會想到，如果是用Photoshop的快速選取等工具來製作Mask的話就更有效率&精準多了。於是SD介面裡就又有了這個Inpaint Upload。讓你可以將在外部使用其它軟體製作好的Mask蒙版上傳到SD裡。

這裡唯一要注意的地方就是，在Inpaint裡，要Mask的地方是塗成黑色，但在Inpaint Upload裡則是反過來，黑色是not Mask，白色才是Mask。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/img2img19.png)

Inpaint Masked，同一位女孩換穿不同衣服 : red dress → blue dress![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/xyz_grid-0049-904093939.png)

Inpaint not masked，同樣red dress換不同模特來穿 : a girl in red dress → (a man:1.4) in red dress

![](https://dianxiaoeryu.com/wp-content/uploads/2023/08/xyz_grid-0053-2424772231.jpg)

ControlNet裡，目前針對邊緣檢測進行線條約束的類型分別有Cannny、Lineart、SoftEdge、Scribble以及MLSD。

為了只專注在了解ControlNet不同約束類型的功能/差異，這裡案例的測試都是在文生圖介面下。先不去另考慮如果是在圖生圖介面下，會多了一個不同Denoising重繪幅度的交錯搭配所產生的其它多元效果/影響。單只利用prompt提示詞+ControlNet約束，如何去控制圖像生成的結果。

------

## 7、**ControlNet 控制器**

### Canny（硬边缘）

**Canny 預處理器**

Canny的預處理器有2個:  
**1\. Canny** : 將圖片內容的輪廓轉成黑底白線的線稿圖(預處理圖)。  
使用Canny預處理器檢測邊緣將圖片輪廓轉成線稿時，可利用高、低閾值(Threshold)來調整線稿圖最終輪廓細節保留多寡。 

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/control_02_01.png)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/control_02_02.png)

**2\. Invert(from white bg & black line)** : 如果是自行上傳一般白底黑線的線稿圖，則需用Invert來反轉黑白顏色。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/control_02_17-e1693836059667.png)

------

**Canny 實作案例**

下圖我想讓女孩保留整體在畫面中的構圖比例/人物外輪廓，並且臉型五官維持在同樣位置，但是改變一下髮色及帽子種類。只在Prompt裡寫上我要新更換元素: black hair和straw hat。(這裡沒指定背景，SD還自行腦補了草帽就要搭配海邊的背景~)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/control_02_03_03.png)

如果我想要整張臉都不要受原圖的影響，讓SD自由發揮五官長相以及帽子上不要再出現緞帶。  
於是我把Canny的線稿下載下來進到Photoshop自行加工一下，把面部以及帽子上面有顯示緞帶的線條清除(塗黑)。之後再將圖載入視窗(這時預處理器選擇none就可以了)。  
![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/control_02_05.png)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/control_02_04.png)

PS. 很多時後，如果提供的線稿圖SD大致能猜出是什麼照片內容時，即使Prompt處全空白，它也能自行腦補畫出正常合理的圖出來。如上面這張圖，Prompt處我就沒填上任何文字描述。

------

### Lineart（线条）

**Lineart 預處理器 & 實例\_寫實照片**

Lineart目前預設有的預處理器共有6個(lineart\_animeL、lineart\_anime\_denoise、lineart\_coarse、lineart\_realistic、lineart\_standard以及和Canny一樣也有一個轉黑白稿的Invert)。

每個預處理器對輪廓線特徵提取的效果，以及在此約束下所生成圖片的效果如下所示 :  
(PS. 原圖與ControlNet約束下生成圖片所使用的Checkpoint為同一個真人寫實模型，提示詞皆為空白，以及其它所有的參數設定也都一樣。)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/control_02_06-scaled.jpg)

雖然有些預處理器名稱裡有”anime”，但也不見得真實照片類的就不適合拿它來做特徵的提取。就看你想要的呈現效果不同去選擇，並沒有說用哪個就一定最好。

單以上面這張圖的例子在不同預處理器的測試下 :

- 與Canny相比，使用Lineart提取出來的線條相對更柔和(線條邊緣)，最後的成像效果都將原圖往更”沙龍照(矇矓)”風格偏，特別是使用名字帶有”anime”字樣的預處理器後的成像更明顯。
- 對應原圖想要對所有物件有更相似的”立體度”約束，lineart\_standard做得最好(ex.注意圖片右上角帽子的凹陷程度)

**Lineart 預處理器 & 實例\_卡通圖片**

這邊再拿一張我之前圖庫裡的向量素材圖來測試看看，如果我想要把它轉換成寫實照片風格的話:  
(prompt : pink peggy bank, golden coins)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/control_02_07-scaled.jpg)

最終產出的圖像還無法直接使用。也許自己在Illustrator裡把這張向量素材轉成線稿去蕪存菁保留比較清楚明確/重點的線條、或是換個checkpoint模型多刷幾次圖、也或許再把圖丟到圖生圖的inpaint裡針局部不合理處進行局部重繪…..。

然後背景留白處上下左右延伸調整排版一下方便使用者放上文字文案，就又獲得一張可以上傳圖庫，適合拿來做文宣banner使用的照片素材圖了(keywords概念就是財富、儲蓄、理財….)~

------

### SoftEdge（柔边缘）

功能與約束效果方式都和Canny與Lineart一樣，SoftEdge這裡就不重複一樣的生成圖片對比，只列出每個預處理器所提取的效果給大家參考:

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/control_02_08-e1693816621976.jpg)

------

### Scribble（涂鸦）

**Scribble 預處理器**

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/control_02_09.jpg)
**Scribble 實作案例**

scribble\_hed與scribble\_pidinet預處理器提取出來的線條極其極簡抽像，但加上搭配Scribble的模型後，SD就是能夠天馬行空的自行腦補出合理的圖像來:

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/control_02_10.jpg)

(視窗載入scribble的預處理圖，Canny、Lineart、SoftEdge模式下的預處理器都選none)  
![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/control_02_12-e1693819070522.png)
![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/control_02_11.jpg)
那麼反過來，把Canny、Lineart、SofeEdge所提取出相對scribble明確精細(至少人眼看得懂)的預處理圖讓Scribble的模型來讀取使用的話：

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/control_02_13.jpg)
結果來看，Scribble模型對線條的腦補能力(包容性)最強大，如果今天我自己畫一張極度手殘簡約的線稿圖，搭配Scribble的模型下，SD一定也能自行腦補畫出像樣的成果來吧~

那就Photoshop + 滑鼠來畫張極簡線稿來試試這幾個ControlNet模型會如何讀取特徵讓SD生成圖像:  
(PS. prmopt空白)  

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/control_02_14.jpg)

------

### MLSD（直线）

MLSD專門/只能用來提取畫面中”直線”的線條，特別適合用在室內設計與建物外觀線條輪廓的提取。預處理器參數中可透過Value Threshold以及Distance Threshold的數值來調整畫面中線條訊息的多寡。

- **Value Threshold** : 數值在0.01~2之間，值愈大，檢測到的線條愈少，丟失掉愈多的直線細節訊息。
- **Distance Threshold** : 數值在0.01~20之間，值愈大，物體越遠處被提取的線條越少，更專注於近處的線條訊息。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/control_02_15.png)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/value.gif)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/distance.gif)

利用MLSD提取原圖室內牆面、天花板、桌椅傢俱等具備直線特徵的線條固定住室內透視、傢具配置位置/外觀輪廓大小，之後在prompt提示詞裡寫上想要改變的風格，morden style、industrial style、white wall….等。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/control_02_16-scaled.jpg)

------

ControlNet的Depth可以提取出畫面中人物/物體的前後關系/前景後景的分別，而Normal(法線)則可以紀錄出畫面中物體的凹凸面訊息。透過這兩種ControlNet約束類型，就可以幫助我們對成像的空間深度關係與物體的凹凸立體感/亮面暗面的光影效果進行約束控制。

------

### Depth（深度）

Depth各預處理器效果如下圖，所產生出來的預處理圖，畫面愈近處愈白，畫面愈遠處則顏色漸深/至全黑。

(下圖提示詞 : street view in Korea at night, rainny day)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/controlnet_depth_01_02.jpg)



在depth\_leres 與 depth\_leres++ 預處理器下，可透過Remove Near% 與 Remove Background%調整，對預處理圖的深度效果進行增減。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/controlnet_depth_02-e1694277050836.png)

Remove Near% : 數值從0~100，由最近處(白色)往最遠處開始逐漸將畫面中不同深度的人/物去除深度，直至全白(平面沒有深度)為止。

Remove Background% : 數值從0~100，由最遠處(黑色)往近處開始逐漸將畫面中不同深度的人/物去除深度，直至全黑(平面沒有深度)為止。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/controlnet_depth_03-scaled.jpg)

------

Depth只能提供深度的訊息，在生成圖片時無法很好的掌控物體的內容與細節，成像效果通常再加上prompt描述或是搭配其它ContronlNet的特徵約束一起使用會比較理想。

Depth + (提示詞空白)。SD沒有自行腦補出每人手裡拿的是手機，有些該畫人臉的地方也被不知何物的物體所取代~

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/controlnet_depth_06-scaled-e1694277998102.jpg)

Depth + (提示詞:crowd of people taking piture with smart phone in the party at night)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/controlnet_depth_07-scaled-e1694278157801.jpg)

------

雖然Depth無法掌控物體的內容與細節，但大家可以比對一下下面2種ControlNet約束成像方式(Depth與Lineart)的差別。最後畫面都是同樣的主題構圖，但經過Depth約束處理後的成像看起來會更立體/生動(感覺得出畫面的遠近深度)。

而從Lineart的線條約束中，常理透過線條輪廓所畫出的人臉比例大小，人類能理解腦補出畫面遠近的深度感。但對SD來說只有線條特徵並無法有效理解畫面的深淺前後關係，因此所畫出來的圖也就會少了該有的透視感，畫面整體看起來會很平面。

Depth與Lineart對比 ，(提示詞都是:crowd of people taking piture with smart phone in the party at night)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/controlnet_depth_08.jpg)

(PS.上圖畫面中各種人手畸形的部分就先忽略它吧，對AI繪圖來說，畫手本來就是弱項了，畫面中又出現這麼多小面積要畫手的構圖，要整個畫面沒有bug完全畫得正常，不管怎麼調整也實在是為難了現在的SD與自己。這種時後就會很有感，同樣的主題畫面，相機攝影完勝AI繪圖~ 這張圖相機按下快門就能完成的事，我拿SD狂刷圖+細節一個個想辦法修正可能要花更多的時間吧~ 有些圖，用拍照的比較省事，有些圖用AI畫比較快~)

------

### Normal（法线）

有學過3D的人對Normal map(法線貼圖)一定不陌生，它是一種模擬凹凸處光照效果的技術。經過ControlNet Normal預處理器提取出原圖畫面中物體的凹凸面/光影亮面暗面方向訊息後，就能用來約束新生成圖像中物體的立體度與光影方向效果。

Normal的預處理器有2個，一個是Normal\_bae，另一個是Normal\_midas。目前為止，我都只有用Normal\_bae，測試過許多圖用Normal\_midas讀取出來的效果與後續生成的圖片都是不太理想與成像會有許多奇怪的紋理。

(提示詞 : black hair, white dress)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/controlnet_depth_09-scaled-e1694282047360.jpg)

另外當我們在使用OpenPose，遇到特定姿勢如果一直無法正確提取出來時，Normal圖也能很好彌補這部份的缺失。

如下圖左邊男人坐在椅子上翹腳的姿勢，由於OpenPose所提取的姿勢骨架圖是平面的沒有深度，對於這種畫面角度需要考慮到深度效果的姿勢時，很大機率就會無法順利生成。但如果改用Normal則可以比較容易正確還原出原圖人物的動作姿勢。

(提示詞 : a man and a woman sitting on chair talking to each other)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/controlnet_depth_10.jpg)

不過Normal的預處理圖又會控制住畫面中過多姿勢以外我不需要的細節訊息特徵(邊桌、椅子造型樣式…等)，這時如果是本身有使用3D軟體的人，當SD與ControlNet一直無法調整出理想效果時，也許就可以直接用3D軟體產出一張去除不必要細節的Normal圖來讓SD在限定的人物動作以外其它細節都自由發揮變化。

------

### OpenPose 預處理器 

OpenPose目前的預處理器有6個 : openpose、openpose\_full、openpose\_hand、openpose\_face、openpose\_face\_only、dw\_openpose\_full。

首先一開始，我們先拿最簡單辨識的正面人物擺拍圖來測試。(提示詞都是空白)

**openpose : 只提取人物大致全身骨架位置**由於openpose只提取出人物全身骨架位置，缺少手部關節訊息，最後成像有可能如下圖人物的左手，腰側並沒有口袋，但整個手掌就不見了(沒畫到)。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/openpose01.jpg)

**openpose\_hand : 提取人物大致全身骨架位置 + 手部關節**

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/openpose04.jpg)

**openpose\_face : 提取人物大致全身骨架位置 + 臉部輪廓/五官位置**雖然也沒有提取出手部關節，但這次刷圖剛好SD左手腦補的很自然合理

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/openpose05.jpg)
**openpose\_face\_only : 只提取臉部輪廓/五官位置**

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/openpose06.jpg)

**openpose\_full : 提取人物大致全身骨架位置 + 手部關節 + 臉部輪廓/五官位置**

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/openpose02.jpg)

**dw\_openpose\_full : 提取人物大致全身骨架位置+ 手部關節 + 臉部輪廓/五官位置**和openpose\_full一樣，骨架、臉與手部關節全提取，但這張圖dw\_openpose\_full把右手只露出手一小部分手背的地方也偵測出來了。目前大多數的人像全身圖測試下來，都是以dw\_openpose\_full的靈敏度(準確度)最好。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/openpose03.jpg)

上例這張原始圖人物的動作姿勢還比較簡單好辨別，經過各預處理器產出的圖差別不太大(都能產出正常合理的圖)。但後面其它人物動作姿勢比較複雜時(要考慮深度或是肢體有重疊交錯)就可以明顯看出各預處理器間的差距。

------

接下來我們來測試一下難一點的動作姿勢，下面這張原圖人物左右腳前後交錯。(提示詞都是空白)

從下圖的預處理圖可以看出，openpose\_full沒能提取到右手關節，而dw\_openpose\_full則全部動作姿勢特徵都順利提取到(身體骨架、兩手關節、臉部)。

但就像之前在depth深度約束那篇文章裡有提過，openpose的人物骨架圖訊息是平面的，對於左右腳前後交錯的空間位置，在最後的成像圖上並無法完全還原出原圖的效果(右腳雖交錯在後，但是稍微往外靠而不是整個縮在後方)。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/openpose07.jpg)

------

可能上面這張原圖的人物動作姿勢深度的差別不明顯，那麼我們再來測試一張更明顯的例子，來看看openpose的預處理器會不會都翻車。

(這張圖需要給點提示詞 : a girl taking selfies with smart phone)

和上一個例子一樣，dw\_openpose\_full提取的效果比openpose\_full好(雖然dw\_openpose\_full也沒把手關節完全提取正確，但至少兩手都有辨識到)。不過兩張最後的成像除了手的問題以外，人物的頭身比例和前後深度感仍然很詭異/不自然。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/openpose08.jpg)

即然覺得深度透視感出了問題，那我們就來試試再添加一個depth深度約束來輔助成像。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/openpose09.jpg)

加了depth深度約束後，畫面整體的感覺又更自然合理了些。或是其實以這張圖的人物動作來說，要還原圖中人物的動作姿勢，直接使用一個depth控制約束就行。openpose並不實用。

------

最後我們再來看看不同類型的人物圖透過openpose提取特徵的效果。

畫面中多人合照圖 : (提示詞 : man and women looking at a tablet cheerfully)。這張SD很自然地自動腦補骨架最高的畫成man，其他骨架畫成women。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/openpose10.jpg)
雖然dw\_openpose\_full最後的成像有點小失誤(紅框中男女兩人手臂交疊處前後順序與原圖稍有不同)，不過整體沒太大的問題。而openpose\_full在多人同時出現在畫面中又彼此靠都得很近的情況下則丟失掉更多的動作姿勢訊息。

------

從上一個多人合照案例中，我們發現，畫面中人物肢體交疊處似乎特別容易辨別失誤，那麼我們再來試一張最後讓所有預處理器都翻車的照片 :

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/openpose11.jpg)
到了這張圖很意外地，前面一直表現勝過openpose\_full的dw\_openpose\_full反而翻車得更嚴重，這兩張預處理圖都無法直接使用。

不過難道我們就只能受限於現有預處理器效果的限制，無法不論是在任何動作姿勢的狀況下，也能生成一張完全符合我們需求的人物骨架圖嗎？

當然不是~ 當Openpose裡所有的預處理器都無法達到我們需求時，我們還可以透過各式調整骨架圖的外掛擴充來修正預處理器判斷/提取失敗的部分，又或者自行生成骨架圖給OpenPose的Model讀取生成圖像。

**OpenPose 骨架圖修改/調整外掛工具**

從extensions頁面下搜尋”openpose”，可以看到目前有4個相關的外掛擴充可用。關於如何安裝外掛擴充，請參考之前的文章 :

[→ AI繪圖-Stable Diffusion 007- 外掛擴充 Extensions 的安裝、更新、移除與備份![](https://dianxiaoeryu.com/ai%e7%b9%aa%e5%9c%96-stable-diffusion-007-%e5%a4%96%e6%8e%9b%e6%93%b4%e5%85%85-extensions-%e7%9a%84%e5%ae%89%e8%a3%9d%e3%80%81%e6%9b%b4%e6%96%b0%e3%80%81%e7%a7%bb%e9%99%a4%e8%88%87%e5%82%99%e4%bb%bd/)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/openpose12.png)

------

這邊我們先安裝第一個”sd-webui-openpose-editor-editing”來測試。安裝完成重啟SD後，在Openpose的預處理圖視窗右下角處點擊”Edit”就會進到針對預處理圖修改/調整的面頁 :

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/openpose13.png)

這個編輯畫面使用上就挺直覺的，右邊畫布區滑動滑鼠滾輪放大縮小、空白鍵+滑鼠左鍵移動畫布。左下方可以自行增減人物群組，這邊就和Photoshop的圖層操作使用上一樣。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/openpose14-e1694498050553.png)

唯一注意的就是要針對整個部位群組(如下圖的右手)做放大縮小旋轉移動時，在下拉選單沒展開的狀態下，直接點選手部位置就會出現變形操作的外框。但如果是在下拉選單展開的狀態下的話，就要用拖曳框選出手部所有的關節才行。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/openpose15.png)

如果是要對群組內的個別節點做調整修改時(如下圖調整右手關節位置)，就要先將群組選單展開，之後再點選各個節點操作。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/openpose16-e1694498738942.png)

------

費了些時間，總算把父女倆人的骨架與手部關節大致完成。接著將骨架圖傳送回ControlNet。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/openpose17_02.png)

首先，只單用一張OpenPose來約束成像。(提示詞 : father holding little girl，畫布改成原圖長寬一樣以外。其它所有參數設定都直接用預設)

骨架圖還原了”平面”的動作姿勢，但人物肢體交錯前後位置則無法掌控。~ 小女孩左手要蓋住右手，男人的右手要在小女孩右腳後方拖住屁股 ~

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/openpose18.jpg)



也許單靠平面骨架圖就有機率剛好可以刷出和原圖一樣的前後位置(不過我刷了幾十張才出現過1、2張@@)，但如果凡是只靠運氣刷圖，就不是我們多花時間學SD的目的。

因此，我們再來實驗搭配其它約束類型來試看看。

多增加一個depth深度約束，單從depth預處理圖來看，至少小女孩的右腳應該要是在男人右手的前面，但不管如何試(即便把depth約束的權重拉高+depth的Control Mode 用ControlNet更重要)，都還是一樣，刷不出原圖該有的前後位置。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/openpose19-scaled.jpg)

即然depth深度約束行不通，那麼再來試看看搭配normal，直覺上normal預處理圖的效果對這種前後貼很近的位置關係應該會比depth更精準表現。但最後出圖的結果只把小女孩左手蓋住右手這部分修正了，但男人的右手還是固執地畫在小女孩右腳的前面。

這裡實在讓人難以理解，明明預處理圖都這麼明確指示小女孩的右腳更凸出是整個蓋過男人的右手(即便把normal約束的權重拉高+normal的Control Mode 用ControlNet更重要)，為何你SD一直要把右手往前畫~這種抱法不符合人體工學好嗎，右手應該要拖在小女孩的屁股上才抱得穩呀~~~

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/openpose20-scaled.jpg)

depth不行，normal也不行，最後我再試一個，特別針對右手要放在小女孩後面這部分加上線條約束(Lineart)。

搭配Lineart(Lineart約束的權重預設的1 + Control Mode 用 Balanced)，終於差不多有一半的機率會正確畫出男人右手在小女孩右腳後面，同時小女孩的左手也蓋在右手上了。

並且，由於這裡的Lineart預處理圖我是另外有修改把非動作姿勢以外的線條給清除掉(為了不讓人物長相太過與原圖相像)，這時盡量Lineart約束的權重別設太高或是Lineart的Control Mode也不要設ControlNet更重要，因為這樣有很大的機率會莫明奇妙畫出第三、第四顆人頭畸形的畫面~ 因為你讓SD過度偏重Lineart預處理圖，但畫面中又太多地方沒有給出線條的指示，SD只好發揮它天馬行空的專長，畫些奇奇怪怪的畸形圖給你了。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/openpose21.jpg)

最後的最後，我想要出圖有正確動作姿勢的機率再拉高一點，一次開3個ControlNet類型來約束成像看看。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/openpose22-scaled.jpg)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/openpose23-scaled.jpg)

三個ControlNet一起使用的情況下，每次刷出來的圖的動作姿勢幾乎就是我要的了，不過不知為何，成像的圖怎麼愈來愈走復古舊照片的調調了？看來這裡又是要再後續處理的問題了……

為了這動作，刷了一下午的圖，內心感慨，給我一台相機吧，有時在那刷圖猜測久了也是挺累人的@@~ 不如走出去拍拍真實的照片吧 ~ 拍下想要的照片之餘也順便調劑身心放鬆心情 ~

(PS. 用SD刷圖，特別是在一直有使用ContrlNet的情況下，用久了有時覺得刷出來的圖怪怪的(如下圖像是某個參數異常調得太高或太低)，可是明明不是參數沒調對，反而比較像是SD透逗時，就把SD關閉重啟吧~ 很多時後原本一直困擾的問題就通通不見了~)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/00150-2970581397.png)

------

至於另外3個修改調整骨架圖的外掛擴充，我也只使用過3D Openpose Editor tab。另2個大家有覺得比較好上手使用也可試看看，我是前2個(“sd-webui-openpose-editor-editing” 和 3D Openpose Editor tab)就覺夠用了(也比較方便操作)。

而3D Openpose Editor tab在操作介面上對沒使用過3D軟體的人可能會覺得不太好操作掌控，不過因為它有更多的參數可調整，可以更精細調整動作姿勢。有興趣的人可以先到它的線上網頁版試操作看看，覺得有必要(好用)，再安裝到SD上。

[**→ https://zhuyu1997.github.io/open-pose-editor/**![](https://zhuyu1997.github.io/open-pose-editor/)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2-2023-09-12-175828-e1694513214812.png)

------

### Segmentation（语义分割）

ControlNet的Seg預處理器目前有3種，各別預處理圖的效果與成像實例如下圖所示。目前測試下來，絕大多數的情況，seg\_ofade20k的效果都比較理想，辨別的準度相較較高。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/seg01-scaled-e1694594176306.jpg)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/seg03-e1694594291415.jpg)

**Segmentation 的應用**

Segmentation的預處理圖讓我想到之前圖生圖裡的Sketch塗鴉功能。只是在用Sketch塗鴉功能時，在提示詞裡多少還是要將畫面的內容物進行文字的描述，告訴SD畫面中我塗鴉的地方各別大約需要些什麼內容物。但如果應用上Segmentation，語義分割事先就將每個不同的顏色定義出特定的物品類型了，我們可以不用再多做文字描述SD就知道該畫些什麼東西出現在畫面中。而且很多時後，當畫面內容物愈複雜時，SD未必就這麼看得懂你所有的文字描述，但語義分割後的區塊則就很明確有效地限制住SD該畫些什麼類型的物品出來。

我們可以事先把一張看起來符合自己大致理想的畫面構圖進行語義分割，之後再丟進Photoshop裡自行塗鴉調整/增減畫面中的色塊(內容物) :

如下圖，原圖中左邊的草地禿了一塊，我想把它補上，另外左後方再加間小木屋。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/seg04.jpg)

又或者可以自行查看 [**Segmentation Color Code**![](https://docs.google.com/spreadsheets/d/1se8YEtb2detS7OuPE86fXGyD269pMycAWe2mtKUj2W8/edit#gid=0) ，找出每種物品類型對應的顏色來畫張色塊塗鴉稿，再讓SD來生圖。

從Color Code裡找到Lake的色碼是”#0ABED4″，同樣上面這張風景圖我就再加上個門前有湖、門口出入的道路改道繞一下…..

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/seg05.jpg)

------

另外一個搭配應用就是，前面文章我們提到過Depth深度約束能夠表達畫面物品前後深度關係，但並無法紀錄下不同深度下的內容物品分別是什麼，而現在Seg則是可以標註畫面區塊的內容物類別，可是它是平面的，缺少深度的訊息。

那麼在使用SD生成圖像必要時我們就可以把這兩者互相配合使用，就像前一篇OpenPose動作姿勢約束裡的案例一樣，有些需要考慮深度前後位置關係的動作光靠骨架圖無法直接產出理想的畫面時，我們就再加一個Depth深度約束來一起使用。

ControlNet的某些約束類型很多時後單一使用並不這麼好用/或是無法有效解決問題，總是會覺得還不夠精準明確/有點廢。但其實就是要多花些時間/耐心，想一下把各種組合搭配試看看/截長補短，同時也可以結合原本所學過的其它軟體應用一起實驗。最後會發現很多功能再廢，經過思考配合，在某些特定時後它也是能發揮出大作用的~

ControlNet 官方的其它特殊效果主要有 Shuffle、Tile、Inpaint、IP2P、Reference，其中Tile和Inpaint會花比較多篇幅就之後另外再介紹，這篇就先來看Shuffle & IP2P & Reference這三種ControlNet成像效果。

------

### Shuffle（洗牌）

Shuffle預處理器會將原本的圖片畫面打散重新洗牌(而且每都是隨機亂數提取)，所以同一張原圖每次提取出的預處理圖被打散的樣式會都不一樣。但重點就是提取出原圖的顏色/風格，進而去影響新生成圖像的整體畫風/色調。

先用文生圖簡單生成一張真人照片

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/others01.png)

加入ControlNet Shuffle。這裡雖然所有設定不變，連Seed值也固定住，不過加入ControlNet Shuffle的影響後，風格移植了，但同時無法固定住照片原本的構圖。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/others02_02.jpg)

前面構圖改變太多的問題，雖然也可透過把Control Weight權重調低的方式改善，但又怕權重愈調低了，風格移植的效果愈不明顯。那不如不要去改變權重，只要再加入第二個ControlNet的Canny線條約束來限制住大致的輪廓外觀就好。

再多加一個Canny的線條約束，如此，算是有把清明上河圖的風格/色調移植到新圖上了吧？

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/others03.png)

Shuffle的權重預設的1就差不多很剛好，再低風格效果不明顯，再高又會畫面崩壞 :

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/xyz_grid-0001-661202695-scaled.jpg)

而前面說的透過把Control Weight權重調低的方式來改善畫面構圖不要被改變太多，但實測再低的權重也是無法很準確有效地定住原構圖的細節，不如線條約束實用 :

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/xyz_grid-0000-661202695-scaled.jpg)

------

再來一張套上水墨風格的成像。到這裡一直都是用真人風格的Checkpoint模型，人臉的部分看起來就只是轉黑白色調而已，沒有水墨畫風的質感。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/others02_04.jpg)

如果換成專畫卡通人物的Checkpoint模型(AnythingV3)，這樣好像風格移植的效果更明顯些，不是只有顏色移植。所以，在做風格轉換時也需要注意一下所使用的Checkpoint模型與最終想要成像的風格效果搭不搭配。ControlNet提取風格的原圖如果是卡通動畫、二次元、或是像這張水墨風等，想要不是只有顏色/色調的移植，而是要連畫風的質感都時展現出來時，那麼就要記得避開使用專畫三次元真人寫實風格的Checkpoint模型。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/others02_05.jpg)

------

### IP2P（特效）

IP2P沒有預處理器，它的效果就是可以把一張原圖加上提示詞描述(ex. “make it on fire”)，來轉換場景狀態，例如讓場景起火、下雪變冬天…..等。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/others02_06_2-e1694683146205.jpg)

------

這邊在提示詞的部分，官網上介紹註明 : Also, it seems that instructions like “make it into X” works better than “make Y into X”

從下面的人像圖所下的提示詞就可看出差別。照常理，我會在提示詞裡寫上”make **her** on fire”或是”make **her** snow”。但可以明顯發現，這樣原圖的人物會有所改動，幾乎是變成另外一個人。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/others02_07.jpg)

但如果照官網指示，不管是針對場景還是人物，提示詞的開頭都統一寫”make **it** ……”，會比較理想。如下圖，原圖人物的長相特徵有保留住的情況下做到了場景狀態轉換。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/others02_08.jpg)

------

### Reference（参考）

Reference的功用是用來生成與原圖風格內容類似的圖。使用Reference目前有3種預處理器，但並不需要有對應的Control Model。

在官網的示範中(下圖的圖片來源 : [https://github.com/Mikubill/sd-webui-controlnet![](https://github.com/Mikubill/sd-webui-controlnet))，看起來似乎很好用，好像用一張參照圖，就可以去生成參照圖片中人物/動物的各種變化圖來(固定住人物/動物的特徵去生成變化不同姿態/表情)。
(Prompt “a dog running on grassland, best quality, …”)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/ref-e1694692449466.png)

如此一來，就可以用一張圖去生成訓練LoRa模型時要用到的多張同個人物角色，但不同臉部表情/角度的圖片，或是說，一張參考照片就能搞定固定住人物特徵實現人設統一，那是不是就不需要LoRa了？

看上面狗在草地上奔跑的例子效果很好，但如果放在人物身上時呢 ？

下面圖例讓原圖中戴墨鏡，沒有表情的女孩，加上微笑。在3種Reference預處理器下的效果 :

提示詞 : a girl wearing sunglasses, smile

最後面放了一張關閉ControlNet Reference效果，只有提示詞產出的圖來對比。感覺Reference差不多就是固定住髮型、和在畫面中大致的姿勢構圖。至於你說人的五官長相有沒有像，同一個模型的這些人臉看久了我實在有些臉盲了@@

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/others02_11-scaled.jpg)

Reference 控制下連刷10張圖 : 有的髮型固定住了，有的衣服特徵固定住。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/grid-0022_02.jpg)

我用動物測試時真的都挺像的，可以連刷10張奔跑姿勢都沒問題，看起來10張都是同一隻狗沒錯。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/others02_13-e1694695142448.png)

但真人的五官長相我實在刷不出這樣都固定住的效果。而且像上面載太陽眼鏡女孩的例子，如果提示詞裡沒去交代有戴太陽眼鏡的話，那就只會生成一個笑臉女生，差不多的頭髮長度，上半身正面照。如此的話，那我用不用Reference好像差別意義不太大？稍微可輔助固定特徵，但很大呈度上都是靠提示詞細描述和所使用的Checkpoint模型？

最後不死心，再拿張長相比較有辨識度的人像來測看看，加上Reference，看看SD會參照還原畫出怎樣類似的特徵來。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/badofan.jpg)

提示詞只有”a man, smile”。看得出來，Reference抓住灰白髮色+自然捲特徵(這個是我提示詞沒說明，很明確是Reference的功勞)。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/grid-0027.jpg)

總之，目前為止，Referenc我還沒能玩出真的像網上有些標題說的這麼厲害，可以取代LoRa，人設統一之類的地步(是朝這個方向沒錯，只是離穩定品質還有很大的差距)。有時訓練模型的樣本數不夠時或許這個Reference現在可以幫忙加減多提供一些變化的樣本圖，但至於其它，還是先不要太過期待Reference的效果，等它之後再進化/優化的版本/演算效果出現時再說吧~

------

另外，補充一下前面沒說到Reference預處理器下有個”Style Fidelity (only for “Balanced” mode) “的參數可調整，它是用來控制Reference風格保真度的高低(只在Control Mode是Balanced模式下有效)。

實測圖如下，我是覺得一般都用預設的0.5就可以了，拉低少了相似度，拉太高生成的圖又很容易會畫面崩壞。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/others02_10.png)
![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/others02_14.jpg)

看起來大致上就是Reference\_only和Reference\_adain+attn，保真度約預設的0.5剛好，而Reference\_adain有需要時可以稍微往1的方向拉高，也不至於出現畫面崩壞。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/others02_15.jpg)

------

### Inpaint（局部重绘）

首先，在文生圖底下，我們先來看三種預處理器處理過的預處理圖與最終成像效果的差異 : inpaint\_only、inpaint\_global\_harmonias、inpaint\_only+lama

提示詞 : a girl, red hat, smile。但ControlNet的Inpaint只塗黑臉部。Control Mode : 提示詞更重要。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/others04_02.jpg)

inpaint\_only、inpaint\_global\_harmonias的預處理器，會把塗黑處轉成半透明，但還保留原臉部外觀。而inpaint\_only+lama把塗黑處轉成半透明同時，也把原本臉部的內容去除掉了。而最終成像效果則是 :

- inpaint\_only : 只針對塗黑範圍重繪，提示詞有提到 “red hat” 和 “smile”，但這裡只會修改臉部表情，不影響帽子。
- inpaint\_global\_harmonias : 除了塗黑範圍，會對整張圖進行重繪，如案例在提示詞有”red hat” ，雖然帽子並不在塗黑範圍裡，但最後仍然會被提示詞影響，重畫成紅色帽子。
- inpaint\_only+lama : 這個案例的成像效果和inpaint\_only一樣，但它主要的強項功能不在此。而是能夠將背景無中生有延伸，這個後面我們會再實作測試。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/others07_02.jpg)

------

上面的例子可以把臉部表情換成我們要的笑臉，但人臉的五官長相也是換成了另一個人，看不出是同一個女孩。如果這裡把ControlNet的Reference(參照原圖提取出人物的某些外貌特徵)搭配一起使用看看效果如何。能不能畫出同一個女孩的笑臉~

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/others08-scaled.jpg)

這樣並排一起看，效果就很明顯，加了Reference的笑臉與原圖女孩最像同一個人(雖然微笑的幅度變小)。前一篇單一測試Reference時還覺得目前Reference沒好用到可以取代LoRa、人設統一的地步，但這樣一試，其實搭配著其它ControlNet時，也是能有不錯的應用效果。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/others09-scaled.jpg)

**Inpaint\_only\_lama的背景延伸**

利用inpaint\_only\_lama的預處理器也能快速實現自動無中生有延伸填滿背景。提示詞基本上試過全空白也行，SD會先自行辨識現有背景內容去想像生成，但如果覺得最終成像不理想延伸出的背景不夠貼合自然的話，這時才再稍微提示補充一下畫面中目前背景的地點即可。

其它主要設定要注意的地方就是，Control Mode 選 ControlNet更重要，Resize Mode 選 Resize and fill。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/others10-scaled.jpg)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/background_gif01_02.gif)

再來測試豎向延伸 :

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/background_gif02.gif)

------

如果畫面中需要填補延伸的部分都是背景，沒有切到明顯主體的話，基本上inpaint\_only\_lama處理的效果都不錯。不過還是有許多照片就無法填充延伸得這麼理想。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/background_gif03.gif)
![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/background_gif04.gif)

I**npaint\_only\_lama的背景延伸功能在圖生圖底下效果比較好~？**

當初在看網上教學介紹inpaint\_only\_lama做背景延伸時就很納悶，為什麼大家都一定要在圖生圖底下去用Inpaint，甚至很多有提到，在圖生圖底下所延伸出的背景效果畫得比較好。但我比對測試，怎樣都試不出很明確的結論說，圖生圖下生成的背景延伸圖就有比較好，兩邊都差不多，有些圖有些時後試到哪邊比較適合的機會都有都一樣。

我們先來看在圖生圖底下使用inpaint\_only\_lama做背景延伸時所需要做的設定 :

ControlNet裡Inpaint的設定就和前面文生圖時一樣。其它在圖生圖介面中，只有2個參數我們來分別測試看看差別(下圖紅框處)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/others11-scaled.jpg)

- Reize mode : 除了ControlNet裡的Resize mode，這裡也有一個Resize mode要設定。這裡勾選哪個都可以使用，只是對最後成像效果各有些許不同變化。
- Denoising strength : 要對背景進行填滿延伸，這裡的重繪幅度至少都要設定在0.7以上結果才比較正常理想。

下面是測試Resize mode和Denoising strength不同參數下的對比圖(這裡Seed值我都是固定住用同一個，提示詞全空白) :

Resize mode : Just resize

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/xyz_grid-0000-3799072724_01-scaled.jpg)
Resize mode : Crop and resize

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/xyz_grid-0000-3799072724_02-scaled.jpg)
Resize mode : Resize and fill

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/xyz_grid-0000-3799072724_03-scaled.jpg)
Resize mode : Just resize(laten upscale)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/xyz_grid-0000-3799072724_04-scaled.jpg)

------

以上面這張多人合照的豎向延伸，用文生圖還是圖生圖底下去進行背景延伸的成果，基本上沒什麼差別，最多就是圖生圖底下你同一個Seed值下可以多刷幾張不同Denoising值(0.7~1之間)的成像做挑選，但要總結說在圖生圖底下所延伸出的背景效果畫得比較好這點感覺就比較不是這麼絕對了吧~

下面再拿個橫向延伸的背景圖測試看看。

同樣的Checkpoint模型、Seed值、提示詞 : south asian street background。

圖生圖底下 : Denoising 0.7~1之間產4張圖來選擇。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/xyz_grid-0000-3074491267_5_03-scaled.jpg)

文生圖底下 : 刷4張圖。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/others12-scaled.jpg)

兩邊成果都有可用的圖，且這次文生圖介面下的產出整體我還比較滿意。雖然沒差多少時間，但圖生圖的介面就是要多幾個步驟(多一個要拖放原圖的視窗、多一個Resize mode要勾選、還要再想一下決定Denoising值要多高~) 。我很懶，同樣的結果能省事的地方就別多費力吧

------

## 8、Tile（高清修复）

的原理，它的作用/約束方式就是 :

**_把畫面中出現的物體辨識出來是什麼，然後將它鎖定住(它會忽略掉原圖中的細節，只記憶控制物體所佔的區塊範圍/顏色資訊)。_**

至於新圖像所生成的畫面/物體有多少細節內容，則是靠你給的提示詞、畫布尺寸大小、以及再加上模型本身的品質。最終就在鎖定住物體的區塊範圍內去畫出/生成新的圖片出來。

所以，那些所謂tile能增加畫面細節的說法就不是這麼準確，少了前因後果的邏輯關係。能讓畫面/物體的細節變多/畫得很細緻靠的不是tile，最直接主要關連的還是”畫面尺寸”大小(可以說影響最重要，之面文章講文生圖的高清修復、圖生圖的放大重繪時也一直有在強調~)、同尺寸下把提示詞寫得很細很細(cfg值拉高)，或是再加上你所使用的Checkpoint模型本來的品質所影響。

能夠做到高清修復也是因為生圖過程中，一開始的階段先應用tile鎖定住所辨識出原圖裡的物體後，在圖生圖裡開4k、8k以上放大的畫布重繪時，就算Denoising重繪幅度拉很高，也能達到有了高重繪幅度去細重畫每個分割區塊裡的內容物，同時又不會畫出奇幻的畸型圖來。

**實測有無Tile模型效果**

#### **範例一 、模糊超小尺寸的圖，重繪放大**

原圖是一張64\*64模糊不清的小圖(官網上的示範原圖)，要放大成512×512尺寸，然後畫面不模糊，可以看清物體該有的細節~

提示詞 : dog on grassland，Denoising重繪幅度 : 1

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tile03.jpg)

tile辨識出這張模糊的圖是隻狗，綠色的區塊是草地我想應該也是大致能辨識出來的，於是鎖定住畫面中的物體是”狗”、”草地”，以及各自構圖所佔比例和顏色訊息。之後提示詞也和tile辨識的內容一致，沒有懸念地，最後生成出一張乍看很像一樣的圖，但狗已經不是同一隻、草地也不是同一片草地了。

同樣的原圖，官方示範畫出的狗或是我再換別的Checkpoint模型、採樣法…..等時，都是會畫出長得或多或少不太一樣的一隻狗。而畫面中所呈現出的細節(狗毛畫得的細膩度…)，則是取決於現在512×512畫布下，加上我給的提示詞和所使用的Checkpoint模型品質本來就能畫出的細節程度。tile跟畫出更多細節這件事本身沒太大關係，它的功能就是”辨識鎖定物體”、”控制物體構圖所佔比例和顏色訊息”

另外這裡看一下tile三種預處理器的差別，可能和所使用的Checkpoint模型或採樣法不同時對色調的影響程度會有差，但大致上就是如上圖所示 :

- **tile\_resample** : 對成像色彩飽和度會差很多，主體的狗本身倒是還ok，但草地的顏色實在差太多了。
- **tile\_colorfix** : 有明顯改善了草地的顏色，但是狗毛似乎開始被草地的綠色給汙染了(反而resample的狗毛顏色比較沒被汙染)，以及畫面變得有點開始發虛模糊的傾向。
- **tile\_colorfix+sharp** : 雖然本意是想把圖片做顏色修正，同時把畫面銳化不要看起來變得模糊。可惜實際使用後覺得效果並不好，它只是把顏色的對比拉高而已，並沒有很好地改善畫面模糊的問題，反而還讓狗毛被綠色缺染的效果更明顯了@@

讓我選圖來用的話，那還是resample比較好，後製要改變顏色的飽和度太容易，但糊掉軟軟的圖要銳化變清晰卻又能自然沒有塗抹感就非常困難了~

跑了一下各個denoising數值下resample生成的圖的差別，resample的顏色從0.7開始明顯跑掉了….

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/xyz_grid-0001-655883119-scaled.jpg)

換個採樣法看看顏色能不能盡量不要跑偏這麼嚴重 :

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/xyz_grid-0010-655883119-scaled.jpg)

換不同的採樣法是有稍微改善了，不過只要是用resample的處理器，Denoising愈高，草地顏色都是會開始有偏差。

後來還想說，那提示詞特別註明”green” grassland會不會有機會改變草地顏色的問題，結果反而弄巧成拙……，算了算了，直接Photoshop後製，這樣比較快。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/xyz_grid-0002-2589505107-scaled.jpg)

------

而三種採樣器底下專門對應的參數為何，直接看圖示就很清楚。

**tile\_resample :**

Down Sampling Rate數值如果是2的話，就會把原圖是512×512尺寸的圖縮小成256×256。圖縮的愈小，SD在重繪成大圖時就有更多重新自由發揮的空間。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tile02_2.png)

**tile\_colorfix :**

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tile04_2.png)
![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tile04.jpg)

**tile\_colorfix\_sharp :**

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tile05_2.png)
![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tile05.jpg)

------

#### **範例二 、失去所有內容細節/畫崩壞的圖，重繪成像**

原圖是一張512\*512失去內容細節/畫崩壞的圖(官網上的示範原圖)

提示詞 : dog on grassland，Denoising重繪幅度 : 1，預處理器 : tile\_resample

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tile06.jpg)

這裡把各Denoising數值下的演變圖也放出來，大家看這過程是不是有熟悉的感覺~

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/xyz_grid-0012-655883119-scaled.jpg)

之前圖生圖裡的sketch塗鴉不就也是一樣，我原圖給它一張手殘的色塊圖，之後只要再給SD一些提示詞說明畫面中物體有些什麼，就一樣能畫出一張修復圖(或者應該說是點石成金的圖給我)。

這裡tile主要就是提供了”辨識鎖定”物體為何的功能(以及記錄構圖所佔比例和顏色訊息)，原圖再崩壞，但只要在tile還能辨識出原圖是個什麼物體的情況下，就算不給提示詞也能重繪新生成一張和原圖長得差不多的圖給你。

因此，別再只因為512×512的崩壞原圖和新生成的圖也都是512×512的尺寸，但結果畫面”細節”變多了/修復了崩壞的原圖，就認知成tile模型可以修復原圖/增加細節…..太神奇了….。

------

#### **範例三 、解決圖生圖放大重繪時，重繪幅度過高產生崩壞幻覺圖的問題**

以往在圖生圖裡對小圖進行重繪放大時，我們都得要小心注意放大的畫面尺寸超過一定大小後，即便想要對原本的小圖進行更多的變化細節內容時，但重繪幅度也不能拉太高。受限於Stable Diffusion 1.5模型訓練的圖都是512×512，開太大尺寸的畫布來進行繪圖的話，就會出現奇怪/畸形的重疊幻覺圖。

如下圖所示，隨著圖片的倍率愈放大，能畫出正常圖片可使用的重繪幅度值就愈低。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tile07-scaled.jpg)

但現在有了tile對原圖進行辨識鎖定以及記錄構圖所佔比例和顏色訊息後，多頭身的奇幻狀況就迎刃而解了，現在即使在高倍率放大下，開再高的Denoising值也沒問題。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tile08-scaled.jpg)

理論上，再繼續放大尺寸重繪也是不會有問題的，不過我的顯卡不充許…….。

但問題都是有解的，下面最後一個範例，就是再加上Ultimate SD Upscale腳本功能，幫助我們把圖往4K、8K，16K…的尺寸邁進~

------

#### **範例四 、Tile搭配Ultimate SD Upscale，把圖重繪放大放大再放大~**

Ultimate SD Upscale這個外掛的功能就是把你要的尺寸大小的圖切割成512×512(或是更小的區塊)去算圖，如此一來，就不用煩惱原本顯卡只能畫出最大圖的極限。SD每次就只畫512×512的圖，之後再拼接成一張大圖的邏輯下，”理論上”畫出來的圖是可以無限放大的(只是愈大張的圖就要花費愈多的時間)。

的確，在一定程度的尺寸時，Ultimate SD Upscale是個好用的工具。但實際使用時總還是會出現一些問題存在…..。

使用Ultimate SD Upscale，要先到extension搜尋安裝Ultimate SD Upscale外掛，外掛安裝相關可參考之前文章 :

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tile09.png)

安裝後就可以在圖生圖介面下的Script處找到新安裝的Ultimate SD Upscale

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tile10.png)

------

現在來用Ultimate SD Upscale把這張512×768的原圖放大8倍(4096×6144)先測看看。

前面圖生圖和ControlNet Tile的設定都和範例三一樣，而Ultimate SD Upscale的參數介面設置如下 :

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tile11_02.png)

- **Target size type** : 我都選以這邊設定放大的倍率為最後輸出，設定成這個選項後，上方圖生圖介面下原本的尺寸設定就會被忽略。
- **Upscaler** : 依據你的圖片類型(真人照片還是二次元動漫)來選擇適合的放大演算法。
- **Type** : 這邊我都直接用預設的Linear，選另一個chess跑出來的圖也沒看出來有差別。
- **Tile width** : 這邊預設是512，但如果你發現512你的顯卡一樣跑不動的話(Out of memory)，那就再繼續縮小數值。
- 另外**Seams fix Type** 設定存在的目的，是因為畢竟這是用切割的方式跑完圖後再拼接組合回去，所以有時你會發現圖中每個區塊組合邊緣會有格狀線條痕跡在(特別容易在背景的地方看出來)。這個痕跡明不明顯則是依你的原圖內容而定，有的很明顯看得出來，有的幾乎看不出來。所以這時我們會想到要去修復這些組合邊緣痕跡。but，目前所有Seams fix Type測試過後都沒什麼作用(我都是以真人照片的圖為主，也許其它類型的圖片有效也不一樣，大家可以自行測試)，邊緣痕跡看起來很明顯的圖怎樣都還是會有痕跡存在。所以這裡的設定我都不去使用它，真的遇到會有格線痕跡的照片時，那就放棄使用Ultimate SD upscale，或是還算有得救的就勤勞一點Photoshop後製修一下。
- **Save options / Seams fix** : 如果有使用Seams fix Type時，記得這裡要勾選最後畫出來的圖才會有儲存下來。

------

按照網上許多教學的說法，Ultimate SD Upscale再搭配上tile可以高清放大，得到一張以往畫不出的大圖。我原本也想像這樣不就可以輕鬆生成高畫質的大圖來上傳圖庫，但現實總是沒這麼簡單的，可能網上教學的案例都是拿二次元動漫畫風的圖來放大所以感覺不明顯，但如果我主要是想用在真人寫實照片的高清放大時，難免各種缺點很明顯就顯露出來了 :

前面測試開啟tile可以抑制住放大尺寸重繪時，Denoising重繪幅度拉太高出現的多頭身奇幻圖。但現在放大到8倍後，tile的控制度也不太行了，雖然沒有出現多頭身奇幻圖，但畫面中很多地方也開始出現各式幻覺了。所以開啟tile後可拉高重繪幅度的能力，也只能限制在一定大小範圍內，並不是完全沒極限。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tile12_02-scaled.jpg)

即然太高的重繪幅度不行，那我就放棄高重繪幅度，只是單純想把圖按原樣放大就好呢 ？這邊把重繪幅度設置0.2。

但結果就是，得到一張平面塗抺感很重的放大圖，用重繪放大卻不能開高一點的重繪幅度去增畫細節，那還不如直接把原圖拿去Extras附加功能底下去用同一個放大演算法去放大就好。直接用放大演算法放大還更省時間(Time taken: 53.2 sec)，不用去繞這一大圈把圖切小塊去重繪組合放大(Time taken: 6 min. 45.9 sec.)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tile13-scaled.jpg)

------

也許再多一點耐心和實驗精神，再去微調整CFG、Denoising、Controlnet權重、提詞再加加減減一下…..等的搭配設定可以比直接放大好些，少點塗抺感。但總體就是這樣，都還是有避不過的極限限制在(遠看還行，拉大近看還是有破綻)。

後來又再好奇比對一下，如果是直接重繪放大4倍(目前我顯卡跑圖尺寸的極限值)，和使用Ultimate SD upscale分割畫面區塊再重組也是放大4倍的情況下，所產生出來的圖像會不會有差別，因為都說有了Ultimate SD upscale是低顯卡配備的救星，省錢也能畫大圖。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tile14-scaled.jpg)

這次的Denoising值只拉到0.5，同樣都開啟了tile，但有使用Ultimate SD upscale分格畫圖，tile抑制幻覺圖的能力會有所下降。不過在這張Denoising : 0.5的情況下，用Ultimate SD upscale的塗抺感沒這麼重，整體畫面看起來還比直接重繪放大4倍的清晰度/銳利感更好(因為Ultimate SD upscale裡有套用到放大演算法。開低倍率少量使用放大演算法可以改稍微善清晰度/銳利感，但如果倍率開太大同時卻又無法用高重繪幅度畫更多細節的話就只會產生嚴重塗抺感)。

那就稍微再降一點Denoising，可惜有使用Ultimate SD upscale時，直到Denoising降到0.3以下才不存在幻覺的鬼影。但這樣一來，沒有足夠的重繪幅度增添細節，那因為放大演算法的塗抺感又會跑出來了….。

------

_**補充 :** 在做完上面的測試後，看到國外Youtube介紹使用Ultimate SD upscale時才發現有個好用的小技巧可以一定程度避開上面有開啟tile，使用高重繪幅度情況下，只要一使用Ultimate SD upscale分格算圖就會比直接重繪放大容易產生幻覺圖的問題。_

**_“只要把提示詞裡，有關圖片內容描述的正向提示詞通通拿掉，最多只留一些中性的詞就好(high quality, realistic photo….)，又或是全空白。”_**

_用這小技巧我再重測一遍後，如果只是放大4倍，Denoising 0.5，即使用了Ultimate SD upscale還不會出現幻覺鬼影，但如果Denoising到了0.8以上，或是倍數開到8倍以上畫面裡還是一樣會開始出現奇奇怪怪幻覺，或是小部份畫面像是畫圖用力過頭崩壞/畫壞的質感。_

_後來再重思考想到文章開頭關於tile影片的講解中提到的，圖片過大時，提示詞對大圖中的每個小區塊(512×512)會**“分別”**產生影響。提示詞與tile間就是你認為和AI認為的拉扯，那麼就讓這裡不要有拉扯，全AI判斷(只要AI對圖片中的內容沒有剛好判斷錯誤~應該機率很小)，去掉提示詞會”分別”對每個小區塊產生影響的因素拿掉後就更保險、不易出現幻覺鬼影。所以這裡可以拿掉提示詞或是再拉高tile權重去降低使用Ultimate SD upscale分格算圖時的幻覺鬼影。_

這個Youtube – Olivio Sarikas的Stable Diffusion教學，有空可以把他的教學影片都看一遍。

------

在現有電腦顯卡配置下，想得到一張遠近都能看的高清放大圖，以這張圖我會選擇處理的方式就是，不用Ultimate SD upscale。直接用顯卡極限重繪放大畫一張增加了高重繪幅度細節原圖4倍尺寸的圖(2048×3072)，之後再用Extras下的放大演算法去放大2倍(4096×6144)。這樣是目前試出效果最理想也相對省時的方案。

(PS. 不管上網去搜羅哪種超好用的放大演算法，我覺得目前這些放大演算法都只動用到放大2倍就好，再高的倍數都是會有滿滿的失真塗抺感，只能遠觀不能近看~)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tile15-scaled.jpg)

------

如果真的還是要用Ultimate SD upscale的話，也有試過另一種方法就是 :

一次先放大2倍(denoising : 0.3)→丟回img2img再放大2倍(denoising : 0.3)→再丟回img2img再放大2倍(denoising : 0.1)

同樣最後達到原圖的8倍(4096×6144)，結果能得到的效果要比一次放大8倍來得好很多。每次的Denoising盡量調低一點(差不多足夠抵掉演算放大法相應倍數的塗抺感就行)，不然女孩會隨著一次次的再重繪放大2倍的過程中愈長愈”成熟”(細節過多人像易顯老，連背景，整張圖看起來都會有畫過頭的不自然感)~

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tile17_02-scaled.jpg)

不過我覺得Ultimate SD upscale實在還是太麻煩了，每一張圖或許多注意調整各個參數找到一個完美的搭配，可以讓圖有細節的放大沒有塗抺感又不出現幻覺鬼影。可是別忘了還有個邊緣格狀線條痕跡的問題要注意。如果最後放大的圖還是出現格狀線條痕跡的話，那我真的就束手無策了。

這張圖用了Ultimate SD upscale的方式重繪放大後，最終在背景處還是出現了一格一格區塊……@@。白忙一場空

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tile16.png)

------

不過大家別忘了開源的AI繪圖，最大的優點就是一有需要解決的問題時，集眾人之力，很快就會有更優化的更新方式出現。在Ultimate SD upscale之後，又還有一個更強的分格放大繪圖 : Tiled Diffusion with Tiled VAE

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tile18.png)

官網上說明 : Compare to Ultimate SD Upscale, the algorithm is **much more faithful to the original image** and produces significantly fewer artifacts.

以及最重要的”Tile Overlap”，每個分格的區塊都會互相重疊一部分，而不是像Ultimate SD upscale是單純的拼接，這樣就可以解決邊緣格狀不自然接縫痕跡(seams)的問題了吧~

這部分就之後另一篇文章再來測試，看能不能把我想要的真人寫實照片也能真的沒有塗抺感的高清放大~

------

由於現有顯卡性能限制，想要在圖生圖裡重繪放大一張圖到4k以上的尺寸就得要借用各種分格繪圖再重拼接成大圖的方式，無法一次生成。之前試過大家很推崇的Ultimate SD upscale，但對於我要重繪放大的”真人寫實照片”類型的圖來說，一直出現各種問題(即使有Controlnet輔助，仍然是一下畫面還是有鬼影、一下死平塗抺感很重、一下又是格狀的邊緣痕跡明顯…..沒完沒了)。今天就再來測試另一個也是利用分格繪圖再拼接的重繪放大外掛工具- Tiled Diffusion and VAE。

想要把一張小圖放大像素值的同時又能保留原本圖片裡的細節，不要各種死平的塗抺感，那就只能在放大像素的同時增添相應足夠的細節上去。所以一般只是單純利用放大演算功能把圖放大，或多或少不管哪個多厲害的演算法都一樣，那種塗抺感都避不掉(細節丟失)，大多都是遠看還行拉大近看就破功(特別是在”真人寫實照片”類型的圖更明顯)。

因此，要小圖放大同時又有細節在，那就只能用重繪放大的方式。所以現在我的生圖作業流程都是所有文生圖裡產出的小圖，用重繪放大畫出一張顯卡一次能畫出最大的尺寸之後，再用放大演算把圖放大2倍(2倍以下是目前我比較接受不至於把圖拉近時明顯看得出塗抹感的值)。

可是目前我的顯卡(RTX 3080, 10G)，一張512×768的原圖，重繪放大不爆顯存能畫的最大尺寸差不多只能到2048×3072左右，之後再用放大演算把圖放大2倍也就只能得到4096×6144左右，4K以上8K不到。

後來有了Ultimate SD upscale分格算圖再重拼接生成大圖的重繪放大外掛出現，我就想試看看能不能就此產出更大尺寸的圖但同時保留我能接受至少該有的細節質感。

可惜試過之後，個人覺得不是很理想。在最終圖像的成果和效率上都還是不如之前的作業方式。情況下，得到我要的效果(得到更大尺寸的圖，但維持該有的真實細節~不是那種假假生硬的高清放大)。

## 9、Tiled Diffusion & Tiled VAE 功能與特色

Tiled Diffusion 與 Tiled VAE各別有不同的功能作用 :

(https://github.com/pkuliyi2015/multidiffusion-upscaler-for-automatic1111#%F0%9F%86%95-tiled-noise-inversion)

- **Tiled Diffusion :** 本質類似於高清修復，是對圖片進行重繪的方式放大圖片尺寸。和Ultimate SD upscale一樣，它也是利用分區塊的方式重繪算圖，可解除顯卡算圖尺寸的上限值。但其中特別的一點是，每個區塊拼接的方式”Tile Overlap”，讓每個區塊(tile)部分重疊融合，這樣可以減少格狀的邊緣痕跡。如下圖官網裡的說明 :

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tiles_explain.png)

- **Tiled VAE :** 則是原作者獨創的演算法，能有效降低顯存的消耗。所以一般使用Tiled Diffusion生成重繪大圖時，都會建議一起搭配使用。但Tiled VAE也是可以單獨使用，用來提升顯卡原本的算力，例如在高清修復時，原本你只能放大1.5倍，但開啟Tiled VAE之後，就有可能可以提升至2倍。

### Tiled Diffusion & Tiled VAE 介面參數

在安裝完外掛後，在文生圖與圖生圖的頁面下，會看到多了2個下拉選單

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tiled01.png)

**Tiled Diffusion**

除了紅框以外的部分，Retouch 和 Renoise kernel size，我也不清楚這兩個到底是用來做什麼的，官網上也沒有針對這個有說明，就按預設狀態不要動它吧。而最下方的Region Prompt Control下拉選單，是用來對畫面分區域進行各別區域的提示詞設定。不像一般我們使用提示詞時，會針對整個畫面進影響，無法指定哪個區域要有什麼物品以及該物品的特徵描述。這個功能我是還沒去使用過，但網上已有其他很多利用這功能在文生圖裡進行提示詞分區對畫面描述控制的教學，有興趣的人可以再去找來看或是參考官網說明，這篇主要是要測試重繪放大功能的效果比較，就跳過這部分。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tiled02_02.png)

- **Enable Tiled Diffusion** : 開啟使用 Tiled Diffusion
- **Keep input image size** : 勾選會讓上方原本的長寬尺寸設定失效，會以圖生圖視窗內原圖的長寬尺寸為基準進行重繪放大。
- **Method** : 這裡有Multidiffusion 和 Mixture of Diffusers兩種可選擇。按官網說明，MultiDiffusion適合用在重繪(高清修復)、Mixture of Diffusers更適放大。我使用上覺得兩個好像效果都沒差別。我的目的是要重繪放大，所以通常都只選MultiDiffusion。
- **Laten tile width & height** : 這裡是決定每個區塊的大小，數值愈大，一張圖所需分的區塊就愈少，算圖速度愈快，但所佔用的顯存也愈大。預設值是96，官方作者建議使用128。
- **Laten tile overlap** : 是指區塊與區塊間重疊面積大小，數值愈大，接縫愈少，但算圖速度愈慢。原作者建議，使用MultiDiffusion時設定32或是48，使用Mixture of Diffusers時設定16或32。
- **Laten tile batch size** : 指一次算圖處理的區塊數量，數量愈多，算圖速度愈快，但也更佔顯存。
- **Upscaler** : 選擇放大要使用的演算法。
- **Scale Factor** : 放大的倍數。
- **Noise Inversion** : 按官網說明，開啟Noise Inversion會在生圖時進行噪聲反推，讓新生成的圖像與原圖保有更高度的一致性，以及如果覺得生成的圖像感覺有變比較模糊時，可試著提高Inversion steps、降低Renoise strength。  
  有使用ControlNet的Tile模型去拉高重繪幅度時，如果畫面因此細節過多變雜亂，就可以考慮打開Noise Inversion去調整兩邊的參數，找到一個所需畫面質感的平衡。  
  不過這個選項實際使用，會讓圖產生平滑磨皮少掉部分細節，很難找到一個剛好理想的平衡點，所以我一般選擇不太去使用它。

**Tiled VAE**

Tiled VAE有個很貼心的地方，它會根據每台電腦顯卡效能不同，在開啟下拉選單後，裡面最一開始的預設參數值大致就是最適合你顯卡能運行的狀態。

- **Enable Tiled VAE** : 開啟使用 Tiled VAE
- **Encoder & Decoder Tile Size** : 預設數值遇到爆顯存(Out of memory)時，再把數值向下調整即可(在不爆顯存的前提，數值是盡量愈高愈好)。
- **Fast Encoder Color Fix** : 當Fast Encoder勾選時才會出現的選項，勾選使用Fast Encoder算圖發現成像顏色變調時，可試開啟此選項。而Fast Encoder有沒有勾選算圖的速度實測一次也差沒多少時間，所以一般我也不會去勾選Fast Encoder，用了反而多一次顏色可能失真又要再修復(又有可能修復的不理想)的麻煩。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tiled03.png)

### Tiled Diffusion & Tiled VAE 搭配ControlNet-Tile 實測重繪放大

**512×768重繪放大8倍(4096×6144)**

拿之前重繪放大一樣的圖來實測對比。512×768一次重繪放大8倍(4096×6144) :

denoising0.3，先不管我覺得女孩皮膚看起來氣色很差，長斑…的問題。低重繪值，一樣不夠8倍率放大所需增加的細節，髮絲開始塗成一片。然後感覺畫面糊糊矇矇，依官網建議加上Noise Inversion，但果然不出所料，就是塗抺/磨皮效果，代價換來更假假的平貼塗抺感。但以8倍重繪放大來說，是有比Ultimate SD upscale好一點，假假的塗抺感相對有下降一點點…。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tiled04-scaled.jpg)

------

denoising0.7。改用高一點重繪值，解決放大8倍細節不足夠的部分。髮絲有改善，但整張畫面中開始出現奇怪的小凹點，不只下圖所標示出來的地方，整個背景處也有。而拉高重繪幅度值後，如果想用Noise Inversion去去除一些高重繪幅度產生過度細節產生的雜亂，一樣的問題，Inversion steps、Renoise strength值不管怎樣調，要有效消除雜亂的地方和假假的磨皮感只能二選一。

但這裡放大8倍後，不像使用Ultimate SD upscale會有明顯的格狀痕跡(seams)，Tiled Diffusion的”Tile Overlap”的確是有解決了seams的問題。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tiled05-scaled.jpg)

------

**512×768重繪放大4倍(4096×6144)**

8倍結果不理想，挑戰失敗。那先只用4倍，來看使用Tiled Diffusion with VAE的重繪放大4倍，和直接重繪放大4倍的區別。

以下面對比圖來看，這次我比較喜歡有使用Tiled Diffusion with VAE重繪(0.7)放大4倍的髮絲和皮膚紋理/膚色的處理，加上同樣0.7的重繪幅度，對人物臉部長相原樣維持統一度更好。唯一可惜的是人物衣服上和放大8倍時一樣出現奇怪凹點和面料質地也有點畫崩了。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tiled06-scaled.jpg)

------

**512×768分多次低重繪幅度放大8倍(4096×6144)**

最後和測試Ultimate SD upscale時一樣，也用Tiled Difussion去分次重繪放大 :

一次先放大2倍(denoising : 0.4)→丟回img2img再放大2倍(denoising : 0.4)→再丟回img2img再放大2倍(denoising : 0.1)

同樣最後達到原圖的8倍(4096×6144)，最終結果要比一次放大8倍來得好很多(即使只要放大4倍，也是一次2倍、再2倍放大的效果比較好，畫面中比較不容易出現一些奇怪的小問題)。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tiled07_02-scaled.jpg)

------

**三種重繪放大8倍(512×768 → 4096×6144 )過程的結果比較** :

各有各自的小問題(不滿意的地方)在，不過其中Ultimate SD upscale我覺得可以直接放棄不用了，Tiled Diffusion with VAE能達成一樣的分格算圖解除顯卡效能限制，且畫面中出現的小缺點也比較少，更重要的是背景放大來看不會有格狀的痕跡，唯一不如的地方大約就是Tiled Diffusion with VAE算圖相對比Ultimate SD upscale費時。

而第一張除了牛仔褲頭上的皮革貼標處沒畫好糊成一片，其它細節放大來看，都比另兩張好，少了許多”AI的筆觸/雜亂畫崩的痕跡(artifacts)”，整體細節過度得最自然(例如在下圖中注意側臉輪廓與頭髮瀏海間)。且第一張的作業流程也是最省時省事的。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tiled08_02-scaled.jpg)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tiled08_02.jpg)

------

**Tiled Diffusion with VAE重繪放大16倍(512×768 → 9182×12288 )挑戰** :

最後再拿Tiled Diffusion with VAE去進一步把4096×6144的圖重繪放大2倍(8192×12288)，看會不會崩圖~

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tiled09.jpg)

雖然算圖費時很可觀，但絕對是可以生成超大圖片，且整體看來還算可以，沒有明顯崩圖或什麼奇怪幻覺。只是拉近放大來看，原本4096×6144大小時就有的小缺點更進一步變明顯，另外只要是淺色處的區塊，會有明顯粗糙崩壞的紋理出現。

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/tiled10-scaled.jpg)

這張原圖如果想要生成細節自然的超大圖，不怕麻煩的話，可以把前面三種重繪放大方式比較中的第一張(在8倍大小時，小缺點最少，細節放大也最細緻自然)，和其它張稍微用PS合成修補一下，取長補短，之後再利用Tiled Diffusion with VAE來進一步重繪放大2倍，就可以生成更理想的超大圖(8192×12288)。

------

## 10、StableSR 高保真圖像放大

**Step 1 : 安裝StableSR外掛**



![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/stableSR_01-e1695286322356.png)

**Step 2 : 下載模型檔案**

StableSR安裝完成後，我們還需要再把運作StableSR所需的Checkpoints模型檔案 & StableSR模組下載放入相應的資料夾裡才能開始使用。

- Checkpoints模型 (Stable Diffusion V2.1 768 **EMA** checkpoint (~5.21GB)) :  
  從HuggingFace網址下載 : [HuggingFace![](https://huggingface.co/stabilityai/stable-diffusion-2-1 "Stable Diffusion V2.1 768 EMA checkpoint")  
  檔案下載後放進資料夾路徑 :  …….\\models\\Stable-diffusion
- StableSR模組(webui\_768v\_139.ckpt) :  
  從HuggingFace網址下載 : [HuggingFace\_StableSR Module![](https://huggingface.co/Iceclear/StableSR/blob/main/webui_768v_139.ckpt)  
  檔案下載後放進資料夾路徑 :  …….\\extensions\\sd-webui-stablesr\\models

**Step 3 : 下載官方建議搭配使用的其它外掛或是VAE模型(自選，非必要)**

- Tiled Diffusion & tiled VAE 外掛:  
  請參考之前文章 : [AI繪圖-Stable Diffusion 016- Tiled Diffusion with Tiled VAE![](https://dianxiaoeryu.com/ai%e7%b9%aa%e5%9c%96-stable-diffusion-016-tiled-diffusion-with-tiled-vae/)
- VQGAN VAE模型 :  
  下載連結 : [https://drive.google.com/file/d/1ARtDMia3\_CbwNsGxxGcZ5UP75W4PeIEI/view![](https://drive.google.com/file/d/1ARtDMia3_CbwNsGxxGcZ5UP75W4PeIEI/view)  
  檔案下載後放進資料夾路徑 :  …….\\models\\VAE

### StableSR 操作介面 & 使用設定注意事項

完成所有安裝與所需模型檔案下載後，在圖生圖功能頁下的的Script(腳本)處就會看到多出了 StableSR的選項

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/stableSR_02-e1695295222913.png)

- **SR Model** : 這邊就是之前下載的StableSR模組 – webui\_768v\_139.ckpt
- **Scale Factor** : 圖片放大倍數。(啟用StableSR後，其它地方圖片尺寸的設定都會無效)
- **Color Fix** : 在使用StableSR與分格繪圖(ex. Tiled Diffusion)時很容易會產色顏色偏移，所以需開啟Color Fix。一共有2個選項(Wavelet、AdaIN)，這邊官網建議使用Wavelet算法的效果比較好。
- **Pure Noise** : Pure Noise開啟時，SD會無視重繪幅度，最終生成一張更具細節的圖片。Pure Noise沒開啟時，即使重繪幅度設置到最大值1，最後圖片也不會完全達到重繪幅度1原本會有的細節呈度(這樣也許對成像效果反而在美感上更理想)，而在Pure Noise沒開啟時，官方建議重繪幅度設置成1。

**操作注意/建議事項 :**

1. 注意Checkpoint要選擇指定的大模型 ，而SD VAE雖然並不一定要用官網提供的，但既然官網有另提供，還選擇官網推薦的來用。  
   ![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/stableSR_03.png)  

2. 圖生圖的採樣方法(Sampling method)建議使用 : Euler a,  CFG Scale=7, 採樣步數(Sampling steps) >= 20

3. 官網實測建議，加上Negative prompts有助於成像品質(ex. 3d, cartoon, anime, sketches, (worst quality:2), (low quality:2))，而正向提示詞(Prompts)的幫助不大，但可能也有些許作用(ex. (masterpiece:2), (best quality:2), (realistic:2),(very clear:2))

4. 生成的圖片尺寸> 512時，建議搭配使用Tiled Diffusion & VAE，不然成像畫質會變差。(真的會變很差……根本Tiled Diffusion & VAE就是必用的搭配吧？)  

   在搭配StableSR使用時，Tiled Diffusion的設定官方建議如下 :  
   **Method = Mixture of Diffusers** :  
   Latent tile size = 96, Latent tile overlap = 48  
   **Latent tile batch size :** 愈大愈好，只要不會到爆顯存就行。  
   **Upscaler處要選擇”none”** (因為不需要在這裡放大，放大的作業是會在StableSR處進行)  
   ![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/stableSR_04.jpg)

一切設定完成後，就把圖放進圖生圖視窗開始算圖吧~

### StableSR 圖像放大實測

見鬼了，我已經完全照官網的參數來設置，網上找到的教學也是一樣模一樣的設置，唯一差別就只是我用的是真人寫實照片，比較不是用二次元或是2.5D動畫照片。但說好的”高保真”放大呢？、超高清無損？滿滿的細節？

這個外掛也說Suitable for most images (Realistic or Anime, Photography or….)

唉~算了，都花時間安裝/下載一些要配對的模型檔案了，還是把結果都記錄一下吧，之後再來卸安裝刪除，別浪費空間和增加SD運行的負擔。

512×768 放大4倍 :

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/stableSR_05-scaled.jpg)
還只是放大4倍，原以為那2倍就好，一次放大小一點，結果也是沒差多少，就是寫實照片變得很平貼，然後畫面加上滿滿的顆粒狀紋理/artifacts/畫壞的各種小區塊…..。

PS. 512×768 放大4倍，如果沒搭配Tiled Diffusion with tiled VAE的話會長這樣 :

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/stableSR_06-scaled.jpg)

------

最後實在好奇，照著大家教學用的二次元/2.5D動漫圖是不是效果就會有差 :

用二次元的圖來試就沒像真人照片效果慘烈，但也沒好到多驚豔的地步，StableSR相對要多一些下載的檔案和設定，結果效果也沒變比較好………..

(下圖對比為原圖768×768放大4倍(3072×3072)，有啟用Pure Noise效細節效果會比沒啟用Denoising設置1的更好一些)

![](https://dianxiaoeryu.com/wp-content/uploads/2023/09/stableSR_07-scaled.jpg)
