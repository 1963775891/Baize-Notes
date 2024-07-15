import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from itertools import product

class ImageSplitter:
    def __init__(self, master):
        self.master = master
        master.title("矩阵分割")

        # Instruction label
        tk.Label(master, text="请输入分割的行数和列数", width=36).grid(row=0, column=0, columnspan=2, pady=(10, 4))

       # 行和列输入在同一行
        input_frame = tk.Frame(master)
        input_frame.grid(row=1, column=0, columnspan=2, pady=4)


   
        self.row_entry = tk.Entry(input_frame, width=8)
        self.row_entry.pack(side=tk.LEFT)
        
        tk.Label(input_frame, text="*").pack(side=tk.LEFT, padx=4)
        
        self.col_entry = tk.Entry(input_frame, width=8)
        self.col_entry.pack(side=tk.LEFT)

        # Browse button
        self.browse_button = tk.Button(master, text="选择图片", command=self.browse_files, width=20)
        self.browse_button.grid(row=2, column=0, columnspan=2, pady=2)

        # Execute button
        self.execute_button = tk.Button(master, text="OK", command=self.execute, width=20)
        self.execute_button.grid(row=3, column=0, columnspan=2, pady=16)

        self.files = []

    def browse_files(self):
        self.files = filedialog.askopenfilenames(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
        # 删除选择文件时的提示

    def execute(self):
        if not self.files:
            messagebox.showerror("Error", "No files selected")
            return

        rows = self.row_entry.get() or None
        cols = self.col_entry.get() or None

        for file in self.files:
            self.split_image(file, rows, cols)

        messagebox.showinfo("Success", "Image splitting completed")

    def split_image(self, filename, rows=None, cols=None):
        img = Image.open(filename)
        w, h = img.size

        if not rows and not cols:
            # 根据图像大小自动检测行和列
            aspect_ratio = w / h
            rows = int((aspect_ratio * 3) ** 0.5)
            cols = int(rows * aspect_ratio)
        else:
            rows = int(rows) if rows else 1
            cols = int(cols) if cols else 1

        tile_w, tile_h = w // cols, h // rows

        # 创建输出目录
        base_name = os.path.splitext(os.path.basename(filename))[0]
        output_dir = os.path.join(os.path.dirname(filename), base_name)
        os.makedirs(output_dir, exist_ok=True)

        for i, j in product(range(rows), range(cols)):
            box = (j * tile_w, i * tile_h, (j + 1) * tile_w, (i + 1) * tile_h)
            out = os.path.join(output_dir, f'{base_name}_{i}_{j}.png')
            img.crop(box).save(out)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageSplitter(root)
    root.mainloop()