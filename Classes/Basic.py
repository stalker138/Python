'''
Created on 23 марта 2016 г.

@author: Stalker
'''

class Class():
    def init(self):
        self.i = 0
        self.s = ""

    def f1(self):
        print("Call f1")

    def f2(self):
        # f1()            Так не работает!!!
        self.f2()

c = eval("Class()")
pass
