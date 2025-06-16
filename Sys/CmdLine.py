'''
Created on 31 марта 2016 г.

@author: Alex
'''

import sys
import time

from getopt import getopt, GetoptError
from optparse import OptionParser
from argparse import ArgumentParser

def test(a1, a2):
    print(a1+a2)

# использование sys - наиболее простой способ
print("argv = " + str(sys.argv))

def ugetopt():
    input("Hello, getopt!")
    # C-style command line options. Совершенно ничего непонятно
    # Почему-то завершается после отображения строки с примером использования
    try:
        opts, args = getopt(sys.argv[1:], "ho:v", ["help", "output="])
        print(opts, args)
    except GetoptError as err:
        # print help information and exit:
        print("Wrong args:", err)  # will print something like "option -a not recognized"
        sys.exit(2)

def uargparser():
    input("Hello, ArgumentParser!")
    # Более эффективный с точки зрения кода, но также совершенно непонятный, способ 
    # По крайней мере не завершается после отображения строки с примером использования
    parser = ArgumentParser(description='Process some integers.')
    parser.add_argument("-w", action="store_false", dest="verbose")
    args = parser.parse_args()
    print(args)

def uoptparser():
    input("Hello, OptionParser!")
    # Какой-то альтернативный более изощренный способ.
    # Также совершенно непонятный 
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                      help="write report to FILE", metavar="FILE")
    parser.add_option("-w",
                      action="store_false", dest="verbose",
                      help="don't print status messages to stdout")
    (options, args) = parser.parse_args()
    print(options, args)

#ugetopt()
uargparser()
uoptparser()

input("By!")
time.sleep(10)
