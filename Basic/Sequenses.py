'''
Created on 18 февр. 2016 г.

@author: Stalker
'''

def outside():
    ''' Проверка обращения за пределами диапазона внутри if '''
    l = ["0", "1"]
    print(l[2] if len(l)>2 else "Outside!!!")   # Outside!!!

outside()
