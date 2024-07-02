import tkinter as tk
from tkinter import ttk, messagebox
import os
from gptpdf import parse_pdf
import threading

class PDFMDUI:
    def __init__(self, master):
        self.master = master
        master.title("PDF批量转MD工具")
        master.geometry("400x180")

        # PDF输入目录
        tk.Label(master, text="PDF输入目录:").pack(pady=5)
        self.pdf_dir = tk.Entry(master, width=50)
        self.pdf_dir.pack()

        # MD输出目录
        tk.Label(master, text="MD输出目录:").pack(pady=5)
        self.md_dir = tk.Entry(master, width=50)
        self.md_dir.pack()

        # 执行按钮
        self.execute_button = tk.Button(master, text="执行", command=self.execute)
        self.execute_button.pack(pady=20)

        # 进度条
        self.progress = ttk.Progressbar(master, length=400, mode='determinate')
        self.progress.pack(pady=10)

        # 状态标签
        self.status_label = tk.Label(master, text="")
        self.status_label.pack()

    def execute(self):
        pdf_dir = self.pdf_dir.get()
        md_dir = self.md_dir.get()
        
        if not pdf_dir or not md_dir:
            messagebox.showerror("错误", "请填写PDF输入目录和MD输出目录")
            return

        if not os.path.exists(pdf_dir):
            messagebox.showerror("错误", "PDF输入目录不存在")
            return

        if not os.path.exists(md_dir):
            os.makedirs(md_dir)

        # 获取所有PDF文件
        pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]
        
        if not pdf_files:
            messagebox.showinfo("提示", "指定目录中没有找到PDF文件")
            return

        self.execute_button.config(state=tk.DISABLED)
        self.progress['value'] = 0
        self.status_label.config(text="开始批处理...")

        # 在新线程中执行批处理
        thread = threading.Thread(target=self.process_pdfs, args=(pdf_dir, md_dir, pdf_files))
        thread.start()

    def process_pdfs(self, pdf_dir, md_dir, pdf_files):
        total_files = len(pdf_files)
        for i, pdf_file in enumerate(pdf_files, 1):
            try:
                pdf_path = os.path.join(pdf_dir, pdf_file)
                output_dir = os.path.join(md_dir, os.path.splitext(pdf_file)[0])
                os.makedirs(output_dir, exist_ok=True)

                self.status_label.config(text=f"处理 {pdf_file} ({i}/{total_files})")

                def update_progress(progress):
                    total_progress = (i - 1 + progress / 100) / total_files * 100
                    self.progress['value'] = total_progress
                    self.master.update_idletasks()

                parse_pdf(
                    pdf_path,
                    output_dir='./', 
                    api_key=None,
                    base_url=None,
                    model='gpt-4o',
                    verbose=False,
                )

            except Exception as e:
                messagebox.showerror("错误", f"处理 {pdf_file} 时出错: {str(e)}")

        self.status_label.config(text="批处理完成")
        self.execute_button.config(state=tk.NORMAL)
        messagebox.showinfo("完成", f"已处理 {total_files} 个PDF文件")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMDUI(root)
    root.mainloop()