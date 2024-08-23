'''
Created on 3 авг. 2024 г.

@author: stalker
'''

from functools import reduce
import operator
 
def unpack(l):
    ''' Различные способы распаковки списков, словарейб ... '''
    ((v11, v12), v2) = l
    r = (reduce(operator.add, l))
    print("Unpack:", r)
 
unpack((['a', 'apple'], ['b', 'ball']))