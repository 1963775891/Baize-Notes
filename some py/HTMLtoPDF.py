# HTMLtoPDF.py

import os
import pdfkit
import time
import threading
import signal
import sys
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# 动态设置 wkhtmltopdf 的路径
if getattr(sys, 'frozen', False):
    # 如果是打包后的可执行文件
    wkhtmltopdf_path = os.path.join(sys._MEIPASS, 'wkhtmltopdf.exe')
else:
    # 如果是直接运行的脚本
    wkhtmltopdf_path = r'C:\path\to\wkhtmltopdf\bin\wkhtmltopdf.exe'  # 替换为实际路径

# 确保 wkhtmltopdf 可执行文件存在
if not os.path.exists(wkhtmltopdf_path):
    raise FileNotFoundError(f'wkhtmltopdf not found at {wkhtmltopdf_path}')

# 更新 pdfkit 配置
config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

# 初始化暂停标志
pause_flag = threading.Event()
pause_flag.set()  # 设置初始状态为继续

def convert_html_to_pdf(input_directory):
    input_directory = os.path.abspath(input_directory)  # 获取绝对路径
    # 设置输出目录
    output_directory = os.path.join(input_directory, 'Outfiles')

    # 如果输出目录不存在，则创建
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # 获取输入目录中所有HTML文件的列表
    html_files = [f for f in os.listdir(input_directory) if f.endswith('.html')]

    total_files = len(html_files)
    for index, html_file in enumerate(html_files):
        input_html_path = os.path.join(input_directory, html_file)
        output_pdf_path = os.path.join(output_directory, os.path.splitext(html_file)[0] + '.pdf')
        
        try:
            pdfkit.from_file(input_html_path, output_pdf_path, configuration=config)
            print(f'[{index + 1}/{total_files}] 成功将 {html_file} 转换为 PDF.')
        except Exception as e:
            print(f'[{index + 1}/{total_files}] 转换 {html_file} 失败. 错误: {e}')
        
        # 更新进度条
        progress_var.set((index + 1) / total_files * 100)
        
        # 检查暂停标志
        while not pause_flag.is_set():
            time.sleep(0.1)

def pause_conversion(signum, frame):
    if pause_flag.is_set():
        pause_flag.clear()
        print('处理已暂停. 按 Ctrl+C 继续处理.')
    else:
        pause_flag.set()
        print('处理已继续.')

# 绑定 Ctrl+C 信号处理函数
signal.signal(signal.SIGINT, pause_conversion)

def on_submit(event=None):
    input_directory = entry.get().strip()
    if not input_directory:
        messagebox.showwarning("输入错误", "请输入HTML文件的目录路径")
        return

    conversion_thread = threading.Thread(target=convert_html_to_pdf, args=(input_directory,))
    conversion_thread.start()

# 创建主窗口
root = tk.Tk()
root.title("HTML to PDF Converter")

# 创建并放置文本框和标签
label = tk.Label(root, text="请输入HTML文件的目录路径:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)
entry.bind("<Return>", on_submit)
entry.insert(0, " ")  # 提示信息

hint_label = tk.Label(root, text="回车执行，Ctrl+C切换暂停和继续转换")
hint_label.pack(pady=10)

# 创建进度条
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
progress_bar.pack(pady=10, fill=tk.X, padx=20)

# 运行主循环
root.mainloop()
