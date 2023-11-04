'''
Created on 18 февр. 2016 г.

@author: Stalker
'''

''' Распаковка параметров в вызове функции '''
def f(p, n1, v1=1, *s, n2, v2=2, **d):
    print("Позиционный: " + str(p))
    print("По умолчанию: " + str(v1) + " " + str(v2))
    print("Именованный: " + str(n1) + " " + str(n2))
    print("Кортеж:" + str(s))
    print("Словарь:" + str(d))

def testf():
    print("Так можно")
    f(0, 11, 111, 4, 5, n2=22, d1=1, d2=2)
    print("Так тоже")
    f(0, 11, 111, 4, 5, n2=22, v2=222, d1=1, d2=2)
    print("Так тоже, но v1 не передастся по умолчанию")
    f(0, 11, 4, 5, n2=22, d1=1, d2=2)

    print("А вот так нет: не указан именованный аргумет n2")
    try: f(0, 11, 111, 4, 5)
    except Exception as e: print(e)

    print("Так тоже нет: позиционный аргумент (v1) следует за именнованным"
          "Причем исключение возникает на стадии 'компиляции'"
          "Не срабатывает даже finally!!!")
    #try: f(0, n1=11, 111, 4, 5, n2=22)
    #except Exception as e: print(e)
    #except: print("?")
    #finally: print("!")

    print("И так тоже нет: s является позиционным аргументом, следующим за именнованным")
    #try: f(0, n1=11, v1=111, 4, 5, n2=22)
    #except Exception as e: print(e)

    print("А вот запросто!")
    f(0, n1=11, v1=111, s=(4, 5), n2=22)

''' Распаковка параметров внутри функции'''
def f2(p, s1, s2, d1, d2, n, v=2):         # 1. Так можно
#def f2(p, s1, s2, n, d1, d2, v=2):        # 2. Так тоже
#def f2(p, s1, s2, n, v=2, d1, d2):        # 3. А вот так уже нельзя
    print("Позиционный: " + str(p))
    print("По умолчанию: " + str(v))
    print("Именованный: " + str(n))
    print("Кортеж:" + str(s1) + " " +str(s2))
    print("Словарь:" + str(d1) + " " +str(d2))

s = (1, 2)
d = {'d1': 5, 'd2': 6}

def f2test():
    f2(0, *s, **d, n=3, v=4)
    f2(0, *s, n=3, **d)
    f2(0, *s, n=3, v=4, **d)

    print("Такой вызов возможен только в случае 2 определения")
    try: f2(0, *s, 3, **d)
    except Exception as e: print(e)

''' Комбинированный вариант '''
def ff(p, s1, s2, n1, v1=1, *s, n2, v2=2, d1, d2, **d):
    print("Позиционный: " + str(p))
    print("По умолчанию: " + str(v1) + " " + str(v2))
    print("Именованный: " + str(n1) + " " + str(n2))
    print("Упакованный Кортеж:" + str(s1) + " " + str(s2))
    print("Упакованный Словарь:" + str(d1) + " " + str(d2))
    print("Кортеж:" + str(s))
    print("Словарь:" + str(d))

ff(0, *s, 11, 1, 3, 4, **d, d3=33, d4=44, n2=22, v2=222)
