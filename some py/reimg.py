import tkinter as tk
from tkinter import filedialog, messagebox
import re
import shutil
import os

def remove_duplicate_images(input_file):
    # 自动创建副本
    output_file = input_file.replace('.md', '_backup.md')
    shutil.copy(input_file, output_file)
    
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # 使用正则表达式查找所有图片引用，包括网络图片
    image_pattern = re.compile(r'!\[.*?\]\((https?://.*?)\)')
    images = image_pattern.findall(content)

    # 查找重复的图片
    seen = set()
    unique_images = []
    for image in images:
        if image not in seen:
            unique_images.append(image)
            seen.add(image)
    
    # 重新生成Markdown内容，删除重复图片
    for image in unique_images:
        first_occurrence = True
        content_lines = content.split('\n')
        for i, line in enumerate(content_lines):
            if f'({image})' in line:
                if first_occurrence:
                    first_occurrence = False
                else:
                    content_lines[i] = ''
        content = '\n'.join(content_lines)

    with open(input_file, 'w', encoding='utf-8') as file:
        file.write(content)

    messagebox.showinfo("完成", "重复的图片引用已删除，并已创建副本：\n" + output_file)

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Markdown files", "*.md")])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def execute_script():
    input_file = file_entry.get()
    if not input_file:
        messagebox.showwarning("警告", "请选择Md文件")
        return
    if not os.path.exists(input_file):
        messagebox.showwarning("警告", "选择的文件不存在")
        return

    remove_duplicate_images(input_file)

# 创建主窗口
root = tk.Tk()
root.title("删除重复图片引用")

# 创建并放置组件
file_label = tk.Label(root, text="选择Md文件：")
file_label.grid(row=0, column=0, padx=10, pady=10)

file_entry = tk.Entry(root, width=20)
file_entry.grid(row=0, column=1, padx=10, pady=10)

browse_button = tk.Button(root, text="浏览", command=browse_file)
browse_button.grid(row=0, column=2, padx=10, pady=10)

execute_button = tk.Button(root, text="执行", command=execute_script)
execute_button.grid(row=1, column=1, padx=10, pady=10)

# 运行主循环
root.mainloop()
