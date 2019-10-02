"""
Python字典(dict)是一种可变容器模型，且可存储任意类型对象，字典也被称为关联数组或哈希表
键必须是唯一的，值则不必

"""

# 创建 字典
# d={key1: value1, key2: value2}

dict = {'Name': 'xmj', 'Age': '17', 'Name': 'Manni'}

"""
字典值可以是任何python对象
不允许同一个键出现两次，在创建时如果同一个键被赋值两次，后一个值会覆盖前一个值
"""

print(dict['Name'])


