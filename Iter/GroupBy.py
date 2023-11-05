'''
Created on 26 июл. 2019 г.

@author: Stalker
'''

from itertools import *

l = [(1,"2",3), (1,"2",4), (2,"3",4), (2,"3",5)]
print(sum([float(t[1]) for t in l]))

g = [list(g) for k, g in groupby(l, lambda x: x[0:2])]
print(list(g))
s = [(g[0][0], sum(float([s[1] for s in g]), g[0][2]) for g in g]
print(s)