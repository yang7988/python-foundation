# global 语句
# 如果你想给一个在程序顶层的变量赋值（也就是说它不存在于任何作用域中，无论是函数还
# 是类），那么你必须告诉 Python 这一变量并非局部的，而是全局（Global）的。我们需要通
# 过 global 语句来完成这件事。因为在不使用 global 语句的情况下，不可能为一个定义于
# 函数之外的变量赋值。
# 函数
# 60
# 你可以使用定义于函数之外的变量的值（假设函数中没有具有相同名字的变量）。然而，这
# 种方式不会受到鼓励而且应该避免，因为它对于程序的读者来说是含糊不清的，无法弄清楚
# 变量的定义究竟在哪。而通过使用 global 语句便可清楚看出这一变量是在最外边的代码块
# 中定义的。

x = 50
def func():
    global x
    print('x is', x)
    x = 2
    print('Changed global x to', x)

func()
print('Value of x is', x)

# 输出：
# $ python function_global.py
# x is 50
# Changed global x to 2
# Value of x is 2
# 它是如何工作的
# global 语句用以声明 x 是一个全局变量——因此，当我们在函数中为 x 进行赋值时，这
# 一改动将影响到我们在主代码块中使用的 x 的值。
# 你可以在同一句 global 语句中指定不止一个的全局变量，例如 global x, y, z 。