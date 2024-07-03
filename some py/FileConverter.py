import os
import tkinter as tk
from tkinter import ttk, messagebox
import pdfplumber
import threading
import pdfkit
import sys
from PIL import Image

class FileConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("文件转换器")
        self.master.geometry("400x200")

        self.label = tk.Label(master, text="请输入转化文件的路径:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, width=50)
        self.entry.pack(pady=5)

        button_frame = tk.Frame(master)
        button_frame.pack(pady=10)

        self.pdf_to_md_button = tk.Button(button_frame, text="PDF转MD", command=self.start_pdf_to_md)
        self.pdf_to_md_button.pack(side=tk.LEFT, padx=5)

        self.html_to_pdf_button = tk.Button(button_frame, text="HTML转PDF", command=self.start_html_to_pdf)
        self.html_to_pdf_button.pack(side=tk.LEFT, padx=5)

        self.hint = tk.Label(master, text="点击按钮执行，Ctrl+C 切换暂停/继续")
        self.hint.pack(pady=5)

        self.progress = ttk.Progressbar(master, orient="horizontal", mode="determinate", length=350)
        self.progress.pack(pady=10)

        self.status = tk.Label(master, text="")
        self.status.pack(pady=5)

        self.pause_event = threading.Event()
        self.pause_event.set()

        # 动态设置 wkhtmltopdf 的路径
        if getattr(sys, 'frozen', False):
            # 如果是打包后的可执行文件
            wkhtmltopdf_path = os.path.join(sys._MEIPASS, 'wkhtmltopdf.exe')
        else:
            # 如果是直接运行的脚本
            wkhtmltopdf_path = r'D:\Software\wkhtmltopdf\bin\wkhtmltopdf.exe'  # 替换为实际路径

        # 确保 wkhtmltopdf 可执行文件存在
        if not os.path.exists(wkhtmltopdf_path):
            raise FileNotFoundError(f'wkhtmltopdf not found at {wkhtmltopdf_path}')
            # 更新 pdfkit 配置
        self.config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

    def toggle_pause(self, event):
        if self.pause_event.is_set():
            self.pause_event.clear()
            self.status.config(text="已暂停...")
        else:
            self.pause_event.set()
            self.status.config(text="继续...")

    def start_pdf_to_md(self):
        input_dir = self.entry.get()
        if not os.path.isdir(input_dir):
            messagebox.showerror("错误", "目录不存在。")
            return

        self.output_dir = os.path.join(input_dir, "Outfiles")
        os.makedirs(self.output_dir, exist_ok=True)
        self.status.config(text="处理中...")

        self.conversion_thread = threading.Thread(target=self.convert_pdfs, args=(input_dir,))
        self.conversion_thread.start()

        self.master.bind("<Control-c>", self.toggle_pause)

    def convert_pdfs(self, pdf_dir):
        pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith(".pdf")]
        total_files = len(pdf_files)
        self.progress["maximum"] = total_files

        for i, pdf_file in enumerate(pdf_files, 1):
            self.pause_event.wait()  # 检查暂停
            pdf_path = os.path.join(pdf_dir, pdf_file)
            md_path = os.path.join(self.output_dir, f"{os.path.splitext(pdf_file)[0]}.md")
            img_dir = os.path.join(self.output_dir, "img")
            os.makedirs(img_dir, exist_ok=True)

            self.process_pdf(pdf_path, md_path, img_dir)
            self.progress["value"] = i
            self.status.config(text=f"已处理 {i}/{total_files} 个文件")

        self.status.config(text="转换完成!")

    def process_pdf(self, pdf_path, md_path, img_dir):
        md_text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    md_text += text + "\n"
                
                for j, img in enumerate(page.images):
                    try:
                        img_bbox = self.adjust_bbox(img, page.width, page.height)
                        if img_bbox:
                            img_obj = page.within_bbox(img_bbox).to_image()
                            img_path = os.path.join(img_dir, f"{os.path.splitext(os.path.basename(pdf_path))[0]}_img_{i+1}_{j+1}.png")
                            img_obj.save(img_path)
                            relative_img_path = os.path.relpath(img_path, os.path.dirname(md_path))
                            md_text += f"![Image]({relative_img_path})\n"
                        else:
                            print(f"警告: 图像在页面 {i+1} 完全在页面边界之外，无法处理.")
                    except Exception as e:
                        print(f"警告: 无法处理页面 {i+1} 上的图像. Error: {e}")
                        continue

        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_text)

    def adjust_bbox(self, img, page_width, page_height):
        x0, top, x1, bottom = img['x0'], img['top'], img['x1'], img['bottom']
        
        # 检查图像是否完全位于页面之外
        if x0 > page_width or x1 < 0 or top > page_height or bottom < 0:
            return None

        # 调整边界框，使其适合页面大小
        x0 = max(0, min(x0, page_width))
        x1 = max(0, min(x1, page_width))
        top = max(0, min(top, page_height))
        bottom = max(0, min(bottom, page_height))

        # 确保框架有正面区域
        if x1 <= x0 or bottom <= top:
            return None

        return (x0, top, x1, bottom)

    def start_html_to_pdf(self):
        input_directory = self.entry.get().strip()
        if not os.path.isdir(input_directory):
            messagebox.showerror("错误", "目录不存在。")
            return

        self.conversion_thread = threading.Thread(target=self.convert_html_to_pdf, args=(input_directory,))
        self.conversion_thread.start()

        self.master.bind("<Control-c>", self.toggle_pause)

    def convert_html_to_pdf(self, input_directory):
        input_directory = os.path.abspath(input_directory)
        output_directory = os.path.join(input_directory, 'Outfiles')

        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        html_files = [f for f in os.listdir(input_directory) if f.endswith('.html')]

        total_files = len(html_files)
        self.progress["maximum"] = total_files

        for index, html_file in enumerate(html_files):
            self.pause_event.wait()  # 检查暂停
            input_html_path = os.path.join(input_directory, html_file)
            output_pdf_path = os.path.join(output_directory, os.path.splitext(html_file)[0] + '.pdf')
            
            try:
                pdfkit.from_file(input_html_path, output_pdf_path, configuration=self.config)
                self.status.config(text=f"已处理 {index + 1}/{total_files} 个文件")
            except Exception as e:
                self.status.config(text=f"转换 {html_file} 失败. 错误: {e}")
            
            self.progress["value"] = index + 1

        self.status.config(text="转换完成!")

def run_app():
    root = tk.Tk()
    app = FileConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_app()