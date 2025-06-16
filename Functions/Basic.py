'''
Created on 18 июн. 2020 г.

@author: Alex
Виды функций, передача аргументов, аннотации, атрибуты, ...
'''

tt = (1, 2)
dd = {'d1': 5, 'd2': 6}

def test_common():
    '''  Наиболее характерные примеры '''

    def f(p, n1, v1=1, *t, n2, v2=2, **d):
        ''' Распаковка параметров в вызове функции '''
        print("Позиционный: " + str(p))
        print("По умолчанию: " + str(v1) + " " + str(v2))
        print("Именованный: " + str(n1) + " " + str(n2))
        print("Кортеж:" + str(t))
        print("Словарь:" + str(d))

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

    print("И так тоже нет: t является позиционным аргументом, следующим за именнованным")
    #try: f(0, n1=11, v1=111, 4, 5, n2=22)
    #except Exception as e: print(e)

    print("А вот так запросто!")
    f(0, n1=11, v1=111, t=(4, 5), n2=22)

    ''' Порядок следования аргументов '''
    def f2(p, s1, s2, d1, d2, n, v=2):         # 1. Так можно
    #def f2(p, s1, s2, n, d1, d2, v=2):        # 2. Так тоже
    #def f2(p, s1, s2, n, v=2, d1, d2):        # 3. А вот так уже нельзя
        print(''' Порядок следования аргументов ''')
        print("Позиционный: " + str(p))
        print("По умолчанию: " + str(v))
        print("Именованный: " + str(n))
        print("Кортеж:" + str(s1) + " " +str(s2))
        print("Словарь:" + str(d1) + " " +str(d2))

    f2(0, *tt, **dd, n=3, v=4)
    f2(0, *tt, n=3, **dd)
    f2(0, *tt, n=3, v=4, **dd)

    print("Такой вызов возможен только в случае 2 определения")
    try: f2(0, *tt, 3, **dd)
    except Exception as e: print(e)

    ''' Более сложный вариант '''
    def ff(p, t1, t2, n1, v1=1, *t, n2, v2=2, d1, d2, **d):
        print("Позиционный: " + str(p))
        print("По умолчанию: " + str(v1) + " " + str(v2))
        print("Именованный: " + str(n1) + " " + str(n2))
        print("Упакованный Кортеж:" + str(t1) + " " + str(t2))
        print("Упакованный Словарь:" + str(d1) + " " + str(d2))
        print("Кортеж:" + str(t))
        print("Словарь:" + str(d))

    ff(0, *tt, 11, 1, 3, 4, **dd, d3=33, d4=44, n2=22, v2=222)

    ff.attr = "Атрибут"
    print("Атрибут: " + ff.attr)

    # Обход аргументов, функция exec 
    for p in dir(ff):
        s = "print('" + p + ":', ff." + p + ")"
    #    print(s)
        exec(s)

def test_annotate():
    ''' Тестирование функции с параметрами + аннотация '''
    def f(p: int, n1: 'str', *s: tuple, v: 'default', n2: set, **d: {'d1': '1', 'd2': 2})->bool:
        ''' Eclipse выдает ошибку на v: 'default', если он стоит перед *s. Но на самом деле работает и так
        Передавать в любом случае надо и s, и v '''
        print("Позиционный: " + str(p))
        print("По умолчанию: " + str(v))
        print("Именованный: " + str(n1) + " " + str(n2))
        print("Кортеж:" + str(s))
        print("Словарь:" + str(d))
        return True
    f(1, '2', (3, 4), v='test', n2='not a set', d3=0)

def test_lambda():
    ''' lamda-функции практически не отличаются от обычных '''
    l = (lambda p, n, v='default', *s, **d: str((p, n*v, str(s), str(d))))

    print(dir(l))
    print(l.__name__)
    print(l.__class__)

    '''Однако неверная передача именованных совместно с позиционными аргументами
    приводит к неожиданным результатам (по крайней мере, в eclipse):
    Программа ничего не делает, но нет даже сообщения об ошибке(!!!) '''
    print(l(0, 2))          # Так можно
    print(l(0, n=2))        # Так тоже
    print(l(0, n=2, v=3))   # И даже так
    #print(l(0, n=2, 3))    # А так уже нет!!! Попробуйте раскомментировать!!!

    print("Классический вызов: " + l(0, 1, 2, 3, 4, d1=11, d2=22))

def test_fcall():
    ''' Тест передачи функции в качестве параметра '''
    def some(par=''):
        print("Some Function", par)

    def ff(f1=None, f2=None, f3=None):
        if f1:
            f1 = f1()
    ff(some, some(), some('Parameter'))

def test_nested():
    ''' Передача вложенного списка параметров '''
    def unpack(a1=1, a2=2, *, named=''):
        print("a1 = ", a1, "a2 = ", a2, "named = ", named)

    def nested(*a):
        print("a = ", *a)

# Использование атрибутов, в т.ч доступ из самой ф-ции к собственным атрибутам
def selfref(f):
    f.func_defaults = f.func_defaults[:-1] + (f,)
    return f
@selfref
def foo(verb, adverb='swiftly', self=None):
    return '%s %s %s' % (self.subject, verb, adverb)
def test_selfref():
    ''' Использование атрибутов '''
    foo.subject = 'Fred'
    bar = foo
    del foo
    bar('runs')

test_selfref()
test_common()
