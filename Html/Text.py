'''
Created on 13 июля 2016 г.

@author: Alex
'''

import re
 
def safeSplit(regex, text):
    res=[]
    sear=regex.search(text)
    while sear:
        res.append(text[:sear.end()])
        text=text[sear.end():]
        sear=regex.search(text)
    res.append(text)
    return res
 
text = '"Что за хрень?" спросила Алиса и т.п. Вовсе нет, ответил А. С. Пушкин.' 
re1 = re.compile("""
    (?:
        (?:
            (?<!\\d(?:р|г|к))
            (?<!и\\.т\\.(?:д|п))
            (?<!и(?=\\.т\\.(?:д|п)\\.))
            (?<!и\\.т(?=\\.(?:д|п)\\.))
            (?<!руб|коп)
        \\.) |
        [!?\\n]
    )+
    """, re.X)
 
#print("\n- - - - -\n".join(safeSplit(re1, text)))
print (list(filter((lambda s: len(s)>7), re.split("[.!?\n] +\w", text))))

