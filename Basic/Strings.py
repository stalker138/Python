'''
Created on 18 февр. 2016 г.

@author: Stalker
'''

def simple():
    ''' Простые строки, экранирование '''
    s = "Hello, World!";        print(s)
    s = '"\'Hello, World\'"';   print(s)
    r = r'\n\t';                print(r)    # "Сырая"
    #r = r'\';                  print(r)    # Не может заканчиваться обратным слэшем
    b = b'\xc3';                print(b)

def multilines():
    ''' Многострочные строки '''
    m = ("First"
         "Second"
         "last")
    print(m)
    m = "First" + \
        "Second" + \
        "last"
    print(m)
    m = """First
         Second
         last"""
    print(m)

import sys
def formats():
    ''' Форматирование '''
    s = "String"        # Строка
    c = 'S'             # Символ
    d = 123             # Целое
    x = 1.23456789      # Вещественное
    print("%s | %c | %d | %e | %f | %g" % (s, c, d, x, x, x))

    # Из словаря
    print("From dict: %(k)d %(v)s" % {"k":1, "v":"spam"})

    # Современное
    spam = "spam"
    fmt = "{0} {1} and {2}"                 # Позиционное
    print(fmt.format(spam, spam, spam))
    fmt = "{spam} {food} and {spam}"        # Именованное
    print(fmt.format(spam='spam', food='food'))
    fmt = "{0} {food} and {0}"              # Смешанное
    print(fmt.format(spam, food='food'))

    # Ключи, атрибуты и смещения
    fmt = "My {1[comp]} runs {0.platform} first: {2[0]}, third: {2[2]}"
    print(fmt.format(sys, {'comp':'note'}, [1,2,3,4]))
    fmt = "My {d[comp]} runs {a.platform} first: {l[0]}, third: {l[2]}"
    print(fmt.format(a=sys, d={'comp':'note'}, l=[1,2,3,4]))

import decimal
def specifikators():
    "{0} {0!s} {0!r} {0!a}".format(decimal.Decimal("93.4"))

    s = "The sword of truth"
    "{0}".format(s)         # форматирование по умолчанию
    "{0:25}".format(s)      # минимальная ширина 25
    "{0:.25}".format(s)     # максимальная ширина 25
    "{0:>25}".format(s)     # по правому краю, минимальная ширина 25
    "{0:^25}".format(s)     # по центру, минимальная ширина 25
    "{0:-^25}".format(s)    # заполнитель, по центру, минимальная ширина 25
    "{0:-<25}".format(s)    # заполнитель, по левому краю, минимальная ширина 25

    maxwidth =12
    "{0}".format(s[:maxwidth])      # обычный срез
    "{0:.{1}".format(s, maxwidth)   # вложенное замещаемое поле

formats()
