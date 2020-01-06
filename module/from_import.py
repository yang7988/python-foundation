# 如果你希望直接将 argv 变量导入你的程序（为了避免每次都要输入 sys. ），那么你可以
# 通过使用 from sys import argv 语句来实现这一点。
# 警告：一般来说，你应该尽量避免使用 from...import 语句，而去使用 import 语句。
# 这是为了避免在你的程序中出现名称冲突，同时也为了使程序更加易读。
# 案例：
from math import sqrt
print("Square root of 16 is", sqrt(16))