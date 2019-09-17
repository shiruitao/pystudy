"""
使用input()函数获取键盘输入
使用int()进行类型转换
用占位符格式化输出的字符串
"""

a = int(input("a = "))
b = int(input("b = "))
print("%d + %d = %d" % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))

"""
使用type()检查变量的类型
"""

a = 1
b = 1.2
c = True
d = 1 + 2j
e = "abc"

print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'bool'>
print(type(d))  # <class 'complex'>
print(type(e))  # <class 'str'>

"""
int()：将一个数值或字符串转换成整数，可以指定进制。
float()：将一个字符串转换成浮点数。
str()：将指定的对象转换成字符串形式，可以指定编码。
chr()：将整数转换成该编码对应的字符串（一个字符）。
ord()：将字符d串（一个字符）转换成对应的编码（整数）。
"""

print(int("123"))
print(float("1.2"))
print(str(1+2j))
print(chr(500))
print(ord("a"))

"""
运算符的使用
"""

a = 5
b = 10
c = 3
d = 4
e = 5
a += b
a -= c
a *= d
a /= e
print("a = ", a)

flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print("flag1 = ", flag1)
print("flag2 = ", flag2)
print("flag3 = ", flag3)
print("flag4 = ", flag4)
print("flag5 = ", flag5)
print(flag1 is True)
print(flag2 is not False)

"""
输入年份 如果是闰年输出True 否则输出False
"""

year = int(input('请输入年份: '))
# 如果代码太长写成一行不便于阅读 可以使用\或()折行
is_leap = year % 4 == 0 and year % 100 != 0 or \
           year % 400 == 0
print(is_leap)
