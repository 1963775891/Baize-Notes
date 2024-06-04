## 1、JS基础知识

### 1_01 **Js的保留关键字**

不可以用作变量、标签或者函数名。如：var、this、in、for、let、case等不能用做变量名。

#### **变量的命名规则**

- 以字母、下划线、$开头，不能用数字开头。
- 由字母、下划线、$或数字组成。
- 区分大小写。
- 不能使用关键字和保留字。

**注意**：变量名最好起有实际意义的英文或拼音，不要使用类似αa，bb之类的无意义的字符。

#### **注释**

注释用来解释JavaScript代码，它不参与代码的执行，可以帮助我们更好的理解代码。

```javascript
//单行注释以英文状态下//开头，任何位于//之后的不换行文本都会被JavaScript忽略（不会执行）。

var name = "华安"; // 定义名称
var num = 9527;    // 定义编号
```

```javascript
//多行注释以/*开头，以*/结尾，位于其中的文本都不会被执行。

/*
作者：比邻课堂
QQ:554579800
*/
```

### 1_02 变量数据类型及转换

#### **变量的数据类型**

常见的数据有以下几种：

```javascript
//字符串（string）
var name = "王大气";

//数字(Number)
var age = 18;

//数组(Array)
var hobby = ['旅游', '追剧', '服装设计'];

//布尔(Boolean)
var iFlag = true;	//只能有两个值：true 或 false

//对象（Object）
var obj = {};
```



#### **AE中常用到的三种数据类型：**

**字符串，**是插入到成对的单引号或双引号任意字符，用于存储和处理文本。

**数字，**整数、小数、0、负数都是数字。数字不需要放在引号中间，如果放在引号中间就成了字符串。

**数组，**不涉及到类型转换，后面我们再详细说明。

#### **typeof类型检测**

typeof操作符用来检测变量的数据类型。

```javascript
//在文本层的源文本属性写如下表达式进行测试：

name = "王大气";
typeof name; // string
age = 18;
typeof age; // number
typeof false; // boolean

//在js中，数组是一种特殊的对象类型。因此 typeof [12,3,4] 返回object

arr = [1,2,3,4];
typeof arr; // object

//个没有值的变量会返回undefined

typeof b; // undefined
```

#### **变量数据类型转换**

##### js中数据类型转换有三种

```javascript
//将字符串str转为数字：

Number(str); // str必须为纯数字的字符串

//将数字num转为字符串：

String(num)

//将字符串、数字转换为布尔值：

Boolean()
```

##### **ae中最常见的就是数字和字符串的相互转换**

```javascript
//一些会用到的类型转换方法：

num.toString()：//将数字num转为字符串。

num.toFixed(n)：//把数字num转换为字符串，并四舍五入显示n位小数。

parseInt(str)：//把字符串转为一个整数，字符串必须以数字开头。

parseFloat(str)：//把字符串转为一个浮点数，字符串必须以数字开头。

"0" + 5; // 字符串，字符串+数字得到字符串

"5" - 1; // 数字，字符串-数字，得到数字
```

### 1_03_字符串

字符串是插入到成对的单引号或双引号中的任意字符，用于存储和处理文本。

```javascript
var a = "王大气";
var b = "18";
var c = "Hello World!";
var d = "[1,2,3,4]";
var e = "It's my book!";
var f = "It's mybook！"; // 报错，AE中不会提示错误，就直接不显示字符串内容

//当数字放到引号中间的时候，它的类型就是字符串类型，不是数字类型了，如果要进行运算，需要进行类型转换。

var X="10"；
var y=24；
x +y;	//1024
Number (x)+y；	//34
```



#### **特殊字符**

反斜杠（\）用来在字符串中插入单引号、双引号、换行符、反斜杠等特殊字符

```javascript
//\'插入单引号
'it\'s ok';

//\"插入双引号
"中国是瓷器的故乡，因此china与\"China（中国）\"同名。"

//\n插入换行符
"王大气\n王漂亮";

//\\插入反斜杠
“汤米\\杰瑞”
```

#### **字符串长度**

length属性，用于获取字符串的长度，空格也算。

```javascript
var a = "比邻课堂";
a.length; // 4

var b = "比邻课堂";
b.length; // 7
```

#### 分割：split()

split(separator,howmany)方法用于把一个字符串分割成字符串数组。

separator，分隔符，可以是字符串也可以是正则表达式，指定字符串分割的位置。

howmany，指定返回的字符串数组最大长度。

```javascript
str = "hello";
str.split(""); // [h,e,l,l,o]

//在匹配的位置分割：
str = "hello";
str.split("l"); // [he,o]

str = "hello";
str.split("", 2); // [h,e]

//从-的位置把字符串分割成字符串数组
str = "1995-06-02";
str.split("-"); // [1995, 06, 02]
```

#### **slice()**

slice(start,end)，方法提取字符串指定部分，并把被提取的部分以新的字符串返回。新的字符串包括start，不包括end。

字符串中第一个字符位置为0，第二个字符位置为1，以此类推。

```javascript
//返回1-6之间的字符，不包含6
txt = "hello,world!";
txt.slice(1,6); // "ello,"

//返回第6位以后的所有字符
txt = "hello,world!";
txt.slice(6); // "world!"

//如果参数为负数，则从后往前返回对应个数的字符
txt = "hello,world!";
txt.slice(-2); // d!
```

#### **toUpperCase()**

把字符串转换为大写。

```javascript
str = "Hello,World!";
str.toUpperCase(); // "HELLO,WORLD!"
```

#### toLowerCase()

把字符串转换为小写。

```javascript
str ="Hello,World!
str.toLowerCase();	//hello,world!
```

#### repeat()

str.repeat(n)，将字符串复制n次。

```javascript
//新建一个文本图层，给源文本属性添加表达式
var str = "8";
// 定义一个字符串
str.repeat(3); // 将这个字符串重复3次，结果为：888
```

```javascript
// 新建一个文本层，随便输一个数字，比如0，然后添加表达式
text.sourceText.repeat(8); // 00000000
```

#### charAt()

返回指定位置的字符。第一个字符位置为0，第二个字符位置为1,以此类推。

```javascript
var str = "Hello,World!";
var n = str.charAt(1); // e
```

#### fromCharCode()

将Unicode编码数字转为字符（字母）。

```javascript
String.fromCharCode(65); // A

// 随机生成26个英文字母
posterizeTime(10);
n = Math.round(random(65, 90));
String.fromCharCode(n)
```

#### 创建数组

```javascript
// []里的任意字符，如果是数字可以不用引号
var cars = ["保时捷", "奥迪", "布加迪"];
var num = [1, 2, 3, 4];
```

#### 访问数组

通过索引来访问某个数组元素，数组的索引是从0开始的。

```javascript
var cars = ["保时捷", "奥迪", "布加迪"];
cars[0] // 保时捷
cars[1] // 奥迪
cars[2] // 布加迪
```

#### 获取数组长度

```javascript
var cars = ["保时捷", "奥迪", "布加迪"];
cars.length // 3
```

ae中位置[x,y,z]、缩放[x,y,z]、颜色[red,green,blue,alpha]等都是以数组的形式存在的。

```javascript
position[0]; // 获取x坐标
scale[1];  // 获取高度
color[2];  // 获取blue数值
```

#### 获取数组中最大值

```javascript
var arr = [12, 5, 77, 89, 2, 99, 520, 88];
Math.max(...arr); // 520
```

ES6的扩展运算符，可以将数组转换为以逗号隔开的参数的形式，这样就可以很方便的通过Math.max获取到最大值。

#### push()

push()，向数组的末尾添加一个或多个元素，并返回新的数组长度。

```javascript
cars = ['迈凯轮', "布加迪威龙'];
cars.push('迈巴赫', '帕加尼');	// 4
cars; // ['迈凯轮', '布加迪威龙', '迈巴赫', '帕加尼']
```

#### splice() 

方法用于添加或删除数组中的元素，并返回除被删除元素以外的其他元素的数组。
该方法会改变原数组。

```javascript
var arr = [1,2,3,4,5,6,7,8,9,10];
// 删除第1位元素以后的所有元素，并返回
arr.splice(1); // 2,3,4,5,6,7,8,9,10
arr:
// 删除从第2位元素开始往后数4位的所有元素，并返回
arr.splice(2,4); // 3,4,5,6
// 删除从第2位元素开始往后数4位的所有元素，并在被删除元素位置添加新元素a，b
arr.splice(2,4,"a","b");
arr // [1,2,a,b]

// 从后往前返回指定数位的元素，参数为负数只能传一个参数
arr.splice(-1); // 10
```

map()方法返回一个新数组，新数组中的元素为原始数组元素调用函数处理后的值。

```javascript
// 获取元素的Position（位置），得到一个数组
p = thisComp.layer("rect").transform.position.value;

// 将数组中的元素取整
p.map(function(item) {
    return item.toFixed(0)
})
```

#### join();

join()方法可以将数组转换为字符串，并可以指定分隔符，如果任何参数都不传默认逗号分隔。

```javascript
var arr = ["a", "b", "c", "d", "e"];
arr.join(); // a,b,c,d,e
arr.join(""); // abcde
arr.join("_"); // a-b-c-d-e
typeof arr.join(); // string
```

#### toString()

toString()方法可以将数组转为字符串。

```javascript
arr = ["hello", "520", "比邻课堂"];
typeof arr;
// Object
Array.isArray(arr); // true
typeof arr.toString(); // string
```

### 1_05_函数

函数就是一段写在中的可重复使用，用来完成特定功能的代码块。

**如何定义函数**

```javascript
function fnName01 {
    // 执行代码
}

function a()｛
	return 2+1;
｝
```

**如何调用函数**
函数会在被调用的时候执行。调用函数只需在函数名后加上()即可。

```javascript
function a()
{
    return 2+1;
}
a(); //调用函数
```

**注意：AE中函数需要先定义才能调用，也就是函数定义要写在函数调用之前。**

#### 带参数的函数

定义函数的时候可以给函数传递参数，这个参数可以在函数中使用。

function fnName(参数1, 参数2...)
{
    // 执行代码
}
fnName(参数1, 参数2);

```javascript
function a(n1, n2)
{
    return n1 + n2;
}
a(8, 8); // 16
```

```javascript
//补0函数
function addzero(n) {
    if(n < 10) {
        return "0" + n;
    } else {
        return n;
    }
}
addzero(Math.round(time)）;
```

### 1_06_对象

一切皆对象，在JavaScript中，对象是拥有属性和方法的数据。
属性是与对象相关的值。
方法是能够在对象上执行的动作。

#### **现实中的对象**

```javascript
// 现实中车、手机、人都可以看成对象，它们都有各自的属性跟方法。比如：隔壁老王
属性：
性别、年龄、身高、体重等
方法：
吃饭、睡觉等

1. 访问对象属性：
   laowang.sex = "男"
   laowang.age = "28"

2. 访问对象方法
   laowang.eat()
   laowang.sleep()
```

#### **js中的对象**

```javascript
var people = {
    name: "老王", // 属性
};

age: "28".
属性
sex: 男.
// 属性
sleep:function() {
    // do something
}
jobs:{
    // 对象是可以嵌套的，对象可以作为其他对象的属性
    job1: "司机",
    // 属性
    job2: "摄影师"
    // 属性
}
// 获取姓名
people.name; // 老王
people["name"]; // 老王
// 获取第一个职业
people.jobs.job1;
jobs.job1: // 报错，jobs不是顶级对象，需要指向其父级
// 对象是可以嵌套的（对象可以作为其他对象的属性）
// 非顶级对象，访问时需要指向其父级
// 比如ae中获取图层A，需要指定其父级合成：
thisComp.layer("A");
layer("A"); // 报错
```

#### **获取对象的属性键名和键值**

Object.keys(obj)，返回对象属性的键名，返回结果为数组。
Object.values(obj)，返回对象属性的键值，返回结果为数组。
**注意：**在AE中要通过Object.keys(obj)和Object.values(obj)返回相关值，需要将表达式引擎切换为JavaScript，否则AE不支持这种写法（AECC2019，高版本未测试）。
点击文件-项目设置-表达式将表达式引擎切换为JavaScript。

```javascript
obj = {
    "name": "若比邻",
    "sex": "男",
    "age": 18
};

/*
"name"就是属性键名
“若比邻”就是属性键值
*/
Object.keys(obj); // name, sex, age
Object.values(obj); // 若比邻, 男, 18
```

### 1_07_if条件语句&for循环语句

#### if条件语句

if条件语句是基于不同的条件来执行不同的动作的。

#### if语句

if(condition) { // 当条件为true时执行的代码 }

```javascript
if(下雨) {
	“出门带伞”
}
/*
这条语句表明：如果下雨就带伞，但是没有指明，没下雨就不带伞，所以当天晴的时候，这条语句是没有返回值的，在AE中是会报错的。
*/
```



#### if...else语句

if(condition) { // 当条件为true时执行的代码 }else { // 当条件为false时执行的代码 }

```javascript
score = 80;
if(score > 60) {
    "及格"
} else {
    “不及格”
}
```

#### if...else if...else语句

用来在多个代码块中选择条件成立的来执行。

```javascript
time = 15;
if (time <= 10) {
    “早上好”，
} else if (time <= 14) {
    “中午好”；
} else if(time <= 18) {
    “下午好”；
} else {
    “晚上好”；
}
```

```javascript
// ae不支持下面这种写法
// 也就是10<n<80这种写法
if(10 < n < 80) {
//     //do something
}
```

#### for循环语句

for(语句1; 语句2; 语句3) {
    // 需要执行的代码
}
**语句1** 循环开始前执行，定义一个数字变量，通常为0；
**语句2** 定义运行循环的条件；
**语句3** 在花括号中的代码被执行一次之后执行，通常是语句1定义的数字变量的累加。

```javascript
// 将下面表达式添加到文本的sourceText，代码会执行4（数组的长度）遍
cars = ['阿斯顿马丁', '迈凯轮', '帕加尼', '迈巴赫'];
for(i=0; i<cars.length; i++) {
    car += cars[i] + '\n';
}
/*
阿斯顿马丁，
迈凯轮，
帕加尼，
迈巴赫
*/
```

### 1_08_运算符

#### **算术运算符**

```javascript
+  加法	3+5 	// 8
    "3" + 5	 // "35"

-  减法	5 - 3 	// 2
	8-“5”	//3

*  乘法	3*5 	// 15

/  除法	4 / 2 	// 2

%  取模(余数)5%2 	// 1

++ 自增	++5	//6先加1	5++，下一次加1，多用在for循环中

-- 自减	--5 // 5
```

**注意：**
1、一个字符串加一个数字，或者两个字符串相加的时候，相当于字符串拼接，将多个字符串拼接成一个字符串。
2、加减乘除运算存在隐式类型转换的情况，在计算时要弄清楚参与计算的元素类型。
3、加减乘除运算存在精度问题，比如：0.1+0.2=0.3000000000004，0.3-0.1=0.1999999999999，在计算中需要修正。

以下是根据您提供的图片内容，以Markdown格式排版的文字：

#### 赋值运算符

```javascript
=	X = 5	// 将右侧的值赋给左侧的变量，它是最简单最常用的运算符
+=	x += 5	x = x + 5	// 加法运算或连接操作并赋值
-=	x -= 5	x = x - 5	// 减法运算并赋值
*=	x *= 5	x = x * 5	// 乘法运算并赋值
/=	x /= 5	x = x / 5	// 除法运算并赋值
%=	x %= 5	x = x % 5	// 取模运算并赋值
```

= 等号，在js中表示赋值，比如 x=5，将5赋值给x。

#### 比较运算符

```javascript
==	等于	5 == 5 // true
		"5" == 5 // true
===	绝对等于（值和类型均相等）	5 === "5" // false
!=	不等于
>	大于
<	小于
>=	大于或等于
<=	小于或等于
```

#### **逻辑运算符**

逻辑运算符用于判定变量或值之间的逻辑关系。

```javascript
&&	与	// 符号两侧的条件都必须为true，它的结果就为true
||	或	// 符号两侧的条件只要一个为true，它的结果就为true
!	非	// 取反，当a为true时，!a就为false

a = 15;
b = 5
if(a > 10 && b > 10) {
  a + b
} else {
  a
}
```

#### 三目运算符

三目运算符是if...else条件语句的简化版，合理的使用能够简化我们的代码。

```javascript
/*
条件语句成立，返回值1/执行操作1，否则返回值2/执行操作2
等同于 if (条件) {操作1} else {操作2}
*/
a = 5;
b = 8;
a > b ? "大于" : "小于";
// 等同于
if(a > b) {
  "大于"
} else {
  "小于"
}	// ae中表达式书写的地方空间小，在有多个判断时，可以减少代码的行数。
```

#### 运算符优先级

下表按从最高到最低的优先级列出JavaScript运算符，具有相同优先级的运算符按从左至右的顺序求值。

| 运算符  | 描述                           |
| ------- | ------------------------------ |
| */ %    | 乘法、除法、取模               |
| +-+     | 加法、减法、字符串连接         |
| <<= >>= | 小于、小于等于、大于、大于等于 |
| &       | 按位与                         |
| \|      | 按位或                         |
| &&      | 逻辑与                         |
| \|\|    | 逻辑或                         |
| ?:      | 条件                           |

```javascript
// time * 200 然后结果跟 100 进行取模运算
	time * 200 % 100;
// time 先跟 200 进行取模运算，结果再乘以 100
	time % 200 * 100;
```

### 1_09_常用方法和函数

#### **Math.round()**

Math.round(n)，把n四舍五入为最接近的整数。

```javascript
Math.round(3.4); // 3
Math.round(-2.6); // -3
Math.round("3.14"); // 3 数字字符串也可以进行转换
```

#### **Math.floor()**

Math.floor(n)，向下取整，返回小于等于n的最大整数。

```javascript
Math.floor(3.9); // 3
Math.floor(-3.9); // -4
```

#### **Math.ceil()**

Math.ceil(n)，向上取整，返回大于等于n的最大整数。

```javascript
Math.ceil(3.9); // 4
Math.ceil(-3.9); // -3
```

#### **Math.sin()**

Math.sin(n)，返回数字n的正弦值，返回值在-1到1之间。

```javascript
Math.sin(45); // 0.850903
```

#### **Math.cos()**

Math.cos(n)，返回数字n的余弦值，返回值在-1到1之间。

```javascript
Math.cos(45); // 0.525321
```

#### **Math.atan2()**

返回-PI到PI之间的值，是从X轴正向逆时针旋转到点(x,y)时经过的角度的弧度值。

```javascript
// 指定一个坐标（x，y），坐标值（4，8），使用atan2()方法计算坐标与X轴之间的角度的弧度
// 如下实例：
Math.atan2(8, 4); // 1.1071487177940904
```

#### **Math.tan()**

Math.tan(n)，返回数值n的正切值，表示一个角（单位：弧度）
// 正切值是指是直角三角形中，某一锐角的对边与另一相邻直角边的比值。

```javascript
Math.tan(1); // 1.5574077246549023
```

#### **Math.exp()**

Math.exp(n)，返回e的n次幂的值，e代表自然对数的底数，其值近似为2.71828。

```javascript
Math.exp(-5) = 0.006737947
Math.exp(-4) = 0.01831564
Math.exp(-3) = 0.04978707
Math.exp(-2) = 0.135335
Math.exp(-1) = 0.367879
Math.exp(0) = 1
```

#### **Math.abs()**

Math.abs(n)，返回n的绝对值。

```javascript
Math.abs(-1); // 1
Math.abs(-3.5); // 3.5
```

#### **Math.sqrt()**

Math.sqrt()方法返回一个数的平方根。

```javascript
Math.sqrt(9); // 3
Math.sqrt(2); // 1.414213562373095
Math.sqrt(0); // 0
Math.sqrt(-1); // NaN
```

#### **Math.pow()**

Math.pow(x, y)，返回x的y次幂的值。

```javascript
Math.pow(2, 3); // 8
Math.pow(-2, 4); // 16
Math.pow(-2, 3); // -8
```

#### **Math.max()**

Math.max(value1, value2) 返回指定值中最大的值。

```javascript
Math.max(10, 99); // 99
```

#### **Math.min()**

Math.min(value1, value2) 返回指定值中最小的值。

请注意，由于图片内容可能存在格式问题或不清晰，以上内容是根据您提供的图片文字尽可能准确地转录的。如果有任何错误或遗漏，请告知我进行修正。

```javascript
Math.max(10, 99); // 99  
```

#### **Math.PI**  

返回圆周率π（约等于3.1415926）  

```javascript
Math.PI;  // 3.1415926  
```

#### **toFixed()**  

n.toFixed(num); // 把n四舍五入为指定小数位数的数字，如果省略了参数num，则用0代替。  

```javascript
3.1415924.toFixed(2);  // 3.14  
3.1415924.toFixed();  // "3"，这个3是个字符串，再进行运算，需要类型转换  
```

#### **Number()**  

Number(n)，将参数n转为数字，n必须是字符串类型的数字。  

```javascript
str = "10";  
str + 10;	// "1010"  
Number(str) + 10;	// 20  
```

#### **parseInt()**  

parseInt(str)，将字符串str转为整数，这个字符串必须以数字开头，或者本身就是数字字符串。  

```javascript
parseInt("3.14");  	// 3  
parseInt("hello1995");  	// NaN  
parseInt("-3.14");  	// -3  
```

#### **eval()**  

eval(string) 函数可将参数字符串作为脚本代码来执行。  
参数是表达式或者js语句。  

```javascript
str = "x=10;y=20;x+y";  
eval(str); // 30  
```

eval()函数在js中用的不多，在AE表达式中也仅仅是在加载外部.txt文件那个案例中会用到。

### 1_10_try...catch语句  

try...catch用来测试处理代码中可能出现的错误。  try部分包含需要运行的代码，catch部分包含错误发生时运行的代码。  

```javascript
try
{
	// 需要运行的代码  
}
catch(err)  
	// 错误发生时运行的代码
}

// 以text的sourceText为例  
try{ 
	value.toFixed(1);	// text的SourceText的value是个string类型，没有toFixed()方法。
    }
catch(err){
	value  
}
```



### 1_11_for in  

for...in语句用于遍历数组或者对象的属性（对数组或者对象的属性进行循环操作）。  

```javascript
// for in遍历数组  
//新建一个文本图层，给源文本属性添加如下表达式  
// ctr1+d复制5个图层，就会将数组中的值输出到5个图层  
arr = ["比邻课堂", "欢迎关注", "若比邻", "表达式", "王大气"];  
for(index in arr){ 
arr[index - 1]  
} 

// for in遍历对象  
// 新建一个文本图层，给源文本属性添加如下表达式，就会输出对象的值  
obj = {  
  "若比邻"  
  "sex": "男"  
  "age": 18  
};  
result = "";  
for(i in obj){
	result += obj[i];  
}  
```



### 1_12_while循环  

while循环会在指定条件为真时循环执行代码块。  

```javascript
// 语法  
while（条件）{ 
	需要执行的代码  
} 

// 当字符长度小于4的时候，在前面补零  
n = "88";  
while(n.length < 4){ 
	n = "0" + n; 
} 
```



## 2、常用表达式  

### 2_01AE中的对象  

**对象、方法、属性的理解**  
AE中Comp、thisComp、Layer、Solid、Light、Footage等都是对象，它们都有各自对应的方法和属性。



#### AE中的comp、layer、property

AE中的对象和函数：

```javascript
// 示例：
thisComp.layer("Shape Layer 1").transform.position[0]
thisComp.layer("Shape Layer 1").content("Rectangle 1").content("Fill 1").color[0];
```

这些方法、属性可以帮我们获取元素，得到元素的属性值。

下面这张图，清晰的解释了AE中如何通过对象、对象的方法、属性来获取我们要操作的元素以及元素的
属性值。

![](D:\Baize_Notes\JS基础知识\image1.jpg)

合成(comp叭thisComp)是AE的基础，位于层级的最顶层称为全局对象，全局对象不需要作出任何指向说明。
不属于全局对象的对象就称为非**全局对象**，要使用**非全局对象**须指向它的**上一级对象**。
因此要获取对象的方法、属性就需要遵循以下层级结构：

**Comp > object > property**

```javascript
//比如：
thisComp.layer("Shape Layer 1").transform.position[0]

thisComp.layer("Shape Layer 1").content("Rectangle 1").content("Fill 1").color[0];

layer("Shape Layer 1").transform.position[0];//报错
```

对象的类型
AE中的对象有object（对象）和function（函数对象）两种类型。
下图是用typeof检测AE中常见的对象的类型截图。

![](D:\Baize_Notes\JS基础知识\image2.jpg)

了解它们的类型，对于我们正确的调用其方法属性至关重要。

比如，有这样一个需求，需要将开启了3d开关的position.属性[x,y,z]中的[x,y]提取出来。

![](D:\Baize_Notes\JS基础知识\image3.jpg)

```javascript
//名为rect的形状图层开启了3d开关
p=thisComp.layer("rect").position；

p.slice(0,2)；//这里会报错，类型为function的position没有slice（）,这个方法。
```

将slider control的值用toFixed()这个方法四舍五入取一位小数.

![](D:\Baize_Notes\JS基础知识\image4.jpg)

```javascript
s = effect("Slider Control")("Slider");
s.toFixed(2);	// 报错，slider control 没有toFixed()这个方法
```

### 2_02_图层属性及属性值value

**图层的属性**
图层有很多属性，当你向图层添加效果、蒙版等，AE会将新的属性添加到时间轴面板中。属性虽然很多，但无论任何类型的图层，都有一个Transform对象，包含以下属性：anchorPoint	中心点
position	位置
scale	缩放
rotation	旋转
opacity	透明度
除了摄像机图层跟灯光图层有些不同之外，其他的都一样。

以Position属性为例，Position是属性名，后面的蓝色值是属性值。可以通过属性名直接获取属性值，**属性名的第一个字母不能大写**。

```javascript
// position
position;	// 获取position的值，比如[800，600，0]；
position[0]；	// 800
position[1];	// 600
position[2];	// 0

position + [100，100]；

// anchorPoint
anchorPoint + [100，100，0]；
opacity;	//不透明度
scale;	//宽高
rotation;	//旋转
```

在同一个图层的属性之间，可以直接通过属性名关键字来获取到属性的值，不需要做出任何指向说明。

**属性值value**
value返回属性当前的值。

![](D:\Baize_Notes\JS基础知识\image7.jpg)

Anchor Point （中心点） value： 0， 0
Position（位置）value： 900， 500

```javascript
//给position添加表达式，默认值为[900， 500]
value + [100，100]；	//结果为[1000，600]

value[0]；	//900
value[1]；	//500
```

Source Text的value就是默认输入的文字，这个值是个字符串，即使你输入的是数字，在进行算术运算时需要考虑类型转换。

![](D:\Baize_Notes\JS基础知识\image8.jpg)

```javascript
value+"比邻课堂";	//结果：欢迎关注比邻课堂
//如果不加value，就会替换掉默认的值

//比如默认输入数字10，然后给value + 10，这里相当于字符串拼接
value+10;	//1010
```

**属性值value的类型**
ae中属性值的类型有以下几种：
Number数字Opacity,Rotation等
String 字符串 text的 Source Text
Array数组Position, Scale等

```javascript
//可以用typeof测试

typeof position[0]；	// Number
typeof position.value[0]；	// Number

typeof text.sourceText.value;	// String

typeof position;	//数组，function 函数对象
typeof scale;	//数组，function 函数对象
```

**属性、属性值value的区别**
属性看起来跟value的功能相同，其实两者是有差别的，属性跟value它们的类型不同。

属性是个函数

![](D:\Baize_Notes\JS基础知识\image9.jpg)

value是个对象：

![](D:\Baize_Notes\JS基础知识\image10.jpg)

```javascript
//有时候我们开启了图层的3d开关，position属性多了一个z轴的值，但是我们却只需要x， y轴的值，这个时候就需要将x，y从[x，y，z]中提取出来
thiscomp.layer("形状图层").transform.position.splice(0,2);	// 报错

thiscomp.layer("形状图层").transform.position.value.splice(0,2);	// [800,600]
//position 能得到一个数组[800，600，0]，但是position是一个function，它没有splice（）方法，所以这里需要position.value
```



### 2_03_常用方法、属性

AE中的元素主要有合成（Comp）、图层（layer）、素材（footage）这三种。

通过AE表达式语言菜单可以看到，除了Vector Math（适量数学）、Random Number（随机数），Interpolation（差值）、Color Conversion（颜色转换）， Other Math， JavaScript Math这些通用的表达式外，其他的表达式都是跟合成（Comp）、图层（layer）、素材（footage）相关的。

![](D:\Baize_Notes\JS基础知识\image11.jpg)

**thisComp**
当前写有表达式的合成。大多时候我们都是在thisComp中进行操作，跨合成的表达式操作较少。

```javascript
// 合成常用属性、方法

thisComp.width;	// 返回当前合成的宽度

thisComp.height;	// 返回当前合成的高度

thisComp.bgcolor;	// 返回当前合成的背景色 [0，0，0，1] rgba a表示透明度

thisComp.numLayers;	// 返回当前合成中的图层数

thisComp.duration;	// 返回合成持续时间（以秒为单位）

thisComp.frameDuration;	//返回帧持续时间（以秒为单位）合成帧率为25，那么frameDuration为1/25

thisComp.name;	//返回当前合成的名称

thisComp.layer(1).name;	//获取图层1的名称

//AE表达式没有直接获取帧率frame rate的属性或方法，可以通过frameDuration计算
thisComp.frameDuration;	// 0.04

//那么帧率就等于
1/thisComp.frameDuration;	//25

Math.floor（（time / thisComp.frameDuration）/8）；	//每8帧改变一次，需要几帧就将8改成几
```

**comp(name)**
根据name获取合成。thisComp有的方法、属性，comp也有，

```javascript
// 获取名为text的合成。
comp ("text");
```

通过comp0可以在多个合成之间建立关联。比如，名为text的合成里有很多文字，可以通过：
**comp（“text”）.layer（“置身于苦难与阳光之间”）.text.sourceText**，将合成text里的文字在其他合成里引用，这样便于集中管理。

![](D:\Baize_Notes\JS基础知识\image12.jpg)

**layer()**
layer（name），返回名为name的图层。因为layer不是全局对象，所以需要指向合成，多为thisComp。

```javascript
//如果存在重复的名称，则AE将使用“时间轴”面板中第一个的（最上面的）名称
thisComp.layer（"比邻课堂"）；//获取名为“比邻课堂”的图层。
```

**图层常用方法、属性**

![](D:\Baize_Notes\JS基础知识\image13.jpg)

```javascript
// 图层 rect
thisComp.layer("rect").sourceRectAtTime();	//用来获取元素的宽、高，左边界，上边界
thiscomp.layer（“rect”）.width；	//获取图层宽度，以像素为单位
thisComp.layer（“rect”）.height；	//获取图层高度
thisComp.layer（“rect”）.inPoint；	//获取图层的入点，以秒为单位
thiscomp.layer（“rect”）.outPoint；	// 获取图层的出点
thisComp.layer（“rect”）.sampleImage（）；	// 对图层的颜色和 alpha 通道值进行采样
thisComp.layer("rect").anchorPoint;	//获取图层的锚点值
thiscomp.layer（“rect”）.transform.position；	// 获取图层的位置
thiscomp.layer("rect").transform.scale;	//获取图层的缩放值, 百分比.
thisComp.layer("rect").transform.rotation;	//获取图层旋转值
thisComp.layer（“rect”）.transform.opacity；	//获取图层的不透明度值
thisComp.layer("rect") .parent.name;	//获取图层父图层的名字
```

**footage**
获取外部导入的图片、声音、视频等。

```javascript
//返回素材项目的持续时间（以秒为单位）
footage ("music") .duration

// 返回素材项目的名称
footage ( "music") .name;

//返回素材项目的宽度（以像素为单位）
footage ("pic").width;

//返回素材项目的高度（以像素为单位）
footage ("pic") .height;
```

当前对象
AE获取图层、属性的表达式看起来很繁琐，为了便于书写、记忆，AE提供了简化的对象写法。
比如, thisComp, thisLayer, thisProperty;
thisComp，当前合成；
thisLayer，当前写有表达式的图层，一般省略不写。

```javascript
//当前图层，可以省略
thisLayer.position	//获取当前图层的位置属性，可简写为position。
```

thisProperty，当前写有表达式的属性，一般省略不写。

```javascript
//以text的source Text为例
thisProperty.name;	// Source Text，这时这里的thisProperty就不能省略。

name;	//获取的是图层的名称
```



### 2_04_index

index 索引，表示元素在某一组排序中的位置。
比如：26个字母 abcdefg...
比如：书籍的章节 第一章、第二章...

**图层的索引**
layer（index），返回指定索引的图层。

![](D:\Baize_Notes\JS基础知识\image14.png)

AE时间轴面板中的图层都有一个编号，这个编号就是它的索引值，通过这个值就可以获取到该图层。

```javascript
thisComp.layer（1）；//获取当前合成中的第一个图层。

//除了可以直接使用索引，还可以对索引通过表达式计算获取指定的图层。
//当只有一个图层时， index82不等于0，会报错，所以这里需要进行容错处理。
try{
	if（thisComp.layer（index82==0））{	//获取偶数图层，将其旋转index*30度
		30；
		｝
else
	｛
		0
	｝
｝
catch(err){
	0
｝
```

**数组的索引**
AE中很多属性是数组，比如Position属性 [640，360]，要访问这个数组的值，可以通过索引来访问。

```javascript
p=[640， 360]；

p[0]；	// 640
p[1];	// 360
```

**属性的索引**

![](D:\Baize_Notes\JS基础知识\image15.jpg)

上图中Anchor Point在Transform的第一位，我们就可以通过下面的表达式获取锚点。

```javascript
thisComp.layer(1).transform(1);
```

获取Anchor Point属性的x坐标值：

```javascript
thisComp.layer(1).transform(1) [0];
// 这种写法看着不直观，无法一眼确认获取的是那个值，一般不用这种写法。
```

Anchor Point在Trannsform中第一位，索引值是1，那position就是2， scale就是3， rotation就是4，opacity就是5，像下面这样。

```javascript
thisComp.layer(1).transform(1);	// Anchor Point value
thisComp.layer(2).transform(2);	// Position value
thisComp.layer(3).transform(3）；	// Scale value
thisComp.layer(4).transform(4);	// Rotation value
thisComp.layer(5).transform(5);	// Opacity value
```

然而，缩放、旋转、不透明度得到的都是0。

```javascript
thisComp.layer("Shape Layer 1").transform(3);	//0
thisComp.layer("Shape Layer 1").transform(4);	//0
thisComp.layer("Shape Layer 1").transform(5);	//0
```

**propertyIndex**
获取某个属性的索引值。

```javascript
thisComp.layer("solid").transform.scale.propertyIndex;	// 6
thisComp.layer("solid").transform.rotation.propertyIndex;	//10
thisComp.layer("solid").transform.opacity.propertyIndex	// 11
//就可以通过获取缩放属性
thisComp.layer("solid").transform(6);
```

**关键帧的索引**
当添加关键帧以后，AE会自动给关键帧生成一个数字编号，这个编号可以作为关键帧的索引，它从1开始，最大为关键帧的个数。

可以通过key（index）方法获取指定索引的关键帧。

```javascript
//获取position的第三个关键帧对应的x坐标
transform.position.key（1）.value[0]；
```



### 2_05_time

time，获取时间指针当前所对应的时间，单位是秒。

![](D:\Baize_Notes\JS基础知识\image17.jpg)

在不做任何数学运算的时候， time的最小值为0，最大值为合成的时间长度。

![](D:\Baize_Notes\JS基础知识\image18.jpg)

合成的总时长为10秒，得到的结果却是9.96，这是因为time是从0开始的，就跟数组的下标一样，比总时长少1帧。



#### **time的数据类型**

用typeof检测time的类型为Number。那么就可以直接对time进行加、减、乘、除、取模等运算。

```javascript
// Source Text
typeof time;	//Number

time + 2;
time - 1;
time * 30;	//常用
time / 2;
time % 2;	//循环，两秒一次时间循环
```

帧率为25时每帧之间相差1/25—0.04，这是一个非常小的值，在实际使用时一般会给它乘一个数字以增加属性的改变速度。

```javascript
// 以Rotation旋转属性为例
time;	//每帧旋转0.04度（帧率为25），每秒旋转1度
time * 30;	// 每秒旋转30度
```

#### **time的精度问题**

当合成的帧率为24、30等的时候time会显示为小数点后一长串数字。
当合成的帧率为25时，time显示为小数点后2位数字。

![](D:\Baize_Notes\JS基础知识\image20.jpg)

![](D:\Baize_Notes\JS基础知识\image21.jpg)

当time进行加减乘除运算时，运算结果有时也会显示一长串数字。

![](D:\Baize_Notes\JS基础知识\image22.jpg)

造成这个问题的原因是，二进制跟十进制转换引起的精度问题。
因此，在用time做一些需要显示数字的案例时，就要对time取整或者小数点位数进行控制。

#### **time取模运算**

通过time取模运算，循环缩放矩形形状图层。

```javascript
/*
	1、新建一个矩形形状
	2、按s展开缩放属性，添加如下表达式，按空格键预览
*/
if(time % 2 < 1){
	s=time % 1 * 100;
}
else
{
	s=100 - time % 1 * 100;
}

[s,s]
```

#### **time乘以负数**

以Rotation旋转属性为例。

```javascript
// 给旋转属性添加表达式
time * 60;	//表示顺时针每秒旋转60度
time * -60;	//表示逆时针每秒旋转60度
```



### 2_06_wiggle()

#### **语法**

**wiggle(freq, amp, octaves=1, amp_mult=.5, t=time)**
freq 频率，每秒抖动的次数。
amp振幅，每次抖动的幅度，如果设为20，那么这个振幅就在—20到20之间。
octaves意思是八度音、倍频程，在ae中表示振幅幅度，每次在振幅的基础上再进行一定的抖动，一般很少用。
amp_mult 频率倍频，默认为0.5不需要修改。
t= time 持续时间，抖动时间为合成时间，单位为秒，一般默认即可。

#### **单独抖动**

position等属性的值是数组，抖动都是在x、y方向进行，那如何单轴向抖动呢？

以位置属性X轴抖动为例，这里wiggle0抖动的结果是个数组，只要获取数组的第一个值，就实现了X轴的抖动。

```javascript
w= wiggle（1，200） [0]；
[w, 540]

//也可以这样写
wiggle(1,200);
[w[0], 540]
```

#### **逐渐停止抖动**

实现原理：让抖动的幅度逐渐变小直到为0。

```javascript
//将下面表达式添加到位置属性
wiggle(5, 800/Math.exp(time*2));
```

在指定时间段抖动

```javascript
if（time>3 && time <4）{
	wiggle (20,200)
}
else
{
	value;
}
```

你也可以把抖动的频率或者振幅绑定到slider control上，给slider control做个从指定数字到0的动画，也可以实现，指定时间段抖动的效果。

### 2_07_posterizeTime()

**posterizeTime(framesPerSecond)**
将属性的运行帧速率设置为低于合成的速率，framesPerSecond意思是每秒多少帧。
posterizeTime（1），表示1秒更新1次属性。
posterizeTime（12），表示1秒更新12次属性。
framesPerSecond可以是小数， posterizeTime（0.5），表示两秒更新一次属性。
合成的帧率为25，将framesPerSecond设为大于25的值没有意义。
**posterizeTime（framesPerSecond），它是用来设置其他表达式的运行环境的，不能单独使用，一般写在表达式的第一行。**

比如：给rotation属性添加下面的表达式，将旋转帧率改成12

```javascript
posterizeTime (12);
time * 100
```



### 2_08_random()

在每一帧生成一个指定范围内的随机值。
它的语法结构如下：
random（）不传递参数，生成0到1之间的随机数
random（maxVal） 传递一个参数，指定随机数的最大值
random（minVal， maxVal） 传递2个参数，指定随机数的范围
random（array）传递一个数组，指定随机数组的最大值

```javascript
random ()	//每一帧生成一个0—1之间的随机数，不包含0和1。
random(8)	//每一帧生成一个0—8之间的随机数， 不包含0和8。
random(2,6)	//每一帧生成一个2—6之间的随机数，不包含2和6。
random([50,100])	// [0,0] [50,100]
Math.round（random（100））	//生成一个0—100之间的整数，Math.round（）四舍五入，所以这里包括0和100。

//每秒产生2次随机
posterizeTime（2）；	//将帧率改为2
Math.round( random(100) );

//从数组中随机选一个值
posterizeTime (1);

fruitArr = ["Apple","Strawberry", "Orange", "Slump"];

fruit = fruitArr[Math.floor(random()*fruitArr.length)];

"我最喜欢的水果是: " + fruit;
```

#### 随机颜色

```javascript
//将表达式添加到颜色、fil1等属性上， 复制图层，可得到随机颜色
seedRandom(index, true);
random([0,0,0,1], [1,1,1,1]);
```

#### 随机位置

```javascript
// 将表达式添加到位置属性上， 复制图层，可得到随机位置。
seedRandom(index, true);
min = [0,0];
max = [thisComp.width, thisComp.height];
random (min,max);
```

### 2_09_seedRandom()

计算机并不会产生绝对的随机数，你看到的随机数是根据算法生成的有规律的伪随机数。
seedRandom（）不会生成随机数，它只是为随机数生成器提供种子。

以下图为例，从1—6之间生成一个随机数：

![](D:\Baize_Notes\JS基础知识\image25.png)

1—6这6个数就是种子；
假设取出的5是随机结果；
seedRandom（），会在每一次生成随机数后，将种子的初始值改变。

![](D:\Baize_Notes\JS基础知识\image26.png)

**语法**
seedRandom(offset, timeless=false)
offset，设置随机种子的初始值。
timeless，有true和false两个选择，当为true时，随机种子不随时间变化。当为false，随机种子会跟随时间变化，默认为false。

```javascript
// 添加到source Text上，产生了一个随机数
seedRandom(9527, false);
random(0,100);

// 添加到Source Text上，产生了一个固定数，不会随着时间变换
seedRandom(9527, true);
random(0,5);
```

**控制随机频率实现原理**

![](D:\Baize_Notes\JS基础知识\image27.png)

当timeless为true，种子不随时间变化，始终是从1到6这样的排序。

offset为固定值时，假设offset为5，这样会生成一个固定值5。

offset为不断变化的值时，就可以产生一个随机数，通过控制这个值变化的频率，也就实现了控制随机的频率。

```javascript
//offset是个变化的值，可以用time，也可以用slider Control制作关键帧动画
seedRandom(time, true);
random(0,5);
```

**seedRandom（）控制随机频率**
将offset设为time或对time进行相关运算。
将timeless设为true。
利用Math.floor（time/.5），一秒钟数字改变2次，就可以实现控制随机频率的效果。

```javascript
//将下面表达式添加给位置属性
seedRandom (Math.floor (time/0.5),true);	//一秒钟随机2次
random([thiscomp.width, thiscomp.height]);
```

**在某个时间段内随机**
将offset绑定到slider control上，给slider contol在指定时间段做关键帧动画。

将seedRandom的第二个参数设为true.

![](D:\Baize_Notes\JS基础知识\image28.jpg)

```javascript
//将下面表达式添加到位置属性
seedRandom(Math.floor(effect("Slider Control") ("slider")),true);
random([thisComp.width,thisComp.height])
```



### 2_10_noise()

**描述**
noise(time).返回-1到1之间的随机数，这些随机数之间相差不大。
noise0,必须传入一个参数，一般用time作为参数，传入一个固定数字没什么意义。

```javascript
//传入一个固定数值
noise(100);	//生成一个固定的值
noise(time);	//生成-1到1之间的随机值，一般参数就用time

//通过s1ider产生一个不断变化的参数
noise(effect("Slider Control")("Slider"));
```

**noise0制作心电图效果**
1、新建合成，新建一个纯色层命名为"writeOn",添加Write-on效果。给Brush Position（画笔位置）添加如下表达式。

```javascript
x = effect("Write-on")("Brush Position")[0] + time*200;
y = effect("Write-on")("Brush Position")[1] + noise(time*3)*200;
[x,y]
```

![](D:\Baize_Notes\JS基础知识\image29.jpg)

用椭圆工具画一个圆形，命名为“circle”，展开position属性，将位置跟笔刷的位置绑定。

```javascript
thisComp.layer("wirteOn").effect("Write-on")("Brush Position")
```

![](D:\Baize_Notes\JS基础知识\image30.jpg)

3、将第一步的表达式修改一下，让笔刷的y轴逐渐趋于0，实现心电图消失的效果。

```javascript
n = noise(time*3)*300 / Math.exp(time);
x = effect("Write-on")("Brush Position")[0] + time*300;
y = effect("Write-on")("Brush Position")[1] + n;

[x,y]
```

![](D:\Baize_Notes\JS基础知识\image31.jpg)

4、将noise()改成random()试试。

```javascript
n = random(-300, 300) / Math.exp(time);
x = effect("Write-on")("Brush Position")[0] + time*300;
y = effect("Write-on")("Brush Position")[1] + n;

[x,y]
```

![](D:\Baize_Notes\JS基础知识\image32.jpg)

### 2_11_loopOut() / loopIn()

关键帧之前循环loopln，关键帧之后循环loopOut。

![](D:\Baize_Notes\JS基础知识\image33.png)

**loopout(type="cycle",numKeyframes=0)**
type,指定循环的类型
numKeyframes,指定从那个关键帧开始循环，不常用。

```javascript
loopOut(type="cycle");	//(默认）动画播放结束，从头开始继续循环播放。
loopOut(type="pingpong");	//动画播放结束，然后从结束位置运动回开始位置，如此反复，类似打乒乓球
loopOut(type="offset");	//动画播放结束，从结束点继续往下重复运动，0+1,1+1,2+1，3+1...
loopOut(type="continue");	//动画播放结束，从结束点继续往下重复运动，它的运动增量取决于最后两个关键顿之间的运动速度。以Postion属性为例，从0帧到第1秒的时间从400运动到800，接下来它的增量为400/帧率25。
```

前三种类型numKeyframes可选，type="continue",不接受numKeyframes:这个参数。
numKeyframes=0循环所有关键帧；
numKeyframes=1循环最后2个关键帧；
numKeyframes=2循环最后3个关键帧；

...

当给numKeyframesi设置大于关键帧个数的数字时，就跟0一样，循环所有关键帧，这个参数一般默认0即可。

**loopIn（）**
功能用法同loopOut(0,looplr(0在第一个关键帧之前开始循环，loopOut(0在最后一个关键帧后开始循环。

```javascript
//连续出入循环
loopIn()+loop0ut()-value;
```



### 2_12_valueAtTime()

valueAtTime(t) 根据时间t获取值

```javascript
/*
新建1个圆形，命名为:circle
以透明度属性为例，给它做从0到100的动画效果
*/
thisComp.layer("circle").transform.opacity.valueAtTime(2);	//返回第2秒时的透明
```

```javascript
/*
新建1个圆形，命名为:circle
以透明度属性为例，给它做从0到100的动画效果
*/
thisComp.layer("circle").transform.opacity.valueAtTime(time-0.2);	//返回当前时间time(秒)之前0.2秒时的透明度
```

### 2_13_speedAtTime() / velocityAtTime()

**speedAtTime（）**
返回指定时间的（空间）速度。

**velocityAtTime（）**
返回指定时间的（瞬时）速度。

**speedAtTime（）与velocityAtTime（）的区别：**
velocityAtTime0,有方向，它的类型为数字或者数组；
speedAtTime0,它的类型为数字。

![](D:\Baize_Notes\JS基础知识\image35.jpg)

无论匀速运动还是非匀速运动，抛开方向它们的值都是一样的。

![](D:\Baize_Notes\JS基础知识\image35.jpg)

文字倾斜飞入效果
1、新建一个文本图层，输入文字。

![](D:\Baize_Notes\JS基础知识\image37.png)

2、给文字制作一个从右往左运动的效果。

![](D:\Baize_Notes\JS基础知识\image38.jpg)

3、给文字图层添加CC Slant（倾斜）和Directional Blur（方向模糊）效果。
给CC Slant的Slant和Directional Blur的Blur Length添加如下表达式。

```javascript
transform.position.speedAtTime(time);
```

预览，就得到了如下图所示的，文字倾斜飞入的效果，根本不需要去K关键帧。



![](D:\Baize_Notes\JS基础知识\image39.jpg)

speed
返回属性在默认时间的速度。

### 2_14_numLayers

numLayers 获取图层数量

**代码示例**

```javascript
// 假设有2个图层
thisComp.numLayers; 	// 2
```

根据图层的增加或减少来调整图形的旋转角度

```javascript
//给旋转属性添加表达式，ctrI+d复制图层
n =360/thisComp.numLayers;
(index-1)*n
```

![](D:\Baize_Notes\JS基础知识\image40.png)

### 2_15_vector math

vector math矢量（向量）数学函数是对数组执行操作的全局方法。

**add（）**

add(vec1,vec2),求vec1,vec2相加的结果。不一定非要数组相加，数字也可以。

```javascript
n1=[100,100]
n2=[50,50]
add(n1,n2);	//[150,150]

//相当于
[100,100]+[50,50]	//[150,150]

n1=100
n2=50
add(n1,n2);	//150

n1=[100,100]
n2=50
add(n1,n2);	//[150,100]

n1=[100,100,100,100]
n2=[200,200,200,200]
add(n1,n2);	//[300,300,300,300]
```

**sub（）**
sub(vec1,vec2),求vec1,vec2相减的结果。

```javascript
n1=[100,100]
n2=[60,60]
3ub(n1,n2)i//[40,40]
```

**mul（）**
mul(vec,amount),求vec的每个维度的值与数值amount相乘的结果。

```javascript
n1=[100,100]
n2=6
mu1(n1,n2);//[600,600]
```

**div（）**
div(vec,amount),求vec的每个维度的值与数值amount相除的结果。

```javascript
n1=[100,100]
n2=5
mu1(n1,n2);//[20,20]
```



### 2_16_gaussRandom()

gaussRandom(),高斯随机，结果具有高斯（钟形）分布，大约90%的结果在范围内0-1，其余10%的在这个范围之外。

高斯钟形分布图

![](D:\Baize_Notes\JS基础知识\image41.jpg)

```javascript
//此方法返回一个随机数。大约90%的结果在OtomaxValOrArray范围内，其余10%的在此范围之外。
gaussRandom(maxvalorArray);
```

```javascript
//此方法返回一个随机数。大约90的结果在从minValOrArray到的范围内maxValOrArray,其余10%:的在此范围之外。
gaussRandom(minValorArray,maxValorArray);
```

minValOrArray,maxValOrArray.为数字或者数组。

### 2_17_角度弧度互相转换

角度转弧度：degreesToRadians(degrees)
弧度转角度：radiansToDegrees(radians)

### 2_18_查AE属性的可用属性和方法

reflect.properties,查看可用属性。
reflect.methods,查看可用方法。
JavaScript引擎不支持reflect.properties和reflect.methods,.这两项是ExtendScript的特有方法，JavaScript中没有直接对应的方法。

```javascript
//将下面表达式添加到文本图层的源文本属性上，可以查看位置属性的可用属性
	transform.position.reflect.properties;
//将下面表达式添加到文本图层的源文本属性上，可以查看位置属性的可用方法
	transform.position.reflect.methods;
```

## 3、表达式汇总

### 1、万能弹性表达式

```javascript
freq = 6;
decay = 4;
n = 0;
if (numKeys > 0){
	n = nearestKey(time).index;
		if (key(n).time > time){
			n--;
		}
}
if (n > 0){
		t = time - key(n).time;
		amp = velocityAtTime(key(n).time - thisComp.frameDuration/20);
		w = freq*Math.PI*2;
		value + amp*(Math.sin(t*w)/Math.exp(decay*t)/w);
}
else
{
		value;
}
```
用法：添加到属性上，需要先做关键帧动画。

### 2、循环表达式

可以用来做循环效果，当freq和amp足够大时，会产生抖动。

```javascript
freq = 0.6;
amp = 5;
loopTime = 2;
t = time % loopTime;
wiggle1 = wiggle(freq, amp, 1, 0.5, t);
wiggle2 = wiggle(freq, amp, 1, 0.5, t - loopTime);
linear(t, 0, loopTime, wiggle1, wiggle2);
```
用法：添加到属性上，需要先做关键帧动画。

### 3、循环形状路径

```javascript
pingpong = false;
if (numKeys > 1){
	k1 = key(1).time;
	kn = key(numKeys).time;
	dur = kn - k1;
	t0 = time - k1;
	t = t0%dur;
	n = Math.ceil(t0/dur);
	if (pingpong == true && n%2 == 0){
		valueAtTime(kn - t);
	} else {
	valueAtTime(t + k1);
	}
} else {
	value;
}
```
用法：给形状图层路径（path）做关键帧动画以后，添加到路径（path）属性上。

### 4、随机表达式

可以添加到位置、缩放等至少是数组类型的属性上，制作随机效果，

```javascript
holdTime = 0.5;
minVal = [0.1 * thisComp.width, 0.1 * thisComp.height];
maxVal = [0.9 * thisComp.width, 0.9 * thisComp.height];
seed = Math.floor(time / holdTime);
seedRandom(seed, true);
random(minVal, maxVal);
```
用法：直接添加到属性上，不需要做关键帧动画。

### 5、拖尾、跟随效果表达式
```javascript
// 将这段表达式添加到位置属性上
delay = 5; // 设置延迟的帧数
d = delay * thisComp.frameDuration * (index - 1);
thisComp.layer(1).position.valueAtTime(time - d);

// 将这段表达式添加到透明度属性上
opacityFactor = 0.75;
Math.pow(opacityFactor, index - 1) * 100;
```
用法：位置属性需要制作关键帧动画，不透明度属性不需要，需要复制多个层。

### 6、金额增长表达式
```javascript
numDecimals = 0; // 小数点后的位数
commas = true; // 金额是否按千位逗号分割
currencySign = true; // 是否显示货币符号
beginCount = 0; // 开始值
endCount = 1000000; // 最大值
dur = 2; // 增长到最大值所用的时间
t = time - inPoint;
s = linear (t, 0, dur, beginCount, endCount).toFixed(numDecimals);

prefix = "";
if (s[0] == "-"){
	prefix = "-";
	s = s.substr(1);
}
if(currencySign) prefix += "$";// 这里可以修改货币符号
if (commas){
	decimals = "";
	if (numDecimals > 0){
	decimals = s.substr(-(numDecimals + 1));
	s = s.substr(0,s.length - (numDecimals + 1));
}
outStr = s.substr(-s.length, (s.length-1)%3 +1);
for (i = Math.floor((s.length-1)/3); i > 0; i--){
	outStr += "," + s.substr(-i*3,3);
}
	prefix + outStr + decimals;
}else{
	prefix + s;
}
```
用法：直接添加到文本图层的源文本属性上。

### 7、多个元素整体放大个体缩小
```javascript
s = [];
ps = parent.transform.scale.value;
for (i = 0; i < ps.length; i++){
	s[i] = value[i]*100/ps[i];
}
s

// 更简单的写法
ps = parent.transform.scale.value;
s = value[0] * 100 / ps[0];
[s, s]
```
用法：将表达式添加到元素缩放属性上，并给元素一个Null空对象作为父级。缩放父级即可看到效果。

### 8、文字动画效果
```javascript
//弹性动画效果
freq = 2;
decay = 4;
duration = 0.25;
retard = textIndex*thisComp.frameDuration*1;
t = time - (inPoint + retard);
startVal = [100,100,100];
endVal = [0,0,0];
if (t < duration){
	linear(t,0,duration,startVal,endVal);
}else{
	amp = (endVal - startVal)/duration;
	w = freq*Math.PI*2;
	endVal + amp*(Math.sin((t-duration)*w)/Math.exp(decay*(t-duration))/w);
}

//随机动画效果
freq = 3;
amplitude = 100;
decay = 4;
maxDelay = 0.7;
seedRandom(textIndex,true);
myDelay = random(maxDelay);

retard = textIndex*thisComp.frameDuration*1;
t = time - (inPoint + myDelay);
if (t >= 0){
	s = amplitude*Math.cos(freq*t*2*Math.PI)/Math.exp(decay*t);
	[s,s]
}
else{
	value
}
```

用法：

1. 新建文本图层
2. 展开文本图层，添加位置、缩放等属性
3. 点击Add(添加)，选择selector，添加expression表达式
4. 将上面表达式粘贴进去
5. 调整第2步添加的位置、缩放等属性的值，即可看到动画效果。

### 9、波动的文字效果

```javascript
/*
1、新建一个文本层，输入文字
2、点击Animate后面的箭头，添加position
3、点击Add后面的箭头，选择selector-Expression
4、展开Amount，将selectorValue * textIndex / textTotal 替换成下面这句，注意这里的index是textIndex 文本的索引
5、调整position的x、y就可以实现上下、左右波动效果
*/
Math.sin((time - inPoint) * 5 + textIndex) * 100;
```

### 10、形状图层缩放描边大小保持不变

```javascript
value / length(toComp([0, 0]), toComp([0.7071, 0.7071])) || 0.001;
```

用法：直接添加到形状图层的描边大小属性上。

```javascript
s = transform.scale[0];
value/ (s/100);
```

用法:
1、将描边宽度跟缩放属性的一个值绑定。
2、将上面表达式添加到形状图层的描边大小属性上。

### 11、路径循环表达式

可实现类似loopOut()的循环效果。

```javascript
if(numKeys>1 && time>key(numKeys).time)
{
	t1 = key(1).time;
	t2 = key(numKeys).time;
	span = t2 - t1;
	delta = time - t2;
	t = delta % span;
	valueAtTime(t1 + t);
}
else
{
	value;
}
```

这是上面表达式的一种更简单的实现方法，但是第一个关键帧必须在0帧位置，否则循环中间会停留一段时间。这段时间就是第0帧到第一个关键帧的时间。

```plaintext
valueAtTime(time % key(numKeys).time);
```

可实现类似loopIn、loopOut同时使用的效果。

```javascript
if(numKeys>1 && time>key(numKeys).time)
{
	t1 = key(1).time;
	t2 = key(numKeys).time;
	span = t2 - t1;
	delta = time - t2;
	t = delta % span;
	valueAtTime(t1 + t);
}
else if(numKeys>1 && time<key(1).time)
{
	t1 = key(1).time;
	t2 = key(numKeys).time;
	span = t2 - t1;
	delta = time + t2;
	t = delta % span;
	valueAtTime(t1 + t);
}
else
{
	value;
}
```

用法：直接添加到路径path上，需要先做关键帧动画。

### 12、拉伸压缩效果表达式

可以用来做弹跳的小球效果。只需调整一个参数即可，比较方便。

```javascript
w = value[0];
h = 100 - w;
n = value[1] + h;
[w, n]
```

用法：将表达式添加到缩放属性上，然后取消宽高的链接，调整一个参数，另一个也跟着变化。

### 13、弹性变形表达式

```javascript
maxDev = 10; // 最大形变大小
spd = 30; // 速度
decay = 1.0; // 静止快慢

t = time - inPoint;
x = scale[0] + maxDev*Math.sin(spd*t)/Math.exp(decay*t);
y = scale[0]*scale[1]/x;
[x,y]
```

用法：直接添加到缩放属性上即可，不需要做关键帧动画。

### 14、淡入淡出效果表达式

当有大量元素淡入淡出的时候，用这段表达式会比较方便，省了k帧的时间，可以任意设置出入点。

```javascript
FadeTime=framesToTime( 15 );
if(time < inPoint+FadeTime* 1.2 ) {
	linear(time,inPoint,inPoint+FadeTime, 0 ,value)
}
else {
	linear(time,outPoint-FadeTime,outPoint,value, 0 )
};
```

用法：直接添加表达式到不透明度属性上。

### 15、缩小/放大效果表达式

可用来制作从大到小再到大的效果，配合上面的淡入淡出表达式使用效果更好。

```javascript
snapScale = 300; // 缩放的百分比
trans = 4; // 变化持续时间，4帧
trans = trans * thisComp.frameDuration;
inTrans = easeOut(time, inPoint, inPoint + trans, [snapScale,snapScale],
[0,0]);
outTrans = easeIn(time, outPoint, outPoint - trans, [0,0], [snapScale,
snapScale]);
value+ inTrans + outTrans
```

用法：直接添加到缩放属性上。

### 16、3D图层始终朝向摄像机

使用此表达式，3D图层将始终面向相机，而不会发生任何倾斜和变形。

```javascript
try{
L = thisComp.activeCamera;
u = fromWorldVec(L.toWorldVec([1,0,0]));
v = fromWorldVec(L.toWorldVec([0,1,0]));
w = normalize(fromWorldVec(L.toWorldVec([0,0,1])));

sinb = clamp(w[0],-1,1);
b = Math.asin(sinb);
cosb = Math.cos(b);
if (Math.abs(cosb) > .0005){
	c = -Math.atan2(v[0],u[0]);
	a = -Math.atan2(w[1],w[2]);
}else{
	a = (sinb < 0 ? -1 : 1)*Math.atan2(u[1],v[1]);
	c = 0;
}
	[radiansToDegrees(a),radiansToDegrees(b),radiansToDegrees(c)]
}catch(err){
	value
}
```

用法：

1. 新建一个矩形形状，打开3D开关，给其方向属性添加上面表达式。
2. 再新建2个矩形形状，打开3D开关。
3. 新建一个摄像机。
4. 旋转摄像机，添加了表达式的矩形始终朝向摄像机。

### 17、自动闪烁

```javascript
freq = 10;
n = Math.sin(time * freq);
n < 0 ? 0 : 100
```

用法：将表达式添加给元素的不透明度属性即可。

可以通过修改freq的值，修改闪烁的频率。

### 18、仅在X方向抖动

```plaintext
[wiggle(5, 300)[0], value[1]]
```

### 19、仅在Y方向抖动

```javascript
[value[0], wiggle(5,300)[1]]
```


### 20、仅在Z方向抖动
Z轴抖动，可以实现视觉上的缩放效果。
```javascript
//打开图层的3d开关，将表达式添加到位置属性上
x = value[0];
Y = value[1];
z = wiggle(10,200)[2];
[X,Y,z]
```

### 21、以指定频率抖动
```javascript
fps=5; //频率
amp=50; //抖动的幅度
wiggle(fps,amp,octaves = 1, amp_mult = 20,(Math.round(time*fps))/fps);
```

### 22、逐渐停止抖动
```javascript
wiggle(5,800/Math.exp(time*2));
```

### 23、在指定时间段抖动
```javascript
if(time>3 && time <4){
	wiggle(20,200)
}
else
{
	value;
}
```

### 24、震荡旋转
创建连续旋转效果：
```javascript
from=-60; //旋转开始的角度
to=60; //旋转结束的角度
period=0.5; //完成一次旋转需要的时间，以秒为单位，值越大旋转的越慢
t=time%(period*2); //生成一个从0到period*2不断循环的数
if（t>period）//当不断循环的数t，大于指定的时间period时，重新计算t的值
  t = 2 * period - t;
linear(t,0,period,from,to)
```
用法：直接添加到旋转属性上。

### 25、脉冲效果
创建脉冲效果：
```javascript
freq = 2;
amp = 150;
x = amp*Math.sin(freq*time*Math.PI*2);
value + [x,0]
```
用法：直接添加到位置、缩放等数组类型的属性上。可以根据需要修改最后一句，这样也可以添加到旋转、不透明度等属性上。

### 26、平均分布图层
```javascript
n = thisComp.numLayers;
if (n > 2){
	p1 = thisComp.layer(1).transform.position;
	pn = thisComp.layer(n).transform.position;
	linear(index,1,n,p1,pn)
}else{
	value
}
```
用法：直接添加到位置属性上，然后ctrl+d复制图层，移动位置。

### 27、闪烁效果
创建闪烁效果：
```javascript
wiggle(5,100)
random(0,100)
100*Math.sin(time*5)
Math.abs(100*Math.sin(time*Math.PI*1))
Math.abs(Math.sin(time*6))*100
```
用法：添加到不透明度属性上，可以修改相关数字，得到不同的闪烁效果。

### 28、背对摄像机不可见
当图层背对摄像机时设置不可见：
```javascript
toCompVec([0, 0,1])[2]>0 ? 100:0
```
用法：添加到不透明度属性上，打开3D开关，旋转就可以看到效果。

### 29、补零函数
当数字小于10的时候，给前面加上0：
```javascript
function addzero(n){
  if(n<10){
    n="0"+n
  }
  else
  {
  	n
  }
    return n;
}
addzero(90); // 90
addzero(9);  // 09
```

### 30、生成指定位数英文字母
生成指定位数的英文字母：
```javascript
posterizeTime(10);
var str = "";
for(i=0; i<10; i++){
  n = Math.round(random(65,90));
  str += "" + String.fromCharCode(n)
}
```

### 31、模拟保持关键帧
如果要临时删除关键帧之间的过渡。可以右键单击关键帧并选择Toggle Hold Keyframes”，这样就可以做到这一点，但这种方法具有破坏性，会丢失之前的缓动数据。
为了解决这个问题，我们可以使用表达式来模拟相同的效果，方法是找到后一个关键帧并保持其值。

```javascript
var nearest = nearestKey(time); //获取离当前时间最近的关键帧
var isInThePast = nearest.time <= time; //当前时间是否大于离它最近的关键帧所处的时间
isInThePast ? nearest : key(nearest.index-1);
```
用法：给属性（比如位置属性）做关键帧动画，然后添加表达式，即可实现保持关键帧效果。

### 32、简单打字机效果
创建打字机效果：
```javascript
startAt = 0;
endAt = 5; //5秒钟打完文字
maxLetters = Math.floor(linear(time, startAt, endAt, 0, value.length));
value.substring(0,maxLetters);
```
用法：新建文本图层，输入文字，将表达式添加到源文本属性上。

### 33、满屏随机数
生成满屏随机数：
```javascript
var str = "";
for(var i=0; i<520; i++){	//520是要显示的字数，可以根据需要修改，实际的到的是1040个数字
  str += Math.round(random(100));	 //60是一行显示60个字，可根据需要修改
  str.replace(/[^\x00-\xff]/g,"$&\x01").replace(/.{60}\x01?/g,"$&\n").replace(/\x01/g,"");
  }
```
用法：新建文本图层，将表达式添加到源文本属性上。

### 34、圆周运动
创建顺时针或逆时针的圆周运动：
```javascript
// 顺时针运动
value + [Math.sin(time*4)*200,-Math.cos(time*4)*250]

// 逆时针运动
value + [Math.sin(time*4)*200,Math.cos(time*4)*250]
```
用法：将表达式粘贴到位置属性上。
