// ==UserScript==
// @name         Enhanced Image Downloader
// @namespace    http://tampermonkey.net/
// @version      0.2
// @description  Download PNG and JPG images from the current page with size filtering
// @match        *://*/*
// @grant        GM_download
// ==/UserScript==

(function() {
    'use strict';

    // 创建控制面板
    const panel = document.createElement('div');
    panel.style.cssText = `
        position: fixed;
        left: 20px;
        bottom: 20px;
        background-color: #f3f3f3;
        border-radius: 8px;
        padding: 5px;
        z-index: 9999;
        display: flex;
        align-items: center;
    `;

    // 创建输入框和标签
    const createInput = (placeholder) => {
        const input = document.createElement('input');
        input.type = 'number';
        input.placeholder = placeholder;
        input.style.cssText = `
            width: 55px;
            height: 25px;
            margin: 0 5px;
            padding: 5px;
            border: 1px solid #ccc;
            border-radius: 8px;
        `;
        return input;
    };

    const widthInput = createInput('宽度');
    const heightInput = createInput('高度');

    // 创建下载按钮
    const button = document.createElement('button');
    button.textContent = 'Go';
    button.style.cssText = `
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 5px 10px;
        border-radius: 8px;
        cursor: pointer;
        margin-left: 10px;
    `;

    panel.appendChild(document.createTextNode('尺寸: '));
    panel.appendChild(widthInput);
    panel.appendChild(document.createTextNode('x'));
    panel.appendChild(heightInput);
    panel.appendChild(button);

    document.body.appendChild(panel);

    // 创建进度条
    const progressBar = document.createElement('div');
    progressBar.style.cssText = `
        width: 100%;
        height: 5px;
        background-color: #ddd;
        border-radius: 5px;
        margin-top: 10px;
        display: none;
    `;
    const progressInner = document.createElement('div');
    progressInner.style.cssText = `
        width: 0%;
        height: 100%;
        background-color: #4CAF50;
        border-radius: 8px;
        transition: width 0.5s;
    `;
    progressBar.appendChild(progressInner);
    panel.appendChild(progressBar);

    // 下载函数
    function downloadImages() {
        const minWidth = parseInt(widthInput.value) || 0;
        const minHeight = parseInt(heightInput.value) || 0;

        const images = [...document.getElementsByTagName('img')];
        const filteredImages = images.filter(img => {
            return (img.naturalWidth >= minWidth || minWidth === 0) && 
                   (img.naturalHeight >= minHeight || minHeight === 0) &&
                   (img.src.endsWith('.png') || img.src.endsWith('.jpg') || img.src.endsWith('.jpeg')|| img.src.endsWith('.gif')|| img.src.endsWith('.svg'));
        });

        const totalImages = filteredImages.length;
        let downloadedImages = 0;

        if (totalImages === 0) {
            alert('没有找到符合条件的图片');
            return;
        }

        progressBar.style.display = 'block';

        filteredImages.forEach((img, index) => {
            const src = img.src;
            const filename = src.split('/').pop();
            setTimeout(() => {
                GM_download(src, filename);
                downloadedImages++;
                progressInner.style.width = `${(downloadedImages / totalImages) * 100}%`;
                if (downloadedImages === totalImages) {
                    setTimeout(() => {
                        progressBar.style.display = 'none';
                        progressInner.style.width = '0%';
                    }, 1000);
                }
            }, index * 200);  // 每200ms下载一张图片，避免同时发起过多请求
        });
    }

    // 添加点击事件
    button.addEventListener('click', downloadImages);
})();
