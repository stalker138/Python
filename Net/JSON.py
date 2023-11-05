'''
Created on 11 июл. 2018 г.

@author: Stalker
'''

import json

s = '{"test":[1,2,3]}'
js = json.loads(s)

f = open("json.txt", "rt")
js = json.load(f)
pass