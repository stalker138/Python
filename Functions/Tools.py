'''
Created on 16 нояб. 2022 г.

@author: stalker
Средства функционального программирования
'''

# filter(function, sequence) Фильтрация элементов sequence функцией function
def f(x):
    for y in range(2, x):
        if (x%y == 0): return 0
    return 1
f = filter(f, range(2, 40))
print(list(f))

# map(function, sequence) Последовательное применение функции funcion к элементамs sequence
def cube(x): return x*x*x
m = map(cube, range(1, 11))
print(list(m))

''' Не работает 
seq1 = ['cat', 'mouse', 'bird']
seq2 = ['кот', 'мышь', 'птица']
for x, y in map(None, seq1, seq2):
    print (x, y)
'''

# zip(seq1, ...) Преобразование пары списков в список пар
# Вместо map с None:
a = (1, 2, 3, 4)
b = (5, 6, 7, 8)
c = (9, 10, 11)
d = (12, 13)
print(list(zip(a)))             # [(1,), (2,), (3,), (4,)]
print(list(zip(a, b)))          # [(1, 5), (2, 6), (3, 7), (4, 8)]
print(list(zip(a, d)))          # [(1, 12), (2, 13)]
print(list(zip(a, b, c, d)))    # [(1, 5, 9, 12), (2, 6, 10, 13)]

from functools import reduce
# reduce(function, sequence, initial=sequence[0])
# Последовательное применение функции function к элементам sequence с накоплением результатов
r = range(1, 5)
print(reduce(lambda x, y: x*y, r))  # 24
print(reduce(lambda x, y: x+y, r))  # 10
