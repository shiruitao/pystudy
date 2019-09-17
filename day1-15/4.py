"""
在Python中构造循环结构有两种做法，一种是for-in循环，一种是while循环。
"""

import random

sum = 0
for i in range(101):
    sum += i
print(sum)

"""
用for循环实现1~100之间的偶数求和
"""
# range(2, 101, 2) 可以产生一个 2 到 100 的奇数序列，其中的 2 是步长，即数值序列的增量。
sum = 0
for x in range(2, 101, 2):
    sum += x
print(sum)

"""
while循环
"""

# answer = random.randint(1, 100)
# counter = 0
# while True:
#     counter += 1
#     number = int(input('请输入: '))
#     if number < answer:
#         print('大一点')
#     elif number > answer:
#         print('小一点')
#     else:
#         print('恭喜你猜对了!')
#         break
# print('你总共猜了%d次' % counter)
# if counter > 7:
#     print('你的智商余额明显不足')

"""
九九乘法表
"""

for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d*%d=%d" % (i, j, i * j), end='\t')
    print()

"""
最大公约数和最小公倍数
"""
x = int(input('x = '))
y = int(input('y = '))
if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break