# 集合
#
# 集合（Set）是简单对象的无序集合（Collection）。当集合中的项目存在与否比起次序或其出
# 现次数更加重要时，我们就会使用集合。
# 通过使用集合，你可以测试某些对象的资格或情况，检查它们是否是其它集合的子集，找到
# 两个集合的交集，等等。

bri = set(['brazil', 'russia', 'india'])
print('india' in bri)

print('usa' in bri)

bric = bri.copy()
bric.add('china')
print(bric.issuperset(bri))

bri.remove('russia')
print(bri & bric)  # OR bri.intersection(bric)
