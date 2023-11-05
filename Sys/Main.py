'''
Created on 07 апр. 2016 г.

@author: Alex
'''

import sys

''' Имя модуля в пакете обязательно должно квалифицироваться!
    Даже если оба модуля из одного каталога!!!'''
from Sys.Module2 import *       # абсолютное импортирование
from Sys.Sub import SubPacked

def Argv():
    print("Main: " + sys.argv[0])
    SubPacked.Argv()            # В данном вызове нельзя Sys.Sub.SubPacked.Argv()

def Globals():
    global Z1, Z2

    print(Z2)           # => 0
    Z2 = 1 
    print(Z2)           # => 1
    FZ()                # => 0???

if __name__ == '__main__':
#    from . import Module1       # !!! Main: Относительный импорт неприменим
#    print("Z1 = " + str(Module1.Z1))

    Argv()
    Globals()

else:
    from . import Module1               # !!! Non Main:
    print("Z1 = " + str(Module1.Z1))    # !!! Так можно
