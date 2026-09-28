// code-enhance.js — 代码块视觉增强（语言标签、可访问复制按钮、引用块语义）
(function () {
  function getCodeText(pre, button, status) {
    var code = pre.querySelector("code");
    if (code) return code.textContent || code.innerText || "";

    return Array.prototype.slice.call(pre.childNodes)
      .filter(function (node) { return node !== button && node !== status; })
      .map(function (node) { return node.textContent || ""; })
      .join("");
  }

  function copyWithFallback(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text).catch(function () {
        return copyUsingTextarea(text);
      });
    }
    return copyUsingTextarea(text);
  }

  function copyUsingTextarea(text) {
    return new Promise(function (resolve, reject) {
      var textarea = document.createElement("textarea");
      textarea.value = text;
      textarea.setAttribute("readonly", "");
      textarea.style.position = "fixed";
      textarea.style.opacity = "0";
      document.body.appendChild(textarea);
      textarea.select();
      textarea.setSelectionRange(0, textarea.value.length);

      try {
        if (!document.execCommand("copy")) throw new Error("复制命令不可用");
        resolve();
      } catch (error) {
        reject(error);
      } finally {
        document.body.removeChild(textarea);
      }
    });
  }

  function setCopyStatus(button, status, message, isError) {
    button.textContent = message;
    button.title = message;
    button.setAttribute("aria-label", message);
    button.classList.toggle("copy-failed", Boolean(isError));
    status.textContent = message;

    window.setTimeout(function () {
      button.textContent = "复制";
      button.title = "复制代码";
      button.setAttribute("aria-label", "复制代码");
      button.classList.remove("copy-failed");
      status.textContent = "";
    }, isError ? 1800 : 2200);
  }

  function addCopyButton(pre) {
    if (pre.querySelector(".code-copy-btn")) return;

    var button = document.createElement("button");
    var status = document.createElement("span");
    button.type = "button";
    button.className = "code-copy-btn";
    button.textContent = "复制";
    button.title = "复制代码";
    button.setAttribute("aria-label", "复制代码");
    status.className = "code-copy-status";
    status.setAttribute("aria-live", "polite");
    status.setAttribute("aria-atomic", "true");
    pre.style.position = "relative";
    pre.appendChild(button);
    pre.appendChild(status);

    button.addEventListener("click", function () {
      copyWithFallback(getCodeText(pre, button, status)).then(function () {
        setCopyStatus(button, status, "已复制", false);
      }).catch(function () {
        setCopyStatus(button, status, "复制失败", true);
      });
    });
  }

  function addCalloutClass(blockquote) {
    var calloutClasses = [
      "warning-callout", "bug-callout", "insight-callout", "success-callout", "note-callout"
    ];
    if (calloutClasses.some(function (className) { return blockquote.classList.contains(className); })) {
      return;
    }

    var firstParagraph = blockquote.querySelector("p");
    var text = (firstParagraph ? firstParagraph.textContent : blockquote.textContent).trim();
    var calloutClass = "";

    if (/🐛|\b(?:common\s+)?bug\b|错误|报错|踩坑/i.test(text)) {
      calloutClass = "bug-callout";
    } else if (/✅|💚|\bsuccess\b|成功|通关|完成/i.test(text)) {
      calloutClass = "success-callout";
    } else if (/📝|\bnote\b|注(?:意|释|记)?[：:]|补充/i.test(text)) {
      calloutClass = "note-callout";
    } else if (/⚠|\bwarning\b|警告|当心|提醒/i.test(text)) {
      calloutClass = "warning-callout";
    } else if (/💡|🧠|\b(?:key\s+)?insight\b|\bpro\s+tip\b|要点|洞见|记住这一句/i.test(text)) {
      calloutClass = "insight-callout";
    }

    if (calloutClass) blockquote.classList.add(calloutClass);
  }

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("pre").forEach(function (pre) {
      var cls = pre.className || "";
      var code = pre.querySelector('code[class*="language-"]');
      var lang = "text";
      var languageMatch = cls.match(/language-([\w-]+)/i) || (code && code.className.match(/language-([\w-]+)/i));
      if (languageMatch) lang = languageMatch[1].toUpperCase();
      pre.setAttribute("data-lang", lang);
      addCopyButton(pre);
    });

    document.querySelectorAll("blockquote").forEach(addCalloutClass);
    addLongChapterNavigation();
  });

  function addLongChapterNavigation() {
    var main = document.querySelector("#content main");
    if (!main || main.querySelector(".chapter-reading-nav")) return;

    var title = main.querySelector(":scope > h1");
    var headings = Array.prototype.slice.call(main.querySelectorAll(":scope > h2"))
      .filter(function (heading) {
        return /^\d+\.\d+/.test((heading.textContent || "").trim());
      });

    // 短章节不加导航；长项目页只列编号小节，避免把练习、总结也塞进目录。
    if (!title || headings.length < 5) return;

    var nav = document.createElement("nav");
    var label = document.createElement("strong");
    var list = document.createElement("ol");
    nav.className = "chapter-reading-nav";
    nav.setAttribute("aria-label", "本章导航");
    label.textContent = "本章导航";
    nav.appendChild(label);

    headings.forEach(function (heading) {
      var link = document.createElement("a");
      var item = document.createElement("li");
      var headingLink = heading.querySelector("a.header");
      var target = heading.id || (headingLink && headingLink.getAttribute("href"));
      if (!target) return;
      link.href = target.charAt(0) === "#" ? target : "#" + target;
      link.textContent = (heading.textContent || "").trim();
      item.appendChild(link);
      list.appendChild(item);
    });

    if (!list.children.length) return;
    nav.appendChild(list);
    title.insertAdjacentElement("afterend", nav);

    var button = document.createElement("button");
    button.type = "button";
    button.className = "back-to-top";
    button.textContent = "↑ 顶部";
    button.title = "回到本章顶部";
    button.setAttribute("aria-label", "回到本章顶部");
    button.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
    document.body.appendChild(button);

    function updateBackToTopVisibility() {
      button.classList.toggle("is-visible", window.scrollY > 420);
    }
    window.addEventListener("scroll", updateBackToTopVisibility, { passive: true });
    updateBackToTopVisibility();
  }
})();
