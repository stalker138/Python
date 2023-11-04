'''
Created on 19 июл. 2019 г.

@author: Stalker
'''

class My(Exception):
    def __init__(self, e):
        print("My Exception")

def bad(x, i, y):
    ''' Простейшая функция - огромное кол-во разнообразных исключений '''
    x[i] / y

''' Словари и списки - лучшие кандидаты для неправильного использования '''
D = {0: '0', 1: '1'}
L = [0, 1]

def attempt(x, i, y):
    ''' Вызов какого-либо исключения через внешнюю функцию '''
    try:
        bad(x, i, y)
    except TypeError:
        print("Type Error")
    except (KeyError, IndexError) as e:
        print(type(e), e)
    except My as e:
        print("My Exception")
    except Exception as e:
        print("Exception", e)
        raise My(e)
    except:
        print("All Exceptions")
    else:
        print("Normal")
    finally:
        print("Final")
    print("After try")

attempt(D, 0, 0)        # TypeError
attempt(D, 2, 0)        # KeyError
attempt(L, 2, 0)        # IndexError
attempt(L, 0, 0)        # Division by zero
