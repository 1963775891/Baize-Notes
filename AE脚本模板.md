## 一套脚本UI模板

```javascript
// 创建一个新的窗口面板
var win = new Window("palette", "My Script", undefined);
win.spacing = 5;

// 创建第一行的按钮
var group = win.add("group");
group.orientation = "row";
group.spacing = 5;

// 定义第一行按钮的名称
var buttonNames = ["加密", "A", "B", "C"];

//按钮A函数功能写在外部
  function A() {// 恒速主要功能函数
    app.beginUndoGroup("Constant speed");
  }

// 定义第一行按钮的功能
var buttonFunctions = [
// 加密脚本
  function() {
    var scriptContent = "@JSXBIN@ES@2.0@MyBbyBn...";//不可以分行，不然会报错
    eval(scriptContent);},
// 按钮A
  function() { //引用按钮A函数功能
    A(); },
// 按钮B
  function() { alert("按钮 B 被点击了"); },
// 按钮C
  function() { alert("按钮 C 被点击了"); },
];

// 定义第一行按钮的悬停提示词
var buttonTips = [  
  "这是按钮 加密",
  "这是按钮 A",
  "这是按钮 B",
  "这是按钮 C",
];

// 创建并设置按钮
for (var i = 0; i < buttonNames.length; i++) {
  var button = group.add("button", undefined, buttonNames[i]);
  button.size = [25, 25];
  button.helpTip = buttonTips[i];
  button.onClick = buttonFunctions[i];
}

    // 为按钮添加右键点击事件
    if (buttonNames[i] === "加密") {
        button.addEventListener('mousedown', function(event) {
            if (event.button === 2) { // 右键点击
                加密();
            }
        });
    }
}

// 显示窗口
win.show();
```

------

## 浮动脚本模板

```JavaScript
// 创建一个可停靠的面板
var myPanel = this instanceof Panel ? this : new Window("palette", "My Floating Panel", undefined, { resizeable: true });

// 设置面板的布局和大小
myPanel.orientation = "column";
myPanel.alignChildren = ["fill", "fill"];
myPanel.spacing = 5;

// 创建按钮名称数组
var buttonNamesRow1 = ["灯", "空", "填", "渐", "光", "曲", "角", "三", "定", "路"];
var buttonNamesRow2 = ["速", "测", "接", "当", "左", "右", "控", "合", "表", "抠"];

// 创建按钮功能数组
var buttonFunctionsRow1 = [
  function() { 
    var comp = app.project.activeItem;
    if (comp && comp instanceof CompItem) {
      var light = comp.layers.addLight("灯光", [comp.width / 2, comp.height / 2]);
      light.lightType = LightType.POINT;
    } else {
      alert("请先选择一个合成");
    }
  },
  function() { alert("空按钮被点击了"); },
  function() { alert("填按钮被点击了"); },
  function() { alert("渐按钮被点击了"); },
  function() { alert("光按钮被点击了"); },
  function() { alert("曲按钮被点击了"); },
  function() { alert("角按钮被点击了"); },
  function() { alert("三按钮被点击了"); },
  function() { alert("定按钮被点击了"); },
  function() { alert("路按钮被点击了"); }
];

var buttonFunctionsRow2 = [
  function() { alert("速按钮被点击了"); },
  function() { alert("测按钮被点击了"); },
  function() { alert("接按钮被点击了"); },
  function() { alert("当按钮被点击了"); },
  function() { alert("左按钮被点击了"); },
  function() { alert("右按钮被点击了"); },
  function() { alert("控按钮被点击了"); },
  function() { alert("合按钮被点击了"); },
  function() { alert("表按钮被点击了"); },
  function() { alert("抠按钮被点击了"); }
];

// 创建按钮悬停提示数组
var buttonTipsRow1 = [
  "添加灯光",
  "右键添加填充效果",
  "填充效果",
  "渐变效果",
  "光效果",
  "曲线效果",
  "角效果",
  "三角效果",
  "定位效果",
  "路径效果"
];

var buttonTipsRow2 = [
  "速度效果",
  "测量效果",
  "接合效果",
  "当效果",
  "左对齐效果",
  "右对齐效果",
  "控件效果",
  "合并效果",
  "表达式效果",
  "右键添加填充效果"
];

// 创建一个函数来添加按钮行
function addButtonRow(panel, buttonNames, buttonFunctions, buttonTips) {
  var group = panel.add("group");
  group.orientation = "row";
  group.alignChildren = ["fill", "fill"];
  group.spacing = 5;

  for (var i = 0; i < buttonNames.length; i++) {
    var button = group.add("button", undefined, buttonNames[i]);
    button.size = [undefined, 25];
    button.helpTip = buttonTips[i];
    button.onClick = buttonFunctions[i];

    // 如果是“空”按钮，添加右键点击功能
    if (buttonNames[i] === "空") {
      button.addEventListener("mousedown", function(event) {
        if (event.button === 2) { // 检查是否是右键点击
          var comp = app.project.activeItem;
          if (comp && comp.selectedLayers.length > 0) {
            var layer = comp.selectedLayers[0];
            layer.property("ADBE Effect Parade").addProperty("ADBE Fill");
          } else {
            alert("请先选择一个图层");
          }
        }
      });
    }

    // 如果是“抠”按钮，添加右键点击功能
    if (buttonNames[i] === "抠") {
      button.addEventListener("mousedown", function(event) {
        if (event.button === 2) { // 检查是否是右键点击
          var comp = app.project.activeItem;
          if (comp && comp.selectedLayers.length > 0) {
            var layer = comp.selectedLayers[0];
            layer.property("ADBE Effect Parade").addProperty("ADBE Fill");
          } else {
            alert("请先选择一个图层");
          }
        }
      });
    }
  }
}

// 添加两行按钮到面板
addButtonRow(myPanel, buttonNamesRow1, buttonFunctionsRow1, buttonTipsRow1);
addButtonRow(myPanel, buttonNamesRow2, buttonFunctionsRow2, buttonTipsRow2);

// 确保面板像其他面板一样调整大小和位置
myPanel.layout.layout(true);
myPanel.onResizing = myPanel.onResize = function () {
  myPanel.layout.resize();
};

// 显示面板
if (myPanel instanceof Window) {
  myPanel.center();
  myPanel.show();
} else {
  myPanel.layout.layout(true);
}

```

