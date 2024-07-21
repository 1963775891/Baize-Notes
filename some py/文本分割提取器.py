import sys
import os
import re
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QLabel, QFileDialog, QLineEdit, QTextEdit
from PyQt5.QtGui import QFont

class AdvancedTextProcessorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.selected_files = []

    def initUI(self):
        self.setWindowTitle('高级文本处理器')
        self.setGeometry(200, 200, 300, 400)

        main_layout = QVBoxLayout()

        help_label = QLabel("请选择要处理的文本文件，输入分割符或正则表达式，然后点击相应按钮。\n处理后的文件将保存在源文件同目录下的'out'文件夹中。")
        help_label.setFont(QFont('Arial', 10))
        main_layout.addWidget(help_label)

        self.file_list = QListWidget()
        main_layout.addWidget(self.file_list)

        self.input_box = QLineEdit()
        regex_hints = (
            "选择需要分割的文本"
        
        )
        self.input_box.setPlaceholderText(regex_hints)
        main_layout.addWidget(self.input_box)

  

        button_layout = QHBoxLayout()

        browse_button = QPushButton('浏览')
        browse_button.clicked.connect(self.browseFiles)
        button_layout.addWidget(browse_button)

        split_button = QPushButton('分割')
        split_button.clicked.connect(self.executeSplit)
        button_layout.addWidget(split_button)

        extract_button = QPushButton('提取')
        extract_button.clicked.connect(self.executeExtract)
        button_layout.addWidget(extract_button)

        main_layout.addLayout(button_layout)

        self.result_box = QTextEdit()
        self.result_box.setReadOnly(True)
        main_layout.addWidget(self.result_box)

        self.setLayout(main_layout)

        self.showMessage(f"正则表达式书写：\n\n"
        ".:任意字符   *:多个   ?：前面字符   \\n:换行   \\r:手动换行\n\n"
        "\\t:制表符   \\s:空白   \\d:数字   \\w:字母数字\n\n"
        "示例：\\d+ 匹配一个或多个数字")

    def browseFiles(self):
        files, _ = QFileDialog.getOpenFileNames(self, "选择文本文件", "", "Text Files (*.txt);;All Files (*)")
        if files:
            self.selected_files = files
            self.file_list.clear()
            self.file_list.addItems([os.path.basename(f) for f in files])

    def executeSplit(self):
        if not self.selected_files:
            self.showMessage("请先选择要处理的文件。")
            return

        delimiter = self.input_box.text().strip() or '\n'  # 如果未输入，默认按段落分割
        for file_path in self.selected_files:
            self.splitTextFile(file_path, delimiter)

        self.showMessage(f"分割完成。处理后的文件已保存在各源文件同目录下的'out'文件夹中。")

    def executeExtract(self):
        if not self.selected_files:
            self.showMessage("请先选择要处理的文件。")
            return

        pattern = self.input_box.text().strip()
        if not pattern:
            self.showMessage("请输入要提取的正则表达式。")
            return

        for file_path in self.selected_files:
            self.extractTextFile(file_path, pattern)

        self.showMessage(f"提取完成。处理后的文件已保存在各源文件同目录下的'out'文件夹中。")

    def splitTextFile(self, file_path, delimiter):
        output_dir = os.path.join(os.path.dirname(file_path), 'out')
        os.makedirs(output_dir, exist_ok=True)

        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        parts = content.split(delimiter)

        base_name = os.path.splitext(os.path.basename(file_path))[0]
        for i, part in enumerate(parts, 1):
            if part.strip():
                output_file = os.path.join(output_dir, f"{base_name}_split_{i}.txt")
                with open(output_file, 'w', encoding='utf-8') as out_file:
                    out_file.write(part.strip())

    def extractTextFile(self, file_path, pattern):
        output_dir = os.path.join(os.path.dirname(file_path), 'out')
        os.makedirs(output_dir, exist_ok=True)

        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        matches = re.findall(pattern, content)

        base_name = os.path.splitext(os.path.basename(file_path))[0]
        output_file = os.path.join(output_dir, f"{base_name}_extracted.txt")
        with open(output_file, 'w', encoding='utf-8') as out_file:
            for match in matches:
                out_file.write(f"{match}\n")

        self.result_box.setText(f"在文件 {base_name} 中找到并提取了 {len(matches)} 个匹配项。")

    def showMessage(self, message):
        self.result_box.setText(message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AdvancedTextProcessorApp()
    ex.show()
    sys.exit(app.exec_())
