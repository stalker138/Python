'''
Created on 23 марта 2016 г.

@author: Stalker
'''

class Base():
    def __init__(self):
        print("Base Init!")
        self.i = 0
        self.s = ""

    def f1(self):
        print("Call f1")

    def f2(self):
        # f1()            Так не работает!!!
        self.f1()

    def df(self, p1, p2='Base'):
        print("Call df!", p1, p2)

class D1(Base):
    def __init__(self):
        Base.__init__(self)
        print("D1 Init!")

    def df(self, p1, p2='D1'):
        print("Call df!", p1, p2)

class D2(Base):
    def __init__(self):
        Base.__init__(self)
        print("D2 Init!")

    def df(self, p1):
        print("D2 Call df!", p1)

class D3(Base):
    def __init__(self):
        Base.__init__(self)
        print("D3 Init!")

c = eval("Base()")
d1 = D1()
d2 = D2()
d3 = D3()
d3.df("d3 Call!")
d2.df("d2 Call!")
d1.df("d1 Call!")
pass
