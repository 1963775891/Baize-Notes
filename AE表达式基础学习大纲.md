禁用、拾取表达式，显示表达式图表



A:Enable Expression 禁用、启用表达式
B：Show Post—Expression Graph 激活此图标，点开图形编辑器以后可以看到表达式产生的数据变化。 C:Expression Pich Whip 表达式拾取螺旋线
D:Expression Language Menu 表达式语言菜单

------

## 1、JavaScript基础

101变量 

**什么是变量？**
变量可以理解为是一个容器，用来存储数据。 

**创建变量**
使用变量之前需要先创建变量，在js中使用关键字var，后面跟一个字符（变量名）来创建变量。（关 键字是js定义好的有一定特殊含义的单词）。
```JAVA
var a；//声明一个名为a的变量 
```
**给变量赋值**

创建变量以后，需要给它赋值，js中用=来给变量赋值。 
```JAVA
var a=“比邻课堂”
var b=9527; 
```
**ae中创建变量**

ae中可以省略var关键字，直接给变量名赋值。

```JAVA
a=“比邻课堂”；
b=9527;
var name=“王大气”；//ae中如果使用了var，默认不会显示变量值，需要引用一下才行 name;
```
注意：在写复杂的表达式时，声明变量建议加上var关键字，但是因为我们不会写太复杂的表达式，不 加var大多数时候不会造成错误，所以我一般不加var。

**为什么要使用变量？**
使用变量可以简化代码，增强代码的可读性，可以重复使用，随时根据需要进行改变。
比如：获取形状图层的宽度，将其赋值给变量w，这样就可以直接用w，而不用再重复写一句很长的代码。
```JAVA
w = thisComp.layer("Shape Layer 1").content("Rectangle 1").content("Rectangle Path 1").size[0];
w/2;
```

**js中的保留关键字**
Javascript的保留关键字不可以用作变量、标签或者函数名。
如：var、this、in、for、let、case等不能用做变量名 

**变量的命名规则**

- 以字母、下划线、$开头，不能用数字开头
- 由字母、下划线、$或数字组成
- 区分大小写
- 不能使用关键字和保留字 

*注意：*
*变量名最好起有实际意义的英文或拼音，不要使用类似aa，bb之类的无意义的字符。 注释*
*注释用来解释javaScript代码，它不参与代码的执行，可以帮助我们更好的理解代码。*

```JAVA
//单行注释 以英文状态下 //开头 任何位于 // 之后的不换行文本都会被 Javascript 忽路(不会执行)
var name ="华安";//定义名称var name
var num = 95277//定义编号
    
// 多行注释以 /*开头，以*/结尾，位于其中的文本都不会被执行
/*
作者:比邻课堂
QQ:554579800
*/
```

**变量的数据类型**
常见的数据有以下几种:

```JAVA
//字符串(string)
var iname="王大气"；
//数字(Number)
    var age 18;
//数组(Array)
varhobby=【'旅游'，·追剧'，·服装设计']；
//布尔(Boolean)
    var iFlag true;	//只能有两个值：true或false
//对象(object)
var obj =(
```

**AE中常用到的三种数据类型:**

**字符串**，是插入到成对的单引号或双引号任意字符，用于存储和处理文本。

**数字**，整数、小数、0、负数都是数字。数字不需要放在引号中间，如果放在引号中间就成了数组

**数组**，不涉及到类型转换，后面我们再详细说明。

**typeof类型检测**
typeof操作符用来检测变量的数据类型

```JAVA
//在文本层的源文本属性写如下表达式进行测试
name="王大气"；
typeof name;//string
    
age 18;
typeof age;//number

typeof false;//boolean

//在js中，数组是一种特殊的对象类型。因此typeof[1,2,3,4]返回object
arr=[1,2,3,4]
typeof arr;//object

//typeof一个没有值的变量会返回undefined
typeof b;//undefined
```

**变量数据类型转换**
js中数据类型转换有三种：

```JAVA
//将字符串str转为数字
Number(str);	//str必须为纯数字的字符串

//将数字num转为字符串
String(num)

//将字符串、数字转换为布尔值
Boolean();
```

ae中最常见的就是数字和字符串的相互转换

```JAVA
//一些会到的类型转换方法：
num.toString();	//将数字num转为字符串
num.toFixed(n);	//把数字num转换为字符串，并四舍五入显示n位小数
parseInt(str);	//把字符串转为为一个整数，字符串必须以数字开头
parseFloat(str);	//把字符串转为一个浮点数，字符串必须以数字开头
"0"+5:	//字符串，字符串+数字得到字符串
"5"-1;	//数字，字符串-数字，得到数字
```

### 103字符串

字符串是插入到成对的单引号或双引号中的任意字符，用于存储和处理文本。

```JAVA
var a="王大气"；
var b="18";
var c 'Hello World!';
var d='[1,2,3,4]'i
var e "It's my book!";
var f='It's my book!'；	//报错，AE中不会提示错误，就直接不显示字符串内容
    
//当数字放到引号中间的时候，它的类型就是字符串类型，不是数字类型了，如果要进行运算，需要先进行类型转换
var x "10";
var y =24;
x+y:	//1024

Number(x)+yi	//34
```

**特殊字符**

反斜杠（\）用来在字符串中插入单引号、双引号、换行符、反斜杠等特殊字符

```JAVA
//\' 插入单引号
'it\'s ok';

//\” 插入双引号
"中国是瓷器的故乡，因此china与\"China（中国）\"同名。"
    
//\n 插入换行符
"王大气\n王漂亮"；
    
//\\ 插入反斜杠
"汤米\\杰瑞"
```

**字符串长度**

length属性，用于获取字符串的长度，空格也算。

```JAVA
var
a="比邻课堂"
a.length;//4

varb="比邻课堂"；
b.length;//7
```

**split（）**
split(separator,howmany)方法用于把一个字符串分割成字符串数组。
separator，分隔符，可以是字符串也可以是正则表达式，指定字符串分割的位置。
howmany，指定返回的字符串数组最大长度，不包含此值，

```JAVA
str "hello";
str.split("");	//[h,e,1,1,o]

//在匹配的位置分割
str "hello";
str.split("1");//[he,,o]

str "hello";
str.split("",2);/[h,e]
    
//从-的位置把字符串分割成字符串数组
str="1995-06-02":
str.6p1it("-");//[1995,06,02]
```

**slice（）**
slice(start,end),方法可提取字符串指定部分，并把被提取的部分以新的字符串返回。
新的字符串包括stat,不包括end.
字符串中第一个字符位置为0，第二个字符位置为1，以此类推。

```JAVA
//返回1-6之间的字符，不包含6
txt "hello,world!";
txt.slice(1,6);	// ello,

//返回第6位以后的所有字符
txt "hello,world!"
txt.slice(6);	//world!

//如果参数为负数，则从后往前返回对应个数的字符
txt = "hello,world!";
txt.slice(-2)i// d!
```

**toUppercase()**
把字符串转换为大写。
```JAVA
str ="Hello,World!"
str.toUpperCase()i；	//HELLO,WORLD!
```
**toLowerCase()**
把字符串转换为小写。
```JAVA
str ="Hello,World!"
str.toLowerCase()i；	//hello,world!
```
**repeat()**
str.repeat(n)，将字符串复制n次。

```JAVA
//新建一个文本图层，给源文本属性添加表达式
var str ="8";	//定义一个字符串
str.repeat(3);	//将这个字符串重复3次,结果为:888

//新建一个文本层，随便输一个数字，比如0，然后添加表达式
text.sourceText.repeat(8)://00000000
```

**charAt()**
返回指定位置的字符。
第一个字符位置为 0,第二个字符位置为 1,以此类推。

```JAVA
var str ="Hello,world!"
var n=str.charAt(1)i//e
```
**fromcharCode()**
将 Unicode 编码数字转为字符(字母)

```JAVA
string.fromcharCode(65);	//A

//随机生成26个英文字母
posterizeTime(10)；
n = Math.round(random(65,90));
string.fromcharCode(n)
```

### 1_04_数组

数组用于在单一变量中存储多个值。

**创建数组**

```JAVA
//[]里的任意字符，如果是数字可以不用引号

var cars =["保时捷","奥迪","布加迪"];
var num=[1,2,3,4]
```
**访问数组**

通过索引来访问某个数组元素，数组的索引是从0开始的。

```JAVA
var cars =["奥迪","保时捷","布加迪"];

cars[0]	//奥迪

cars[1]	//保时捷

cars[2]	//布加迪
```

**获取数组长度**

```JAVA
var cars =["保时捷""奥迪”""布加迪"];
cars.length	 //3
```

ae中位置[x,y,Z]、缩放[x,y,Z]、颜色[red, green, blue, alpha]等都是以数组的的形式存在的。
```JAVA
position[0]; 	//获取x坐标
scale[1];	// 获取高度
color[2];	// 获取blue数值
```

**获取数组中最大值**
```JAVA
var arr=[12,5,77,89,2,99,520,88];
Math.max(...arr);	//520
```
ES6的扩展运算符…，可以将数组转换为以逗号隔开的参数的形式，这样就可以很方便的通过Math.max获取到最大值。

**push()**
push()，向数组的未尾添加一个或多个元素，并返回新的数组长度，

```JAVA
cars =〔'迈凯轮'，'布加迪威龙'];
cars.push('迈巴赫''帕加尼');// 4
cars;//〔'迈凯轮'，'布加迪威龙'，迈巴赫’'帕加尼']
```

**splice()**
splice() 方法用于添加或删除数组中的元素，并返回除被删除元素以外的其他元素的数组。
该方法会改变原数组，

```JAVA
var arr=[1,2,3,4,5,6,7,8,9,10];
//除第1位元素以后的所有元素，并返回
arr.sp1ice(1);//2,3,4,5,6,7,8,9,10
arr;	//1

//刚除从第2位元素开始往后数4位的所有元素，并返回
arr.sp1ice(2,4);//3,4,5,6

//别除从第2位元素开始往后数4位的所有元素，并在被删除元素位置添加新元素a,b
arr.splice(2,4,"a","b");
arr /1,2,a,b

//从后往前返回指定数位的元素，参数为负数只能传一个参数
arr.splice(-1);/10
```



### **1_07_if条件语句&for循环语句**

**if条件语句**
if条件语句是基于不同的条件来执行不同的动作的。

 **if语句**
if(condition){当条件为true时执行的代码}
```JAVA
 if(下雨){
	“出门带伞”
}
/*
这条语句表明：如果下雨就带伞，
但是没有指明，没下雨就不带伞，所以当天晴的时候，这条语句是没有返回值的，在AE中是会报错的。
*/
```
**if...else语句**
if(condition){当条件为true 时执行的代码}else{当条件为false时执行的代码} 
```JAVA
score -80
if(acore 60){ 
	及格"
elae{ 
	“不及格”
 }
```
**if...else if...else语句**
用来在多个代码块中选择条件成立的来执行 

```JAVA
time=15;
if (time<=10) {
	“早上好”;
) else if (time <=14){
	“中午好”；
else if (time<=18){
 	“下上好”；
) else(
	“晚上好”；
}
//ae不支持下面这种写法
//也就是10<n<80这种写法 
    if(10<n<80)	//do something 
}
```

**for循环语句**
for循环可以将}中的代码执行指定的次数。
```JAVA
for（语句1；语句2；语句3）{
//需要执行的代码
}
```
**语句1 **循环开始前执行，定义一个数字变量，通常为0； 
**语句2 **定义运行循环的条件：
**语句3** 在花括号中的代码被执行一次之后执行，通常是语句1定义的数字变量的累加。 

```JAVA
//将下面表达式添加到文本的source Text，代码会执行4（数组的长度）遍
cars=['阿斯顿马丁'，'迈凯轮'，'帕加尼'，'迈巴赫
car='';    
for(i=0; i=cars.length; i++){
	 car +=cara[i] +'\n' 
}

/* 
阿斯顿马丁，
迈凯轮，
 帕加尼，
 迈巴赫
*/
```

### 1_08运算符

 **算术运算符**

```JAVA
+  加法	3+5	//8
   		 “3”+5	//35
-  减法	8-5	//3
    	 8-“5”	//3 
*  乘法	3*5	//15 
/  除法	4/2	//2 
%  取模(余数)	5%2	//1 
++  自增	++5	//6先加1	5++，下一次加1，多用在for循环中 
--  自减	5--	//5 
```

**注意：**
1、一个字符串加一个数字，或者两个字符串相加的时候，相当于字符串拼接，将多个字符串拼接成一 个字符串。
2、加减除运算存在隐式类型转换的情况，在计算时要楚参与计算的的元素类型。
3、加减乘除运算存在精度问题，比如：0.1+0.2=0.3000000000004，0.3-0.1=0.1999999999999在 计算中需要修正。

**赋值运算符**

```JAVA
x = 5		//将右侧的值赋给左侧的变量,它是最简单最常用的运算符
+=	x += 5	 x=x + 5	//加法运算或连接操作并赋值
-=	x -= 5	 x=x - 5	//减法运算并赋值
*=	x *= 5	 x=x * 5	//乘法运算并赋值
/=	x /= 5	 x=x / 5	//除法运算并赋值
%=	x %= 5	 x=x % 5	//取模运算并赋值
```

**比较运算符**

**逻辑运算符**
逻辑运算符用于判定变量或值之间的逻辑关系。

**三目运算符**
三目运算符是if..else条件语句的简化版，合理的使用能够简化我们的代码。



 **运算符优先级**
下表按从最高到最低的优先级列出javaScript运算符，具有相同优先级的运算符按从左至右的顺序求值。

### 1_09_常用JS方法和函数

**Math.round()**
Math.round（n），把n四舍五入为最接近的整数。 



**Math.floor()**
Math.floor（n），向下取整，返回小于等于n的最大整数。

**Math.ceil()**
Math.ceil（n），向上取整，返回大于等于n的最大整数。



**Math.sin()**
Math.sin（n），返回数字n的正弦值，返回值在—1到1之间。 

**Math.cos()**
Math.cos（n），返回数字n的余弦值，返回值在—1到1之间。 

**Math.atan2()**
atan2()方法可返回从圆点[0.0]到点（x.y）之间的角度的弧度值。
返回—PI到PI之间的值，是从X轴正向逆时针旋转到点（xy）时经过的角度的弧度值。

```JAVA
//指定一个坐标（x，y），坐标值（4，8），使用atan2（）方法计算坐标与x轴之间的角度的弧度， 如下实例：
Math.atan2(8,4);	//1.1071487177940904
```

 Math.tan()
Math.tan（n），返回数值n的正切值，表示一个角（单位：弧度）
正切值是指是直角三角形中，某一锐角的对边与另一相邻直角边的比值。

Math.tan(1);//1.5574077246549023
**Math.exp()**
Math.exp（n），返回e的n次幂的值，e代表自然对数的底数，其值近似为2.71828。 

 **Math.abs()**
Math.abs(n),返回n的绝对值。

 

**Math.sgrt()**
Math.sqrt()方法返回一个数的平方根 

**Math.pow**
Math.pow(x.y),返回x的y次幂的值。 

**Math.max()**
Math.max(value1,value2)返回指定值中最大的值。 

**Math.min()**
Math.min(value1,value2)返回指定值中最小的值。 

**Math.PI**
返回圆周率n（约等于3.1415926）。

 **toFixed()**
n.toFixed（num）；/把n四舍五入为指定小数位数的数字，如果省略了参数num，则用0代替。

**Number()**
Number（n），将参数n转为数字，n必须是字符串类型的数字。

**parselnt()**
parselnt(str)，将字符串str转为整数，这个字符串必须以数字开头，或者本身就是数字字符串。

**eval()**
eval（string）函数可将参数字符串作为脚本代码来执行。
参数是表达式或者js语句。

eval()函数在js中用的不多，在AE表达式中也仅仅是在加载外部.txt文件那个案例中会用到。

###  1_10_try.catch语句

try..catch用来测试处理代码中可能出现的错误。try部分包含需要运行的代码，catch部分包含错误发 生时运行的代码。



### 1_11_for in

for..in语句用于遍历数组或者对象的属性（对数组或者对象的属性进行循环操作）。



### 1_12_while()循环

while循环会在指定条件为真时循环执行代码块。



## 2、常用表达式

### 2_01_AE中的对象 

**对象、方法、属性的理解**
AE中Comp、thisComp、Layer、Solid、Light、Footage等都是对象，它们都有各自对应的方法和属性。
这些方法、属性可以帮我们获取元素，得到元素的属性值。
下面这张图，清晰的解释了AE中如何通过对象、对象的方法、属性来获取我们要操作的元素以及元素的 属性值。

thisComp.layer("矩形").transform.position 
对象(comp)	对象(layer)	对象(group)	属性

合成（comp\thisComp）是AE的基础，位于层级的最顶层称为全局对象，全局对象不需要作出任何指向说明。
不属于全局对象的对象就称为非全局对象，要使用非全局对象须指向它的上一级对象。
因此要获取对象的方法、属性就需要遵循以下层级结构：
**Comp Object> property**

**对象的类型**
AE中的对象有object（对象）和function（函数对象）两种类型。 
下图是用typeof检测AE中常见的对象的类型截图。

了解它们的类型，对于我们正确的调用其方法属性至关重要。

比如，有这样一个需求，需要将开启了3d开关的position属性[xy.z]中的[x.y]提取出来。

将slider control的值用toFixed()这个方法四舍五入取一位小数。

如何解决这个问题，等学了下节课你应该就会明白。

### 2_02 图层属性及属性值value

**图层的属性**
图层有很多属性，当你向图层添加效果、蒙版等，AE会将新的属性添加到时间轴面板中。

属性虽然很多，但无论任何类型的图层，都有一个Transform对象，包含以下属性
anchorPoint 中心点
position 位置
scale 缩放
rotation 旋转
opacity 透明度
除了摄像机图层跟灯光图层有些不同之外，其他的都一样。



以Position属性为例，Position是属性名，后面的蓝色值是属性值。
可以通过属性名直接获取属性值，属性名的第一个字母不能大写。



在同一个图层的属性之间，可以直接通过属性名关键字来获取到属性的值，不需要做出任何指向说明。 

**属性值value**
value返回属性当前的值。

 Anchor Point(中心点)value: 0,0
Position(位置)value: 900,500
...


Source Text的value就是默认输入的文字，这个值是个字符串，即使你输入的是数字，在进行算术运算 时需要考虑类型转换。

 **属性值value的类型**
ae中属性值的类型有以下几种：
Number 数字 Opacity、Rotation等 
String 字符串text的 Source Text 
Array 数组Position。Scale等

**属性、属性值value的区别**
属性看起来跟value的功能相同，其实两者是有差别的，属性跟value它们的类型不同。 
属性是个函数：

value是个对象：



### 2_03_常用方法、属性

AE中的元素主要有合成(Comp)、图层(layer)、素材(footage)这三种。
通过AE表达式语言菜单可以看到，除了Vector Math(适量数学)、Random Number(随机数)，
Interpolation(差值)、Color Conversion(颜色转换)，Other Math、javaScript Math这些通用的表达式 外，其他的表达式都是跟合成（Comp）、图层（layer）、素材（footage）相关的。

 **thisComp**
当前写有表达式的合成。大多时候我们都是在thisComp中进行操作，跨合成的表达式操作较少。



**comp(name)**
根据name获取合成。thisComp有的方法、属性，comp也有，

通过comp()可以在多个合成之间建立关联。比如，名为text的合成里有很多文字，可以通过：
comp("text").layer("置身于苦难与阳光之间").text.sourceText,将合成text里的文字在其他合成里 引用，这样便于集中管理。
**layer()**
layer(name),返回名为name的图层。因为layer不是全局对象，所以需要指向合成，多为thisComp。

**图层常用方法、属性**

```JAVA
// 图层 rect
thiacomp.layer(rect").sourceRectAtTime();	//用来获取元素的宽、高，左边界，上边界 
thiscomp.layer("rect").width;	//获取图层宽度，以像素为单位
thiscomp.layer("rect").height;//获取图层高度
thisComp.layer("rect").inPoint;	//获取图层的入点，以秒为单位
thiscomp.layer("rect").outPoint;//获取图层的出点
thiscomp.layer("rect").aampleImage();	//对图层的颜色和 alpha 通道值进行采样 thiscomp.layer("rect").anchorPoint;	//获取图层的锚点值
thiscomp.layer("rect"),tranaform.position;	//获取图层的位置
thiscomp.layer("rect").tranaform.scale;	//获取图层的缩放值，百分比thiscomp.layer("rect").transform.rotation;	//获取图层旋转值
thiscomp.layer("rect").transform.opacity;	//获取图层的不透明度值
thiacomp.layer("rect").parent.name;	//获取图层父图层的名字
```

 **footage**
获取外部导入的图片、声音、视频等。

```JAVA
//返回素材项目的持续时间（以秒为单位）
footage("music").duration 

//返回素材项目的名称
footage("music").name;
/返回素材项目的宽度（以像素为单位）

footage("pic").width;
//返回素材项目的高度（以像素为单位）

footage("pic").height;
```

**当前对象**
AE获取图层、属性的表达式看起来很繁琐，为了便于书写、记忆，AE提供了简化的对象写法。
比如：thisComp, thisLayer. thisProperty:
thisComp,当前合成 
thisLayer，当前写有表达式的图层，一般省略不写。

```JAVA
//当前图层，可以省略
thisLayer.position	//获取当前图层的位置属性，可简写为position。
```

thisProperty，当前写有表达式的属性，一般省略不写。
```JAVA
//以text的source Text为例
thisProperty.name;	//source Text,这时这里的thiaProperty就不能省略。
name；//获取的是图层的名称
```

### 2_04_index

index索引，表示元素在某一组排序中的位置。比如：26个字母abcdefg..
比如：书籍的章节第一章、第二章.图层的索引

**数组的索引**
AE中很多属性是数组，比如Position属性[640.360]，要访问这个数组的值，可以通过索引来访问。

**属性的索引**

上图中Anchor Point在Transform的第一位，我们就可以通过下面的表达式获取锚点。

