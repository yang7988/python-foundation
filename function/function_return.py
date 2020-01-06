# return 语句用于从函数中返回，也就是中断函数。我们也可以选择在中断函数时从函数中返
# 回一个值。

def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y


print(maximum(2, 3))


# 要注意到如果 return 语句没有搭配任何一个值则代表着 返回 None 。 None 在 Python 中一
# 个特殊的类型，代表着虚无。举个例子， 它用于指示一个变量没有值，如果有值则它的值便
# 是 None（虚无） 。
# 每一个函数都在其末尾隐含了一句 return None ，除非你写了你自己的 return 语句。你可
# 以运行 print(some_function()) ，其中 some_function 函数不使用 return 语句，就像这
# 样：
# def some_function():
# pass
# Python 中的 pass 语句用于指示一个没有内容的语句块。
# 提示：有一个名为 max 的内置函数已经实现了“找到最大数”这一功能，所以尽可能地使
# 用这一内置函数。
