'''
Created on 18 февр. 2016 г.

@author: Stalker
'''

def assigns():
    ''' Присваивания '''
    a = 1               # Простое
    a = b = 1           # Групповое
    [a, b] = [1, 2]     # Присванивание списком
    a, b = 1, 2         # Присваивание кортежем
    a, b = b, a         # swap -трюк
    a += 1              # Комбинированное

    # Присваивание последовательностей, распаковка
    s = "test"
    a, b, c, d = s          # Одинаковое число элементов с обеих сторон
    print(a, b, c, d)

    try:
        a, b, c, d, e = s   # Много
    except Exception as x:
        print(x)
    try:
        a, b, c = s         # Мало
    except Exception as x:
        print(x)

    a, *b, c = s                            # Распаковка
    print("Распаковка: ", a, b, c)          # t ['e', 's'] t
    a, *b, c, d = s                         # Распаковка: даже если один эл-т - все равно список
    print("Все равно список: ", a, b, c, d) # t ['e'] s t
    a, *b, c, d, e = s                      # Распаковка: пустой список (не исключение!)
    print("Пустой список: ", a, b, c, d, e) # t [] e s t

    try:
        a, *b, c, *d = s                    # Более одного эл-та для распаковки
    except Exception as x:
        print(x)
    try:
        *b = s                              # Единственный эл-т для распаковки
    except Exception as x:
        print(x)
    *b, = s                                 # А так можно
    print("Единственный эл-т: ", b)         # ['t', 'e', 's', 't']

# Логические операторы возвращают первый подходящий операнд
print(2 and 3, 3 or 2)          # (3, 3)
print([] or {})                 # {}
print([] and {})                # []
a = b = c = False; default = "spam"
print(a or b or c or default)   # Трюк: одно из или по умолчанию

e = True
a = False if e else True;       print(a)    # Аналог ?:

def cycles():
    for i in range(10):
        print("i indide: " + str(i))
        if i == 10: break
        i += 2                       # Никакие изменения не влияют на итерации
    else: print("No Break!\n")
    print("i = " + str(i))          # i=11 !!Последняя итерация влияет!! (11==9+2)

assigns()