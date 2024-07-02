import PyInstaller.__main__
import os

# 获取当前脚本所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 设置图标文件路径（如果有的话）
# icon_path = os.path.join(current_dir, 'icon.ico')

PyInstaller.__main__.run([
    'pdfmd.py',
    '--onefile',
    '--windowed',
    '--name=PDF批量转MD工具',
    '--icon', 'C:/Users/Misla/Downloads/gptpdf/Exchange.ico',  # 如果有图标文件，取消这行的注释
    '--add-data=pdfmd.py:.',  # 添加gptpdf.py作为数据文件
])

