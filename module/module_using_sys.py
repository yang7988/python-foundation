import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)
print('\n\nThe PYTHONPATH is', sys.path, '\n')


# 首先，我们通过 import 语句导入 sys 模块。基本上，这句代码将转化为我们告诉 Python
# 我们希望使用这一模块。 sys 模块包含了与 Python 解释器及其环境相关的功能，也就是所
# 谓的系统功能（system）。
# 当 Python 运行 import sys 这一语句时，它会开始寻找 sys 模块。在这一案例中，由于其
# 是一个内置模块，因此 Python 知道应该在哪里找到它。
# 如果它不是一个已编译好的模块，即用 Python 编写的模块，那么 Python 解释器将从它的
# sys.path 变量所提供的目录中进行搜索。如果找到了对应模块，则该模块中的语句将在开始
# 运行，并能够为你所使用。在这里需要注意的是，初始化工作只需在我们第一次导入模块时
# 完成。
# sys 模块中的 argv 变量通过使用点号予以指明，也就是 sys.argv 这样的形式。它清晰地
# 表明了这一名称是 sys 模块的一部分。这一处理方式的另一个优点是这个名称不会与你程序
# 中的其它任何一个 argv 变量冲突。
# sys.argv 变量是一系列字符串的列表（List）（列表将在后面的章节予以详细解释）。具体
# 而言， sys.argv 包含了命令行参数（Command Line Arguments）这一列表，也就是使用命
# 令行传递给你的程序的参数。
# 如果你正在使用一款 IDE 来编写并运行这些程序，请在程序菜单中寻找相关指定命令行参数
# 的选项。
# 在这里，当我们运行 python module_using_sys.py we are arguments 时，我们通过 python 命
# 令来运行 module_using_sys.py 模块，后面的内容则是传递给程序的参数。 Python 将命令行
# 参数存储在 sys.argv 变量中供我们使用。
# 在这里要记住的是，运行的脚本名称在 sys.argv 的列表中总会位列第一。因此，在这一案
# 例中我们将会有如下对应关系： 'module_using_sys.py' 对应 sys.argv[0] ， 'we' 对应
# sys.argv[1] ， 'are' 对应 sys.argv[2] ， 'arguments' 对应 sys.argv[3] 。要注意到
# Python 从 0 开始计数，而不是 1。
# sys.path 内包含了导入模块的字典名称列表。你能观察到 sys.path 的第一段字符串是空的
# ——这一空字符串代表当前目录也是 sys.path 的一部分，它与 PYTHONPATH 环境变量等
# 同。这意味着你可以直接导入位于当前目录的模块。否则，你必须将你的模块放置在
# sys.path 内所列出的目录中。
# 另外要注意的是当前目录指的是程序启动的目录。你可以通过运行 import os;
# print(os.getcwd()) 来查看你的程序目前所处在的目录。