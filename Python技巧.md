## 0、Python部署

1. 安装

```python
#打开终端（PowerShell或命令提示符）

#导航到你下载Python安装程序的目录。
cd C:\Users\YourUsername\Downloads 

#运行安装程序
python-3.12.3-amd64.exe /quiet InstallAllUsers=1 PrependPath=1

#验证Python安装
python --version
```

2. 将Python加入环境变量

 ```bash
 系统 < 高级系统设置 < 系统属性 < 环境变量，加入Python和Python的Scripts目录路径
 ```

3. 升级

```python
python.exe -m pip install --upgrade pip
```

4. 常见指令

```python
# 运行Python脚本：
python script.py

# 安装Python包：
pip install package_name

# 升级Python包
pip install --upgrade package_name

# 列出已安装的Python包
pip list
    
# 卸载Python包
pip uninstall package_name
```

5. 卸载

```python
#使用以下命令列出所有已安装的Python版本
wmic product where "name like 'Python%%'" get name,version

#卸载指定版本的Python,例如，卸载Python 3.10.0
wmic product where "name='Python 3.10.0'" call uninstall
```

------

## 1、网页爬取并转为Markdown

首先，安装所需的库：

```bash
pip install requests beautifulsoup4 markdownify
```

#### **爬取网页并转换为Markdown保存到桌面：**

```python
import os
import requests
from bs4 import BeautifulSoup
import markdownify

# 目标网页URL
url = 'https://example.com'

# 获取桌面路径
# desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
# 生成输出文件路径
# output_file = os.path.join(desktop_path, 'example.md')

# 指定输出文件夹路径
# output_file = 'C:/指定路径/example.md' 

# 发送GET请求获取网页内容
response = requests.get(url)
html_content = response.text

# 使用BeautifulSoup解析网页内容
soup = BeautifulSoup(html_content, 'html.parser')

# 获取网页的主要内容（根据具体网页结构调整选择器）
main_content = soup.find('div', {'class': 'main-content'})

# 将HTML内容转换为Markdown
markdown_content = markdownify.markdownify(str(main_content), heading_style="ATX")

# 将Markdown内容写入文件
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(markdown_content)

print(f"网页内容已成功转换为Markdown格式并保存到桌面：{output_file}")
```

#### **批量爬取指定网页并将转换为Markdown格式保存到桌面**

```python
import requests
from bs4 import BeautifulSoup
import markdownify
import os

# 目标网页URL
base_url = 'https://www.coze.com'
start_url = 'https://www.coze.com/docs/guides'

# 获取桌面路径
# desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
# 在桌面创建输出文件夹路径
# output_dir = os.path.join(desktop_path, 'example')

# 指定输出文件夹路径
# output_dir = 'C:/指定路径/example'  

# 创建保存Markdown文件的目录
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 发送GET请求获取目录页面内容
response = requests.get(start_url)
html_content = response.text

# 使用BeautifulSoup解析目录页面内容
soup = BeautifulSoup(html_content, 'html.parser')

# 获取所有目录链接（根据具体网页结构调整选择器）
menu_items = soup.select('ul li a')

# 逐一爬取每个目录链接的内容并保存为Markdown文件
for item in menu_items:
    link = item.get('href')
    if link.startswith('/docs/'):
        full_url = base_url + link
        page_response = requests.get(full_url)
        page_content = page_response.text

        page_soup = BeautifulSoup(page_content, 'html.parser')
        main_content = page_soup.find('div', {'class': 'main-content'})

        if main_content:
            markdown_content = markdownify.markdownify(str(main_content), heading_style="ATX")
            # 使用链接的最后一部分作为文件名
            file_name = link.split('/')[-1] + '.md'
            file_path = os.path.join(output_dir, file_name)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(markdown_content)
            print(f"已保存: {file_path}")

print("所有网页内容已成功转换为Markdown格式并保存到桌面。")
```

------

## 视频下载

```python
# 安装所需库
pip install requests beautifulsoup4 imageio[ffmpeg]

# 更新 requests 和 urllib3 库
pip install --upgrade requests urllib3

# 安装所需进度条
pip install requests beautifulsoup4 imageio[ffmpeg] tqdm
```



**下载视频**

直接输入网址或提供的包含多网址的 .txt 文件

```python
# 示例 .txt 文件内容
https://www.example.com/video1
https://www.example.com/video2
https://www.example.com/video3
```
**代码实现**

```python
import os
import requests
from bs4 import BeautifulSoup
import imageio_ffmpeg as ffmpeg
import threading
import signal
import sys
import urllib3
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 禁用不安全请求的警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 全局变量用于控制下载
stop_download = False
video_links_and_names = []

# 常见的请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Connection': 'keep-alive',
}

# 获取网页内容
def get_page_content(url):
    # 使用 Selenium 获取动态加载的内容
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    # 指定 ChromeDriver 路径
    chromedriver_path = os.path.join(os.path.dirname(__file__), 'chromedriver.exe')  # 确保 chromedriver 可执行文件路径正确，Windows 系统需要加上 .exe 后缀
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    
    try:
        # 等待页面加载完成
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'video'))
        )
        page_source = driver.page_source
    finally:
        driver.quit()
    
    return page_source

# 解析网页并获取视频链接和名称
def parse_video_links_and_names(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    video_links_and_names = []

    # 尝试解析不同类型的视频标签
    for idx, video_tag in enumerate(soup.find_all(['video', 'source', 'iframe'])):
        source_tag = video_tag if video_tag.name == 'source' else video_tag.find('source')
        video_src = source_tag.get('src') if source_tag else video_tag.get('src')
        if video_src:
            video_name = video_tag.get('title') or source_tag.get('title') or f"video_{idx + 1}"
            video_links_and_names.append((video_src, video_name))
    
    # 打印调试信息
    if not video_links_and_names:
        print("No video links found.")
        print("HTML content:")
        print(html_content[:1000])  # 打印前1000个字符的HTML内容进行调试
    else:
        for idx, (video_link, video_name) in enumerate(video_links_and_names):
            print(f"Found video {idx + 1}: {video_name}, link: {video_link}")

    return video_links_and_names

# 下载视频文件
def download_video(url, output_dir, video_name):
    global stop_download
    response = requests.get(url, headers=headers, stream=True, verify=False)
    response.raise_for_status()
    filename = os.path.join(output_dir, f"{video_name}{os.path.splitext(url)[1]}")
    total_size = int(response.headers.get('content-length', 0))
    with open(filename, 'wb') as file, tqdm(
        desc=video_name,
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for chunk in response.iter_content(chunk_size=8192):
            if stop_download:
                print("Download stopped.")
                return None
            file.write(chunk)
            bar.update(len(chunk))
    print(f"Downloaded and saved: {filename}")
    return filename

# 下载并合并.ts文件
def download_and_merge_ts_files(m3u8_url, output_file):
    global stop_download
    response = requests.get(m3u8_url, headers=headers, verify=False)
    response.raise_for_status()
    ts_urls = [line.strip() for line in response.text.splitlines() if line and not line.startswith('#')]
    
    ts_files = []
    for ts_url in ts_urls:
        ts_file = download_video(ts_url, os.path.dirname(output_file), os.path.basename(ts_url))
        if ts_file is None:
            return
        ts_files.append(ts_file)
    
    # 合并.ts文件为.mp4
    ffmpeg.input('concat:' + '|'.join(ts_files)).output(output_file, c='copy').run()
    
    # 删除.ts文件
    for ts_file in ts_files:
        os.remove(ts_file)

# 信号处理函数
def signal_handler(sig, frame):
    global stop_download
    print('You pressed Ctrl+C!')
    stop_download = True

# 清理未完成的下载文件
def clean_incomplete_files(output_dir):
    for file in os.listdir(output_dir):
        if file.endswith('.part'):
            os.remove(os.path.join(output_dir, file))

# 下载单个网页的视频
def download_videos_from_page(url, output_dir, indices=None):
    global stop_download
    html_content = get_page_content(url)
    video_links_and_names = parse_video_links_and_names(html_content)
    
    if indices is None:
        indices = range(len(video_links_and_names))
    
    for idx in indices:
        if stop_download:
            break
        video_link, video_name = video_links_and_names[idx]
        try:
            if video_link.endswith('.m3u8'):
                output_file = os.path.join(output_dir, f"{video_name}.mp4")
                download_and_merge_ts_files(video_link, output_file)
            else:
                downloaded_file = download_video(video_link, output_dir, video_name)
                if downloaded_file is None:
                    break
                # 检查下载文件的扩展名
                if downloaded_file.endswith('.ts'):
                    output_file = os.path.join(output_dir, f"{video_name}.mp4")
                    ffmpeg.input(downloaded_file).output(output_file, c='copy').run()
                    os.remove(downloaded_file)  # 删除原始.ts文件
                else:
                    print(f"Downloaded and saved: {downloaded_file}")
        except Exception as e:
            print(f"Failed to download {video_name}: {e}")

# 主函数
def main():
    global stop_download
    signal.signal(signal.SIGINT, signal_handler)
    
    # 第一步：提示用户输入下载的视频网址
    url_input = input("请输入下载的视频网址或包含多网址的.txt文件路径：").strip()
    urls = []
    if os.path.isfile(url_input) and url_input.endswith('.txt'):
        with open(url_input, 'r') as file:
            urls = [line.strip() for line in file.readlines()]
    else:
        urls.append(url_input)
    
    # 第二步：提示用户输入视频要输出的目录路径
    output_dir = input("请输入视频要输出的目录路径：").strip()
    os.makedirs(output_dir, exist_ok=True)
    
    # 清理未完成的下载文件
    clean_incomplete_files(output_dir)
    
    # 第三步：列出网址下的视频并按数字排序为目录
    for url in urls:
        html_content = get_page_content(url)
        video_links_and_names = parse_video_links_and_names(html_content)
        
        print("即将下载的视频目录:")
        for idx, (video_link, video_name) in enumerate(video_links_and_names):
            print(f"{idx + 1}. 视频名称: {video_name}, 视频链接: {video_link}")
        
        user_input = input("请输入要下载的视频序号（用逗号分隔，直接回车即为全部下载）：")
        if user_input.strip():
            indices = [int(x) - 1 for x in user_input.split(',')]
        else:
            indices = None
        
        download_videos_from_page(url, output_dir, indices)

if __name__ == '__main__':
    main()
```

```
# 代码说明
1.全局变量控制下载：使用 stop_download 变量来控制下载的暂停或停止。
2.信号处理函数：使用 signal 库注册信号处理函数，当用户按下 Ctrl+C 时，3.设置 stop_download 变量为 True，以停止下载。
清理未完成的下载文件：在开始新的下载前，清理未完成的 .part 文件。
4.解析视频链接和名称：使用 BeautifulSoup 解析网页内容，提取视频链接和名称。
5.列出即将下载的视频目录：在下载视频前列出视频目录，包括视频名称和链接，并按数字排序。
6.获取用户输入：用户可以输入要下载的视频序号（用逗号分隔），或者直接回车下载全部视频。
7.下载视频文件：在下载过程中检查 stop_download 变量，如果为 True，则停止下载。使用视频名称命名文件。
8.下载并合并 .ts 文件：如果视频链接是 .m3u8 文件，下载所有 .ts 文件并使用 ffmpeg 合并为 .mp4 文件，最后删除 .ts 文件。
9.多线程下载：使用多线程并行下载多个网页的视频，每个线程处理一个网页。
# 注意事项
	反爬虫机制：某些网站可能有反爬虫机制，你可能需要模拟浏览器行为或使用合适的请求头。
	合法性：确保你爬取和下载的视频内容符合版权和使用协议。
	路径处理：确保 output_dir 路径存在，如果不存在可以使用 os.makedirs 创建。
```

