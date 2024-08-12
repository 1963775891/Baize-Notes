import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

def split_file(input_file):
    input_dir = os.path.dirname(input_file)
    input_filename = os.path.basename(input_file)
    input_name, _ = os.path.splitext(input_filename)

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = content.split('\n\n')

    output_dir = os.path.join(input_dir, f"{input_name}_split")
    os.makedirs(output_dir, exist_ok=True)

    count = 0
    for i, part in enumerate(parts, 1):
        if part.strip():
            output_file = os.path.join(output_dir, f"{input_name}_part_{i}.txt")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(part.strip())
            count += 1

    return count, output_dir

def browse_files():
    files = filedialog.askopenfilenames(filetypes=[("Text files", "*.txt")])
    if files:
        file_listbox.delete(0, tk.END)
        for file in files:
            file_listbox.insert(tk.END, file)

def split_files():
    files = file_listbox.get(0, tk.END)
    if not files:
        messagebox.showwarning("警告", "请先选择文件！")
        return

    total_parts = 0
    for file in files:
        count, output_dir = split_file(file)
        total_parts += count

    messagebox.showinfo("完成", f"已处理 {len(files)} 个文件，总共分割出 {total_parts} 个部分。\n保存在各自的 *_split 目录中。")

# 创建主窗口
root = tk.Tk()
root.title("文本文件分割器")
root.geometry("250x100")

# 创建并放置控件
frame = ttk.Frame(root, padding="5")
frame.pack(fill=tk.BOTH, expand=True)

# 创建一个Frame来容纳按钮
button_frame = ttk.Frame(frame)
button_frame.pack(fill=tk.X, pady=5)

browse_button = ttk.Button(button_frame, text="浏览文件", command=browse_files)
browse_button.pack(side=tk.LEFT, padx=(0, 5))

split_button = ttk.Button(button_frame, text="分割文件", command=split_files)
split_button.pack(side=tk.LEFT)

# 创建一个Frame来容纳Listbox和Scrollbar
list_frame = ttk.Frame(frame)
list_frame.pack(fill=tk.BOTH, expand=True, pady=5)

file_listbox = tk.Listbox(list_frame, selectmode=tk.MULTIPLE)
file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# 添加一个垂直滚动条
scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=file_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
file_listbox.config(yscrollcommand=scrollbar.set)

# 运行主循环
root.mainloop()