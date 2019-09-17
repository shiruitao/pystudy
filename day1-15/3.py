"""
if 语句的使用
"""

from random import randint

face = randint(1, 7)
if face == 1:
    result = 1
elif face == 2:
    result = 2
elif face == 3:
    result = 3
elif face == 4:
    result = 4
elif face == 5 or face == 7:
    result = 5
else:
    result = 6
print(result)
