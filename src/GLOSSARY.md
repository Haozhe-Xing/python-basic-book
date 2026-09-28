# 术语表（Glossary）

> 术语按中文名称的拼音首字母分组。每条给出英文名称、最短解释和首次重点学习位置，忘记时可以随时回来查。

---

## B

**变量（Variable）** — 给数据起的名字；重新赋值时，名字会指向新的值。首次重点：[第 2 章](foundations/variables.md)。

**编程（Programming）** — 把解决问题的步骤写成计算机可以执行的指令。

**编码（Encoding）** — 文本与字节之间的转换规则。读写中文文件时通常明确使用 UTF-8。首次重点：[Chapter 16B](functions/files-data.md)。

## C

**参数（Parameter）** — 定义函数时用来接收数据的名字；调用函数时传入的具体数据叫实参。首次重点：[第 14 章](functions/functions-intro.md)。

**测试（Test）** — 用代码自动检查实际结果是否符合预期。首次重点：[Chapter 16C](functions/testing-types.md)。

**抽象（Abstraction）** — 保留问题的关键特征、隐藏暂时无关的细节，用更简单的模型思考复杂问题。

**常量（Constant）** — 按约定不应修改的值。Python 通常用全大写名字表示，例如 `MAX_SCORE = 100`，但语言本身不会禁止重新赋值。

## D

**代码（Code）** — 用编程语言写成的、可以被解释器执行的指令文本。

**递归（Recursion）** — 函数直接或间接调用自己，并不断接近停止条件的解题方式。首次重点：[第 15 章](functions/scope-recursion.md)。

**迭代（Iteration）** — 重复执行步骤的过程；`for` 和 `while` 都能实现迭代。

## F

**函数（Function）** — 一段有名字、可以重复调用的代码；可以接收参数并返回结果。首次重点：[第 14 章](functions/functions-intro.md)。

## H

**哈希 / 可哈希（Hash / Hashable）** — Python 用来快速定位集合元素和字典键的机制。可哈希对象的哈希值在生命周期内保持稳定，因此列表不能作为字典键。首次重点：[第 12 章](data-structures/dictionaries.md)。

## J

**集合（Set）** — 保存不重复元素的数据结构，适合去重和集合运算。首次重点：[第 11 章](data-structures/tuples-sets.md)。

**解释器（Interpreter）** — 读取 Python 代码并执行相应操作的程序。你运行 `.py` 文件时，就是把它交给 Python 解释器。

**计算思维（Computational Thinking）** — 把大问题拆小、发现规律、建立模型、设计步骤并验证结果的思考方式。

## K

**可变对象（Mutable Object）** — 创建后可以在原对象上改变内容的对象，例如列表和字典。

**不可变对象（Immutable Object）** — 创建后不能修改其内部值的对象，例如整数、字符串和只包含可哈希元素的元组。

## L

**列表（List）** — 有顺序、可修改、允许重复元素的数据结构。首次重点：[第 10 章](data-structures/lists.md)。

**路径（Path）** — 文件或文件夹在文件系统中的地址；可以用 `pathlib.Path` 安全表示和拼接。首次重点：[Chapter 16B](functions/files-data.md)。

## M

**模块（Module）** — 一个可被导入的 Python 文件。把相关函数放进独立 `.py` 文件，可以在其他程序中复用。首次重点：[第 16 章](functions/modules.md)。

## S

**算法（Algorithm）** — 解决某类问题的一组明确、有限步骤。首次重点：[第 17 章](algorithms/big-o.md)。

**数据结构（Data Structure）** — 组织和访问数据的方式，例如列表、字典、集合、栈和队列。

## T

**调试（Debugging）** — 复现问题、观察现象、定位原因、修改并重新验证的过程。首次重点：[第 9 章](control-flow/debugging.md)。

**类型提示（Type Hint）** — 写在函数参数和返回值旁的类型说明，例如 `name: str`、`-> int`；它帮助阅读和检查代码，但通常不会自动阻止错误运行。首次重点：[Chapter 16C](functions/testing-types.md)。

## X

**虚拟环境（Virtual Environment）** — 为一个项目隔离 Python 与第三方依赖的目录，避免不同项目互相影响。首次重点：[第 0 章](getting-started/install.md)。

## Y

**异常（Exception）** — 程序运行时遇到无法按原计划处理的问题，例如 `ValueError`、`FileNotFoundError`。首次重点：[Chapter 16A](functions/exceptions.md)。

## Z

**字典（Dictionary / dict）** — 用“键 → 值”关系保存数据的数据结构，适合按名字快速查找内容。首次重点：[第 12 章](data-structures/dictionaries.md)。

**终端 / 命令行（Terminal / Shell）** — 通过文字命令运行程序和操作文件的窗口，例如 Windows PowerShell 或 macOS 终端。

**作用域（Scope）** — 一个名字可以被访问的代码范围，例如函数内部的局部作用域。首次重点：[第 15 章](functions/scope-recursion.md)。

## 英文缩写

**CSV（Comma-Separated Values）** — 用行和列保存表格数据的文本格式；应使用标准库 `csv` 处理引号、逗号和换行。首次重点：[Chapter 16B](functions/files-data.md)。

**IDE（Integrated Development Environment）** — 集成代码编辑、运行、调试和提示功能的软件，例如 VS Code。

**JSON（JavaScript Object Notation）** — 常用于保存和交换列表、字典、字符串、数字等结构化数据的文本格式。首次重点：[Chapter 16B](functions/files-data.md)。

**PATH（环境变量）** — 操作系统查找可执行程序时使用的路径列表。安装 Python 后，终端需要能通过 PATH 找到解释器。

**Python** — 本书使用的编程语言，强调代码可读性并拥有丰富的标准库与第三方生态。
