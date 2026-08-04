<div style="display:flex; gap:12px; margin-bottom:24px; flex-wrap:wrap; align-items:center;">
  <span style="background:#f0f4ff; color:#4A6CF7; padding:4px 12px; border-radius:20px; font-size:0.85em; font-weight:600; border:1px solid rgba(74,108,247,0.2);">📖 附录 C</span>
  <span style="background:#f0fdf4; color:#16a34a; padding:4px 12px; border-radius:20px; font-size:0.85em; border:1px solid rgba(22,163,74,0.2);">⏱️ ~15 min read</span>
  <span style="background:#fef9ec; color:#d97706; padding:4px 12px; border-radius:20px; font-size:0.85em; border:1px solid rgba(100,100,100,0.15);">🎯 Intermediate</span>
</div>

# 附录 C：Python 之禅（中英对照 + 少年版解读）

> Python 的作者 Guido van Rossum（龟叔）之外，另一位大佬 Tim Peters 把"写好 Python 的 19 条心法"写进了一段隐藏彩蛋里。

## 怎么看这段"禅"

在你装好的 Python 里（终端敲 `python` 或 `python3` 进入 `>>>`），输入：

```python
import this
```

屏幕就会打印出下面这 19 句话。它们不只是"文艺句子"，更是**贯穿全书的编程价值观**——很多章的"为什么这样写更好"，背后都是这 19 条在撑腰。

> 💡 **Key Insight:** 这 19 条不用背，但建议你每学几章就回来读一遍。你会发现：原来书里教你的"拆函数、写清楚、少嵌套"，早被前辈总结成"禅"了。

---

## 十九条，逐条解读

| # | 英文 | 中文 | 少年版白话解读 | 对应章节 |
|---|------|------|----------------|----------|
| 1 | Beautiful is better than ugly. | 优美胜于丑陋。 | 代码也是作品，写得整洁漂亮比乱糟糟强。 | 第 14 章（函数封装让代码变美） |
| 2 | Explicit is better than implicit. | 明了胜于隐晦。 | 把意图写明白，别让人猜。 | 第 14 章（函数参数、返回值要明确） |
| 3 | Simple is better than complex. | 简洁胜于复杂。 | 能简单解决，就别绕弯子。 | 第 21 章（选对数据结构，思路更简） |
| 4 | Complex is better than complicated. | 复杂胜于凌乱。 | 真复杂时，至少要有秩序，别一团浆糊。 | 第 20 章（递归与分治，把复杂变有序） |
| 5 | Flat is better than nested. | 扁平胜于嵌套。 | 别层层套娃，能平铺就平铺。 | 第 6 章 / 第 8 章（少写深层嵌套） |
| 6 | Sparse is better than dense. | 疏朗胜于拥挤。 | 代码留点空隙、别挤一行。 | 第 9 章（可读性 = 好调试） |
| 7 | Readability counts. | 可读性很重要。 | 能让人一眼看懂，比炫技强百倍。 | 第 14 章 / 全书（命名与注释） |
| 8 | Special cases aren't special enough to break the rules. | 特殊情况不足以打破规则。 | 别为个别例外破坏整体一致性。 | 第 6 章（条件逻辑要规整） |
| 9 | Although practicality beats purity. | 尽管实用性胜过纯粹性。 | 太死板也不行，好用最重要。 | 第 22 章（贪心/模拟讲究实用） |
| 10 | Errors should never pass silently. | 错误不应被悄悄放过。 | 出错了就要让它"叫"出来。 | 第 9 章（别掩盖 bug） |
| 11 | Unless explicitly silenced. | 除非你明确让它闭嘴。 | 想忽略错误，得写清楚、有意为之。 | 第 9 章（异常处理留伏笔） |
| 12 | In the face of ambiguity, refuse the temptation to guess. | 面对歧义，拒绝猜测的诱惑。 | 看不懂就问清/查文档，别瞎蒙。 | 第 18 章（二分条件要精确） |
| 13 | There should be one— and preferably only one —obvious way to do it. | 应当只有一种、且最好只一种明显的做法。 | 好方案通常唯一且显然。 | 第 16 章（模块/标准库的惯用法） |
| 14 | Although that way may not be obvious at first unless you're Dutch. | 尽管那个做法起初并不明显（除非你是荷兰人）。 | 幽默：龟叔是荷兰人，有些"显然"对他明显。 | 第 16 章（多读标准库就懂了） |
| 15 | Now is better than never. | 现在做总比不做好。 | 别拖延，先写一版出来。 | 第 26 章（动手比空想重要） |
| 16 | Although never is often better than *right* now. | 尽管"不做"常比"立刻瞎做"好。 | 但该想清楚时别急着写，先想后码。 | 第 26 章（先设计再实现） |
| 17 | If the implementation is hard to explain, it's a bad idea. | 如果实现很难解释，那它就是个坏主意。 | 讲不清的代码，多半设计错了。 | 第 14 章 / 第 15 章（递归要讲得通） |
| 18 | If the implementation is easy to explain, it may be a good idea. | 如果实现很容易解释，那它可能是个好主意。 | 能讲明白的，通常就是好方案。 | 第 14 章（好函数一眼懂） |
| 19 | Namespaces are one honking great idea — let's do more of those! | 命名空间是个绝妙的主意，咱们多用用！ | 把名字分门别类放好，不打架。 | 第 16 章（模块 = 命名空间） |

---

## 三句最该先记住的"禅"

> 💡 **Key Insight:** 19 条里，和初学者关系最密切的是这三条——它们几乎能解释你书里看到的每一个"为什么这样写"：

1. **Readability counts（可读性很重要）** —— 你写的代码是给人看的，顺便给机器跑。命名清楚、留好空隙，将来（包括明天的你）才看得懂。
2. **Explicit is better than implicit（明了胜于隐晦）** —— 函数该传什么、返回什么，写明白；别让读代码的人去猜。
3. **Simple is better than complex（简洁胜于复杂）** —— 算法也是一样：能简单清楚的，别硬上花活。本书第五篇讲"效率"时，你会反复体会到这点。

> 📝 **Note:** 这 19 条是"价值观"，不是"语法规则"。语法错了 Python 会报错；价值观错了，代码能跑但会很难维护。两者都重要——语法靠多练，价值观靠多读、多回看这张表。
