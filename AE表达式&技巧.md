### 0.去除ctrl+空格占用.reg

```sh
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Control Panel\Input Method\Hot Keys\00000010]
"Key Modifiers"=hex:06,c0,00,00
"Target IME"=hex:00,00,00,00
"Virtual Key"=hex:21,00,00,00

[HKEY_CURRENT_USER\Control Panel\Input Method\Hot Keys\00000011]
"Key Modifiers"=hex:06,c0,00,00
"Target IME"=hex:00,00,00,00
"Virtual Key"=hex:70,00,00,00

[HKEY_USERS\.DEFAULT\Control Panel\Input Method\Hot Keys\00000010]
"Key Modifiers"=hex:06,c0,00,00
"Target IME"=hex:00,00,00,00
"Virtual Key"=hex:21,00,00,00

[HKEY_USERS\.DEFAULT\Control Panel\Input Method\Hot Keys\00000011]
"Key Modifiers"=hex:06,c0,00,00
"Target IME"=hex:00,00,00,00
"Virtual Key"=hex:70,00,00,00
```

------

### 1. 弹性表达式

```JAVA
amp = 0.4;	//幅度
freq = 2.0;	// 值越高, 频率越高
decay = 5.0;	// 值越高, 延迟越小
n = 0;
if (numKeys > 0){
n = nearestKey(time).index;
if (key(n).time > time)
{n--;}
}
if (n == 0)
{t = 0;}
else
{t = time - key(n).time;}
if (n > 0)
{v = velocityAtTime(key(n).time - thisComp.frameDuration/10);
value + v*amp*Math.sin(freq*t*2*Math.PI)/Math.exp(decay*t);}
else{value;}
```