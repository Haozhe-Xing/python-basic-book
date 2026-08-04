# -*- coding: utf-8 -*-
"""Bulk-insert 5 '练一练' interactive cards into the body of each chapter,
   anchored right after the chosen section heading. Safe: aborts without writing
   if any anchor fails to match (so no partial corruption)."""

DATA = {
    "src/getting-started/install.md": [
        ("0.0 两条路", "如果你只想 5 分钟跑出第一幅画，该走哪条路？",
         "答案：走<b>在线环境</b>（Replit / Colab），不用本地安装就能跑。等想长期写代码、打比赛，再回来看本章本地安装。"),
        ("0.1 Windows", "在 Windows 安装 Python 时，那个必须勾上的小框叫什么？不勾会怎样？",
         "答案：勾 <code>Add python.exe to PATH</code>。不勾的话，在命令行输入 <code>python</code> 会提示“找不到命令”，后面每步都踩坑。"),
        ("0.2 macOS", "在 macOS 终端里，你应该输入 python 还是 python3？为什么？",
         "答案：用 <code>python3</code>。macOS 自带一个老旧的 <code>python</code> 指向 Python 2（已淘汰），用它会踩一堆坑。"),
        ("0.3 验证", "写出两条能“证明 Python 装好了”的命令。",
         "答案：① <code>python3 --version</code>（或 <code>python --version</code>）显示版本号；② <code>python3</code> 进入 <code>&gt;&gt;&gt;</code> 交互模式，能直接算 <code>1+1</code>。"),
        ("0.4 （可选）", "uv 是干什么的？零基础现在必须装它吗？",
         "答案：uv 用来管虚拟环境、装第三方包。<b>不必</b>——学到第 16 章“模块”再装也不迟。"),
    ],
    "src/getting-started/hello-python.md": [
        ("1.0 在线环境", "在在线环境里，点“运行”后，代码的输出显示在哪里？",
         "答案：显示在编辑器<b>下方的控制台 / 输出区</b>。如果没看到，确认你按了“运行 / Run”按钮。"),
        ("1.1 你的第一行", "让电脑打印出你自己的名字。",
         "答案：<code>print(\"小龙\")</code> 会输出 <code>小龙</code>。<code>print()</code> 括号里用引号包住文字即可。"),
        ("1.2 海龟画图", "让海龟画一个正方形（提示：forward 前进 + right 右转各 4 次）。",
         "答案：<code>import turtle</code> 后，<code>for _ in range(4): t.forward(100); t.right(90)</code>。"),
        ("1.3 让画", "让海龟画一个等边三角形（每个外角是 120°）。",
         "答案：<code>for _ in range(3): t.forward(100); t.right(120)</code>。每画一条边右转 120° 刚好合拢。"),
        ("🧠 Mental Model: 海龟与画布", "海龟刚启动时，它面朝哪个方向？",
         "答案：面朝<b>右（东）</b>。<code>forward(100)</code> 让它朝当前面向前进 100 步，<code>right(90)</code> 原地右转 90°。"),
    ],
    "src/foundations/variables.md": [
        ("2.1 变量是什么", "用变量存你的年龄，再打印“我今年 X 岁”。",
         "答案：<code>age = 14</code>，再用 f-string：<code>print(f\"我今年 {age} 岁\")</code> 输出 <code>我今年 14 岁</code>。"),
        ("2.2 四种基础", "判断 3.14 是 int 还是 float？",
         "答案：<code>float</code>（带小数点）。整数 3 才是 <code>int</code>。可用 <code>type(3.14)</code> 验证。"),
        ("2.3 给变量起名", "下面哪个变量名不合法：my_name / 2cool / total_score / class？",
         "答案：<code>2cool</code>（不能以数字开头）、<code>class</code>（是 Python 关键字）。合法：my_name、total_score。"),
        ("2.4 看清类型", "用 type() 看看字符串 \"hello\" 的类型。",
         "答案：<code>type(\"hello\")</code> 输出 <code>&lt;class 'str'&gt;</code>。"),
        ("2.5 类型转换", "把字符串 \"42\" 变成整数 42，再加 8，打印结果。",
         "答案：<code>n = int(\"42\") + 8</code>，<code>print(n)</code> 输出 <code>50</code>。"),
    ],
    "src/foundations/strings.md": [
        ("3.1 字符串是什么", "创建字符串 s = \"Python\"，打印它的长度。",
         "答案：<code>s = \"Python\"</code> 后 <code>print(len(s))</code> 输出 <code>6</code>。"),
        ("3.2 拼接", "把 \"Hello\" 和 \"World\" 拼成 \"HelloWorld\"（中间不留空格）。",
         "答案：<code>print(\"Hello\" + \"World\")</code> 输出 <code>HelloWorld</code>。要加空格就写 <code>\"Hello \" + \"World\"</code>。"),
        ("3.3 索引", "s = \"Python\"，取出第 1 个字符（索引 0）和最后一个（负数索引）。",
         "答案：<code>s[0]</code> 是 <code>'P'</code>，<code>s[-1]</code> 是 <code>'n'</code>。负数从右往左数。"),
        ("3.4 切片", "s = \"Python\"，取出中间的 \"yth\"（索引 1 到 3）。",
         "答案：<code>s[1:4]</code> 输出 <code>'yth'</code>。切片 <code>[a:b]</code> 取从 a 到 b-1。"),
        ("3.5 长度", "字符串 \"banana\"，数一数里面有几个字母 'a'？",
         "答案：3 个。可用 <code>\"banana\".count('a')</code> 得到 <code>3</code>。"),
    ],
    "src/foundations/operators.md": [
        ("4.1 算术", "17 // 5 和 17 % 5 各是多少？",
         "答案：<code>17 // 5 = 3</code>（整除，商 3），<code>17 % 5 = 2</code>（取余，剩 2）。"),
        ("4.2 比较", "写表达式判断年份 y 是闰年（被 4 整除且不被 100 整除，或被 400 整除）。",
         "答案：<code>(y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)</code>。整百年必须被 400 整除才算闰年。"),
        ("4.3 逻辑", "表达式 True and False or True 的结果是？",
         "答案：<code>True</code>。先算 <code>and</code>：<code>True and False = False</code>，再算 <code>or</code>：<code>False or True = True</code>。"),
        ("4.4 运算符优先级", "3 + 2 * 4 等于几？为什么不是 20？",
         "答案：<code>11</code>。<b>乘法优先于加法</b>，先算 2*4=8，再加 3。要想先加就加括号：(3+2)*4=20。"),
        ("4.5 真值表", "用真值表判断：not (True and False) 是？",
         "答案：<code>not False = True</code>。先括号里 <code>True and False = False</code>，再取反得到 True。"),
    ],
    "src/foundations/input-output.md": [
        ("5.1 input", "用 input() 问用户名字，并打印“你好，XX”。",
         "答案：<code>name = input(\"你叫什么？\")</code> 后 <code>print(\"你好，\" + name)</code>。"),
        ("5.2 类型转换：int", "让用户输入两个数（用 int(input())），打印它们的和。",
         "答案：<code>a=int(input()); b=int(input()); print(a+b)</code>。注意 input 得到的是字符串，必须转 int 才能相加。"),
        ("5.3 f-string 输出", "用 f-string 打印“我叫 X，今年 Y 岁”（变量 name、age）。",
         "答案：<code>print(f\"我叫 {name}，今年 {age} 岁\")</code>。花括号里直接写变量名。"),
        ("5.4 多值输入", "用户输入一行“3 5 7”，用 split 取出三个数并求和。",
         "答案：<code>nums = input().split()</code> 得到 <code>['3','5','7']</code>，再 <code>sum(int(x) for x in nums)</code> = 15。"),
        ("5.5 案例：互动问答", "写一个互动问答：问对方最喜欢的语言，打印一句带答案的话。",
         "答案：<code>lang = input(\"你最喜欢的语言？\")</code> 然后 <code>print(f\"原来你喜欢 {lang}！\")</code>。"),
    ],
    "src/control-flow/conditionals.md": [
        ("6.0 为什么需要", "在生活里举一个需要“判断”的例子，写成“如果…就…否则…”的形式。",
         "答案：例如“如果下雨，就带伞；否则戴帽子”。编程里的 <code>if / else</code> 就是这种分叉。"),
        ("6.1 最简单的判断", "写 if 判断变量 x 是否大于 10，是则打印“大”。",
         "答案：<code>if x &gt; 10: print(\"大\")</code>。注意冒号 <code>:</code> 和下一行缩进。"),
        ("6.2 多岔路口", "用 elif 把 0~100 的分数分成 优（≥90）、良（≥80）、中（≥60）、差 四档。",
         "答案：<code>if s&gt;=90: print('优')</code>  elif <code>s&gt;=80</code> 良，<code>elif s&gt;=60</code> 中，<code>else</code> 差。"),
        ("6.3 案例一", "成绩判断：≥90 为 A，≥80 为 B，≥60 为 C，否则 D（写完整 if/elif/else）。",
         "答案：<code>if s&gt;=90: g='A' elif s&gt;=80: g='B' elif s&gt;=60: g='C' else: g='D'</code>。顺序很重要，先判最高的。"),
        ("6.4 嵌套判断", "判断一个数字是“正数 / 负数 / 零”。",
         "答案：<code>if n&gt;0: print('正数') elif n&lt;0: print('负数') else: print('零')</code>。"),
    ],
    "src/control-flow/while-loops.md": [
        ("7.0 生活里的", "在生活里举一个“只要…就一直…”的例子。",
         "答案：例如“只要水还没开，就继续等”；或“只要还剩作业，就继续写”。这就是 while 思维。"),
        ("7.1 while 的基本", "用 while 打印 1 到 5。",
         "答案：<code>i=1</code> 然后 <code>while i&lt;=5: print(i); i+=1</code>。循环变量 i 要在循环里更新，否则死循环。"),
        ("7.2 案例一", "用 while 计算 1 + 2 + … + 100。",
         "答案：<code>total=0; i=1</code>；<code>while i&lt;=100: total+=i; i+=1</code>，结果 5050。"),
        ("7.3 break", "用 while 和 break 实现“输入 quit 就退出”。",
         "答案：<code>while True:</code> 内 <code>s=input(); if s=='quit': break</code>。break 立刻跳出循环。"),
        ("7.4 防范死循环", "防范死循环的三条铁律里，循环变量必须在循环体内完成什么动作？",
         "答案：必须<b>更新</b>（让循环条件终会变为假），比如 <code>i += 1</code>，否则条件永远成立。"),
    ],
    "src/control-flow/for-loops.md": [
        ("8.0 生活里的", "在生活里举一个“对每一样东西都做一遍”的例子。",
         "答案：例如“对每一本书都盖个章”；或“对每一个同学都点一次名”。这就是 for 思维。"),
        ("8.1 for", "用 for 遍历列表 [1, 2, 3]，把每个元素打印出来。",
         "答案：<code>for x in [1,2,3]: print(x)</code>。每次循环 x 依次取 1、2、3。"),
        ("8.2 range", "用 range 分别打印：0~4、1~5、0~9 的偶数。",
         "答案：<code>range(5)</code> → 0,1,2,3,4；<code>range(1,6)</code> → 1..5；<code>range(0,10,2)</code> → 0,2,4,6,8。"),
        ("8.3 遍历字符串", "用 for 遍历字符串 \"hello\"，把每个字符打印出来。",
         "答案：<code>for ch in \"hello\": print(ch)</code> 依次输出 h e l l o。"),
        ("8.4 案例一", "用嵌套 for 打印 3 行、每行 5 个星号 * 的矩形。",
         "答案：外层 <code>for r in range(3):</code>，内层 <code>for c in range(5): print('*', end='')</code>，每行结束 <code>print()</code> 换行。"),
    ],
    "src/control-flow/debugging.md": [
        ("9.1 读得懂报错", "SyntaxError 一般是什么类型的错误？",
         "答案：<b>语法写错</b>，比如少冒号、引号没闭合、缩进不对。Python 会在出错行打红叉提示。"),
        ("9.2 print 调试", "程序没报错，但答案不对，最朴素怎么查？",
         "答案：在关键位置插 <code>print(变量)</code>，看中间值是不是你以为的那样，逐步缩小怀疑范围。"),
        ("9.3 断言", "用 assert 给“分数必须在 0~100”加一道警报。",
         "答案：<code>assert 0 &lt;= score &lt;= 100, \"分数越界\"</code>。条件为假时立刻报错停下来。"),
        ("9.4 缩小范围", "一段很长的代码出错，用“二分定位法”该先在哪儿插 print？",
         "答案：先在<b>正中间</b>插。看前半段还是后半段出错，再在出错的那半段中间插，像二分查找一样快速锁定。"),
        ("9.5 橡皮鸭法", "什么是“橡皮鸭法”？",
         "答案：把代码<b>逐行讲给一只橡皮鸭（或任何东西）听</b>。讲着讲着，你常常自己就发现了 bug 在哪。"),
    ],
    "src/data-structures/lists.md": [
        ("10.1 为什么需要", "为什么用列表，而不是定义一堆 a1、a2、a3 散装变量？",
         "答案：列表能<b>统一遍历、统一增删</b>，散装变量做不到“对每一个都做一遍”。"),
        ("10.2 创建列表", "创建列表 scores = [88, 92, 75]，打印第二个元素（索引 1）。",
         "答案：<code>scores = [88,92,75]</code> 后 <code>print(scores[1])</code> 输出 <code>92</code>。"),
        ("10.3 索引", "列表 nums = [10, 20, 30]，取出最后两个元素（用切片）。",
         "答案：<code>nums[-2:]</code> 得到 <code>[20, 30]</code>。负数切片从末尾数。"),
        ("10.4 切片", "用 append 往 [\"a\", \"b\"] 后面加一个 \"c\"。",
         "答案：<code>lst = [\"a\",\"b\"]; lst.append(\"c\")</code>，此时 lst 为 <code>['a','b','c']</code>。"),
        ("10.5 增", "用 for 遍历列表 [\"小明\",\"小红\",\"小刚\"]，逐个打印名字。",
         "答案：<code>for name in [\"小明\",\"小红\",\"小刚\"]: print(name)</code>。"),
    ],
    "src/data-structures/tuples-sets.md": [
        ("11.1 元组 tuple", "元组 (1, 2, 3) 创建之后，能修改其中的元素吗？",
         "答案：<b>不能</b>。元组（tuple）是不可变的，这是它和列表最大的区别。"),
        ("11.2 为什么", "什么时候用元组比用列表更好？",
         "答案：当这串数据<b>不该被改动</b>时（如坐标、配置），用元组更安全，还能当作字典的键。"),
        ("11.3 元组也能", "遍历元组 t = (1, 2, 3)，把每个元素打印出来。",
         "答案：<code>for x in (1,2,3): print(x)</code>。元组同样支持遍历和切片。"),
        ("11.4 集合 set", "集合 set([1, 1, 2, 2, 3]) 去重之后是？",
         "答案：<code>{1, 2, 3}</code>。集合自动丢弃重复元素，顺序不保证。"),
        ("11.5 集合的运算", "用集合求两个班的“共同学生”（交集）。",
         "答案：<code>set(a) & set(b)</code> 得到同时属于两班的人。并集用 <code>|</code>，差集用 <code>-</code>。"),
    ],
    "src/data-structures/dictionaries.md": [
        ("12.1 创建字典", "创建字典存小明的成绩 {\"语文\":88, \"数学\":95}，查“数学”的分数。",
         "答案：<code>d = {\"语文\":88, \"数学\":95}</code>，<code>print(d[\"数学\"])</code> 输出 <code>95</code>。"),
        ("12.2 查", "用 get() 查一个可能不存在的 key，并给默认值 0。",
         "答案：<code>d.get(\"英语\", 0)</code>。若不存在返回 0，而不会像 <code>d[\"英语\"]</code> 那样报错。"),
        ("12.3 增 / 改", "往字典 d 里加一对新的键值 age: 14。",
         "答案：<code>d[\"age\"] = 14</code>。若 key 已存在则是“改”，不存在就是“增”。"),
        ("12.4 删", "用 for 遍历字典的 items()，打印“科目: 分数”。",
         "答案：<code>for k, v in d.items(): print(f\"{k}: {v}\")</code>。<code>items()</code> 一次拿出键和值。"),
        ("12.5 遍历", "判断 \"数学\" 是不是字典 d 里的 key。",
         "答案：<code>\"数学\" in d</code> 返回 <code>True</code>。用 <code>in</code> 判断键在不在，最快。"),
    ],
    "src/data-structures/nested-data.md": [
        ("13.1 列表套字典", "怎么用“列表套字典”表示多个学生？",
         "答案：<code>[{\"name\":\"小明\",\"age\":14}, {\"name\":\"小红\",\"age\":13}]</code>。列表管“一群”，字典管“每个人的属性”。"),
        ("13.2 遍历嵌套", "遍历上面的嵌套列表，把每个学生的名字打印出来。",
         "答案：<code>for stu in students: print(stu[\"name\"])</code>。先取出每个学生字典，再按 key 取值。"),
        ("13.3 字典套列表", "字典套列表：{\"一班\":[\"小明\",\"小红\"]}，打印“一班”所有人。",
         "答案：<code>for name in classes[\"一班\"]: print(name)</code>。外层字典取值得到列表，再遍历列表。"),
        ("13.4 字典套字典", "字典套字典：{\"小明\":{\"age\":14}}，查小明的年龄。",
         "答案：<code>students[\"小明\"][\"age\"]</code> 得到 <code>14</code>。像查两层抽屉。"),
        ("13.5 改嵌套", "把嵌套数据里“小红”的年龄从 13 改成 14。",
         "答案：<code>students[\"小红\"][\"age\"] = 14</code>。定位到最里层再赋值即可。"),
    ],
    "src/functions/functions-intro.md": [
        ("14.1 你的第一个", "写一个名为 greet 的函数，输入名字，打印“你好，XX”。",
         "答案：<code>def greet(name): print(f\"你好，{name}\")</code>，调用 <code>greet(\"小龙\")</code>。"),
        ("14.2 参数", "写函数 add(a, b)，打印 / 返回两个数的和。",
         "答案：<code>def add(a, b): return a + b</code>。参数 a、b 是喂进函数的“料”。"),
        ("14.3 return", "写函数 square(n)，用 return 返回 n 的平方（不是只打印）。",
         "答案：<code>def square(n): return n * n</code>。return 让函数“吐”出结果，能被别的代码接着用。"),
        ("14.4 文档字符串", "给函数 square 写一句文档字符串（docstring）。",
         "答案：<code>def square(n):\n    \"\"\"返回 n 的平方\"\"\"\n    return n * n</code>。三引号写在函数体最前面。"),
        ("14.5 为什么封装", "为什么把重复代码写成函数？",
         "答案：① 避免重复抄写；② 改一处全部生效；③ 好测试、好复用。函数就是给一串操作起了个名字。"),
    ],
    "src/functions/scope-recursion.md": [
        ("15.1 局部变量", "在函数里定义的变量，函数外面能直接用吗？",
         "答案：<b>不能</b>。那是<b>局部变量</b>，只活在这个函数的“房间”里。"),
        ("15.2 全局变量", "全局变量和局部变量的主要区别？",
         "答案：全局变量<b>所有函数共享</b>（像客厅），局部变量只在自己函数内有效（像卧室私物）。"),
        ("15.3 参数传递", "列表这种“可变对象”作为参数传进函数，在里面被修改，会影响外面的原列表吗？",
         "答案：<b>会</b>。因为传的是同一个对象的引用，函数里改了，外面也跟着变。"),
        ("15.4 递归：函数", "用递归思想算 factorial(5)：写出“大问题 = 小一号的同问题”这个关系。",
         "答案：<code>factorial(n) = n * factorial(n-1)</code>，基线 <code>factorial(1)=1</code>。大问题化成小一号的自己。"),
        ("15.5 递归三要素", "写递归的三个要素（checklist）是？",
         "答案：① <b>基线条件</b>（何时停）；② <b>递归步</b>（调用自己，规模变小）；③ <b>向基线收敛</b>（每步都更接近停下）。"),
    ],
    "src/functions/modules.md": [
        ("16.1 三种导入", "写出导入 math 模块的三种方式。",
         "答案：① <code>import math</code>；② <code>from math import sqrt</code>；③ <code>import math as m</code>（起别名）。"),
        ("16.2 标准库之 math", "用 math 模块求 16 的平方根。",
         "答案：<code>import math</code> 后 <code>math.sqrt(16)</code> 得到 <code>4.0</code>。"),
        ("16.3 标准库之 random", "用 random 模块模拟掷一个六面骰子。",
         "答案：<code>import random</code> 后 <code>random.randint(1, 6)</code> 随机返回 1~6。"),
        ("16.4 标准库之 datetime", "用 datetime 打印今天的日期。",
         "答案：<code>from datetime import date</code> 后 <code>print(date.today())</code>。"),
        ("16.5 pip", "pip 是干什么用的？",
         "答案：pip 用来<b>安装第三方包</b>（别人写好的工具），比如 <code>pip install 包名</code>，站在别人肩膀上。"),
    ],
    "src/algorithms/big-o.md": [
        ("17.1 什么是", "衡量一个“好算法”的三个标准是什么？",
         "答案：① <b>正确</b>；② <b>快</b>（时间）；③ <b>省内存</b>（空间）。"),
        ("17.2 时间复杂度", "数“操作次数”：把数组每个元素加一遍，和双重循环两两比较，复杂度分别是？",
         "答案：逐个加是 <code>O(n)</code>（n 次）；双重循环是 <code>O(n²)</code>（约 n×n 次）。"),
        ("17.3 四种最常见", "用一句生活比喻分别说明 O(1)、O(log n)、O(n)、O(n²)。",
         "答案：O(1) 喊名字（一下就好）；O(log n) 翻书找页（每次砍半）；O(n) 一页页翻（挨个问）；O(n²) 全班握手（人人两两见面）。"),
        ("17.4 最坏情况", "算法分析里常说的“最坏情况（Worst Case）”指什么？",
         "答案：指<b>输入最不利</b>时算法的表现。我们通常用最坏情况来给算法“保底”估价。"),
        ("17.5 别被常数", "为什么比较 O(n) 和 O(2n) 时，说它们“差不多”？",
         "答案：因为看的是<b>增长趋势</b>、忽略常数系数。n 很大时，n 和 2n 都比 n² 快得多。"),
    ],
    "src/algorithms/searching.md": [
        ("18.1 线性查找", "线性查找最坏情况下，要比较多少次？",
         "答案：最多 <b>n 次</b>（目标在最后，或根本不在）。数据无序时只能挨个问。"),
        ("18.2 二分查找", "二分查找能“每次砍半”的前提是什么？",
         "答案：数据必须<b>有序</b>。无序就没法判断目标在左半还是右半，二分失效。"),
        ("18.3 代码实现", "写线性查找，在 [3, 1, 4, 2] 中找 4，返回它的索引。",
         "答案：<code>for i,x in enumerate([3,1,4,2]): if x==4: print(i)</code> 输出 <code>2</code>。"),
        ("18.4 数一数", "二分每轮把范围砍成一半，n = 1000 大约几轮能找到？",
         "答案：约 <b>10 轮</b>。因为 2^10 = 1024 ≥ 1000，每次砍半，10 次就够。"),
        ("18.5 线性 vs 二分", "什么时候该用线性查找，而不是二分？",
         "答案：数据<b>无序</b>或<b>很小</b>时。无序没法二分；很小则二分省下的次数不值当。"),
    ],
    "src/algorithms/sorting.md": [
        ("19.1 为什么排序", "排序为什么这么重要？",
         "答案：二分查找、去重、做排行榜都<b>依赖数据有序</b>。排序是很多算法的“前置动作”。"),
        ("19.2 冒泡排序", "冒泡排序每一轮主要做什么？",
         "答案：<b>相邻两个比大小</b>，大的往后“冒”。一轮下来，最大的数就沉到最右了。"),
        ("19.3 选择排序", "手动走一遍给 [3, 1, 2] 做选择排序，第一趟结束后数组变成？",
         "答案：第一趟找最小的 1 换到最前，变成 <code>[1, 3, 2]</code>。再两趟得到 [1,2,3]。"),
        ("19.4 插入排序", "插入排序像生活里整理什么的动作？",
         "答案：像<b>理扑克牌</b>——每张新牌，从右往左插到已排好序的那叠里合适的位置。"),
        ("19.5 三种排序对比", "冒泡、选择、插入这三种排序，时间复杂度都是？",
         "答案：都是 <code>O(n²)</code>。数据量一大就慢，但<b>思路直观</b>，是理解排序的好起点。"),
    ],
    "src/algorithms/recursion-divide.md": [
        ("20.1 递归回顾", "递归是“函数调用自己”，它必须有一个什么，否则会无限循环？",
         "答案：必须有<b>基线条件（base case）</b>——一个不再调用自己、直接返回的最小情形。"),
        ("20.2 分治思想", "“分而治之（分治）”一般分哪三步？",
         "答案：① <b>拆</b>：把大问题拆成小问题；② <b>解</b>：分别解决小问题；③ <b>合</b>：把小答案合并成最终答案。"),
        ("20.3 归并排序", "归并排序的时间复杂度是多少？为什么比 O(n²) 快？",
         "答案：<code>O(n log n)</code>。它每次把数组对半拆（log n 层），每层合并共扫 n 个（n 倍），相乘即 n·log n。"),
        ("20.4 汉诺塔", "n 个盘子的汉诺塔，最少需要几步？",
         "答案：<code>2^n - 1</code> 步。3 盘需 7 步，4 盘需 15 步，指数增长。"),
        ("20.5 记忆化", "记忆化（Memoization）主要解决什么问题？",
         "答案：解决<b>重复子问题被重复计算</b>。比如斐波那契不改写会算很多遍，用字典缓存中间结果就快了。"),
    ],
    "src/algorithms/basic-structures.md": [
        ("21.1 栈（Stack）", "栈（Stack）最主要的特点是什么？用生活比喻。",
         "答案：<b>后进先出 LIFO</b>（Last In First Out），像一摞盘子——最后放上去的，最先被拿走。"),
        ("21.2 队列（Queue）", "用 Python 列表模拟一个栈：入栈和出栈分别对应什么操作？",
         "答案：入栈 <code>stack.append(x)</code>，出栈 <code>stack.pop()</code>（弹出最后一个）。"),
        ("21.3 链表（Linked", "队列（Queue）和栈相反，它的特点？",
         "答案：<b>先进先出 FIFO</b>（First In First Out），像排队买票——先来的人先办完走。"),
        ("21.4 三种结构", "链表（Linked List）里每个“节点”由哪两部分组成？",
         "答案：① <b>数据</b>（本节点存的值）；② <b>指针 / next</b>（指向下一个节点的地址）。"),
        ("⚔️ 挑战擂台", "撤销（Ctrl+Z）功能更适合用栈还是队列？为什么？",
         "答案：<b>栈</b>。撤销总是退回“最近一次”操作，正是后进先出。"),
    ],
    "src/algorithms/greedy-simulation.md": [
        ("22.1 贪心直觉", "贪心算法每一步怎么选？",
         "答案：每一步都选<b>当下看起来最优</b>的那个，选了不回头、不反悔。"),
        ("22.2 何时贪心", "活动选择问题里，贪心通常按什么来排序挑选？",
         "答案：按<b>结束时间</b>从早到晚排，每次选“结束最早、且不和已选冲突”的活动，能安排最多。"),
        ("22.3 模拟题套路", "算法竞赛里的“模拟题”一般怎么下手？",
         "答案：先把现实问题<b>建模成状态</b>（变量表示当前情况），再用 <code>循环</code> 一步一步推进状态直到结束。"),
        ("22.4 两个 USACO", "用面值 [100, 50, 20, 10, 1] 贪心凑出 370 元，怎么选？",
         "答案：每次拿能拿的最大面值：100×3 + 50×1 + 20×1 = 370，共 5 张（最少）。"),
        ("⚔️ 挑战擂台", "贪心算法得到的结果一定是最优的吗？",
         "答案：<b>不一定</b>。只有满足“贪心选择性质”的问题（如零钱、活动选择）才对，其他的贪心会翻车。"),
    ],
    "src/projects/text-adventure.md": [
        ("23.1 先把", "动手写文字冒险前，先把“古堡”想成什么数据结构？",
         "答案：想成<b>字典</b>——键是场景名，值是该场景的信息（描述 + 可走的方向）。"),
        ("23.2 用字典存", "每个“场景”字典里，至少要有哪两类信息？",
         "答案：① <b>描述</b>（这个场景长啥样）；② <b>可选方向</b>（能去哪、对应哪个场景）。"),
        ("23.3 用函数驱动", "用函数驱动冒险时，负责“显示当前场景”的函数通常叫什么？",
         "答案：常叫 <code>show_room()</code> 之类——它根据当前场景打印描述和可走方向。"),
        ("23.4 主循环", "主循环要让游戏一直跑下去，直到发生什么才停？",
         "答案：直到玩家<b>输入退出命令</b>、或<b>到达胜利场景</b>。用 <code>while</code> 循环 + 退出条件实现。"),
        ("23.5 完整代码", "这个冒险游戏怎么运行？",
         "答案：把代码保存成 <code>adventure.py</code>，在终端运行 <code>python adventure.py</code> 即可开玩。"),
    ],
    "src/projects/data-analysis.md": [
        ("24.1 数据从哪", "做数据分析，数据一般先从哪来？",
         "答案：先<b>有一份数据</b>——可以是硬编码的列表（练习用），也可以是读入的文件（实战用）。"),
        ("24.2 用列表和循环", "不用内置函数，自己用循环算 [80, 90, 70] 的平均分。",
         "答案：<code>total=0</code> 遍历累加得 240，再 <code>total/len(scores)</code> = 80.0。"),
        ("24.3 排序", "给成绩列表排序，用内置的什么方法 / 函数？",
         "答案：原地排用 <code>scores.sort()</code>，不改动原列表拿新列表用 <code>sorted(scores)</code>。"),
        ("24.4 画一张柱状图", "用纯文本画柱状图，每行怎么表示一个人？",
         "答案：打印 <code>名字 + \" \" + \"*\" * 次数</code>。星号个数代表数值高低，永远能跑。"),
        ("24.5 完整代码", "这份数据分析代码怎么运行？",
         "答案：保存为 <code>analyze.py</code>，终端运行 <code>python analyze.py</code> 看统计结果和图表。"),
    ],
    "src/projects/algorithm-arena.md": [
        ("25.1 擂台规则", "在算法擂台里，每道小题建议写清哪几部分？",
         "答案：① <b>题干</b>；② <b>思路讲解</b>；③ <b>可运行参考解</b>；④ <b>复杂度</b>。像竞赛题解一样完整。"),
        ("25.2 Problem 1", "“有序数组里找目标”这道，该用什么算法？",
         "答案：<b>二分查找</b>。因为数组有序，每次砍半，O(log n) 比线性快。"),
        ("25.3 Problem 2", "“乱序数组去重后再排序”，正确步骤是？",
         "答案：先用 <code>set()</code> <b>去重</b>，再用 <code>sorted()</code> <b>排序</b>。顺序不能反（排序不保证去重）。"),
        ("25.4 Problem 3", "“爬楼梯方法数”这道，用什么思路解？",
         "答案：<b>递归</b>（f(n)=f(n-1)+f(n-2)）或<b>动态规划</b>优化，避免重复计算。"),
        ("25.5 总结", "USACO Bronze 级别到底主要考什么？",
         "答案：考<b>模拟 + 贪心 + 基础搜索/排序</b>。代码量不大，但要想清楚“状态怎么变”。"),
    ],
    "src/projects/next-steps.md": [
        ("26.1 你已经拥有", "学完本书，盘点一下你已经掌握了什么？",
         "答案：变量/循环/函数/数据结构，外加<b>计算思维与基础算法</b>（搜索、排序、递归、贪心）。这是后续路线的地基。"),
        ("26.2 路线 A", "路线 A“算法竞赛”指的是什么？",
         "答案：指参加 <b>USACO</b> 等信息学竞赛，用本书的算法基础继续刷题干到 Silver/Gold。"),
        ("26.3 路线 B", "路线 B“AI / 机器学习”需要什么基础？",
         "答案：扎实的 <b>Python + 数学 + 数据结构与算法</b>，再加机器学习框架（如 PyTorch）。"),
        ("26.4 路线 C", "路线 C“Web 开发”大致做些什么？",
         "答案：做<b>网站</b>——前端（页面）和后端（服务器/数据库），Python 可用 Django / FastAPI 写后端。"),
        ("26.6 Git 入门", "Git 的三次“存档”动作，对应哪三条常用命令？",
         "答案：<code>git add</code>（暂存）→ <code>git commit</code>（存档）→ <code>git push</code>（推到远程如 GitHub）。"),
    ],
}

CARD_TMPL = """<div class="try-it">
<strong>🧩 练一练 {num}</strong>
<p>题目：{prompt}</p>
<details><summary>💡 看看答案</summary>
<p>{answer}</p>
</details>
</div>"""

BAD = 0
for path, cards in DATA.items():
    lines = open(path, encoding="utf-8").read().split("\n")
    out = list(lines)
    pos = 0
    ok = True
    for (anchor, prompt, answer) in cards:
        idx = None
        for i in range(pos, len(out)):
            head = out[i].lstrip("#").strip()
            if head.startswith(anchor) or out[i].strip().startswith(anchor):
                idx = i
                break
        if idx is None:
            print(f"❌ 锚点未找到 [{path}]: {anchor!r}")
            ok = False
            break
        # chapter number: derive from first heading number in anchor (e.g. "2.1 ...")
        ch = anchor.split()[0].split(".")[0]
        # card numbering within chapter = position
        sub = cards.index((anchor, prompt, answer)) + 1
        num = f"{ch}.{sub}"
        card = CARD_TMPL.format(num=num, prompt=prompt, answer=answer)
        out.insert(idx + 1, "")
        out.insert(idx + 2, card)
        pos = idx + 2
    if not ok:
        BAD += 1
        print(f"   → 跳过写入 {path}（保持原样）")
        continue
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"✅ 已插入 {len(cards)} 个练一练：{path}")

print(f"\n完成。失败文件数：{BAD}")
