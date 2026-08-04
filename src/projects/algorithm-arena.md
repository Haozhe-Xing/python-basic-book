<div style="display:flex; gap:12px; margin-bottom:24px; flex-wrap:wrap; align-items:center;">
  <span style="background:#f0f4ff; color:#4A6CF7; padding:4px 12px; border-radius:20px; font-size:0.85em; font-weight:600; border:1px solid rgba(74,108,247,0.2);">📖 第25章</span>
  <span style="background:#fef9ec; color:#d97706; padding:4px 12px; border-radius:20px; font-size:0.85em; font-weight:600; border:1px solid rgba(245,158,11,0.2);">⏱️ ~45 min read</span>
  <span style="background:#fef2f2; color:#ef4444; padding:4px 12px; border-radius:20px; font-size:0.85em; font-weight:600; border:1px solid rgba(239,68,68,0.2);">🎯 Advanced</span>
</div>

# Chapter 25: 项目三 · 算法挑战擂台（USACO Bronze 风格）

> 📝 **Before You Continue:** 本章是"算法启蒙篇"的实战收口，假定你已见过：
> - [第17章 大 O 与复杂度](../algorithms/big-o.md) —— 衡量算法快慢的尺子
> - [第18章 查找算法](../algorithms/searching.md) —— 本题一"找目标"的来路
> - [第19章 排序算法](../algorithms/sorting.md) —— 本题二"排序"的来路
> - [第20章 递归与分治](../algorithms/recursion-divide.md) —— 本题三"递归"的来路
> - [第21章 基础数据结构](../algorithms/basic-structures.md) —— `set`/`list` 等工具箱
> - [第22章 贪心与模拟](../algorithms/greedy-simulation.md) —— "按规则一步步推"的思维

前面两章你做出了能跑的小作品。这一章换个味道：**上擂台做题**。USACO（美国计算机奥赛）的 Bronze 组，考的就是"把题目描述翻译成正确、不太慢的代码"。它不要求你背高级算法，但要求你**想清楚、写对、不超时**。

本章三道题，全是 Bronze 常客：① 有序数组里找目标（二分查找）；② 乱序去重后排序；③ 递归算爬楼梯方法数。每题我都给**题干 → 思路 → 可运行参考解 → 复杂度**，并把"为什么快/慢"讲透。

<div class="story-scene">
<strong>🎬 开场小剧场：算法擂台开赛</strong>
<p>游乐场中央升起一座擂台，屏幕上出现三道挑战题。小派看见题干就想直接写代码，擂台裁判 arena 立刻吹哨：“先读题！输入是什么？输出是什么？数据有多大？”</p>
<p>裁判指着计时器说：“Bronze 不考花哨魔法，考的是把题意翻译成正确代码，还不能太慢。”这章就是把前面的搜索、排序、递归拉到实战场上。</p>
</div>

<div class="quest-card">
<strong>🎯 本章任务卡</strong>
<ul>
<li>按“题干 → 思路 → 代码 → 复杂度”拆竞赛题。</li>
<li>用二分查找解决有序数组找目标。</li>
<li>用集合和排序处理去重排序。</li>
<li>用递归、记忆化和 DP 解决爬楼梯。</li>
<li>养成先写对、再优化的竞赛节奏。</li>
</ul>
</div>

<div class="boss-bug">
<strong>👾 本章 Boss Bug：读题跳步怪</strong>
<p>它会催你没看清输入输出就开始敲代码。打败它的流程是：圈出数据、写样例、说出朴素解，再决定要不要优化。</p>
</div>

---

## 25.1 ⚔️ 擂台规则

<div class="try-it">
<strong>🧩 练一练 25.1</strong>
<p>题目：在算法擂台里，每道小题建议写清哪几部分？</p>
<details><summary>💡 看看答案</summary>
<p>答案：① <b>题干</b>；② <b>思路讲解</b>；③ <b>可运行参考解</b>；④ <b>复杂度</b>。像竞赛题解一样完整。</p>
</details>
</div>

- **输入即给定**：题干会给数组/数字，我们直接用变量接住，专注"处理逻辑"。
- **要的是"对 + 不太慢"**：Bronze 的数据量一般 ≤ 10⁵，所以 O(n²) 往往危险、O(n log n) 或 O(n) 才稳。
- **先写对的，再想快的**：能跑出正确答案最重要；复杂度是"进阶分"。

> 💡 **Key Insight:** 竞赛和平时项目一样——**先有正确版本，再优化**。很多人卡在"一上来就想最优解"，结果写错还调试不动。本题三的解法演进（递归→记忆化→DP）完美演示这条路。

![算法擂台流程：读题 → 想思路 → 写解 → 算复杂度](../images/proj-arena.svg)

上图是做每道题的固定流程：先读懂输入输出，再想"用什么数据结构/套路"，写出可运行解，最后用 [第17章 大 O](../algorithms/big-o.md) 估一下快慢。

---

## 25.2 Problem 1 · 有序数组里找目标（二分查找）

<div class="try-it">
<strong>🧩 练一练 25.2</strong>
<p>题目：“有序数组里找目标”这道，该用什么算法？</p>
<details><summary>💡 看看答案</summary>
<p>答案：<b>二分查找</b>。因为数组有序，每次砍半，O(log n) 比线性快。</p>
</details>
</div>

### 题干
给定一个**已从小到大排序**的整数数组 `arr` 和一个目标值 `target`，如果 `target` 在数组里，返回它的**下标**；不在则返回 `-1`。
示例：`arr = [2,5,8,12,16,23,38,56,72,91]`，`target = 23` → 返回 `5`（23 在下标 5）。

### 思路讲解
最笨的办法：从头到尾一个个比（`for` 扫一遍），这叫**线性查找**，最坏要比 n 次。但数组是**排好序**的——这是关键线索！既然有序，我们可以用**二分查找**：每次看"中间的那个数"，它比目标大就往左半边找，比目标小就往右半边找，每次直接**砍掉一半**。

> 🧠 **Mental Model: 猜数字游戏** 朋友心里想一个 1–100 的数，你猜 50：他说"大了"，你就知道答案在 1–49，一半直接排除。二分查找就是把这套"每次砍一半"自动化。

### 可运行参考解

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1     # 当前搜索区间 [left, right]
    while left <= right:
        mid = (left + right) // 2     # 中点（整除）
        if arr[mid] == target:
            return mid                 # 找到了，返回下标
        elif arr[mid] < target:
            left = mid + 1             # 目标在右半边
        else:
            right = mid - 1            # 目标在左半边
    return -1                          # 区间空了还没找到

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(binary_search(arr, 23))   # 5
print(binary_search(arr, 100))  # -1
print(binary_search(arr, 2))    # 0
```

> 🐛 **Common Bug:** 循环条件写成 `while left < right:` 会**漏掉**只剩一个元素的情况（此时 `left == right`，应再比一次）。正确是 `left <= right`。另一个坑：更新写成 `left = mid` / `right = mid`，可能导致死循环——必须 `mid ± 1` 跳过已比过的 `mid`。

### 🧮 算法小课堂：复杂度

- **时间**：每轮把区间砍半，砍 k 次后区间长度变成 `n / 2^k`。当 `n / 2^k ≈ 1` 即 `k ≈ log₂ n` 时结束。所以 **O(log n)**——10 万个元素也只要比约 17 次！
- **空间**：只用了几个变量，**O(1)**。
- 对比线性查找 O(n)：n=10⁵ 时，线性要 10 万次，二分只要 17 次。这就是"利用有序性"的红利。

> ⚡ **Pro Tip:** Python 其实内置 `bisect` 模块能直接做二分。但竞赛练习时**自己写一遍**才真正理解；考试允许用库时再偷懒。

---

## 25.3 Problem 2 · 乱序去重后排序

<div class="try-it">
<strong>🧩 练一练 25.3</strong>
<p>题目：“乱序数组去重后再排序”，正确步骤是？</p>
<details><summary>💡 看看答案</summary>
<p>答案：先用 <code>set()</code> <b>去重</b>，再用 <code>sorted()</code> <b>排序</b>。顺序不能反（排序不保证去重）。</p>
</details>
</div>

### 题干
给定一个可能含重复元素的整数数组 `nums`，请返回**去重后、从小到大排序**的结果。
示例：`nums = [5,3,9,3,5,1,9,7,1]` → 返回 `[1,3,5,7,9]`。

### 思路讲解
两件事："去重"和"排序"。去重最自然的工具是 **`set`（集合）**——集合天生不允许重复，把列表丢进 `set` 自动去重；再 `sorted()` 排个序即可。一行就能写完：`sorted(set(nums))`。

但为了理解，我们也写"显式版"：建一个空集合，遍历数组把每个数 `add` 进去，最后排序。

> 🤔 **Why 用 set 而不是嵌套循环去重？** 嵌套循环（每数比一遍是否出现过）是 O(n²)；用 `set` 的 `add` 平均 O(1)，整体降到 O(n)。这是 [第21章 基础数据结构](../algorithms/basic-structures.md) 里"选对结构省时间"的典型例子。

### 可运行参考解

```python
def dedupe_and_sort(nums):
    seen = set()            # 集合：自动去重
    for x in nums:
        seen.add(x)
    return sorted(seen)     # sorted 返回排好序的新列表

nums = [5, 3, 9, 3, 5, 1, 9, 7, 1]
print(dedupe_and_sort(nums))        # [1, 3, 5, 7, 9]
print(sorted(set(nums)))            # 一行版，结果相同
```

### 🧮 算法小课堂：复杂度

- **时间**：遍历 `nums` 是 O(n)；`sorted` 在 Python 里是 Timsort，约 **O(n log n)**。总体 **O(n log n)**。
- **空间**：`set` 和排序结果都额外占 O(n) 空间。
- 注意：如果"先排序再去重"（排序 O(n log n)，再去重扫一遍 O(n)），总时间仍是 O(n log n)，也是对的——两条路都达标，看你怎么顺手。

> 📝 **Note:** `set` 不保证顺序，所以去重后**必须**再 `sorted` 才满足"从小到大"的要求。直接 `list(set(nums))` 得到的是乱序，会答错。

---

## 25.4 Problem 3 · 爬楼梯方法数（递归 + 优化）

<div class="try-it">
<strong>🧩 练一练 25.4</strong>
<p>题目：“爬楼梯方法数”这道，用什么思路解？</p>
<details><summary>💡 看看答案</summary>
<p>答案：<b>递归</b>（f(n)=f(n-1)+f(n-2)）或<b>动态规划</b>优化，避免重复计算。</p>
</details>
</div>

### 题干
你每次可以跨 **1 级** 或 **2 级** 台阶。问：爬到第 `n` 级台阶，一共有多少种**不同的方法**？
示例：`n = 3` → 方法数 `3`（`1+1+1`、`1+2`、`2+1`）；`n = 4` → `5` 种。

### 思路讲解（递归）
到第 `n` 级，最后一步要么是"从 n-1 跨 1 级"，要么是"从 n-2 跨 2 级"。所以：

```
爬到第 n 级的方法数 = 爬到 n-1 的方法数 + 爬到 n-2 的方法数
```

这就是著名的**斐波那契**关系。边界：`n=0`（地面，算 1 种"不动"）和 `n=1`（只有 1 种）都返回 1。

### 可运行参考解（三档：从对到快）

```python
# ① 纯递归：好懂，但慢
def climb_rec(n):
    if n == 0 or n == 1:
        return 1
    return climb_rec(n - 1) + climb_rec(n - 2)

# ② 记忆化：用 lru_cache 缓存算过的值，避免重复算
from functools import lru_cache
@lru_cache(maxsize=None)
def climb_memo(n):
    if n == 0 or n == 1:
        return 1
    return climb_memo(n - 1) + climb_memo(n - 2)

# ③ 动态规划（DP）：从底向上推，只用两个变量，最快最省内存
def climb_dp(n):
    if n == 0 or n == 1:
        return 1
    a, b = 1, 1            # 分别代表 dp[0], dp[1]
    for _ in range(2, n + 1):
        a, b = b, a + b    # 滚动更新：新 b = 前两项之和
    return b

for n in [1, 2, 3, 4, 5, 10]:
    print(n, climb_rec(n), climb_memo(n), climb_dp(n))   # 三档结果一致
print("n=40:", climb_dp(40))   # 165580141，瞬间出
```

> 💡 **Key Insight:** ① 纯递归对 `n=40` 会卡很久（甚至算不出），因为它把同一子问题算了成千上万遍；② 记忆化给它"记小本本"立刻起飞；③ DP 连递归都不要，从下往上滚，空间也从 O(n) 降到 O(1)。**三档结果完全一样，差别只在快慢**——这正是 [第20章 递归与分治](../algorithms/recursion-divide.md) 的核心课。

> 🐛 **Common Bug:** 边界写错：`climb(2)` 若只判 `n==1` 返回 1，会递归到 `climb(0)` 没定义而报错。务必把 `n==0` 也当成返回 1 的边界（它表示"已经在地面、作为一种起点"）。

### 🧮 算法小课堂：复杂度

| 版本 | 时间 | 空间 | 说明 |
|------|------|------|------|
| ① 纯递归 | **O(2ⁿ)** | O(n) 调用栈 | 指数级，n 大了崩溃 |
| ② 记忆化 | O(n) | O(n) | 每个子问题算一次 |
| ③ DP | O(n) | **O(1)** | 滚动变量，最快最省 |

> ⚠️ **Warning:** Bronze 题目里 `n` 可能到 10⁵ 甚至更大。**纯递归的绝对不要用**——O(2ⁿ) 在 n=40 就已超过 1 万亿次运算。看到"方法数/方案数 + 可拆成子问题"，立刻想到记忆化或 DP。

---

## 25.5 总结：Bronze 到底考什么

<div class="try-it">
<strong>🧩 练一练 25.5</strong>
<p>题目：USACO Bronze 级别到底主要考什么？</p>
<details><summary>💡 看看答案</summary>
<p>答案：考<b>模拟 + 贪心 + 基础搜索/排序</b>。代码量不大，但要想清楚“状态怎么变”。</p>
</details>
</div>

把三题放一起看，Bronze 的套路很清楚：

1. **利用数据的"序"或"结构"**（题一的有序 → 二分；题二的集合去重）。
2. **把大问题拆成相同的子问题**（题三的递归 / DP）。
3. **永远关心复杂度**：能跑对只是及格，O(n²) 常在大数据下超时，要想 O(n log n) 或 O(n)。

> 🔍 **计算思维聚焦：模式识别 + 抽象** 做题时你在做两件事：① **模式识别**——"这题是不是二分？是不是 DP？"把新题套进见过的套路；② **抽象**——忽略具体数字，抓住"输入→输出→约束"的骨架。这两件事，比背代码值钱得多。

---

## 🏅 本章通关徽章：算法擂台选手

<div class="badge-card">
<strong>如果你能做到下面 4 件事，就获得“算法擂台选手”徽章：</strong>
<ul>
<li>能把题干拆成输入、输出和约束。</li>
<li>能写出至少一种正确解法。</li>
<li>能用复杂度判断解法是否可能超时。</li>
<li>能从朴素解一步步升级到更快解。</li>
</ul>
</div>

---

## ⚠️ Common Mistakes in Chapter 25

| # | 误区 | 示例 | 为什么错 | 修正 |
|---|------|------|---------|------|
| 1 | 二分写 `while left < right` | 单元素区间被跳过，漏解 | 应允许 `left == right` 再比一次 | 改成 `while left <= right` |
| 2 | 二分更新用 `mid` 不 ±1 | 可能死循环（区间不收缩） | 已比过 `mid` 必须排除 | `left = mid + 1` / `right = mid - 1` |
| 3 | 去重后忘了排序 | `list(set(nums))` 是乱序 | 题干要求"从小到大" | 套一层 `sorted(...)` |
| 4 | 爬楼梯用纯递归解大 n | n=40 卡死/超时 | 指数级 O(2ⁿ) | 用 `@lru_cache` 或 DP |
| 5 | 递归边界漏 `n==0` | `climb(2)` 调到 `climb(0)` 报错 | 没把地面当合法起点 | 边界写 `if n==0 or n==1: return 1` |

---

## Chapter Summary

### 📌 Key Takeaways

| 题 | 套路 | 复杂度 | 关键提醒 |
|----|------|--------|---------|
| ① 二分查找 | 利用"有序"，每次砍半 | 时间 O(log n)，空间 O(1) | `left<=right` 且 `mid±1` |
| ② 去重排序 | `set` 去重 + `sorted` | 时间 O(n log n)，空间 O(n) | 去重后必须再排序 |
| ③ 爬楼梯 | 递归/记忆化/DP（斐波那契） | 纯递归 O(2ⁿ) → DP O(n) | 大 n 禁用纯递归 |

### ❓ FAQ

**Q1: 二分查找必须数组有序吗？**
> A: 必须。无序时"中间比目标大"不能推出"目标在左半边"，二分的前提直接崩塌。若无序，先 `sorted`（O(n log n)）再二分，或干脆线性查找。

**Q2: `set` 去重后顺序乱了，怎么保持"原顺序去重"？**
> A: 用 `dict.fromkeys(nums)`（Python 3.7+ 字典保插入序）或列表推导：`seen=set(); [seen.add(x) or x for x in nums if x not in seen]`。但本题只要"排序后"，所以 `sorted(set(nums))` 最简。

**Q3: 爬楼梯的 DP 为什么 `a, b = b, a+b` 是对的不是错乱的？**
> A: 这是"同时赋值"：右边先用旧 `a,b` 算出新值，再一次性赋给左边。等价于 `new_b = a+b; new_a = b`，正确滚动斐波那契。若分开写 `a=b; b=a+b` 就错（第二行用了刚改的 a）。

### 🔗 Connections to Later Chapters

- **[第22章 贪心与模拟](../algorithms/greedy-simulation.md)** 是 Bronze 另一大常客——"按局部最优一步步推"，和本题"拆子问题"互补。
- **[第26章 下一步去哪？](next-steps.md)** 的 **USACO 路线**会告诉你：刷完 Bronze 套路，下一步是 Silver（堆/二分答案/前缀和），本章就是地基。
- **AI/ML 路线**里，递归与 DP 的思想也会以"动态规划/序列模型"的形式再次出现。

---


## 🎮 加练任务包

> 下面这些题目不一定比章末题更难，但更适合“多刷几遍、把手感练出来”。建议先独立做，再展开提示。

### 加练 25.A · 读题三问 🟢

看到一道竞赛题，动手写代码前先问哪三个问题？

<details>
<summary>💡 提示 / 答案要点</summary>

输入是什么？输出是什么？数据范围多大？这三问决定代码结构和复杂度要求。

</details>

---

### 加练 25.B · 样例自测 🟢

为什么自己要再造 2-3 个小样例？

<details>
<summary>💡 提示 / 答案要点</summary>

样例能暴露边界问题，如空列表、目标不存在、最小输入、重复元素等。

</details>

---

### 加练 25.C · 从慢到快 🟡

如果 O(n²) 会超时，下一步应该怎么想？

<details>
<summary>💡 提示 / 答案要点</summary>

先找是否能排序、用集合/字典、二分、前缀和或减少重复计算。目标是把重复工作删掉。

</details>

---


---

## Practice Problems

⚔️ **挑战擂台：** 下面每题都按"题干 → 自己先想 → 点开看解"的擂台节奏来。

---

**Problem 25.1 — 二分查找的"第一次出现"** 🟡 Medium

数组可能含重复元素且已排序，如 `[1,2,2,2,3,4]`，目标 `2`。请返回目标**第一次出现**的下标（这里是 `1`），不存在返回 `-1`。提示：找到后别急着返回，继续往左半边找更小的下标。

<details>
<summary>💡 Solution (click to reveal)</summary>

**Approach:** 标准二分，但命中时不立即返回，而是记录答案并继续向左（`right = mid - 1`）。

```python
def first_pos(arr, target):
    left, right = 0, len(arr) - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            ans = mid
            right = mid - 1      # 可能左边还有更早的
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return ans

print(first_pos([1,2,2,2,3,4], 2))   # 1
```

**Key points:**
- 用 `ans` 暂存"目前为止最左的命中"。
- 复杂度仍是 O(log n)。

</details>

---

**Problem 25.2 — 统计"出现次数"** 🟡 Medium

接上题，返回目标在有序数组里的**出现次数**（如 `[1,2,2,2,3,4]` 中 `2` 出现 `3` 次）。要求比"线性数一遍"更快。

<details>
<summary>💡 Solution (click to reveal)</summary>

**Approach:** 用上题的"首次出现"和对称的"末次出现"下标相减 +1。

```python
def last_pos(arr, target):
    left, right = 0, len(arr) - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            ans = mid
            left = mid + 1       # 继续向右找更晚的
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return ans

def count(arr, target):
    a, b = first_pos(arr, target), last_pos(arr, target)
    return b - a + 1 if a != -1 else 0

print(count([1,2,2,2,3,4], 2))   # 3
```

**Key points:**
- 两次二分都是 O(log n)，整体远快于线性扫描。
- 这是二分"变形题"的通用套路：把"找值"改成"找边界"。

</details>

---

**Problem 25.3 — 爬楼梯升级：一次可跨 1/2/3 级** 🔴 Hard

若每次可跨 1、2 或 3 级，爬到第 `n` 级有多少种方法？写出 DP 解法，并说清状态转移。

<details>
<summary>💡 Solution (click to reveal)</summary>

**Approach:** 到第 n 级，最后一步来自 n-1 / n-2 / n-3，故 `dp[n] = dp[n-1]+dp[n-2]+dp[n-3]`。

```python
def climb3(n):
    if n == 0: return 1
    if n == 1: return 1
    if n == 2: return 2          # 1+1, 2
    dp = [0] * (n + 1)
    dp[0], dp[1], dp[2] = 1, 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n]

for n in range(1, 8):
    print(n, climb3(n))          # 1,1,2,4,7,13,24...
```

**Key points:**
- 状态转移从"两项和"变成"三项和"，思想完全一样。
- 用数组 `dp` 自底向上，O(n) 时间、O(n) 空间；也可滚动三个变量压到 O(1)。

</details>

---

**Problem 25.4 — 自己命题并解出** 🏆 Challenge

模仿题二，设计一个"给定字符串列表，返回**去重后按长度排序**的单词列表"的函数（长度相同按字典序）。写出代码并用 `["banana","apple","pear","apple","kiwi","pear"]` 验证。

<details>
<summary>💡 Solution (click to reveal)</summary>

**Approach:** `set` 去重后，`sorted` 用 `key` 指定"先按长度、再按字典序"。

```python
def unique_by_len(words):
    uniq = list(set(words))
    return sorted(uniq, key=lambda w: (len(w), w))

words = ["banana","apple","pear","apple","kiwi","pear"]
print(unique_by_len(words))
# ['pear', 'kiwi', 'apple', 'banana']  (长度 4,4,5,6；同长度按字母)
```

**Key points:**
- `key=lambda w: (len(w), w)` 是"多关键字排序"：先比长度，相等再比字符串本身。
- 这把题二的"去重+排序"套到了字符串上，证明套路可迁移。

</details>

---

> 💡 **记住这一句：** 竞赛不是比谁代码长，而是比谁先把"对的解"想清楚、再把"慢的解"换成"快的解"——二分、集合、DP，就是你武器库里的前三件。
