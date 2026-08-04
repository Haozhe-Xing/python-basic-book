<div style="display:flex; gap:12px; margin-bottom:24px; flex-wrap:wrap; align-items:center;">
  <span style="background:#f0f4ff; color:#4A6CF7; padding:4px 12px; border-radius:20px; font-size:0.85em; font-weight:600; border:1px solid rgba(74,108,247,0.2);">📖 第14章</span>
  <span style="background:#f0fdf4; color:#16a34a; padding:4px 12px; border-radius:20px; font-size:0.85em; border:1px solid rgba(22,163,74,0.2);">⏱️ ~35 min read</span>
  <span style="background:#fef9ec; color:#d97706; padding:4px 12px; border-radius:20px; font-size:0.85em; border:1px solid rgba(100,100,100,0.15);">🎯 Intermediate</span>
</div>

# Chapter 14: 函数入门 —— 把重复代码打包成"按钮"

> 📝 **Before You Continue:** 这一章建立在你已经会写"直来直去"的代码之上：变量与字符串（[第2章 变量](../foundations/variables.md)、[第3章 字符串](../foundations/strings.md)）、`if` 判断（[第6章](../control-flow/conditionals.md)）、循环（[第7-8章](../control-flow/while-loops.md)）、以及用列表/字典管数据（[第10-13章](../data-structures/lists.md)）。特别是[第7章的积分系统](../control-flow/while-loops.md)和[第5章的门票问答机](../foundations/input-output.md)，本章会拿它们"开刀"重构成函数。

你有没有过这种经历：每天早上都要重复"磨豆 → 烧水 → 冲泡 → 洗杯子"这一串动作？如果厨房墙上有一个**一键咖啡按钮**，按一下就自动跑完所有步骤，生活会变得多轻松。

写代码也一样。前面十几章你写了不少**重复**的东西：第 7 章积分系统里，每次给游客加分都重写一遍"算分 + 打印"；第 5 章门票问答机里，每问一个问题都复制粘贴同样的提示语。**重复的代码就像没装按钮的咖啡机——每次都得手动把流程走一遍，又累又容易出错。**

这一章，你就来给代码装上"按钮"——也就是**函数（function）**。装好之后，一串复杂操作，以后只要喊一声名字就搞定。

<div class="story-scene">
<strong>🎬 开场小剧场：自动售货机厂长登场</strong>
<p>游乐场里的饮料摊每天都重复同一套动作：收钱、找零、吐饮料、打印小票。小派一开始每卖一瓶都手写一遍流程，写到第三瓶就眼花了。</p>
<p>自动售货机厂长 function 说：“把流程装进机器里吧。以后只要按 <code>make_drink("橙汁")</code>，机器自己跑完整套步骤。”函数，就是给代码装按钮。</p>
</div>

<div class="quest-card">
<strong>🎯 本章任务卡</strong>
<ul>
<li>用 <code>def</code> 定义自己的按钮。</li>
<li>用参数给按钮喂不同材料。</li>
<li>用 <code>return</code> 把结果吐出来。</li>
<li>写文档字符串，让未来的自己看懂。</li>
<li>把前面章节的重复代码重构成函数。</li>
</ul>
</div>

<div class="boss-bug">
<strong>👾 本章 Boss Bug：print 冒牌 return 怪</strong>
<p>它最会骗初学者：屏幕上明明显示了结果，你却没法把结果继续拿来计算。记住：<code>print</code> 是“给人看”，<code>return</code> 是“交给程序继续用”。</p>
</div>

---

## 14.1 你的第一个函数：问候函数

<div class="try-it">
<strong>🧩 练一练 14.1</strong>
<p>题目：写一个名为 greet 的函数，输入名字，打印“你好，XX”。</p>
<details><summary>💡 看看答案</summary>
<p>答案：<code>def greet(name): print(f"你好，{name}")</code>，调用 <code>greet("小龙")</code>。</p>
</details>
</div>

函数用 `def` 开头（`def` = define，定义）。看一个最小例子：

```python
def greet(name):              # ① def 定义，greet 是函数名，name 是参数
    message = "你好, " + name  # ② 函数体（必须缩进！）
    return message             # ③ return 把结果"吐"出来


# 调用（按按钮）
print(greet("小明"))          # 输出：你好, 小明
print(greet("小红"))          # 输出：你好, 小红
```

把这四行拆开看：

| 部分 | 含义 | 类比 |
|------|------|------|
| `def` | 关键词"我要定义一个函数" | 宣告"开始装按钮" |
| `greet` | 函数名，以后靠它调用 | 按钮上写的字 |
| `(name)` | 参数（parameter），调用时喂进来的"料" | 按钮需要的输入 |
| 缩进的函数体 | 真正要执行的一串操作 | 按钮按下后跑的流程 |
| `return` | 把计算结果交还给调用者 | 按钮"吐"出的产出 |

> 💡 **Key Insight:** 函数 = 一个"有名字的一串操作"。定义一次，之后可以**无限次、用不同参数**调用它——这就是"封装"的雏形。

---

## 14.2 参数：给"按钮"喂不同的料

<div class="try-it">
<strong>🧩 练一练 14.2</strong>
<p>题目：写函数 add(a, b)，打印 / 返回两个数的和。</p>
<details><summary>💡 看看答案</summary>
<p>答案：<code>def add(a, b): return a + b</code>。参数 a、b 是喂进函数的“料”。</p>
</details>
</div>

`name` 叫**形参（parameter）**，调用时写进括号的 `"小明"` 叫**实参（argument）**。形参是"占位符"，实参是"真正喂进去的值"。

多个参数用逗号隔开：

```python
def add(a, b):          # 两个形参
    return a + b

print(add(3, 5))        # 实参 3 和 5 → 输出 8
print(add(10, 20))      # 输出 30
```

> 🤔 **Why 要分"形参/实参"两个词？** 因为定义时函数还不知道会用谁——它只知道"我需要一个 a 和一个 b"。直到你调用 `add(3,5)`，a 才真正变成 3。分开说，能避免"函数里用的 a 到底是哪来的"这种混乱。初学记不住也别慌，先记住：**定义里写的是形参，调用里填的是实参。**

参数还能给**默认值**，调用时可省略：

```python
def power(base, exp=2):     # exp 默认是 2（平方）
    return base ** exp

print(power(5))             # 没给 exp → 用默认 2 → 25
print(power(5, 3))          # 给了 → 5 ** 3 = 125
```

> 📝 **Note:** 带默认值的参数必须写在**不带默认值**的参数后面，否则 Python 会报错："non-default argument follows default argument"。记住顺序：**先必填，后选填**。

---

## 14.3 return：让函数"吐"出结果（不是只打印）

<div class="try-it">
<strong>🧩 练一练 14.3</strong>
<p>题目：写函数 square(n)，用 return 返回 n 的平方（不是只打印）。</p>
<details><summary>💡 看看答案</summary>
<p>答案：<code>def square(n): return n * n</code>。return 让函数“吐”出结果，能被别的代码接着用。</p>
</details>
</div>

很多初学者分不清 `print` 和 `return`，这俩**完全不是一回事**：

```python
def bad_double(x):
    print(x * 2)            # 只是把结果显示在屏幕上，没交出来

def good_double(x):
    return x * 2            # 把结果交还给调用者，可以接着用


bad_double(4)               # 屏幕显示 8，但这个结果"用不掉"
y = good_double(4)          # y 现在是 8，可以接着算
print(y + 1)                # 输出 9
```

- `print(...)`：把东西**显示**出来，函数本身不返回有用的值（默认返回 `None`）。
- `return 值`：把值**交出去**，调用处能接住它继续运算。

> 🐛 **Common Bug:** 想接着用结果却只写了 `print`。比如写 `return print(x*2)`，其实 `print()` 返回的是 `None`，等于 `return None`——白白把结果弄丢了。要"算完还能用"，用 `return`；要"只是给人看"，用 `print`。两者也可以都要。

函数里一旦执行到 `return`，**立刻结束**并返回：

```python
def absolute(x):
    if x >= 0:
        return x        # x 非负，直接返回，下面不执行
    return -x           # 只有 x 为负才走到这

print(absolute(7))      # 7
print(absolute(-3))     # 3
```

---

## 14.4 文档字符串：给未来的自己写说明书

<div class="try-it">
<strong>🧩 练一练 14.4</strong>
<p>题目：给函数 square 写一句文档字符串（docstring）。</p>
<details><summary>💡 看看答案</summary>
<p>答案：<code>def square(n):
    """返回 n 的平方"""
    return n * n</code>。三引号写在函数体最前面。</p>
</details>
</div>

函数稍微复杂点，过两周你自己都看不懂它在干嘛。用**文档字符串（docstring）**——函数体第一行用三引号 `"""..."""` 写说明——就能随时用 `help()` 查：

```python
def celsius_to_fahrenheit(c):
    """把摄氏度转成华氏度。

    参数:
        c (float): 摄氏度
    返回:
        float: 对应的华氏度
    """
    return c * 9 / 5 + 32


help(celsius_to_fahrenheit)      # 打印上面那段说明
print(celsius_to_fahrenheit(0))  # 32.0
print(celsius_to_fahrenheit(100))# 212.0
```

> ⚡ **Pro Tip:** 好的 docstring 不是"写了就行"，而是写清**这个函数干嘛、要什么参数、返回什么**。现在很多编辑器（VS Code）会在你调用函数时自动弹出这段说明——等于白送一个"迷你使用手册"。这是专业程序员的基本功，现在养成习惯最划算。

---

## 14.5 为什么封装：避免重复、易改

<div class="try-it">
<strong>🧩 练一练 14.5</strong>
<p>题目：为什么把重复代码写成函数？</p>
<details><summary>💡 看看答案</summary>
<p>答案：① 避免重复抄写；② 改一处全部生效；③ 好测试、好复用。函数就是给一串操作起了个名字。</p>
</details>
</div>

现在揭晓本章最核心的问题：**为什么要把代码塞进函数？**

假设第 7 章积分系统里，每来一位游客都要干这件事：

```python
# 改造前：重复三遍，逻辑散落各处
visitor = "小明"
points = 10
print(visitor + " 当前积分：" + str(points))

visitor = "小红"
points = 25
print(visitor + " 当前积分：" + str(points))

visitor = "小刚"
points = 15
print(visitor + " 当前积分：" + str(points))
```

问题一眼可见：**同样的结构复制了三遍**。哪天你想改格式（比如加个"🌟"），得改三处，改漏一处就显示不一致。

封装成一个函数后：

```python
# 改造后：逻辑只写一次
def show_points(visitor, points):
    print(visitor + " 当前积分：" + str(points) + " 🌟")

show_points("小明", 10)
show_points("小红", 25)
show_points("小刚", 15)
```

好处：

1. **避免重复**：逻辑只写一次，调用处干干净净。
2. **易改**：想改格式？只改函数体那一处，所有调用自动跟着变。
3. **可读**：`show_points("小明", 10)` 一眼就知道"这是在显示积分"，比一堆拼接字符串好读太多。
4. **可测试**：单独测这个函数对不对，不用管整个程序。

### 🔍 计算思维聚焦：封装 / 抽象（Encapsulation / Abstraction）

> 把一串操作打包成一个"按钮"——外面的人只管按、只管喂参数、只管接结果，**不用关心里面怎么实现的**。这就是**封装 / 抽象**。

想想你天天用的手机：你按"拍照"就知道会出照片，但你完全不用懂 CMOS 感光、ISP 图像处理那些底层电路。**函数就是代码世界的"拍照按钮"**：把复杂藏起来，只暴露简单接口。抽象是计算思维的基石——没有它，你永远只能对着最底层的细节劳作，写不出大程序。

---

## 14.6 实战重构：把第7章积分系统重构成函数

回到第 7 章的积分系统（详见[第7章](../control-flow/while-loops.md)）。当时你大概是这样累加积分的（这里用函数版重构成"发奖励"）：

```python
# 重构前（伪代码思路）：每次加分都手写一遍"加分 + 提示"
score = 0
score = score + 10
print("获得 10 分，当前 " + str(score))
score = score + 50
print("获得 50 分，当前 " + str(score))
```

用函数封装"加分并报告"这一动作：

```python
def reward_points(score, gained):
    """给当前积分加上 gained，并打印一条提示，返回新的总分。"""
    score = score + gained
    print("获得 " + str(gained) + " 分，当前 " + str(score) + " 🌟")
    return score


score = 0
score = reward_points(score, 10)   # 当前 10
score = reward_points(score, 50)   # 当前 60
score = reward_points(score, 5)    # 当前 65
print("最终总分：", score)          # 最终总分： 65
```

> 💡 **Key Insight:** 注意 `score = reward_points(score, 10)` 这种写法——因为函数用 `return` 把新分数交回来，我们再赋给 `score`，就完成了"读取旧值 → 计算 → 写回新值"的闭环。这就是函数与外界"交换数据"的标准姿势。

重构后，无论加 10 分还是 1000 分，都只是换个数字调用，逻辑零重复。

> 🧮 **算法小课堂（前置彩蛋）：** 这一章你学会了"把操作打包成函数"——这看似只是省事，其实是为第 17 章起的算法世界铺路：搜索、排序、分治，本质是"把大问题拆成一堆小函数"。特别是**递归**（第 15 章）和**分治**（第 20 章），全靠"函数能调用函数"才能成立。先记住：**好函数 = 好算法的积木。**

---

## 14.7 🛠️ 项目工坊：算法游乐场"函数化"

前面各章我们给"算法游乐场"攒了不少零件：第 1 章画的招牌、第 5 章的门票问答机、第 7 章的积分系统、第 10-13 章用列表/字典管游客和排行榜。**但这些零件很多是"散装代码"。** 本章把它们重构成函数，让游乐场清爽起来。

下面是一段**自包含**的代码（直接复制运行，纯终端、无新依赖），把"打印门票"和"打招呼"都封装成函数：

```python
def print_ticket(name):
    """打印一张欢迎门票。"""
    print("=" * 28)
    print("   🎡 算法游乐场 门票")
    print("   欢迎你，" + name + "！")
    print("=" * 28)


def greet_visitor(name):
    """向游客打招呼，并返回一句欢迎语。"""
    msg = "你好, " + name + "！祝你玩得开心～"
    print(msg)
    return msg


# 模拟三位游客入园
guests = ["小明", "小红", "阿强"]
for guest in guests:
    print_ticket(guest)         # 按"门票按钮"
    greet_visitor(guest)        # 按"问候按钮"
    print()
```

运行后你会看到三位游客各拿到一张整齐的门票和一句问候。**现在游乐场多了两个"按钮"：`print_ticket(name)` 负责出票、`greet_visitor(name)` 负责问候——原本散落的打印逻辑被收进了函数，主流程只剩一个干净的循环。**

> ⚡ **Pro Tip:** 项目越做越大，"函数化"就越值钱。等你写到第 14 章之后、准备做排行榜时，你会发现：几乎所有功能都能是"一个函数"。这一章就是让你养成"先想函数，再写逻辑"的肌肉记忆。

---

## 14.8 ⚔️ 挑战擂台

> 擂台题偏开放，答案不唯一，敢写就赢。

**擂台 1 — 万能门票机：** 给 `print_ticket` 加一个可选参数 `vip=False`，当 `vip=True` 时门票显示"🌟 VIP 通道"，否则显示普通通道。

**擂台 2 — 积分翻倍卡：** 写一个函数 `double_if_even(score)`，如果当前积分是偶数就翻倍返回，奇数则原样返回（提示：用 `%` 取余判断奇偶）。

---

## 🏅 本章通关徽章：按钮工程师

<div class="badge-card">
<strong>如果你能做到下面 4 件事，就获得“按钮工程师”徽章：</strong>
<ul>
<li>能用 <code>def</code> 定义一个函数。</li>
<li>能用参数让同一个函数处理不同输入。</li>
<li>能分清 <code>print</code> 和 <code>return</code>。</li>
<li>能把重复代码重构成一个可复用函数。</li>
</ul>
</div>

---

## ⚠️ Common Mistakes in Chapter 14

| # | 误区 | 示例 | 为什么错 | 修正 |
|---|------|------|---------|------|
| 1 | 忘写冒号 `:` | `def greet(name)` | `def` 行必须以 `:` 结尾 | 改成 `def greet(name):` |
| 2 | 函数体没缩进 | `def f():\nprint("hi")` | 函数体必须缩进，否则不属于函数 | 函数体统一缩进 4 个空格 |
| 3 | 该用 `return` 却用 `print` | `return print(x*2)` | `print` 返回 `None`，结果被丢掉 | 要"接住结果"就用 `return x*2` |
| 4 | 默认值参数写前面 | `def f(exp=2, base)` | 必填参数不能在选填参数后 | 顺序改成 `def f(base, exp=2)` |
| 5 | 以为 `return` 后代码还会跑 | `return x\nprint("done")` | `return` 立刻结束函数 | 把还要执行的代码放 `return` 之前 |
| 6 | 调用时张冠李戴参数 | `add(b=3, a=5)` 写反 | 位置参数顺序错会算错 | 用位置传参时按顺序；要乱序就写 `add(a=5, b=3)` |

---

## Chapter Summary

### 📌 Key Takeaways

| 概念 | 要点 | 为什么重要 |
|------|------|------------|
| `def` 定义函数 | `def 名(参数):` + 缩进函数体 | 把一串操作打包成"按钮" |
| 形参 / 实参 | 定义里是形参，调用里填实参 | 区分"占位"和"真值"，避免混淆 |
| `return` | 把结果交出去，可继续用 | 与 `print` 完全不同，是函数对外接口 |
| 默认值参数 | `def f(a, b=2)`，必填在前 | 让函数更灵活、调用更省事 |
| docstring | 三引号写在函数首行 | 自动生成说明，专业基本功 |
| 封装 / 抽象 | 隐藏细节，只暴露接口 | 计算思维基石，避免重复、易改 |

### ❓ FAQ

**Q1: 函数和变量一样，要先定义才能用吗？**
> A: 对。`def` 那一段只是"造按钮"，必须写在调用之前（或同一文件里先执行到）。如果调用时 Python 还没见过这个函数，会报 `NameError`。写脚本时养成"先定义、后调用"的顺序就好。

**Q2: 一个函数能调用另一个函数吗？**
> A: 当然，而且非常常见。比如 `print_ticket` 里可以再调用一个 `draw_border()` 画边框。函数互相调用，正是拼出大程序的方式——这也是第 15 章递归（函数调用自己）和后续算法的基础。

**Q3: 什么时候该把代码写成函数？**
> A: 三个信号：① 同一段逻辑出现了两次以上；② 某段代码有了"独立意义"（如"算出票""发奖励"）；③ 你想单独测试它。满足任一，就封装。初学不必过度拆分，但"重复"是最该封装的信号。

### 🔗 Connections to Later Chapters

- **[Chapter 15: 作用域与递归](../functions/scope-recursion.md)** 会讲函数内部的变量"活在哪"、以及函数如何**自己调用自己**（递归）。
- **[Chapter 16: 模块与标准库](../functions/modules.md)** 讲怎么把函数组织进"模块"，并直接复用别人写好的函数（标准库）。
- **[第17章起 · 算法启蒙](../algorithms/big-o.md)** 的搜索、排序、分治，本质都是"用函数把算法步骤封装好"——今天的函数就是明天算法的积木。

---


## 🎮 加练任务包

> 下面这些题目不一定比章末题更难，但更适合“多刷几遍、把手感练出来”。建议先独立做，再展开提示。

### 加练 14.A · 门票函数 🟢

写函数 `ticket_total(price, count)` 返回总价。

<details>
<summary>💡 提示 / 答案要点</summary>

`def ticket_total(price, count): return price * count`。用 `return` 交出结果，别只 `print`。

</details>

---

### 加练 14.B · 问候复用 🟢

写函数 `greet(name)` 返回 `你好，name`，并调用两次。

<details>
<summary>💡 提示 / 答案要点</summary>

函数定义一次，可用不同参数调用多次：`greet("小明")`、`greet("小红")`。

</details>

---

### 加练 14.C · 重构重复代码 🟡

如果三处都要打印同样格式的排行榜标题，你会怎样用函数减少重复？

<details>
<summary>💡 提示 / 答案要点</summary>

写一个 `print_title(title)` 函数，把重复的装饰线和标题输出放进去，需要时调用。

</details>

---


---

## Practice Problems

---

**Problem 14.1 — 写个求平方的函数** 🟢 Easy

写一个函数 `square(n)`，返回 `n` 的平方。然后调用它算出 `square(7)` 并打印。

**Sample Input:** （调用 `square(7)`）
**Sample Output:** `49`

<details>
<summary>💡 Solution (click to reveal)</summary>

**Approach:** 函数接收一个数，用 `**` 运算符求平方，再用 `return` 交回结果。

```python
def square(n):
    return n ** 2

print(square(7))     # 49
```

**Key points:**
- `return n ** 2` 直接把结果交出去，调用处 `print(square(7))` 接住再打印。
- 如果写成 `print(n ** 2)` 而不 `return`，`square(7)` 会返回 `None`，后面想接着运算就接不到。

</details>

---

**Problem 14.2 — 带默认参数的问候** 🟡 Medium

写一个函数 `welcome(name, vip=False)`：普通游客打印 `"欢迎，{name}！"`，VIP 打印 `"🌟 贵宾欢迎，{name}！"`。分别用 `welcome("小明")` 和 `welcome("王总", vip=True)` 调用。

**Sample Output:**
```
欢迎，小明！
🌟 贵宾欢迎，王总！
```

<details>
<summary>💡 Solution (click to reveal)</summary>

**Approach:** 用 `if` 判断 `vip` 这个布尔参数，决定打印哪句话。默认值 `vip=False` 让普通调用可省略。

```python
def welcome(name, vip=False):
    if vip:
        print("🌟 贵宾欢迎，" + name + "！")
    else:
        print("欢迎，" + name + "！")

welcome("小明")
welcome("王总", vip=True)
```

**Key points:**
- `vip=False` 是默认值参数，必须放在 `name` 之后。
- 想触发 VIP 分支，调用时显式写 `vip=True`（关键字传参，顺序随意也安全）。

</details>

---

**Problem 14.3 — 重构：把重复代码变成函数** 🟡 Medium

下面这段"散装代码"重复了三遍同样的格式。把它重构成一个函数 `report(subject, score)`，再调用三次。

```python
print("科目 数学 得分 88")
print("科目 语文 得分 92")
print("科目 英语 得分 76")
```

**Sample Output:**
```
科目 数学 得分 88
科目 语文 得分 92
科目 英语 得分 76
```

<details>
<summary>💡 Solution (click to reveal)</summary>

**Approach:** 把"科目 X 得分 Y"这一定型文字封装成函数，两个变化的部分变成参数 `subject` 和 `score`。

```python
def report(subject, score):
    print("科目 " + subject + " 得分 " + str(score))

report("数学", 88)
report("语文", 92)
report("英语", 76)
```

**Key points:**
- `score` 是整数，拼接字符串前要 `str(score)` 转成文字。
- 重构后想改格式（比如加 emoji）只改函数一处，三处调用全自动更新——这就是封装的价值。

</details>

---

**Problem 14.4 — 🏆 Challenge：迷你计算器** 🏆 Challenge

写一个函数 `calculator(a, b, op)`，根据 `op` 的值（`"+"`、`"-"`、`"*"`、`"/"`）返回 `a` 和 `b` 的对应运算结果。处理除零：当 `op` 是 `"/"` 且 `b == 0` 时，返回字符串 `"除数不能为0"`。用 `calculator(10, 5, "+")`、`calculator(10, 0, "/")` 测试。

**Sample Output:**
```
15
除数不能为0
```

<details>
<summary>💡 Solution (click to reveal)</summary>

**Approach:** 用 `if / elif / else` 分支匹配不同的 `op`；除法先特判 `b == 0`。

```python
def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "除数不能为0"
        return a / b
    else:
        return "不支持的运算"


print(calculator(10, 5, "+"))   # 15
print(calculator(10, 0, "/"))   # 除数不能为0
```

**Key points:**
- `return` 写在每个分支里，匹配到就立刻返回，互不干扰。
- 除零用 `if b == 0` 提前拦下，避免运行时抛 `ZeroDivisionError`。
- `else` 兜底"不支持的运算"，让函数更健壮。

</details>

---

> 💡 **记住这一句：** 函数是给代码装的"按钮"——**定义一次，调用千次；逻辑只写一遍，改动只改一处。**
