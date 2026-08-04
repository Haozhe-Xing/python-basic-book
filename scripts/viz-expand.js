// viz-expand.js — 交互式可视化 Lightbox 放大支持
// 章节通过 <iframe src="...html?embed&vizId=ID"> 嵌入可视化时，
// 本脚本允许在 iframe 内通过 postMessage 请求父页面放大/还原。
(function () {
  function isEmbed() {
    return /[?&]embed\b/.test(window.location.search) ||
           window.self !== window.top;
  }
  if (!isEmbed()) return; // 仅在 iframe 内生效

  document.addEventListener("dblclick", function () {
    try {
      window.parent.postMessage({ type: "viz-expand", vizId: getVizId() }, "*");
    } catch (e) {}
  });

  function getVizId() {
    var m = window.location.search.match(/vizId=([^&]+)/);
    return m ? m[1] : null;
  }
})();
