'''
Created on 26 июл. 2018 г.

@author: Stalker

Конфигурация фреймов и сеток
'''

import tkinter as tk
from tkinter import ttk

class MyButton():
    def __init__(self, root, text):
        self.but = tk.Button(root, text=text)
        self.but.bind("<Button-1>",self.printer)
        self.but.pack()
    def printer(self,event):
        print ("Как всегда очередной 'Hello World!'")

root = tk.Tk()

fr1 = tk.Frame(root,width=1500,height=100,bg="darkred", bd=20)  # bd обязателен

class Frame2():
    def __init__(self, root):
        fr = tk.Frame(root,width=300,height=200,bg="green", bd=20)    # Именно он определяет видимые размеры
        fr.grid(row=0, column=1, sticky="nswe")

        fr.columnconfigure(0, pad=20)
        fr.rowconfigure(0, pad=10)

        tk.Label(fr, text="Short", background="lightcyan", width="15", anchor="w", padx="7").grid(sticky="w", padx=17)
        ttk.Label(fr, text="Long Label", style="TLabel").grid(row=1, sticky="w", padx="20", ipadx=15)

        self.dvar = tk.DoubleVar()
        self.svar = tk.StringVar()
        tk.Entry(fr, width=10, bd=3, relief=tk.RAISED, justify=tk.RIGHT, textvariable=self.dvar, state=tk.DISABLED).grid(row=0, column=1)
        tk.Entry(fr, width=10, bd=3, relief=tk.SUNKEN, justify=tk.RIGHT, textvariable=self.svar, state=tk.DISABLED).grid(row=1, column=1)

        self.list = tk.Listbox(fr, height=5, width=15, selectmode=tk.SINGLE)
        self.list.grid(row=2, column=0)
        list2=[u"Канберра",u"Сидней",u"Мельбурн",u"Аделаида"]
        for l in list2:
            self.list.insert(tk.END, l)

        but = tk.Button(fr, text="Button 2")

fr2 = Frame2(root)
fr3 = tk.Frame(root,width=500,height=150,bg="darkblue", bd=5)

fr1.grid(row=0, column=0, sticky="nswe")
fr3.grid(row=0, column=2, sticky="nswe")

top = tk.Toplevel(root,relief=tk.SUNKEN,bd=10,bg="lightblue")
top.title("Дочернее окно")
top.minsize(width=400,height=200)

tabs = ttk.Notebook(top)  
tab1 = ttk.Frame(tabs)  
tab2 = ttk.Frame(tabs)  
tabs.add(tab1, text='Первая')  
tabs.add(tab2, text='Вторая')  
tabs.pack(expand=1, fill='both')  

#but0 = MyButton(root, "Button 0")
but1 = MyButton(fr1, text="Button 1")
but3 = MyButton(fr3, text="Button 3")

def testf(event=None):
    print("Test")
butw = tk.Button(top, text="Button 4", command=testf)
#butw.pack()

listbox1=tk.Listbox(fr1,height=5,width=15,selectmode=tk.EXTENDED)
list1=[u"Москва",u"Санкт-Петербург",u"Саратов",u"Омск"]
for i in list1:
    listbox1.insert(tk.END,i)
listbox1.pack()

val = tk.DoubleVar()
val.set(1000)
ent = tk.Entry(fr1, textvariable=val, justify="right")
ent.pack()

var1=tk.IntVar()
var2=tk.IntVar()
check1=tk.Checkbutton(fr1,text='1 пункт',variable=var1,onvalue=1,offvalue=0)
check2=tk.Checkbutton(fr1,text='2 пункт',variable=var2,onvalue=1,offvalue=0)
check1.pack()
check2.pack()

style = ttk.Style()
data = {}                                                                      
style.configure("TFrame", foreground="black", background="lightgray")
style.configure("TLabel", background="lightgray", width="20", anchor="w", padx="20")

root.attributes('-topmost', True)
root.mainloop()