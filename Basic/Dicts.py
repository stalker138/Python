'''
Created on 18 февр. 2016 г.

@author: Stalker
'''

def basic():
    ''' Создание и основные операции '''
    d = {};                         print(d)    # Пустой список
    d = {1:'1', '2':2};             print(d)    # Стандартный
    d = dict(first='1', second=2);  print(d)    # Встроенный класс
    keys = [1,'2']; vals = ('1',2)
    d = dict(zip(keys, vals));      print(d)    # Zip
    d = dict.fromkeys(keys);        print(d)    # Из ключей, значения - None
    d = {v: v*2 for v in range(5)}; print(d)    # Генератор

    d1 = {1:'1', '2':2}; d2 = {'1':1, '2':22}
    d1.update(d2);                  print(d1)   # Слияние
    print(d1.keys() & d2.keys())                # Пересечение

def opers(d, k):
    ''' Проверка сущ-я, Чтение/запись. обход'''
    print(str(type(d)) + ' ' + str(isinstance(d, dict)))

    print(str(k in d))

    try:
        v = d[k]
    except KeyError:
        print("KeyError!")
        print(str(d.get(k, "No such key!")))
    else:
        print("Value:" + str(v))

    print(str(list(d)))

    for k in d:
        print(str(k) + ' ')
    for v in d.values():
        print(str(v) + ' ')
    for k, v in d.items():
        print(str(k) + ' ' + str(v) + '\n')

print("Множества: ")
s0 = set()                  # Пустое множество
s1 = set("123321")
s2 = set((1, 2, 3, '3', (2,), 1))
s3 = {1, 2, 3, 4}
sg = {s for s in (1, 2, 3, 4)}

def sets(s1, s2):
    print(s1)
    print(s2)

    print("Вхождение: " + repr(4 in s2))
    print("Разность: " + repr(s2 - s1))
    print("Объединение: " + repr(s2 | s1))
    print("Пересечение: " + repr(s2 & s1))
    print("Симметрическая Разность: " + repr(s2 ^ s1))

    print("Надмножество, подмножество: " + repr(s2>s1, s2<s1))

    for s in s1:
        print(s)
#opers({"s": "str", 1:"number", (1,2,3):[1,2,3]}, (1,2,3))
basic()
