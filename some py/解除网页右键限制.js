// ==UserScript==
// @name         Enable Right Click
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Removes right-click restrictions on websites
// @match        *://*/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    function enableRightClick() {
        document.oncontextmenu = null;
        document.onselectstart = null;
        document.ondragstart = null;
        document.onmousedown = null;
        document.body.oncontextmenu = null;
        document.body.onselectstart = null;
        document.body.ondragstart = null;
        document.body.onmousedown = null;
        document.body.oncut = null;
        document.body.oncopy = null;
        document.body.onpaste = null;
    }

    // Run the function when the page loads
    enableRightClick();

    // Also run the function periodically in case the page dynamically adds restrictions
    setInterval(enableRightClick, 1000);
})();
