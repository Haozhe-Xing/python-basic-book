# Python 入门：像计算机科学家一样思考

> 为零基础中学生 / 高中生打造的 Python 第一本书。双引擎：**计算思维 + 算法启蒙**，为算法竞赛（USACO Bronze → Silver）与 AI/ML 路线打底。

本仓库是这本书的 [mdBook](https://rust-lang.github.io/mdBook/) 源码工程。

## 目录结构

```
.
├── book.toml                # mdBook 配置
├── src/                       # 书稿正文（Markdown + 内嵌 SVG 图示）
│   ├── SUMMARY.md             # 目录（章节顺序的唯一来源）
│   ├── getting-started/       # 准备出发：环境安装、Hello Python
│   ├── foundations/           # 第一篇：变量、字符串、运算符、输入输出
│   ├── control-flow/          # 第二篇：if / while / for / 调试思维
│   ├── data-structures/       # 第三篇：list / tuple / set / dict / 嵌套数据
│   ├── functions/             # 第四篇：函数、作用域与递归、模块
│   ├── algorithms/            # 第五篇：Big-O、搜索、排序、递归分治、栈队列链表、贪心模拟
│   ├── projects/              # 第六篇：文字冒险、数据分析、算法擂台
│   ├── appendices/            # 附录：错误速查、Python 之禅、习题答案
│   └── GLOSSARY.md            # 术语表
├── styles/                    # 自定义 CSS（website / theme-lock）
├── scripts/                   # 前端增强脚本（主题锁定、图示放大、代码增强）
├── Python入门书-理想大纲.md    # 写作大纲与设计意图
└── book/                      # 构建产物（已 gitignore）
```

## 本地构建

```bash
# 安装 mdBook（任选其一）
cargo install mdbook
# 或 brew install mdbook

# 构建静态站点到 book/
mdbook build

# 本地预览（带热更新）
mdbook serve --open
```

## 写作约定

- 新增章节：先创建 `src/<篇目>/<章节>.md`，再在 `src/SUMMARY.md` 中登记，否则不会出现在书里。
- 图示优先使用手写 SVG，与章节同目录，便于随正文一起版本管理。
- 面向读者是零基础中学生：术语首次出现要解释，代码示例尽量可直接运行。

## 许可

私有仓库，版权保留。
