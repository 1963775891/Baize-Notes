### 0.去除ctrl+空格占用.reg

```javascript
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

```javascript
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

------

### 2.遮罩影响图层表达式：通过遮罩羽化做衰减动画

```javascript
// 让图层对蒙版做出反应
// 要求使用 AE 16.0 (CC2019) 中引入的新 "Javascript "表达式引擎
// 如果将所有 "let "替换为 "var"，该表达式在以前的版本中应该可以工作
// 将遮罩层命名"MASK"

const numDivisions = 5; // Adjust this number for more or less precision
const maskLayer = thisComp.layer("MASK"); // Replace "MASK" with the name of your layer
const maskName = "Mask 1"; // Change this to the name of your mask

const maskPath = maskLayer.mask(maskName).maskPath;
const rawMaskPoints = maskPath.points();
const inTangents = maskPath.inTangents();
const outTangents = maskPath.outTangents();
const isMaskClosed = maskPath.isClosed();
const maskFeather = maskLayer.mask(maskName).maskFeather[0];
const fallOffSquared = Math.pow(maskFeather, 2);

function needsSubdivision(c1, c2) {
    const tangentThreshold = 0.1;
    return (length(c1) > tangentThreshold || length(c2) > tangentThreshold);
}

function bezier(t, p1, c1, c2, p2) {
    var u = 1 - t, tt = t * t, uu = u * u, uuu = uu * u, ttt = tt * t;
    return [
        uuu * p1[0] + 3 * uu * t * c1[0] + 3 * u * tt * c2[0] + ttt * p2[0],
        uuu * p1[1] + 3 * uu * t * c1[1] + 3 * u * tt * c2[1] + ttt * p2[1]
    ];
}

function subdivideBezierSegment(p1, c1, c2, p2, numDivisions) {
    var newPoints = [];
    for (var i = 0; i <= numDivisions; i++) {
        var t = i / numDivisions;
        newPoints.push(bezier(t, p1, c1, c2, p2));
    }
    return newPoints;
}

function transformMaskPoints(layer, pathPoints, inTangents, outTangents, isClosed) {
    var allPoints = [];
    var count = isClosed ? pathPoints.length : pathPoints.length - 1;

    for (var i = 0; i < count; i++) {
        var nextIndex = (i + 1) % pathPoints.length;
        var c1 = pathPoints[i] + outTangents[i];
        var c2 = pathPoints[nextIndex] + inTangents[nextIndex];

        if (needsSubdivision(outTangents[i], inTangents[nextIndex])) {
            allPoints = allPoints.concat(subdivideBezierSegment(pathPoints[i], c1, c2, pathPoints[nextIndex], numDivisions));
        } else {
            allPoints.push(pathPoints[i], pathPoints[nextIndex]);
        }
    }

    return allPoints.map(pt => layer.toComp(pt));
}

const transformedMaskPoints = transformMaskPoints(maskLayer, rawMaskPoints, inTangents, outTangents, isMaskClosed);

function inside(point, path) {

    let [minX, maxX, minY, maxY] = [Infinity, -Infinity, Infinity, -Infinity];
    for (let i = 0; i < path.length; i++) {
        minX = Math.min(minX, path[i][0]);
        maxX = Math.max(maxX, path[i][0]);
        minY = Math.min(minY, path[i][1]);
        maxY = Math.max(maxY, path[i][1]);
    }
    if (point[0] < minX || point[0] > maxX || point[1] < minY || point[1] > maxY) {
        return false;
    }

    let inside = false;
    for (let i = 0, j = path.length - 1; i < path.length; j = i++) {
        let xi = path[i][0], yi = path[i][1];
        let xj = path[j][0], yj = path[j][1];
        let intersect = ((yi > point[1]) != (yj > point[1])) && (point[0] < (xj - xi) * (point[1] - yi) / (yj - yi) + xi);
        if (intersect) inside = !inside;
    }
    return inside;
}

function distanceToLineSquared(point, a, b) {
    let lineLengthSquared = Math.pow(a[0] - b[0], 2) + Math.pow(a[1] - b[1], 2);
    if (lineLengthSquared == 0) return Math.pow(point[0] - a[0], 2) + Math.pow(point[1] - a[1], 2);
    let t = ((point[0] - a[0]) * (b[0] - a[0]) + (point[1] - a[1]) * (b[1] - a[1])) / lineLengthSquared;
    t = Math.max(0, Math.min(1, t));
    return Math.pow(point[0] - (a[0] + t * (b[0] - a[0])), 2) + Math.pow(point[1] - (a[1] + t * (b[1] - a[1])), 2);
}

function closestDistanceSquared(point, path) {
    let closestDistSquared = Infinity;
    for (let i = 0; i < path.length - 1; i++) {
        let distSquared = distanceToLineSquared(point, path[i], path[i + 1]);
        if (distSquared < closestDistSquared) closestDistSquared = distSquared;
    }
    return closestDistSquared;
}

const anchorPoint = thisLayer.transform.anchorPoint;
const toCompAnchor = thisLayer.toComp([anchorPoint[0], anchorPoint[1]]);
let effectValue = thisProperty.key(1).value;
let closestDistSquared = closestDistanceSquared(toCompAnchor, transformedMaskPoints);

if (isMaskClosed) {
    let isInside = inside(toCompAnchor, transformedMaskPoints);
    if (isInside) {
        effectValue = thisProperty.key(2).value;
    } else if (maskFeather > 0 && closestDistSquared <= fallOffSquared) {
        let normalizedDistance = Math.sqrt(closestDistSquared) / maskFeather;
        effectValue = linear(normalizedDistance, 0, 1, thisProperty.key(2).value, thisProperty.key(1).value);
    }
} else {
    if (maskFeather > 0 && closestDistSquared <= fallOffSquared) {
        let normalizedDistance = Math.sqrt(closestDistSquared) / maskFeather;
        effectValue = linear(normalizedDistance, 0, 1, thisProperty.key(2).value, thisProperty.key(1).value);
    }
}

effectValue;
```

