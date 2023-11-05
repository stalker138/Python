'''
Created on 07 апр. 2016 г.

@author: Alex
'''

import os
from pathlib import Path

PATH = "e:/btc/data/"

def context():
    # Работа с контекстом: finally: fin.close() не требуется
    # conextlib.nested(...) почему-то не работает, но "," прекрасно справляется
    try:
        with open("Input.txt") as fin, open("Output.txt", "w") as fout:
            for line in fin:
                print(line.rstrip())
                fout.write(line)
    except OSError as err:
        print(err) 

    data = open("Input.txt", "rt", encoding='IBM866').read()

def files():
    p = Path(PATH+"huobi/")
    fl = [x for x in p.iterdir() if x.is_file()]
    print(fl)

    fl = list(p.glob("**/*.zip"))
    for f in fl:
        print(f, f.name, f.parts)

os.replace("d:/test", "d:/test.test")       # Нельзя перемещать на другой диск!!!

files()
pass