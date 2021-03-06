# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用，除了可变参数无法和命名关键字参数混合。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数。
# 比如定义一个函数，包含上述若干种参数：

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


print(f1(1, 2))
# a = 1 b = 2 c = 0 args = () kw = {}
print(f1(1, 2, c=3))
# a = 1 b = 2 c = 3 args = () kw = {}
print(f1(1, 2, 3, 'a'))

print(f1(1, 2, 3, 'a', 'b'))
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
print(f1(1, 2, 3, 'a', 'b', x=99))
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
print(f2(1, 2, d=99, e=88, ext=None))
# a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}

# 所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。