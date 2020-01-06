# 列表
# 列表 是一种用于保存一系列有序项目的集合，也就是说，你可以利用列表保存一串项目的序
# 列。想象起来也不难，你可以想象你有一张购物清单，上面列出了需要购买的商品，除开在
# 购物清单上你可能为每件物品都单独列一行，在 Python 中你需要在它们之间多加上一个逗
# 号。
# 项目的列表应该用方括号括起来，这样 Python 才能理解到你正在指定一张列表。一旦你创建
# 了一张列表，你可以添加、移除或搜索列表中的项目。既然我们可以添加或删除项目，我们
# 会说列表是一种可变的（Mutable）数据类型，意即，这种类型是可以被改变的。

# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']
print('I have', len(shoplist), 'items to purchase.')
print('These items are:', end=' ')

for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice.')

shoplist.append('rice')

print('My shopping list is now', shoplist)
print('I will sort my list now')

shoplist.sort()
print('Sorted shopping list is', shoplist)
print('The first item I will buy is', shoplist[0])

olditem = shoplist[0]
del shoplist[0]

print('I bought the', olditem)
print('My shopping list is now', shoplist)