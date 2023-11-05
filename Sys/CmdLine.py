'''
Created on 31 марта 2016 г.

@author: Alex
'''

import sys
import time

from getopt import *
from optparse import *
import argparse

def test(a1, a2):
    print(a1+a2)

#opts, args = getopt(sys.argv[1:], "ho:v", ["help", "output="])
print("argv = " + str(sys.argv))
input("Hello!")

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-w",
                  action="store_false", dest="verbose",
                  help="don't print status messages to stdout")
(options, args) = parser.parse_args()
print(options, args)

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("-w",
                  action="store_false", dest="verbose")
args = parser.parse_args()
print(args)

input("By!")
time.sleep(10)
