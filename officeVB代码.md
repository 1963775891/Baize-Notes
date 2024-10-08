> **使用说明：**
>
> - 按 `Alt + F11` 打开VBA编辑器，在VBA编辑器中，选择 `插入 -> 模块`，创建一个新的模块。关闭并返回文档。按 `Alt + F8` 打开宏对话框，选择 `RemoveTextBoxes`，然后点击 `运行`。
>
>
> - 批量导入`VB`，将所有代码整合，后缀改为`.bas`

 ## 1、提取文本框内文本并按顺序插入Word
```vbscript
Sub RemoveTextBoxes()
    Dim doc As Document
    Dim textBox As Shape
    Dim textBoxRange As Range
    Dim para As Paragraph
    Dim insertPoint As Range

    ' 获取当前文档
    Set doc = ActiveDocument

    ' 循环遍历文档中的所有形状
    For Each textBox In doc.Shapes
        ' 检查形状是否是文本框
        If textBox.Type = msoTextBox Then
            ' 获取文本框中的文本范围
            Set textBoxRange = textBox.TextFrame.TextRange
            
            ' 设置插入点在文本框所在段落的前面
            Set insertPoint = textBox.Anchor.Paragraphs(1).Range
            insertPoint.Collapse Direction:=wdCollapseStart
            
            ' 插入文本框中的文本，并添加换行符
            insertPoint.FormattedText = textBoxRange.FormattedText
            insertPoint.InsertAfter vbCrLf
            
            ' 删除文本框
            textBox.Delete
        End If
    Next textBox
End Sub
```


```vbscript
Sub RemoveTextBoxesAndKeepText()
    Dim shp As Shape
    Dim inlShp As InlineShape
    Dim shpText As Range
    Dim inlShpText As Range
    Dim para As Paragraph

    ' 遍历所有浮动形状
    For Each shp In ActiveDocument.Shapes
        ' 如果形状是文本框
        If shp.Type = msoTextBox Then
            ' 复制文本框内容
            Set shpText = shp.TextFrame.TextRange.Duplicate
            ' 插入到文本框前的段落
            shpText.Copy
            shp.Anchor.Parent.Range.InsertBefore shpText.Text
            ' 删除文本框
            shp.Delete
        End If
    Next shp
    
    ' 遍历所有内嵌形状
    For Each inlShp In ActiveDocument.InlineShapes
        ' 检查是否为内嵌文本框
        If inlShp.Type = wdInlineShapeTextBox Then
            ' 复制文本框内容
            Set inlShpText = inlShp.Range.Duplicate
            ' 插入到文本框前的段落
            inlShpText.Copy
            inlShp.Range.InsertBefore inlShpText.Text
            ' 删除内嵌文本框
            inlShp.Delete
        End If
    Next inlShp

    ' 清理段落：去除空段落，合并连续的段落
    For Each para In ActiveDocument.Paragraphs
        If Len(Trim(para.Range.Text)) = 0 Then
            para.Range.Delete
        End If
    Next para

    ' 优化文本
    Call OptimizeTextFormatting

End Sub

Sub OptimizeTextFormatting()
    Dim para As Paragraph
    
    ' 遍历所有段落并应用格式化
    For Each para In ActiveDocument.Paragraphs
        ' 删除段落的前后多余空白
        para.Range.Text = Trim(para.Range.Text)
        ' 将段落间距调整为标准
        para.SpaceBefore = 6
        para.SpaceAfter = 6
        para.Range.ParagraphFormat.Alignment = wdAlignParagraphLeft
    Next para
End Sub

```

------

## 2 、快速删除空白页

```vb
Sub RemoveBlankPages()
    Dim doc As Document
    ' 获取当前文档
    Set doc = ActiveDocument

    Dim i As Integer
    ' 从文档末尾往前遍历每一页
    For i = doc.Range.Information(wdActiveEndAdjustedPageNumber) To 1 Step -1
        ' 检查该页是否为空白页
        If Len(Trim(doc.Range(doc.GoTo(wdGoToPage, wdGoToAbsolute, i).Start, _
            doc.GoTo(wdGoToPage, wdGoToAbsolute, i + 1).Start).Text)) = 0 Then
            ' 删除空白页
            doc.Range(doc.GoTo(wdGoToPage, wdGoToAbsolute, i).Start, _
                doc.GoTo(wdGoToPage, wdGoToAbsolute, i + 1).Start).Delete
        End If
    Next i
End Sub
```

------

## 3、快速删除两行和两行以上的空行

```vb
Sub RemoveMultipleEmptyLines()
    Dim doc As Document
    ' 获取当前文档
    Set doc = ActiveDocument
    
    ' 查找和替换连续的两个段落标记（即两个空行）
    With doc.Content.Find
        .ClearFormatting
        .Text = "^13^13"
        Do While .Execute(Replace:=wdReplaceAll, ReplaceWith:="^p")
        Loop
    End With
End Sub
```

------

## 4、选中图片高度统一设为10厘米，宽度等比

```vbscript
Sub ResizeSelectedImages()
    Dim sel As Selection
    Dim shape As InlineShape
    
    ' 获取当前选中的内容
    Set sel = Selection
    
    ' 遍历选中的所有图片
    For Each shape In sel.InlineShapes
        If shape.Type = wdInlineShapePicture Then
            ' 锁定宽高比例
            shape.LockAspectRatio = msoTrue
            ' 设置高度为10厘米
            shape.Height = CentimetersToPoints(10)
        End If
    Next shape
End Sub
```

------

## 5、PPT图片转形状：可改透明度

```vbscript
Sub ConvertPictureToShape()
    Dim slide As slide
    Dim shp As shape
    Dim shpRange As shapeRange
    Dim newShp As shape

    ' 获取当前选中的图片
    If ActiveWindow.Selection.Type = ppSelectionShapes Then
        Set shpRange = ActiveWindow.Selection.ShapeRange
        For Each shp In shpRange
            ' 只处理图片类型的形状
            If shp.Type = msoPicture Then
                ' 复制图片
                shp.Copy
                ' 粘贴为形状
                Set newShp = shp.Parent.Shapes.PasteSpecial(DataType:=ppPasteShape)
                ' 删除原来的图片
                shp.Delete
                ' 调整新形状的大小和位置
                With newShp
                    .LockAspectRatio = msoTrue
                    .Left = shp.Left
                    .Top = shp.Top
                    .Height = shp.Height
                    .Width = shp.Width
                End With
            End If
        Next shp
    Else
        MsgBox "请选择要转换的图片", vbExclamation
    End If
End Sub

```

------

## 6、清除文本框的形状格式

```vbscript
Sub ClearTextBoxFormatting()
    Dim shp As Shape
    Dim inlShp As InlineShape

    ' 遍历所有浮动形状
    For Each shp In ActiveDocument.Shapes
        ' 如果形状有文本框
        If shp.Type = msoTextBox Then
            With shp
                ' 清除文本框的形状格式
                .Line.Visible = msoFalse        ' 隐藏边框
                .Fill.Transparency = 1          ' 设置填充透明
                .Shadow.Visible = msoFalse      ' 移除阴影
                .Glow.Radius = 0                ' 移除辉光
                .SoftEdge.Radius = 0            ' 移除软边缘
                ' 清除 3D 格式
                .ThreeD.Visible = False
            End With
        End If
    Next shp
    
    ' 遍历所有内嵌形状
    For Each inlShp In ActiveDocument.InlineShapes
        ' 检查是否为内嵌文本框
        If inlShp.Type = wdInlineShapeTextBox Then
            With inlShp
                ' 将内嵌文本框转换为 Shape 类型
                Dim tempShape As Shape
                Set tempShape = .ConvertToShape
                ' 清除文本框的形状格式
                With tempShape
                    .Line.Visible = msoFalse    ' 隐藏边框
                    .Fill.Transparency = 1      ' 设置填充透明
                    .Shadow.Visible = msoFalse  ' 移除阴影
                    .Glow.Radius = 0            ' 移除辉光
                    .SoftEdge.Radius = 0        ' 移除软边缘
                    ' 清除 3D 格式
                    .ThreeD.Visible = False
                End With
            End With
        End If
    Next inlShp

End Sub

```

------

## 7、Word文档清理

```vbscript
Sub CleanupDocument()
    Dim doc As Document
    Dim sec As Section
    Dim para As Paragraph
    Dim shp As Shape
    Dim rng As Range
    Dim txtBox As TextFrame
    
    ' 关闭屏幕更新以提高性能
    Application.ScreenUpdating = False
    
    Set doc = ActiveDocument
    
    ' 删除多余的分页符、分栏符和分节符
    doc.Content.Select
    Selection.Find.ClearFormatting
    Selection.Find.Replacement.ClearFormatting
    With Selection.Find
        .Text = "^b^m^l^k^p^n" ' 匹配分节符、分页符、分栏符、换行符、段落标记和手动换行符
        .Replacement.Text = "^p" ' 替换为单个段落标记
        .Forward = True
        .Wrap = wdFindContinue
        .Format = False
        .MatchCase = False
        .MatchWholeWord = False
        .MatchWildcards = False
        .MatchSoundsLike = False
        .MatchAllWordForms = False
    End With
    Selection.Find.Execute Replace:=wdReplaceAll
    
    ' 清除页眉和页脚
    For Each sec In doc.Sections
        sec.Headers(wdHeaderFooterPrimary).Range.Delete
        sec.Footers(wdHeaderFooterPrimary).Range.Delete
    Next sec
    
    ' 提取文本框内容并转换为普通文本
    For Each shp In doc.Shapes
        If shp.Type = msoTextBox Then
            Set txtBox = shp.TextFrame
            If txtBox.HasText Then
                doc.Paragraphs.Add doc.Paragraphs(doc.Paragraphs.Count).Range
                doc.Paragraphs(doc.Paragraphs.Count).Range.InsertAfter txtBox.TextRange.Text
                shp.Delete
            End If
        End If
    Next shp
    
    ' 清除格式，设置为默认，并应用指定的字体
    doc.Content.Select
    With Selection.Font
        .Name = "微软雅黑"
        .Size = 4
    End With
    Selection.ClearFormatting
    
    ' 使用错误处理来设置样式
    On Error Resume Next
    Selection.Style = ActiveDocument.Styles("正文")
    If Err.Number <> 0 Then
        Selection.Style = ActiveDocument.Styles("Normal")
    End If
    On Error GoTo 0
    
    ' 重新应用字体设置（因为ClearFormatting可能会重置字体）
    With Selection.Font
        .Name = "微软雅黑"
        .Size = 4
    End With
    
    ' 重新开启屏幕更新
    Application.ScreenUpdating = True
    
    MsgBox "文档清理完成！", vbInformation
End Sub
```

------

## 8、Word每450字符添加下划线

```vbscript
Sub AddUnderlineEvery450Chars()
    Dim doc As Document
    Set doc = ActiveDocument
    
    Dim content As String
    content = doc.Content.Text
    
    Dim result As String
    Dim i As Long
    Dim chunk As String
    
    For i = 1 To Len(content) Step 450
        chunk = Mid(content, i, 450)
        result = result & chunk & vbNewLine & String(Len(chunk), "_") & vbNewLine & vbNewLine
    Next i
    
    doc.Content.Text = result
    
    ' 格式化下划线
    With doc.Content.Find
        .Text = String(1, "_")
        .Replacement.Text = ""
        .Forward = True
        .Wrap = wdFindContinue
        .Format = True
        .Replacement.Font.Underline = wdUnderlineSingle
        .Execute Replace:=wdReplaceAll
    End With
End Sub
```

------

## 9、Word宏:删除所有中文字符

```VBScript
Sub DeleteChineseCharacters()
    Dim rng As Range
    Dim i As Long
    
    ' 设置范围为整个文档
    Set rng = ActiveDocument.Content
    
    ' 循环遍历每个字符
    For i = rng.Characters.Count To 1 Step -1
        ' 检查字符是否是中文
        If AscW(rng.Characters(i)) >= 19968 And AscW(rng.Characters(i)) <= 40959 Then
            rng.Characters(i).Delete
        End If
    Next i
    
    MsgBox "所有中文字符已被删除。", vbInformation
End Sub
```

------

## 10、Word宏:将空格替换为下划线

```vbscript
Sub ReplaceSpacesWithUnderscores()
    Dim rng As Range
    Dim para As Paragraph
    Dim txtOld As String
    Dim txtNew As String
    
    ' 禁用屏幕更新以提高性能
    Application.ScreenUpdating = False
    
    ' 遍历文档中的每个段落
    For Each para In ActiveDocument.Paragraphs
        Set rng = para.Range
        txtOld = rng.Text
        
        ' 使用正则表达式替换连续的单词之间的空格为下划线
        txtNew = ReplaceWordsWithUnderscores(txtOld)
        
        ' 如果文本有变化，则更新段落
        If txtOld <> txtNew Then
            rng.Text = txtNew
        End If
    Next para
    
    ' 重新启用屏幕更新
    Application.ScreenUpdating = True
    
    MsgBox "所有单词之间的空格已被替换为下划线。", vbInformation
End Sub

Function ReplaceWordsWithUnderscores(ByVal text As String) As String
    Dim regex As Object
    Set regex = CreateObject("VBScript.RegExp")
    
    With regex
        .Global = True
        .MultiLine = True
        .Pattern = "(\w+)(\s+)(\w+)"
    End With
    
    ReplaceWordsWithUnderscores = regex.Replace(text, "$1_$3")
End Function
```

------

## 11、将单元格16进制颜色码转化为填充

```vbscript
Sub HexToFillColor()
    Dim rng As Range
    Dim cell As Range
    Dim hexColor As String
    Dim red As Long
    Dim green As Long
    Dim blue As Long
    
    ' 选择要处理的范围
    On Error Resume Next
    Set rng = Application.Selection
    On Error GoTo 0
    
    ' 遍历选定范围内的每个单元格
    For Each cell In rng
        hexColor = cell.Value
        
        ' 去掉可能存在的#符号
        If Left(hexColor, 1) = "#" Then hexColor = Mid(hexColor, 2)
        
        ' 确保是一个有效的6位16进制数
        If Len(hexColor) = 6 Then
            ' 分别提取红、绿、蓝分量
            red = CLng("&H" & Mid(hexColor, 1, 2))
            green = CLng("&H" & Mid(hexColor, 3, 2))
            blue = CLng("&H" & Mid(hexColor, 5, 2))
            
            ' 将单元格填充色设置为提取的RGB颜色
            cell.Interior.Color = RGB(red, green, blue)
        End If
    Next cell
End Sub
Sub HexToFillColor()
    Dim rng As Range
    Dim cell As Range
    Dim hexColor As String
    Dim red As Long
    Dim green As Long
    Dim blue As Long
    
    ' 选择要处理的范围
    On Error Resume Next
    Set rng = Application.Selection
    On Error GoTo 0
    
    ' 遍历选定范围内的每个单元格
    For Each cell In rng
        hexColor = cell.Value
        
        ' 去掉可能存在的#符号
        If Left(hexColor, 1) = "#" Then hexColor = Mid(hexColor, 2)
        
        ' 确保是一个有效的6位16进制数
        If Len(hexColor) = 6 Then
            ' 分别提取红、绿、蓝分量
            red = CLng("&H" & Mid(hexColor, 1, 2))
            green = CLng("&H" & Mid(hexColor, 3, 2))
            blue = CLng("&H" & Mid(hexColor, 5, 2))
            
            ' 将单元格填充色设置为提取的RGB颜色
            cell.Interior.Color = RGB(red, green, blue)
        End If
    Next cell
End Sub
Sub HexToFillColor()
    Dim rng As Range
    Dim cell As Range
    Dim hexColor As String
    Dim red As Long
    Dim green As Long
    Dim blue As Long
    
    ' 选择要处理的范围
    On Error Resume Next
    Set rng = Application.Selection
    On Error GoTo 0
    
    ' 遍历选定范围内的每个单元格
    For Each cell In rng
        hexColor = cell.Value
        
        ' 去掉可能存在的#符号
        If Left(hexColor, 1) = "#" Then hexColor = Mid(hexColor, 2)
        
        ' 确保是一个有效的6位16进制数
        If Len(hexColor) = 6 Then
            ' 分别提取红、绿、蓝分量
            red = CLng("&H" & Mid(hexColor, 1, 2))
            green = CLng("&H" & Mid(hexColor, 3, 2))
            blue = CLng("&H" & Mid(hexColor, 5, 2))
            
            ' 将单元格填充色设置为提取的RGB颜色
            cell.Interior.Color = RGB(red, green, blue)
        End If
    Next cell
End Sub

```





