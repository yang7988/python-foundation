import mymodule

mymodule.say_hi()
print('Version', mymodule.__version__)


# 它是如何工作的
# 你会注意到我们使用相同的点符来访问模块中的成员。Python 很好地重用了其中的符号，这
# 充满了“Pythonic”式的气息，这使得我们可以不必学习新的方式来完成同样的事情。
