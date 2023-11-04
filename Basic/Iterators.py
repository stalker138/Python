'''
Created on 28 апр. 2020 г.

@author: Alex
'''

l = [1, 2, 3]
d = {'1':1, '2':2, '3':3}
dk = d.keys(); dv = d.values(); di = d.items(); de = enumerate(d)
print("Объекты словаря: ", dk, dv, di, de)
s = {1, 2, 3}
r = range(3);       print(r)            # Объект диапазона

z = zip((1, 2, 3), (11, 22, 33))

L = iter(l);        print(L)            # List итератор
D = iter(d);        print(D)            # Dict итератор
S = iter(s);        print(S)            # Set итератор
R = iter(r);        print(R)            # Range итератор
E = iter(de);       print(E, E is de)   # Объект-итератор нумератора E === de
Z = iter(z);        print(Z)            # Zip итератор

while True:
    try:
        v = next(E)
    except StopIteration:
        print("Конец списка")
        break;
    print(v, end='')

def shared():
    ''' Множественные и единственные итераторы '''
    R2 = iter(r)
    print("Range Iterator: ", next(R), next(R2))
    Z2 = iter(z)
    print("Zip Iterator: ", next(Z), next(Z2))

def generators():
    ''' Генераторы '''
    dg = {str(x): x**2 for x in l}              # Генератор словаря
    sg = {x**2 for x in l}                      # Генератор множества
    xy = [x+y for x in L for y in d.values() if x != 1 if y != 2]   # Генератор списка

    print("Dict: ", type(dg), dg)
    print("Sets: ", type(dg), sg)
    print("List: ", type(xy), xy)

    # Выражение-генератор - однократный итератор
    G = (x**2 for x in l)
    print(G, G is iter(G))
    print("Преобразование: ", set(G))
    print("Итератор исчерпан: ", list(G))
    G = (x**2 for x in l)                       # Пересоздание
    print(next(G), next(iter(G)))

    def gen():
        ''' Простая функция-генератор '''
        for x in range(5):
            yield x**2
    G = gen()
    print("Простая функция-генератор: ", next(G), next(G), next(G))

    def genext():
        ''' Расширенный протокол '''
        for x in range(5):
            X = (yield x**2)
            print(X)
    G = genext()
    next(G)                 # Необходимо для инициализации генератора
    S = G.send(4)        # Переход к следующему и передача значения
    print(S)
    print(next(G))
    G.close()
    next(G)                 # Передается None

shared()

generators()