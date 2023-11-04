'''
Created on 7 дек. 2019 г.

@author: stalker
'''

print(1<2<3)    # 1<2 and 2<3

print(str(5/2))     # истинное деление            2.5
print(str(-5/2))    # истинное деление            -2.5

# Проверка на -1
print(~-1)    # False (0)
print(~1)     # True (!0)

print("Вывод str: " + str(1/3) + " repr: " + repr(1/3))

import math
# Распространенные константы
print("pi: " + str(math.pi) + " e: " + str(math.e))

# округление вниз
print(math.floor(2.5))      #  2
print(str(5//2))            # деление с округлением вниз  2
print(math.floor(-2.5))     # -3
print(str(-5//2))           # деление с округлением вниз  -3

# усечение
print(math.trunc(2.5))      #  2
print(math.trunc(-2.5))     # -2

from decimal import Decimal
print("Фиксированная точность:")
print(0.1 + 0.1 + 0.1 - 0.3)
n = Decimal(0.1) + Decimal(0.1) + Decimal(0.1)
print("n = " + repr(n))
print(repr(Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3)))

from fractions import Fraction
print("Вещественные числа:")
f1 = Fraction(1,3)
f2 = Fraction(2,3)
print("Дробь: " + str(f1) + " Сложение: " + str(f1+f2) + " Вычитание: " + str(f1-f2))
f = Fraction(1,10) + Fraction(1,10) + Fraction(1,10) - Fraction(3,10)
print("Точность: " + repr(f))

print("Преобразования:")
f = 2.5
print(f.as_integer_ratio())
print(Fraction.from_float(f))
