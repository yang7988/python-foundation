# 编写你自己的模块很简单，这其实就是你一直在做的事情！这是因为每一个 Python 程序同时
# 也是一个模块。你只需要保证它以 .py 为扩展名即可。下面的案例会作出清晰的解释。

def say_hi():
    print('Hi, this is mymodule speaking.')


__version__ = '0.1'


# 上方所呈现的就是一个简单的模块。正如你所看见的，与我们一般所使用的 Python 的程序相
# 比其实并没有什么特殊的区别。我们接下来将看到如何在其它 Python 程序中使用这一模块。
# 要记住该模块应该放置于与其它我们即将导入这一模块的程序相同的目录下，或者是放置在
# sys.path 所列出的其中一个目录下。