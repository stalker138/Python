'''
Created on 18 июн. 2020 г.

@author: Alex
'''

def test_args():
    ''' Тестирование функции с параметрами + аннотация '''
    def f(p: int, n: str, *s: tuple, v: 'default', **d: {'d1': '1', 'd2': 2})->bool:
        ''' Eclipse выдает ошибку на v: 'default', если он стоит перед *s. Но на самом деле работает и так
        Передавать в любом случае надо и s, и v '''
        print("p = ", str(p), "n = ", n, "v = ", v, "s = ", str(s), "d = ", str(d))
        return True
    f(1, '2', (3, 4), v='test')
    f.attr = "Атрибут"
    print("Атрибут: " + f.attr)

    for p in dir(f):
        s = "print('" + p + ":', f." + p + ")"
    #    print(s)
        exec(s)

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

test_fcall()
