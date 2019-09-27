"""
序列数据结构 之 列表
"""
# 1. 列表索引从0 开始，列表可以进行截取（切片）、组合等
import time

list1 = ['中国', '美国', 1997, 2019]
list2 = [1, 2, 3, 4, 5, 6, 7]
print(id(list1))
print('list1[0]:', list1[0])
print('切片', list2[1:5])

# 2. 更新 列表
print(list1[3])
list1[2] = 1864
print(list1[2])

# 3. 删除 列表 元素

del list1[3]
list1.remove(1864)

print(list1)
# pop()方法来删除列表中指定位置元素 ，无参数时 删除最后一个元素

list2.pop(2)
list2.pop()
print(list2)

# 4. 添加列表元素
# 使用 append()方法在列表的末尾添加元素
list2.append(time.time())
print(list2)

print(list(range(1,10)))

L = []
for x in range(1, 10):
    L.append(x*x)

print(L)

# 偶数 的平方
print([x*x for x in range(1,11) if x % 2 == 0])

LL = ['Hello', 'World', 'IBM', 'Apple', 'HuaWei']
print([s.lower() for s in LL])

print([m+n for m in 'ABC' for n in 'XYZ'])