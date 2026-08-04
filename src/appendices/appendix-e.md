<div style="display:flex; gap:12px; margin-bottom:24px; flex-wrap:wrap; align-items:center;">
  <span style="background:#f0f4ff; color:#4A6CF7; padding:4px 12px; border-radius:20px; font-size:0.85em; font-weight:600; border:1px solid rgba(74,108,247,0.2);">📖 附录 E</span>
  <span style="background:#f0fdf4; color:#16a34a; padding:4px 12px; border-radius:20px; font-size:0.85em; border:1px solid rgba(22,163,74,0.2);">⏱️ ~18 min read</span>
  <span style="background:#fef9ec; color:#d97706; padding:4px 12px; border-radius:20px; font-size:0.85em; border:1px solid rgba(100,100,100,0.15);">🎯 Intermediate</span>
</div>

# 附录 E：习题参考答案与提示

> 各章末尾的 **Practice Problems** 里，答案都藏在 `<details>` 折叠块中——**先自己憋一憋，真卡住了再点开**。本附录不重抄全部代码，而是把每题的"关键思路"汇成一张索引，方便你快速回看"我当时卡在哪"。

---

## 若卡住，先看这条导引

> 📝 **Note:** 做题的正确姿势是"先想后看"：
> 1. 自己写一版，哪怕跑不通也没关系；
> 2. 看本附录对应那题的"关键思路提示"，只瞄思路、不瞄代码；
> 3. 还不行，再回去点开原章 `<details>` 看完整答案。

> 💡 **Key Insight:** 能独立写出"丑但能跑"的代码，远比抄"漂亮答案"学得牢。提示是拐杖，不是轮椅——尽早扔掉它。

---

## 第〇章 安装开发环境

| 题号 | 主题 | 关键思路提示 | 章节回链 |
|------|------|--------------|----------|
| 0.1 | 查看 Python 版本 | Windows 用 `python --version`，macOS 用 `python3 --version`；看到 `Python 3.x.y` 即成功，报错回去重做 PATH 勾选 | [install.md §0.3](../getting-started/install.md) |
| 0.2 | 打印一句问候 | `print("...")` 让电脑说话；注意文件后缀 `.py`、引号用英文 | [install.md §0.2](../getting-started/install.md) |
| 0.3 | 装第三方库 emoji | `pip install emoji`（Mac 可能 `pip3`）；装一次后 `import` 反复用 | [install.md §0.4](../getting-started/install.md) |

---

## 第一章 你好，Python！

| 题号 | 主题 | 关键思路提示 | 章节回链 |
|------|------|--------------|----------|
| 1.1 | 让电脑自我介绍 | 三行独立 `print`；第三行用逗号把文字和 `1+1` 隔开，Python 先算再拼 | [hello-python.md §1.1](../getting-started/hello-python.md) |
| 1.2 | 海龟画更大的正方形 | 只改 `forward(150)`，转角 `right(90)` 不变（正方形永远转直角） | [hello-python.md §1.2](../getting-started/hello-python.md) |
| 1.3 | 猜图形（正多边形） | 规律：正 n 边形每次转角 = `360 / n`；`360/5 = 72` → 正五边形 | [hello-python.md §1.3](../getting-started/hello-python.md) |

> 📝 **Note:** 以上第〇、一章的条目**取自已完稿的原章**。下面第二~二十六章的练习为**按全书大纲预设**的"预期方向 + 通用思路提示"，待各章 Practice Problems 定稿后，主编可把真实题号与提示补进本表（结构保持一致即可）。

---

## 第二章 变量与数据类型（预设）

| 题号 | 主题 | 关键思路提示 | 章节回链 |
|------|------|--------------|----------|
| 2.1 | 交换两个数 | 用临时变量或 `a, b = b, a` 并行赋值 | [variables.md](../foundations/variables.md) |
| 2.2 | 单位换算 | 读入数字先 `int/float`，再乘换算系数 | [variables.md](../foundations/variables.md) |
| 2.3 | 类型互转 | `str()` 输出、`int()` 输入；小数先 `float` 再 `int` | [variables.md](../foundations/variables.md) |

## 第三章 字符串与文本处理（预设）

| 题号 | 主题 | 关键思路提示 | 章节回链 |
|------|------|--------------|----------|
| 3.1 | 反转字符串 | 切片 `s[::-1]` 一步到位 | [strings.md](../foundations/strings.md) |
| 3.2 | 统计某字符出现次数 | `s.count(ch)` 或遍历累加 | [strings.md](../foundations/strings.md) |
| 3.3 | 提取用户名 | 用 `split()` 或切片取子串 | [strings.md](../foundations/strings.md) |

## 第四章 运算符与表达式（预设）

| 题号 | 主题 | 关键思路提示 | 章节回链 |
|------|------|--------------|----------|
| 4.1 | 判断闰年 | 能被 4 整除且不被 100 整除，或能被 400 整除 | [operators.md](../foundations/operators.md) |
| 4.2 | 奇偶与范围 | 用 `% 2` 判奇偶；区间用 `a <= x <= b` | [operators.md](../foundations/operators.md) |

## 第五章 输入与输出（预设）

| 题号 | 主题 | 关键思路提示 | 章节回链 |
|------|------|--------------|----------|
| 5.1 | 读入多个数 | `input().split()` 再逐个 `int()` | [input-output.md](../foundations/input-output.md) |
| 5.2 | 格式化成绩单 | 用 f-string 对齐姓名与分数 | [input-output.md](../foundations/input-output.md) |

## 第六章 条件判断（预设）

| 题号 | 主题 | 关键思路提示 | 章节回链 |
|------|------|--------------|----------|
| 6.1 | 成绩分档 | 用 `if / elif / else` 互斥分支，从高分往低判 | [conditionals.md](../control-flow/conditionals.md) |
| 6.2 | 三角形判定 | 三边满足"两短边之和大于最长边" | [conditionals.md](../control-flow/conditionals.md) |

## 第七章 while 循环（预设）

| 题号 | 主题 | 关键思路提示 | 章节回链 |
|------|------|--------------|----------|
| 7.1 | 猜数字游戏 | `while` 里比对，猜中才 `break`；记得更新状态 | [while-loops.md](../control-flow/while-loops.md) |
| 7.2 | 累加 1 到 n | 累加器 `total=0`，循环内 `total += i` | [while-loops.md](../control-flow/while-loops.md) |

## 第八章 for 与 range（预设）

| 题号 | 主题 | 关键思路提示 | 章节回链 |
|------|------|--------------|----------|
| 8.1 | 打印乘法表 | 两层 `for` 嵌套，i 行 j 列 | [for-loops.md](../control-flow/for-loops.md) |
| 8.2 | 求列表最大值 | 先设 `mx = lst[0]`，遍历逐个比较更新 | [for-loops.md](../control-flow/for-loops.md) |

## 第九章 调试与调试思维（预设）

| 题号 | 主题 | 关键思路提示 | 章节回链 |
|------|------|--------------|----------|
| 9.1 | 读一段报错定位 | 滚到最后一行看类型与行号 | [debugging.md](../control-flow/debugging.md) |
| 9.2 | 用打印调试 | 在循环里打印中间变量，观察哪步偏离 | [debugging.md](../control-flow/debugging.md) |

## 第十章 列表 list（预设）

| 题号 | 主题 | 关键思路提示 | 章节回链 |
|------|------|--------------|----------|
| 10.1 | 去重保序 | 遍历原表，新表里没有才加 | [lists.md](../data-structures/lists.md) |
| 10.2 | 列表反转 | `lst[::-1]` 或双指针 | [lists.md](../data-structures/lists.md) |

## 第十一章 元组与集合（预设）

| 题号 | 主题 | 关键思路提示 | 章节回链 |
|------|------|--------------|----------|
| 11.1 | 统计独立元素 | 用 `set` 去重后看 `len` | [tuples-sets.md](../data-structures/tuples-sets.md) |
| 11.2 | 两集合交集 | `set_a & set_b` | [tuples-sets.md](../data-structures/tuples-sets.md) |

## 第十二章 字典 dict（预设）

| 题号 | 主题 | 关键思路提示 | 章节回链 |
|------|------|--------------|----------|
| 12.1 | 词频统计 | 遍历，键不存在就初始化为 0 再 +1（用 `get`） | [dictionaries.md](../data-structures/dictionaries.md) |
| 12.2 | 找最高分的人 | 边遍历 `items()` 边记录最大值的键 | [dictionaries.md](../data-structures/dictionaries.md) |

## 第十三章 嵌套与结构化数据（预设）

| 题号 | 主题 | 关键思路提示 | 章节回链 |
|------|------|--------------|----------|
| 13.1 | 二维表求和 | 两层循环，注意"先行后列" `matrix[i][j]` | [nested-data.md](../data-structures/nested-data.md) |
| 13.2 | 学生成绩查询 | 嵌套字典按层 `.get` 取值，缺键给默认 | [nested-data.md](../data-structures/nested-data.md) |

## 第十四章 函数入门（预设）

| 题号 | 主题 | 关键思路提示 | 章节回链 |
|------|------|--------------|----------|
| 14.1 | 写 `is_prime(n)` | 明确参数与 `return`；先处理小值再试除到 √n | [functions-intro.md](../functions/functions-intro.md) |
| 14.2 | 写 `max_of_three` | 封装比较逻辑，返回结果而非打印 | [functions-intro.md](../functions/functions-intro.md) |

## 第十五章 作用域与递归初步（预设）

| 题号 | 主题 | 关键思路提示 | 章节回链 |
|------|------|--------------|----------|
| 15.1 | 阶乘递归 | 基线 `n==0` 返回 1；递归 `n * f(n-1)` | [scope-recursion.md](../functions/scope-recursion.md) |
| 15.2 | 斐波那契 | 基线 `n<=1`；注意朴素递归会重复计算 | [scope-recursion.md](../functions/scope-recursion.md) |

## 第十六章 模块与标准库（预设）

| 题号 | 主题 | 关键思路提示 | 章节回链 |
|------|------|--------------|----------|
| 16.1 | 用 `random` 抽奖 | `import random` 后 `random.choice` | [modules.md](../functions/modules.md) |
| 16.2 | 自写工具模块 | 把函数放 `utils.py`，主文件 `from utils import ...` | [modules.md](../functions/modules.md) |

## 第十七章 算法与效率入门（预设）

| 题号 | 主题 | 关键思路提示 | 章节回链 |
|------|------|--------------|----------|
| 17.1 | 数一数操作次数 | 随 n 增大，时间怎么变 → O(n)? O(n²)? | [big-o.md](../algorithms/big-o.md) |
| 17.2 | 对比两种实现 | 同结果不同复杂度，体会"快"的来源 | [big-o.md](../algorithms/big-o.md) |

## 第十八章 搜索算法（预设）

| 题号 | 主题 | 关键思路提示 | 章节回链 |
|------|------|--------------|----------|
| 18.1 | 线性查找 | 从头扫到尾，找到返回下标，否则 -1 | [searching.md](../algorithms/searching.md) |
| 18.2 | 二分查找 | 前提有序；维护 `lo/hi`，`mid` 比对后收缩区间 | [searching.md](../algorithms/searching.md) |

## 第十九章 排序算法（预设）

| 题号 | 主题 | 关键思路提示 | 章节回链 |
|------|------|--------------|----------|
| 19.1 | 冒泡排序 | 相邻比大往右"冒"，外层 n-1、内层 n-1-i | [sorting.md](../algorithms/sorting.md) |
| 19.2 | 选择排序 | 每轮选最小放到前面，已排部分不再动 | [sorting.md](../algorithms/sorting.md) |

## 第二十章 递归与分治（预设）

| 题号 | 主题 | 关键思路提示 | 章节回链 |
|------|------|--------------|----------|
| 20.1 | 归并排序 | 先分两半递归排，再合并两个有序段 | [recursion-divide.md](../algorithms/recursion-divide.md) |
| 20.2 | 二分查找递归版 | 基线：区间为空返回 -1；否则取 mid 分左右 | [recursion-divide.md](../algorithms/recursion-divide.md) |

## 第二十一章 基础数据结构（预设）

| 题号 | 主题 | 关键思路提示 | 章节回链 |
|------|------|--------------|----------|
| 21.1 | 用栈做括号匹配 | 遇 `(` 压栈，遇 `)` 弹栈比对 | [basic-structures.md](../algorithms/basic-structures.md) |
| 21.2 | 用队列做排队模拟 | `deque` 的 `append/popleft` 实现先进先出 | [basic-structures.md](../algorithms/basic-structures.md) |

## 第二十二章 贪心与模拟（预设）

| 题号 | 主题 | 关键思路提示 | 章节回链 |
|------|------|--------------|----------|
| 22.1 | 活动选择贪心 | 按结束时间排序，能选就选不冲突的 | [greedy-simulation.md](../algorithms/greedy-simulation.md) |
| 22.2 | 小游戏模拟 | 把规则逐条翻译成状态更新，注意顺序与边界 | [greedy-simulation.md](../algorithms/greedy-simulation.md) |

## 第二十三章 项目一：互动文字冒险（预设）

| 题号 | 主题 | 关键思路提示 | 章节回链 |
|------|------|--------------|----------|
| 23.1 | 状态机设计 | 用字典存 `state`，根据输入转移分支 | [text-adventure.md](../projects/text-adventure.md) |
| 23.2 | 输入容错 | 先 `strip().lower()` 再匹配命令 | [text-adventure.md](../projects/text-adventure.md) |

## 第二十四章 项目二：数据小分析（预设）

| 题号 | 主题 | 关键思路提示 | 章节回链 |
|------|------|--------------|----------|
| 24.1 | 读 CSV 算平均 | 跳过表头，数值先转换再累加求平均 | [data-analysis.md](../projects/data-analysis.md) |
| 24.2 | 画简单图表 | 用列表存数据点，挑合适的可视化方式 | [data-analysis.md](../projects/data-analysis.md) |

## 第二十五章 项目三：算法挑战擂台（预设）

| 题号 | 主题 | 关键思路提示 | 章节回链 |
|------|------|--------------|----------|
| 25.1 | 暴力 vs 优化 | 先写能跑的暴力解，再想怎么降复杂度 | [algorithm-arena.md](../projects/algorithm-arena.md) |
| 25.2 | 读题建模 | 把文字题抽象成"数组/查找/排序"哪一类 | [algorithm-arena.md](../projects/algorithm-arena.md) |

## 第二十六章 下一步去哪（预设）

| 题号 | 主题 | 关键思路提示 | 章节回链 |
|------|------|--------------|----------|
| 26.1 | 制定练习计划 | 每天动手写，选定一条路线（竞赛/AI/Web） | [next-steps.md](../projects/next-steps.md) |
| 26.2 | 注册一个 OJ | 在 USACO / 洛谷等平台做第一题 Bronze | [next-steps.md](../projects/next-steps.md) |

---

> 💡 **Key Insight:** 提示只给你"方向"，不替你写代码——这才是练脑子的正确方式。等第二~二十六章定稿，本表就是一张完整的"全书习题导航图"，复习时按图索骥即可。

> 📝 **Note:** 第〇、一章的题号与提示与已完稿原章一致；第二~二十六章为预设索引，主编定稿各章 Practice Problems 后，把真实题号与思路按相同四列表格补入即可，无需改动结构。
