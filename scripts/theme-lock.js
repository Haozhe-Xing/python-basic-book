// theme-lock.js — 强制本书使用浅色主题
(function () {
  try {
    localStorage.setItem("mdbook-theme", "light");
    localStorage.setItem("mdbook-prefered-theme", "light");
  } catch (e) {}
  var root = document.documentElement;
  if (root) {
    root.classList.remove("theme-dark");
    root.setAttribute("data-theme", "light");
    root.style.colorScheme = "light";
  }
})();
