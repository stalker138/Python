'''
Created on 26 июл. 2019 г.

@author: Stalker
'''

from itertools import groupby
from collections import Counter, defaultdict
import operator as op

l = [(1,"2",3), (1,"2",4), (2,"3",4), (2,"3",5)]

g = [list(g) for k, g in groupby(l, lambda x: x[0:2])]
print(list(g))
s = [(g[0][0], sum([float(s[1]) for s in g]), g[0][2]) for g in g]
print(s)

# initialize list
test_list = [('gfg', ), ('is', ), ('best', ), ('gfg', ),
             ('is', ), ('for', ), ('geeks', )]
# Исключаем дублирование
set_list = list(set(test_list))

ipl = [("1.1.2.1", ""), ("1.3.1.2", ), ("1.1.2.2", ""), ("1.1.2.1", ""),
       ("1.1.1.1", ""), ("1.1.1.4", ""), ("1.1.1.2", ""), ("1.1.1.3", ""), ("1.1.1.3", "x"), ("1.1.1.3", ), ("1.1.1.1", ""), ("1.1.1.5", ""), 
       ("1.1.3.1", ""), ("1.1.3.2", ""), ("1.1.3.3", ""), ("1.1.1.4", ""),
       ("1.2.1.1", ""), ("1.2.2.1", "x"), ("1.2.3.2", ""), ("1.2.3.3", ""), ("1.2.4.3", ""), ("1.2.5.3", ""), ("1.2.6.4", ""),
       ("1.3.1.1", ""), ("1.3.2.1", ""),
       ("1.4.1.1", "")]

def counters():
    ''' Различные способы подсчета кол-ва вхождений эл-та в список '''
    # Group and count similar records using Counter() + list comprehension + items()
    res = [(counter, ) + ele for ele, counter in Counter(test_list).items()]
    print("using Counter()", str(res))

    # Using count(),join(),list() and set() methods
    res = []
    for s in set_list:
        a = test_list.count(s)
        b = "".join(s)
        res.append((a, b))
    print("using set() & count():", str(res))
    res = [(test_list.count(s), "".join(s)) for s in set_list]
    print("the same result:", str(res))

    # using operator.countOf() method
    res = []
    for s in set_list:
        a = op.countOf(test_list, s)
        b = "".join(s)
        res.append((a, b))
    print("using operator.countOf():", str(res))
    res = [(op.countOf(test_list, s), "".join(s)) for s in set_list]
    print("the same result:", str(res))

    # Using defaultdict() and list comprehension
    counter = defaultdict(int)
    for s in test_list:
        counter[s] += 1
    res = [(count,) + s for s, count in counter.items()]
    print("using defaultdict():", str(res))

    # Using itertools.groupby() and len()
    test_list.sort()
    res = [(len(list(group)), key) for key, group in groupby(test_list)]
    print("Using itertools.groupby()", str(res))

#counters()

ip4 = [('.'.join(i[:2]), ('.'.join(i[:3]), 'x' if i[4:] and i[4:][0] else '')) for i in [ip[0].split('.')+list(ip[1:]) for ip in ipl if '.' in ip[0]]]
#ip4 = sorted(ip4, key = lambda ip: ip[1])
ipd = {}
for k, v in ip4:
    print(k, v)
    ip2 = ipd.get(k)
    if ip2:
        ip2[1] += 1             #
        ip3 = ip2[0].get(v[0])  #
        if ip3:
            ip3[0] += 1
        else:
            ip3 = ip2[0][v[0]] = [1, 0]
    else:
        ip3 = [1, 0]
        ip2 = ipd[k] = [{v[0]: ip3}, 1, 0]
    if not v[1]:
        ip3[1] += 1
        ip2[2] += 1
print("That is All!")
