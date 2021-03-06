# 局部变量:
# 当你在一个函数的定义中声明变量时，它们不会以任何方式与身处函数之外但具有相同名称
# 的变量产生关系，也就是说，这些变量名只存在于函数这一局部（Local）。这被称为变量的
# 作用域（Scope）。所有变量的作用域是它们被定义的块，从定义它们的名字的定义点开始。

x = 50


def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)


func(x)
print('x is still', x)


# 输出：
# $ python function_local.py
# x is 50
# Changed local x to 2
# x is still 50
# 它是如何工作的
# 当我们第一次打印出存在于函数块的第一行的名为 x 的值时，Python 使用的是在函数声明
# 之上的主代码块中声明的这一参数的值。
# 接着，我们将值 2 赋值给 x 。 x 是我们这一函数的局部变量。因此，当我们改变函数中
# x 的值的时候，主代码块中的 x 则不会受到影响。
# 随着最后一句 print 语句，我们展示出主代码块中定义的 x 的值，由此确认它实际上不受
# 先前调用的函数中的局部变量的影响。
