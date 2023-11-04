'''
Created on 12 янв. 2020 г.

@author: Stalker

Области видимости, доступность, ...
'''
from _tracemalloc import start

GL = "Неизменяемая глобальная переменная "
def global1():
    ''' Глобальная переменная определяется ниже испльзующей ее функции '''
    global GN, GG
    try:
        GL += "изменилась"                                  # Попытка изменить неглобальную
    except Exception as e:
        print("GL: ", e)
    print(GL)
    GL = "Неизменяемая глобальная переменная изменилась"    # Переменная изменилась локально
    print(GL)
    GG += "изменилась"                                      # Переменная изменилась глобально
    GN = "Несуществующая глобальная переменная "
GG = "Изменяемая глобальная переменная "

def global1test():
    print("GL: " + GL)
    print("GG: " + GG)
    try:
        print("GN: " + GN)
    except Exception as e:
        print("GN: ", e)
    global1()
    print("GL: " + GL)
    print("GG: " + GG)
    print("GN: " + GN)

GE = "Глобальная переменная "
def maker(N):
    GE = "Объемлимающая переменная переопределяет глобальную"
    def action1(X):
        nonlocal GE         # Нелокальная переменная должна уже
        print("GE: ", GE)   # существовать в объемливающей области
        GE += "изменена"
        print("GE: ", GE)
        return X**N

    action2 = (lambda X: X**N)

    actions = []
    for x in range(1, 3):
        actions.append(lambda x=x: x**N)

    return action1, action2, actions

def counter(start):
    ''' Классический пример: счетчик вызовов '''
    state = start           # Каждый вызов сохраняет свой экземпляр state
    def nested(label):
        nonlocal state
        print(label, state)
        state += 1          # Изменит значение nonlocal переменной
    return nested

def nonlocaltest():
    print("GE: " + GE)
    f1, f2, ff = maker(2)
    print(f1(3), f2(3))
    print(f1(4), f2(4))
    print("GE: " + GE)

#global1test()
nonlocaltest()