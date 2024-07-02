// ==UserScript==
// @name         提取data-link链接
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  提取页面中所有data-link属性的值并下载为txt文件
// @match        *://*/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // 创建按钮
    function createButton() {
        const button = document.createElement('button');
        button.textContent = '提取link';
        button.style.position = 'fixed';
        button.style.left = '10px';
        button.style.bottom = '10px';
        button.style.zIndex = '9999';
        button.style.padding = '10px';
        button.style.backgroundColor = '#4CAF50';
        button.style.color = 'white';
        button.style.border = 'none';
        button.style.borderRadius = '5px';
        button.style.cursor = 'pointer';
        button.addEventListener('click', extractLinks);
        document.body.appendChild(button);
    }

    // 提取链接并下载
    function extractLinks() {
        const links = Array.from(document.querySelectorAll('[data-link]'))
                           .map(el => el.getAttribute('data-link'));

        if (links.length === 0) {
            alert('没有找到data-link链接！');
            return;
        }

        const content = links.join('\n');
        const blob = new Blob([content], {type: 'text/plain;charset=utf-8'});
        const a = document.createElement('a');
        a.href = URL.createObjectURL(blob);
        a.download = 'data_links.txt';
        a.style.display = 'none';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    }

    // 页面加载完成后创建按钮
    window.addEventListener('load', createButton);
})();