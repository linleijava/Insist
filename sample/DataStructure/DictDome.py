"""
Python字典(dict)是一种可变容器模型，且可存储任意类型对象，字典也被称为关联数组或哈希表
键必须是唯一的，值则不必

"""

# 创建 字典
# d={key1: value1, key2: value2}
from datetime import datetime

dict = {'Name': 'xmj', 'Age': '17', 'Name': 'Manni'}

print(len(dict))
"""
字典值可以是任何python对象
不允许同一个键出现两次，在创建时如果同一个键被赋值两次，后一个值会覆盖前一个值
键不可变，所以可以用数字、字符串或 元组 充当，用列表不行
"""

print(dict['Name'])

stu = {'Name': '王海', 'Age': 17, 'Class': '计算机一班'}

print(stu['Name'])

# print(stu[sex])
# 修改字典
stu['Age'] = 18
# 增加键值
stu['School'] = '中原工学院'

print(stu)

# 删除字典中的元素
"""
del()方法允许使用键从字典中删除元素（条目）
clear()方法清空字典中的所有元素
"""
del stu['Name']  # 删除键是 'Name'的元素（条目）
print(id(stu))

print(stu.pop('Age'))  # 展示删除的内容， 删除
print(stu)


stu.clear()     # 清空字典中的所有元素

del stu   # 删除字典， 用del 删除后字典不再存在

# in 运算
"""
字典里的 in 运算用于判断某个键是否在字典里面，对于 value 值不适用，其功能与 has_key(key)相似
使用get 函数判断

"""

print('Name' in dict)
print('sex' in dict)
print(dict.get('Sex', '不存在'))


# 获取字典中的所有值 dict.values()

print(dict.values())
print(list(dict.values()))


# items()方法
"""
items()方法把字典中的每个key 和 value 组成一个元组，并把这些元组放在列表中返回

"""
stu1 = {'Name': '王海', 'Age': 17, 'Class': '计算机一班'}

for key,value in stu1.items():
    print(key, value)


# popitem()方法，随机删除一个键值对

d10 = {'Year': 2019, 'Month': 10, 'Day': 3}
v1 = d10.popitem()

print(v1)


# copy (浅拷贝)

dict1 = dict.copy()
del dict['Name']
print(dict1)
print(dict)
print(id(dict1))
print(id(dict))


print(datetime.now())

