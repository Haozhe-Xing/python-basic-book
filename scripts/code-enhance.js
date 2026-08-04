// code-enhance.js — 代码块视觉增强（语言标签 + 复制按钮）
(function () {
  document.addEventListener("DOMContentLoaded", function () {
    var pres = document.querySelectorAll("pre");
    pres.forEach(function (pre) {
      // 1) 提取语言标签
      var cls = pre.className || "";
      var lang = "text";
      if (/language-(\w+)/i.test(cls)) {
        lang = RegExp.$1.toUpperCase();
      } else if (pre.querySelector('code[class*="language-"]')) {
        var codeCls = pre.querySelector('code').className || "";
        if (/language-(\w+)/i.test(codeCls)) {
          lang = RegExp.$1.toUpperCase();
        }
      }
      pre.setAttribute("data-lang", lang);

      // 2) 添加复制按钮
      if (!pre.querySelector(".code-copy-btn")) {
        var btn = document.createElement("span");
        btn.className = "code-copy-btn";
        btn.textContent = "复制";
        btn.setAttribute("title", "点击复制代码");
        pre.style.position = "relative";
        pre.appendChild(btn);
        btn.addEventListener("click", function () {
          var code = pre.querySelector("code") || pre;
          var text = code.textContent || code.innerText;
          navigator.clipboard.writeText(text).then(function () {
            btn.textContent = "✓ 已复制!";
            setTimeout(function () { btn.textContent = "复制"; }, 1800);
          }).catch(function () {
            btn.textContent = "失败";
            setTimeout(function () { btn.textContent = "复制"; }, 1500);
          });
        });
      }
    });

    // 3) <details> 折叠框：给 summary 加 emoji 前缀装饰（可选）
    var summaries = document.querySelectorAll("details > summary:first-child");
    summaries.forEach(function (s) {
      // 如果 summary 文本以 💡 开头，说明已有 emoji，不重复加
      if (s.textContent.match(/^[\p{Emoji_Presentation}\s]/u)) return;
    });
  });
})();
