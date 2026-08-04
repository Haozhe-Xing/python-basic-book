<div style="display:flex; gap:12px; margin-bottom:24px; flex-wrap:wrap; align-items:center;">
  <span style="background:#f0f4ff; color:#4A6CF7; padding:4px 12px; border-radius:20px; font-size:0.85em; font-weight:600; border:1px solid rgba(74,108,247,0.2);">📖 第16章</span>
  <span style="background:#f0fdf4; color:#16a34a; padding:4px 12px; border-radius:20px; font-size:0.85em; border:1px solid rgba(22,163,74,0.2);">⏱️ ~30 min read</span>
  <span style="background:#fef9ec; color:#d97706; padding:4px 12px; border-radius:20px; font-size:0.85em; border:1px solid rgba(100,100,100,0.15);">🎯 Intermediate</span>
</div>

# Chapter 16: 模块与标准库 —— 不重复造轮子

> 📝 **Before You Continue:** 这一章是"函数篇"的收尾，也接上 [第0章 0.4 的包管理彩蛋](../getting-started/install.md)。你已会写函数（[第14章](functions-intro.md)）甚至递归（[第15章](scope-recursion.md)）。现在学怎么**组织函数成模块**，以及**直接借用别人写好的函数**。

想象你要造一辆车。你会从螺丝钉开始自己炼钢吗？当然不——你直接去买现成的轮胎、发动机、电路板，拼起来就行。写程序也一样：**Python 自带一大箱"现成零件"（标准库），网上还有成千上万个别人做好的"零件包"（第三方库）。** 这一章教你如何把这些零件"拼"进自己的程序——这就是 **`import`（导入）**。

<div class="story-scene">
<strong>🎬 开场小剧场：标准库装备箱打开</strong>
<p>算法游乐场要装一个圆形喷泉，小派准备自己写圆周率、自己算平方根、自己造随机数。工具仓库管理员 module 听完差点把扳手掉地上。</p>
<p>他打开一只大箱子：“别重复造轮子。<code>math</code>、<code>random</code>、<code>datetime</code> 都是现成装备。会 <code>import</code>，就等于会借用整个 Python 世界的工具。”</p>
</div>

<div class="quest-card">
<strong>🎯 本章任务卡</strong>
<ul>
<li>掌握三种常见 <code>import</code> 写法。</li>
<li>用 <code>math</code> 完成数学计算。</li>
<li>用 <code>random</code> 做随机抽奖。</li>
<li>认识标准库和第三方库的区别。</li>
<li>学会把自己的代码组织成模块。</li>
</ul>
</div>

<div class="boss-bug">
<strong>👾 本章 Boss Bug：星号导入污染怪</strong>
<p>它会把一大堆名字倒进你的代码里，让变量名互相撞车。打败它的习惯是：少用 <code>from xxx import *</code>，优先写清楚模块名前缀。</p>
</div>

---

## 16.1 三种导入方式

<div class="try-it">
<strong>🧩 练一练 16.1</strong>
<p>题目：写出导入 math 模块的三种方式。</p>
<details><summary>💡 看看答案</summary>
<p>答案：① <code>import math</code>；② <code>from math import sqrt</code>；③ <code>import math as m</code>（起别名）。</p>
</details>
</div>

`import` 的本质是"把别人写好的代码请进你的文件里用"。常用三种写法：

```python
import math                      # ① 整块导入：用 math.xxx 调用
print(math.sqrt(16))             # 4.0

from math import sqrt, pi        # ② 挑着导入：直接用 sqrt / pi，不用加前缀
print(sqrt(9))                   # 3.0
print(pi)                        # 3.141592653589793

import math as m                 # ③ 起别名：嫌名字长就缩写
print(m.sqrt(25))                # 5.0
```

| 写法 | 调用时 | 适合场景 |
|------|--------|---------|
| `import math` | 必须写 `math.` 前缀 | 用到很多 math 功能，前缀能避免名字冲突 |
| `from math import sqrt` | 直接写 `sqrt` | 只用其中一两个，图省事 |
| `import math as m` | 写 `m.` 前缀 | 模块名长（如 `matplotlib`），缩写更清爽 |

> ⚠️ **Warning:** `from math import *`（星号导入所有）虽然能"不写前缀直接用一切"，但会**把一堆名字倒进你的命名空间**，极易和你自己的变量撞名、还难排查。**初学者尽量避免 `import *`**，用前三种更安全。

---

## 16.2 标准库之 math：数学好帮手

<div class="try-it">
<strong>🧩 练一练 16.2</strong>
<p>题目：用 math 模块求 16 的平方根。</p>
<details><summary>💡 看看答案</summary>
<p>答案：<code>import math</code> 后 <code>math.sqrt(16)</code> 得到 <code>4.0</code>。</p>
</details>
</div>

`math` 是 Python 自带的"科学计算器"，常用成员：

```python
import math

print(math.pi)           # 圆周率 3.141592653589793
print(math.sqrt(2))      # 开方 ≈ 1.4142135623730951
print(math.pow(2, 10))   # 2 的 10 次方 = 1024.0
print(math.floor(3.7))   # 向下取整 3
print(math.ceil(3.2))    # 向上取整 4
```

**案例：算圆形花坛的面积**

```python
import math

def circle_area(radius):
    """返回半径为 radius 的圆面积。"""
    return math.pi * radius ** 2

r = 5
print("半径", r, "的圆面积 ≈", round(circle_area(r), 2))   # 半径 5 的圆面积 ≈ 78.54
```

> 💡 **Key Insight:** 注意 `round(值, 2)` 把结果四舍五入到两位小数——打印给用户看时，"≈ 78.54" 比一长串小数友好得多。这是让输出"体面"的小技巧。

---

## 16.3 标准库之 random：制造"随机"

<div class="try-it">
<strong>🧩 练一练 16.3</strong>
<p>题目：用 random 模块模拟掷一个六面骰子。</p>
<details><summary>💡 看看答案</summary>
<p>答案：<code>import random</code> 后 <code>random.randint(1, 6)</code> 随机返回 1~6。</p>
</details>
</div>

抽奖、随机出题、游戏里掉装备——全靠 `random`。最常用三个：

```python
import random

print(random.randint(1, 6))        # ① 闭区间随机整数 [1, 6]，像掷骰子
print(random.choice(["红", "黄", "蓝"]))   # ② 从列表里随机抽一个
print(round(random.random(), 2))   # ③ [0,1) 随机小数，保留两位
```

**案例：游乐场抽奖机**

```python
import random

def draw_prize():
    """随机抽取一份奖品。"""
    prizes = ["棉花糖", "发光头箍", "不限次通行证", "谢谢参与"]
    return random.choice(prizes)

print("恭喜抽中：", draw_prize())
```

> 🤔 **Why 叫"伪随机"？** 计算机本质是确定的，它用的是"伪随机数生成器"——从一个种子算出看似随机的序列。对游戏、抽奖完全够用；但真要"密码级安全随机"，得用 `secrets` 库。中学生阶段，`random` 够玩遍所有玩具项目。

---

## 16.4 标准库之 datetime 与 os：时间与文件

<div class="try-it">
<strong>🧩 练一练 16.4</strong>
<p>题目：用 datetime 打印今天的日期。</p>
<details><summary>💡 看看答案</summary>
<p>答案：<code>from datetime import date</code> 后 <code>print(date.today())</code>。</p>
</details>
</div>

这两个库帮你"感知世界"——一个管时间，一个管文件系统。

**datetime：记下开园、闭园时刻**

```python
import datetime

now = datetime.datetime.now()
print(now)                                  # 2026-07-17 14:30:05.123456
print(now.strftime("%Y-%m-%d %H:%M"))       # 2026-07-17 14:30（自定义格式）
```

**os：看看当前目录里有什么**

```python
import os

print(os.getcwd())          # 当前工作目录（你程序"站在"哪个文件夹）
print(os.listdir("."))      # 当前目录下的文件/文件夹列表
```

> 📝 **Note:** `os` 还能做"读写文件""建文件夹""拼路径"等——等你做第 13 章的排行榜存档、或第六篇项目时，`os` 会派上大用场。本章先认个脸，知道"有这个零件"即可。

---

## 16.5 pip：装上更多"第三方零件"

<div class="try-it">
<strong>🧩 练一练 16.5</strong>
<p>题目：pip 是干什么用的？</p>
<details><summary>💡 看看答案</summary>
<p>答案：pip 用来<b>安装第三方包</b>（别人写好的工具），比如 <code>pip install 包名</code>，站在别人肩膀上。</p>
</details>
</div>

标准库是 Python 自带的；但网上还有海量**第三方库**（别人写好后上传到 PyPI 仓库）。用 `pip` 一条命令就能装：

```bash
pip install requests        # Windows
pip3 install requests       # macOS 可能要用 pip3
```

装完就能 `import` 使用：

```python
import requests
r = requests.get("https://api.example.com/hello")
print(r.status_code)        # 200 表示请求成功
```

> 🔗 **接第0章 0.4：** 第 0 章说过，第三方库就像"别人写好的积木"——`turtle` 是自带的，但做网站的 `django`、做数据的 `pandas` 需要 `pip` 装。今天你正式见到了 `import` 怎么用这些积木；将来想玩更硬核的包管理，可搜 "astral uv"（第 0 章提过的现代工具）。

> ⚠️ **Warning:** `pip install` 装的是**全网任何人**上传的包。初学阶段只装"有名、常用"的库（如 `requests`、`pandas`、`matplotlib`），别乱装来路不明的包，避免安全风险。

### 🔍 计算思维聚焦：复用（Reuse）

> **站在别人肩膀上——能借现成的，就不自己重造。** 这是工程世界最重要的思维之一。你花一小时 `import` 一个库，可能省下别人几个月写的代码。复用不是"偷懒"，而是把精力留给真正属于你的问题。

想想看：没有复用，每个程序员都得重写排序、重写随机数、重写网络请求——人类早就累瘫了。**会找轮子、会用轮子，比会造轮子有时更关键。** 当然，第 17 章起你也会亲手"造"一些基础轮子（排序、搜索），那是为了懂原理；懂了之后，实战里照样优先用现成的。

![模块拼图：站在别人肩膀上](../images/f4-module-puzzle.svg)

上图把 `random`、`math`、`datetime`、`os` 画成四块拼图，一片片 `import` 进你的主程序——不用自己从零写随机数算法、不用自己实现圆周率，直接拼上就用。

> 🧮 **算法小课堂（前置彩蛋）：** 标准库里藏着算法的影子——`random.choice` 背后的随机抽取、`sorted()` 背后的排序算法（第 19 章会亲手实现）。理解"库函数怎么干活"，你才不会把它们当黑魔法；第 17 章起，我们就一层层掀开这些算法的盖子。

---

## 16.6 🛠️ 项目工坊：算法游乐场"随机事件"

游乐场想每天整点"惊喜"：闭园前随机抽取一位**幸运游客**，再随机送个奖品。用 `random` 两行就搞定——这就是复用的威力。

下面是一段**自包含**代码（纯终端、只用标准库）：

```python
import random
import datetime

def lucky_draw(guests):
    """从游客名单里随机抽一位幸运游客，并随机送一份奖品。"""
    if not guests:                       # 防空列表，避免抽空出错
        return "今天还没有游客～"
    lucky = random.choice(guests)        # 随机抽游客
    prizes = ["棉花糖", "发光头箍", "不限次通行证"]
    prize = random.choice(prizes)        # 随机抽奖品
    now = datetime.datetime.now().strftime("%H:%M")
    return "[" + now + "] 🎉 幸运游客 " + lucky + " 获得：" + prize


# 模拟今日游客名单（也可来自第 10-13 章的列表/字典）
today_guests = ["小明", "小红", "阿强", "老王", "小美"]
print(lucky_draw(today_guests))
print(lucky_draw(today_guests))
```

每次运行结果都不同——因为 `random.choice` 真随机。**现在游乐场多了"随机事件引擎"：`lucky_draw(guests)` 一个函数，借 `random` + `datetime` 两块现成拼图，就实现了"抽幸运游客 + 送随机奖品 + 打时间戳"。** 你没写一行随机数算法，却拥有了抽奖机。

> ⚡ **Pro Tip:** 真实项目里 `today_guests` 会来自第 10-13 章用列表/字典管理的游客数据。模块的价值正在于此：你前面攒的"数据零件"和这里攒的"功能零件"，可以无缝拼装。

---

## 16.7 ⚔️ 挑战擂台

**擂台 1 — 掷骰子统计：** 用 `random.randint(1,6)` 模拟掷 10 次骰子，统计每个点数出现了几次（提示：用第 12 章的字典存计数）。

**擂台 2 — 自定义格式时间戳：** 用 `datetime` 输出"今天是 2026年07月17日 周五"这样的中文字符串（查 `strftime` 的 `%Y %m %d %A` 等格式符，注意中文星期可能需要额外处理）。

---

## 🏅 本章通关徽章：工具仓库管理员

<div class="badge-card">
<strong>如果你能做到下面 4 件事，就获得“工具仓库管理员”徽章：</strong>
<ul>
<li>能写出三种常见 <code>import</code> 方式。</li>
<li>能用 <code>math</code>、<code>random</code> 等标准库解决小问题。</li>
<li>能解释为什么不推荐 <code>import *</code>。</li>
<li>能把自己的函数拆成模块复用。</li>
</ul>
</div>

---

## ⚠️ Common Mistakes in Chapter 16

| # | 误区 | 示例 | 为什么错 | 修正 |
|---|------|------|---------|------|
| 1 | 没 import 就用 | `print(pi)` | `pi` 不在当前命名空间 | 先 `import math` 或 `from math import pi` |
| 2 | `from x import *` 污染命名 | `from math import *` 后变量冲突 | 倒进一堆名字，难排查 | 用 `import math` 或精准 `from math import sqrt` |
| 3 | 以为 random 真随机 | 用于密码/抽奖公正性 | 是伪随机，可预测 | 密码场景用 `secrets` 库 |
| 4 | macOS 用 `pip` 装不上 | `pip install xxx` 报错 | Mac 常要 `pip3` | 换成 `pip3 install xxx` |
| 5 | 别名写错调用 | `import math as m` 后写 `math.sqrt` | 起了别名后原名失效 | 统一用别名 `m.sqrt` |
| 6 | 抽空列表 | `random.choice([])` | 空列表没东西可抽，报错 | 调用前判断列表非空 |

---

## Chapter Summary

### 📌 Key Takeaways

| 概念 | 要点 | 为什么重要 |
|------|------|------------|
| `import` | 把现成代码请进来用 | 不重复造轮子 |
| 三种导入 | `import` / `from..import` / `as` 别名 | 按场景选，避免命名冲突 |
| `math` | `pi` / `sqrt` / `pow` / `floor` | 数学计算现成可用 |
| `random` | `randint` / `choice` / `random` | 抽奖、随机、游戏核心 |
| `datetime` / `os` | 时间格式化 / 文件系统 | 感知世界的两块基础拼图 |
| `pip` | 装第三方库（Mac 用 `pip3`） | 扩展能力，接第0章 0.4 |

### ❓ FAQ

**Q1: `import math` 和 `from math import sqrt` 哪个好？**
> A: 没有绝对好坏。用到很多 math 功能、且想避免名字冲突时，用 `import math`（调用写 `math.sqrt`）；只偶尔用一两个、想少打字，用 `from math import sqrt`。关键是保持一个文件里的风格一致、可读。

**Q2: 标准库和第三方库有什么区别？**
> A: 标准库（如 `math`、`random`、`datetime`、`os`）随 Python 一起安装，开箱即用；第三方库（如 `requests`、`pandas`）需要 `pip install` 额外装。前者管"基础通用"，后者管"专业领域"。两者都通过 `import` 使用，对你是一样的"积木"。

**Q3: `pip` 装包时报权限错误或找不到命令怎么办？**
> A: Windows 一般是 PATH/权限问题，可试 `python -m pip install 包名`；macOS 多半是命令写成 `pip` 而系统要 `pip3`，换成 `pip3 install 包名`。本书第 0 章的排查思路同样适用。

### 🔗 Connections to Later Chapters

- **[第17章 · 大 O 记法](../algorithms/big-o.md)** 起，算法篇正式开始——你会亲手实现排序、搜索，理解"库函数背后的原理"。
- **第六篇 · 综合项目**（[文本冒险](../projects/text-adventure.md)、[数据分析](../projects/data-analysis.md)、[算法擂台](../projects/algorithm-arena.md)）会大量 `import` 标准库与第三方库，把今天学的"拼图"拼成完整作品。
- **[下一步去哪](../projects/next-steps.md)** 会指向 USACO 竞赛、AI/ML 路线——那条路上 `numpy`、`pandas`、`requests` 等第三方库是日常。

---


## 🎮 加练任务包

> 下面这些题目不一定比章末题更难，但更适合“多刷几遍、把手感练出来”。建议先独立做，再展开提示。

### 加练 16.A · 随机抽奖 🟢

用 `random` 从名单里随机抽出一名幸运游客。

<details>
<summary>💡 提示 / 答案要点</summary>

`import random`，然后 `random.choice(names)`。模块像现成工具箱。

</details>

---

### 加练 16.B · 圆形面积 🟢

用 `math.pi` 计算半径为 3 的圆面积。

<details>
<summary>💡 提示 / 答案要点</summary>

`import math`，面积 `math.pi * 3 ** 2`。保留小数可用 f-string 格式符。

</details>

---

### 加练 16.C · 导入方式选择 🟡

为什么 `import math` 比 `from math import *` 更适合初学者？

<details>
<summary>💡 提示 / 答案要点</summary>

`math.sqrt` 前缀清楚，不容易名字冲突；星号导入会倒入太多名字，出错难查。

</details>

---


---

## Practice Problems

---

**Problem 16.1 — 用 math 算球体积** 🟢 Easy

球体积公式 `V = 4/3 · π · r³`。写代码用 `math.pi` 计算半径 `r = 7` 的球体积，四舍五入到两位小数打印。

**Sample Output:** `约 1436.76`

<details>
<summary>💡 Solution (click to reveal)</summary>

**Approach:** `import math` 后直接用 `math.pi`，幂运算用 `** 3`，最后 `round(..., 2)` 收两位小数。

```python
import math

r = 7
volume = 4 / 3 * math.pi * r ** 3
print("约", round(volume, 2))
```

**Key points:**
- `4 / 3` 在 Python 3 里是浮点除法，结果正确；若写成 `4 // 3` 会变整数 `1`，是常见坑。
- `round(值, 2)` 让输出清爽。

</details>

---

**Problem 16.2 — 用 random 模拟掷骰子** 🟡 Medium

写一个函数 `roll_dice()`，用 `random.randint(1, 6)` 返回一次掷骰子的点数。连续调用 5 次并打印。

**Sample Output:**（每次不同，示例）
```
3
6
1
5
2
```

<details>
<summary>💡 Solution (click to reveal)</summary>

**Approach:** `randint(1, 6)` 给出闭区间 `[1, 6]` 的随机整数；循环调用 5 次即可。

```python
import random

def roll_dice():
    return random.randint(1, 6)

for _ in range(5):
    print(roll_dice())
```

**Key points:**
- `for _ in range(5)` 里 `_` 表示"我不用这个循环变量"，是 Python 习惯写法。
- 每次运行结果不同，这正是随机性的体现。

</details>

---

**Problem 16.3 — from 导入与别名** 🟡 Medium

用 `from math import sqrt as s` 把 `sqrt` 别名为 `s`，再计算 `s(144)`、`s(225)` 并打印。体会"挑着导入 + 缩写"的组合用法。

**Sample Output:**
```
12.0
15.0
```

<details>
<summary>💡 Solution (click to reveal)</summary>

**Approach:** `from math import sqrt as s` 既"挑着导入"又"起别名"，之后直接用 `s(...)`。

```python
from math import sqrt as s

print(s(144))     # 12.0
print(s(225))     # 15.0
```

**Key points:**
- 别名 `as s` 之后，原名 `sqrt` 在本文件不可用了，统一用 `s`。
- 这种写法适合"只用一个函数"又"想少打字"的场景。

</details>

---

**Problem 16.4 — 🏆 Challenge：闭园幸运抽奖** 🏆 Challenge

写一个函数 `closing_lottery(guests, prizes)`，从 `guests` 随机抽一位幸运游客、从 `prizes` 随机抽一份奖品，返回形如 `"🎉 幸运游客 小明 获得 发光头箍"` 的字符串。要求：若 `guests` 为空，返回 `"今日无游客"`；用 `random.choice` 实现。用 `closing_lottery(["小明","小红","阿强"], ["棉花糖","不限次通行证"])` 测试。

**Sample Output:**（随机，示例）
```
🎉 幸运游客 小红 获得 不限次通行证
```

<details>
<summary>💡 Solution (click to reveal)</summary>

**Approach:** 先判空防错，再用两次 `random.choice` 分别抽游客和奖品，拼成字符串返回。

```python
import random

def closing_lottery(guests, prizes):
    if not guests:                 # 防空列表
        return "今日无游客"
    lucky = random.choice(guests)
    prize = random.choice(prizes)
    return "🎉 幸运游客 " + lucky + " 获得 " + prize


print(closing_lottery(["小明", "小红", "阿强"],
                      ["棉花糖", "不限次通行证"]))
```

**Key points:**
- `if not guests:` 是判断"列表为空"的惯用写法，避免 `random.choice([])` 报错。
- 函数返回字符串而非直接 `print`，调用处可自由决定怎么展示——这正是第 14 章封装思想的延续。
- 此函数与第 16.6 节项目工坊的 `lucky_draw` 思路一致，是把"随机事件"封装复用的完整范例。

</details>

---

> 💡 **记住这一句：** 模块就是"借来的轮子"——**`import` 一下，站上别人肩膀，把精力留给真正属于你的难题。**
