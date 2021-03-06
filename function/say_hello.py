# 函数（Functions）是指可重复使用的程序片段。它们允许你为某个代码块赋予名字，允许你
# 通过这一特殊的名字在你的程序任何地方来运行代码块，并可重复任何次数。这就是所谓的
# 调用（Calling）函数。我们已经使用过了许多内置的函数，例如 len 和 range 。
# 函数概念可能是在任何复杂的软件（无论使用的是何种编程语言）中最重要的构建块，所以
# 我们接下来将在本章中探讨有关函数的各个方面。
# 函数可以通过关键字 def 来定义。这一关键字后跟一个函数的标识符名称，再跟一对圆括
# 号，其中可以包括一些变量的名称，再以冒号结尾，结束这一行。随后而来的语句块是函数
# 的一部分。下面的案例将会展示出这其实非常简单：

def say_hello():
    # 该块属于这一函数
    print('hello world')


# 函数结束
say_hello()  # 调用函数
say_hello()  # 再次调用函数
