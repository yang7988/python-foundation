# Pickle
#
# Python 提供了一个叫作 Pickle 的标准模块，通过它你可以将任何纯 Python 对象存储到一
# 个文件中，并在稍后将其取回。这叫作持久地（Persistently）存储对象。

import pickle

# The name of the file where we will store the object
shoplistfile = 'shoplist.data'
# The list of things to buy
shoplist = ['apple', 'mango', 'carrot']
# Write to the file
f = open(shoplistfile, 'wb')
# Dump the object to a file
pickle.dump(shoplist, f)
f.close()
# Destroy the shoplist variable
del shoplist
# Read back from the storage
f = open(shoplistfile, 'rb')
# Load the object from the file
storedlist = pickle.load(f)
print(storedlist)

# 要想将一个对象存储到一个文件中，我们首先需要通过 open 以写入（write）二进制
# （binary）模式打开文件，然后调用 pickle 模块的 dump 函数。这一过程被称作封装
# （Pickling）。
# 接着，我们通过 pickle 模块的 load 函数接收返回的对象。这个过程被称作拆封
# （Unpickling）。
