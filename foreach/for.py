# 在这一程序中，我们打印了一序列的数字。我们通过内置的 range 函数生成这一数字序列。
# 在这里我们所要做的事情是提供两个数字，而 range 将会返回一序列的数字，从第一个数字
# 开始，至第二个数字结束。举个例子， range(1,5) 将输出序列 [1, 2, 3, 4] 。在默认情况
# 下， range 将会以 1 逐步递增。如果我们向 range 提供第三个数字，则这个数字将成为逐
# 步递增的加数。同样举个例子来说明， range(1,5,2) 将会输出 [1, 3] 。要记住这一序列扩
# 展直到第二个数字，也就是说，它不会包括第二个数字在内。
# 另外需要注意的是， range() 每次只会生成一个数字，如果你希望获得完整的数字列表，要
# 在使用 range() 时调用 list() 。例如下面这样： list(range(5)) ，它将会返回 [0, 1, 2,3, 4]


def foreach():
    for i in range(1, 5):
        print(i)
    else:
        print('The for loop is over')


def foreach1():
    for i in range(1, 5, 2):
        print(i)
    else:
        print('The for loop is over')


if __name__ == '__main__':
    foreach()
    foreach1()
