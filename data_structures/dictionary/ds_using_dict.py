# 字典
#
# 字典就像一本地址簿，如果你知道了他或她的姓名，你就可以在这里找到其地址或是能够联
# 系上对方的更多详细信息，换言之，我们将键值（Keys）（即姓名）与值（Values）（即地
# 址等详细信息）联立到一起。在这里要注意到键值必须是唯一的，正如在现实中面对两个完
# 全同名的人你没办法找出有关他们的正确信息。
#
# 另外要注意的是你只能使用不可变的对象（如字符串）作为字典的键值，但是你可以使用可
# 变或不可变的对象作为字典中的值。基本上这段话也可以翻译为你只能使用简单对象作为键
# 值。
#
# 在字典中，你可以通过使用符号构成 d = {key : value1 , key2 : value2} 这样的形式，来成
# 对地指定键值与值。在这里要注意到成对的键值与值之间使用冒号分隔，而每一对键值与值
# 则使用逗号进行区分，它们全都由一对花括号括起。
#
# 另外需要记住，字典中的成对的键值—值配对不会以任何方式进行排序。如果你希望为它们
# 安排一个特别的次序，只能在使用它们之前自行进行排序。
#
# 你将要使用的字典是属于 dict 类下的实例或对象。


# “ab”是地址（Address）簿（Book）的缩写
ab = {
'Swaroop': 'swaroop@swaroopch.com',
'Larry': 'larry@wall.org',
'Matsumoto': 'matz@ruby-lang.org',
'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is", ab['Swaroop'])

# 删除一对键值—值配对
del ab['Spammer']
print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

# 添加一对键值—值配对
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])