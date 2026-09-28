// theme-lock.js — 本书仅使用浅色主题
(function () {
  var root = document.documentElement;

  function applyLightTheme() {
    try {
      localStorage.setItem("mdbook-theme", "light");
      localStorage.setItem("mdbook-preferred-theme", "light");
    } catch (e) {}

    root.classList.remove("theme-dark", "theme-navy", "theme-coal", "theme-ayu");
    root.classList.add("theme-light");
    root.setAttribute("data-theme", "light");
    root.style.colorScheme = "light";
  }

  applyLightTheme();
  document.addEventListener("DOMContentLoaded", applyLightTheme);
})();
