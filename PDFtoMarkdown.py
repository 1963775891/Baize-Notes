import os
import tkinter as tk
from tkinter import ttk, messagebox
import pdfplumber
import threading
from PIL import Image

class PDFtoMarkdownApp:
    def __init__(self, master):
        self.master = master
        self.master.title("PDF转Markdown")
        self.master.geometry("300x150")

        self.label = tk.Label(master, text="请输入PDF文件的目录路径:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, width=39)
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", self.start_conversion)

        self.hint = tk.Label(master, text="回车执行，Ctrl+C 切换暂停/继续")
        self.hint.pack(pady=5)

        self.progress = ttk.Progressbar(master, orient="horizontal", mode="determinate", length=280)
        self.progress.pack(pady=10)

        self.status = tk.Label(master, text="")
        self.status.pack(pady=5)

        self.pause_event = threading.Event()
        self.pause_event.set()

    def start_conversion(self, event):
        pdf_dir = self.entry.get()
        if not os.path.isdir(pdf_dir):
            messagebox.showerror("Error", "Directory does not exist.")
            return

        self.output_dir = os.path.join(pdf_dir, "Outfiles")
        os.makedirs(self.output_dir, exist_ok=True)
        self.status.config(text="Processing...")

        self.conversion_thread = threading.Thread(target=self.convert_pdfs, args=(pdf_dir,))
        self.conversion_thread.start()

        self.master.bind("<Control-c>", self.toggle_pause)

    def toggle_pause(self, event):
        if self.pause_event.is_set():
            self.pause_event.clear()
            self.status.config(text="Paused...")
        else:
            self.pause_event.set()
            self.status.config(text="Resuming...")

    def convert_pdfs(self, pdf_dir):
        pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith(".pdf")]
        total_files = len(pdf_files)
        self.progress["maximum"] = total_files

        for i, pdf_file in enumerate(pdf_files, 1):
            self.pause_event.wait()  # Check for pause
            pdf_path = os.path.join(pdf_dir, pdf_file)
            md_path = os.path.join(self.output_dir, f"{os.path.splitext(pdf_file)[0]}.md")
            img_dir = os.path.join(self.output_dir, "img")
            os.makedirs(img_dir, exist_ok=True)

            self.process_pdf(pdf_path, md_path, img_dir)
            self.progress["value"] = i
            self.status.config(text=f"Processed {i}/{total_files} files")

        self.status.config(text="Conversion complete!")

    def process_pdf(self, pdf_path, md_path, img_dir):
        md_text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    md_text += text + "\n"
                
                # Extract images
                for j, img in enumerate(page.images):
                    img_bbox = (img['x0'], img['top'], img['x1'], img['bottom'])
                    img_obj = page.within_bbox(img_bbox).to_image()
                    img_path = os.path.join(img_dir, f"{os.path.splitext(os.path.basename(pdf_path))[0]}_img_{i+1}_{j+1}.png")
                    img_obj.save(img_path)
                    relative_img_path = os.path.relpath(img_path, os.path.dirname(md_path))
                    md_text += f"![Image]({relative_img_path})\n"

        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_text)

def run_app():
    root = tk.Tk()
    app = PDFtoMarkdownApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_app()
